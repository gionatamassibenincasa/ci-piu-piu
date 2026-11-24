# Prodotti – ci-piu-piu

**Stato:** allineato a SPEC v0.8 (2026-11-24)

Il corso non è un unico artefatto. Sono **prodotti** con consumatori diversi, generati dallo stesso modello di capitolo (`activity_id` + frontmatter + Markdown).

| ID | Prodotto | Consumatore principale | Valore percepito | Comando / output |
|----|----------|------------------------|------------------|------------------|
| **P1** | OER online | Studente (studio, recupero) | Alto per lo studente; bassa disponibilità a pagare come prodotto isolato | `build` → LiaScript (`dist/`) |
| **P2** | Classroom50 | Docente di **laboratorio** | Alto (consegne, clone, scadenze) | `scaffold-assignment` → template repo |
| **P3** | Paper Pack | Docente di **teoria / valutazione** | Molto alto dove servono verifiche scritte | `print --template paper` → PDF + griglia + registro |
| **P4** | Materiale docente | Docente; eventuale interlocutore editoriale | Alto (soluzioni, griglie estese, guida) | Non nel `build` studente; path riservati se presenti |

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

P4 non compare nel diagramma delle proiezioni pubbliche: è materiale di supporto (e, se si dialoga con un editore, parte del pack docente), non una quarta cartella parallela di lezioni.

La **coesione** non si ottiene duplicando file per prodotto, ma con:

1. **`activity_id`** come chiave primaria condivisa;
2. **frontmatter** come contratto dati (`components`, `files`, `assessment`, `registro`);
3. **item stabili** per Predict / Paper Pack;
4. generatori (`build`, `scaffold-assignment`, `print`) come *proiezioni* del modello.

---

## Modulo Fondamenti (`order` 0–15)

Unità di riferimento per completezza didattica e per eventuali interlocutori esterni (scuole, editori).

| Voce | Contenuto |
|------|-----------|
| **Cosa è** | Percorso lab di base in C++ (ambiente, programma minimo, I/O, selezione, cicli, formattazione essenziale), con PRIMM e verifiche allineabili |
| **Cosa non è** | Corso annuale completo, manuale universitario, piattaforma LMS dell’editore |
| **Prerequisiti** | PC in lab, toolchain C++ come nelle lezioni 0–1; account GitHub se si usa P2 |
| **Esiti attesi** | Studente scrive/compila programmi minimi, usa selezione e cicli su casi semplici di contesto lavorativo leggero, affronta una verifica PRIMM |

I capitoli oltre `order` 15 sono **estensione** del percorso scuola, non parte del perimetro Fondamenti finché `products.md` non viene aggiornato.

---

## Scopo editoriale (senza dossier)

Senza sostituire un pack editoriale dedicato, il repository si orienta così:

- **campione di qualità** = lezioni Fondamenti usabili in autonomia (P1) + compito (P2) + verifica (P3) sullo stesso `activity_id`;
- **linguaggio** dei capitoli campione: obiettivi osservabili, confini di lezione, scenari coerenti (gestionale / operatore), non metafore scollegate dall’indirizzo;
- **promesse sobrie**: modulo lab + valutazione, non “adozione di volume” né copertura di tutto il piano di studi.

Dettaglio normativo tooling: [`SPEC.md`](SPEC.md) §0 e §8.

---

## Decisione: separare le lezioni in directory per prodotto?

### Opzione A — Un file capitolo, tre proiezioni pubbliche (scelta adottata)

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

| Priorità | Regola | Dove si applica |
|----------|--------|-----------------|
| **Alta** | Domande sul **perché** e sullo **stato** (tracing), non solo sull’output | `components.predict_quiz`, `assessment.*`, Investigate |
| **Alta** | **ID stabili** per ogni item valutativo | `items[].id` / id derivato da `activity_id` + phase |
| **Media** | **`context`**: spiegazione della risposta corretta in griglia | `assessment.*.context` / `typical_errors` |
| **Media** | **A/B** con prompt e/o **dati diversi** | `assessment.versions` + `variants` |
| **Media** | Visualizzazione memoria/processo dove serve | corpo Investigate |

Dettaglio: `docs/SPEC.md` §4 e `docs/paper_pack.md`.
