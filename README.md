# Ci Più Più

Open Educational Resource sul linguaggio **C++** per studenti di **3ª ITE SIA** (circa 90 ore).

Metodologia: lezioni segmentate, **PRIMM**, stile *brain-friendly* (Head First), esempi di economia aziendale.  
Fruizione: **LiaScript**. Consegne: **GitHub** + **Classroom50** (un assignment ≈ un capitolo).

## Struttura del repository

```
chapters/           # sorgenti (frontmatter YAML + Markdown)
docs/
  SPEC.md           # specifiche tooling
  template_*.md     # PRIMM / lab / guide / convention
schemas/
  chapter-frontmatter.schema.json
tools/
  cipiupiu/         # nucleo + CLI (unica fonte di verità)
  validate_chapters.py   # wrapper → cipiupiu validate
scaffolds/          # file per files[].template_from
index.md            # decide cosa entra nel *corso completo* (#include)
preprocess.py       # wrapper → cipiupiu render (compatibilità)
dist/               # artefatti LiaScript (in git; generati da build, slice B)
```

## CLI `cipiupiu` (slice A)

Unica entrypoint. Logica in `tools/cipiupiu/core.py`.

```bash
pip install pyyaml jinja2
# opzionale ma consigliato:
pip install jsonschema

# dalla root del repository:
python -m tools.cipiupiu list
python -m tools.cipiupiu list --all --format json
python -m tools.cipiupiu validate
python -m tools.cipiupiu validate chapters/05_variabili_costanti_tipi.md
python -m tools.cipiupiu render chapters/05_variabili_costanti_tipi.md
python -m tools.cipiupiu render index.md -o README.md

# genera corso + lezioni (timestamp; --force per forzare)
python -m tools.cipiupiu build
python -m tools.cipiupiu build course
python -m tools.cipiupiu build lessons --mode dev
python -m tools.cipiupiu build lessons --only 5
```

**Lezioni vs corso:** solo `build lessons` antepone il commento HTML LiaScript e i link prev/next.  
`build course` usa l’header già presente in `index.md` (nessun commento duplicato).


| Comando | Ruolo |
|---------|--------|
| `list` | Capitoli con frontmatter, ordinati per `order` |
| `validate` | Schema + vincoli (`create`, quiz, …) |
| `render` | Strip YAML, strip `<!--#`, Jinja `[[ ]]`, espande `#include` |
| `build` | `dist/README.md` (corso) + `dist/lessons/*` (lezioni con header LiaScript) |

**Compatibilità:**

```bash
python preprocess.py index.md > README.md          # = cipiupiu render index.md
python tools/validate_chapters.py chapters/05_….md # = cipiupiu validate …
```

### Decisioni di prodotto (congelate)

- **Corso completo**: contenuto deciso da `index.md` (`#include`).
- **Lezioni singole** (`dist/lessons/`, slice B): ordinate e collegate (prev/next) tramite `order` nel frontmatter.
- **`build` senza argomenti** (slice B): genera course + lessons con invalidazione tipo Makefile sui timestamp.
- **`dist/`** resta in git (file letti da LiaScript).

## Frontmatter

Campi obbligatori: `activity_id`, `title`, `methodology`, `order`.  
`methodology`: `PRIMM` | `lab` | `guide` | `convention`.  
Dettaglio: `docs/SPEC.md`, `schemas/chapter-frontmatter.schema.json`.

## Template nuova lezione

| Metodologia | File |
|-------------|------|
| PRIMM | `docs/template_primm.md` |
| Lab | `docs/template_lab.md` |
| Guida | `docs/template_guide.md` |
| Convenzione | `docs/template_convention.md` |

## Visualizzazione LiaScript

Dopo `python -m tools.cipiupiu render index.md -o README.md` e push:

`https://liascript.github.io/course/?https://raw.githubusercontent.com/<org>/<repo>/refs/heads/main/README.md`

## Licenza

Vedi `LICENSE`.
