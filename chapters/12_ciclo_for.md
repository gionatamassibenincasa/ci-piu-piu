---
activity_id: for-01
title: 'Il contatore compatto: ripetere con il ciclo for'
methodology: PRIMM
assignment_profile: full
order: 12
version: '2026-11-20'
last_update: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      for (int i = 0; i < 5; ++i) {
          std::cout << i << "\n";
      }
    items:
      - question: 'Quali valori vengono stampati dal ciclo?'
        options:
          - text: '`0, 1, 2, 3, 4`, perché il ciclo si ferma prima di 5'
            correct: true
          - text: '`1, 2, 3, 4, 5`, perché il contatore parte sempre da 1'
            correct: false
          - text: '`0, 1, 2, 3`, perché il ciclo esegue quattro giri'
            correct: false
      - question: 'Quante volte viene eseguito il corpo del `for`?'
        options:
          - text: 'Cinque volte, per i valori da 0 a 4'
            correct: true
          - text: 'Sei volte, perché il valore 5 viene incluso'
            correct: false
          - text: 'Una sola volta, perché `i` viene dichiarata nell''intestazione'
            correct: false
      - question: 'Perché la condizione è `i < 5` e non `i <= 5` se vuoi cinque iterazioni?'
        options:
          - text: 'Con `i < 5` i valori validi sono 0, 1, 2, 3 e 4'
            correct: true
          - text: 'Perché `<=` non può mai essere usato in un ciclo'
            correct: false
          - text: 'Perché il contatore viene aggiornato prima del primo giro'
            correct: false
      - question: 'Quale ruolo ha `++i` nell''intestazione?'
        options:
          - text: 'Aumenta il contatore dopo ogni esecuzione del corpo'
            correct: true
          - text: 'Imposta `i` a zero prima di ogni giro'
            correct: false
          - text: 'Decide quale testo deve stampare `std::cout`'
            correct: false
      - question: 'Perché un `for` è adatto a dodici mesi di un report?'
        options:
          - text: 'Il numero di ripetizioni è noto e il contatore può avanzare da 1 a 12'
            correct: true
          - text: 'Un `for` è obbligatorio ogni volta che si usano numeri interi'
            correct: false
          - text: 'Il `for` serve soltanto per leggere dati fino a una sentinella'
            correct: false
  investigate_quiz:
    code: |
      const int NUMERO_ANNI = 5;
      double valoreResiduo = 10000.0;
      const double QUOTA_ANNUA = 2000.0;

      for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
          valoreResiduo = valoreResiduo - QUOTA_ANNUA;
      }
    items:
      - question: 'Quando viene eseguita l''inizializzazione `int anno = 1`?'
        options:
          - text: 'Una sola volta, prima del primo controllo della condizione'
            correct: true
          - text: 'Dopo ogni iterazione, per riportare l''anno a 1'
            correct: false
          - text: 'Solo quando il valore residuo diventa zero'
            correct: false
      - question: 'Quale sequenza descrive correttamente un giro del `for`?'
        options:
          - text: 'Controllo condizione → corpo → aggiornamento del contatore'
            correct: true
          - text: 'Corpo → inizializzazione → condizione → aggiornamento'
            correct: false
          - text: 'Aggiornamento → corpo → condizione, senza controllo iniziale'
            correct: false
      - question: 'Perché dopo cinque iterazioni `valoreResiduo` vale `0.0`?'
        options:
          - text: 'Ogni giro sottrae 2000 dal valore iniziale di 10000'
            correct: true
          - text: 'Il `for` azzera automaticamente tutte le variabili alla fine'
            correct: false
          - text: 'La costante `QUOTA_ANNUA` viene sottratta due volte al primo giro'
            correct: false
      - question: 'Che cosa succede quando `anno` diventa `6`?'
        options:
          - text: 'La condizione `anno <= 5` è falsa e il ciclo termina'
            correct: true
          - text: 'Il corpo viene eseguito ancora una volta per il valore finale'
            correct: false
          - text: 'Il contatore torna automaticamente a 1'
            correct: false
      - question: 'Perché il numero di iterazioni è prevedibile in `for (int anno = 1; anno <= 5; ++anno)`?'
        options:
          - text: 'Inizializzazione, limite e aggiornamento definiscono un percorso chiuso'
            correct: true
          - text: 'Il compilatore conta le righe stampate invece dei valori di `anno`'
            correct: false
          - text: 'Il ciclo termina quando una variabile decimale diventa negativa'
            correct: false
  modify_quiz:
    code: |
      for (int anno = 1; anno <= 5; ++anno) {
          std::cout << anno << "\n";
      }
    items:
      - question: 'Quale modifica stampa dodici mesi invece di cinque anni?'
        options:
          - text: 'Sostituire il limite `5` con `12` mantenendo `anno = 1` e `++anno`'
            correct: true
          - text: 'Cambiare `++anno` in `--anno`'
            correct: false
          - text: 'Spostare `anno = 1` dentro il corpo'
            correct: false
      - question: 'Quale modifica fa partire il conteggio da 0 e arrivare fino a 4?'
        options:
          - text: 'Usare `int anno = 0; anno < 5; ++anno`'
            correct: true
          - text: 'Usare `int anno = 1; anno <= 4; --anno`'
            correct: false
          - text: 'Usare `int anno = 5; anno < 0; ++anno`'
            correct: false
      - question: 'Che effetto ha cambiare `anno <= 5` in `anno < 5` in un ciclo che parte da 1?'
        options:
          - text: 'Il ciclo esegue gli anni da 1 a 4, quindi una iterazione in meno'
            correct: true
          - text: 'Il ciclo esegue gli anni da 1 a 5 come prima'
            correct: false
          - text: 'Il ciclo parte da zero senza modificare l''inizializzazione'
            correct: false
      - question: 'Quale modifica permette un conto alla rovescia da 5 a 1?'
        options:
          - text: 'Usare `int anno = 5; anno >= 1; --anno`'
            correct: true
          - text: 'Usare `int anno = 1; anno <= 5; ++anno`'
            correct: false
          - text: 'Usare `int anno = 5; anno <= 1; ++anno`'
            correct: false
      - question: 'Perché conviene modificare una sola parte dell''intestazione alla volta?'
        options:
          - text: 'Per capire se il risultato è cambiato per inizializzazione, condizione o aggiornamento'
            correct: true
          - text: 'Perché un `for` può contenere una sola modifica in tutto il programma'
            correct: false
          - text: 'Perché il corpo del ciclo non può essere eseguito dopo una modifica'
            correct: false
  make_instructions: >
    Crea `interesse_composto.cpp`: simula per sei anni un deposito aziendale
    con capitale iniziale 10000.00 e tasso costante 0.04. A ogni anno calcola
    gli interessi, aggiorna il capitale e stampa anno, interessi e capitale.
  visualization:
    kind: pythontutor
    note: 'Seguire il contatore anno e il capitale dopo ogni iterazione.'
