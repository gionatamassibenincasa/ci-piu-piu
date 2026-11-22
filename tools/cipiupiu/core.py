"""Nucleo condiviso ci-più-più: frontmatter, Jinja, include, strip author blocks."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise SystemExit("Dipendenza mancante: pip install pyyaml") from e

try:
    from jinja2 import Environment, BaseLoader, StrictUndefined
except ImportError as e:  # pragma: no cover
    raise SystemExit("Dipendenza mancante: pip install jinja2") from e

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHAPTERS = ROOT / "chapters"
DEFAULT_SCHEMA = ROOT / "schemas" / "chapter-frontmatter.schema.json"

REQUIRED_FM = ("activity_id", "title", "methodology", "order")
METHODOLOGIES = frozenset({"PRIMM", "lab", "guide", "convention"})
ACTIONS = frozenset({"create", "reference"})
PHASES = frozenset({"predict", "run", "investigate", "modify", "make"})


@dataclass
class Chapter:
    path: Path
    meta: dict[str, Any] = field(default_factory=dict)
    body: str = ""

    @property
    def order(self) -> int | None:
        o = self.meta.get("order")
        return o if isinstance(o, int) else None

    @property
    def activity_id(self) -> str:
        return str(self.meta.get("activity_id") or self.path.stem)

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.path.stem)

    @property
    def methodology(self) -> str:
        return str(self.meta.get("methodology") or "")


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """(metadata, body). Senza frontmatter → ({}, text)."""
    raw = text.lstrip("\ufeff")
    if not raw.startswith("---"):
        stripped = raw.lstrip()
        if not stripped.startswith("---"):
            return {}, text
        raw = stripped
    rest = raw[3:]
    if rest.startswith("\n"):
        rest = rest[1:]
    end = rest.find("\n---")
    if end == -1:
        return {}, text
    yaml_text = rest[:end]
    body = rest[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    try:
        meta = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError:
        raise
    if not isinstance(meta, dict):
        meta = {}
    return meta, body


def load_chapter(path: Path) -> Chapter:
    text = path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)
    return Chapter(path=path.resolve(), meta=meta, body=body)


def strip_author_blocks(body: str) -> str:
    """Rimuove blocchi <!--# ... #--> (anche monolinea)."""
    lines = body.splitlines(keepends=True)
    out: list[str] = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.lstrip().startswith("<!--#"):
            while idx < len(lines) and "#-->" not in lines[idx]:
                idx += 1
            idx += 1
            continue
        out.append(line)
        idx += 1
    return "".join(out)



def normalize_quiz_items(pq: dict[str, Any] | None) -> list[dict[str, Any]]:
    """Lista di {question, code?, options} da un blocco quiz (items[] o legacy)."""

    """Lista di {question, code?, options} da predict_quiz (items[] o legacy)."""
    if not pq:
        return []
    shared_code = pq.get("code")
    items = pq.get("items")
    if isinstance(items, list) and items:
        out: list[dict[str, Any]] = []
        for it in items:
            if not isinstance(it, dict):
                continue
            entry = {
                "question": it.get("question") or "",
                "options": list(it.get("options") or []),
            }
            code = it.get("code", shared_code)
            if code:
                entry["code"] = code
            out.append(entry)
        return out
    if pq.get("question") and pq.get("options"):
        entry = {
            "question": pq.get("question") or "",
            "options": list(pq.get("options") or []),
        }
        if shared_code:
            entry["code"] = shared_code
        return [entry]
    return []


def normalize_predict_items(pq: dict[str, Any] | None) -> list[dict[str, Any]]:
    return normalize_quiz_items(pq)


