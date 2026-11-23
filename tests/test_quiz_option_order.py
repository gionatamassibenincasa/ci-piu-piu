"""La risposta corretta non deve codificarsi come 'sempre la prima option'."""
from __future__ import annotations

import unittest

from tools.cipiupiu.core import shuffle_quiz_options, render_jinja


class QuizOptionOrderTests(unittest.TestCase):
    def test_shuffle_moves_correct_when_authored_first(self) -> None:
        opts = [
            {"text": "giusta", "correct": True},
            {"text": "sbagliata-a", "correct": False},
            {"text": "sbagliata-b", "correct": False},
        ]
        # Prova più seed: almeno uno non lascia la corretta in posizione 0
        positions = set()
        for key in ("q1", "q2", "domanda lunga sul cout", "altro|seed"):
            sh = shuffle_quiz_options(opts, seed_key=key)
            positions.add(next(i for i, o in enumerate(sh) if o.get("correct")))
            self.assertEqual(sum(1 for o in sh if o.get("correct")), 1)
        self.assertTrue(positions - {0}, msg="shuffle non deve fissare sempre correct in 0")

    def test_render_preserves_correct_marker_not_index(self) -> None:
        meta = {
            "components": {
                "predict_quiz": {
                    "items": [
                        {
                            "question": "Test ordine?",
                            "options": [
                                {"text": "AAA-corretta", "correct": True},
                                {"text": "BBB", "correct": False},
                                {"text": "CCC", "correct": False},
                            ],
                        }
                    ]
                }
            }
        }
        out = render_jinja("[[ predict_block() ]]", meta)
        self.assertIn("[(X)] AAA-corretta", out)
        self.assertIn("[( )] BBB", out)
        lines = [ln for ln in out.splitlines() if ln.startswith("[(")]
        self.assertEqual(len(lines), 3)
        # Non richiedere che X non sia prima per questo seed; solo che X sia sul testo giusto
        x_line = next(ln for ln in lines if "[(X)]" in ln)
        self.assertIn("AAA-corretta", x_line)


if __name__ == "__main__":
    unittest.main()
