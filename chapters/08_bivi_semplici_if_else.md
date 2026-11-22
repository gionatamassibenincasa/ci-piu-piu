---
activity_id: if-else-01
title: 'Bivi e decisioni: scegliere con if e if-else'
methodology: PRIMM
assignment_profile: full
order: 8
version: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      double saldoDisponibile = 45.00;
      double importoSpesa = 62.50;

      if (saldoDisponibile >= importoSpesa) {
          std::cout << "Approvato\n";
      } else {
          std::cout << "Negato\n";
      }
    items:
      - question: 'Quale ramo viene eseguito con saldo `45.00` e spesa `62.50`?'
        options:
          - text: 'Il ramo `else`, perché il saldo non è sufficiente'
            correct: true
          - text: 'Il ramo `if`, perché ogni pagamento viene approvato'
            correct: false
          - text: 'Entrambi i rami, uno dopo l''altro'
            correct: false
      - question: 'Perché `saldoDisponibile >= importoSpesa` è una condizione utile per il POS?'
        options:
          - text: 'Confronta i due importi e produce vero solo quando il saldo basta'
            correct: true
          - text: 'Somma automaticamente il saldo e la spesa'
            correct: false
          - text: 'Trasforma i due importi in messaggi di testo'
            correct: false
      - question: 'Che cosa succede se saldo e importo valgono entrambi `45.00`?'
        options:
          - text: 'La condizione è vera perché `>=` include anche l''uguaglianza'
            correct: true
          - text: 'La condizione è falsa perché due valori uguali non possono essere confrontati'
            correct: false
          - text: 'Il programma esegue sempre il ramo `else` in caso di parità'
            correct: false
      - question: 'Perché le graffe sono importanti nell''esempio?'
        options:
          - text: 'Raggruppano tutte le istruzioni che appartengono a ciascun ramo'
            correct: true
          - text: 'Servono solo a rendere il codice più colorato nell''editor'
            correct: false
          - text: 'Sostituiscono la condizione tra parentesi'
            correct: false
      - question: 'Quale risultato produce un `if` semplice quando la condizione è falsa?'
        options:
          - text: 'Salta il suo blocco e continua con l''istruzione successiva'
            correct: true
          - text: 'Esegue automaticamente il blocco `else`, anche se non esiste'
            correct: false
          - text: 'Ripete la condizione finché diventa vera'
            correct: false
  investigate_quiz:
    code: |
      double saldoDisponibile = 45.00;
      double importoSpesa = 62.50;

      if (saldoDisponibile >= importoSpesa) {
          saldoDisponibile = saldoDisponibile - importoSpesa;
          std::cout << "Approvato\n";
      } else {
          std::cout << "Negato\n";
          std::cout << "Mancano " << importoSpesa - saldoDisponibile << " euro\n";
      }
    items:
      - question: 'Qual è il primo passaggio eseguito quando il programma arriva all''if?'
        options:
          - text: 'Confronta `saldoDisponibile` con `importoSpesa`'
            correct: true
          - text: 'Sottrae sempre la spesa dal saldo'
            correct: false
          - text: 'Esegue prima tutte le istruzioni dentro le graffe'
            correct: false
      - question: 'Perché il saldo non viene sottratto nel caso `45.00` contro `62.50`?'
        options:
          - text: 'La sottrazione si trova nel ramo `if`, che non viene eseguito quando la condizione è falsa'
            correct: true
          - text: 'I numeri decimali non possono essere sottratti in C++'
            correct: false
          - text: 'Il ramo `else` annulla sempre tutte le variabili del programma'
            correct: false
      - question: 'Quale valore viene calcolato dall''espressione `importoSpesa - saldoDisponibile`?'
        options:
          - text: '`17.50`, cioè l''importo ancora mancante'
            correct: true
          - text: '`107.50`, perché i due importi vengono sommati'
            correct: false
          - text: '`-17.50`, perché il saldo viene sempre scritto per primo'
            correct: false
      - question: 'Perché, dopo il blocco `if-else`, il programma può eseguire altre istruzioni?'
        options:
          - text: 'Il bivio sceglie un ramo, poi il flusso continua dopo le graffe'
            correct: true
          - text: 'Il programma esce da `main` ogni volta che incontra `else`'
            correct: false
          - text: 'Le graffe trasformano il bivio in un ciclo'
            correct: false
      - question: 'Che cosa accade con questo codice? `if (saldoDisponibile >= importoSpesa); { std::cout << "Approvato"; }`'
        options:
          - text: 'Il punto e virgola chiude subito l''if, quindi il blocco successivo non è più controllato'
            correct: true
          - text: 'Il punto e virgola rende la condizione più precisa'
            correct: false
          - text: 'Il compilatore interpreta il punto e virgola come un ramo `else`'
            correct: false
  modify_quiz:
    code: |
      double saldoDisponibile = 45.00;
      double importoSpesa = 62.50;

      if (saldoDisponibile >= importoSpesa) {
          std::cout << "Approvato\n";
      } else {
          std::cout << "Negato\n";
      }
    items:
      - question: 'Quale modifica fa approvare la spesa di `62.50` con saldo `100.00`?'
        options:
          - text: 'Cambiare `saldoDisponibile` in `100.00`'
            correct: true
          - text: 'Cambiare `>=` in `<=`'
            correct: false
          - text: 'Spostare il messaggio "Negato" dentro il ramo `if`'
            correct: false
      - question: 'Quale modifica permette di mostrare anche il nuovo saldo dopo un pagamento approvato?'
        options:
          - text: 'Aggiungere una stampa nel ramo `if` dopo la sottrazione'
            correct: true
          - text: 'Aggiungere la stampa nel ramo `else` prima del confronto'
            correct: false
          - text: 'Sostituire `std::cout` con `std::cin`'
            correct: false
      - question: 'Che effetto ha cambiare `>=` in `>` quando saldo e spesa sono uguali?'
        options:
          - text: 'Il pagamento diventa negato, perché l''uguaglianza non soddisfa più la condizione'
            correct: true
          - text: 'Il pagamento resta approvato perché i due operatori sono equivalenti'
            correct: false
          - text: 'Il programma esegue entrambi i rami'
            correct: false
      - question: 'Quale modifica aggiunge un avviso per una scorta sotto cinque pezzi senza creare un secondo ramo obbligatorio?'
        options:
          - text: 'Aggiungere un secondo `if` semplice con condizione `scorte < 5`'
            correct: true
          - text: 'Aggiungere sempre `else` al primo `if` del pagamento'
            correct: false
          - text: 'Mettere la quantità dentro una stringa stampata'
            correct: false
      - question: 'Perché conviene modificare una sola condizione alla volta?'
        options:
          - text: 'Per capire quale cambiamento ha prodotto il nuovo ramo eseguito'
            correct: true
          - text: 'Perché un programma C++ può contenere una sola condizione'
            correct: false
          - text: 'Perché `if` funziona soltanto prima della prima modifica'
            correct: false
  make_instructions: >
    Crea `controllo_caveau.cpp`: chiedi un codice PIN già memorizzato e verifica
    con un if-else se il codice coincide con la costante; stampa accesso consentito
    oppure accesso negato. Usa graffe, una sola condizione e nessun else-if.
  visualization:
    kind: pythontutor
    note: 'Seguire il valore della condizione e il solo ramo eseguito.'
