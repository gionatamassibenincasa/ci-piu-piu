"""Export tipografico degli esercizi PRIMM dal frontmatter validato."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from . import core
from .core import normalize_predict_items, shuffle_quiz_options


FIELD_PATHS = {
    "activity_id": ("activity_id",),
    "chapter_order": ("order",),
    "chapter_title": ("title",),
    "predict_question": ("components", "predict_quiz", "question"),
    "predict_code": ("components", "predict_quiz", "code"),
    "predict_options": ("components", "predict_quiz", "options"),
    "predict_option_text": ("components", "predict_quiz", "options", "*", "text"),
    "predict_option_correct": ("components", "predict_quiz", "options", "*", "correct"),
    "modify_instructions": ("components", "modify_instructions"),
    "make_instructions": ("components", "make_instructions"),
    "investigate_questions": ("components", "investigate_questions"),
    "files": ("files",),
    "file_path": ("files", "*", "path"),
    "file_action": ("files", "*", "action"),
    "file_phase": ("files", "*", "phase"),
    "file_description": ("files", "*", "description"),
    "file_template_content": ("files", "*", "template_content"),
    "file_validation_rules": ("files", "*", "validation_rules"),
    # Paper Pack / registro elettronico
    "registro": ("registro",),
    "registro_argomenti": ("registro", "argomenti"),
    "registro_note": ("registro", "note"),
    "assessment": ("assessment",),
    "assessment_duration": ("assessment", "duration_min"),
    "assessment_total_points": ("assessment", "total_points"),
    "assessment_versions": ("assessment", "versions"),
    "assessment_predict": ("assessment", "predict"),
    "assessment_investigate": ("assessment", "investigate"),
    "assessment_modify": ("assessment", "modify"),
    "assessment_make": ("assessment", "make"),
}

PRINTABLE_PHASES = ("predict", "modify", "make")
PAPER_PHASES = ("predict", "investigate", "modify", "make")
_PHASE_LABEL = {
    "predict": "Predict",
    "investigate": "Investigate",
    "modify": "Modify",
    "make": "Make",
}
_STYLE_IMPORT = "stile_compito.typ"  # copiato in outdir da _ensure_style


def _get(model: Any, path: tuple[str, ...]) -> Any:
    if not path:
        return model
    key, *rest = path
    if key == "*":
        if not isinstance(model, list):
            return None
        return [_get(item, tuple(rest)) for item in model]
    if not isinstance(model, dict) or key not in model:
        return None
    return _get(model[key], tuple(rest))


def _field(meta: dict[str, Any], name: str) -> Any:
    return _get(meta, FIELD_PATHS[name])


def _chapter_path(identifier: str) -> Path:
    supplied = Path(identifier)
    if supplied.is_file():
        return supplied

    order = int(identifier) if identifier.isdigit() else None
    matches = [
        chapter.path
        for chapter in core.iter_chapters()
        if chapter.activity_id == identifier
        or chapter.order == order
        or chapter.path.stem == identifier
    ]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise ValueError(f"Capitolo non trovato: {identifier}")
    raise ValueError(f"Identificatore capitolo ambiguo: {identifier}")


def _validated_chapter(identifier: str) -> core.Chapter:
    path = _chapter_path(identifier)
    errors = core.validate_chapter(path, core.load_schema())
    if errors:
        raise ValueError("Frontmatter non valido:\n- " + "\n- ".join(errors))
    return core.load_chapter(path)


def _starter_files(meta: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    files = _field(meta, "files") or []
    paths = _field(meta, "file_path") or []
    actions = _field(meta, "file_action") or []
    phases = _field(meta, "file_phase") or []
    descriptions = _field(meta, "file_description") or []
    contents = _field(meta, "file_template_content") or []
    validations = _field(meta, "file_validation_rules") or []

    result: list[dict[str, Any]] = []
    for index in range(len(files)):
        if actions[index] != "create" or phases[index] != phase:
            continue
        path = str(paths[index])
        content = contents[index]
        result.append(
            {
                "path": path,
                "description": descriptions[index],
                "code": content if Path(path).suffix in {".c", ".cc", ".cpp", ".h", ".hpp"} else None,
                "validation_rules": validations[index],
            }
        )
    return result


def _phase_item(meta: dict[str, Any], phase: str) -> dict[str, Any] | None:
    if phase == "predict":
        components = meta.get("components") or {}
        items = normalize_predict_items(components.get("predict_quiz"))
        if not items:
            return None
        # Un solo item modello legacy; se multipli, prompt concatenato + choices del primo
        # (gli item multipli sono gestiti in build_paper_model).
        first = items[0]
        return {
            "id": f"{_field(meta, 'activity_id')}-predict",
            "phase": phase,
            "prompt": first.get("question") or "",
            "code": first.get("code"),
            "choices": [
                o.get("text") for o in (first.get("options") or []) if o.get("text")
            ],
            "starter_files": [],
            "_predict_items": items,
        }

    if phase == "investigate":
        questions = _field(meta, "investigate_questions") or []
        assess = _field(meta, "assessment_investigate") or {}
        if isinstance(assess, dict) and assess.get("questions"):
            questions = assess["questions"]
        if not questions:
            return None
        prompt = "\n".join(f"{i}. {q}" for i, q in enumerate(questions, 1))
        return {
            "id": f"{_field(meta, 'activity_id')}-investigate",
            "phase": phase,
            "prompt": prompt,
            "code": None,
            "choices": [],
            "starter_files": [],
            "points": assess.get("points") if isinstance(assess, dict) else None,
            "typical_errors": list(assess.get("typical_errors") or [])
            if isinstance(assess, dict)
            else [],
        }

    instructions = _field(meta, f"{phase}_instructions")
    starter_files = _starter_files(meta, phase)
    descriptions = [
        item["description"]
        for item in starter_files
        if item.get("description") and item["description"] != instructions
    ]
    prompt_parts = [text for text in (instructions, *descriptions) if text]
    if not prompt_parts and not starter_files:
        return None
    return {
        "id": f"{_field(meta, 'activity_id')}-{phase}",
        "phase": phase,
        "prompt": "\n\n".join(prompt_parts),
        "code": None,
        "choices": [],
        "starter_files": starter_files,
    }


def build_print_model(chapter_id: str, phases: tuple[str, ...]) -> dict[str, Any]:
    """Costruisce il modello canonico dai soli nodi del frontmatter validato."""
    unknown = set(phases) - set(PRINTABLE_PHASES)
    if unknown:
        raise ValueError(f"Fasi stampabili non valide: {', '.join(sorted(unknown))}")

    chapter = _validated_chapter(chapter_id)
    meta = chapter.meta
    items = [item for phase in phases if (item := _phase_item(meta, phase)) is not None]
    if not items:
        raise ValueError("Il capitolo non contiene esercizi stampabili per le fasi richieste")

    return {
        "format_version": 1,
        "chapter": {
            "order": _field(meta, "chapter_order"),
            "activity_id": _field(meta, "activity_id"),
            "title": _field(meta, "chapter_title"),
        },
        "items": items,
    }



def _stable_item_id(activity_id: str, phase: str, slot: int | None = None) -> str:
    """Id stabile: activity_id/phase[/n]."""
    if slot is None:
        return f"{activity_id}/{phase}"
    return f"{activity_id}/{phase}/{slot}"


def _correct_choices(meta: dict[str, Any]) -> list[str]:
    texts = list(_field(meta, "predict_option_text") or [])
    flags = list(_field(meta, "predict_option_correct") or [])
    return [str(t) for t, f in zip(texts, flags) if t and f]


def _merge_variant(item: dict[str, Any], override: dict[str, Any] | None) -> dict[str, Any]:
    """Applica override di variants.X sulla fase."""
    if not override:
        return dict(item)
    out = dict(item)
    for key in ("prompt", "code", "context", "points"):
        if key in override and override[key] is not None:
            out[key] = override[key]
    if override.get("questions") is not None:
        qs = list(override["questions"])
        out["questions"] = qs
        out["prompt"] = "\n".join(f"{i}. {q}" for i, q in enumerate(qs, 1))
    if override.get("typical_errors") is not None:
        out["typical_errors"] = list(override["typical_errors"])
    if override.get("must_include") is not None:
        out["must_include"] = list(override["must_include"])
    return out


def build_paper_model(chapter_id: str) -> dict[str, Any]:
    """Paper Pack model format_version 2: id stabili, context, items_by_version."""
    chapter = _validated_chapter(chapter_id)
    meta = chapter.meta
    assessment = _field(meta, "assessment") or {}
    if not assessment:
        raise ValueError(
            "Paper Pack richiede il blocco frontmatter `assessment` "
            "(vedi docs/paper_pack.md)"
        )

    activity_id = str(_field(meta, "activity_id"))
    versions = list(assessment.get("versions") or ["A"])
    variants = assessment.get("variants") or {}
    if not isinstance(variants, dict):
        variants = {}

    base_items: list[dict[str, Any]] = []

    pred = assessment.get("predict") or {}
    base_pred = _phase_item(meta, "predict")
    if base_pred:
        items = list(base_pred.pop("_predict_items", None) or [])
        if not items:
            items = [
                {
                    "question": base_pred.get("prompt"),
                    "code": base_pred.get("code"),
                    "options": [
                        {"text": c, "correct": False}
                        for c in (base_pred.get("choices") or [])
                    ],
                }
            ]
        n = max(len(items), 1)
        points_each = pred.get("points")
        if points_each is not None and n > 1:
            # ripartisci i punti in modo uniforme se multi-item
            try:
                points_each = float(points_each) / n
            except (TypeError, ValueError):
                points_each = pred.get("points")
        for j, pit in enumerate(items, 1):
            opts = [o for o in (pit.get("options") or []) if isinstance(o, dict)]
            correct = [str(o.get("text")) for o in opts if o.get("correct") and o.get("text")]
            seed_key = f"{pit.get('question', '')}|{'|'.join(sorted(str(o.get('text', '')) for o in opts))}"
            shuffled = shuffle_quiz_options(opts, seed_key=seed_key)
            choices = [str(o.get("text")) for o in shuffled if o.get("text")]
            base_items.append(
                {
                    "id": pred.get("id")
                    or (
                        _stable_item_id(activity_id, "predict", j)
                        if n > 1
                        else _stable_item_id(activity_id, "predict")
                    ),
                    "phase": "predict",
                    "prompt": pit.get("question") or "",
                    "code": pit.get("code") or base_pred.get("code"),
                    "choices": choices,
                    "starter_files": [],
                    "points": points_each,
                    "typical_errors": list(pred.get("typical_errors") or []),
                    "context": pred.get("context") or "",
                    "correct_choices": correct,
                }
            )

    inv_block = assessment.get("investigate") or {}
    inv = _phase_item(meta, "investigate")
    if inv:
        base_items.append(
            {
                **inv,
                "id": inv_block.get("id") or _stable_item_id(activity_id, "investigate"),
                "context": inv_block.get("context") or inv.get("context") or "",
                "questions": list(inv_block.get("questions") or []),
            }
        )

    for phase in ("modify", "make"):
        block = assessment.get(phase) or {}
        starters = _starter_files(meta, phase)
        prompt = block.get("prompt") or ""
        if not prompt:
            fallback = _phase_item(meta, phase)
            if fallback:
                prompt = fallback["prompt"]
                starters = fallback.get("starter_files") or starters
        if not prompt and not starters:
            continue
        # Se assessment definisce "code" (anche per omettere lo scaffold Classroom), niente starter files sul foglio.
        if "code" in block:
            paper_code = block.get("code") or None
            paper_starters = []
        else:
            paper_code = None
            paper_starters = starters
        base_items.append(
            {
                "id": block.get("id") or _stable_item_id(activity_id, phase),
                "phase": phase,
                "prompt": prompt,
                "code": paper_code,
                "choices": [],
                "starter_files": paper_starters,
                "points": block.get("points"),
                "must_include": list(block.get("must_include") or []),
                "typical_errors": list(block.get("typical_errors") or []),
                "context": block.get("context") or "",
            }
        )

    if not base_items:
        raise ValueError("assessment presente ma nessuna sezione utilizzabile per la verifica")

    items_by_version: dict[str, list[dict[str, Any]]] = {}
    for ver in versions:
        ver_over = variants.get(ver) if isinstance(variants.get(ver), dict) else {}
        items_by_version[ver] = [
            _merge_variant(item, ver_over.get(item["phase"])) for item in base_items
        ]

    return {
        "format_version": 2,
        "kind": "paper",
        "chapter": {
            "order": _field(meta, "chapter_order"),
            "activity_id": activity_id,
            "title": _field(meta, "chapter_title"),
        },
        "assessment": {
            "duration_min": assessment.get("duration_min"),
            "total_points": assessment.get("total_points"),
            "versions": versions,
        },
        "registro": {
            "argomenti": _field(meta, "registro_argomenti"),
            "note": _field(meta, "registro_note"),
        },
        "items": items_by_version[versions[0]],
        "items_by_version": items_by_version,
    }


def _typ_string(value: str | None) -> str:
    """Literal Typst string (JSON-encoded)."""
    return json.dumps(value or "", ensure_ascii=False)


def _typ_text(value: str | None) -> str:
    """Typst content: newline → linebreak(); # → unicode hash."""
    raw = value or ""
    raw = raw.replace("\\", "\\\\")
    raw = raw.replace("#", "\\u{23}")
    raw = raw.replace("[", "\\[").replace("]", "\\]")
    parts = raw.split("\n")
    # A capo forzati così le domande 1) 2) 3) non restano su una riga sola.
    joined = " #linebreak() ".join(parts)
    return "[" + joined + "]"