def _make_jinja_env(meta: dict[str, Any]) -> Environment:
    env = Environment(
        loader=BaseLoader(),
        variable_start_string="[[",
        variable_end_string="]]",
        block_start_string="[%",
        block_end_string="%]",
        comment_start_string="[#",
        comment_end_string="#]",
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
    )

    def _format_quiz_block(pq: dict | None, label: str = "Domanda") -> str:
        items = normalize_quiz_items(pq if isinstance(pq, dict) else None)
        if not items:
            return f"<!-- nessun quiz {label} -->"
        codes = [it.get("code") for it in items if it.get("code")]
        shared = codes[0] if codes and len(set(codes)) == 1 else None
        blocks: list[str] = []
        if shared:
            blocks.append("\n".join(["```cpp", str(shared).rstrip(), "```"]))
        for idx, item in enumerate(items, 1):
            lines: list[str] = []
            if len(items) > 1:
                lines.append(f"**{label} {idx}**")
                lines.append("")
            lines.append(str(item.get("question") or "Cosa succede?"))
            lines.append("")
            code = item.get("code")
            if code and code != shared:
                lines.extend(["```cpp", str(code).rstrip(), "```", ""])
            for opt in item.get("options") or []:
                mark = "X" if opt.get("correct") else " "
                lines.append(f"[({mark})] {opt.get('text', '')}")
            blocks.append("\n".join(lines))
        return "\n\n".join(blocks)

    def predict_block() -> str:
        components = meta.get("components") or {}
        return _format_quiz_block(components.get("predict_quiz"), "Domanda")

    def investigate_block() -> str:
        components = meta.get("components") or {}
        return _format_quiz_block(components.get("investigate_quiz"), "Domanda")

    def modify_block() -> str:
        components = meta.get("components") or {}
        return _format_quiz_block(components.get("modify_quiz"), "Domanda")

    env.globals["predict_block"] = predict_block
    env.globals["investigate_block"] = investigate_block
    env.globals["modify_block"] = modify_block
    return env


def render_jinja(body: str, meta: dict[str, Any]) -> str:
    if "[[" not in body and "[%" not in body:
        return body
    env = _make_jinja_env(meta)
    ctx = dict(meta)
    ctx.setdefault("components", {})
    ctx.setdefault("files", [])
    return env.from_string(body).render(**ctx)


def expand_includes(text: str, base_dir: Path, visited: set[Path] | None = None) -> str:
    """Espande #include <rel> fuori dai fence ```; ricorsivo."""
    if visited is None:
        visited = set()
    result: list[str] = []
    in_code = False
    for line in text.splitlines(keepends=True):
        if line.strip().startswith("```"):
            in_code = not in_code
            result.append(line)
            continue
        m = re.match(r"^\s*#include\s*<(.+?)>\s*$", line) if not in_code else None
        if not m:
            result.append(line)
            continue
        inc = m.group(1)
        target = (base_dir / inc).resolve()
        if not target.is_file() and Path(str(target) + ".md").is_file():
            target = Path(str(target) + ".md")
        if not target.is_file():
            result.append(f"<!-- ERRORE: File non trovato '{inc}' -->\n")
            continue
        if target in visited:
            result.append(f"<!-- ERRORE: Inclusione circolare '{inc}' -->\n")
            continue
        visited.add(target)
        ch = load_chapter(target)
        # include: pipeline completa sul figlio (senza re-includere se non richiesto)
        child = strip_author_blocks(ch.body)
        child = render_jinja(child, ch.meta)
        child = expand_includes(child, target.parent, visited)
        result.append(child)
        if child and not child.endswith("\n"):
            result.append("\n")
    return "".join(result)


def render_file(path: Path, *, expand: bool = True) -> str:
    """
    Pipeline unica:
    frontmatter separato → strip author → Jinja → (opz.) include.
    Il frontmatter non compare nell'output.
    """
    path = path.resolve()
    ch = load_chapter(path)
    body = strip_author_blocks(ch.body)
    body = render_jinja(body, ch.meta)
    if expand:
        body = expand_includes(body, path.parent, visited={path})
    return body


def iter_chapters(chapters_dir: Path | None = None) -> list[Chapter]:
    """Capitoli con frontmatter, ordinati per order (poi nome file)."""
    d = chapters_dir or DEFAULT_CHAPTERS
    chapters: list[Chapter] = []
    for path in sorted(d.glob("*.md")):
        ch = load_chapter(path)
        if not ch.meta:
            continue
        chapters.append(ch)
    chapters.sort(key=lambda c: (c.order if c.order is not None else 10**9, c.path.name))
    return chapters