registro:
  argomenti: 'Selezione in C++ con `if`, `if-else`, condizioni relazionali, graffe e flusso a due rami; laboratorio PRIMM su autorizzazione di un pagamento POS.'
  note: 'Verifica formativa su condizioni, ramo eseguito e modifica controllata di un bivio.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Prevedere il ramo scelto da una condizione e il significato di `>=` e delle graffe.'
  investigate:
    points: 2
    questions:
      - 'Qual è il primo passaggio eseguito quando il programma incontra `if`?'
      - 'Perché il saldo non viene sottratto quando il ramo è `else`?'
      - 'Che cosa accade con il punto e virgola dopo la condizione?'
    typical_errors:
      - 'Pensare che entrambi i rami vengano eseguiti'
      - 'Confondere `>=` con `>`'
    context: 'Seguire il flusso e riconoscere il punto e virgola come errore logico.'
  modify:
    points: 1
    prompt: 'Modifica il programma affinché mostri il nuovo saldo soltanto quando il pagamento è approvato.'
    code: |
      double saldoDisponibile = 45.00;
      double importoSpesa = 30.00;

      if (saldoDisponibile >= importoSpesa) {
          saldoDisponibile = saldoDisponibile - importoSpesa;
          std::cout << "Approvato\n";
      } else {
          std::cout << "Negato\n";
      }
    typical_errors:
      - 'Stampa il nuovo saldo anche nel ramo negato'
      - 'Dimentica di sottrarre l''importo prima della stampa'
    context: 'Collegare la modifica al ramo corretto e all''ordine delle istruzioni.'
  make:
    points: 1
    prompt: 'Crea un controllo PIN per un caveau: se il PIN coincide con la costante stampa accesso consentito, altrimenti stampa accesso negato.'
    must_include:
      - 'if'
      - 'else'
      - 'const'
      - 'std::cout'
    typical_errors:
      - 'Usa `=` invece di `==` nel confronto'
      - 'Dimentica le graffe di uno dei due rami'
    context: 'Trasferire il bivio a un controllo di sicurezza aziendale.'
  variants:
    B:
      modify:
        prompt: 'Modifica il pagamento portando il saldo a `30.00` e l''importo a `30.00`; indica quale ramo viene eseguito e perché.'
        code: |
          double saldoDisponibile = 45.00;
          double importoSpesa = 62.50;

          if (saldoDisponibile >= importoSpesa) {
              std::cout << "Approvato\n";
          } else {
              std::cout << "Negato\n";
          }
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # If e if-else

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Usa sempre le graffe e ricompila dopo ogni modifica.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Bivio POS

      Rispondi prima di eseguire il programma.

      1. Quale ramo viene eseguito?
      >

      2. Perché la condizione è vera o falsa?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Terminale POS

      1. Quale messaggio compare a video?
      >

      2. Quale ramo ti aspettavi?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Bivio POS

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Qual è il primo passaggio eseguito quando il programma incontra `if`?
      >

      2. Perché il saldo non viene sottratto quando il ramo è `else`?
      >

      3. Che cosa accade con il punto e virgola dopo la condizione?
      >
  - path: student_work/modify/autorizzazione_pos.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          double saldoDisponibile = 45.00;
          double importoSpesa = 62.50;
          if (saldoDisponibile >= importoSpesa) {
              std::cout << "Approvato\n";
          } else {
              std::cout << "Negato\n";
          }
          return 0;
      }
    validation_rules:
      min_lines: 11
      must_contain:
        - if
        - else
  - path: student_work/make/caveau.cpp
    action: create
    phase: make
    description: Controllo di accesso aziendale con PIN e bivio if-else.
    template_content: |
      /**
       * @brief Controllo accessi a un caveau aziendale.
       */
      #include <iostream>

      int main() {
          const int PIN_SEGRETO = 4821;
          /// TODO: spiega perché il codice deve essere confrontato prima dell'accesso.
          // TODO: dichiara il PIN inserito e scrivi l'if-else
          return 0;
      }
    validation_rules:
      min_lines: 10
      must_contain:
        - if
        - else
        - const
