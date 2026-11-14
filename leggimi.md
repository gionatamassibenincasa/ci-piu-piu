# Ci Più Più

Open Educational Resource sul linguaggio **C++** per studenti di **3ª ITE SIA** (circa 90 ore).

Metodologia: lezioni segmentate, **PRIMM**, stile *brain-friendly* (Head First), esempi di economia aziendale.  
Fruizione: **LiaScript**. Consegne: **GitHub** + **Classroom50** (un assignment ≈ un capitolo).

## Struttura del repository

```
chapters/           # sorgenti lezione (frontmatter YAML + Markdown)
docs/
  SPEC.md           # specifiche tooling (fonte di verità)
  template_*.md     # template PRIMM / lab / guide / convention
  primm.md, chunking.md, head_first_style.md, quiz_liascript.md
schemas/
  chapter-frontmatter.schema.json
tools/
  validate_chapters.py
scaffolds/          # file referenziati da files[].template_from
index.md            # include ordinati per il corso completo
preprocess.py       # include + strip commenti <!--# ... #-->
dist/               # output generato (README corso + lessons/) — non editare a mano
```

## Frontmatter e validazione

Ogni capitolo **deve** iniziare con YAML tra `---`:

- campi obbligatori: `activity_id`, `title`, `methodology`, `order`
- `methodology`: `PRIMM` | `lab` | `guide` | `convention`
- `order`: ordinamento canonico del corso e dei link prev/next

```bash
pip install python-frontmatter jsonschema
python tools/validate_chapters.py              # tutti i chapters/
python tools/validate_chapters.py chapters/08_bivi_complessi_e_regole_if.md
```

Dettaglio: `docs/SPEC.md` e `schemas/chapter-frontmatter.schema.json`.

## Generare il corso per LiaScript

```bash
python3 preprocess.py index.md > README.md
```

In prospettiva il preprocessor produrrà anche `dist/lessons/` (lezioni autonome).  
I blocchi `<!--#` … `#-->` sono note d’autore e **non** compaiono nell’output.

## Template di una nuova lezione

| Metodologia | File da copiare |
|-------------|-----------------|
| PRIMM (default) | `docs/template_primm.md` |
| Laboratorio ambiente | `docs/template_lab.md` |
| Guida di metodo | `docs/template_guide.md` |
| Convenzione (es. Doxygen) | `docs/template_convention.md` |

`docs/template_lezione.md` rimanda al template PRIMM.

## Visualizzazione

Corso su LiaScript (dopo push di `README.md`):

`https://liascript.github.io/course/?https://raw.githubusercontent.com/<org>/<repo>/refs/heads/main/README.md`

## Licenza

Vedi `LICENSE`.
