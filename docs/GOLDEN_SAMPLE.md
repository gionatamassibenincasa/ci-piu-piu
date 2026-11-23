# Golden sample

**Capitolo di riferimento:** [`chapters/03_ciao_mondo.md`](../chapters/03_ciao_mondo.md)  
**activity_id:** `ciao-mondo-01`  
**Commit di fissaggio (orientativo):** branch `main` post-quiz concettuali 5+5+5 (nov 2026).

Questo file è lo **standard di qualità** per:

1. struttura della lezione PRIMM (OER LiaScript);
2. tipo e qualità delle domande (Predict / Investigate / Modify);
3. coerenza frontmatter → macro `[[ *_block() ]]` → Paper Pack / Classroom50.

## Cosa copiare dal golden sample

| Elemento | Standard |
|----------|----------|
| Titolo | Concreto + costrutto; **niente** “Capitolo N” |
| Metafora | Box `> 💡 **Metafora:**` con mapping esplicito |
| Obiettivo | **Uno** osservabile |
| Prima del lab | Tabelle brevi (parti del linguaggio + flusso) |
| Predict | `components.predict_quiz.items[]` (~5), MC, *prima* del Run |
| Run | Programma completo + `@LIA.cpp` |
| Investigate | `investigate_quiz.items[]` (~5), *perché* / ordine / errori |
| Modify | `modify_quiz.items[]` (~5) sull’effetto della modifica, poi edit guidati |
| Make | Scenario SIA, requisiti chiusi, scaffold in `<details>` |
| Registro / assessment | Presenti se c’è verifica o compito |

## Etichette semantiche (progressivo)

Da variabili/cicli/funzioni in poi, le domande possono usare i **ruoli** e i **pattern di ciclo** in italiano ([`semantic_labels.md`](semantic_labels.md), fonti [UniBo CSEd](https://csed-unibo.github.io/#!pages/ruoli_variabili.md)).  
Il golden sample 03 non le richiede (ancora niente cicli/parametri).

## Qualità delle domande (obbligatoria)

Vedi [`quiz_design.md`](quiz_design.md). Sintesi:

- Preferire **perché** e **tracing** a “cosa stampa?” isolato.
- Ogni MC ha **distrattori da misconception** reali, non assurdità.
- Una domanda = un’idea cognitiva (non tre domande in un unico testo con una sola risposta).
- Predict ≠ Investigate: prima del Run vs dopo il Run.
- Modify quiz ≠ Make: effetto di un cambiamento vs creare da zero.

## Come revisionare un capitolo in `chapters/`

1. `python -m tools.cipiupiu validate chapters/NN_….md`
2. Confrontare struttura e quiz con `03_ciao_mondo.md` e `template_primm.md`
3. Controllare checklist in coda a `template_primm.md` e in `SKILLS.md`
4. Solo dopo: `build lessons` / Paper Pack

## Cosa non è golden sample

- `00` guida di studio e `01` ambiente: methodology diversa (`guide` / `lab`); non forzare PRIMM 5+5+5.
- Capitoli molto corti: si può scendere a 3+3+3 **mantenendo** il tipo di domanda.

## Aggiornare lo standard

Se il golden sample cambia in modo sostanziale, aggiornare **nella stessa PR**:

- questo file;
- `docs/template_primm.md`;
- `docs/quiz_design.md`;
- eventuale nota in `SKILLS.md`.
