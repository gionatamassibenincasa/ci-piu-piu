---
activity_id: "for-01"
title: "Il Contatore Compatto (Il Ciclo `for` )"
methodology: PRIMM
order: 11
version: "2026-11-14"
language: it
components:
  predict_quiz:
    question: "Quante righe stampa questo ciclo?"
    code: |
      for (int i = 0; i < 5; ++i) {
          std::cout << i << "\n";
      }
    options:
      - text: "5 righe: `1 2 3 4 5`"
        correct: false
      - text: "5 righe: `0 1 2 3 4`"
        correct: true
      - text: "4 righe: `0 1 2 3`"
        correct: false
      - text: "Ciclo infinito"
        correct: false
  make_instructions: "Scenario SIA — Interesse composto su deposito aziendale"
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Ciclo for

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Nel `for` controlla sempre inizio, condizione e avanzamento.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – For

      1. Quali valori stampa il contatore?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Ammortamento

      1. Quante righe della tabella vengono stampate?
      >
      2. Qual è il residuo finale?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Contatore

      1. Quando viene eseguito `++anno`?
      >
      2. Come cambia il valore residuo a ogni giro?
      >
  - path: student_work/modify/ammortamento_cespite.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          for (int anno = 1; anno <= 5; ++anno) {
              std::cout << anno << "\n";
          }
          return 0;
      }
  - path: student_work/make/interesse_composto.cpp
    action: create
    phase: make
    template_content: |
      /**
       * @brief Simula capitalizzazione composta su N anni.
       */
      #include <iostream>

      int main() {
          // capitale, tasso, anni; for; stampa guadagno netto
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain: ["int main"]
---

## ⏳ Il Contatore Compatto (Il Ciclo `for`)

> "La regolarità e la prevedibilità sono le migliori alleate della precisione contabile."
> — *Principio di Revisione Aziendale*

Il `while` è ideale quando **non sai quanti** giri farai (articoli al nastro, fatture fino alla sentinella).  
In azienda però molte ripetizioni sono **già note**: 5 anni di ammortamento, 12 mesi, 24 rate.

Con un `while` i tre ingredienti restano sparsi nel file: è facile dimenticare l’aggiornamento.  
Il ciclo **`for`** li raccoglie in **una sola riga**.

> 💡 **Metafora: timer del microonde / macchina industriale**  
> Imposti sul display: *“Parti da 1; fermati a 5; avanza di 1 a ogni scatto”*.  
> La macchina esegue la sequenza senza che tu debba ricordarti di far avanzare il contatore a mano.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un `for` per ripetere un calcolo un numero noto di volte

---

### ⚙️ Prima del laboratorio: `for` = `while` in forma compatta

```cpp
// while equivalente
int anno = 1;
while (anno <= 5) {
    // corpo
    anno = anno + 1;
}

// stessa logica con for
for (int anno = 1; anno <= 5; ++anno) {
    // corpo
}
```

| Parte nell’intestazione `for` | Ruolo |
|-------------------------------|--------|
| `int anno = 1` | **Inizializzazione** (una sola volta, all’ingresso) |
| `anno <= 5` | **Condizione** (prima di ogni iterazione) |
| `++anno` | **Aggiornamento** (dopo ogni corpo) |

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Init contatore;
while (Condizione?) is (sì)
  :Corpo;
  :Aggiorna contatore;
endwhile (no)
stop
@enduml
```

---

### 🧭 Prima del laboratorio: il timer conta prima di fermarsi

L'intestazione del `for` dice alla macchina industriale quando partire, quando
fermarsi e di quanto avanzare dopo ogni giro.

| Parte | Domanda a cui risponde |
|-------|-------------------------|
| Inizializzazione | Da quale numero parto? |
| Condizione | Posso fare un altro giro? |
| Aggiornamento | Come preparo il giro successivo? |

---

### 🔬 Laboratorio PRIMM: Piano di ammortamento

Costruiamo la tabella di ammortamento a quote costanti anno per anno.

#### 1. PREDICT (Prevedi)


[[ predict_block() ]]


<details>
<summary>💡 Spiegazione</summary>
<code>i</code> parte da <code>0</code>; la condizione è <code>i &lt; 5</code>; dopo ogni giro <code>++i</code>.  
Valori stampati: 0, 1, 2, 3, 4 — cinque righe.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ammortamento_cespite.cpp
 * @brief Piano di ammortamento a quote costanti su N anni.
 */
#include <iostream>

/**
 * @brief Stampa tabella anno / quota / valore residuo.
 * @return int 0 se ok.
 */
int main() {
    const double COSTO_CESPITE = 10000.0;
    const int NUMERO_ANNI = 5;
    const double QUOTA_ANNUA = COSTO_CESPITE / NUMERO_ANNI;

    double valoreResiduo = COSTO_CESPITE;

    std::cout << "Anno\tQuota\tResiduo\n";
    std::cout << "----\t-----\t-------\n";

    for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
        valoreResiduo -= QUOTA_ANNUA;
        std::cout << anno << "\t" << QUOTA_ANNUA << "\t" << valoreResiduo << "\n";
    }

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Con 5 anni e cespite 10000:

| anno | Quota | Residuo dopo |
|------|-------|--------------|
| 1 | 2000 | 8000 |
| 2 | 2000 | 6000 |
| … | … | … |
| 5 | 2000 | 0 |

> 🔗 Segui `anno` e `valoreResiduo` su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
    valoreResiduo -= QUOTA_ANNUA;
}
```

</details>

1. **Fondo ammortamento**  
   Prima del ciclo: `double fondo = 0.0;`.  
   A ogni giro: `fondo += QUOTA_ANNUA;` e stampalo in tabella.

2. **Conto alla rovescia**  
   ```cpp
   for (int anniRimanenti = NUMERO_ANNI; anniRimanenti >= 1; --anniRimanenti)
   ```
   Adatta la stampa in modo coerente.

3. **Dodici mesi**
   Imposta `NUMERO_ANNI` a `12` e interpreta ogni giro come un mese: verifica che
   il timer esegua esattamente dodici scatti.

#### 5. MAKE (Crea)
**Scenario SIA — Interesse composto su deposito aziendale**

Scrivi `interesse_composto.cpp`:

- `double capitale = 10000.00`
- `const double TASSO = 0.04` (4% annuo)
- `const int ANNI = 6`
- Ciclo `for` da anno 1 a `ANNI`:
  - interessi dell’anno = `capitale * TASSO`
  - aggiorna `capitale`
  - stampa: anno, interessi, nuovo capitale
- A fine ciclo: guadagno netto = capitale finale − 10000

**Requisiti:** Doxygen, `///` sulle grandezze finanziarie, tabella leggibile.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Simula capitalizzazione composta su N anni.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché il tasso resta costante per tutta la simulazione.
    // TODO: capitale, tasso, anni; for; stampa guadagno netto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `for` = quando il numero di ripetizioni è **noto** (o facile da esprimere con un contatore).
- Intestazione: `init; condizione; aggiornamento`.
- Stesso potere del `while`; forma più sicura per i conteggi regolari.
- Per input a sentinella resta preferibile il `while`.

---

### ➡️ Prossimo chunk
A volte il corpo del ciclo deve girare **almeno una volta** (es. chiedere un dato finché non è valido).  
Entra in scena il **`do-while`**: controllo in coda.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: for e conteggio noto
  [x] Metafora timer
  [x] Quiz sintassi corretta
  [x] Predict conteggio da 0
  [x] PRIMM ammortamento cespite
  [x] Make interesse composto (SIA)
  [x] do-while solo annunciato
-->