def validate_chapter(path: Path, schema: dict | None = None) -> list[str]:
    """Errori di validazione; lista vuota = ok."""
    errors: list[str] = []
    try:
        ch = load_chapter(path)
    except yaml.YAMLError as exc:
        return [f"{path.name}: YAML non valido: {exc}"]

    if not ch.meta:
        return [f"{path.name}: manca il frontmatter YAML (--- ... ---)"]

    if schema is not None:
        try:
            from jsonschema import Draft7Validator
        except ImportError:
            schema = None
        else:
            for err in sorted(Draft7Validator(schema).iter_errors(ch.meta), key=lambda e: list(e.path)):
                loc = ".".join(str(p) for p in err.path) or "(root)"
                errors.append(f"{path.name}: {loc}: {err.message}")

    meta = ch.meta
    for key in REQUIRED_FM:
        if key not in meta:
            errors.append(f"{path.name}: manca campo required '{key}'")

    if "methodology" in meta and meta["methodology"] not in METHODOLOGIES:
        errors.append(f"{path.name}: methodology non valida: {meta.get('methodology')!r}")

    if "order" in meta and (not isinstance(meta["order"], int) or meta["order"] < 0):
        errors.append(f"{path.name}: order deve essere intero >= 0")

    components = meta.get("components") or {}
    for qkey in ("predict_quiz", "investigate_quiz", "modify_quiz"):
        if qkey not in components:
            continue
        pq = components[qkey] or {}
        items = normalize_quiz_items(pq if isinstance(pq, dict) else None)
        if not items:
            errors.append(
                f"{path.name}: {qkey}: serve question+options oppure items[] non vuoto"
            )
        for j, item in enumerate(items):
            opts = item.get("options") or []
            if not any(isinstance(o, dict) and o.get("correct") for o in opts):
                errors.append(
                    f"{path.name}: {qkey} item[{j}]: nessuna option con correct=true"
                )
    
    create_paths: set[str] = set()
    for i, item in enumerate(meta.get("files") or []):
        if not isinstance(item, dict):
            errors.append(f"{path.name}: files[{i}] non è un oggetto")
            continue
        if "path" not in item or "action" not in item:
            errors.append(f"{path.name}: files[{i}] richiede path e action")
            continue
        if item["action"] not in ACTIONS:
            errors.append(f"{path.name}: files[{i}].action non valido")
        phase = item.get("phase")
        if phase is not None and phase not in PHASES:
            errors.append(f"{path.name}: files[{i}].phase non valido")
        if item.get("action") == "create":
            path_f = item.get("path")
            if path_f in create_paths:
                errors.append(f"{path.name}: files[{i}].path duplicato: {path_f}")
            create_paths.add(str(path_f))
            tf, tc = item.get("template_from"), item.get("template_content")
            has_from = bool(tf)
            has_content = tc is not None and str(tc) != ""
            if has_from == has_content:
                errors.append(
                    f"{path.name}: files[{i}] action=create richiede esattamente uno tra "
                    "template_from e template_content"
                )
            if has_from and not (ROOT / str(tf)).is_file():
                errors.append(f"{path.name}: files[{i}].template_from non trovato: {tf}")


    # ——— Lint corpo Markdown (minimo) ———
    body = ch.body

    if meta.get("methodology") == "PRIMM":
        # Heading Predict (accetta #### 1. PREDICT o ### 1. Predict)
        if not re.search(
            r"^#{2,4}\s*(?:\d+\.\s*)?PREDICT\b",
            body,
            re.M | re.I,
        ):
            errors.append(
                f"{path.name}: methodology PRIMM richiede un heading '1. PREDICT' nel corpo"
            )
        # Single source Predict = components + macro
        pq = components.get("predict_quiz")
        if not pq:
            errors.append(
                f"{path.name}: methodology PRIMM richiede components.predict_quiz "
                "(unica fonte del quiz Predict)"
            )
        if "[[ predict_block() ]]" not in body and "[[predict_block()]]" not in body:
            errors.append(
                f"{path.name}: methodology PRIMM richiede [[ predict_block() ]] nel corpo "
                "(macro generata da components.predict_quiz)"
            )
        # Evita quiz Predict duplicati a mano (opzioni LiaScript fuori dalla macro)
        # Solo warning soft se molte opzioni e nessuna macro - già coperta sopra

    # dedupe preservando ordine
    return list(dict.fromkeys(errors))



def load_schema(path: Path | None = None) -> dict | None:
    p = path or DEFAULT_SCHEMA
    if not p.is_file():
        return None
    import json

    return json.loads(p.read_text(encoding="utf-8"))


# ——— Slice B: build course / lessons ———

