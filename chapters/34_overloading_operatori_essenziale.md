---
activity_id: "operatori-01"
title: "Linguaggio del dominio: overloading essenziale di <<"
methodology: PRIMM
order: 34
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "A cosa serve tipicamente sovraccaricare `operator<<` per una classe?"
    code: |
      std::cout << articolo;
    options:
      - text: "Stampare l’oggetto in modo leggibile su uno stream"
        correct: true
      - text: "Aprire un file in automatico"
        correct: false
      - text: "Creare template"
        correct: false
      - text: "Sostituire il costruttore"
        correct: false
files:
  - path: student_work/make/stampa_articolo_op.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <string>
      int main() { return 0; }
    validation_rules:
      min_lines: 12
      must_contain:
      - "operator"
      - "class"
---


## 💬 Linguaggio del dominio: overloading essenziale (`<<`)

> "Meglio `std::cout << articolo` che quattro getter in fila."  
> — *API leggibile*

L’**overloading** degli operatori adatta la sintassi al dominio.  
In questo chunk un solo focus: **`operator<<`** per l’output.

> 💡 **Metafora:** il modulo di stampa dello scontrino sa come disporre i campi dell’articolo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare `operator<<` per una classe semplice
- Stampare un oggetto con `std::cout << obj`

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
<code>operator&lt;&lt;</code> definisce come inserire l’oggetto in uno <code>ostream</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_ostream.cpp
 * @brief operator<< per Articolo.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) : codice(c), prezzo(p) {}
    friend std::ostream& operator<<(std::ostream& os, const Articolo& a) {
        os << a.codice << " €" << a.prezzo;
        return os;
    }
};

int main() {
    Articolo a("A-100", 12.5);
    std::cout << a << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Elemento | Ruolo |
|----------|--------|
| `friend` | Accesso ai private per la stampa |
| `return os` | Consente `cout << a << b` |
| `const Articolo&` | Non modifica l’oggetto |

#### 4. MODIFY (Modifica)
1. Formatta il prezzo con due decimali (`iomanip`).
2. Aggiungi la giacenza in stampa.
3. Stampa due articoli in sequenza.

#### 5. MAKE (Crea)
**Scenario SIA — Scheda stampabile**

`stampa_articolo_op.cpp`: classe con `operator<<`; `main` dimostra almeno due stampe.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo { /* friend operator<< */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Un operatore per chunk: qui solo `<<`
- Restituisci lo stream
- Preferisci `const&` sul parametro oggetto
- Leggibilità del dominio > acrobazie

---

### ➡️ Prossimo chunk
Procedure uguali su tipi diversi: **funzioni template**.