registro:
  argomenti: 'Ciclo `for`; inizializzazione, condizione e aggiornamento nell''intestazione; conteggio noto; tabella di ammortamento e simulazione finanziaria.'
  note: 'Laboratorio PRIMM su un piano di ammortamento a quote costanti.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Prevedere valori e numero di iterazioni usando limite e aggiornamento del contatore.'
  investigate:
    points: 2
    questions:
      - 'Qual è l''ordine tra condizione, corpo e aggiornamento?'
      - 'Perché il contatore assume i valori da 1 a 5?'
      - 'Che cosa accade quando il contatore supera il limite?'
    typical_errors:
      - 'Contare anche il valore escluso dalla condizione `<`'
      - 'Pensare che l''inizializzazione si ripeta a ogni giro'
    context: 'Seguire il tracing di contatore e valore residuo.'
  modify:
    points: 1
    prompt: 'Modifica il ciclo affinché stampi dodici righe, una per ogni mese, partendo da 1.'
    code: |
      for (int periodo = 1; periodo <= 5; ++periodo) {
          std::cout << periodo << "\n";
      }
    typical_errors:
      - 'Cambiare solo il testo senza cambiare il limite'
      - 'Usare `periodo < 12` partendo da 1 e ottenere undici iterazioni'
    context: 'Adattare limite e nome del contatore a un numero noto di periodi.'
  make:
    points: 1
    prompt: 'Simula sei anni di interesse composto con un ciclo `for`, aggiornando capitale e interessi annuali.'
    must_include:
      - 'for'
      - 'double'
      - 'const double'
      - 'std::cout'
    typical_errors:
      - 'Dimenticare di aggiornare il capitale dentro il ciclo'
      - 'Usare un limite che produce cinque o sette anni'
    context: 'Trasferire il conteggio noto a una simulazione economica.'
  variants:
    B:
      modify:
        prompt: 'Modifica il ciclo per stampare sei rate numerate da 1 a 6, mantenendo l''aggiornamento crescente.'
        code: |
          for (int periodo = 1; periodo <= 5; ++periodo) {
              std::cout << periodo << "\n";
          }
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

      Rispondi prima di eseguire il programma.

      1. Quali valori stampa il contatore?
      >

      2. Quante iterazioni esegue?
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

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Qual è l'ordine tra condizione, corpo e aggiornamento?
      >

      2. Perché il contatore assume i valori da 1 a 5?
      >

      3. Che cosa accade quando il contatore supera il limite?
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
    validation_rules:
      min_lines: 7
      must_contain:
        - for
        - ++anno
  - path: student_work/make/interesse_composto.cpp
    action: create
    phase: make
    description: Simulazione di capitalizzazione composta su sei anni.
    template_content: |
      /**
       * @brief Simula la capitalizzazione composta su un deposito aziendale.
       */
      #include <iostream>

      int main() {
          /// TODO: spiega perché il tasso resta costante nella simulazione.
          // TODO: dichiara capitale, tasso, anni e scrivi il for.
          return 0;
      }
    validation_rules:
      min_lines: 10
      must_contain:
        - for
        - double
