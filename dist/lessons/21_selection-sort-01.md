<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-14
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/20_ricerca-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/22_esempio-primm-22.md)

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

### Predict
Se l'array è già ordinato, quanti confronti fa comunque il Selection Sort?
- [(X)] Il numero di confronti è sempre lo stesso (n·(n‑1)/2)
- [( )] Zero, poiché l'algoritmo riconosce l'array ordinato
- [( )] n‑1 confronti
- [( )] Dipende dalla presenza di duplicati

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

> 🔖 *Attività* `selection-sort-01` · *ordine* 21 · *metodo* PRIMM
