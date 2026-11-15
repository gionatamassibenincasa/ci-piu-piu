---
activity_id: "funzioni-01"
title: "Il Primo Reparto: una funzione che restituisce un valore"
methodology: PRIMM
order: 14
language: it
components:
  predict_quiz:
    question: "Quale valore restituisce calcolaIva(100.0)?"
    code: |
      double calcolaIva(double imponibile) {
          return imponibile * 0.22;
      }
    options:
      - text: "22"
        correct: true
      - text: "100"
        correct: false
      - text: "122"
        correct: false
  make_instructions: "Calcolare una commissione POS con una funzione."
files:
  - path: README.md
    action: create
    template_content: |
      # Prima funzione
      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict
      1. Quale valore torna dalla funzione?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run
      1. Quale importo IVA hai ottenuto?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate
      1. Quale valore entra e quale valore esce dalla funzione?
      >
  - path: student_work/modify/calcolo_iva.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>
      double calcolaIva(double imponibile) { return imponibile * 0.22; }
      int main() { std::cout << calcolaIva(100.0) << "\n"; }
  - path: student_work/make/commissione_pos.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      double calcolaCommissione(double importo) {
          /// TODO: spiega perché la percentuale è applicata all'importo.
          return 0.0;
      }
      int main() { return 0; }
    validation_rules:
      min_lines: 8
      must_contain: ["return"]
---

## 🏢 Il Primo Reparto: una funzione che restituisce un valore

> 💡 **Metafora:** una funzione è un reparto: riceve un ordine, svolge un lavoro
> preciso e restituisce il risultato senza mostrare tutti i passaggi interni.

### 🎯 Obiettivo
Scrivere e chiamare una funzione che riceve un valore e ne restituisce uno.

---

### ⚙️ Prima del laboratorio: ingresso e uscita

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

`imponibile` è il dato che entra nel reparto; `return` consegna il valore
calcolato a chi ha chiamato la funzione.

---

### 🧭 Prima del laboratorio: chiamare il reparto

```cpp
double iva = calcolaIva(100.0);
```

Il valore `100.0` entra nella funzione; `22.0` torna e viene salvato in `iva`.

---

### 🔬 Laboratorio PRIMM: IVA di una fattura

#### 1. PREDICT

[[ predict_block() ]]

#### 2. RUN

```cpp
#include <iostream>

double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

int main() {
    double iva = calcolaIva(100.0);
    std::cout << "IVA: " << iva << "\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE

| Passo | Valore |
|---|---|
| Chiamata | `imponibile = 100.0` |
| `return` | `22.0` |
| In `main` | `iva = 22.0` |

> 🔗 Osserva i due frame su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY

<details><summary>💡 Scaffold</summary>

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

</details>

1. Calcola l'IVA di `250.0`.
2. Sostituisci `0.22` con `0.10` e osserva il risultato.
3. Rinomina `imponibile` in `importoNetto` in firma e corpo.

#### 5. MAKE

**Scenario SIA:** scrivi `commissione_pos.cpp` con una funzione
`calcolaCommissione(double importo)` che restituisce l'1% dell'importo e stampa
il risultato in `main`.

### 📝 Riepilogo tascabile
- Una funzione riceve dati, svolge un lavoro e può restituire un valore.
- `return` termina la funzione e consegna il risultato.
- La chiamata usa il valore restituito in un'espressione.

### ➡️ Prossimo chunk
Nel prossimo chunk separeremo programmi più grandi in più reparti.
