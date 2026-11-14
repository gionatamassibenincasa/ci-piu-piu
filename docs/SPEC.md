# Specifiche tooling – ci-piu-piu (v0.2)

Fonte di verità per preprocessor, frontmatter, template repository e integrazione Classroom50.

## 1. Obiettivi v1

| ID | Obiettivo | Priorità |
|----|-----------|----------|
| O1 | Schema + template lezione | Must |
| O2 | Template repo + assignment Classroom50 (1 assignment = 1 capitolo) | Must |
| O3 | `dist/README.md` corso completo | Must |
| O4 | `dist/lessons/*.md` lezioni autonome con prev/next | Must |
| O5 | Post-scadenza: download repo + `validation_rules` base | Should |
| O6 | Tracking visualizzazione opt-in | Could |

**Corso completo** = un unico Markdown amalgamato (`dist/README.md`) per la sequenza annuale.  
**Lezione autonoma** = un capitolo in `dist/lessons/`, con link prev/next, per recupero e link diretti.

## 2. Commenti `<!--#` … `#-->`

**Si mantengono.**  
Sono note autore/LLM **non** destinate a LiaScript. `preprocess.py` le elimina interamente (apertura, corpo, chiusura `#-->`).  
Non sono annidabili. Non sostituiscono il frontmatter: il frontmatter è dato strutturale; i blocchi `<!--#` sono appunti di produzione.

## 3. Frontmatter

- Schema: `schemas/chapter-frontmatter.schema.json`
- Validazione: `python tools/validate_chapters.py [path…]`
- **`order`** = ordinamento canonico (non il nome file, non solo `index.md`)
- **`methodology`**: `PRIMM` | `lab` | `guide` | `convention`
- **`components`**: dati per assignment/validazione e macro Jinja **esplicite** (es. `[[ predict_block() ]]`). Il Markdown didattico resta la narrazione principale; non va riscritto tutto in YAML.
- **`files`**: `action: create` → repo template studente; `reference` → solo supporto. Per `create`: esattamente uno tra `template_from` e `template_content`.
- Capitoli non-PRIMM: `components` assente o vuoto; `files` può essere `[]`.
- `target` non usato in v1 (gli assignment li decide la config classe).

### Merge metadati LiaScript

1. Default globali (`course.yaml` o header di generazione)
2. Campi scalari del capitolo sovrascrivono
3. `import` = unione ordinata globali + capitolo, senza duplicati
4. Frontmatter **non** compare nell’output LiaScript (solo metadati espansi nel formato atteso dal player)

## 3.1 CLI `cipiupiu` (fonte unica)

Entrypoint: `python -m tools.cipiupiu`.

| Slice | Comandi | Stato |
|-------|---------|--------|
| A | `validate`, `list`, `render` | attuale |
| B | `build` (course + lessons, timestamp) | previsto |
| C | `scaffold-assignment` | previsto |
| D | `collect` | previsto |

Nucleo condiviso: `tools/cipiupiu/core.py`  
(`load_frontmatter` / `split_frontmatter`, `strip_author_blocks`, `render_jinja`, `expand_includes`, `render_file`, `iter_chapters`, `validate_chapter`).

Regole:
- `index.md` decide i capitoli del **corso completo**.
- `order` decide ordinamento/prev-next delle **lezioni singole**.
- `dist/` versionato in git (consumo LiaScript).


## 4.1 Predict: unica fonte di verità

Per i capitoli `methodology: PRIMM`:

1. Il quiz Predict vive in **`components.predict_quiz`** (frontmatter).
2. Nel corpo Markdown, sotto `#### 1. PREDICT`, compare solo **`[[ predict_block() ]]`**.
3. Non duplicare opzioni `[(X)]` a mano nel Predict (il render le genera dalla macro).
4. `cipiupiu validate` verifica: heading PREDICT, presenza di `predict_quiz`, presenza della macro.

## 4. Jinja nel corpo Markdown

Delimitatori che non collidono col C++:

| Tipo | Delimitatore |
|------|----------------|
| Variabile / macro | `[[ ... ]]` |
| Blocco | `[% ... %]` |
| Commento | `[# ... #]` |

Macro tipiche (implementazione successive): `[[ predict_block() ]]`, `[[ nav_prev_next() ]]`.  
I quiz già scritti a mano con sintassi LiaScript restano validi.

## 5. Pipeline logica

```
chapters/*.md  (+ frontmatter)
        │
        ▼
preprocessor (frontmatter + Jinja + strip <!--# + includes)
        │
        ├── dist/README.md
        └── dist/lessons/<order>_<slug>.md
        │
config classe YAML
        │
        ▼
template repo (solo files action=create) + assignment Classroom50
        │
        ▼
(post-scadenza) clone studenti + validation_rules
```

## 6. Template lezione

| File | Uso |
|------|-----|
| `docs/template_lezione.md` | Alias / puntatore al template PRIMM |
| `docs/template_primm.md` | Lezioni PRIMM |
| `docs/template_lab.md` | Sessioni lab (es. toolchain) |
| `docs/template_guide.md` | Guide metodologiche |
| `docs/template_convention.md` | Convenzioni (es. Doxygen) |

## 7. Fuori scope v1

- Più capitoli in un solo assignment
- Test I/O / runner
- UI web docente
- Sostituzione di Classroom50
- Tracking obbligatorio

## 8. Riferimenti

- LiaScript: https://liascript.github.io/
- Classroom50: https://classroom50.org /
- Schema locale: `schemas/chapter-frontmatter.schema.json`
