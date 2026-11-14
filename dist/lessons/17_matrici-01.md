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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_array-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/18_puntatori-01.md)

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

### Predict
Se inverti l'ordine dei due cicli `for` annidati in una matrice `2×3`, in che ordine vengono stampati gli elementi?
```cpp
int mat[2][3] = {{1,2,3},{4,5,6}};
// ciclo interno primo
for (int i=0;i<2;i++){
  for (int j=0;j<3;j++){
    std::cout << mat[i][j];
  }
}
// ciclo esterno primo (invertito)
// ...
```
- [(X)] 1 2 3 4 5 6
- [( )] 1 4 2 5 3 6
- [( )] 4 5 6 1 2 3
- [( )] Errore di compilazione

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

> 🔖 *Attività* `matrici-01` · *ordine* 17 · *metodo* PRIMM
