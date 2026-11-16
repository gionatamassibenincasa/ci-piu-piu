import json
import unittest
from pathlib import Path

from tools.cipiupiu import printing


SCHEMA_PATH = Path("schemas/chapter-frontmatter.schema.json")


def _declared(node: object, prefix: tuple[str, ...] = ()) -> set[tuple[str, ...]]:
    if not isinstance(node, dict):
        return set()
    paths: set[tuple[str, ...]] = set()
    for name, sub in (node.get("properties") or {}).items():
        path = prefix + (name,)
        paths.add(path)
        paths |= _declared(sub, path)
    if "items" in node:
        path = prefix + ("*",)
        paths.add(path)
        paths |= _declared(node["items"], path)
    return paths


class PrintContractGuardTests(unittest.TestCase):
    def test_printer_reads_only_declared_frontmatter_fields(self) -> None:
        declared = _declared(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))
        for name, path in printing.FIELD_PATHS.items():
            self.assertIn(path, declared, f"Campo non a contratto: {name} -> {path}")


if __name__ == "__main__":
    unittest.main()