def render_typst(model: dict[str, Any], template: str) -> str:
    """Adatta il modello canonico worksheet a Typst."""
    chapter = model["chapter"]
    out = [
        f'#import "{_STYLE_IMPORT}": *',
        (
            "#compito-intestazione("
            f"numero: {chapter['order']}, "
            f"titolo: {_typ_string(chapter['title'])}, "
            f"template: {_typ_string(template)})"
        ),
        "",
    ]
    for number, item in enumerate(model["items"], 1):
        out.extend(
            [
                f"= Esercizio {number} — {_PHASE_LABEL[item['phase']]}",
                f"#testo({_typ_text(item['prompt'])})",
                "",
            ]
        )
        if item.get("code"):
            out.extend([f"#codice({_typ_string(item['code'])})", ""])
        for choice in item.get("choices") or []:
            out.append(f"#scelta({_typ_string(choice)})")
        if item.get("choices"):
            out.append("")
        for starter in item.get("starter_files") or []:
            out.append(f"*File di partenza: `{starter['path']}`*")
            if starter.get("code"):
                out.extend(["", f"#codice({_typ_string(starter['code'])})"])
            rules = starter.get("validation_rules") or {}
            requirements: list[str] = []
            if rules.get("min_lines") is not None:
                requirements.append(f"almeno {rules['min_lines']} righe")
            requirements.extend(
                f"contiene `{value}`" for value in rules.get("must_contain", []) or []
            )
            if requirements:
                out.extend(["", "*Requisiti:*"])
                out.extend(f"- {requirement}" for requirement in requirements)
            out.append("")
        out.extend([f'#spazio-risposta(fase: "{item["phase"]}")', ""])
    return "\n".join(out)



