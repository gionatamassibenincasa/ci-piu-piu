---
activity_id: chiedere-informazioni-01
title: 'Chiedere informazioni: leggere dati con std::cin'
methodology: PRIMM
assignment_profile: full
order: 6
version: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      int quantita;
      double prezzo;
      std::cin >> quantita;
      std::cin >> prezzo;
    items:
      - question: 'Che cosa fa `std::cin >> quantita;` quando il programma arriva a questa riga?'
        options:
          - text: 'Attende un valore da tastiera e lo memorizza nella variabile `quantita`'
            correct: true
          - text: 'Stampa il nome `quantita` sullo schermo'
            correct: false
          - text: 'Assegna automaticamente a `quantita` il valore zero'
            correct: false
      - question: 'Perché una variabile deve essere dichiarata prima di essere usata con `std::cin`?'
        options:
          - text: 'Il compilatore deve conoscere nome e tipo dello spazio in cui conservare il dato'
            correct: true
          - text: 'La tastiera può inviare dati solo a variabili dichiarate come `const`'
            correct: false
          - text: 'Senza dichiarazione `std::cin` stampa sempre un messaggio di errore a video'
            correct: false
      - question: 'Se il programma esegue prima `std::cin >> quantita;` e poi `std::cin >> prezzo;`, che cosa deve inserire l''utente?'
        options:
          - text: 'Prima un valore compatibile con `quantita`, poi uno compatibile con `prezzo`'
            correct: true
          - text: 'Un solo testo che contiene contemporaneamente nome e prezzo'
            correct: false
          - text: 'Prima il prezzo, perché `double` viene sempre letto per primo'
            correct: false
      - question: 'Perché il messaggio `Inserisci la quantità:` va scritto prima di `std::cin`?'
        options:
          - text: 'Per spiegare all''utente quale dato deve digitare prima che il programma attenda'
            correct: true
          - text: 'Perché `std::cin` legge solo dopo aver stampato almeno tre righe'
            correct: false
          - text: 'Per trasformare automaticamente un intero in una stringa'
            correct: false
      - question: 'Quale tipo è coerente con una quantità intera di prodotti?'
        options:
          - text: '`int`, perché una quantità di confezioni può essere un numero intero'
            correct: true
          - text: '`double`, perché ogni dato inserito da tastiera contiene decimali'
            correct: false
          - text: '`char`, perché la quantità è sempre un singolo carattere'
            correct: false
  investigate_quiz:
    code: |
      int quantita;
      double prezzoUnitario;

      std::cout << "Quantita: ";
      std::cin >> quantita;
      std::cout << "Prezzo: ";
      std::cin >> prezzoUnitario;
    items:
      - question: 'Qual è l''ordine corretto quando l''utente inserisce `3` e poi `12.50`?'
        options:
          - text: 'Il `3` entra in `quantita`, poi `12.50` entra in `prezzoUnitario`'
            correct: true
          - text: 'Entrambi i valori entrano nella stessa variabile `quantita`'
            correct: false
          - text: '`12.50` viene letto per primo perché è un numero decimale'
            correct: false
      - question: 'Perché `std::cin` non mostra da solo la richiesta "Quantita:"?'
        options:
          - text: '`std::cin` legge dati; il messaggio per l''utente deve essere scritto con `std::cout`'
            correct: true
          - text: 'La tastiera non permette di visualizzare messaggi'
            correct: false
          - text: 'Ogni variabile deve contenere il testo della richiesta'
            correct: false
      - question: 'Che cosa succede se inserisci `3` quando `std::cin` sta leggendo un `double`?'
        options:
          - text: 'Il valore può essere letto come `3.0`, perché un intero è compatibile con un numero decimale'
            correct: true
          - text: 'Il programma si chiude sempre senza leggere nulla'
            correct: false
          - text: 'Il numero viene trasformato in una parola composta da tre caratteri'
            correct: false
      - question: 'Perché l''istruzione `double totale = quantita * prezzoUnitario;` deve venire dopo le due letture?'
        options:
          - text: 'Prima di quel punto le variabili potrebbero non contenere ancora i dati inseriti dall''utente'
            correct: true
          - text: 'Le moltiplicazioni in C++ sono permesse solo nell''ultima riga di `main`'
            correct: false
          - text: '`std::cin` cancella i valori se il calcolo viene scritto prima'
            correct: false
      - question: 'Se inserisci testo come `tre` quando `std::cin` attende un `int`, perché il calcolo successivo è inaffidabile?'
        options:
          - text: 'La lettura fallisce e la variabile non riceve il numero atteso'
            correct: true
          - text: 'C++ converte sempre automaticamente ogni parola nel numero corretto'
            correct: false
          - text: 'Il testo viene memorizzato nell''intero come se fosse un carattere'
            correct: false
  modify_quiz:
    code: |
      int quantita;
      double prezzoUnitario;

      std::cout << "Quantita: ";
      std::cin >> quantita;
      std::cout << "Prezzo: ";
      std::cin >> prezzoUnitario;
    items:
      - question: 'Quale modifica permette di leggere anche uno sconto percentuale?'
        options:
          - text: 'Dichiarare `double sconto;` e aggiungere `std::cin >> sconto;` dopo il prezzo'
            correct: true
          - text: 'Scrivere `std::cin << sconto;` senza dichiarare la variabile'
            correct: false
          - text: 'Cambiare `quantita` in `const double` per ricevere un nuovo dato'
            correct: false
      - question: 'Se vuoi leggere prima il prezzo e poi la quantità, quale modifica è necessaria?'
        options:
          - text: 'Invertire sia i messaggi sia l''ordine delle due istruzioni `std::cin`'
            correct: true
          - text: 'Cambiare solo i nomi delle variabili, lasciando invariato il codice'
            correct: false
          - text: 'Usare `std::cout` al posto di entrambe le istruzioni di lettura'
            correct: false
      - question: 'Che effetto ha aggiungere `std::cout << " euro\n";` dopo il totale?'
        options:
          - text: 'Aggiunge l''unità di misura all''output, senza cambiare il calcolo'
            correct: true
          - text: 'Converte il totale in un intero arrotondato'
            correct: false
          - text: 'Fa inserire un altro prezzo all''utente'
            correct: false
      - question: 'Quale modifica conserva i centesimi del prezzo inserito?'
        options:
          - text: 'Dichiarare il prezzo come `double` e leggerlo con `std::cin`'
            correct: true
          - text: 'Dichiarare il prezzo come `int` perché è più semplice'
            correct: false
          - text: 'Leggere il prezzo in un `char` e poi moltiplicarlo'
            correct: false
      - question: 'Perché conviene aggiungere una sola lettura o modifica alla volta?'
        options:
          - text: 'Per capire quale passaggio ha causato un errore o un ordine di input inatteso'
            correct: true
          - text: 'Perché `std::cin` può leggere una sola variabile in tutta la funzione'
            correct: false
          - text: 'Perché ogni nuova variabile cancella automaticamente la precedente'
            correct: false
  make_instructions: >
    Crea `preventivo.cpp` per un preventivo aziendale: chiedi con `std::cin` codice
    quantità e prezzo unitario, calcola il totale e stampa un riepilogo. Usa tre
    variabili dichiarate prima della lettura e mantieni l''ordine delle richieste.
  visualization:
    kind: pythontutor
    note: 'Seguire il valore iniziale delle variabili e il momento in cui std::cin lo sostituisce con l''input.'
