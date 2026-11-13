# Ci Più Più: Copilot Instructions

## Repository architecture

- This repository publishes an Italian interactive LiaScript course that introduces C++ to third-year SIA students (about 16 years old).
- `index.md` is the source entry point: it holds the LiaScript metadata/imports and composes lessons with `#include <chapters/...>`.
- Each `chapters/XX_*.md` file is a self-contained lesson chunk. `README.md` is the generated, publishable course assembled from `index.md`; do not hand-edit it.
- Regenerate the course after changing `index.md` or any chapter. In Windows Command Prompt or PowerShell:

  ```powershell
  cmd /c "set PYTHONIOENCODING=utf-8&&python preprocess.py index.md > README.md"
  ```

  On Unix-like shells:

  ```bash
  python3 preprocess.py index.md > README.md
  ```

- Preview the generated course with the LiaScript dev server:

  ```bash
  liascript-devserver -i README.md -o -l
  ```

- `.mcp.json` configures the LiaScript DevServer MCP bridge for Copilot CLI. It starts `liadev --mcp --live -i README.md`; install `@liascript/devserver` before using it. The bridge writes local session transcripts to `.chats/`, which is ignored.
- There is no configured automated test or lint suite. Use the generation command above as the relevant content check, then inspect the generated diff and preview it when changing LiaScript behavior.
- `syllabus/data/programmazione_3_sia.yaml` composes the curriculum plan from `syllabus/data/ufc/*.yaml`; `syllabus/schemas/schema_programmazione.json` defines its data shape. Preserve `$ref` composition when editing this material.

## Required authoring references

Before creating or revising course material, read and apply these in order:

1. `SKILLS.md` for the target audience, pedagogy, C++ constraints, and output rules.
2. The relevant files in `docs/`: start every lesson from `docs/template_lezione.md`; use `chunking.md`, `primm.md`, `head_first_style.md`, and `quiz_liascript.md` as applicable.
3. `.agents/skills/liascript-syntax/` for supported LiaScript syntax. Do not invent LiaScript constructs.
4. `.agents/skills/liascript-skill/` for general interactive-course patterns.

## Lesson and content conventions

- Write in Italian for C++ beginners transitioning from block programming. Use a direct, encouraging `tu` voice, concrete metaphors, and realistic SIA/business scenarios such as inventory, POS payments, invoices, and customer records.
- Keep each chapter to one observable learning objective and a 15–25 minute core. Follow the established order: context and metaphor, explicit objective, PRIMM, pocket summary, then a bridge to the next chapter.
- Every new programming concept follows **Predict → Run → Investigate → Modify → Make**. Predict comes before execution; Run uses an executable C++ block ending in `@LIA.cpp`; Investigate includes a trace table and a Python Tutor link when variables or memory are involved; Modify provides progressive changes and a `<details>` scaffold; Make reuses the concept in a different business scenario without exposing a complete solution first.
- Begin each abstract concept with `> 💡 **Metafora:**`. Keep code samples below roughly 30–40 lines and use tables, diagrams, and restrained emoji as visual anchors.
- Use only native LiaScript quiz forms: `[(X)]` / `[( )]` for single choice, `[[X]]` / `[[ ]]` for multiple choice, and `[[answer]]` for text input. Put blank lines before and after each quiz; do not use Markdown task-list quiz syntax.
- Use ````text @plantUML` for diagrams. Follow the LiaScript syntax skill for headings, effects, attributes, and quizzes, whose placement rules can fail silently.
- For C++ programs or functions longer than 15 lines, include complete Doxygen documentation. For shorter snippets and exercises, use `///` comments only to explain the economic/logical *why*, never the obvious *what*. If deliberately teaching an error, include the compiler output and explain how to interpret it.
- When introducing raw arrays, include the required `> ⚠️ **Nota dal Mondo Reale:**` explaining that production code normally prefers `std::vector`.
