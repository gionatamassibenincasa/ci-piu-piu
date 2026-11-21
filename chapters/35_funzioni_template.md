---
activity_id: "template-fun-01"
title: "Stessa procedura, tipi diversi: funzioni template"
methodology: PRIMM
order: 35
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Una funzione `template <typename T> T massimo(T a, T b)` può essere usata su `int` e su `double`?"
    code: |
      massimo(3, 5);
      massimo(2.5, 2.7);
    options:
      - text: "Sì, il compilatore istanzia le versioni necessarie"
        correct: true
      - text: "No, solo su int"
        correct: false
      - text: "Solo se T è class"
        correct: false
      - text: "No, serve virtual"
        correct: false
files:
  - path: student_work/make/util_template.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      int main() { return 0; }
    validation_rules:
      min_lines: 12
      must_contain:
      - "template"
---


## 🔧 Stessa procedura, tipi diversi: funzioni template

> "Il confronto ‘chi è maggiore’ vale per pezzi e per prezzi."  
> — *Riuso algoritmico*

Una **funzione template** descrive un algoritmo **generico**: il compilatore genera le versioni per i tipi usati.

> 💡 **Metafora:** modulo aziendale standard compilato per reparti diversi (stessa procedura, dati diversi).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una funzione `template <typename T>` semplice
- Usarla con tipi diversi (`int`, `double`)

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
Il compilatore crea istanze distinte di <code>massimo</code> per i tipi dedotti dagli argomenti.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file massimo_template.cpp
 * @brief Funzione template massimo.
 */
#include <iostream>

template <typename T>
T massimo(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << massimo(3, 5) << '\n';
    std::cout << massimo(2.5, 2.7) << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Chiamata | T dedotto |
|----------|-----------|
| `massimo(3, 5)` | `int` |
| `massimo(2.5, 2.7)` | `double` |

I tipi devono supportare `>`.

#### 4. MODIFY (Modifica)
1. Scrivi `template <typename T> void scambia(T& a, T& b)`.
2. Usa `scambia` su due `double`.
3. Prova `massimo` su due `char`.

#### 5. MAKE (Crea)
**Scenario SIA — Utility generiche**

`util_template.cpp`: `massimo` e `scambia` template; demo su quantità (`int`) e prezzi (`double`).

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
template <typename T>
T massimo(T a, T b) { /* ... */ }
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Template = algoritmo generico
- Istanziazione a compile-time
- T deve offrire le operazioni usate
- Non è magia runtime: è generazione di codice

---

### ➡️ Prossimo chunk
Usare un contenitore template della libreria: `std::vector`.