def render_paper_student_typst(model: dict[str, Any], version: str) -> str:
    """Foglio studente Paper Pack (una versione)."""
    chapter = model["chapter"]
    assess = model.get("assessment") or {}
    duration = assess.get("duration_min")
    total = assess.get("total_points")
    meta_line = f"Versione {version}"
    if duration:
        meta_line += f" · {duration} min"
    if total is not None:
        meta_line += f" · {total} punti"

    items = (model.get("items_by_version") or {}).get(version) or model.get("items") or []
    modify_hint = (
        "Barra il codice che devi eliminare; scrivi il codice da inserire "
        "nelle righe lasciate libere o sotto il listato."
    )

    out = [
        f'#import "{_STYLE_IMPORT}": *',
        (
            "#compito-intestazione("
            f"numero: {chapter['order']}, "
            f"titolo: {_typ_string(chapter['title'])}, "
            f"template: {_typ_string('paper')})"
        ),
        f"#meta-riga({_typ_text(meta_line)})",
        "",
    ]
    for number, item in enumerate(items, 1):
        pts = item.get("points")
        heading = f"Esercizio {number} — {_PHASE_LABEL[item['phase']]}"
        if pts is not None:
            heading += f" ({pts} pt)"
        out.extend([f"= {heading}", f"#testo({_typ_text(item['prompt'])})", ""])
        if item.get("code"):
            out.extend([f"#codice({_typ_string(item['code'])})", ""])
        for choice in item.get("choices") or []:
            out.append(f"#scelta({_typ_text(str(choice))})")
        if item.get("choices"):
            out.append("")
        if item["phase"] == "modify":
            out.append(f"#istruzione-modify({_typ_text(modify_hint)})")
            out.append("")
        for starter in item.get("starter_files") or []:
            if starter.get("code"):
                out.extend(
                    [
                        f"*Codice di partenza (`{starter['path']}`):*",
                        "",
                        f"#codice({_typ_string(starter['code'])})",
                        "",
                    ]
                )
        must = item.get("must_include") or []
        if must:
            out.append("*Deve comparire nel codice:* " + ", ".join(f"`{m}`" for m in must))
            out.append("")
        phase = item["phase"]
        if phase == "predict" and item.get("choices"):
            # Nessun box vuoto sotto le sole scelte multiple (niente "run" su carta)
            continue
        out.extend([f'#spazio-risposta(fase: "{phase}")', ""])
    return "\n".join(out)


