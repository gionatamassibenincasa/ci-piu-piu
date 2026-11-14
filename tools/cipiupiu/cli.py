"""CLI cipiupiu — validate, list, render, build."""

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



def cmd_build(args: argparse.Namespace) -> int:
    """build | build course | build lessons — timestamp-aware."""
    cfg = core.load_course_config(Path(args.config) if args.config else None)
    force = bool(args.force)
    mode = args.mode
    target = args.target  # None, "course", "lessons"

    do_course = target in (None, "course")
    do_lessons = target in (None, "lessons")

    index = Path(args.index) if args.index else Path(cfg.get("index") or "index.md")
    if not index.is_absolute():
        index = (core.ROOT / index).resolve()

    if args.output and target == "course":
        course_out = Path(args.output)
    else:
        course_out = Path(cfg.get("course_out") or "dist/README.md")
    if not course_out.is_absolute():
        course_out = (core.ROOT / course_out).resolve()

    lessons_dir = Path(args.lessons_dir) if args.lessons_dir else None

    n_written = 0
    if do_course:
        path, written = core.build_course(
            index_path=index,
            out_path=course_out,
            force=force,
        )
        status = "updated" if written else "up-to-date"
        print(f"course: {status} → {path}")
        n_written += int(written)

    if do_lessons:
        results = core.build_lessons(
            course_cfg=cfg,
            lessons_dir=lessons_dir,
            mode=mode,
            force=force,
            only=args.only,
        )
        for path, written in results:
            status = "updated" if written else "up-to-date"
            print(f"lesson: {status} → {path.name}")
            n_written += int(written)
        if not results:
            print("lesson: nessun capitolo con frontmatter", file=sys.stderr)

    print(f"done: {n_written} file scritti")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cipiupiu",
        description="CLI tooling OER ci-più-più (validate, list, render, build).",
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

    b = sub.add_parser(
        "build",
        help="Genera dist/README.md (corso) e/o dist/lessons/* (con header LiaScript)",
    )
    b.add_argument(
        "target",
        nargs="?",
        choices=("course", "lessons"),
        default=None,
        help="Solo course, solo lessons, o entrambi se omesso",
    )
    b.add_argument("--force", action="store_true", help="Ignora timestamp")
    b.add_argument("--mode", choices=("dev", "prod"), default=None)
    b.add_argument("--config", default=None, help="Path course.yaml")
    b.add_argument("--index", default=None, help="index.md del corso")
    b.add_argument("-o", "--output", default=None, help="Output corso (solo target course)")
    b.add_argument("--lessons-dir", default=None)
    b.add_argument("--only", default=None, help="Filtra lezioni (order, activity_id o nome file)")
    b.set_defaults(func=cmd_build)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))
