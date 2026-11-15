# Interfaccia `scaffold-assignment` (v1)

Comando CLI che prepara il **repository template GitHub** usato da Classroom50  
per **un’attività = un capitolo** (`activity_id`).

Implementazione: `tools/cipiupiu/assignments.py`  
Entrypoint: `python -m tools.cipiupiu scaffold-assignment`

---

## Scopo

| Fa | Non fa (v1) |
|----|-------------|
| Legge il capitolo tramite `activity_id` | Creare l’assignment Classroom50 via API |
| Materializza solo `files[]` con `action: create` | Generare acceptance link |
| Crea o aggiorna `{org}/{template_repo}` su GitHub | Validare i repo degli studenti (`collect`) |
| Imposta il flag **Template repository** | Aggregare più capitoli in un assignment |
| Stampa istruzioni CLI/web per Classroom50 | Eseguire test I/O sul codice studente |

---

## Sintassi

```bash
python -m tools.cipiupiu scaffold-assignment \
  --activity ACTIVITY_ID \
  [--config PATH.yaml] \
  [--org GITHUB_ORG] \
  [--classroom "NOME CLASSROOM"] \
  [--chapters DIR]
```

### Argomenti

| Flag | Required | Descrizione |
|------|----------|-------------|
| `--activity` | **Sì** | `activity_id` del frontmatter (es. `ciao-mondo-01`) |
| `--config` | No | YAML di classe (`assignments/…yaml`). Se presente, cerca l’entry con lo stesso `activity_id` |
| `--org` | Cond. | Organizzazione GitHub. Obbligatorio se assente in config |
| `--classroom` | Cond. | Nome/id classroom Classroom50. Obbligatorio se assente in config |
| `--chapters` | No | Directory capitoli (default: `chapters/`) |

**Risoluzione org / classroom:** CLI vince sulla config; almeno una delle due fonti deve fornire entrambi i valori.

```text
org       = --org       OR config.classroom.org
classroom = --classroom OR config.classroom.classroom_name
```

### Esempi

Solo CLI (esperimento rapido):

```bash
python -m tools.cipiupiu scaffold-assignment \
  --activity ciao-mondo-01 \
  --org dip-inf-savoia-benincasa \
  --classroom "26-27 3A SIA"
```

Con config di classe (uso quotidiano):

```bash
python -m tools.cipiupiu scaffold-assignment \
  --config assignments/3sia-2026.yaml \
  --activity ciao-mondo-01
```

---

## Input: capitolo (`activity_id`)

1. Cerca in `chapters/*.md` un frontmatter con `activity_id` uguale a `--activity`.
2. Deve esistere **almeno un** elemento in `files` con `action: create`.
3. Per ogni `create`:
   - `path` — percorso relativo nel repo studente (vietati `..`, path assoluti)
   - esattamente uno tra `template_content` (inline) e `template_from` (file sotto la root del progetto, es. `scaffolds/…`)

`action: reference` è **ignorato** (solo supporto didattico, non finisce nel template).

---

## Input: config YAML (opzionale)

Schema minimo:

```yaml
classroom:
  org: dip-inf-savoia-benincasa
  classroom_name: "26-27 3A SIA"

assignments:
  - activity_id: ciao-mondo-01
    template_repo_name: cpp-ciao-mondo-template   # opzionale
    title: "Il Primo Dialogo con la Macchina"    # opzionale
    slug: ciao-mondo                             # opzionale
    deadline: "2026-12-01T23:59:00+01:00"        # opzionale, ISO-8601
```

| Campo assignment | Default se omesso |
|------------------|-------------------|
| `template_repo_name` | `cpp-{activity_id}-template` |
| `title` | `title` del capitolo |
| `slug` | `activity_id` senza suffisso numerico finale (`ciao-mondo-01` → `ciao-mondo`) |
| `deadline` | placeholder `YYYY-MM-DDTHH:MM:00+01:00` nelle istruzioni stampate |

`template_repo_name` deve essere **solo il nome** del repo (niente `org/`).

---

## Comportamento passo-passo

1. **Resolve** capitolo e `AssignmentOptions`.
2. **Staging** in directory temporanea: scrive i file `create`.
3. **GitHub**
   - se `{org}/{template_repo}` non esiste → `gh repo create … --private` (o policy corrente dello script)
   - clone / sync del contenuto
   - commit se ci sono differenze (`Aggiorna scaffold attività`)
   - push su `origin`
   - attiva il flag **template repository** via API GitHub
4. **Stdout** con URL del template e istruzioni per creare l’assignment (manuale in v1).

Idempotenza: rieseguire lo stesso comando **aggiorna** i file del template se il frontmatter è cambiato; se non ci sono diff, non crea commit inutili.

---

## Output previsto (successo)

```text
Template repository creato: https://github.com/ORG/cpp-ciao-mondo-01-template
Flag 'Template repository' attivato.

A) CLI:
   gh teacher assignment add ORG "26-27 3A SIA" ciao-mondo \
     --name "…" \
     --template ORG/cpp-ciao-mondo-01-template \
     --due 2026-12-01T23:59:00+01:00

B) Web: classroom50.org → classroom → New assignment → scegli il template sopra.
```

(Il testo esatto può variare leggermente; URL e nomi repo sono la parte stabile del contratto.)

---

## Precondizioni

- `gh` installato e autenticato (`gh auth status`)
- Permessi di creazione repository sull’organizzazione
- Rete verso GitHub
- Capitolo valido con almeno un `files[].action: create`

---

## Errori (exit ≠ 0, messaggio su stderr)

| Situazione | Effetto |
|------------|---------|
| `activity_id` assente | errore |
| Nessun `action: create` | errore |
| `--org` / `--classroom` mancanti e config incompleta | errore |
| `template_from` inesistente o fuori root | errore |
| `path` non sicuro (`..`, assoluto) | errore |
| Fallimento `gh` / `git` | errore, senza istruzioni di successo |

---

## Contratto con Classroom50

```text
[capitolo frontmatter files create]
        │
        ▼
scaffold-assignment ──► repo template GitHub (flag template)
        │
        ▼  (manuale v1)
Classroom50 assignment ──► repo per studente (accept link)
```

Un assignment Classroom50 punta a **un** template; un template deriva da **un** `activity_id`.

---

## Fuori scope / roadmap

| Versione | Contenuto |
|----------|-----------|
| **v1** (attuale) | Template repo + istruzioni |
| **v1.1** | Creazione assignment + acceptance link se l’API/`gh teacher` lo consente in modo stabile |
| **v2** | `collect` post-scadenza + `validation_rules` |

Vedi anche `docs/SPEC.md` §5 e §5.1.
