# Quiz design (Predict / Investigate / Modify)

**Golden sample:** [`chapters/03_ciao_mondo.md`](../chapters/03_ciao_mondo.md) — vedi anche [`GOLDEN_SAMPLE.md`](GOLDEN_SAMPLE.md).

## Riferimenti

- Etichette semantiche (ruoli / pattern, termini IT UniBo): [`semantic_labels.md`](semantic_labels.md)

- Crichton & Krishnamurthi, *Profiling Programming Language Learning* (PACMPL OOPSLA 2024), https://doi.org/10.1145/3649812  
  Domande più discriminative = **concettuali** (perché non compila / perché questo comportamento), non solo riconoscimento sintattico.
- Quiz del [Rust Book](https://github.com/cognitive-engineering-lab/rust-book/tree/main/quizzes): MC con **distrattori da misconception**, tracing, `context` per la spiegazione.

## Allineamento PRIMM

| Fase | Quando | Tipo di domanda | Macro |
|------|--------|-----------------|-------|
| **Predict** | Prima del Run | Effetto, completezza, significato di un pezzo di sintassi | `[[ predict_block() ]]` |
| **Investigate** | Dopo il Run | *Perché* include/main/namespace, ordine di esecuzione, errori tipici | `[[ investigate_block() ]]` |
| **Modify** | Prima/durante le edit | Effetto di una modifica o *quale* modifica ottiene un risultato | `[[ modify_block() ]]` |

**Make** resta consegna aperta guidata (requisiti + scaffold), non un quinto blocco di 5 MC obbligatorie.

## Quantità

| Contesto | Target |
|----------|--------|
| Lezione OER completa (golden) | ~**5 + 5 + 5** (Predict / Investigate / Modify) |
| Chunk più corto | minimo **3 + 3 + 3**, stesso *tipo* di domanda |
| Paper Pack (verifica) | subset; durata tipica 10–15 min, non scaricare tutte le MC OER sul foglio |

## Schema frontmatter

```yaml
components:
  predict_quiz:
    code: |        # opzionale, condiviso
      …
    items:
      - question: "…"
        options:
          - text: "…"
            correct: true
          - text: "…"
            correct: false
  investigate_quiz: { code?: …, items: […] }
  modify_quiz: { code?: …, items: […] }
```

Legacy ammesso: una sola `question` + `options` a root (una MC). **Non** mettere tre domande testuali in un unico `question` con una sola risposta.

## Regole di qualità (checklist)

- [ ] Ogni item ha **esattamente un** focus cognitivo
- [ ] Almeno una domanda per fase è di tipo **perché** o **tracing**
- [ ] Distrattori = errori che uno studente di 3ª SIA farebbe davvero
- [ ] Nessun costrutto non ancora insegnato
- [ ] Predict non richiede di aver già eseguito; Investigate sì
- [ ] `python -m tools.cipiupiu validate` OK (ogni item ha `correct: true`)

## Esempi di formulazione

**Preferire**

> Perché serve `#include <iostream>` in questo programma?

**Evitare come unica domanda del blocco**

> Cosa stampa il programma? (senza alternativa concettuale)


## Ordine delle opzioni

In frontmatter l’ordine di `options` è libero (spesso la corretta è in cima per comodità d’autore).  
In **LiaScript** e nel **foglio studente** Paper Pack le opzioni vengono **rimescolate in modo deterministico** in fase di render (`shuffle_quiz_options`): la chiave è il flag `correct: true` / testo della risposta, **non** la posizione.
