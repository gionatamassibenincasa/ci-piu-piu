---
activity_id: "scope-01"
title: "La Fotocopia vs L'Originale: Scope e Passaggio per Riferimento (`&` )"
methodology: PRIMM
order: 15
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Cosa succede se una funzione prende un parametro per valore invece che per riferimento (`&`) quando dovrebbe modificare la variabile originale?"
    code: |
      void aumenta(int valore) { valore += 5; }
      void aumentaRef(int& valore) { valore += 5; }
      int x = 10;
      aumenta(x);
      // x è ?
    options:
      - text: "x rimane 10 (non modificato)"
        correct: true
      - text: "x diventa 15"
        correct: false
      - text: "Compila con errore"
        correct: false
      - text: "Il programma crasha"
        correct: false
  make_instructions: "Scenario SIA — Aggiornamento Listino e Scambio"
files:
  - path: student_work/make/aggiorna_listino.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Aggiorna prezzo di un prodotto nel listino e scambia prezzi tra due prodotti.
       */
      #include <iostream>

      void applicaScontoPromozionale(double& prezzo, double percentuale) {
          // TODO: implementare sconto
      }

      void scambiaPrezzi(double& p1, double& p2) {
          // TODO: implementare scambio
      }

      int main() {
          // driver di esempio
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain: ["int main"]
---

## 🎯 La Fotocopia vs L'Originale: Scope e Passaggio per Riferimento (`&`)

> "Il segreto del valore è chi lo possiede realmente."
>
> — *Metafora di gestione dei dati*

### Obiettivo
- Distinguere passaggio per valore da passaggio per riferimento.
- Comprendere lo scope delle variabili locali e globali.
- Utilizzare `const &` per efficienza.

---

## 📚 Teoria
1. Passaggio per valore copia il dato.
2. Passaggio per riferimento (`&`) passa un alias alla variabile originale.
3. `const &` permette lettura senza copia.
4. Scope locale vs globale.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


[[ predict_block() ]]


<details>
<summary>💡 Spiegazione</summary>
Il parametro per valore è una copia locale; le modifiche non si riflettono sulla variabile originale.
</details>

### Run
```cpp
/**
 * @file aggiorna_listino.cpp
 * @brief Funzioni per sconto e scambio prezzi.
 */
#include <iostream>

void applicaScontoPromozionale(double& prezzo, double percentuale) {
    // implementazione
}

void scambiaPrezzi(double& p1, double& p2) {
    // implementazione
}

int main() {
    double a = 100.0, b = 150.0;
    applicaScontoPromozionale(a, 10.0);
    scambiaPrezzi(a, b);
    std::cout << "a=" << a << " b=" << b << std::endl;
    return 0;
}
```
@LIA.cpp

### Investigate
Usa Python Tutor per visualizzare le due variabili e l'alias dopo la chiamata.

### Modify
Aggiungi una versione `void applicaScontoCostante(const double& prezzo, double percentuale, double& risultato)`.

### Make
**Scenario SIA — Aggiornamento Listino e Scambio**

Scrivi `aggiorna_listino.cpp` con le funzioni richieste, includendo Doxygen (`@brief`, `@param`, `@return`). Il programma deve dimostrare sconto e scambio.

---