---

## 🚦 Bivi e decisioni: scegliere con `if` e `if-else`

Un gestionale non esegue sempre la stessa azione. Un pagamento può essere
approvato o rifiutato; una scorta può essere sufficiente o sotto il minimo; un
badge può essere valido oppure no.

Con `if` e `if-else` insegni al programma a scegliere un percorso.

> 💡 **Metafora:** Immagina un tornello aziendale. La condizione è il lettore
> che controlla il badge; il blocco `if` è il passaggio verde quando la regola
> è vera; il blocco `else` è il passaggio rosso quando la regola è falsa. Con
> `if-else` passa un solo percorso, mai entrambi.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un `if` o un `if-else` con graffe per scegliere il ramo corretto in base a una condizione.

---

### ⚙️ Prima del laboratorio: i due modelli

Un `if` semplice esegue un blocco soltanto quando la condizione è vera:

```cpp
if (giacenza < 5) {
    std::cout << "Scorte in esaurimento\n";
}
```

Un `if-else` sceglie uno dei due blocchi:

```cpp
if (saldo >= importo) {
    std::cout << "Pagamento approvato\n";
} else {
    std::cout << "Fondi insufficienti\n";
}
```

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| Condizione | Un confronto che vale vero o falso | Decide il percorso |
| `if` | Ramo per il caso vero | Esegue l'azione consentita |
| `else` | Ramo per il caso falso | Gestisce l'alternativa |
| `{ }` | Confini del blocco | Tiene insieme tutte le istruzioni del ramo |

---

### 🧭 Prima del laboratorio: seguire il flusso

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi saldo e importo;
if (saldo >= importo?) then (vero)
  :Sottrai l'importo;
  :Mostra "Approvato";
else (falso)
  :Mostra "Negato";
endif
:Continua dopo il bivio;
stop
@enduml
```

Operatori utili per confrontare valori già noti:

| Operatore | Significato | Esempio |
| :---: | :--- | :--- |
| `>` | maggiore di | `scorte > 0` |
| `<` | minore di | `scorte < 5` |
| `==` | uguale a | `pinInserito == PIN_SEGRETO` |
| `>=` | maggiore o uguale | `saldo >= importo` |

Non confondere `==`, che confronta, con `=`, che assegna un valore.

---

### 🔬 Laboratorio PRIMM: autorizzazione di un pagamento POS

Il terminale deve decidere se il saldo disponibile basta per una spesa.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma completo e confronta l'output con la tua previsione.

```cpp
/**
 * @file autorizzazione_pos.cpp
 * @brief Verifica se un pagamento può essere autorizzato.
 */
