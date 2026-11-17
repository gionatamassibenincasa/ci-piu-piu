# Specifiche tooling – ci-piu-piu (v0.5)

Fonte di verità per preprocessor, frontmatter, template repository, configurazione compiti e integrazione Classroom50.

**Stato**: Slice A, B, C ed E operative; D previsto.
**Data**: 2026-11-16

---

## 1. Contesto e obiettivi

### 1.1 Contesto operativo

- Una classe alla volta (~15 studenti), due classi per anno scolastico.
- Organizzazione GitHub e classi Classroom50 già esistenti.
- Materiale didattico: capitoli modulari (`chapters/*.md`) con frontmatter YAML + corpo Markdown.
- Metodologia prevalente: **PRIMM**. Alcuni capitoli usano `lab`, `guide` o `convention`.
- Gli studenti **visualizzano** su LiaScript; non clonano il repository del corso.
- Il clone del repository di lavoro è gestito da Classroom50.
- Tooling docente: solo Python, configurazione esterna, segreti in `.env`.

### 1.2 Obiettivi v1

| ID | Obiettivo | Priorità | Stato |
|----|-----------|----------|--------|
| O1 | Schema frontmatter + template lezione | Must | Fatto |
| O2 | Template repo + istruzioni assignment Classroom50 (1 assignment = 1 capitolo) | Must | Fatto (v1 semi-automatica) |
| O3 | `dist/README.md` corso completo | Must | Fatto / in rifinitura |
| O4 | `dist/lessons/*.md` lezioni autonome con prev/next | Must | Fatto / in rifinitura |
| O5 | Post-scadenza: download repo + `validation_rules` base | Should | Previsto (Slice D) |
| O6 | Tracking visualizzazione opt-in | Could | Non iniziato |
| O7 | Compito PRIMM stampabile dal frontmatter validato | Must | Fatto (JSON / Typst; PDF con Typst) |

**Corso completo** = un unico Markdown amalgamato (`dist/README.md`) per la sequenza annuale.  
**Lezione autonoma** = un capitolo in `dist/lessons/`, con link prev/next, per recupero e link diretti.

### 1.3 Principi progettuali

- Due livelli di configurazione nettamente separati:
  - **Capitolo** (frontmatter) = autoconsistente.
  - **Config compiti per classe** = dipende dai capitoli.
- Un assignment Classroom50 = **un solo capitolo**.
- La stampa è un consumatore: legge soltanto il modello di capitolo già
  validato, come il build, e non interpreta di nuovo il Markdown.
- Preferire standard esistenti (YAML frontmatter, Jinja2, JSON Schema).
- Implementare prima i componenti a più alto rischio.
- `dist/` resta versionato in git (consumo diretto da LiaScript).

---

## 2. User Stories

### Docente

| ID | Storia |
|----|--------|
| US-D1 | Come docente, voglio creare un nuovo capitolo con frontmatter + corpo Markdown (template PRIMM/lab/guide/convention) e validarlo senza scrivere codice di tooling. |
| US-D2 | Come docente, voglio eseguire `python -m tools.cipiupiu validate` e ricevere errori chiari su schema, Predict e `files[]`. |
| US-D3 | Come docente, voglio eseguire `python -m tools.cipiupiu build` e ottenere `dist/README.md` + `dist/lessons/*` con header LiaScript e prev/next. |
| US-D4 | Come docente, voglio, da un file di configurazione della classe, generare il repository template (solo `action: create`) e ricevere le istruzioni per creare l’assignment Classroom50. |
| US-D5 | Come docente, voglio dopo la scadenza scaricare i repo studenti e applicare le `validation_rules` dichiarate, ottenendo un report leggibile. |
| US-D6 | Come docente, voglio generare lezioni in modalità `dev` o `prod` (URL di navigazione) senza modifiche manuali. |
| US-D7 | Come docente, voglio stampare Predict, Modify e Make di un capitolo (worksheet) senza duplicare consegne o soluzioni nel Markdown. |
| US-D8 | Come docente, voglio generare un **Paper Pack** (verifica A/B, griglia docente, testo registro) da un capitolo con `assessment` + `registro`, in JSON/Typst/PDF. |
| US-D9 | Come docente, voglio copiare `registro.argomenti` nel registro elettronico senza riscrivere a mano gli argomenti della lezione. |

### Studente

