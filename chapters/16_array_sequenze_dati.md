---
activity_id: "array-01"
title: "La Batteria di Locker: gli array e le sequenze di dati"
methodology: PRIMM
order: 17
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Con `double vendite[30];`, cosa succede leggendo `vendite[30]`?"
    code: |
      double vendite[30];
      double x = vendite[30];
    options:
      - text: "Compila e legge 0"
        correct: false
      - text: "Compila ma comportamento indefinito (indice fuori range)"
        correct: true
      - text: "Errore di compilazione obbligatorio"
        correct: false
      - text: "Il programma non parte"
        correct: false
  make_instructions: "Controllo vendite mensili con array di 12 double"
files:
  - path: student_work/make/controllo_vendite.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      int main() {
          // TODO: 12 mesi, somma, media, mese max
          return 0;
      }
    validation_rules:
      min_lines: 20
      must_contain: ["for", "double"]
---

## 📦 La Batteria di Locker: gli array e le sequenze di dati

> "I dati non vivono isolati: vivono in elenchi."  
> — *Principio di progettazione dei sistemi informativi*

Finora ogni variabile era **uno sportello**.  
In azienda, però, i dati arrivano a **serie**: 12 mesi di vendite, 50 codici prodotto, 100 movimenti di cassa.  
Aprire 100 variabili diverse è insostenibile. Serve una **fila ordinata di sportelli**: l’**array**.

> 💡 **Metafora: batteria di locker InPost**  
> - L’**array** = una fila di locker **identici** e **numerati**  
> - L’**indice** (`0`, `1`, `2`…) = il numero sullo sportello (parte da **zero**)  
> - La **dimensione** = quanti locker hai prenotato (fissa, in C++ “grezzo”)  
> - `vendite[3]` = “apri il locker numero 3” (il **quarto** della fila)  
> - `vendite[30]` su 30 locker (`0`…`29`) = chiedi un locker che **non esiste** → caos

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare un array monodimensionale, indicizzarlo correttamente e scorrerlo con un `for`
- Riconoscere e evitare l’accesso **fuori dai limiti** (out-of-bounds)

---

### ⚙️ In breve

```cpp
double vendite[12];          // 12 locker: indici 0..11
vendite[0] = 1500.0;         // gennaio
vendite[11] = 2100.0;        // dicembre

for (int i = 0; i < 12; ++i) {
    std::cout << vendite[i] << '\n';
}
```

| Idea | Regola |
|------|--------|
| Indice legale | Da `0` a `N - 1` |
| `vendite[N]` | **Fuori**: il compilatore spesso **non** ti ferma |
| Tipo | Tutti gli elementi dello stesso tipo |

---

### 🔬 Laboratorio PRIMM: Vendite mensili

Registriamo 6 mesi di fatturato e calcoliamo un totale.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
Con dimensione 30 gli indici validi sono 0…29. L’indice 30 è fuori: il C++ non obbliga un controllo a runtime; il risultato è indefinito.
</details>

#### 2. RUN (Esegui)

Digita e premi **Run**.

```cpp
/**
 * @file vendite_semestre.cpp
 * @brief Totale vendite su sei mesi (array).
 */
#include <iostream>

int main() {
    double vendite[6] = {1200.0, 980.0, 1500.0, 1100.0, 1300.0, 1600.0};
    double totale = 0.0;

    for (int i = 0; i < 6; ++i) {
        totale = totale + vendite[i];
        std::cout << "Mese " << (i + 1) << ": " << vendite[i] << '\n';
    }
    std::cout << "Totale semestre: " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Elemento | Ruolo |
|----------|--------|
| `vendite[6]` | Sei celle contigue di `double` |
| `i` da 0 a 5 | Visita ogni locker una volta |
| `totale = totale + vendite[i]` | Accumulo (stesso schema del `while` contabile) |

> 🔗 Copia il programma su [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva l’array nella memoria.

#### 4. MODIFY (Modifica)
1. Cambia un valore in inizializzazione e verifica il nuovo totale.
2. Stampa anche la **media** (`totale / 6`).
3. Trova e stampa il **mese con fatturato massimo** (indice + valore).

#### 5. MAKE (Crea)
**Scenario SIA — Controllo vendite annuali**

Scrivi `controllo_vendite.cpp`:
- Array di **12** `double` (un anno)
- Inizializza con valori di esempio (o input se preferisci)
- Stampa totale, media, mese di massimo fatturato (1–12, non 0–11 in output)
- Documentazione Doxygen se superi ~15 righe

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    double vendite[12] = {/* ... */};
    // totale, media, max
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Array = fila di sportelli **stesso tipo**, indici da **0**
- L’ultimo indice valido è **N − 1**
- Fuori range = bug silenzioso tipico
- Si scorre quasi sempre con un `for`

---

### ➡️ Prossimo chunk
Quando i dati sono a **griglia** (reparti × mesi), serve un array a **due dimensioni**.
