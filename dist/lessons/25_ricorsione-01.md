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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/24_db-memoria-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/26_class-incapsulamento-01.md)

---


## 🔁 Il Problema che Chiama Se Stesso: ricorsione

> "Per capire n, capisci n−1; poi combina."  
> — *Schema divide et impera*

Una funzione **ricorsiva** si richiama su un’istanza **più piccola** dello stesso problema, finché raggiunge un **caso base**.

> 💡 **Metafora: matrioske contabili**  
> Per chiudere il totale di n movimenti: prendi l’importo dell’ultimo e **aggiungilo** al totale dei primi n−1.  
> Caso base: zero movimenti → totale 0.

Attenzione: senza caso base si ottiene **ricorsione infinita** (stack overflow).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una funzione ricorsiva con caso base chiaro
- Tracciare le chiamate su un esempio piccolo (fattoriale o somma)

*Non* affrontiamo qui liste collegate complete: restiamo su problemi numerici/array.

---

### 🔬 Laboratorio PRIMM: Fattoriale (per vedere lo stack)

#### 1. PREDICT (Prevedi)

Cosa deve avere ogni funzione ricorsiva corretta?

```cpp
int f(int n) {
    if (n <= 0) return 1; // ?
    return n * f(n - 1);
}
```

[( )] Solo chiamate ricorsive, senza mai fermarsi
[(X)] Almeno un caso base che interrompe la ricorsione
[( )] Obbligo di variabili globali
[( )] Niente `return`

<details>
<summary>💡 Spiegazione</summary>
Senza un if di arresto la catena di chiamate non termina. Il caso base è obbligatorio.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file fattoriale.cpp
 * @brief Esempio didattico di ricorsione con caso base.
 */
#include <iostream>

int fattoriale(int n) {
    if (n <= 1) {
        return 1;  // caso base
    }
    return n * fattoriale(n - 1);
}

int main() {
    std::cout << fattoriale(5) << '\n';  // 120
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Chiamata | Ritorna |
|----------|---------|
| `fattoriale(1)` | `1` |
| `fattoriale(2)` | `2 * 1` |
| `fattoriale(3)` | `3 * 2` |
| … | … |

Usa [Python Tutor](https://pythontutor.com/cpp.html) e osserva i **frame** sullo stack.

#### 4. MODIFY (Modifica)
1. Calcola `fattoriale(0)` e `fattoriale(1)`.
2. Scrivi `int potenza(int base, int exp)` ricorsiva (`exp == 0` → 1).
3. Versione **iterativa** equivalente del fattoriale e confronta leggibilità.

#### 5. MAKE (Crea)
**Scenario SIA — Totale ricorsivo di importi**

`somma_ricorsiva.cpp`: funzione `double somma(const double a[], int n)` ricorsiva  
(`n == 0` → 0; altrimenti `a[n-1] + somma(a, n-1)`). Dimostrazione in `main` su un piccolo array di movimenti.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
double somma(const double a[], int n) {
    if (n <= 0) return 0.0;
    return a[n - 1] + somma(a, n - 1);
}
int main() { /* ... */ return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Ricorsione = caso base + passo che riduce il problema
- Ogni chiamata ha il proprio frame sullo stack
- Senza caso base → ricorsione infinita
- Utile quando il problema ha struttura naturale “a pezzi più piccoli”

---

### ➡️ Prossimo passo
Con array, struct, ricerca, ordinamento e ricorsione hai gli strumenti del **secondo blocco** del corso: dati e algoritmi di base in chiave aziendale.
