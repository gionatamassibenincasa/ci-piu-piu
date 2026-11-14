---
activity_id: "ricerca-01"
title: "Il Dizionario Magico: La Ricerca Dicotomica (Binaria)"
methodology: PRIMM
order: 20
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Se l'array ha 1.024 elementi ordinati, quanti passi al massimo servono per trovare un valore con ricerca binaria?"
    code: |
      // array di 1024 elementi ordinati
      // ricerca binaria di un valore
    options:
      - text: "10"
        correct: true
      - text: "9"
        correct: false
      - text: "11"
        correct: false
      - text: "12"
        correct: false
  make_instructions: "Scenario SIA — Ricerca istantanea del prezzo di un articolo in un catalogo ordinato"
files:
  - path: student_work/make/ricerca_binaria.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Implementa ricerca binaria su array ordinato di double.
       */
      #include <iostream>

      int ricercaBinaria(const double arr[], int n, double target) {
          // TODO: implementare algoritmo
          return -1;
      }

      int main() {
          // esempio di uso
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain: ["int main"]
---

## 🎯 Il Dizionario Magico: La Ricerca Dicotomica (Binaria)

> "Il dizionario è un elenco ordinato: trovare una voce è una ricerca binaria."
>
> — *Metafora di ricerca*

### Obiettivo
- Comprendere i requisiti di un array ordinato.
- Implementare l'algoritmo di ricerca binaria (indice iniziale, finale, medio).
- Analizzare la complessità O(log n).

---

## 📚 Teoria
1. L'array deve essere **ordinato**.
2. Algoritmo: confronta `target` con elemento medio, riduce intervallo a metà.
3. Convergenza quando `inizio > fine` → valore non trovato.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


[[ predict_block() ]]


<details><summary>💡 Spiegazione</summary>2¹⁰ = 1024, quindi al massimo 10 confronti.
</details>

### Run
```cpp
/**
 * @file ricerca_binaria.cpp
 * @brief Ricerca binaria su array ordinato.
 */
#include <iostream>

int ricercaBinaria(const double arr[], int n, double target) {
    int inizio = 0, fine = n - 1;
    while (inizio <= fine) {
        int medio = (inizio + fine) / 2;
        if (arr[medio] == target) return medio;
        if (arr[medio] < target) inizio = medio + 1;
        else fine = medio - 1;
    }
    return -1; // non trovato
}

int main() {
    double dati[5] = {10, 20, 30, 40, 50};
    int idx = ricercaBinaria(dati, 5, 30);
    std::cout << "Indice: " << idx << std::endl;
    return 0;
}
```
@LIA.cpp

### Investigate
Visualizza con Python Tutor l'aggiornamento di `inizio` e `fine` ad ogni iterazione.

### Modify
Aggiungi parametro `bool verbose` per stampare i passi eseguiti.

### Make
**Scenario SIA — Ricerca istantanea del prezzo di un articolo in un catalogo ordinato**

Scrivi `ricerca_binaria.cpp` con Doxygen (`@brief`, `@param`, `@return`). Il programma deve leggere un array, cercare un valore e stampare l'indice o -1.

---

