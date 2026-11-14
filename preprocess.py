#!/usr/bin/env python3
"""
Pre-processore Markdown per ci-piu-piu.

- Espande ricorsivamente `#include <file.md>`
- Elimina i blocchi autore/LLM `<!--#` ... `#-->` (anche su una sola riga)
- Elimina il frontmatter YAML iniziale (`---` ... `---`) da ogni file incluso,
  così non finisce nell'output LiaScript
- Non espande include né interpreta direttive dentro i fence di codice ```
"""

from __future__ import annotations

import os
import re
import sys


def strip_yaml_frontmatter(lines: list[str]) -> list[str]:
    """Se il file inizia con frontmatter YAML, rimuove il blocco --- ... ---."""
    i = 0
    # salta righe vuote / solo whitespace in testa
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        return lines
    i += 1
    while i < len(lines):
        if lines[i].strip() == "---":
            i += 1
            # salta una riga vuota subito dopo il frontmatter, se c'è
            if i < len(lines) and lines[i].strip() == "":
                i += 1
            return lines[i:]
        i += 1
    # frontmatter non chiuso: non modificare
    return lines


def process_file(filepath: str, visited: set[str] | None = None) -> None:
    if visited is None:
        visited = set()

    abs_path = os.path.abspath(filepath)

    if abs_path in visited:
        print(
            f"<!-- ERRORE: Inclusione circolare rilevata per '{filepath}' -->",
            file=sys.stderr,
        )
        return

    visited.add(abs_path)

    if not os.path.isfile(abs_path):
        print(f"<!-- ERRORE: File non trovato '{filepath}' -->", file=sys.stderr)
        return

    with open(abs_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = strip_yaml_frontmatter(lines)

    in_code_block = False
    idx = 0
    while idx < len(lines):
        line = lines[idx]

        # --- strip blocchi <!--# ... #--> ---
        if not in_code_block and line.lstrip().startswith("<!--#"):
            while idx < len(lines) and "#-->" not in lines[idx]:
                idx += 1
            idx += 1  # salta anche la riga di chiusura (o EOF)
            continue

        # fence Markdown
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            print(line, end="")
            idx += 1
            continue

        match = (
            re.match(r"^\s*#include\s*<(.+?)>\s*$", line) if not in_code_block else None
        )

        if match:
            include_file = match.group(1)
            current_dir = os.path.dirname(abs_path)
            target_path = os.path.join(current_dir, include_file)
            if not os.path.isfile(target_path) and os.path.isfile(target_path + ".md"):
                target_path = target_path + ".md"
            process_file(target_path, visited)
        else:
            print(line, end="")

        idx += 1


if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "index.md"
    process_file(target_file)