DEFAULT_COURSE_YAML = ROOT / "course.yaml"
DEFAULT_DIST = ROOT / "dist"
DEFAULT_INDEX = ROOT / "index.md"

DEFAULT_LIASCRIPT_META: dict[str, Any] = {
    "author": "Gionata Massi",
    "email": "gionata.massi@savoiabenicasa.it",
    "version": "2026-11-12",
    "language": "it",
    "narrator": "IT Italian Male",
    "comment": (
        "Appunti delle lezioni di Informatica - Classi terze ITE SIA - "
        "Anno Scolastico 26/27"
    ),
    "import": [
        "https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md",
        "https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md",
        "https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md",
    ],
}


def load_course_config(path: Path | None = None) -> dict[str, Any]:
    """Carica course.yaml se presente; altrimenti default minimi."""
    p = path or DEFAULT_COURSE_YAML
    cfg: dict[str, Any] = {
        "chapters_dir": "chapters",
        "index": "index.md",
        "out_dir": "dist",
        "course_out": "dist/README.md",
        "lessons_dir": "dist/lessons",
        "liascript": dict(DEFAULT_LIASCRIPT_META),
        "urls": {
            "mode": "prod",
            "lessons_prod": (
                "https://raw.githubusercontent.com/gionatamassibenincasa/"
                "ci-piu-piu/main/dist/lessons/"
            ),
            "lessons_dev": "./",
            "course_prod": (
                "https://raw.githubusercontent.com/gionatamassibenincasa/"
                "ci-piu-piu/main/dist/README.md"
            ),
            "course_dev": "../README.md",
        },
    }
    if p.is_file():
        data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        if not isinstance(data, dict):
            return cfg
        for key in ("chapters_dir", "index", "out_dir", "course_out", "lessons_dir"):
            if key in data:
                cfg[key] = data[key]
        if isinstance(data.get("liascript"), dict):
            cfg["liascript"] = {**cfg["liascript"], **data["liascript"]}
        if isinstance(data.get("urls"), dict):
            cfg["urls"] = {**cfg["urls"], **data["urls"]}
    return cfg


def merge_liascript_meta(
    global_meta: dict[str, Any], chapter_meta: dict[str, Any]
) -> dict[str, Any]:
    """Scalari: capitolo vince. import: unione ordinata senza duplicati."""
    out = dict(global_meta)
    for key, val in chapter_meta.items():
        if key in {"components", "files", "activity_id", "title", "methodology", "order"}:
            continue
        if key == "import":
            continue
        if val is not None and key in {
            "author",
            "email",
            "language",
            "narrator",
            "comment",
            "version",
            "translateWithGoogle",
        }:
            out[key] = val
    imports: list[str] = []
    for src in (global_meta.get("import") or [], chapter_meta.get("import") or []):
        if isinstance(src, str):
            src = [src]
        for u in src:
            if u and u not in imports:
                imports.append(u)
    out["import"] = imports
    return out


def format_liascript_header(meta: dict[str, Any]) -> str:
    """Commento HTML in testa richiesto dal player LiaScript (solo lezioni)."""
    lines = ["<!--"]
    keys = ("author", "email", "version", "language", "narrator", "comment", "translateWithGoogle")
    width = max(len(k) for k in keys + ("import",))
    for key in keys:
        if not meta.get(key):
            continue
        val = str(meta[key]).strip()
        pad = " " * (width - len(key) + 2)
        lines.append(f"{key}:{pad}{val}")
    for url in meta.get("import") or []:
        pad = " " * (width - len("import") + 2)
        lines.append(f"import:{pad}{url}")
    lines.append("-->")
    lines.append("")
    return "\n".join(lines)



def lesson_filename(chapter: Chapter) -> str:
    order = chapter.order if chapter.order is not None else 0
    return f"{order:02d}_{chapter.activity_id}.md"


def is_stale(targets: list[Path], sources: list[Path]) -> bool:
    """True se bisogna rigenerare (manca target o source più recente)."""
    if not targets:
        return True
    for t in targets:
        if not t.is_file():
            return True
    try:
        newest_src = max(s.stat().st_mtime for s in sources if s.is_file())
    except ValueError:
        return True
    oldest_tgt = min(t.stat().st_mtime for t in targets)
    return newest_src > oldest_tgt