def render_paper_grid_typst(model: dict[str, Any]) -> str:
    """Griglia docente: punti, context, risposte attese, errori tipici."""
    chapter = model["chapter"]
    assess = model.get("assessment") or {}
    out = [
        f'#import "{_STYLE_IMPORT}": *',
        (
            "#compito-intestazione("
            f"numero: {chapter['order']}, "
            f"titolo: {_typ_string(chapter['title'] + ' — GRIGLIA DOCENTE')}, "
            f"template: {_typ_string('paper-grid')})"
        ),
        "",
    ]
    if assess.get("total_points") is not None:
        out.append(f"#meta-riga({_typ_text(f'Totale: {assess["total_points"]} punti')})")
        out.append("")

    versions = list(assess.get("versions") or ["A"])
    by_ver = model.get("items_by_version") or {"A": model.get("items") or []}

    for ver in versions:
        items = by_ver.get(ver) or []
        out.append(f"= Versione {ver}")
        out.append("")
        for number, item in enumerate(items, 1):
            pts = item.get("points")
            head = f"{number}. {_PHASE_LABEL[item['phase']]}"
            if pts is not None:
                head += f" — {pts} pt"
            out.extend([f"== {head}", f"#testo({_typ_text(item['prompt'])})", ""])
            out.append(f"#item-id({_typ_text('id: ' + str(item.get('id', '')))})")
            out.append("")
            if item.get("code"):
                out.extend([f"#codice({_typ_string(item['code'])})", ""])
            correct = item.get("correct_choices") or []
            if correct:
                out.append("*Risposta/e attesa/e:* " + "; ".join(correct))
                out.append("")
            ctx = (item.get("context") or "").strip()
            if ctx:
                out.append("*Spiegazione (context):*")
                out.append(f"#testo({_typ_text(ctx)})")
                out.append("")
            errors = item.get("typical_errors") or []
            if errors:
                out.append("*Errori tipici:*")
                out.extend(f"- {err}" for err in errors)
                out.append("")
            must = item.get("must_include") or []
            if must:
                out.append("*Deve includere:* " + ", ".join(f"`{m}`" for m in must))
                out.append("")
        if ver != versions[-1]:
            out.append("#pagebreak()")
            out.append("")
    return "\n".join(out)


