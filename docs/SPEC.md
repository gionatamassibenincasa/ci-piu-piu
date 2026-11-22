# Specifiche tooling – ci-piu-piu (v0.7)

Fonte di verità per CLI, frontmatter, Classroom50 e Paper Pack.

**Stato:** Slice A–C ed E operative; D previsto. Paper Pack v2 (id stabili, context, varianti A/B).  
**Data:** 2026-11-18

---

## 0. Tre prodotti

Vedi anche [`docs/products.md`](products.md).

| ID | Prodotto | Cliente | Valore relativo |
|----|----------|---------|-----------------|
| P1 | OER online (LiaScript) | Studente | Alto per lo studente; poca disponibilità a pagare da solo |
| P2 | Template esercizi Classroom50 | Docente laboratorio | Alto (tempo) |
| P3 | Paper Pack | Docente teoria | Molto alto (verifiche in classe) |

Un capitolo = un `activity_id` + un frontmatter. I tre prodotti sono **proiezioni** (`build`, `scaffold-assignment`, `print`), non alberi di file separati. Non si ristrutturano le lezioni per prodotto in v1.

---

## 1. Contesto e obiettivi

- Classe ~15 studenti; GitHub + Classroom50 già in uso.
- Capitoli: `chapters/*.md` (YAML + Markdown). Metodologia tipica: **PRIMM**.
- Studenti su LiaScript; clone repo di lavoro via Classroom50.
- Tooling: solo Python; segreti in `.env`.

| ID | Obiettivo | Priorità | Stato |
|----|-----------|----------|--------|
| O1 | Schema + template lezione | Must | Fatto |
| O2 | Template repo Classroom50 (1 assignment = 1 capitolo) | Must | Fatto (v1 semi-auto) |
| O3 | `dist/README.md` corso completo | Must | Fatto |
| O4 | `dist/lessons/*.md` con prev/next | Must | Fatto |
| O5 | Collect post-scadenza + `validation_rules` | Should | Slice D |
| O6 | Tracking visualizzazione opt-in | Could | Non iniziato |
| O7 | Stampa worksheet + Paper Pack dal frontmatter | Must | Fatto (JSON/Typst; PDF con Typst) |

**Principi:** capitolo autoconsistente; config compiti per classe separata; stampa = consumatore del modello validato (come `build`); `dist/` in git.

---

## 2. User stories

### Docente

| ID | Storia |
|----|--------|
| US-D1 | Creare un capitolo (frontmatter + Markdown) e validarlo senza scrivere tooling. |
| US-D2 | `validate` con errori chiari su schema, Predict, `files[]`. |
| US-D3 | `build` → corso + lezioni autonome (header LiaScript, prev/next). |
| US-D4 | Da config classe: template repo (`action: create`) + istruzioni Classroom50. |
| US-D5 | Dopo scadenza: download repo studenti + report su `validation_rules`. |
| US-D6 | Build lezioni in modalità `dev` o `prod` (URL). |
| US-D7 | Worksheet stampabile (Predict/Modify/Make) senza duplicare consegne nel Markdown. |
| US-D8 | **Paper Pack**: verifica A/B, griglia (risposte + context), registro. |
| US-D9 | Copiare `registro.argomenti` nel registro elettronico. |
| US-D10 | Item con **id stabili** e domande tracing/perché per confrontare classi e migliorare i chunk. |

### Studente

| ID | Storia |
|----|--------|
| US-S1 | Corso completo su LiaScript senza clonare il repo del corso. |
| US-S2 | Lezione autonoma con link prev/next. |
| US-S3 | Accept assignment → repo già strutturato. |
| US-S4 | PRIMM + push con primo filtro automatico. |
| US-S5 | Segnalare visualizzazione (opt-in); offline non bloccato. |
| US-S6 | Compito cartaceo coerente con PRIMM e Classroom50. |

---

## 3. Architettura

```text
chapters/*.md
    → cipiupiu (core condiviso)
         ├─ build  → dist/README.md | dist/lessons/*
         ├─ print  → JSON → Typst → PDF  (worksheet | paper | registro)
         └─ scaffold-assignment → template GitHub + istruzioni
config classe YAML → scaffold-assignment
collect (Slice D) → download + validation_rules
```

### 3.1 CLI

`python -m tools.cipiupiu`

| Slice | Comandi | Stato |
|-------|---------|--------|
| A | `validate`, `list`, `render` | Operativa |
| B | `build` (timestamp) | Operativa |
| C | `scaffold-assignment` | Operativa v1 |
| D | `collect` | Previsto |
| E | `print` | Operativa (PDF se Typst in PATH o `.tools/typst`) |

