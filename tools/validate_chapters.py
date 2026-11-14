#!/usr/bin/env python3
"""Valida il frontmatter YAML dei capitoli.

Preferisce jsonschema se installato; altrimenti applica controlli strutturali
minimi allineati a schemas/chapter-frontmatter.schema.json.

  pip install pyyaml jsonschema   # consigliato
  python tools/validate_chapters.py [path…]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Dipendenza mancante: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

try:
    from jsonschema import Draft7Validator

    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "chapter-frontmatter.schema.json"
DEFAULT_CHAPTERS = ROOT / "chapters"
REQUIRED = ("activity_id", "title", "methodology", "order")
METHODOLOGIES = {"PRIMM", "lab", "guide", "convention"}
ACTIONS = {"create", "reference"}
PHASES = {"predict", "run", "investigate", "modify", "make"}


def load_frontmatter(text: str) -> dict:
    if not text.lstrip("\ufeff").lstrip().startswith("---"):
        raise ValueError("manca il frontmatter YAML (--- ... ---)")
    stripped = text.lstrip("\ufeff")
    if not stripped.startswith("---"):
        stripped = stripped.lstrip()
    rest = stripped[3:]
    if rest.startswith("\n"):
        rest = rest[1:]
    end = rest.find("\n---")
    if end == -1:
        raise ValueError("frontmatter non chiuso (manca il secondo ---)")
    data = yaml.safe_load(rest[:end])
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError("il frontmatter deve essere un mapping YAML")
    return data


def validate_structural(meta: dict, path: Path) -> list[str]:
    """Controlli senza jsonschema (sottoinsieme dello schema)."""
    errors: list[str] = []
    for key in REQUIRED:
        if key not in meta:
            errors.append(f"{path.name}: manca campo required '{key}'")

    if "methodology" in meta and meta["methodology"] not in METHODOLOGIES:
        errors.append(
            f"{path.name}: methodology non valida: {meta.get('methodology')!r}"
        )

    if "order" in meta and not isinstance(meta["order"], int):
        errors.append(f"{path.name}: order deve essere intero >= 0")
    elif isinstance(meta.get("order"), int) and meta["order"] < 0:
        errors.append(f"{path.name}: order deve essere >= 0")

    if "activity_id" in meta:
        aid = meta["activity_id"]
        if not isinstance(aid, str) or not aid or not aid[0].isalnum():
            errors.append(f"{path.name}: activity_id non valido")

    components = meta.get("components") or {}
    if "predict_quiz" in components:
        pq = components["predict_quiz"] or {}
        if "question" not in pq or "options" not in pq:
            errors.append(f"{path.name}: predict_quiz richiede question e options")
        opts = pq.get("options") or []
        if opts and not any(o.get("correct") for o in opts if isinstance(o, dict)):
            errors.append(
                f"{path.name}: components.predict_quiz: nessuna option con correct=true"
            )

    files = meta.get("files") or []
    create_paths: set[str] = set()
    for i, item in enumerate(files):
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
            create_paths.add(path_f)
            tf, tc = item.get("template_from"), item.get("template_content")
            has_from = bool(tf)
            has_content = tc is not None and str(tc) != ""
            if has_from == has_content:
                errors.append(
                    f"{path.name}: files[{i}] action=create richiede esattamente uno tra "
                    "template_from e template_content"
                )
            if has_from and not (ROOT / str(tf)).is_file():
                errors.append(
                    f"{path.name}: files[{i}].template_from non trovato: {tf}"
                )
    return errors


def validate_file(path: Path, schema: dict | None) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    try:
        meta = load_frontmatter(text)
    except ValueError as exc:
        return [f"{path.name}: {exc}"]
    except yaml.YAMLError as exc:
        return [f"{path.name}: YAML non valido: {exc}"]

    if HAS_JSONSCHEMA and schema is not None:
        validator = Draft7Validator(schema)
        for err in sorted(validator.iter_errors(meta), key=lambda e: list(e.path)):
            loc = ".".join(str(p) for p in err.path) or "(root)"
            errors.append(f"{path.name}: {loc}: {err.message}")
        # vincoli applicativi sempre
        errors.extend(
            e
            for e in validate_structural(meta, path)
            if "manca campo" not in e and "methodology non" not in e and "order deve" not in e
            and "activity_id non" not in e and "predict_quiz richiede" not in e
        )
        # re-run full structural for create constraints etc. simpler: always structural
        errors = []
        for err in sorted(validator.iter_errors(meta), key=lambda e: list(e.path)):
            loc = ".".join(str(p) for p in err.path) or "(root)"
            errors.append(f"{path.name}: {loc}: {err.message}")
        errors.extend(validate_structural(meta, path))
        # dedupe
        errors = list(dict.fromkeys(errors))
    else:
        errors = validate_structural(meta, path)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida frontmatter capitoli ci-piu-piu")
    parser.add_argument("paths", nargs="*", type=Path, help="File o directory (default: chapters/)")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    schema = None
    if HAS_JSONSCHEMA and args.schema.is_file():
        with args.schema.open(encoding="utf-8") as f:
            schema = json.load(f)
    elif not HAS_JSONSCHEMA:
        print(
            "Nota: jsonschema non installato; uso validazione strutturale ridotta.",
            file=sys.stderr,
        )

    targets: list[Path] = []
    if not args.paths:
        targets = sorted(DEFAULT_CHAPTERS.glob("*.md"))
    else:
        for p in args.paths:
            if p.is_dir():
                targets.extend(sorted(p.glob("*.md")))
            else:
                targets.append(p)

    all_errors: list[str] = []
    checked = 0
    for path in targets:
        checked += 1
        all_errors.extend(validate_file(path, schema))

    if all_errors:
        print(f"FAIL: {len(all_errors)} errore/i su {checked} file")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {checked} file validi")
    return 0


if __name__ == "__main__":
    sys.exit(main())
