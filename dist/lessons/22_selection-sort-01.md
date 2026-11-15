<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-16
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/21_ricerca-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/23_merge-sort-01.md)

---


## 🗂️ Riordinare il Listino: selection sort

> "Metti in ordine i prezzi prima di cercare il migliore."  
> — *Pratica di listino*

La ricerca binaria chiede dati ordinati.  
Un algoritmo semplice da capire (non il più veloce in assoluto) è il **selection sort**: a ogni passo **seleziona il minimo** della parte non ancora ordinata e lo mette al suo posto.

> 💡 **Metafora: riorganizzare scaffali**  
> Scaffale disordinato di prezzi.  
> 1) Trova il più basso tra quelli ancora fuori posto  
> 2) Scambialo con la prima posizione libera  
> 3) Avanza e ripeti

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Implementare selection sort su un array di `double` (o `int`)
- Spiegare il ruolo del doppio ciclo e dello scambio

---

### 🔬 Laboratorio PRIMM: Prezzi da ordinare

#### 1. PREDICT (Prevedi)

Selection sort, a ogni passo esterno, cosa fa?

```cpp
// for i ...
//   cerca minimo in i..n-1
//   scambia con posizione i
```

[(X)] Sceglie il minimo della parte non ordinata e lo mette in posizione i
[( )] Divide sempre a metà l’array
[( )] Ordina solo i numeri pari
[( )] Usa obbligatoriamente un secondo array

<details>
<summary>💡 Spiegazione</summary>
A ogni iterazione esterna il minimo della coda non ordinata viene portato in testa a quella coda.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file selection_prezzi.cpp
 * @brief Ordinamento crescenti di prezzi con selection sort.
 */
#include <iostream>

int main() {
    double prezzi[6] = {12.5, 4.0, 9.9, 3.5, 20.0, 7.25};
    const int n = 6;

    for (int i = 0; i < n - 1; ++i) {
        int iMin = i;
        for (int j = i + 1; j < n; ++j) {
            if (prezzi[j] < prezzi[iMin]) {
                iMin = j;
            }
        }
        if (iMin != i) {
            double tmp = prezzi[i];
            prezzi[i] = prezzi[iMin];
            prezzi[iMin] = tmp;
        }
    }

    for (int i = 0; i < n; ++i) {
        std::cout << prezzi[i] << ' ';
    }
    std::cout << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Ciclo | Compito |
|-------|---------|
| Esterno `i` | Posizione da “fissare” |
| Interno `j` | Cerca l’indice del minimo in `i..n-1` |
| Scambio | Porta il minimo in posizione `i` |

Esegui a mano il primo passaggio su un array di 4 elementi.

#### 4. MODIFY (Modifica)
1. Ordina in **ordine decrescente**.
2. Estrai `void selectionSort(double a[], int n)`.
3. Conta quanti scambi effettivi (quando `iMin != i`).

#### 5. MAKE (Crea)
**Scenario SIA — Listino prezzi ordinato**

`ordina_prezzi.cpp`: almeno 8 prezzi, selection sort, stampa prima/dopo. Funzione dedicata all’ordinamento.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void selectionSort(double a[], int n) { /* ... */ }
int main() { /* ... */ return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Selection sort: minimo → posizione successiva
- Due `for` annidati; scambi semplici
- Facile da spiegare; non è il più efficiente su grandi N
- Utile per listini piccoli e per capire l’idea di ordinamento

---

### ➡️ Prossimo chunk
Strategie *divide et impera* (merge sort) per ordinamenti più scalabili.
