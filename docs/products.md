# Tre prodotti, una sorgente

**Stato:** decisione architetturale (2026-11-18)

Il corso non è un unico artefatto. Sono **tre prodotti** con acquirenti e utilità diverse, generati dallo stesso modello di capitolo.

| Prodotto | Consumatore principale | Valore percepito | Comando / output |
|----------|------------------------|------------------|------------------|
| **P1 – OER online** | Studente (auto-studio, recupero assenze) | Alto per lo studente; **bassa disponibilità a pagare** come prodotto isolato | `build` → LiaScript (`dist/`) |
| **P2 – Classroom50** | Insegnante di **laboratorio** | **Alto** (risparmio tempo su consegne, clone, scadenze) | `scaffold-assignment` → template repo |
| **P3 – Paper Pack** | Insegnante di **teoria** | **Ancora più alto** in contesti con verifiche scritte | `print --template paper` → PDF + griglia + registro |
| **P4 - Materiale docente** | Insegnante | Alto: programmazione didattica, soluzioni, griglie di valutazione estese, guida docente | |

```text
                    ┌─────────────────────────┐
                    │  Modello capitolo       │
                    │  (activity_id stabile)  │
                    │  Markdown + frontmatter │
                    └───────────┬─────────────┘
            ┌───────────────────┼───────────────────┐
            ▼                   ▼                   ▼
     P1 OER online        P2 Classroom50      P3 Paper Pack
     (LiaScript)          (repo template)     (verifica A/B)
```

La **coesione** non si ottiene duplicando file per prodotto, ma con:

1. **`activity_id`** come chiave primaria condivisa;
2. **frontmatter** come contratto dati (components, files, assessment, registro);
3. **item stabili** (`items[].id`) per Predict / Paper Pack / analisi errori;
4. generatori (`build`, `scaffold-assignment`, `print`) come *proiezioni* del modello.

---

## Decisione: separare le lezioni in directory per prodotto?

### Opzione A — Un file capitolo, tre proiezioni (scelta adottata)

```text
chapters/03_ciao_mondo.md     # narrativo + frontmatter completo
dist/lessons/…                # P1
(template GitHub)             # P2 da files[]
output/paper/ciao-mondo-01/   # P3
```

| Pro | Contro |
|-----|--------|
| Una sola fonte di verità | Frontmatter può crescere |
| Impossibile disallineare obiettivi OER vs compito vs verifica | Serve disciplina YAML |
| `validate` unico | — |

### Opzione B — Directory separate (`lessons/`, `assignments/`, `paper/`)

| Pro | Contro |
|-----|--------|
| File più corti per ruolo | Rischio di divergenza obiettivi/lessico |
| Editor diversi per teoria vs lab | Doppia manutenzione; LLM e patch più fragili |

### Decisione

**Si resta sull’opzione A** (coesione per modello, non per cartelle prodotto).

Si **non** spezzano le lezioni in tre alberi paralleli. Eventuale alleggerimento futuro solo se il frontmatter supera una soglia di leggibilità, es.:

```text
chapters/03_ciao_mondo.md           # narrativo + meta minimi
chapters/03_ciao_mondo.assessment.yaml   # opzionale, merge in validate/print
```

con merge obbligatorio in `cipiupiu` e **stesso** `activity_id`. Non è richiesto in v1.

---

## Qualità delle domande (priorità alta/media)

Ispirato al profiling del [CEL rust-book](https://github.com/cognitive-engineering-lab/rust-book), senza importare la piattaforma mdBook.

| Priorità | Regola | Dove si applica |
|----------|--------|-----------------|
| **Alta** | Domande sul **perché** e sullo **stato** (tracing), non solo sull’output | `components.predict_quiz`, `assessment.*`, Investigate |
| **Alta** | **ID stabili** per ogni item valutativo | `items[].id` / `predict` id derivato da `activity_id` + phase + slot |
| **Media** | **`context`**: spiegazione della risposta corretta anche in griglia | `assessment.*.context` o `typical_errors` + risposta attesa |
| **Media** | **A/B** con prompt e/o **dati diversi** (non solo etichetta) | `assessment.versions` + `assessment.variants` |
| **Media** | **Checklist visualizzazione** memoria/processo | corpo PRIMM Investigate + opzionale `components.visualization` |

Dettaglio normativo: `docs/SPEC.md` §4.1–4.3 e `docs/paper_pack.md`.