def render_registro_text(model: dict[str, Any]) -> str:
    """Testo copia-incolla per il registro elettronico."""
    reg = model.get("registro") or {}
    argomenti = (reg.get("argomenti") or "").strip()
    note = (reg.get("note") or "").strip()
    chapter = model["chapter"]
    lines = [
        f"Capitolo {chapter.get('order')}: {chapter.get('title')}",
        f"activity_id: {chapter.get('activity_id')}",
        "",
        "--- Argomenti (registro elettronico) ---",
        argomenti or "(registro.argomenti non impostato)",
    ]
    if note:
        lines.extend(["", "--- Note interne ---", note])
    lines.append("")
    return "\n".join(lines)


def _parse_csv(value: str) -> tuple[str, ...]:
    values = tuple(item.strip() for item in value.split(",") if item.strip())
    if not values:
        raise ValueError("Indica almeno una fase")
    return values


def _parse_emit(value: str) -> tuple[str, ...]:
    values = _parse_csv(value)
    unknown = set(values) - {"json", "typ", "pdf", "text"}
    if unknown:
        raise ValueError(f"Formati emit non validi: {', '.join(sorted(unknown))}")
    return values


def _find_typst() -> str | None:
    """Cerca typst nel PATH o in .tools/ tipico del repo."""
    found = shutil.which("typst")
    if found:
        return found
    candidate = core.ROOT / ".tools" / "typst"
    if candidate.is_file() and os.access(candidate, os.X_OK):
        return str(candidate)
    return None