| ID | Storia |
|----|--------|
| US-S1 | Come studente, voglio aprire il corso completo su LiaScript e trovare materiale interattivo senza clonare il repo del corso. |
| US-S2 | Come studente, voglio aprire una lezione autonoma con link a precedente e successiva. |
| US-S3 | Come studente, voglio accettare l’assignment Classroom50 di un capitolo e ottenere un repository già strutturato con i file previsti. |
| US-S4 | Come studente, voglio svolgere Predict / Investigate / Modify / Make e fare push, sapendo che esiste un primo filtro automatico. |
| US-S5 | Come studente, voglio poter segnalare (opt-in, login GitHub) di aver visualizzato una lezione, senza obbligo e senza bloccare l’uso offline. |
| US-S6 | Come studente, voglio ricevere un compito cartaceo coerente con le consegne PRIMM e il repository Classroom50. |

---

## 3. Architettura e pipeline

```
chapters/*.md          ← sorgente (frontmatter YAML + Markdown)
        │
        ▼
tools/cipiupiu         ← unica CLI (core.py)
        │
        ├── dist/README.md              (corso completo, da index.md)
        └── dist/lessons/<order>_<slug>.md
        │
        ├── print ──→ modello JSON ──→ Typst ──→ PDF
        │
config compiti (YAML per classe)
        │
        ▼
scaffold-assignment    ← template repo (solo action=create) + istruzioni Classroom50
        │
        ▼
collect                ← download repo studenti + validation_rules
```

### 3.1 CLI `cipiupiu` (fonte unica)

Entrypoint: `python -m tools.cipiupiu`.

| Slice | Comandi | Stato |
|-------|---------|--------|
| A | `validate`, `list`, `render` | Operativa |
| B | `build` (course + lessons, invalidazione su timestamp) | Operativa |
| C | `scaffold-assignment` | Operativa (v1 semi-automatica) |
| D | `collect` | Previsto |
| E | `print` (modello JSON → Typst → PDF) | Operativa, PDF se Typst è installato |

Nucleo condiviso: `tools/cipiupiu/core.py`  
(`load_frontmatter` / `split_frontmatter`, `strip_author_blocks`, `render_jinja`, `expand_includes`, `render_file`, `iter_chapters`, `validate_chapter`).

Regole:
- `index.md` decide i capitoli del **corso completo**.
- `order` decide ordinamento e prev/next delle **lezioni singole**.
- `dist/` versionato in git.
- `build` e `print` validano il frontmatter con lo stesso validatore prima di
  produrre artefatti.

Compatibilità:
```bash
python preprocess.py index.md > README.md          # ≈ cipiupiu render index.md
python tools/validate_chapters.py chapters/05_….md # ≈ cipiupiu validate …
```

### 3.2 course.yaml

Configurazione globale del corso (metadati LiaScript, path, URL prod/dev).  
Usata da `build`. I campi scalari del capitolo sovrascrivono i default; `import` viene unito senza duplicati.

---

## 4. Frontmatter del capitolo

- Schema: `schemas/chapter-frontmatter.schema.json`
- Validazione: `python -m tools.cipiupiu validate [path…]`

### 4.0 Registro elettronico e Paper Pack

Campi opzionali del frontmatter (dettaglio in [`docs/paper_pack.md`](paper_pack.md)):

- `registro.argomenti` — testo per la sezione Argomenti/Contenuti del registro elettronico
- `registro.note` — note interne (tipo di prova, collegamento al compito digitale)
- `assessment` — verifica formale cartacea (punti, prompt Predict/Investigate/Modify/Make, versioni A/B, errori tipici)

Il profilo `print --template paper` genera fogli studente, griglia docente e `registro.txt`.
Il worksheet già supportato da Slice E resta disponibile; il Paper Pack è orientato alla **valutazione in classe**.

### 4.1 Campi principali

**Required**
- `activity_id` (string, pattern stabile)
- `title` (string)
- `methodology`: `PRIMM` | `lab` | `guide` | `convention`
- `order` (integer ≥ 0) — ordinamento canonico

**Opzionali di identità**
- `version`, `last_update`

**Metadati LiaScript (opzionali)**  
`author`, `email`, `language`, `narrator`, `comment`, `import` (array di URI), più eventuale `liascript_extra`.

**components** (oggetto, opzionale per non-PRIMM)
- `predict_quiz`: `{ question, code?, options[{text, correct}] }`
- `investigate_questions`: array di stringhe
- `modify_instructions`, `make_instructions` (stringhe, opzionali)

**files** (array, default `[]`)
- `path` (string, può essere gerarchico)
- `action`: `create` | `reference`
  - `create` → generato nel repository template studente
  - `reference` → solo supporto (es. codice da digitare a mano in Run); **non** entra nel repo
- `phase` (opzionale): `predict` | `run` | `investigate` | `modify` | `make`
- `description` (opzionale, può coesistere con `phase`)
- Per `action: create`: esattamente uno tra `template_from` e `template_content`
- `validation_rules` (opzionale): `min_lines`, `must_contain`

