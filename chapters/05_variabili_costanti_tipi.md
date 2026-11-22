---
activity_id: variabili-tipi-01
title: 'Gli sportelli della memoria: variabili, costanti e tipi'
methodology: PRIMM
assignment_profile: full
order: 5
version: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      int pezzi = 7.85;
      double prezzo = 19.50;
      const double IVA = 0.22;
    items:
      - question: 'Perché `int pezzi = 7.85;` non conserva tutti i decimali?'
        options:
          - text: 'Perché `int` rappresenta numeri interi e la parte decimale viene troncata'
            correct: true
          - text: 'Perché il compilatore arrotonda sempre i prezzi per difetto'
            correct: false
          - text: 'Perché ogni numero con la virgola produce un errore obbligatorio'
            correct: false
      - question: 'Quale tipo è più adatto per memorizzare un prezzo con i centesimi?'
        options:
          - text: '`double`, perché può rappresentare valori con parte decimale'
            correct: true
          - text: '`int`, perché i prezzi sono sempre conteggi di pezzi'
            correct: false
          - text: '`char`, perché ogni prezzo è una singola cifra'
            correct: false
      - question: 'Perché `IVA` dovrebbe essere dichiarata `const`?'
        options:
          - text: 'Per impedire che il valore venga cambiato accidentalmente durante il programma'
            correct: true
          - text: 'Per permettere al programma di modificarla più velocemente'
            correct: false
          - text: 'Perché `const` trasforma automaticamente il numero in una stringa'
            correct: false
      - question: "Quale tipo descrive meglio il codice di reparto `'A'`?"
        options:
          - text: '`char`, perché contiene un solo carattere'
            correct: true
          - text: '`std::string`, perché ogni carattere è sempre una frase'
            correct: false
          - text: '`bool`, perché il reparto può essere vero o falso'
            correct: false
      - question: 'Che cosa indica la dichiarazione `bool haFido = true;`?'
        options:
          - text: 'Un dato con due stati possibili, qui impostato sul valore vero'
            correct: true
          - text: 'Un testo composto dalle lettere `true`'
            correct: false
          - text: 'Un numero decimale uguale a 1.0'
            correct: false
  investigate_quiz:
    code: |
      const double ALIQUOTA_IVA = 0.22;
      int pezzi = 42;
      double prezzoNetto = 19.50;
    items:
      - question: 'Perché `pezzi` è un `int` mentre `prezzoNetto` è un `double`?'
        options:
          - text: 'I pezzi sono conteggi interi, mentre il prezzo può contenere centesimi'
            correct: true
          - text: 'I nomi delle variabili decidono automaticamente il tipo'
            correct: false
          - text: '`double` serve solo per dati più importanti di `int`'
            correct: false
      - question: 'Quale sequenza descrive la dichiarazione `double prezzoNetto = 19.50;`?'
        options:
          - text: 'Il compilatore riserva un dato decimale, gli assegna un nome e gli dà un valore iniziale'
            correct: true
          - text: 'Il programma stampa subito 19.50 senza bisogno di `std::cout`'
            correct: false
          - text: 'Il valore viene sigillato e non potrà mai cambiare'
            correct: false
      - question: 'Perché `ALIQUOTA_IVA` non può essere assegnata di nuovo?'
        options:
          - text: 'La parola `const` la rende di sola lettura dopo l''inizializzazione'
            correct: true
          - text: 'I nomi scritti in maiuscolo sono sempre immutabili in C++'
            correct: false
          - text: 'Un `double` può essere assegnato una sola volta'
            correct: false
      - question: 'Quale valore viene memorizzato in `int pezzi = 7.85;`?'
        options:
          - text: '`7`, perché la parte decimale non appartiene al tipo `int`'
            correct: true
          - text: '`8`, perché C++ arrotonda al numero intero più vicino'
            correct: false
          - text: '`7.85`, perché il tipo dichiarato non influenza il valore'
            correct: false
      - question: 'Perché il programma ha bisogno di `#include <string>` quando usa `std::string`?'
        options:
          - text: 'Per rendere disponibile la definizione del tipo per il testo'
            correct: true
          - text: 'Per convertire automaticamente tutti i numeri in testo'
            correct: false
          - text: 'Per permettere a `int` di contenere più cifre'
            correct: false
  modify_quiz:
    code: |
      const double ALIQUOTA_IVA = 0.22;
      double prezzoNetto = 19.50;
    items:
      - question: 'Quale modifica permette di calcolare l''importo dell''IVA?'
        options:
          - text: 'Dichiarare `double importoIva = prezzoNetto * ALIQUOTA_IVA;`'
            correct: true
          - text: 'Dichiarare `int importoIva = prezzoNetto + ALIQUOTA_IVA;`'
            correct: false
          - text: 'Cambiare `const` in `std::string` senza eseguire un calcolo'
            correct: false
      - question: 'Che cosa succede se aggiungi `ALIQUOTA_IVA = 0.10;`?'
        options:
          - text: 'Il compilatore segnala un errore perché la costante è di sola lettura'
            correct: true
          - text: 'L''aliquota cambia solo per la riga successiva'
            correct: false
          - text: 'Il programma ignora sempre la nuova assegnazione e compila'
            correct: false
      - question: 'Quale modifica è corretta se la giacenza deve diventare 100 pezzi?'
        options:
          - text: 'Cambiare il valore iniziale in `int pezziInMagazzino = 100;`'
            correct: true
          - text: 'Cambiare il tipo in `char` e lasciare il valore `100`'
            correct: false
          - text: 'Dichiarare la giacenza come `const` per poterla aggiornare'
            correct: false
      - question: 'Quale effetto ha cambiare `bool haGaranziaEstesa = true;` in `false`?'
        options:
          - text: 'Il dato rappresenta l''assenza della garanzia estesa e l''output numerico diventa `0`'
            correct: true
          - text: 'Il programma non può più compilare perché `bool` accetta solo `true`'
            correct: false
          - text: 'La variabile diventa automaticamente una stringa vuota'
            correct: false
      - question: 'Perché conviene modificare un tipo o un valore alla volta?'
        options:
          - text: 'Per distinguere quale modifica ha prodotto il nuovo comportamento o l''errore'
            correct: true
          - text: 'Perché ogni programma C++ può avere una sola variabile'
            correct: false
          - text: 'Perché il compilatore non sa leggere due righe consecutive'
            correct: false
  make_instructions: >
    Crea `conto_corrente.cpp` per una scheda di conto aziendale: usa `std::string` per
    banca e IBAN, `double` per saldo e interesse, `const double` per il tasso,
    `bool` per il fido e `char` per il rating; stampa i dati e calcola
    `saldo * tasso` senza modificare la costante.
  visualization:
    kind: pythontutor
    note: 'Osservare nello stack nome, tipo e valore delle variabili e distinguere la costante in sola lettura.'
