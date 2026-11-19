"""Smoke test Paper Pack v2 — regressione rispetto a SPEC v0.6 §4.4."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from tools.cipiupiu import printing


class PaperPackSmokeTests(unittest.TestCase):
    """Fase 0.1: format_version 2, id stabili, A/B, context, emit json."""

    def test_build_paper_model_format_v2_and_stable_ids(self) -> None:
        model = printing.build_paper_model("03")

        self.assertEqual(model["format_version"], 2)
        self.assertEqual(model["kind"], "paper")
        self.assertEqual(model["chapter"]["activity_id"], "ciao-mondo-01")
        self.assertIn("items_by_version", model)
        self.assertIn("A", model["items_by_version"])
        self.assertIn("B", model["items_by_version"])

        ids = [item["id"] for item in model["items"]]
        self.assertEqual(
            ids,
            [
                "ciao-mondo-01/predict",
                "ciao-mondo-01/investigate",
                "ciao-mondo-01/modify",
                "ciao-mondo-01/make",
            ],
        )
        for item in model["items"]:
            self.assertIn("/", item["id"])
            self.assertTrue(str(item["id"]).startswith("ciao-mondo-01/"))

    def test_variant_b_differs_from_a_on_predict(self) -> None:
        model = printing.build_paper_model("ciao-mondo-01")
        a = model["items_by_version"]["A"][0]
        b = model["items_by_version"]["B"][0]
        self.assertEqual(a["phase"], "predict")
        self.assertNotEqual(a["prompt"], b["prompt"])

    def test_predict_has_context_and_correct_choices(self) -> None:
        model = printing.build_paper_model("03")
        pred = model["items_by_version"]["A"][0]
        self.assertTrue((pred.get("context") or "").strip())
        self.assertTrue(pred.get("correct_choices"))

    def test_grid_includes_context_and_ids(self) -> None:
        model = printing.build_paper_model("03")
        grid = printing.render_paper_grid_typst(model)
        self.assertIn("ciao-mondo-01/predict", grid)
        self.assertIn("Spiegazione (context)", grid)
        self.assertIn("Versione A", grid)
        self.assertIn("Versione B", grid)

    def test_cli_print_paper_emits_json_pack(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            args = SimpleNamespace(
                chapter="03",
                template="paper",
                emit="json",
                out_dir=directory,
                phases="predict,modify,make",
            )
            code = printing.cmd_print(args)
            self.assertEqual(code, 0)
            pack = Path(directory) / "paper" / "ciao-mondo-01" / "pack.json"
            self.assertTrue(pack.is_file(), f"manca {pack}")
            data = json.loads(pack.read_text(encoding="utf-8"))
            self.assertEqual(data["format_version"], 2)
            self.assertIn("items_by_version", data)
            reg = Path(directory) / "paper" / "ciao-mondo-01" / "registro.txt"
            self.assertTrue(reg.is_file())


if __name__ == "__main__":
    unittest.main()
