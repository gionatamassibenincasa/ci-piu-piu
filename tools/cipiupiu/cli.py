"""CLI cipiupiu — slice A: validate, list, render."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import core


def cmd_validate(args: argparse.Namespace) -> int:
    schema = core.load_schema(Path(args.schema) if args.schema else None)
    if args.schema and schema is None:
        print(f"Schema non trovato: {args.schema}", file=sys.stderr)
        return 2

    targets: list[Path] = []
    if not args.paths:
        targets = sorted(core.DEFAULT_CHAPTERS.glob("*.md"))
    else:
        for p in args.paths:
            path = Path(p)
            if path.is_dir():
                targets.extend(sorted(path.glob("*.md")))
            else:
                targets.append(path)

    all_errors: list[str] = []
    for path in targets:
        all_errors.extend(core.validate_chapter(path, schema))

    if all_errors:
        print(f"FAIL: {len(all_errors)} errore/i su {len(targets)} file", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(f"OK: {len(targets)} file validi")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    chapters_dir = Path(args.chapters) if args.chapters else core.DEFAULT_CHAPTERS
    chapters = core.iter_chapters(chapters_dir)

    # includi anche file senza FM se --all
    if args.all:
        seen = {c.path for c in chapters}
        for path in sorted(chapters_dir.glob("*.md")):
            if path.resolve() not in seen:
                chapters.append(core.Chapter(path=path.resolve(), meta={}, body=""))

    if args.format == "json":
        data = [
            {
                "order": c.order,
                "activity_id": c.activity_id if c.meta else None,
                "methodology": c.methodology or None,
                "title": c.title if c.meta else None,
                "path": str(c.path.relative_to(core.ROOT)) if c.path.is_relative_to(core.ROOT) else str(c.path),
                "has_create_files": any(
                    isinstance(f, dict) and f.get("action") == "create"
                    for f in (c.meta.get("files") or [])
                ),
            }
            for c in chapters
        ]
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    # table
    print(f"{'ord':>4}  {'activity_id':<28}  {'method':<11}  {'create':<6}  path")
    print("-" * 90)
    for c in chapters:
        if not c.meta:
            print(f"{'—':>4}  {'(no frontmatter)':<28}  {'—':<11}  {'—':<6}  {c.path.name}")
            continue
        has_c = any(
            isinstance(f, dict) and f.get("action") == "create" for f in (c.meta.get("files") or [])
        )
        print(
            f"{c.order if c.order is not None else '—':>4}  "
            f"{c.activity_id:<28}  "
            f"{c.methodology:<11}  "
            f"{'yes' if has_c else 'no':<6}  "
            f"{c.path.name}"
        )
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if not path.is_file():
        print(f"File non trovato: {path}", file=sys.stderr)
        return 2
    try:
        text = core.render_file(path, expand=not args.no_includes)
    except Exception as exc:  # noqa: BLE001
        print(f"Errore render: {exc}", file=sys.stderr)
        return 1
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"Scritto {out}", file=sys.stderr)
    else:
        sys.stdout.write(text)
        if text and not text.endswith("\n"):
            sys.stdout.write("\n")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cipiupiu",
        description="CLI tooling OER ci-più-più (slice A: validate, list, render).",
    )
    sub = p.add_subparsers(dest="command", required=True)

    v = sub.add_parser("validate", help="Valida il frontmatter dei capitoli")
    v.add_argument("paths", nargs="*", help="File o directory (default: chapters/)")
    v.add_argument("--schema", default=None, help="Path allo schema JSON")
    v.set_defaults(func=cmd_validate)

    ls = sub.add_parser("list", help="Elenca i capitoli ordinati per order")
    ls.add_argument("--chapters", default=None, help="Directory chapters/")
    ls.add_argument("--format", choices=("table", "json"), default="table")
    ls.add_argument("--all", action="store_true", help="Include file senza frontmatter")
    ls.set_defaults(func=cmd_list)

    r = sub.add_parser("render", help="Render di un Markdown (strip FM, Jinja, include)")
    r.add_argument("path", help="File sorgente (capitolo o index.md)")
    r.add_argument("-o", "--output", help="Scrivi su file invece che stdout")
    r.add_argument(
        "--no-includes",
        action="store_true",
        help="Non espandere #include (lezione singola grezza)",
    )
    r.set_defaults(func=cmd_render)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))
