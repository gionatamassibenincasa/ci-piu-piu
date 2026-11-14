# Ci Più Più

Open Educational Resource sul linguaggio **C++** per studenti di **3ª ITE SIA**.

Fruizione: **LiaScript**. Consegne: **GitHub** + **Classroom50**.  
Tooling: CLI unica **`cipiupiu`**.

## CLI

```bash
pip install pyyaml jinja2 jsonschema

python -m tools.cipiupiu list
python -m tools.cipiupiu validate
python -m tools.cipiupiu render chapters/05_variabili_costanti_tipi.md
python -m tools.cipiupiu render index.md -o dist/README.md

python -m tools.cipiupiu build              # corso + lezioni (timestamp)
python -m tools.cipiupiu build course       # solo dist/README.md
python -m tools.cipiupiu build lessons      # solo dist/lessons/*.md
python -m tools.cipiupiu build lessons --mode dev
python -m tools.cipiupiu build --force
```

| Comando | Effetto |
|---------|---------|
| `list` | Capitoli per `order` |
| `validate` | Schema + lint corpo (titolo, PREDICT, macro) |
| `render` | Strip FM / `<!--#` / Jinja / include → stdout o `-o` |
| `build course` | `dist/README.md` **senza** aggiungere commento HTML (usa quello di `index.md`) |
| `build lessons` | `dist/lessons/{order}_{activity_id}.md` **con** commento LiaScript + prev/next |

Wrapper legacy: `preprocess.py` → `render`; `tools/validate_chapters.py` → `validate`.

## Predict (unica fonte)

Per `methodology: PRIMM`:

1. Quiz in **`components.predict_quiz`** (frontmatter)
2. Nel corpo, sotto `#### 1. PREDICT`: solo **`[[ predict_block() ]]`**
3. Niente opzioni `[(X)]` scritte a mano nel Predict

## Struttura

```
chapters/   sorgenti + frontmatter
docs/       SPEC, template, metodologia
tools/cipiupiu/  nucleo + CLI
course.yaml metadati LiaScript e URL
dist/       artefatti per LiaScript (in git)
index.md    decide il contenuto del corso completo
```

## Config

`course.yaml` — author/import e `urls.mode` dev|prod per i link prev/next.

## Licenza

Vedi `LICENSE`.