### 4.2 Regole

- Capitoli non-PRIMM: `components` assente/vuoto; `files` può essere `[]`.
- `phase` è opzionale (capitoli lab/guide/convention non devono forzarla).
- Path con `action: create` univoci all’interno del capitolo.
- `target` non usato in v1 (gli assignment li decide la config classe).

### 4.3 Predict: unica fonte di verità

Per i capitoli `methodology: PRIMM`:

1. Il quiz Predict vive in `components.predict_quiz`.
2. Nel corpo Markdown, sotto `#### 1. PREDICT`, compare solo `[[ predict_block() ]]`.
3. Non duplicare opzioni `[(X)]` a mano nel Predict.
4. `cipiupiu validate` verifica: heading PREDICT, presenza di `predict_quiz`, presenza della macro.

### 4.4 Commenti `<!--#` … `#-->`

Si mantengono. Sono note autore/LLM **non** destinate a LiaScript.  
Vengono eliminati interamente dal preprocessore. Non sono annidabili.  
Non sostituiscono il frontmatter.

---

### 4.5 Stampa degli esercizi PRIMM

Il comando `print` è un **consumatore** del frontmatter validato. Non esegue
parsing del corpo Markdown, non aggiunge chiavi e non modifica il capitolo.
Il JSON prodotto è il modello canonico, indipendente dall'adapter Typst.

```bash
python -m tools.cipiupiu print 03 \
  --template worksheet \
  --emit json,typ,pdf \
  --out-dir output
```

`chapter` può essere l'`order`, l'`activity_id` oppure il path del capitolo.
Le fasi stampabili iniziali e predefinite sono `predict`, `modify` e `make`;
si possono limitare, per esempio, con `--phases predict,make`. I template
supportati sono `worksheet`, `exam` e `handout`.

| Dato stampato | Nodo del contratto |
|---|---|
| Numero e titolo | `order`, `title` |
| Quiz Predict senza soluzione | `components.predict_quiz` (`correct` non entra nel modello) |
| Consegne Modify/Make | `components.*_instructions`, `files[].description` |
| Codice di partenza e requisiti | `files[].template_content`, `files[].validation_rules` |

Per il capitolo 03 e il template `worksheet` gli artefatti sono:

```text
output/compito_cap03_worksheet.json
output/compito_cap03_worksheet.typ
output/compito_cap03_worksheet.pdf
```

