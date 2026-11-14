---
activity_id: "puntatori-01"
title: "Il Biglietto di Ritiro: Indirizzi di Memoria, Operatori & e * e Puntatori"
methodology: PRIMM
order: 18
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Dati `int a = 10; int* p = &a; *p = 20;`, quanto vale `a`?"
    code: |
      int a = 10;
      int* p = &a;
      *p = 20; // modifica a
    options:
      - text: "20"
        correct: true
      - text: "10"
        correct: false
      - text: "Compila con errore"
        correct: false
      - text: "Il programma crasha"
        correct: false
  make_instructions: "Scenario SIA — Gestione Fido Bancario tramite Puntatore"
files:
  - path: student_work/make/gestione_fido.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Gestisce il fido bancario usando puntatori.
       */
      #include <iostream>

      void aggiornaFido(double* fido, double importo) {
          // TODO: implementare aggiornamento con verifica nullptr
      }

      int main() {
          double fido = 5000.0;
          aggiornaFido(&fido, 1200.0);
          std::cout << "Fido aggiornato: " << fido << std::endl;
          return 0;
      }
    validation_rules:
      min_lines: 10
      must_contain: ["int main"]
---

## 🎯 Il Biglietto di Ritiro: Indirizzi di Memoria, Operatori & e * e Puntatori

> "Un puntatore è un biglietto che indica dove si trova la merce."
>
> — *Metafora di memoria*

### Obiettivo
- Comprendere gli operatori `&` (indirizzo) e `*` (dereferenza).
- Usare `nullptr` e verificare la validità del puntatore.
- Visualizzare lo stack con Python Tutor per capire la relazione tra puntatore e variabile.

---

## 📚 Teoria
1. `int* p;` dichiara un puntatore a `int`.
2. `p = &var;` assegna l’indirizzo di `var`.
3. `*p` accede al valore puntato.
4. `nullptr` indica nessun puntatore valido.
5. Puntatori a array e passaggio a funzioni.

---

## 🔬 Laboratorio PRIMM

### Predict
Dati `int a = 10; int* p = &a; *p = 20;`, quanto vale `a`?
- [(X)] 20
- [( )] 10
- [( )] Compila con errore
- [( )] Il programma crasha

<details><summary>💡 Spiegazione</summary>Il dereferenziamento `*p = 20` modifica direttamente la variabile `a`.
</details>

### Run
```cpp
/**
 * @file gestione_fido.cpp
 * @brief Gestione di un fido bancario tramite puntatore.
 */
#include <iostream>

void aggiornaFido(double* fido, double importo) {
    if (fido && importo > 0) {
        *fido += importo;
    }
}

int main() {
    double fido = 5000.0;
    aggiornaFido(&fido, 1200.0);
    std::cout << "Fido aggiornato: " << fido << std::endl;
    return 0;
}
```
@LIA.cpp

### Investigate
Usa Python Tutor per visualizzare il collegamento tra `a` e `p`.

### Modify
Aggiungi una funzione `void resetFido(double* fido)` che imposta a zero, controllando `nullptr`.

### Make
**Scenario SIA — Gestione Fido Bancario tramite Puntatore**

Scrivi `gestione_fido.cpp` con Doxygen (`@brief`, `@param`, `@return`). Il programma deve incrementare il fido e stampare il risultato.

---

> 🔖 *Attività* `puntatori-01` · *ordine* 18 · *metodo* PRIMM
