<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-16
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/20_enum-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/22_selection-sort-01.md)

---


## 🔍 Trovare il Codice nel Listino: ricerca dicotomica

> "Non sfogliare tutto il catalogo se è già in ordine alfabetico."  
> — *Efficienza operativa*

Cercare un codice prodotto scorrendo **tutto** l’array funziona, ma su listini lunghi è costoso.  
Se il listino è **ordinato**, possiamo usare la **ricerca dicotomica** (binaria): a ogni passo dimezziamo l’intervallo.

> 💡 **Metafora: elenco telefonico (o catalogo a pagine)**  
> Apri a metà: il nome cercato è prima o dopo?  
> Scarti metà elenco e ripeti.  
> **Precondizione:** l’elenco deve essere **già ordinato**.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Implementare una ricerca binaria su un array di interi **ordinato**
- Spiegare perché l’ordine dei dati è obbligatorio

---

### ⚙️ Idea dell’algoritmo
1. `low = 0`, `high = N - 1`
2. Finché `low <= high`: guarda il centro `mid`
3. Se `a[mid] == chiave` → trovato  
4. Se `a[mid] < chiave` → cerca a destra (`low = mid + 1`)  
5. Altrimenti cerca a sinistra (`high = mid - 1`)

---

### 🔬 Laboratorio PRIMM: Codici prodotto ordinati

#### 1. PREDICT (Prevedi)

La ricerca binaria su un array disordinato è affidabile?

```cpp
// array NON ordinato
// binary_search(...)
```

[( )] Sì, sempre
[(X)] No: richiede array ordinato
[( )] Solo se tutti pari
[( )] Solo su stringhe

<details>
<summary>💡 Spiegazione</summary>
La dicotomica assume ordinamento. Su dati disordinati può “perdere” elementi ancora presenti.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ricerca_codice.cpp
 * @brief Ricerca binaria su codici prodotto ordinati.
 */
#include <iostream>

int main() {
    int codici[8] = {100, 150, 200, 250, 300, 350, 400, 450};
    int chiave = 300;
    int low = 0;
    int high = 7;
    int trovato = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (codici[mid] == chiave) {
            trovato = mid;
            break;
        } else if (codici[mid] < chiave) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    if (trovato >= 0) {
        std::cout << "Trovato in posizione " << trovato << '\n';
    } else {
        std::cout << "Non presente\n";
    }
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Passo | Cosa osservare |
|-------|----------------|
| `mid` | Sempre un indice nell’intervallo corrente |
| `low` / `high` | Si restringono; non devono “incrociarsi” senza uscita |
| Array | Deve restare ordinato in modo non decrescente |

Simula a mano 2–3 iterazioni su carta, poi [Python Tutor](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. Cambia `chiave` in un valore assente e verifica il messaggio.
2. Estrai una funzione `int cerca(const int a[], int n, int chiave)` che restituisce l’indice o `-1`.
3. Conta quante volte si esegue il corpo del `while` (confronti).

#### 5. MAKE (Crea)
**Scenario SIA — Verifica codice EAN interno**

`cerca_codice.cpp`: array ordinato di codici, input della chiave (o costante), stampa posizione o “non trovato”. Funzione dedicata alla ricerca.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int cerca(const int a[], int n, int chiave) {
    // binary search
    return -1;
}
int main() { /* ... */ return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Dicotomica = dimezza l’intervallo a ogni passo
- **Solo** su sequenze ordinate
- Restituisci indice o `-1`
- Molto più scalabile della scansione lineare su listini lunghi

---

### ➡️ Prossimo chunk
Per usare la ricerca binaria serve spesso **ordinare** prima i dati: selection sort.
