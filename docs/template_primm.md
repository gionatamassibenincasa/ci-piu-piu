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
  make_instructions: "[Scenario Make in una frase]"
files:
  - path: student_work/make/esercizio.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      int main() {
          // TODO
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain: ["int main"]
---

<!--
  Copia in chapters/XX_nome.md. Sostituisci i placeholder.
  Chunk 15–25 min. Vedi docs/SPEC.md, docs/primm.md, docs/quiz_liascript.md.
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

### 💡 La Metafora Guida

> 💡 **Metafora:**  
> [Analogia; mappa concetto ↔ immagine.]

---

### ⚙️ [Concetto in breve]

[Tabella o 5–10 righe essenziali.]

### ⚠️ Tranelli tipici
- [Errore classico]

---

### 🔬 Laboratorio PRIMM: [Nome scenario]

[1–2 frasi di contesto obbligatorie sotto il titolo — evitano slide LiaScript vuote.]

**Codice da osservare (senza `@LIA.cpp`):**

```cpp
// snippet Predict
```

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
[2–4 frasi sul perché — non duplicare le opzioni del quiz.]
</details>

#### 2. RUN (Esegui)
Esegui il codice e premi **Run**.

```cpp
/**
 * @file esempio.cpp
 * @brief [breve]
 */
#include <iostream>

int main() {
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Riga / Costrutto | Cosa fa | A cosa serve |
|------------------|---------|--------------|
| `...` | ... | ... |

> 🔗 [Python Tutor C++](https://pythontutor.com/cpp.html)

#### 4. MODIFY (Modifica)
1. [Modifica semplice]
2. [Modifica media]
3. [Modifica impegnativa — solo costrutti già visti]

#### 5. MAKE (Crea)
**Scenario aziendale:** [problema piccolo e realistico]

**Requisiti:**
- [ ]
- Documentazione Doxygen se > ~15 righe

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    // TODO
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
  Checklist: un obiettivo; metafora; Predict prima di Run;
  lab con testo sotto ###; @LIA.cpp solo sul Run; niente costrutti futuri.
#-->
