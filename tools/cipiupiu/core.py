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

    def predict_block() -> str:
        components = meta.get("components") or {}
        pq = components.get("predict_quiz")
        if not pq:
            return "<!-- predict_block: nessun components.predict_quiz -->"
        lines: list[str] = [str(pq.get("question") or "Cosa succede?"), ""]
        code = pq.get("code")
        if code:
            lines.extend(["```cpp", str(code).rstrip(), "```", ""])
        for opt in pq.get("options") or []:
            mark = "X" if opt.get("correct") else " "
            lines.append(f"[({mark})] {opt.get('text', '')}")
        return "\n".join(lines)

    env.globals["predict_block"] = predict_block
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
    if "predict_quiz" in components:
        pq = components["predict_quiz"] or {}
        opts = pq.get("options") or []
        if opts and not any(isinstance(o, dict) and o.get("correct") for o in opts):
            errors.append(f"{path.name}: predict_quiz: nessuna option con correct=true")

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

    # dedupe preservando ordine
    return list(dict.fromkeys(errors))


def load_schema(path: Path | None = None) -> dict | None:
    p = path or DEFAULT_SCHEMA
    if not p.is_file():
        return None
    import json

    return json.loads(p.read_text(encoding="utf-8"))