---

## ⏳ Il contatore compatto: ripetere con il ciclo `for`

Il `while` è utile quando non sai in anticipo quanti giri farai, come nel
registro delle fatture che termina con una sentinella. In azienda, però, molte
ripetizioni sono già note: dodici mesi, cinque anni di ammortamento, ventiquattro
rate.

Il ciclo `for` raccoglie in una sola riga inizializzazione, condizione e
aggiornamento del contatore.

> 💡 **Metafora:** Immagina il timer di una macchina industriale. Imposti:
> “parti da 1, fermati a 5, avanza di 1 a ogni scatto”. La macchina ripete il
> lavoro senza che tu debba ricordarti di aggiornare manualmente il contatore.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un `for` per ripetere un calcolo un numero noto di volte.

---

### ⚙️ Prima del laboratorio: `for` e `while`

Questi due cicli possono esprimere la stessa logica:

```cpp
int anno = 1;
while (anno <= 5) {
    std::cout << anno << "\n";
    anno = anno + 1;
}

for (int anno = 1; anno <= 5; ++anno) {
    std::cout << anno << "\n";
}
```

| Parte del `for` | Ruolo | Quando avviene |
| :--- | :--- | :--- |
| `int anno = 1` | Inizializzazione | Una volta, prima del primo controllo |
| `anno <= 5` | Condizione | Prima di ogni iterazione |
| `++anno` | Aggiornamento | Dopo il corpo di ogni iterazione |

---

### 🧭 Prima del laboratorio: il timer dei periodi

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Inizializza il contatore;
while (Condizione vera?) is (sì)
  :Esegui il corpo;
  :Aggiorna il contatore;
endwhile (no)
:Continua dopo il ciclo;
stop
@enduml
```

Con `for (int anno = 1; anno <= 5; ++anno)`:

| Iterazione | Valore usato nel corpo |
| :---: | :---: |
| 1 | `1` |
| 2 | `2` |
| 3 | `3` |
| 4 | `4` |
| 5 | `5` |

Quando il contatore diventa `6`, la condizione `anno <= 5` è falsa e il corpo
non viene più eseguito.

---

### 🔬 Laboratorio PRIMM: piano di ammortamento

Un'azienda distribuisce il costo di un cespite in cinque quote annuali uguali.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma completo e osserva una riga per ogni anno.

```cpp
/**
 * @file ammortamento_cespite.cpp
 * @brief Calcola un piano di ammortamento a quote costanti.
 */
