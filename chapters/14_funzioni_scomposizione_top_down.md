---
activity_id: "funzioni-01"
title: "I Reparti dell'Azienda: Sviluppo Top-Down e la Funzione come Scatola Nera"
methodology: PRIMM
order: 14
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Cosa accade se una funzione ha istruzioni dopo la riga del `return`?"
    code: |
      int esempio(int x) {
          return x * 2;
          // qui c'è codice inutilizzabile
          int y = x + 1;
          return y;
      }
    options:
      - text: "Il codice dopo `return` viene comunque eseguito"
        correct: false
      - text: "Il codice dopo `return` non viene mai eseguito (è inaccessibile)"
        correct: true
      - text: "Il compilatore sposta il `return` alla fine del blocco"
        correct: false
      - text: "Il programma crasha"
        correct: false
  make_instructions: "Scenario SIA — Calcolo busta paga con funzioni modulari"
files:
  - path: student_work/make/calcolo_stipendio.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Calcola lo stipendio lordo a partire da ore lavorate e tariffa.
       */
      double calcolaLordo(double oreLavorate, double tariffaOraria) {
          // TODO: implementazione
          return 0.0;
      }

      /**
       * @brief Calcola le ritenute fiscali sul lordo.
       */
      double calcolaRitenute(double lordo) {
          // TODO: implementazione
          return 0.0;
      }

      /**
       * @brief Stampa il cedolino del dipendente.
       */
      void stampaCedolino(const std::string& nome, double lordo, double netto) {
          // TODO: implementazione
      }

      int main() {
          // driver di esempio: 3 scenari di calcolo
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain: ["int main"]
---

## 🎯 I Reparti dell'Azienda: Sviluppo Top-Down e la Funzione come Scatola Nera

> "Il dirigente non controlla come l'impiegato lavora, gli consegna i dati e attende il risultato."
>
> — *Metafora applicata al design del software*

### Obiettivo
- Comprendere la scomposizione top‑down (divide et impera) nella progettazione di programmi.
- Distinguere **parametro formale** da **argomento reale**.
- Conoscere prototipo, definizione e `return` di una funzione.
- Usare funzioni `void` per operazioni senza valore di ritorno.

---

## 📚 Teoria
1. **Principio top‑down**: Si parte da una funzionalità alta‑livello e la si suddivide in sotto‑funzioni più piccole.
2. **Scatola Nera**: L’interfaccia (nome, parametri, valore di ritorno) è l’unica cosa che il chiamante conosce.
3. **Parametri**:
   - *Formale*: nella firma della funzione (`double oreLavorate`).
   - *Reale*: valore passato alla chiamata (`calcolaLordo(40, 15.5)`).
4. **Prototipo vs Definizione**.
5. **`return`**: termina la funzione e restituisce un valore.
6. **Funzioni `void`**: eseguono un’azione senza restituire dati.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


[[ predict_block() ]]
Cosa accade se una funzione ha istruzioni dopo la riga del `return`?
```cpp
int esempio(int x) {
    return x * 2;
    // qui c'è codice inutilizzabile
    int y = x + 1;
    return y;
}
```
- [( )] Il codice dopo `return` viene comunque eseguito
- [(X)] Il codice dopo `return` non viene mai eseguito (è inaccessibile)
- [( )] Il compilatore sposta il `return` alla fine del blocco
- [( )] Il programma crasha

<details>
<summary>💡 Spiegazione</summary>
Il `return` termina immediatamente la funzione; le istruzioni successive non sono raggiungibili e vengono scartate dal compilatore (se presenti, generano avviso di codice non usato).
</details>

### 2. Run (Esegui)
```cpp
/**
 * @file calcolo_stipendio.cpp
 * @brief Modulo di calcolo della busta paga.
 */
#include <iostream>
#include <string>

// prototipo
double calcolaLordo(double oreLavorate, double tariffaOraria);
double calcolaRitenute(double lordo);
void stampaCedolino(const std::string& nome, double lordo, double netto);

int main() {
    std::string dipendente = "Mario Rossi";
    double ore = 40.0;
    double tariffa = 15.5;
    double lordo = calcolaLordo(ore, tariffa);
    double ritenute = calcolaRitenute(lordo);
    double netto = lordo - ritenute;
    stampaCedolino(dipendente, lordo, netto);
    return 0;
}
```
@LIA.cpp

### 3. Investigate (Investiga)
Usa Python Tutor per visualizzare lo stack frame quando `main` chiama `calcolaLordo` e `calcolaRitenute`. Nota come il frame di `main` è sospeso fino al ritorno.

### 4. Modify (Modifica)
Aggiungi una funzione `double calcolaBonus(double netto, double percentuale)` e aggiorna `main` per applicare un bonus del 10% al netto.

### 5. Make (Crea)
**Scenario SIA — Calcolo busta paga con funzioni modulari**

Scrivi `calcolo_stipendio.cpp` con le funzioni richieste, includendo Doxygen (`@brief`, `@param`, `@return`). Il programma deve stampare tre scenari di stipendio (normale, straordinario, part‑time).

---