- `index.md` → contenuti del **corso**; `order` → ordine e prev/next delle **lezioni**.
- `build` e `print` validano il frontmatter prima di emettere artefatti.
- Compat: `preprocess.py` ≈ `render`; `tools/validate_chapters.py` ≈ `validate`.

### 3.2 `course.yaml`

Metadati LiaScript globali e URL dev/prod. Scalari del capitolo sovrascrivono; `import` unito senza duplicati.

---

## 4. Frontmatter

- Schema: `schemas/chapter-frontmatter.schema.json` (v0.4+)
- Validazione: `python -m tools.cipiupiu validate [path…]`

### 4.1 Campi

**Required:** `activity_id`, `title`, `methodology` (`PRIMM`|`lab`|`guide`|`convention`), `order` (≥ 0).

**Opzionali:** `version`, `last_update`; metadati LiaScript (`author`, `email`, `language`, `narrator`, `comment`, `import`, `liascript_extra`).

**`components`** (PRIMM):
- `predict_quiz`: `{ question, code?, options: [{text, correct}] }` — **unica fonte** del quiz Predict
- `modify_instructions`, `make_instructions` (testo consegna; possono alimentare scaffold/print)
- `visualization?`: `{ kind: table|pythontutor|plantuml, note? }` (lint futuro)
- ~~`investigate_questions`~~ — **non usare** (rimosso dal contratto; vedi §4.2.1)

**`assignment_profile?`:** `full` | `code_only` | `none` (default implicito: vedi §4.2.2).

**`files[]`:** `path`, `action` (`create`|`reference`), `phase?`, `description?`,  
`template_content` **xor** `template_from` se `create`, `validation_rules?` (`min_lines`, `must_contain`).  
Per `phase: investigate` in profilo `full`, il contenuto del file risposta è una **proiezione** di `assessment.investigate.questions` (non una seconda redazione).

**`registro?`:** `argomenti`, `note` → testo registro elettronico (P3).

**`assessment?`:** verifica formale (P3). Vedi §4.4 e [`paper_pack.md`](paper_pack.md).  
**Investigate: unica fonte** = `assessment.investigate.questions`.

### 4.2 Regole generali

- Non-PRIMM: `components` vuoto/assente; `files` può essere `[]`.
- Path `create` univoci nel capitolo.
- Predict **unica fonte:** quiz solo in `components.predict_quiz`; nel corpo solo `[[ predict_block() ]]` sotto `#### 1. PREDICT`.
- Investigate **unica fonte:** solo `assessment.investigate.questions` (opzione A). Nessun elenco parallelo in `components`.
- Commenti `<!--#` … `#-->`: note autore/LLM, strippati dal preprocessore; non annidabili.

#### 4.2.1 Investigate — policy (opzione A)

| Artefatto | Fonte domande Investigate |
|-----------|---------------------------|
| Paper Pack (foglio + griglia) | `assessment.investigate.questions` (+ `context`, `typical_errors`, `points`) |
| Repo studente `phase: investigate` | **Proiezione** della stessa lista (template generato da scaffold/build helper) |
| Corpo LiaScript | Spiegazione / tabella / tracing — **non** ridichiarare le domande di consegna |

Regole:

1. È vietato mantenere un secondo elenco in `components.investigate_questions`.
2. Se `template_content` di un file `phase: investigate` è presente a mano, deve coincidere con `assessment.investigate.questions` (stesso ordine e testo). Preferire generazione automatica.
3. Il validate (evoluzione) segnala divergenza assessment vs template investigate, oppure assenza di `assessment.investigate.questions` su PRIMM con `assignment_profile: full` o con `assessment` presente.
4. Non è richiesta una macro `[[ investigate_block() ]]` in v1.

#### 4.2.2 `assignment_profile` e checklist `files[]`

Profili ammessi:

| Valore | Uso | `files[]` minimi (`action: create`) |
|--------|-----|-------------------------------------|
| `full` | Assignment Classroom50 completo PRIMM | Vedi checklist sotto |
| `code_only` | Solo Modify/Make in repo (risposte aperte solo su carta) | `modify` + `make` (path codice); README consigliato |
| `none` | Nessun repo studente (guide/lab/convention tipici) | `files: []` o assente |

Se `assignment_profile` è omesso:

- `methodology: PRIMM` → si assume `full` per validate rigoroso (warning se incompleto);
- altrimenti → `none`.

**Checklist minima — `assignment_profile: full`**

Obbligatori:

1. `README.md` — istruzioni PRIMM e path dei file (`action: create`, senza `phase` o `phase` assente)
2. `phase: predict` — file risposte (tipicamente `student_work/predict/answers.md`)
3. `phase: run` — file riflessione post-esecuzione
4. `phase: investigate` — file risposte; contenuto allineato a `assessment.investigate.questions`
5. `phase: modify` — uno o più file codice starter (+ `validation_rules` consigliate)
6. `phase: make` — uno o più file codice da completare/scrivere (+ `validation_rules` consigliate)