def build_course(
    *,
    index_path: Path | None = None,
    out_path: Path | None = None,
    force: bool = False,
) -> tuple[Path, bool]:
    """
    Corso completo: render di index.md (include + Jinja).
    Non aggiunge commento HTML LiaScript (resta quello già in index.md).
    Ritorna (path_output, written).
    """
    index_path = (index_path or DEFAULT_INDEX).resolve()
    out_path = (out_path or (DEFAULT_DIST / "README.md")).resolve()
    sources = [index_path]
    # include grezzi come dipendenze timestamp
    text = index_path.read_text(encoding="utf-8")
    for m in re.finditer(r"^\s*#include\s*<(.+?)>\s*$", text, re.M):
        inc = index_path.parent / m.group(1)
        if inc.is_file():
            sources.append(inc.resolve())
        elif Path(str(inc) + ".md").is_file():
            sources.append(Path(str(inc) + ".md").resolve())

    if not force and not is_stale([out_path], sources):
        return out_path, False

    rendered = render_file(index_path, expand=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(rendered, encoding="utf-8")
    return out_path, True



def liascript_viewer_url(resource_url: str) -> str:
    """Avvolge un URL raw in liascript.github.io/course/? per apertura online."""
    if not resource_url:
        return resource_url
    if resource_url.startswith("https://liascript.github.io/"):
        return resource_url
    if resource_url.startswith("http://") or resource_url.startswith("https://"):
        return f"https://liascript.github.io/course/?{resource_url}"
    return resource_url


def build_lessons_index(
    chapters: list[Chapter],
    *,
    lessons_dir: Path,
    base: str,
    course_link: str,
    global_meta: dict[str, Any],
    mode: str,
    force: bool,
) -> tuple[Path, bool]:
    """Catalogo dist/lessons/index.md con link apribili in LiaScript."""
    out = lessons_dir / "index.md"
    sources = [ch.path for ch in chapters if ch.path.is_file()]
    if DEFAULT_COURSE_YAML.is_file():
        sources.append(DEFAULT_COURSE_YAML)
    if not force and sources and not is_stale([out], sources):
        return out, False

    comment = str(global_meta.get("comment") or "").strip()
    if "Catalogo lezioni" not in comment:
        suffix = "Catalogo lezioni autonome"
        comment = f"{comment} — {suffix}" if comment else suffix

    header = format_liascript_header({**global_meta, "comment": comment})

    def lesson_href(filename: str) -> str:
        raw = f"{base}{filename}"
        return raw if mode == "dev" else liascript_viewer_url(raw)

    course_href = (
        course_link if mode == "dev" else liascript_viewer_url(course_link)
    )

    lines = [
        header.rstrip(),
        "",
        "# Catalogo lezioni — C++ 3ª SIA",
        "",
        f"Apri il [corso completo]({course_href}) in un unico file, "
        "oppure una lezione alla volta dalla tabella.",
        "",
        "| # | Lezione | Metodo | Apri |",
        "|---:|---------|--------|------|",
    ]
    for ch in chapters:
        fn = lesson_filename(ch)
        href = lesson_href(fn)
        title = (ch.title or ch.activity_id).replace("|", r"\|")
        method = ch.methodology or "—"
        order = ch.order if ch.order is not None else "—"
        lines.append(f"| {order} | {title} | `{method}` | [Apri]({href}) |")

    lines.extend(
        [
            "",
            "---",
            "",
            "*Generato da `cipiupiu build lessons`. "
            "Non modificare a mano: sovrascritto al prossimo build.*",
            "",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")
    return out, True


def build_lessons(
    *,
    chapters_dir: Path | None = None,
    lessons_dir: Path | None = None,
    course_cfg: dict[str, Any] | None = None,
    mode: str | None = None,
    force: bool = False,
    only: str | None = None,
) -> list[tuple[Path, bool]]:
    """
    Una lezione per capitolo con frontmatter.
    Aggiunge commento HTML LiaScript + nav prev/next.
    expand_includes=False (lezione autonoma).
    """
    cfg = course_cfg or load_course_config()
    chapters_dir = Path(chapters_dir or cfg.get("chapters_dir") or DEFAULT_CHAPTERS)
    if not chapters_dir.is_absolute():
        chapters_dir = (ROOT / chapters_dir).resolve()
    lessons_dir = Path(lessons_dir or cfg.get("lessons_dir") or (DEFAULT_DIST / "lessons"))
    if not lessons_dir.is_absolute():
        lessons_dir = (ROOT / lessons_dir).resolve()
    lessons_dir.mkdir(parents=True, exist_ok=True)

    urls = cfg.get("urls") or {}
    mode = mode or urls.get("mode") or "prod"
    if mode == "dev":
        base = urls.get("lessons_dev") or "./"
        course_link = urls.get("course_dev") or "../README.md"
    else:
        base = urls.get("lessons_prod") or "./"
        course_link = urls.get("course_prod") or "../README.md"
    if base and not base.endswith("/") and not base.endswith("./"):
        # raw github directory should end with /
        if base.startswith("http"):
            base = base + "/"

    chapters = [c for c in iter_chapters(chapters_dir) if c.meta]
    results: list[tuple[Path, bool]] = []
    global_meta = cfg.get("liascript") or DEFAULT_LIASCRIPT_META

    for i, ch in enumerate(chapters):
        if only and not (
            only in ch.activity_id or only == str(ch.order) or only in ch.path.name
        ):
            continue
        out = lessons_dir / lesson_filename(ch)
        sources = [ch.path]
        if not force and not is_stale([out], sources):
            results.append((out, False))
            continue

        body = render_file(ch.path, expand=False)
        header_meta = merge_liascript_meta(global_meta, ch.meta)
        header = format_liascript_header(header_meta)

        prev_c = chapters[i - 1] if i > 0 else None
        next_c = chapters[i + 1] if i + 1 < len(chapters) else None
        prev_raw = f"{base}{lesson_filename(prev_c)}" if prev_c else None
        next_raw = f"{base}{lesson_filename(next_c)}" if next_c else None

        def _href(raw: str | None) -> str | None:
            if not raw:
                return None
            return raw if mode == "dev" else liascript_viewer_url(raw)

        prev_link = _href(prev_raw)
        next_link = _href(next_raw)
        index_raw = f"{base}index.md"
        index_link = _href(index_raw) or index_raw

        nav_parts: list[str] = []
        if prev_link:
            nav_parts.append(f"[← Prec.]({prev_link})")
        else:
            nav_parts.append("← Prec.")
        nav_parts.append(f"[Indice]({index_link})")
        nav_parts.append(f"[Corso]({course_link})")
        if next_link:
            nav_parts.append(f"[Succ. →]({next_link})")
        else:
            nav_parts.append("Succ. →")
        nav = " · ".join(nav_parts)

        # Ultima slide LiaScript (#) con link espliciti href a indice / prec / succ
        footer_lines = [
            "",
            "---",
            "",
            "# Navigazione",
            "",
            "Continua da qui:",
            "",
            f'- <a href="{index_link}">Indice delle lezioni</a>',
        ]
        if prev_link and prev_c is not None:
            prev_ord = prev_c.order if prev_c.order is not None else "?"
            prev_title = (prev_c.title or prev_c.activity_id).replace('"', "'")
            footer_lines.append(
                f'- <a href="{prev_link}">Lezione precedente ' 
                f"({prev_ord} — {prev_title})</a>"
            )
        else:
            footer_lines.append("- Lezione precedente: — (sei all'inizio)")
        if next_link and next_c is not None:
            next_ord = next_c.order if next_c.order is not None else "?"
            next_title = (next_c.title or next_c.activity_id).replace('"', "'")
            footer_lines.append(
                f'- <a href="{next_link}">Lezione successiva ' 
                f"({next_ord} — {next_title})</a>"
            )
        else:
            footer_lines.append("- Lezione successiva: — (sei alla fine)")
        footer_lines.append("")
        footer = "\n".join(footer_lines)

        content = f"{header}{nav}\n\n---\n\n{body.rstrip()}\n{footer}"
        if not content.endswith("\n"):
            content += "\n"
        out.write_text(content, encoding="utf-8")
        results.append((out, True))

    # Catalogo lezioni (sempre considerato; skip se up-to-date e non --force)
    if not only:
        index_path, index_written = build_lessons_index(
            chapters,
            lessons_dir=lessons_dir,
            base=base,
            course_link=course_link,
            global_meta=global_meta,
            mode=mode,
            force=force,
        )
        results.append((index_path, index_written))

    return results