def _ensure_style(outdir: Path) -> None:
    """Copia lo stile accanto agli .typ generati (import relativo stabile)."""
    src = core.ROOT / "tools" / "cipiupiu" / "templates" / "stile_compito.typ"
    dst = outdir / "stile_compito.typ"
    if not src.is_file():
        raise FileNotFoundError(f"Stile Typst mancante: {src}")
    if not dst.exists() or src.read_bytes() != dst.read_bytes():
        dst.write_bytes(src.read_bytes())


def _compile_typst(typ_path: Path, pdf_path: Path) -> int | None:
    typst = _find_typst()
    if typst is None:
        print(
            "Errore print: comando 'typst' non trovato; installa Typst "
            "(https://typst.app/) oppure metti il binario in .tools/typst",
            file=sys.stderr,
        )
        return 2
    # Root = directory del .typ (contiene stile_compito.typ copiato)
    root = typ_path.parent
    try:
        subprocess.run(
            [typst, "compile", "--root", str(root), str(typ_path), str(pdf_path)],
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"Errore print: Typst non ha compilato {typ_path}: {exc}", file=sys.stderr)
        return exc.returncode or 1
    return None


def _cmd_print_paper(args: Any) -> int:
    """Paper Pack: verifiche A/B, griglia, registro.txt."""
    try:
        emit = _parse_emit(args.emit)
        model = build_paper_model(args.chapter)
    except ValueError as exc:
        print(f"Errore print: {exc}", file=sys.stderr)
        return 2

    outdir = Path(args.out_dir) / "paper" / str(model["chapter"]["activity_id"])
    outdir.mkdir(parents=True, exist_ok=True)
    emitted: list[Path] = []

    if "json" in emit:
        path = outdir / "pack.json"
        path.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        emitted.append(path)

    if "text" in emit or True:
        # registro.txt sempre utile per il docente
        reg_path = outdir / "registro.txt"
        reg_path.write_text(render_registro_text(model), encoding="utf-8")
        emitted.append(reg_path)

    versions = model["assessment"]["versions"]
    need_typ = "typ" in emit or "pdf" in emit
    if need_typ:
        try:
            _ensure_style(outdir)
        except FileNotFoundError as exc:
            print(f"Errore print: {exc}", file=sys.stderr)
            return 2
        for version in versions:
            stem = f"verifica_{version}"
            typ_path = outdir / f"{stem}.typ"
            typ_path.write_text(render_paper_student_typst(model, version), encoding="utf-8")
            emitted.append(typ_path)
            if "pdf" in emit:
                pdf_path = outdir / f"{stem}.pdf"
                err = _compile_typst(typ_path, pdf_path)
                if err is not None:
                    return err
                emitted.append(pdf_path)

        grid_typ = outdir / "griglia.typ"
        grid_typ.write_text(render_paper_grid_typst(model), encoding="utf-8")
        emitted.append(grid_typ)
        if "pdf" in emit:
            grid_pdf = outdir / "griglia.pdf"
            err = _compile_typst(grid_typ, grid_pdf)
            if err is not None:
                return err
            emitted.append(grid_pdf)

    print("Generati: " + ", ".join(str(path) for path in emitted))
    return 0


