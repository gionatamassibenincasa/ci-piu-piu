---
activity_id: "esempio-primm-01"
title: "[Titolo concreto]: [sottotitolo sul costrutto]"
methodology: PRIMM
order: 0
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "[Domanda di previsione]"
    code: |
      // snippet da osservare
    options:
      - text: "[sbagliata plausibile]"
        correct: false
      - text: "[corretta]"
        correct: true
      - text: "[sbagliata]"
        correct: false
  make_instructions: "[Scenario aziendale Make in una frase]"
registro:
  argomenti: >
    [1–4 frasi per il campo Argomenti del registro elettronico:
    costrutti trattati, contesto PRIMM del capitolo.]
  note: >
    [Opzionale: tipo di prova, collegamento al compito Classroom50.]
assessment:
  duration_min: 50
  total_points: 10
  versions: ["A", "B"]
  predict:
    points: 2
  investigate:
    points: 3
    questions:
      - "[Domanda investigate 1]"
      - "[Domanda investigate 2]"
    typical_errors:
      - "[Errore tipico da attendersi in correzione]"
  modify:
    points: 2
    prompt: >
      [Consegna Modify per la verifica in classe, distinta dal lavoro sul repo.]
  make:
    points: 3
    prompt: >
      [Consegna Make chiusa, valutabile in 15–20 minuti.]
    must_include:
      - "std::cout"
      - "return 0"

files:
  - path: README.md
    action: create
    description: Istruzioni PRIMM della consegna
    template_content: |
      # [Titolo attività]

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Scrivi le risposte nei file della fase corrispondente e fai push al termine.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict

      Rispondi prima di eseguire il codice.
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run

      Quale output hai osservato? Corrisponde alla previsione?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate

      Cosa spiega il comportamento del programma?
      >
  - path: student_work/modify/esercizio_modificato.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          std::cout << "[output iniziale]\n";
          return 0;
      }
  - path: student_work/make/esercizio.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>

      int main() {
          /// TODO: spiega il perché economico o logico di una scelta.
          // TODO: completa il programma
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain: ["int main"]
---

<!--
  Copia in chapters/XX_nome.md. Sostituisci i placeholder.
  Chunk 15–25 min. Vedi docs/SPEC.md, docs/primm.md, docs/quiz_liascript.md.

  Il comando `python -m tools.cipiupiu print` usa solo questo frontmatter
  validato: non legge di nuovo il Markdown. Le fasi predefinite stampabili sono
  predict, modify e make; usa `components.*_instructions` e i dati `files`
  della fase (description, template_content, validation_rules) come fonte.
  Per nuovi metadati di stampa, estendi prima lo schema in modo versionato e
  riusabile da Classroom50 e PDF.
-->

## 📌 [Titolo concreto]: [sottotitolo sul costrutto del linguaggio]

> "[Citazione breve]"  
> — *Autore*

[2–4 frasi di contesto. Tono "tu". Scenario aziendale.]

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- [Obiettivo unico e osservabile]

---

> 💡 **Metafora:**  
> [Analogia; mappa concetto ↔ immagine.]

---

### ⚙️ Prima del laboratorio: [mappa del concetto]

[Una slide breve di teoria. Presenta il vocabolario e le parti del costrutto che
servono per affrontare il Predict; usa una tabella, un diagramma o 5–8 righe.
Non anticipare la risposta del quiz.]

| Parte / parola | Idea pratica | Perché serve |
|----------------|--------------|--------------|
| `...` | ... | ... |

---

### 🧭 Prima del laboratorio: [sequenza o regola chiave]

[Seconda slide opzionale. Mostra il flusso di esecuzione, una regola sintattica
o una relazione causa-effetto necessaria al Predict.]

| Passo | Cosa accade |
|:-----:|-------------|
| 1 | ... |
| 2 | ... |

---

### 🔬 Laboratorio PRIMM: [Nome scenario]

[1–2 frasi di contesto obbligatorie sotto il titolo — evitano slide LiaScript vuote.]

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
[2–4 frasi sul perché — non duplicare le opzioni del quiz.]
</details>

#### 2. RUN (Esegui)
Digita il codice a mano, eseguilo e confronta l'output con la tua previsione.

```cpp
#include <iostream>

int main() {
    /// [Spiega il perché logico o economico dell'output.]
    std::cout << "[output]\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Passo di esecuzione | Valori / output osservati |
|---------------------|---------------------------|
| [Passo 1] | [Osservazione] |
| [Passo 2] | [Osservazione] |

| Riga / Costrutto | Cosa fa | A cosa serve |
|------------------|---------|--------------|
| `...` | ... | ... |

> 🔗 **Se il programma usa variabili o memoria:** aprilo in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva ogni passo.

#### 4. MODIFY (Modifica)
1. [Modifica semplice, poi ricompila.]
2. [Modifica intermedia, poi ricompila.]
3. [Modifica impegnativa con soli costrutti già visti, poi ricompila.]

Se introduci un errore intenzionale, mostra l'output del compilatore e spiega
come leggere riga e parola `error`.

<details>
<summary>💡 Scaffold di partenza per Modify</summary>

```cpp
#include <iostream>

int main() {
    std::cout << "[output iniziale]\n";
    return 0;
}
```

</details>

#### 5. MAKE (Crea)
**Scenario aziendale:** [problema piccolo e realistico]

**Requisiti:**
1. [3–5 requisiti osservabili.]
2. [Riusa solo costrutti già introdotti.]
3. [Documentazione Doxygen completa se il programma o una funzione supera ~15 righe.]

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>

int main() {
    /// TODO: spiega il perché economico o logico di una scelta.
    // TODO: completa il programma
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- [Punto 1]
- [Punto 2]

---

### ➡️ Prossimo chunk
[Anteprima del concetto successivo.]

<!--#
  Checklist: registro.argomenti e assessment se serve verifica cartacea;
   un obiettivo; metafora; 1–2 slide teoriche prima del laboratorio;
  Predict prima di Run;
  @LIA.cpp solo sul Run; tabella di traccia e Python Tutor se ci sono variabili;
  scaffold in Modify; Make aziendale; niente costrutti futuri.
#-->