registro:
  argomenti: 'Input da tastiera con `std::cin`; operatore `>>`; ordine tra prompt, lettura e calcolo; compatibilità tra tipi e dati inseriti; laboratorio PRIMM su un ordine POS.'
  note: 'Verifica formativa: leggere quantità e prezzo e calcolare un totale.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Prevedere il ruolo di `std::cin`, la necessità della dichiarazione e l''ordine delle letture.'
  investigate:
    points: 2
    questions:
      - 'Perché `std::cout` e `std::cin` svolgono ruoli diversi?'
      - 'Quale valore riceve ciascuna variabile se l''utente inserisce `3` e `12.50`?'
      - 'Perché inserire testo in una lettura `int` rende il calcolo inaffidabile?'
    typical_errors:
      - 'Invertire il verso degli operatori `<<` e `>>`'
      - 'Confondere ordine del prompt e ordine della lettura'
    context: 'Distinguere output e input e seguire i valori nel flusso del programma.'
  modify:
    points: 1
    prompt: 'Aggiungi al programma una lettura dello sconto percentuale e stampa il dato inserito.'
    code: |
      int quantita;
      double prezzoUnitario;

      std::cout << "Quantita: ";
      std::cin >> quantita;
      std::cout << "Prezzo: ";
      std::cin >> prezzoUnitario;
    typical_errors:
      - 'Usare `std::cin << sconto` invece di `std::cin >> sconto`'
      - 'Dimenticare di dichiarare la nuova variabile'
    context: 'Aggiungere una lettura mantenendo dichiarazione, prompt e ordine.'
  make:
    points: 1
    prompt: 'Crea un preventivo che chieda quantità e prezzo unitario, calcoli il totale e stampi un riepilogo.'
    must_include:
      - 'std::cin'
      - 'std::cout'
      - 'double'
      - 'int'
    typical_errors:
      - 'Calcolare il totale prima delle letture'
      - 'Usare `int` per il prezzo'
    context: 'Trasferire `std::cin` in un contesto aziendale chiuso e verificabile.'
  variants:
    B:
      modify:
        prompt: 'Aggiungi la lettura del numero di articoli resi dopo la quantità venduta e stampa entrambe le quantità.'
        code: |
          int quantita;
          double prezzoUnitario;

          std::cout << "Quantita: ";
          std::cin >> quantita;
          std::cout << "Prezzo: ";
          std::cin >> prezzoUnitario;
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Chiedere informazioni con std::cin

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Digita i dati richiesti e osserva come `std::cin` aggiorna le variabili.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Input da tastiera

      Rispondi prima di eseguire il programma.

      1. Quale variabile riceve il primo valore inserito?
      >

      2. Perché il tipo della variabile è importante?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Ordine POS

      1. Quali valori hai inserito?
      >

      2. Il totale corrisponde alla previsione?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Flusso dell'input

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Perché `std::cout` e `std::cin` svolgono ruoli diversi?
      >

      2. Quale valore riceve ciascuna variabile se l'utente inserisce `3` e `12.50`?
      >

      3. Perché inserire testo in una lettura `int` rende il calcolo inaffidabile?
      >
  - path: student_work/modify/ordine_pos.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          int quantita;
          double prezzoUnitario;
          std::cin >> quantita;
          std::cin >> prezzoUnitario;
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain:
        - std::cin
        - int
        - double
  - path: student_work/make/preventivo.cpp
    action: create
    phase: make
    description: Preventivo aziendale con quantità, prezzo e totale.
    template_content: |
      #include <iostream>

      int main() {
          /// TODO: spiega perché il prezzo deve conservare i centesimi.
          // TODO: dichiara i dati, leggili e calcola il totale
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain:
        - std::cin
        - std::cout
        - return
---

## 🧾 Chiedere informazioni: leggere dati con `std::cin`

Un gestionale non può lavorare soltanto con dati scritti in anticipo. Al POS
l'operatore inserisce una quantità; in un preventivo inserisce un prezzo; in
magazzino comunica quanti pezzi sono arrivati.

Con `std::cin` il tuo programma può aspettare un dato dalla tastiera e
conservarlo in una variabile.

> 💡 **Metafora:** Immagina un addetto allo sportello. `std::cout` è la voce
> con cui l'addetto fa una domanda; `std::cin` è il modulo su cui annota la
> risposta; la variabile è il campo del modulo destinato a quel dato. Se
> chiedi prima la quantità e poi il prezzo, devi registrare le risposte nello
> stesso ordine.

**In questa lezione non** correggiamo ancora gli input errati, non controlliamo
se i dati appartengono a un intervallo valido e non prendiamo decisioni con
`if`. Prima impariamo il percorso normale dalla tastiera alle variabili e al
calcolo.

---

### 🎯 Obiettivi di apprendimento

Alla fine di questa lezione sei in grado di:

- usare `std::cin >>` per assegnare dati inseriti dall'operatore alle variabili;
- coordinare prompt `std::cout`, ordine delle letture e tipi delle variabili;
- distinguere la direzione dei dati con `std::cin`, `std::cout`, `>>` e `<<`;
- calcolare un totale solo dopo aver letto quantità e prezzo unitario.

---

### ⚙️ Prima del laboratorio: input e output

| Istruzione | Direzione del dato | Esempio |
| :--- | :--- | :--- |
| `std::cout << valore` | Dal programma allo schermo | Mostra una richiesta o un risultato |
| `std::cin >> variabile` | Dalla tastiera alla variabile | Conserva ciò che l'utente inserisce |
| `int quantita;` | Prepara uno spazio per interi | Pezzi o confezioni |
| `double prezzo;` | Prepara uno spazio per decimali | Prezzi o importi |

La variabile deve esistere prima della lettura:

```cpp
int quantita;
std::cin >> quantita;
```

Il simbolo `>>` indica che il dato viaggia dalla tastiera verso la variabile.
Non confonderlo con `<<`, che usa la direzione opposta.

---

### 🧭 Prima del laboratorio: l'ordine del dialogo

Un dialogo utile segue questo percorso:

1. `std::cout` spiega quale dato inserire.
2. `std::cin` aspetta la risposta.
3. La variabile conserva il valore.
4. Il programma usa il valore nel calcolo o nel riepilogo.

Se il prezzo viene letto dopo la quantità, anche l'utente deve inserire prima la
quantità e poi il prezzo. Il computer non indovina l'ordine che avevi in mente.

---

### 🔬 Laboratorio PRIMM: un ordine al POS

Il POS deve leggere quantità e prezzo unitario per calcolare il totale di una
riga di vendita.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma completo. Quando compare una richiesta, inserisci un valore
e premi `Invio`; poi inserisci il valore successivo.

```cpp
/**
 * @file ordine_pos.cpp
 * @brief Legge quantità e prezzo per calcolare una riga di vendita.
 */
#include <iostream>

/**
 * @brief Acquisisce i dati di un ordine e calcola il totale.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// La quantità conta confezioni intere vendute.
    int quantita;
    /// Il prezzo deve conservare i centesimi dell'articolo.
    double prezzoUnitario;

    std::cout << "Quantita: ";
    std::cin >> quantita;

    std::cout << "Prezzo unitario: ";
    std::cin >> prezzoUnitario;

    double totale = quantita * prezzoUnitario;
    std::cout << "Totale: " << totale << " euro\n";

    return 0;
}
```
@LIA.cpp

Prova, per esempio, con:

```text
3
12.50
```

Il programma dovrebbe calcolare `37.5` euro.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci il percorso di ciascun dato. Concentrati sul
*perché* e sull'ordine, non soltanto sul totale.

[[ investigate_block() ]]

| Passo | Istruzione | Stato importante |
| :---: | :--- | :--- |
| 1 | `int quantita;` | Esiste uno spazio per un intero |
| 2 | `double prezzoUnitario;` | Esiste uno spazio per un decimale |
| 3 | `std::cin >> quantita;` | Il primo input entra in `quantita` |
| 4 | `std::cin >> prezzoUnitario;` | Il secondo input entra in `prezzoUnitario` |
| 5 | `double totale = ...` | Il calcolo usa i due valori letti |

`std::cin` non crea il messaggio per l'utente: legge soltanto. Per questo
`std::cout` deve precedere ogni lettura con una richiesta chiara.

Se inserisci `tre` quando il programma attende un `int`, la lettura non riceve
il numero previsto. Per ora non gestiamo ancora l'errore: impariamo prima il
percorso normale dei dati.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva come i valori
> inseriti sostituiscono il contenuto iniziale delle variabili.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    int quantita;
    double prezzoUnitario;

    std::cout << "Quantita: ";
    std::cin >> quantita;

    std::cout << "Prezzo unitario: ";
    std::cin >> prezzoUnitario;

    double totale = quantita * prezzoUnitario;
    std::cout << "Totale: " << totale << " euro\n";
    return 0;
}
```

</details>

**Modifica A — aggiungi uno sconto**

Dichiara `double sconto;`, mostra una richiesta e leggi la percentuale dopo il
prezzo unitario. Per ora stampa il valore inserito senza cambiare il totale.

**Modifica B — cambia l'ordine**

Fai chiedere prima il prezzo e poi la quantità. Inverti sia i messaggi sia le
istruzioni `std::cin`, così il dialogo resta coerente.

**Modifica C — aggiungi l'unità di misura**

Completa la stampa del totale con il testo `euro`. Il testo cambia l'output,
non il calcolo.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio commerciale deve creare un piccolo
preventivo per un cliente.

Crea `preventivo.cpp` rispettando tutti i requisiti:

1. Dichiara `int quantita` e `double prezzoUnitario` prima delle letture.
2. Chiedi e leggi quantità e prezzo con `std::cin`.
3. Mantieni lo stesso ordine tra messaggi, input e variabili.
4. Calcola `totale = quantita * prezzoUnitario`.
5. Stampa quantità, prezzo unitario e totale.
6. Usa un commento `///` per spiegare perché il prezzo è `double`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    /// TODO: spiega perché il prezzo deve conservare i centesimi.
    // TODO: dichiara quantità e prezzo, leggili e calcola il totale.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- [ ] `std::cout <<` porta dati dal programma allo schermo.
- [ ] `std::cin >>` porta dati dalla tastiera a una variabile.
- [ ] Dichiaro una variabile prima di usarla per la lettura.
- [ ] L'ordine di prompt e letture corrisponde all'ordine degli input.
- [ ] Uso `int` per quantità intere e `double` per prezzi con centesimi.
- [ ] Calcolo il totale solo dopo aver letto i dati necessari.

---

### ➡️ Prossimo passo nel percorso

Ora il programma sa chiedere dati. Nel prossimo capitolo del percorso
Fondamenti, `09_espressioni_e_operatore_ternario`, trasformi i valori letti in
risultati intermedi con espressioni aritmetiche e operatori. La selezione con
`if` e `else` viene affrontata nel capitolo successivo.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra dialogo e input/output
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli già introdotti
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/06_chiedere_informazioni.md
#-->
