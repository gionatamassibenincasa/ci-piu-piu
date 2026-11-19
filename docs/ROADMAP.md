# Roadmap di implementazione e revisione

**Progetto:** ci-piu-piu  
**Allineata a:** [`docs/SPEC.md`](SPEC.md) v0.6, [`docs/products.md`](products.md)  
**Criteri di priorità:** rischio decrescente, valore decrescente (P3 Paper Pack ≥ P2 Classroom50 ≥ P1 OER per il docente).

Questo file è il **piano di esecuzione** (cosa fare dopo).  
La SPEC resta il **contratto di prodotto**. Non duplicare qui i dettagli di schema/CLI.

**Stato aggiornato:** 2026-11-19

---

## Legenda

| Simbolo | Significato |
|---------|-------------|
| `[ ]` | Da fare |
| `[~]` | In corso |
| `[x]` | Fatto |
| P1 / P2 / P3 | OER online / Classroom50 / Paper Pack |

---

## Fase 0 — Stabilizzazione contratto Paper Pack

Chiudere i buchi che farebbero divergere i tre prodotti prima di allargare i contenuti.

| ID | Lavoro | Stato | Note |
|----|--------|-------|------|
| **0.1** | Smoke test regressione Paper Pack v2 | `[x]` 2026-11-19 | `tests/test_paper_pack_smoke.py` |
| **0.2** | Checklist autore in `docs/paper_pack.md` (id, context, variants B ≠ solo etichetta) | `[ ]` | |
| **0.3** | Cap. 03 golden sample: griglia leggibile, PDF se Typst disponibile | `[ ]` | Revisione umana del PDF/typ |

**Exit fase 0:** un test automatico fallisce se Paper Pack v2 regredisce; checklist e campione 03 usabili dal docente.

---

## Fase 1 — P3 Paper Pack “di produzione”

| ID | Lavoro | Stato |
|----|--------|-------|
| **1.0** | Allineamento sul **tipo di prova** (qualità/quantità domande) usando il primo assessment (cap. 03) come prototipo | `[ ]` **prossima dopo 0.x** |
| **1.1** | Scegliere 6–8 capitoli “verifica in classe” | `[ ]` |
| **1.2** | `registro` + `assessment` completo + variants B sostanziali | `[ ]` |
| **1.3** | Domande perché / tracing | `[ ]` |
| **1.4** | Visualizzazione memoria dove serve | `[ ]` |
| **1.5** | Revisione umana di una griglia stampata per capitolo | `[ ]` |

**Non in fase 1:** assessment su tutti i 36 capitoli.

---

## Fase 2 — P2 Classroom50 affidabile

| ID | Lavoro | Stato |
|----|--------|-------|
| 2.1 | Config classe versionata (`assignments/*.yaml`) | `[ ]` |
| 2.2 | Revisione `files[]` capitoli lab (path, scaffold, validation_rules) | `[ ]` |
| 2.3 | Rituale docente documentato (scaffold → Classroom50) | `[ ]` |
| 2.4 | Slice D `collect` base | `[ ]` alto rischio |
| 2.5 | Acceptance link automatico (C v1.1) | `[ ]` |

---

## Fase 3 — Qualità materiale P1 (OER)

| ID | Lavoro | Stato |
|----|--------|-------|
| 3.1 | Audit PRIMM capitoli 1–12 | `[ ]` |
| 3.2 | Audit 13–25 | `[ ]` |
| 3.3 | Audit 26–36 + rubrica progetto | `[ ]` |
| 3.4 | Smoke LiaScript su 2–3 lezioni | `[ ]` |
| 3.5 | Uniformare titoli / durata chunk | `[ ]` |

---

## Fase 4 — Rifinitura

| ID | Lavoro | Stato |
|----|--------|-------|
| 4.1 | Tipografia PDF | `[ ]` |
| 4.2 | Lint visualization su topic memoria | `[ ]` |
| 4.3 | Tracking opt-in | `[ ]` Could |
| 4.4 | Assessment capitoli fuori dal set fase 1 | `[ ]` |

---

## Sequenza operativa (iterazioni git am + push)

```text
0.1 smoke test          ← fatto in questa iterazione
0.2 checklist paper_pack
0.3 golden sample 03 (revisione artefatti)
1.0 review assessment 03 (tipo/qualità/quantità domande)  ← proposta utente
1.1 set capitoli verifica
1.2+ assessment a ondate
2.x Classroom50
3.x audit OER
4.x polish
```

---

## Già consegnato (riferimento)

- Slice A–C, E; Paper Pack v2 (id stabili, context, variants, format_version 2)
- SPEC v0.6, products.md, capitolo 03 con assessment di riferimento
- Blocchi lezioni 0–36 in catalogo

Aggiornare le caselle `[x]` / `[ ]` a ogni iterazione rilevante.
