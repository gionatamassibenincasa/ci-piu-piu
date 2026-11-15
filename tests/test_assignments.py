import tempfile
import unittest
from pathlib import Path

from tools.cipiupiu import assignments, core


class AssignmentScaffoldTests(unittest.TestCase):
    def test_activity_writes_only_create_files(self) -> None:
        chapter = assignments.load_activity("ciao-mondo-01")

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            assignments.write_template_files(chapter, root)

            self.assertEqual(
                sorted(path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()),
                [
                    "README.md",
                    "student_work/investigate/answers.md",
                    "student_work/make/presentazione.cpp",
                    "student_work/modify/ciao_modificato.cpp",
                    "student_work/predict/answers.md",
                    "student_work/run/answers.md",
                ],
            )

    def test_config_overrides_assignment_defaults(self) -> None:
        chapter = assignments.load_activity("ciao-mondo-01")

        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "3sia.yaml"
            config.write_text(
                """
classroom:
  org: ORG
  classroom_name: 3sia
assignments:
  - activity_id: ciao-mondo-01
    title: Il Primo Dialogo con la Macchina
    slug: ciao-mondo
    deadline: "2026-12-01T23:59:00+01:00"
""",
                encoding="utf-8",
            )
            options = assignments.resolve_options(
                chapter,
                config_path=config,
                org=None,
                classroom=None,
            )

        self.assertEqual(options.org, "ORG")
        self.assertEqual(options.assignment_name, "Il Primo Dialogo con la Macchina")
        self.assertEqual(options.assignment_slug, "ciao-mondo")
        self.assertEqual(options.deadline, "2026-12-01T23:59:00+01:00")

    def test_rejects_unsafe_template_path(self) -> None:
        chapter = core.Chapter(
            path=Path("unsafe.md"),
            meta={
                "files": [
                    {
                        "path": "../outside.txt",
                        "action": "create",
                        "template_content": "unsafe",
                    }
                ]
            },
        )

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "Percorso file non sicuro"):
                assignments.write_template_files(chapter, Path(directory))


if __name__ == "__main__":
    unittest.main()
