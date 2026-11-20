---
activity_id: "esempio-primm-01"
title: "[Titolo concreto]: [sottotitolo sul costrutto del linguaggio]"
methodology: PRIMM
order: 0
version: "2026-11-20"
language: it
components:
  # --- Quiz OER (LiaScript): standard golden sample chapters/03_ciao_mondo.md ---
  # Preferire items[]: una voce = una domanda MC + option corrette/distrattori.
  # Target qualitativo: ~5 Predict + ~5 Investigate + ~5 Modify (adattare se il chunk è più corto).
  predict_quiz:
    code: |
      // Frammento osservato PRIMA del Run (opzionale se ogni item ha il suo code)
    items:
      - question: "[Concettuale: effetto / completezza / perché una forma è sbagliata]"
        options:
          - text: "[Corretta: spiega il comportamento o il vincolo]"
            correct: true
          - text: "[Distrattore da misconception tipica]"
            correct: false
          - text: "[Distrattore plausibile ma falso]"
            correct: false
      - question: "[Seconda domanda Predict…]"
        options:
          - text: "[…]"
            correct: true
          - text: "[…]"
            correct: false
          - text: "[…]"
            correct: false
  investigate_quiz:
    code: |
      // Programma completo già eseguito (dopo Run)
    items:
      - question: "[Perché X? / Quale ordine di esecuzione? / Perché questo errore?]"
        options:
          - text: "[Corretta, concettuale]"
            correct: true
          - text: "[Misconception]"
            correct: false
          - text: "[Misconception]"
            correct: false
  modify_quiz:
    code: |
      // Stesso programma di partenza del Modify
    items:
      - question: "[Effetto di una modifica / quale modifica ottiene Y / perché una alla volta]"
        options:
          - text: "[Corretta]"
            correct: true
          - text: "[Sbagliata plausibile]"
            correct: false
          - text: "[Sbagliata plausibile]"
            correct: false
  make_instructions: >
    [Scenario aziendale Make in una frase; requisiti osservabili.]
  visualization:
    kind: pythontutor
    note: "[Cosa osservare in memoria/flusso, se rilevante]"
registro:
  argomenti: >
    [1–4 frasi per il registro elettronico: costrutti + contesto PRIMM.]
  note: >
    [Opzionale: tipo di prova, collegamento Classroom50.]
assessment:
  # Verifica cartacea: più leggera dell'OER (non tutte le MC del corso).
  duration_min: 15
  total_points: 6
  versions: ["A", "B"]
  predict:
    points: 2
    context: "[Spiegazione sintetica per la griglia docente]"
  investigate:
    points: 2
    questions:
      - "[Allineata alle domande investigate_quiz o subset]"
    typical_errors:
      - "[Errore d'aula reale]"
    context: "[Per la griglia]"
  modify:
    points: 1
    prompt: >
      [Consegna Modify sul foglio: listato con righe libere se serve scrivere a mano.]
    code: |
      // Opzionale: codice con spazi per la scrittura a mano (override scaffold Classroom)
    typical_errors:
      - "[…]"
    context: "[…]"
  make:
    points: 1
    prompt: >
      [Make chiuso, 10–15 min, requisiti osservabili.]
    code: ""
    typical_errors:
      - "[…]"
    context: "[…]"
  variants:
    B:
      modify:
        prompt: "[Stessi obiettivi, letterali/scenario leggermente diversi]"
files:
  - path: README.md
    action: create
    description: Istruzioni PRIMM della consegna
    template_content: |
      # [Titolo attività]

      Ordine: Predict → Run → Investigate → Modify → Make.
      Scrivi nelle cartelle di fase e fai push al termine.
  - path: student_work/modify/esercizio_modificato.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          // TODO: modifica richiesta
          return 0;
      }
  - path: student_work/make/esercizio.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>

      int main() {
          /// TODO: spiega il perché (non il cosa)
          // TODO: implementazione
          return 0;
      }
---

<!--
  GOLDEN SAMPLE: chapters/03_ciao_mondo.md (activity_id ciao-mondo-01)
  Riferimenti obbligatori:
  - docs/quiz_design.md     (tipo e qualità delle domande)
  - docs/primm.md
  - docs/chunking.md
  - docs/head_first_style.md
  - docs/GOLDEN_SAMPLE.md
  - SKILLS.md
  Validazione: python -m tools.cipiupiu validate chapters/XX.md
-->

## 💬 [Titolo concreto]: `[costrutto]`

> "[Citazione breve, pertinente, verificata]"
>
> — *Autore riconoscibile (informatica / didattica)*

[2–4 frasi: collega a ciò che lo studente già sa e a uno scenario SIA. Tono "tu".]

> 💡 **Metafora:**  
> [Analogia concreta. Esplicita *cosa corrisponde a cosa*.]

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- [Un solo obiettivo osservabile sul costrutto principale]

---

### ⚙️ Prima del laboratorio: [concetti essenziali]

[Tabella o elenco breve: pezzi del linguaggio *prima* del codice completo.
Niente muro di testo: max 1 schermo.]

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| `…` | … | … |

---

### 🧭 Prima del laboratorio: [flusso / traccia]

[Ordine di esecuzione o stato, se utile al Predict.]

---

### 🔬 Laboratorio PRIMM: [nome scenario]

```cpp
// Programma di riferimento del laboratorio (completo, compilabile)
```

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

[Istruzioni minime: confronta output e previsione.]

```cpp
/**
 * @brief [Perché esiste questo programma, non parafrasi del codice]
 */
#include <iostream>

int main() {
    /// [Perché, non cosa]
    // …
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

Dopo il Run: domande sul *perché* e sull'ordine, non solo “cosa stampa”.

[[ investigate_block() ]]

[Tabella di traccia e/o `@PythonTutor.cpp` se c'è stato di memoria.]

| Codice | Cosa fa (brain-friendly) | A cosa serve |
| :--- | :--- | :--- |
| `…` | … | … |

#### 4. MODIFY (Modifica)

Prima le MC sull'effetto di una modifica; poi **una modifica alla volta** sul codice.

[[ modify_block() ]]

**Modifica A — …**  
[Consegna breve]

**Modifica B — …**

#### 5. MAKE (Crea)

**Scenario aziendale:** [SIA, diverso dallo snippet di Run.]

**Requisiti** (osservabili, chiusi):

1. …
2. …

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    /// TODO: perché
    // TODO: …
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- [3–6 bullet, incluso un tranello tipico]

---

### ➡️ Prossimo chunk

[Anteprima motivante del concetto successivo.]

<!--#
  Checklist autore / LLM (golden sample = chapters/03_ciao_mondo.md)
  [ ] Un solo obiettivo (chunking)
  [ ] Metafora esplicita
  [ ] predict_quiz.items ~5, concettuali, distrattori da misconception (quiz_design.md)
  [ ] investigate_quiz.items ~5, perché / tracing
  [ ] modify_quiz.items ~5, effetto della modifica
  [ ] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [ ] Run con @LIA.cpp; codice che termina
  [ ] Make con scenario SIA + requisiti + scaffold
  [ ] Commenti /// solo sul perché
  [ ] validate OK
#-->
