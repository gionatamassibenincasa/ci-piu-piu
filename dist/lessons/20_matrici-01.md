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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/19_array-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/21_puntatori-01.md)

---


## 📊 Il Foglio Excel in Memoria: array bidimensionali

> "Una tabella è il modo più naturale di organizzare dati aziendali."  
> — *Pratica di reporting gestionale*

Un array monodimensionale è una **riga**.  
Spesso i report sono **griglie**: righe = reparti, colonne = mesi o trimestri.  
In C++ usiamo un **array bidimensionale** (matrice).

> 💡 **Metafora: foglio Excel**  
> - `vendite[r][c]` = cella all’incrocio **riga r**, **colonna c**  
> - Prima dimensione = righe (reparti)  
> - Seconda = colonne (periodi)  
> - Anche qui gli indici partono da **0**

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare e scorrere un array `tipo nome[RIGHE][COLONNE]`
- Calcolare totali per riga (o per colonna) su dati tabellari

---

### ⚙️ In breve

```cpp
// 2 reparti × 3 mesi
double vendite[2][3] = {
    {1000.0, 1200.0, 900.0},   // reparto 0
    {800.0,  950.0,  1100.0}   // reparto 1
};
```

Due cicli annidati: esterno sulle righe, interno sulle colonne.

---

### 🔬 Laboratorio PRIMM: Due reparti, tre mesi

#### 1. PREDICT (Prevedi)

```cpp
int m[2][3];
```

In `int m[2][3];`, quanti elementi ci sono e qual è l’ultimo indice di colonna?

[( )] 2 elementi in tutto
[( )] 6 elementi; colonne 1..3
[(X)] 6 elementi; colonne 0..2
[( )] 5 elementi; colonne 1..3

<details>
<summary>💡 Spiegazione</summary>
<code>int m[2][3]</code> ha 2×3 = 6 elementi. Le colonne sono indicizzate 0, 1, 2.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file matrice_vendite.cpp
 * @brief Totale per reparto su tre mesi.
 */
#include <iostream>

int main() {
    double vendite[2][3] = {
        {1000.0, 1200.0, 900.0},
        {800.0, 950.0, 1100.0}
    };

    for (int r = 0; r < 2; ++r) {
        double subtotale = 0.0;
        for (int c = 0; c < 3; ++c) {
            subtotale = subtotale + vendite[r][c];
        }
        std::cout << "Reparto " << r << " totale: " << subtotale << '\n';
    }
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Variabile | Significato |
|-----------|-------------|
| `r` | Indice di riga (reparto) |
| `c` | Indice di colonna (mese) |
| `subtotale` | Si azzera a ogni nuova riga |

Segui con [Python Tutor](https://pythontutor.com/cpp.html) l’ordine delle celle visitate.

#### 4. MODIFY (Modifica)
1. Aggiungi un terzo reparto (matrice `3×3`) e aggiorna i cicli.
2. Stampa anche il **totale generale** di tutta la matrice.
3. Stampa i totali **per colonna** (per mese).

#### 5. MAKE (Crea)
**Scenario SIA — Vendite per reparto e trimestre**

`vendite_reparti.cpp`: matrice **3 reparti × 4 trimestri**, totali per riga, per colonna e complessivo. Output leggibile.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    const int R = 3, C = 4;
    double v[R][C] = { /* ... */ };
    // cicli annidati
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Matrice = foglio a righe e colonne
- `m[i][j]`: prima riga, poi colonna
- Quasi sempre **due** `for` annidati
- Stessi pericoli di out-of-bounds, su due assi

---

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai organizzato dati in righe e colonne.
Nel prossimo capitolo, `21_puntatori_e_memoria`, seguirai gli indirizzi in
memoria con i **puntatori**, in modo guidato e cauto.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/19_array-01.md">Lezione precedente (19 — La Batteria di Locker: gli array e le sequenze di dati)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/21_puntatori-01.md">Lezione successiva (21 — Il Numero dello Sportello: puntatori e indirizzi)</a>
