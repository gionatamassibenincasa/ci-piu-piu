---
activity_id: "puntatori-01"
title: "Il Numero dello Sportello: puntatori e indirizzi"
methodology: PRIMM
order: 20
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Dopo `int x = 10; int* p = &x; *p = 25;`, quanto vale `x`?"
    code: |
      int x = 10;
      int* p = &x;
      *p = 25;
    options:
      - text: "10"
        correct: false
      - text: "25"
        correct: true
      - text: "Indefinito"
        correct: false
      - text: "L’indirizzo di x"
        correct: false
  make_instructions: "Scambio di due prezzi con puntatori"
files:
  - path: student_work/make/scambia_prezzi_ptr.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      void scambia(double* a, double* b) {
          // TODO
      }
      int main() { return 0; }
    validation_rules:
      min_lines: 15
      must_contain: ["*", "&"]
---

## 🔑 Il Numero dello Sportello: puntatori e indirizzi

> "Non ti do la merce: ti do la chiave del locker."  
> — *Metafora operativa*

Finora passavamo **valori** (copie) o **riferimenti** (`&` nei parametri).  
Un **puntatore** è una variabile che memorizza l’**indirizzo** di un’altra variabile: il *numero dello sportello*, non la merce.

> 💡 **Metafora**  
> - `x` = merce nel locker  
> - `&x` = numero civico dello sportello  
> - `int* p` = foglietto su cui è scritto un numero di sportello  
> - `p = &x` = “annota l’indirizzo di x”  
> - `*p` = “apri lo sportello indicato e usa la merce”

In questo chunk **non** usiamo ancora `new`/`delete`: solo puntatori a variabili automatiche.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare un puntatore, assegnargli `&variabile` e usare `*` per leggere/scrivere
- Spiegare la differenza tra l’indirizzo (`p`) e il valore puntato (`*p`)

---

### ⚙️ In breve

```cpp
int giacenza = 40;
int* p = &giacenza;   // p contiene l'indirizzo di giacenza
std::cout << *p;      // 40
*p = 35;              // modifica giacenza tramite il puntatore
```

---

### 🔬 Laboratorio PRIMM: Aggiornare la giacenza via puntatore

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
<code>*p = 25</code> scrive nello sportello di <code>x</code>, perché <code>p</code> punta a <code>x</code>. Quindi <code>x</code> diventa 25.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file puntatore_giacenza.cpp
 * @brief Modifica di una variabile tramite puntatore.
 */
#include <iostream>

int main() {
    int giacenza = 40;
    int* p = &giacenza;

    std::cout << "Prima: " << giacenza << '\n';
    *p = *p - 5;  // scarico 5 pezzi
    std::cout << "Dopo:  " << giacenza << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Espressione | Cosa rappresenta |
|-------------|------------------|
| `giacenza` | Valore (merce) |
| `&giacenza` | Indirizzo |
| `p` | Copia dell’indirizzo |
| `*p` | Merce nello sportello puntato |

Osserva in [Python Tutor](https://pythontutor.com/cpp.html) le frecce tra `p` e `giacenza`.

#### 4. MODIFY (Modifica)
1. Stampa anche l’indirizzo con `std::cout << p;` (vedrai un hex).
2. Crea `double prezzo` e un `double*` che lo aggiorna (+IVA 22%).
3. Scrivi una funzione `void azzera(int* q)` che mette a 0 la variabile puntata.

#### 5. MAKE (Crea)
**Scenario SIA — Scambio prezzi listino**

`scambia_prezzi_ptr.cpp`: funzione `void scambia(double* a, double* b)` che scambia due prezzi **via puntatori**. In `main`, dimostra lo scambio su due variabili.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void scambia(double* a, double* b) {
    double tmp = *a;
    // ...
}
int main() {
    double p1 = 10.0, p2 = 20.0;
    scambia(&p1, &p2);
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Puntatore = variabile che tiene un **indirizzo**
- `&x` indirizzo; `*p` valore puntato
- `*p = …` modifica la variabile originale
- In questo corso: prima i puntatori “semplici”, allocazione dinamica più avanti se serve

---

### ➡️ Prossimo chunk
Raggruppiamo dati eterogenei (`struct`) e stati discreti (`enum`) come in un record anagrafico.
