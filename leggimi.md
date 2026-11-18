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

# compito PRIMM stampabile: modello canonico + sorgente Typst
python -m tools.cipiupiu print 03 --emit json,typ --out-dir output
# aggiungi pdf se il comando `typst` è installato e disponibile nel PATH
python -m tools.cipiupiu print 03 --template worksheet --emit json,typ,pdf
# Paper Pack (verifica formale A/B + griglia + registro)
python -m tools.cipiupiu print 03 --template paper --emit json,typ,pdf --out-dir output
python -m tools.cipiupiu print 03 --template registro --out-dir output

# template repo GitHub per Classroom50 (un activity_id)
python -m tools.cipiupiu scaffold-assignment \
  --activity ciao-mondo-01 \
  --org dip-inf-savoia-benincasa \
  --classroom "26-27 3A SIA"
# oppure con config di classe:
#   --config assignments/3sia-2026.yaml --activity ciao-mondo-01
```

| Comando | Effetto |
|---------|---------|
| `list` | Capitoli per `order` |
| `validate` | Schema + lint corpo (titolo, PREDICT, macro) |
| `render` | Strip FM / `<!--#` / Jinja / include → stdout o `-o` |
| `build course` | `dist/README.md` **senza** aggiungere commento HTML (usa quello di `index.md`) |
| `build lessons` | `dist/lessons/{order}_{activity_id}.md` **con** commento LiaScript + prev/next |
| `print` | Frontmatter validato → JSON canonico → Typst → PDF opzionale |
| `scaffold-assignment` | Crea/aggiorna il **template repo** GitHub da `files[].action=create` |

Wrapper legacy: `preprocess.py` → `render`; `tools/validate_chapters.py` → `validate`.

## Predict (unica fonte)

Per `methodology: PRIMM`:

1. Quiz in **`components.predict_quiz`** (frontmatter)
2. Nel corpo, sotto `#### 1. PREDICT`: solo **`[[ predict_block() ]]`**
3. Niente opzioni `[(X)]` scritte a mano nel Predict

## Compiti stampabili

`print` usa esclusivamente il frontmatter già validato: non interpreta il
Markdown del capitolo e non introduce chiavi nuove. Le fasi predefinite sono
`predict,modify,make`; selezionane un sottoinsieme con
`--phases predict,make`.

| Contenuto del compito | Fonte condivisa con Classroom50 |
|---|---|
| Numero, titolo e quiz Predict senza soluzione | `order`, `title`, `components.predict_quiz` |
| Consegne, codice iniziale e requisiti | `components.*_instructions`, `files[]` |

L'output `json` è il modello macchina riusabile; l'output `typ` è rifinibile
dal docente. Lo stile è `tools/cipiupiu/templates/stile_compito.typ`. Per il
PDF installa [Typst](https://typst.app/) e usa `--emit pdf`.

Punti, rubriche o righe di risposta su misura non vanno aggiunti localmente al
frontmatter: richiedono un'estensione versionata dello schema, utile sia alla
stampa sia a Classroom50.

## Struttura

```
chapters/   sorgenti + frontmatter
docs/       SPEC, template, metodologia
tools/cipiupiu/  nucleo + CLI
tools/cipiupiu/templates/  stile Typst dei compiti
course.yaml metadati LiaScript e URL
dist/       artefatti per LiaScript (in git)
index.md    decide il contenuto del corso completo
```

## Config

`course.yaml` — author/import e `urls.mode` dev|prod per i link prev/next.

## Licenza

Vedi `LICENSE`.


## Classroom50 (template repo)

Documentazione completa: **`docs/scaffold_assignment.md`**.

- Un `activity_id` → un repository template → un assignment.
- Solo i file `action: create` del frontmatter finiscono nel template.
- La creazione dell’assignment su Classroom50 resta **manuale** in v1 (istruzioni stampate dal comando).

## Tre prodotti

1. **OER online** (`build`) — LiaScript  
2. **Classroom50** (`scaffold-assignment`) — template esercizi  
3. **Paper Pack** (`print --template paper`) — verifica cartacea  

Un capitolo, un `activity_id`, tre proiezioni. Dettaglio: `docs/products.md`.