registro:
  argomenti: 'Variabili e costanti C++; tipi `int`, `double`, `char`, `bool`, `std::string`; inizializzazione, conversione da `double` a `int`, qualificatore `const`; laboratorio PRIMM su una scheda articolo.'
  note: 'Verifica formativa su scelta del tipo e modifica controllata di dati aziendali.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Scegliere il tipo coerente con il significato aziendale e prevedere il troncamento di un decimale in `int`.'
  investigate:
    points: 2
    questions:
      - 'Perché `pezziInMagazzino` è un `int` e `prezzoNetto` un `double`?'
      - 'Perché una variabile `const` non può essere assegnata di nuovo?'
      - 'Quale valore viene memorizzato in `int pezzi = 7.85;`?'
    typical_errors:
      - 'Confondere troncamento e arrotondamento'
      - 'Pensare che il maiuscolo renda automaticamente una variabile costante'
    context: 'Collegare tipo, significato del dato e regole di modifica.'
  modify:
    points: 1
    prompt: 'Aggiungi il calcolo dell''IVA a un prezzo netto usando la costante `ALIQUOTA_IVA` e una nuova variabile `double`.'
    code: |
      const double ALIQUOTA_IVA = 0.22;
      double prezzoNetto = 19.50;
    typical_errors:
      - 'Somma l''aliquota al prezzo invece di moltiplicare'
      - 'Dichiara il risultato come `int` perdendo i decimali'
    context: 'Usare il tipo decimale e la costante nel calcolo di un importo.'
  make:
    points: 1
    prompt: 'Crea la scheda di un conto corrente aziendale con banca, IBAN, saldo, tasso costante, fido e rating; stampa i dati e l''interesse annuo stimato.'
    must_include:
      - 'const double'
      - 'std::string'
      - 'double'
      - 'bool'
      - 'char'
    typical_errors:
      - 'Usa `int` per il saldo o per il tasso'
      - 'Dimentica `#include <string>`'
    context: 'Scegliere i tipi in base al significato dei dati di una scheda aziendale.'
  variants:
    B:
      modify:
        prompt: 'Sostituisci il prezzo netto con `125.75` e calcola l''importo IVA mantenendo `ALIQUOTA_IVA` costante.'
        code: |
          const double ALIQUOTA_IVA = 0.22;
          double prezzoNetto = 19.50;
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Variabili, costanti e tipi

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Usa Python Tutor durante Investigate per osservare gli sportelli della memoria.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Tipi

      Rispondi prima di eseguire il programma.

      1. Quale tipo sceglieresti per pezzi, prezzo e codice reparto?
      >

      2. Che cosa succede assegnando `7.85` a un `int`?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Scheda articolo

      1. Quali valori stampa il programma?
      >

      2. Come vengono mostrati `true` e `false`?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Sportelli della memoria

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Perché `pezziInMagazzino` è un `int` e `prezzoNetto` un `double`?
      >

      2. Perché una variabile `const` non può essere assegnata di nuovo?
      >

      3. Quale valore viene memorizzato in `int pezzi = 7.85;`?
      >
  - path: student_work/modify/scheda_articolo.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          const double ALIQUOTA_IVA = 0.22;
          double prezzoNetto = 19.50;
          return 0;
      }
    validation_rules:
      min_lines: 7
      must_contain:
        - const
        - double
  - path: student_work/make/conto_corrente.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <string>

      int main() {
          /// TODO: spiega perché il tasso è una costante del conto.
          // TODO: dichiara banca, IBAN, saldo, tasso, fido e rating
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain:
        - const
        - double
        - std::string
---

## 📦 Gli sportelli della memoria: variabili, costanti e tipi

> "Chi controlla il passato controlla il futuro.
> Chi controlla il presente controlla il passato."
>
> -- George Orwell

Finora hai stampato testi fissi. Un software gestionale, però, deve ricordare
dati che cambiano: prezzo di un articolo, giacenza di magazzino, saldo di un
conto.

Per farlo usi variabili e costanti.

> 💡 **Metafora:** Immagina la memoria RAM come una parete di sportelli
> automatici. Il nome della variabile è l'etichetta che leggi tu; il tipo
> indica quale merce può entrare nello sportello; il valore è la merce
> conservata. Uno sportello `const` è sigillato: dopo averlo riempito non puoi
> cambiare il contenuto.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- dichiarare variabili e costanti scegliendo il tipo adatto a un dato aziendale.

In questo chunk non chiediamo ancora dati da tastiera con `std::cin`: ci
concentriamo sul ricordare, mostrare e modificare valori già scritti nel codice.

---

### ⚙️ Prima del laboratorio: i tipi fondamentali

| Tipo | Che cosa contiene | Esempio aziendale |
| :--- | :--- | :--- |
| `int` | Numeri interi | `int giacenza = 42;` |
| `double` | Numeri con parte decimale | `double prezzo = 19.50;` |
| `char` | Un solo carattere | `char reparto = 'A';` |
| `bool` | Uno tra due stati | `bool inPromozione = true;` |
| `std::string` | Testo di lunghezza variabile | `std::string nome = "Mouse";` |
| `const T` | Valore non modificabile | `const double IVA = 0.22;` |

Per usare `std::string` inserisci `#include <string>`.

> ⚠️ **Trappola classica:** `int pezzi = 7.85;` non arrotonda a `8`.
> Conserva `7`, perché `int` non può contenere la parte decimale. Per prezzi,
> saldi e aliquote usa `double`.

---

### 🧭 Prima del laboratorio: dichiarare e sigillare

Una dichiarazione unisce tipo, nome e valore iniziale:

| Scrittura | Come leggerla |
| :--- | :--- |
| `int giacenza = 42;` | Uno sportello per un conteggio intero |
| `double prezzo = 19.50;` | Uno sportello per un valore con centesimi |
| `const double IVA = 0.22;` | Uno sportello sigillato con un valore decimale |

Il tipo non è una decorazione: stabilisce quali valori possono essere
conservati e quali operazioni hanno senso.

---

### 🔬 Laboratorio PRIMM: la scheda articolo

Un magazzino deve mostrare i dati di un articolo: descrizione, reparto,
giacenza, prezzo e garanzia. Ogni dato usa uno sportello adatto.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma completo oppure usa il bottone. Prima di eseguirlo, indica
accanto a ogni variabile quale tipo riconosci.

```cpp
/**
 * @file scheda_articolo.cpp
 * @brief Memorizza e mostra i dati di un articolo di magazzino.
 */
#include <iostream>
#include <string>

/**
 * @brief Mostra una scheda articolo con tipi di dato diversi.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// L'aliquota di legge deve restare uguale durante il calcolo.
    const double ALIQUOTA_IVA = 0.22;
    /// Il nome commerciale può cambiare tra articoli.
    std::string nomeArticolo = "Mouse Wireless Ottico";
    /// Un reparto aziendale può essere rappresentato da un codice breve.
    char codiceReparto = 'A';
    /// La giacenza conta pezzi interi presenti in magazzino.
    int pezziInMagazzino = 42;
    /// Il prezzo richiede i centesimi.
    double prezzoNetto = 19.50;
    /// La garanzia estesa ha soltanto due stati.
    bool haGaranziaEstesa = true;

    std::cout << "=== SCHEDA ARTICOLO MAGAZZINO ===\n";
    std::cout << "Descrizione : " << nomeArticolo << "\n";
    std::cout << "Reparto     : " << codiceReparto << "\n";
    std::cout << "Giacenza    : " << pezziInMagazzino << " pezzi\n";
    std::cout << "Prezzo netto: " << prezzoNetto << " euro\n";
    std::cout << "Garanzia    : " << haGaranziaEstesa << "\n";
    std::cout << "Aliquota IVA: " << ALIQUOTA_IVA << "\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

Ora collega ogni sportello al suo ruolo. Rispondi alle domande sul *perché*,
non solo sul valore stampato.

[[ investigate_block() ]]

| Nome | Tipo | Perché quel tipo? | Si può cambiare? |
| :--- | :--- | :--- | :--- |
| `ALIQUOTA_IVA` | `const double` | È un valore di legge | No |
| `nomeArticolo` | `std::string` | Contiene testo variabile | Sì |
| `codiceReparto` | `char` | Contiene un carattere | Sì |
| `pezziInMagazzino` | `int` | Conta pezzi interi | Sì |
| `prezzoNetto` | `double` | Contiene centesimi | Sì |
| `haGaranziaEstesa` | `bool` | Rappresenta sì/no | Sì |

Apri il programma su [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva come ogni variabile entra nello stack con un tipo e un valore.

Ricorda: senza `std::boolalpha`, `true` viene normalmente mostrato come `1` e
`false` come `0`.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    const double ALIQUOTA_IVA = 0.22;
    double prezzoNetto = 19.50;
    return 0;
}
```

</details>

**Modifica A — calcola l'IVA**

Dichiara una nuova variabile:

```cpp
double importoIva = prezzoNetto * ALIQUOTA_IVA;
```

Poi stampa `importoIva` e il prezzo lordo, ottenuto sommando
`prezzoNetto + importoIva`.

**Modifica B — prova il lucchetto**

Aggiungi questa riga dopo la dichiarazione della costante:

```cpp
ALIQUOTA_IVA = 0.10;
```

Ricompila e osserva l'errore:

```text
error: assignment of read-only variable 'ALIQUOTA_IVA'
```

La parola `const` ha impedito un'assegnazione successiva: il compilatore
protegge il valore sigillato.

**Modifica C — cambia il dato aziendale**

Sostituisci `19.50` con `125.75`, ricompila e osserva come cambiano IVA e
prezzo lordo senza cambiare il tipo.

#### 5. MAKE (Crea)

**Scenario aziendale:** devi preparare una scheda sintetica di un conto
corrente aziendale.

Scrivi `conto_corrente.cpp` rispettando tutti i requisiti:

1. Memorizza banca e IBAN con `std::string`.
2. Memorizza saldo e interesse con `double`.
3. Usa `const double` per il tasso annuo.
4. Usa `bool` per indicare se il conto ha un fido.
5. Usa `char` per la classe di rating.
6. Stampa tutti i dati e calcola `saldo * tasso`.
7. Non modificare la costante del tasso dopo l'inizializzazione.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Scheda sintetica di un conto corrente aziendale.
 */
#include <iostream>
#include <string>

int main() {
    /// Il tasso è costante perché rappresenta la condizione del conto.
    // TODO: dichiara banca, IBAN, saldo, tasso, fido e rating.
    // TODO: stampa i dati e l'interesse annuo stimato.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Una variabile è uno sportello con nome, tipo e valore.
- `int` serve per conteggi interi; `double` per valori con decimali.
- `char` contiene un carattere; `bool` rappresenta due stati; `std::string` contiene testo.
- `const` sigilla un valore dopo l'inizializzazione.
- Scegli il tipo in base al significato aziendale del dato.

---

### ➡️ Prossimo chunk

Ora che sai memorizzare dati con il tipo corretto, userai operatori ed
espressioni per calcolare totali, IVA e differenze in modo controllato.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra memoria e dati aziendali
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli necessari al capitolo
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/05_variabili_costanti_tipi.md
#-->