#include <iostream>

/**
 * @brief Controlla il saldo e comunica l'esito della transazione.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il saldo rappresenta il credito realmente disponibile sul conto.
    double saldoDisponibile = 45.00;
    /// L'importo è decimale perché un pagamento può avere centesimi.
    double importoSpesa = 62.50;

    std::cout << "=== TERMINALE PAGAMENTI POS ===\n";
    std::cout << "Importo richiesto: " << importoSpesa << " EUR\n";

    if (saldoDisponibile >= importoSpesa) {
        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << "TRANSAZIONE APPROVATA\n";
        std::cout << "Nuovo saldo: " << saldoDisponibile << " EUR\n";
    } else {
        std::cout << "TRANSAZIONE NEGATA\n";
        std::cout << "Credito insufficiente\n";
    }

    std::cout << "Operazione conclusa.\n";
    return 0;
}
```
@LIA.cpp

Con i valori iniziali la condizione è falsa, quindi compare
`TRANSAZIONE NEGATA`.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine delle istruzioni e spiega perché il saldo
non cambia nel caso negato.

[[ investigate_block() ]]

| Passo | Cosa osservi | Stato |
| :---: | :--- | :--- |
| 1 | Il programma confronta `45.00 >= 62.50` | `false` |
| 2 | Salta il blocco `if` | Nessuna sottrazione |
| 3 | Entra nel blocco `else` | Stampa transazione negata |
| 4 | Esce dal bivio | Stampa operazione conclusa |

La sottrazione è dentro il ramo `if`: viene eseguita soltanto quando il
confronto è vero. Le istruzioni dopo le graffe appartengono invece al flusso
comune e vengono eseguite dopo il ramo scelto.

Evita questo errore logico:

```cpp
if (saldoDisponibile >= importoSpesa);
{
    std::cout << "Approvato\n";
}
```

Il punto e virgola chiude subito l'`if`; il blocco successivo non è più
controllato dalla condizione. Il programma può compilare, ma il comportamento
non è quello desiderato.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva quale ramo
> viene attraversato.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double saldoDisponibile = 45.00;
    double importoSpesa = 62.50;

    if (saldoDisponibile >= importoSpesa) {
        std::cout << "Approvato\n";
    } else {
        std::cout << "Negato\n";
    }

    return 0;
}
```

</details>

**Modifica A — pagamento approvato**

Cambia `saldoDisponibile` in `100.00`. Ricompila e verifica che venga eseguito
il ramo `if`.

**Modifica B — mostra il nuovo saldo**

Nel ramo `if`, sottrai l'importo e stampa `saldoDisponibile` dopo la
sottrazione. Non aggiungere la stampa nel ramo `else`.

**Modifica C — prova il caso di uguaglianza**

Imposta entrambi i valori a `45.00`. Prevedi il risultato: `>=` include anche
il caso in cui saldo e importo siano uguali.

#### 5. MAKE (Crea)

**Scenario aziendale:** il responsabile sicurezza deve controllare l'accesso
a un caveau aziendale.

Crea `controllo_caveau.cpp` rispettando tutti i requisiti:

1. Dichiara `const int PIN_SEGRETO = 4821`.
2. Dichiara `int pinInserito = 4821`.
3. Confronta i due valori con `==`.
4. Usa un solo `if-else` con graffe.
5. Se il PIN è corretto, stampa `ACCESSO CONSENTITO`.
6. Altrimenti, stampa `ACCESSO NEGATO`.
7. Inserisci un commento `///` che spieghi perché il PIN deve essere confrontato prima dell'accesso.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Controllo accessi a un caveau aziendale.
 */
#include <iostream>

int main() {
    const int PIN_SEGRETO = 4821;
    /// TODO: spiega perché il codice deve essere confrontato prima dell'accesso.
    // TODO: dichiara pinInserito e scrivi l'if-else.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `if` esegue un blocco solo quando la condizione è vera.
- `if-else` sceglie un solo ramo tra vero e falso.
- Usa sempre le graffe per rendere chiaro il blocco controllato.
- `==` confronta; `=` assegna.
- Non mettere `;` subito dopo la condizione.
- Dopo il ramo scelto, il flusso continua con le istruzioni successive.

---

### ➡️ Prossimo chunk

Quando le alternative diventano più di due, un solo bivio non basta. Nel
prossimo chunk userai catene `if / else if / else` per gestire fasce di
sconto e stati diversi di un ordine.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra tornello e if/else
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli già introdotti
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/07_bivi_semplici_if_else.md
#-->
