---
activity_id: "enum-01"
title: "L'Anagrafica Aziendale: Enumerazioni (`enum class`) e Strutture (`struct` )"
methodology: PRIMM
order: 19
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Se assegno `Ordine o2 = o1;`, cosa succede alla memoria?"
    code: |
      enum class StatoOrdine { InAttesa, Confermato, Spedito, Annullato };
      struct Ordine { int id; std::string cliente; double importo; StatoOrdine stato; };
      Ordine o1{1,"Mario",100.0,StatoOrdine::InAttesa};
      Ordine o2 = o1; // copia
    options:
      - text: "Viene copiata campo per campo, occupa nuova memoria"
        correct: true
      - text: "Viene condivisa la stessa memoria (alias)"
        correct: false
      - text: "Compila con errore perché le struct non sono copiabili"
        correct: false
      - text: "Il programma crasha"
        correct: false
  make_instructions: "Scenario SIA — Definizione di struct Dipendente e stampa scheda ordine"
files:
  - path: student_work/make/enum_struct.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Definisce enum class StatoOrdine e struct Ordine, stampa informazioni.
       */
      #include <iostream>
      #include <string>

      enum class StatoOrdine { InAttesa, Confermato, Spedito, Annullato };

      struct Ordine {
          int idOrdine;
          std::string cliente;
          double importoTotale;
          StatoOrdine stato;
      };

      void stampaScheda(const Ordine& o) {
          // TODO: formattare output con iomanip
      }

      int main() {
          // esempio di creazione e stampa
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain: ["int main"]
---

## 🎯 L'Anagrafica Aziendale: Enumerazioni (`enum class`) e Strutture (`struct`)

> "Un enum è il timbro ufficiale dello stato pratica; una struct è la cartella anagrafica."
>
> — *Metafora di dati aziendali*

### Obiettivo
- Creare `enum class` per stati discreti.
- Definire `struct` per raggruppare dati eterogenei.
- Usare `const &` per passare struct a funzione di stampa.
- Formattare output con `<iomanip>`.

---

## 📚 Teoria
1. Sintassi `enum class Nome { ... };` evita conflitti.
2. `struct Nome { ... };` raggruppa campi.
3. Accesso con `.` e `->`.
4. Passaggio per riferimento costante per evitare copie.
5. Doxygen per documentare enum e struct.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


[[ predict_block() ]]


<details><summary>💡 Spiegazione</summary>La copia è profonda per i campi semplici; per campi `std::string` viene effettuata una copia della stringa.
</details>

### Run
```cpp
/**
 * @file enum_struct.cpp
 * @brief Esempio di enum class e struct per ordini.
 */
#include <iostream>
#include <string>
#include <iomanip>

enum class StatoOrdine { InAttesa, Confermato, Spedito, Annullato };

struct Ordine {
    int idOrdine;
    std::string cliente;
    double importoTotale;
    StatoOrdine stato;
};

void stampaScheda(const Ordine& o) {
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "ID: " << o.idOrdine << " Cliente: " << o.cliente
              << " Importo: " << o.importoTotale << " Stato: " << static_cast<int>(o.stato) << "\n";
}

int main() {
    Ordine o{1, "Mario Rossi", 1234.56, StatoOrdine::InAttesa};
    stampaScheda(o);
    return 0;
}
```
@LIA.cpp

### Investigate
Visualizza con Python Tutor l’allocazione di `Ordine` e la copia.

### Modify
Aggiungi funzione `void aggiornaStato(Ordine& o, StatoOrdine nuovo)`.

### Make
**Scenario SIA — Definizione di struct Dipendente e stampa scheda ordine**

Scrivi `enum_struct.cpp` con Doxygen (`@brief`, `@param`, `@return`). Il programma deve creare un ordine, stamparne i dati e consentire aggiornamento stato.

---

