import json
import tempfile
import unittest
from pathlib import Path

from tools.cipiupiu import printing


class PrintingTests(unittest.TestCase):
    def test_builds_model_from_current_frontmatter_contract(self) -> None:
        model = printing.build_print_model("ciao-mondo-01", ("predict", "modify", "make"))

        self.assertEqual(model["format_version"], 1)
        self.assertEqual(model["chapter"]["order"], 3)
        self.assertEqual([item["phase"] for item in model["items"]], ["predict", "modify", "make"])
        self.assertNotIn("correct", model["items"][0]["choices"][0])
        self.assertEqual(model["items"][1]["starter_files"][0]["path"], "student_work/modify/ciao_modificato.cpp")

    def test_renders_typst_from_canonical_model(self) -> None:
        model = printing.build_print_model("03", ("predict",))

        rendered = printing.render_typst(model, "worksheet")

        self.assertTrue(
            '#import "stile_compito.typ": *' in rendered
            or '/tools/cipiupiu/templates/stile_compito.typ' in rendered,
            rendered.splitlines()[0] if rendered else "empty",
        )
        self.assertIn("Esercizio 1 — Predict", rendered)
        self.assertIn("Stampa Ciao, Mondo! e va a capo", rendered)
        self.assertIn("#scelta(", rendered)
        self.assertNotIn("correct", rendered)

    def test_json_model_is_serializable(self) -> None:
        model = printing.build_print_model("03", ("predict", "make"))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.json"
            path.write_text(json.dumps(model, ensure_ascii=False, indent=2), encoding="utf-8")
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["chapter"]["activity_id"], "ciao-mondo-01")


if __name__ == "__main__":
    unittest.main()
