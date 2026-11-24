---
activity_id: "ricorsione-01"
title: "Il Problema che Chiama Se Stesso: ricorsione"
methodology: PRIMM
order: 27
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Cosa deve avere ogni funzione ricorsiva corretta?"
    code: |
      int f(int n) {
          if (n <= 0) return 1; // ?
          return n * f(n - 1);
      }
    options:
      - text: "Solo chiamate ricorsive, senza mai fermarsi"
        correct: false
      - text: "Almeno un caso base che interrompe la ricorsione"
        correct: true
      - text: "Obbligo di variabili globali"
        correct: false
      - text: "Niente `return`"
        correct: false
  make_instructions: "Somma ricorsiva degli elementi di un array"
files:
  - path: student_work/make/somma_ricorsiva.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      int main() { return 0; }
    validation_rules:
      min_lines: 18
      must_contain: ["return"]
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

[[ predict_block() ]]

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

### ➡️ Prossimo passo nel percorso
Nel precedente blocco hai consolidato array, struct, ricerca, ordinamento e
ricorsione. Nel prossimo capitolo, `29_da_struct_a_class`, inizierai il passaggio
da dati raggruppati a oggetti con responsabilità.
