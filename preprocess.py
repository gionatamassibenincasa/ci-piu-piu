#!/usr/bin/env python3
"""
Pre-processore semplice per file Markdown.
- Espande ricorsivamente le direttive `#include <file.md>`
- Elimina i blocchi autore/LLM delimitati da `<!--#` ... `#-->`
  (compresa la riga di chiusura; anche se apertura e chiusura sono
  sulla stessa riga)
"""

import sys
import os
import re


def process_file(filepath, visited=None):
    if visited is None:
        visited = set()

    abs_path = os.path.abspath(filepath)

    if abs_path in visited:
        print(f"<!-- ERRORE: Inclusione circolare rilevata per '{filepath}' -->", file=sys.stderr)
        return

    visited.add(abs_path)

    if not os.path.isfile(abs_path):
        print(f"<!-- ERRORE: File non trovato '{filepath}' -->", file=sys.stderr)
        return

    in_code_block = False
    with open(abs_path, "r", encoding="utf-8") as f:
        for line in f:
            # --- strip blocchi <--# ... #--> (anche su una sola riga) ---
            if not in_code_block and line.lstrip().startswith("<--#"):
                # Salta fino a (e inclusa) la prima riga che contiene #-->
                while "#-->" not in line:
                    try:
                        line = next(f)
                    except StopIteration:
                        break
                continue  # non emettere né l'apertura né la chiusura

            # Rileva fence Markdown ``` (non espandere include dentro ai code block)
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                print(line, end="")
                continue

            match = (
                re.match(r"^\s*#include\s*<(.+?)>\s*$", line)
                if not in_code_block
                else None
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


if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "index.md"
    process_file(target_file)
