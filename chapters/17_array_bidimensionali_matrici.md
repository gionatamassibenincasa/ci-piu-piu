---
activity_id: "matrici-01"
title: "Il Setaccio e la Griglia: Ricerca Lineare e Matrici Contabili"
methodology: PRIMM
order: 18
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Se inverti l'ordine dei due cicli `for` annidati in una matrice 2×3, in che ordine vengono stampati gli elementi?"
    code: |
      int mat[2][3] = {{1,2,3},{4,5,6}};
      // ciclo interno primo
      for (int i=0;i<2;i++){
        for (int j=0;j<3;j++){
          std::cout << mat[i][j];
        }
      }
      // ciclo esterno primo (invertito)
      // ...
    options:
      - text: "1 2 3 4 5 6"
        correct: true
      - text: "1 4 2 5 3 6"
        correct: false
      - text: "4 5 6 1 2 3"
        correct: false
      - text: "Errore di compilazione"
        correct: false
  make_instructions: "Scenario SIA — Griglia di fatturazione mensile"
files:
  - path: student_work/make/matrici_fatturazione.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Analizza fatturazione mensile usando una matrice 4x12.
       */
      #include <iostream>
      #include <iomanip>

      int main() {
          // TODO: implementare analisi matrice fatturazione
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain: ["int main"]
---

## 🎯 Il Setaccio e la Griglia: Ricerca Lineare e Matrici Contabili

> "Una tabella Excel è una griglia di dati dove ogni cella ha riga e colonna."
>
> — *Metafora di matrici* 

### Obiettivo
- Dichiarare e inizializzare matrici 2‑dimensionali.
- Implementare ricerca lineare in una matrice.
- Utilizzare cicli annidati per scorrere righe e colonne.
- Formattare output con `<iomanip>`.

---

## 📚 Teoria
1. Sintassi `tipo nome[RIGHE][COLONNE];`
2. Inizializzazione con `{{...},{...}}`.
3. Accesso `mat[r][c]`.
4. Ricerca lineare su matrice.
5. Formattazione con `std::setw`, `std::fixed`.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


[[ predict_block() ]]


<details><summary>💡 Spiegazione</summary>Il ciclo interno stampa per ogni riga tutti gli elementi della colonna, quindi l'ordine naturale è riga‑per‑riga.
</details>

### Run
```cpp
/**
 * @file matrici_fatturazione.cpp
 * @brief Analisi fatturazione mensile usando una matrice 4×12.
 */
#include <iostream>
#include <iomanip>

int main() {
    const int R = 4, C = 12;
    double fatt[R][C] = { /* dati simulati */ };
    // stampa con formattazione
    std::cout << std::fixed << std::setprecision(2);
    for (int r=0; r<R; ++r) {
        for (int c=0; c<C; ++c) {
            std::cout << std::setw(8) << fatt[r][c];
        }
        std::cout << "\n";
    }
    return 0;
}
```
@LIA.cpp

### Investigate
Usa Python Tutor per visualizzare la memoria lineare della matrice.

### Modify
Aggiungi ricerca di un valore soglia (es. fatturato > 50000) e stampa le coordinate (riga, colonna).

### Make
**Scenario SIA — Griglia di fatturazione mensile**

Scrivi `matrici_fatturazione.cpp` con Doxygen (`@brief`, `@param`, `@return`). Il programma deve stampare la matrice formattata e individuare il valore massimo.

---

