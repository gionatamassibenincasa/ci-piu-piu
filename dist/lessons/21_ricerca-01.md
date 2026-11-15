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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/20_enum-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/22_selection-sort-01.md)

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


Se l'array ha 1.024 elementi ordinati, quanti passi al massimo servono per trovare un valore con ricerca binaria?

```cpp
// array di 1024 elementi ordinati
// ricerca binaria di un valore
```

[(X)] 10
[( )] 9
[( )] 11
[( )] 12


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

