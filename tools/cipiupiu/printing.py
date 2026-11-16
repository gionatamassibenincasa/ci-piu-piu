"""Export tipografico degli esercizi PRIMM dal frontmatter validato."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from . import core


FIELD_PATHS = {
    "activity_id": ("activity_id",),
    "chapter_order": ("order",),
    "chapter_title": ("title",),
    "predict_question": ("components", "predict_quiz", "question"),
    "predict_code": ("components", "predict_quiz", "code"),
    "predict_options": ("components", "predict_quiz", "options"),
    "predict_option_text": ("components", "predict_quiz", "options", "*", "text"),
    "modify_instructions": ("components", "modify_instructions"),
    "make_instructions": ("components", "make_instructions"),
    "files": ("files",),
    "file_path": ("files", "*", "path"),
    "file_action": ("files", "*", "action"),
    "file_phase": ("files", "*", "phase"),
    "file_description": ("files", "*", "description"),
    "file_template_content": ("files", "*", "template_content"),
    "file_validation_rules": ("files", "*", "validation_rules"),
}

PRINTABLE_PHASES = ("predict", "modify", "make")
_PHASE_LABEL = {"predict": "Predict", "modify": "Modify", "make": "Make"}
_STYLE_IMPORT = "/tools/cipiupiu/templates/stile_compito.typ"


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
        question = _field(meta, "predict_question")
        if not question:
            return None
        return {
            "id": f"{_field(meta, 'activity_id')}-predict",
            "phase": phase,
            "prompt": question,
            "code": _field(meta, "predict_code"),
            "choices": [text for text in (_field(meta, "predict_option_text") or []) if text],
            "starter_files": [],
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


def _typ_string(value: str | None) -> str:
    return json.dumps(value or "", ensure_ascii=False)


def render_typst(model: dict[str, Any], template: str) -> str:
    """Adatta il modello canonico a Typst, senza leggere il frontmatter."""
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
                f"#testo({_typ_string(item['prompt'])})",
                "",
            ]
        )
        if item["code"]:
            out.extend([f"#codice({_typ_string(item['code'])})", ""])
        for choice in item["choices"]:
            out.append(f"#scelta({_typ_string(choice)})")
        if item["choices"]:
            out.append("")
        for starter in item["starter_files"]:
            out.append(f"*File di partenza: `{starter['path']}`*")
            if starter["code"]:
                out.extend(["", f"#codice({_typ_string(starter['code'])})"])
            rules = starter["validation_rules"] or {}
            requirements: list[str] = []
            if rules.get("min_lines") is not None:
                requirements.append(f"almeno {rules['min_lines']} righe")
            requirements.extend(f"contiene `{value}`" for value in rules.get("must_contain", []))
            if requirements:
                out.extend(["", "*Requisiti:*"])
                out.extend(f"- {requirement}" for requirement in requirements)
            out.append("")
        out.extend([f'#spazio-risposta(fase: "{item["phase"]}")', ""])
    return "\n".join(out)


def _parse_csv(value: str) -> tuple[str, ...]:
    values = tuple(item.strip() for item in value.split(",") if item.strip())
    if not values:
        raise ValueError("Indica almeno una fase")
    return values


def _parse_emit(value: str) -> tuple[str, ...]:
    values = _parse_csv(value)
    unknown = set(values) - {"json", "typ", "pdf"}
    if unknown:
        raise ValueError(f"Formati emit non validi: {', '.join(sorted(unknown))}")
    return values


def cmd_print(args: Any) -> int:
    """Genera JSON, Typst e opzionalmente PDF dal modello validato."""
    try:
        phases = _parse_csv(args.phases)
        emit = _parse_emit(args.emit)
        model = build_print_model(args.chapter, phases)
    except ValueError as exc:
        print(f"Errore print: {exc}", file=sys.stderr)
        return 2

    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = f"compito_cap{model['chapter']['order']:02d}_{args.template}"
    emitted: list[Path] = []

    if "json" in emit:
        json_path = outdir / f"{stem}.json"
        json_path.write_text(json.dumps(model, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        emitted.append(json_path)

    typ_path = outdir / f"{stem}.typ"
    if "typ" in emit or "pdf" in emit:
        typ_path.write_text(render_typst(model, args.template), encoding="utf-8")
        emitted.append(typ_path)

    if "pdf" in emit:
        typst = shutil.which("typst")
        if typst is None:
            print("Errore print: comando 'typst' non trovato; installa Typst per --emit pdf", file=sys.stderr)
            return 2
        pdf_path = outdir / f"{stem}.pdf"
        try:
            subprocess.run(
                [typst, "compile", "--root", str(core.ROOT), str(typ_path), str(pdf_path)],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            print(f"Errore print: Typst non ha compilato {typ_path}: {exc}", file=sys.stderr)
            return exc.returncode or 1
        emitted.append(pdf_path)

    print("Generati: " + ", ".join(str(path) for path in emitted))
    return 0
