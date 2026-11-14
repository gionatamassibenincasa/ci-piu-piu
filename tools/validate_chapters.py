#!/usr/bin/env python3
"""Wrapper → python -m tools.cipiupiu validate."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.cipiupiu.cli import main


def _argv() -> list[str]:
    args = sys.argv[1:]
    return ["validate", *args]


if __name__ == "__main__":
    raise SystemExit(main(_argv()))
