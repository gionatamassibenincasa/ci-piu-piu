---
activity_id: "selection-sort-01"
title: "Riordinare le Carte: L'Algoritmo Selection Sort"
methodology: PRIMM
order: 21
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Se l'array è già ordinato, quanti confronti fa comunque il Selection Sort?"
    code: |
      int arr[5] = {1,2,3,4,5};
      // algoritmo selection sort
    options:
      - text: "Il numero di confronti è sempre lo stesso (n·(n‑1)/2)"
        correct: true
      - text: "Zero, poiché l'algoritmo riconosce l'array ordinato"
        correct: false
      - text: "n‑1 confronti"
        correct: false
      - text: "Dipende dalla presenza di duplicati"
        correct: false
  make_instructions: "Scenario SIA — Ordinamento del listino prezzi con Selection Sort"
files:
  - path: student_work/make/selection_sort.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Ordina un array di double in ordine crescente usando Selection Sort.
       */
      #include <iostream>

      void selectionSort(double arr[], int n) {
          // TODO: implementare algoritmo
      }

      int main() {
          double prezzi[5] = {250.0, 100.0, 150.0, 200.0, 50.0};
          selectionSort(prezzi, 5);
          // stampa risultato
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain: ["int main"]
---

## 🎯 Riordinare le Carte: L'Algoritmo Selection Sort

> "Un mazzo di carte sparso viene ordinato scegliendo il più piccolo e piazzandolo in prima posizione, ripetendo il processo."
>
> — *Metafora di ordinamento* 

### Obiettivo
- Implementare Selection Sort.
- Analizzare la sua complessità O(n²).
- Riconoscere che il numero di confronti è indipendente dallo stato iniziale dell'array.

---

## 📚 Teoria
1. Per ogni posizione `i` si cerca l'elemento minimo tra `i` e `n‑1`.
2. Si scambia il minimo trovato con `arr[i]`.
3. Il ciclo interno effettua `(n‑i‑1)` confronti; somma totale `n·(n‑1)/2`.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


[[ predict_block() ]]


<details><summary>💡 Spiegazione</summary>Selection Sort non verifica se l'array è già ordinato; continua a confrontare tutti gli elementi.
</details>

### Run
```cpp
/**
 * @file selection_sort.cpp
 * @brief Implementazione di Selection Sort per array di double.
 */
#include <iostream>
#include <iomanip>

void selectionSort(double arr[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        int minIdx = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIdx]) minIdx = j;
        }
        if (minIdx != i) std::swap(arr[i], arr[minIdx]);
    }
}

int main() {
    double prezzi[5] = {250.0, 100.0, 150.0, 200.0, 50.0};
    selectionSort(prezzi, 5);
    std::cout << std::fixed << std::setprecision(2);
    for (double p : prezzi) std::cout << p << " ";
    std::cout << "\n";
    return 0;
}
```
@LIA.cpp

### Investigate
Usa Python Tutor per osservare il ciclo interno e gli scambi.

### Modify
Aggiungi versione `void selectionSortDesc(double arr[], int n)` che ordina decrescente.

### Make
**Scenario SIA — Ordinamento del listino prezzi con Selection Sort**

Scrivi `selection_sort.cpp` con Doxygen (`@brief`, `@param`, `@return`). Il programma deve ordinare un array di prezzi e stamparli.

---

