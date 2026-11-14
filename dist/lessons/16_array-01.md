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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_scope-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/17_matrici-01.md)

---


## 🎯 La Batteria di Locker: Gli Array e le Sequenze di Dati

> "Una fila di locker identici rappresenta un array, ogni locker è un elemento indicizzato."
>
> — *Metafora di memoria contigua*

### Obiettivo
- Comprendere dichiarazione, indicizzazione e inizializzazione di array grezzi.
- Riconoscere pericoli di out‑of‑bounds.
- Utilizzare `for` per scorrere un array e calcolare somme, medie, min/max.

---

## 📚 Teoria
1. Sintassi `tipo nome[DIM];`
2. Indice parte da 0.
3. Inizializzazione con `{}`.
4. Limiti di indice.
5. Confronto con `std::vector`.

---

## 🔬 Laboratorio PRIMM

### Predict
Cosa succede se si accede a `vendite[30]` quando l'array è dichiarato con dimensione 30?
```cpp
double vendite[30];
// ...
double x = vendite[30];
```
- [(X)] Compila ma legge valore casuale (out‑of‑bounds)
- [( )] Compila e stampa 0
- [( )] Errore di compilazione
- [( )] Il programma non avvia

<details><summary>💡 Spiegazione</summary>Indice 30 è fuori dall’intervallo valido `[0‑29]`; il comportamento è indefinito.
</details>

### Run
```cpp
/**
 * @file controllo_vendite.cpp
 * @brief Analisi vendite di 30 giorni.
 */
#include <iostream>

int main() {
    double vendite[30] = { /* dati simulati */ };
    double totale = 0.0;
    double max = vendite[0];
    double min = vendite[0];
    for (int i = 0; i < 30; ++i) {
        totale += vendite[i];
        if (vendite[i] > max) max = vendite[i];
        if (vendite[i] < min) min = vendite[i];
    }
    std::cout << "Totale=" << totale << " Media=" << totale/30 << " Max=" << max << " Min=" << min << "\n";
    return 0;
}
```
@LIA.cpp

### Investigate
Usa Python Tutor per visualizzare l’intero blocco di memoria dell’array.

### Modify
Aggiungi conteggio dei giorni con incasso > soglia (es. 1000 €).

### Make
**Scenario SIA — Controllo Vendite Mensili con Array**

Scrivi `controllo_vendite.cpp` includendo Doxygen (`@brief`, `@param`, `@return`). Il programma deve calcolare totale, media, max, min e giorni sopra soglia.

---

> 🔖 *Attività* `array-01` · *ordine* 16 · *metodo* PRIMM
