#!/usr/bin/env python3
"""Wrapper di compatibilità → python -m tools.cipiupiu render."""

from __future__ import annotations

import sys
from pathlib import Path

# permette `python preprocess.py` dalla root del repo
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.cipiupiu.cli import main


def _compat_argv() -> list[str]:
    # preprocess.py [file]  →  render [file]
    # preprocess.py         →  render index.md
    args = sys.argv[1:]
    if not args:
        return ["render", "index.md"]
    if args[0] in {"-h", "--help"}:
        return ["render", "--help"]
    return ["render", *args]


if __name__ == "__main__":
    raise SystemExit(main(_compat_argv()))