# Migrazione: Investigate (opzione A) e `assignment_profile`

Riferimento normativo: `docs/SPEC.md` v0.7 §4.2.1, §4.2.2, §9.

## Perché

- Oggi le domande Investigate compaiono in `assessment` **e** spesso, con testo diverso, nei `template_content` dei file repo.
- `components.investigate_questions` non è usato in modo coerente e raddoppierebbe ancora la fonte.
- Alcuni capitoli PRIMM non hanno tutti i file `full` (solo Make/Modify): va dichiarato, non lasciato implicito.

## Policy target

1. **Unica fonte Investigate:** `assessment.investigate.questions`.
2. **Repo `phase: investigate`:** proiezione della stessa lista (stesso ordine/testo).
3. **`assignment_profile`:** `full` | `code_only` | `none`.

## Checklist `assignment_profile: full`

`action: create` minimi:

| # | Path tipico | phase |
|---|-------------|-------|
| 1 | `README.md` | — |
| 2 | `student_work/predict/answers.md` | predict |
| 3 | `student_work/run/answers.md` | run |
| 4 | `student_work/investigate/answers.md` | investigate |
| 5 | codice under `student_work/modify/` | modify |
| 6 | codice under `student_work/make/` | make |

Più: `components.predict_quiz`, `make_instructions`, `assessment.investigate.questions` se c’è assessment.

## Piano operativo

| Fase | Azione | Esito |
|------|--------|--------|
| 0 | Merge SPEC/schema/paper_pack | Contratto chiaro |
| 1 | Audit PRIMM 02–15: allinea template investigate → assessment (o genera) | Niente testi divergenti |
| 2 | 07 / 14 / 15: scegliere `full` o `code_only` e chiudere | Validate pulito |
| 3 | Tooling: validate + scaffold proiezione investigate | Meno copia manuale |
| 4 | Rimuovere deprecated da schema/template | Contratto stretto |

### Fase 1 — procedura per capitolo

```text
1. Apri assessment.investigate.questions (lista canonica).
2. Se esiste files[] phase investigate:
   - riscrivi template_content come elenco numerato di quelle domande + breve header;
   - non inventare domande solo nel file.
3. Se non esiste e profile è full: aggiungi il file proiettato.
4. Elimina components.investigate_questions se presente.
5. validate + print --template paper (smoke).
```

### Fase 2 — decisione 07, 14, 15

- Se le risposte predict/run/investigate restano **solo in verifica cartacea** → `assignment_profile: code_only` + files modify/make (+ README).
- Se lo studente deve consegnare anche le risposte nel repo → portare a `full`.

## Anti-duplicazione (riepilogo)

- Predict: solo `components.predict_quiz` + macro.
- Investigate: solo `assessment.investigate.questions` (+ proiezione file).
- Esempi nel corpo MD: restano didattici; non sono la consegna assignment.