Inoltre per PRIMM `full`:

- `components.predict_quiz` presente
- `components.make_instructions` presente (o prompt Make solo in `assessment.make.prompt` se si documenta eccezione)
- `assessment.investigate.questions` non vuoto se è presente il blocco `assessment`

Anti-duplicazione:

- Non copiare il quiz Predict nel `template_content` di predict (riferimento: “rispondi al quiz in LiaScript / sul foglio”; eventuali domande aperte extra vanno solo in assessment se servono in verifica).
- Non riscrivere le domande Investigate nel corpo Markdown del capitolo.
- `modify_instructions` / `make_instructions` in `components` e `assessment.*.prompt` possono coesistere in transizione; a regime il prompt della verifica può specializzarsi (tempo chiuso) mentre `make_instructions` resta la consegna repo.

### 4.3 Qualità delle domande

| Priorità | Regola |
|----------|--------|
| Alta | Domande sul **perché** e **tracing** (stato), non solo output |
| Alta | **Id stabili** `{activity_id}/{phase}` (es. `ciao-mondo-01/predict`) |
| Media | **`context`**: spiegazione corretta in **griglia**, non sul foglio studente |
| Media | **A/B sostanziali** via `assessment.variants` (prompt/code/dati diversi) |
| Media | Su memoria/processo: almeno una visualizzazione (tabella, Python Tutor, plantUML) |

### 4.4 Assessment e Paper Pack (P3)

```yaml
assessment:
  duration_min: 50
  total_points: 10
  versions: ["A", "B"]
  predict: { points: 2, context: "..." }
  investigate: { points: 3, questions: [...], typical_errors: [...], context: "..." }
  modify: { points: 2, prompt: "...", typical_errors: [...], context: "..." }
  make: { points: 3, prompt: "...", must_include: [...], context: "..." }
  variants:
    B:
      predict: { prompt: "..." }   # override
      modify: { prompt: "..." }
```

`print --template paper` produce `pack.json` (**format_version 2**), `verifica_{A|B}.typ|pdf`, `griglia` (con context e risposte attese), `registro.txt`.

Coesione P1–P2–P3:

| Dato | P1 | P2 | P3 |
|------|----|----|-----|
| `activity_id` | nav | nome template | path output |
| `predict_quiz` | LiaScript | — | Predict verifica |
| `files` create | — | repo studente | starter Modify/Make |
| `assessment` / `registro` | — | — | verifica + griglia + registro |

### 4.5 Stampa (`print`)

Consumatore del frontmatter validato: **non** reinterpreta il Markdown didattico.

```bash
# Worksheet (esercizi)
python -m tools.cipiupiu print 03 --template worksheet --emit json,typ,pdf --out-dir output

# Paper Pack (verifica formale)
python -m tools.cipiupiu print 03 --template paper --emit json,typ,pdf --out-dir output

# Solo registro
python -m tools.cipiupiu print 03 --template registro --out-dir output
```

| Template | Output tipico |
|----------|----------------|
| `worksheet` / `exam` / `handout` | `compito_capNN_*.{json,typ,pdf}` — fasi predict/modify/make |
| `paper` | `paper/<activity_id>/` — A/B, griglia, registro, pack.json |
| `registro` | `registro_capNN.txt` |

PDF richiede Typst (`PATH` o `.tools/typst`). Lo stile `stile_compito.typ` è copiato in outdir; compile con `--root` = directory dell’artefatto.

### 4.6 Jinja e metadati LiaScript

| Tipo | Delimitatore |
|------|----------------|
| Espressione | `[[ ... ]]` |
| Blocco | `[% ... %]` |
| Commento | `[# ... #]` |

Macro: `[[ predict_block() ]]`, navigazione lezioni.  
Merge metadati: default `course.yaml` ← scalari capitolo; `import` unione ordinata senza duplicati. Frontmatter non compare nell’HTML LiaScript.

I file in `chapters/` non sono anteprime autonome: usare `dist/lessons/`.

---

## 5. Config compiti (per classe)

```yaml
classroom:
  org: "..."
  classroom_name: "..."
assignments:
  - activity_id: ciao-mondo-01
    template_repo_name: "cpp-ciao-mondo-template"  # opzionale
    title: "..."                                   # default: title capitolo
    deadline: "2026-12-01T23:59:00+01:00"         # opzionale
```

`scaffold-assignment`: solo `files[].action: create` → repo template + flag Template + istruzioni (assignment Classroom50 ancora manuale in v1).  
Contratto: [`docs/scaffold_assignment.md`](scaffold_assignment.md).

---

## 6. Template lezione