`--emit json,typ` non richiede dipendenze oltre a quelle Python del progetto.
Per `--emit pdf` deve essere disponibile il binario
[Typst](https://typst.app/) nel `PATH`; l'errore è esplicito se manca. Lo stile
condiviso è `tools/cipiupiu/templates/stile_compito.typ`; il file Typst
generato lo importa dal root del repository e viene compilato con
`typst compile --root`.

Punti, rubriche, righe di risposta personalizzate o esercizi strutturati oltre
Predict non sono dedotti dal Markdown. Richiedono una successiva estensione
versionata di `chapter-frontmatter.schema.json`, compatibile sia con
Classroom50 sia con questo exporter. Il guard-test
`tests/test_print_contract_guard.py` verifica che ogni percorso letto dal
printer sia dichiarato nello schema; una futura CI dovrà eseguirlo. Una
modifica dello schema deve quindi essere intenzionale e versionata.

### 4.6 Jinja nel corpo Markdown

Delimitatori che non collidono col C++:

| Tipo | Delimitatore |
|------|----------------|
| Variabile / macro | `[[ ... ]]` |
| Blocco | `[% ... %]` |
| Commento | `[# ... #]` |

Macro tipiche: `[[ predict_block() ]]`, `[[ nav_prev_next() ]]`.  
I quiz già scritti a mano con sintassi LiaScript restano validi.

I file in `chapters/` sono sorgenti Jinja e **non** sono anteprime LiaScript
autonome: una macro come `[[ predict_block() ]]` viene espansa solo dal render.
Per vedere una lezione nel DevServer usa il file generato in `dist/lessons/`, per
esempio:

```text
http://localhost:3000/liascript/index.html?http://localhost:3000/dist/lessons/03_ciao-mondo-01.md#4
```

### 4.7 Merge metadati LiaScript

1. Default globali (`course.yaml`)
2. Campi scalari del capitolo sovrascrivono
3. `import` = unione ordinata globali + capitolo, senza duplicati
4. Frontmatter **non** compare nell’output LiaScript (solo metadati espansi nel formato atteso dal player)

---

## 5. Configurazione dei compiti (per classe)

File YAML separato, uno per classe. Dipende dai capitoli; i capitoli non dipendono da esso.

**Campi minimi supportati**:

```yaml
classroom:                    # identificativo Classroom50 / org
  org: "..."
  classroom_name: "..."

assignments:
  - activity_id: ciao-mondo-01
    template_repo_name: "cpp-ciao-mondo-template"   # o generato
    title: "..."
    deadline: "2026-12-01T23:59:00+01:00"
    # eventuali istruzioni aggiuntive
```

Lo script `scaffold-assignment` legge questo file + i frontmatter dei capitoli indicati, crea il template repo (solo `files` con `action: create`) e prepara le istruzioni per creare l’assignment Classroom50.

### 5.1 `scaffold-assignment` v1

Contratto dettagliato: [`docs/scaffold_assignment.md`](scaffold_assignment.md).

```bash
python -m tools.cipiupiu scaffold-assignment \
  --config assignments/3sia-2026.yaml \
  --activity ciao-mondo-01
```

In alternativa, per un primo esperimento:

```bash
python -m tools.cipiupiu scaffold-assignment \
  --activity ciao-mondo-01 \
  --org MIO-ORG \
  --classroom 3sia
```

Il comando:

1. trova il capitolo tramite `activity_id` e richiede almeno un `files[].action: create`;
2. genera soltanto quei file in una directory temporanea, rifiutando percorsi non sicuri;
3. crea o aggiorna `{org}/cpp-{activity_id}-template` (oppure `template_repo_name` della config), quindi abilita il flag GitHub **Template repository**;
4. stampa URL del template, comando `gh teacher assignment add` e istruzioni web.

`title`, `slug` e `deadline` nell’elemento `assignments[]` sono opzionali. Il titolo
predefinito è quello del capitolo, lo slug è l'`activity_id` senza il suffisso numerico
finale e, senza scadenza, l'output usa il segnaposto
`YYYY-MM-DDTHH:MM:00+01:00`. La creazione effettiva dell'assignment e la restituzione
dell'acceptance link restano fuori da v1.

Precondizioni: `gh` installato e autenticato, diritti di creazione repository
nell'organizzazione. Se l'attività non esiste, non contiene `action: create`, la
configurazione è incompleta oppure un comando GitHub/Git fallisce, il comando termina
con un errore esplicito senza stampare istruzioni di successo.

Output previsto:

```text
Template repository creato: https://github.com/ORG/cpp-ciao-mondo-01-template
Flag 'Template repository' attivato.

A) CLI:
   gh teacher assignment add ORG 3sia ciao-mondo \
     --name "Il Primo Dialogo con la Macchina" \
     --template ORG/cpp-ciao-mondo-01-template \
     --due 2026-12-01T23:59:00+01:00

B) Web: classroom50.org → classroom → New assignment → scegli il template sopra.
```

---

## 6. Template lezione

| File | Uso |
|------|-----|
| `docs/template_lezione.md` | Alias / puntatore al template PRIMM |
| `docs/template_primm.md` | Lezioni PRIMM |
| `docs/template_lab.md` | Sessioni lab (es. toolchain) |
| `docs/template_guide.md` | Guide metodologiche |
| `docs/template_convention.md` | Convenzioni (es. Doxygen) |

Scaffold riutilizzabili per `template_from`: directory `scaffolds/`.

---

## 7. Ordine di implementazione (rischio decrescente)

1. **Schema frontmatter + validazione** — fatto
2. **Preprocessor core** (`render`, `build` course/lessons, prev/next, macro Predict) — Slice A operativa, Slice B in corso
3. **Esposizione `action: create` + generazione template repository** — fatto (Slice C v1)
4. **Stampa dal modello validato (JSON → Typst → PDF)** — fatto (Slice E v1)
5. **Creazione diretta assignment Classroom50 e acceptance link** — Slice C v1.1
6. **Collect + validation_rules di base** — Slice D
7. **Tracking opt-in** — Could

---

## 8. Fuori scope v1

- Più capitoli in un solo assignment
- Test I/O avanzati / test runner
- UI web dedicata lato docente
- Sostituzione di Classroom50
- Tracking obbligatorio della visualizzazione

---

## 9. Riferimenti

- LiaScript: https://liascript.github.io/
- Classroom50: https://classroom50.org / https://github.com/foundation50/classroom50
- Schema locale: `schemas/chapter-frontmatter.schema.json`
- Config corso: `course.yaml`
- CLI: `python -m tools.cipiupiu`
- Typst: https://typst.app/

## Riferimento Paper Pack

- [`docs/paper_pack.md`](paper_pack.md) — verifiche formali, griglia, testo registro elettronico