#include <iostream>

/**
 * @brief Stampa quota annuale e valore residuo di un cespite.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il costo è la base economica da distribuire negli anni.
    const double COSTO_CESPITE = 10000.0;
    /// Il numero di anni è noto prima di iniziare il piano.
    const int NUMERO_ANNI = 5;
    /// La quota costante rende confrontabili gli anni del piano.
    const double QUOTA_ANNUA = COSTO_CESPITE / NUMERO_ANNI;
    double valoreResiduo = COSTO_CESPITE;

    std::cout << "Anno  Quota  Residuo\n";

    for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
        valoreResiduo = valoreResiduo - QUOTA_ANNUA;
        std::cout << anno << "     " << QUOTA_ANNUA
                  << "    " << valoreResiduo << "\n";
    }

    return 0;
}
```
@LIA.cpp

Il programma stampa cinque righe. Nell'ultima, il valore residuo arriva a
`0.0`.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine tra contatore, quota e residuo.

[[ investigate_block() ]]

| Anno | Quota sottratta | Residuo dopo il giro |
| :---: | :---: | :---: |
| 1 | `2000` | `8000` |
| 2 | `2000` | `6000` |
| 3 | `2000` | `4000` |
| 4 | `2000` | `2000` |
| 5 | `2000` | `0` |

L'inizializzazione di `anno` avviene una sola volta. Dopo ogni riga del corpo
viene eseguito `++anno`; solo allora il programma verifica se può fare un altro
giro.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva `anno` e
> `valoreResiduo` dopo ogni iterazione.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
    valoreResiduo = valoreResiduo - QUOTA_ANNUA;
}
```

</details>

**Modifica A — aggiungi il fondo ammortamento**

Dichiara `double fondo = 0.0` prima del ciclo. A ogni giro aggiungi
`QUOTA_ANNUA` al fondo e stampalo insieme al residuo.

**Modifica B — usa dodici periodi**

Imposta `NUMERO_ANNI` a `12` e interpreta ogni iterazione come un mese.
Verifica che il ciclo produca esattamente dodici righe.

**Modifica C — conto alla rovescia**

Sostituisci l'intestazione con:

```cpp
for (int periodo = NUMERO_ANNI; periodo >= 1; --periodo)
```

Adatta la stampa in modo che il numero del periodo sia comprensibile.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio finanziario simula la capitalizzazione
composta di un deposito aziendale.

Crea `interesse_composto.cpp` rispettando tutti i requisiti:

1. Dichiara `double capitale = 10000.00`.
2. Dichiara `const double TASSO = 0.04`.
3. Dichiara `const int ANNI = 6`.
4. Usa un `for` da `1` a `ANNI`.
5. A ogni giro calcola `interessi = capitale * TASSO`.
6. Aggiorna `capitale` aggiungendo gli interessi.
7. Stampa anno, interessi e nuovo capitale.
8. Stampa il guadagno netto finale rispetto a `10000.00`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Simula la capitalizzazione composta su un deposito aziendale.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché il tasso resta costante nella simulazione.
    // TODO: dichiara capitale, tasso, anni e scrivi il for.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Usa `for` quando il numero di ripetizioni è noto.
- L'intestazione contiene inizializzazione, condizione e aggiornamento.
- La condizione viene controllata prima di ogni iterazione.
- Con `<` il valore limite non viene incluso; con `<=` può essere incluso.
- Per dati a sentinella e numero di giri sconosciuto resta adatto il `while`.

---

### ➡️ Prossimo chunk

A volte il corpo deve essere eseguito almeno una volta, per esempio quando
chiedi un dato prima di poter controllare se è valido. Nel prossimo capitolo
userai il ciclo `do-while`, con il controllo in coda.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra timer e for
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli già introdotti
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/11_ciclo_for.md
#-->