def _cmd_print_registro(args: Any) -> int:
    """Solo testo argomenti/note per il registro elettronico."""
    try:
        chapter = _validated_chapter(args.chapter)
        meta = chapter.meta
        model = {
            "chapter": {
                "order": _field(meta, "chapter_order"),
                "activity_id": _field(meta, "activity_id"),
                "title": _field(meta, "chapter_title"),
            },
            "registro": {
                "argomenti": _field(meta, "registro_argomenti"),
                "note": _field(meta, "registro_note"),
            },
        }
    except ValueError as exc:
        print(f"Errore print: {exc}", file=sys.stderr)
        return 2

    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"registro_cap{model['chapter']['order']:02d}.txt"
    path.write_text(render_registro_text(model), encoding="utf-8")
    print(f"Generati: {path}")
    return 0


def cmd_print(args: Any) -> int:
    """Genera JSON, Typst e opzionalmente PDF dal modello validato."""
    if args.template == "paper":
        return _cmd_print_paper(args)
    if args.template == "registro":
        return _cmd_print_registro(args)

    try:
        phases = _parse_csv(args.phases)
        emit = _parse_emit(args.emit)
        # worksheet path ignores "text"
        emit = tuple(e for e in emit if e != "text") or ("json",)
        model = build_print_model(args.chapter, phases)
    except ValueError as exc:
        print(f"Errore print: {exc}", file=sys.stderr)
        return 2

    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = f"compito_cap{model['chapter']['order']:02d}_{args.template}"
    emitted: list[Path] = []
    if "typ" in emit or "pdf" in emit:
        try:
            _ensure_style(outdir)
        except FileNotFoundError as exc:
            print(f"Errore print: {exc}", file=sys.stderr)
            return 2

    if "json" in emit:
        json_path = outdir / f"{stem}.json"
        json_path.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        emitted.append(json_path)

    typ_path = outdir / f"{stem}.typ"
    if "typ" in emit or "pdf" in emit:
        typ_path.write_text(render_typst(model, args.template), encoding="utf-8")
        emitted.append(typ_path)

    if "pdf" in emit:
        pdf_path = outdir / f"{stem}.pdf"
        err = _compile_typst(typ_path, pdf_path)
        if err is not None:
            return err
        emitted.append(pdf_path)

    print("Generati: " + ", ".join(str(path) for path in emitted))
    return 0