| File | Uso |
|------|-----|
| `docs/template_primm.md` | PRIMM (default) |
| `docs/template_lab.md` | Lab (es. toolchain) |
| `docs/template_guide.md` | Guide metodologiche |
| `docs/template_convention.md` | Convenzioni (es. Doxygen) |
| `docs/template_lezione.md` | Alias → PRIMM |

Scaffold: `scaffolds/`.

---

## 7. Roadmap

Piano di esecuzione vivo: [`docs/ROADMAP.md`](ROADMAP.md).


1. Schema + validate — fatto  
2. `render` / `build` — fatto  
3. `scaffold-assignment` — fatto v1  
4. `print` worksheet + Paper Pack v2 — fatto  
5. Assignment Classroom50 automatico (acceptance link) — C v1.1  
6. `collect` + validation_rules — D  
7. Tracking opt-in — Could  

---

## 8. Fuori scope v1

- Più capitoli in un assignment  
- Test I/O / test runner avanzati  
- UI web docente  
- Sostituzione di Classroom50  
- Tracking obbligatorio  

---

## 9. Riferimenti

| Risorsa | Path / URL |
|---------|------------|
| Schema | `schemas/chapter-frontmatter.schema.json` |
| CLI | `python -m tools.cipiupiu` |
| Prodotti | [`docs/products.md`](products.md) |
| Paper Pack | [`docs/paper_pack.md`](paper_pack.md) |
| Scaffold | [`docs/scaffold_assignment.md`](scaffold_assignment.md) |
| LiaScript | https://liascript.github.io/ |
| Classroom50 | https://classroom50.org |
| Typst | https://typst.app/ |


---

## 9. Migrazione — Investigate opzione A e `assignment_profile`

Obiettivo: una sola fonte per Investigate, meno testo duplicato, profili assignment espliciti.

### 9.1 Principio anti-duplicazione

| Contenuto | Dove vive | Dove non vive |
|-----------|-----------|---------------|
| Quiz Predict | `components.predict_quiz` + macro | Corpo MD, `files[]` predict |
| Domande Investigate | `assessment.investigate.questions` | `components`, corpo MD (come lista consegna) |
| Starter Modify/Make | `files[]` `template_content` / `template_from` | Duplicati nel corpo oltre agli esempi didattici |
| Consegna repo Make | `components.make_instructions` | — |
| Consegna verifica Make | `assessment.make.prompt` (può essere più chiusa) | Copia identica obbligatoria della consegna repo |

### 9.2 Fasi

**Fase 0 — SPEC e schema (questa revisione)**  
- Documentare policy A e checklist `full`.  
- Schema: aggiungere `assignment_profile`; deprecare `components.investigate_questions` (campo assente o `deprecated` in descrizione).  
- Nessuna rottura immediata dei capitoli esistenti.

**Fase 1 — Capitoli già `full` di fatto (02–03, 05–06, 08–13)**  
- Verificare che ogni `phase: investigate` rifletta `assessment.investigate.questions`.  
- Se il template diverte: **riscrivere il template** dalla lista assessment (non il contrario, salvo correzione didattica consapevole).  
- Rimuovere eventuali `components.investigate_questions` se presenti.  
- Impostare `assignment_profile: full` esplicito (opzionale ma consigliato).

**Fase 2 — Capitoli `code_only` o incompleti (07, 14, 15 al momento del audit)**  
- Scelta per capitolo:
  - **A:** portare a `full` aggiungendo predict/run/investigate answers (template investigate generato da assessment);
  - **B:** dichiarare `assignment_profile: code_only` e non pretendere i file risposta.  
- Preferire B se le risposte aperte restano solo sul Paper Pack.

**Fase 3 — Tooling**  
- `validate`:  
  - warning se PRIMM senza `assignment_profile` e `files` incompleti rispetto a `full`;  
  - errore se esistono sia `components.investigate_questions` sia `assessment.investigate.questions` e differiscono;  
  - errore/warning se template investigate non allineato (normalizzazione whitespace).  
- `scaffold-assignment`: se `phase: investigate` senza `template_content` (o con flag), generare markdown domande da assessment.  
- Opzionale: helper `cipiupiu sync-investigate` che riscrive i template investigate da assessment.

**Fase 4 — Pulizia**  
- Eliminare `investigate_questions` dallo schema e dai template lezione.  
- Documentare in `template_primm.md` solo assessment per Investigate.

### 9.3 Criteri di accettazione migrazione

1. Nessun capitolo in `chapters/` con `components.investigate_questions`.  
2. Ogni PRIMM con `assignment_profile: full` passa la checklist §4.2.2.  
3. `print --template paper` e scaffold non leggono altro che `assessment.investigate` per le domande Investigate.  
4. Audit manuale a campione: testo domande cartaceo = testo file repo investigate.

