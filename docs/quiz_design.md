# Quiz design (Predict / Investigate / Modify)

Riferimenti:

- Crichton & Krishnamurthi, *Profiling Programming Language Learning* (OOPSLA 2024), https://doi.org/10.1145/3649812  
  Domande migliori = **concettuali** (perché non compila / perché questo output), non solo sintassi o sì/no.
- Quiz del [Rust Book](https://github.com/cognitive-engineering-lab/rust-book/tree/main/quizzes): MC con **distrattori da misconception**, tracing, context per la spiegazione.

## Allineamento PRIMM

| Fase | Tipo di domanda |
|------|-----------------|
| **Predict** | Prima del Run: effetto, completezza, significato di un pezzo di sintassi |
| **Investigate** | Dopo il Run: *perché* include/main/namespace, ordine di esecuzione, errori tipici |
| **Modify** | Effetto di una modifica o *quale* modifica ottiene un risultato |

## Schema

```yaml
components:
  predict_quiz: { code?: ..., items: [{ question, options: [{text, correct}] }] }
  investigate_quiz: { ... }
  modify_quiz: { ... }
```

Macro nel corpo: `[[ predict_block() ]]`, `[[ investigate_block() ]]`, `[[ modify_block() ]]`.
