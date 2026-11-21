---
activity_id: switch-01
title: 'Lo smistatore di sportello: scegliere con switch e case'
methodology: PRIMM
order: 10
version: '2026-11-20'
last_update: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      int sceltaMenu = 2;

      switch (sceltaMenu) {
          case 1:
              std::cout << "Prelievo\n";
              break;
          case 2:
              std::cout << "Versamento\n";
              break;
          default:
              std::cout << "Opzione non valida\n";
              break;
      }
    items:
      - question: 'Quale `case` viene selezionato con `sceltaMenu = 2`?'
        options:
          - text: '`case 2`, perché il valore coincide con la sua costante'
            correct: true
          - text: '`case 1`, perché è il primo caso scritto'
            correct: false
          - text: '`default`, perché ogni scelta deve passare dall''alternativa finale'
            correct: false
      - question: 'Perché `break` è importante dopo il messaggio del `case 2`?'
        options:
          - text: 'Ferma lo switch e impedisce di eseguire i case successivi'
            correct: true
          - text: 'Rende uguale il valore di tutti i case'
            correct: false
          - text: 'Fa ripartire lo switch dal primo case'
            correct: false
      - question: 'Che cosa stampa il frammento se `sceltaMenu = 7`?'
        options:
          - text: 'Il messaggio del ramo `default`'
            correct: true
          - text: 'Il messaggio del `case 1`, perché 7 è maggiore di 1'
            correct: false
          - text: 'Tutti i messaggi dei case in ordine'
            correct: false
      - question: 'Per quale tipo di dato è adatto questo `switch`?'
        options:
          - text: 'Un codice discreto come un `int` o un `char`'
            correct: true
          - text: 'Un intervallo continuo come un prezzo `double`'
            correct: false
          - text: 'Una frase completa contenuta in `std::string`'
            correct: false
      - question: 'Che cosa può accadere se togli il `break` da `case 2`?'
        options:
          - text: 'L''esecuzione può continuare nel `case` successivo: è il fall-through'
            correct: true
          - text: 'Il programma torna automaticamente a `case 1`'
            correct: false
          - text: 'Il compilatore cancella il messaggio del `case 2`'
            correct: false
  investigate_quiz:
    code: |
      int sceltaMenu = 2;

      switch (sceltaMenu) {
          case 1:
              std::cout << "Prelievo\n";
              break;
          case 2:
              std::cout << "Versamento\n";
              break;
          case 3:
              std::cout << "Saldo\n";
              break;
          default:
              std::cout << "Opzione non valida\n";
              break;
      }
    items:
      - question: 'Qual è il primo passaggio eseguito quando il programma arriva allo `switch`?'
        options:
          - text: 'Confronta il valore di `sceltaMenu` con i valori dei `case`'
            correct: true
          - text: 'Esegue sempre il primo blocco e poi cerca il valore'
            correct: false
          - text: 'Esegue prima `default` come controllo di sicurezza'
            correct: false
      - question: 'Perché con `sceltaMenu = 2` non viene eseguito `case 3`?'
        options:
          - text: 'Il `break` di `case 2` fa uscire dallo switch'
            correct: true
          - text: 'I case successivi vengono ignorati perché hanno sempre numeri maggiori'
            correct: false
          - text: 'Il programma esegue solo i case che contengono numeri pari'
            correct: false
      - question: 'Che cosa succede senza `break` alla fine di `case 2`?'
        options:
          - text: 'Dopo il messaggio di `case 2`, l''esecuzione continua nel case successivo'
            correct: true
          - text: 'Il programma si ferma sempre con un errore di compilazione'
            correct: false
          - text: 'Viene eseguito soltanto `default`'
            correct: false
      - question: 'Perché `default` non viene eseguito con `sceltaMenu = 2`?'
        options:
          - text: 'Esiste già un case corrispondente e il suo `break` chiude lo switch'
            correct: true
          - text: '`default` funziona soltanto con valori negativi'
            correct: false
          - text: 'Il compilatore elimina sempre `default` quando ci sono tre case'
            correct: false
      - question: 'Perché `double sceltaMenu = 2.0;` non è adatto come espressione dello switch?'
        options:
          - text: 'Lo switch richiede un valore intero o carattere, non un numero decimale'
            correct: true
          - text: 'Un double può essere usato solo per stampare prezzi'
            correct: false
          - text: 'I numeri con decimali non possono essere assegnati a variabili'
            correct: false
  modify_quiz:
    code: |
      int sceltaMenu = 2;

      switch (sceltaMenu) {
          case 1:
              std::cout << "Prelievo\n";
              break;
          case 2:
              std::cout << "Versamento\n";
              break;
          default:
              std::cout << "Opzione non valida\n";
              break;
      }
    items:
      - question: 'Quale modifica aggiunge una voce per la visualizzazione del saldo?'
        options:
          - text: 'Aggiungere `case 3`, stampare il messaggio e chiudere con `break`'
            correct: true
          - text: 'Aggiungere `default 3:` dopo il case 2'
            correct: false
          - text: 'Cambiare `switch` in `std::cout`'
            correct: false
      - question: 'Quale modifica fa eseguire lo stesso messaggio sia con codice `0` sia con codice `9`?'
        options:
          - text: 'Scrivere `case 0:` seguito da `case 9:` prima delle stesse istruzioni'
            correct: true
          - text: 'Scrivere `case 0 || 9:` come se fosse una condizione booleana'
            correct: false
          - text: 'Duplicare `default` due volte'
            correct: false
      - question: 'Che effetto ha aggiungere `break` dopo `default`?'
        options:
          - text: 'Rende esplicita l''uscita dallo switch anche quando nessun case coincide'
            correct: true
          - text: 'Fa eseguire di nuovo il case precedente'
            correct: false
          - text: 'Trasforma `default` in un ciclo'
            correct: false
      - question: 'Quale modifica mantiene il prezzo di una ricarica con i centesimi?'
        options:
          - text: 'Usare una variabile `double` per l''importo dentro il case, senza usarla come scelta'
            correct: true
          - text: 'Usare un `double` come espressione dello switch'
            correct: false
          - text: 'Memorizzare l''importo nel nome del `case`'
            correct: false
      - question: 'Perché conviene modificare un case alla volta?'
        options:
          - text: 'Per distinguere quale case o break ha cambiato il percorso del menu'
            correct: true
          - text: 'Perché uno switch può contenere un solo case in assoluto'
            correct: false
          - text: 'Perché `break` funziona solo nel primo case scritto'
            correct: false
  make_instructions: >
    Crea `cambio_valute.cpp` per un POS: usa un `char` per il codice valuta,
    uno switch con casi per USD, GBP, JPY e CHF, fall-through intenzionale per
    maiuscole/minuscole, default per codici non supportati e un calcolo del
    controvalore in euro.
  visualization:
    kind: plantuml
    note: 'Seguire il salto al case corrispondente e l''uscita prodotta da break.'
registro:
  argomenti: 'Selezione multipla con `switch`, `case`, `break` e `default`; fall-through intenzionale; uso di codici discreti nei menu ATM e nei cambi valuta.'
  note: 'Laboratorio PRIMM su un menu ATM e un convertitore di valute per POS.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Riconoscere il case selezionato, il ruolo di break e la funzione di default.'
  investigate:
    points: 2
    questions:
      - 'Perché `case 2` viene selezionato quando la scelta vale 2?'
      - 'Che cosa succede se manca break?'
      - 'Perché un double non può essere usato come scelta dello switch?'
    typical_errors:
      - 'Confondere switch con una catena di intervalli'
      - 'Pensare che default venga sempre eseguito'
    context: 'Seguire il flusso di selezione e distinguere fall-through da errore di tipo.'
  modify:
    points: 1
    prompt: 'Aggiungi `case 3` per visualizzare il saldo e termina il ramo con `break`.'
    code: |
      int sceltaMenu = 2;

      switch (sceltaMenu) {
          case 1:
              std::cout << "Prelievo\n";
              break;
          case 2:
              std::cout << "Versamento\n";
              break;
          default:
              std::cout << "Opzione non valida\n";
              break;
      }
    typical_errors:
      - 'Dimenticare il break'
      - 'Scrivere default 3 invece di case 3'
    context: 'Aggiungere una scelta discreta senza alterare i rami esistenti.'
  make:
    points: 1
    prompt: 'Crea un convertitore di valute con codici char, quattro case, fall-through per maiuscole/minuscole e default.'
    must_include:
      - 'switch'
      - 'case'
      - 'break'
      - 'default'
    typical_errors:
      - 'Usare un double come scelta dello switch'
      - 'Dimenticare il default per un codice sconosciuto'
    context: 'Trasferire lo schema del menu a un processo POS aziendale.'
  variants:
    B:
      modify:
        prompt: 'Aggiungi `case 4` per una ricarica telefonica e stampa il messaggio prima del break.'
        code: |
          int sceltaMenu = 2;

          switch (sceltaMenu) {
              case 1:
                  std::cout << "Prelievo\n";
                  break;
              case 2:
                  std::cout << "Versamento\n";
                  break;
              default:
                  std::cout << "Opzione non valida\n";
                  break;
          }
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Switch-case

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Ogni `case` utile termina con `break`, salvo fall-through intenzionale.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Menu ATM

      Rispondi prima di eseguire il programma.

      1. Quale case viene selezionato?
      >

      2. Che cosa impedisce di eseguire il case successivo?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Menu ATM

      1. Quale messaggio compare a video?
      >

      2. Quale valore ha la scelta?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Switch

      1. Che cosa succede dopo un `break`?
      >

      2. Quando viene eseguito `default`?
      >
  - path: student_work/modify/menu_atm.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          int sceltaMenu = 2;
          switch (sceltaMenu) {
              case 1:
                  std::cout << "Prelievo\n";
                  break;
              case 2:
                  std::cout << "Versamento\n";
                  break;
              default:
                  std::cout << "Opzione non valida\n";
                  break;
          }
          return 0;
      }
    validation_rules:
      min_lines: 14
      must_contain:
        - switch
        - case
        - break
  - path: student_work/make/cambio_valute.cpp
    action: create
    phase: make
    description: Convertitore di valute per un POS con switch e codici char.
    template_content: |
      /**
       * @brief Conversione di una valuta estera in euro.
       */
      #include <iostream>

      int main() {
          /// TODO: spiega perché il tasso dipende dalla valuta selezionata.
          // TODO: dichiara importo e codice, poi scrivi lo switch.
          return 0;
      }
    validation_rules:
      min_lines: 10
      must_contain:
        - switch
        - case
        - default
---

## 🎛️ Lo smistatore di sportello: scegliere con `switch`

Nel capitolo precedente hai usato `if / else if` per classificare intervalli e
soglie. Quando invece la scelta è un codice preciso, come il tasto `1` di un
menu o il carattere `'U'` di una valuta, una lunga catena può diventare
verbosa.

In questi casi puoi usare `switch`: confronta un valore discreto con diversi
`case`.

> 💡 **Metafora:** Immagina un distributore ATM. Il tasto premuto è il codice
> della scelta; ogni `case` è lo sportello dell'operazione corrispondente;
> `break` è il freno che chiude lo sportello dopo l'erogazione; `default` è il
> messaggio “codice non valido” quando nessuno sportello corrisponde.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere uno `switch` su un codice discreto usando `case`, `break` e `default`.

---

### ⚙️ Prima del laboratorio: anatomia dello switch

```cpp
switch (scelta) {
    case 1:
        std::cout << "Prelievo\n";
        break;
    case 2:
        std::cout << "Versamento\n";
        break;
    default:
        std::cout << "Opzione non valida\n";
        break;
}
```

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| `switch` | Legge un codice discreto | Organizza le alternative |
| `case` | Rappresenta un valore preciso | Collega codice e operazione |
| `break` | Esce dallo switch | Evita il fall-through involontario |
| `default` | Gestisce gli altri valori | Copre il codice non previsto |

Regole operative:

1. La scelta dello `switch` deve essere un tipo intero o carattere, come `int` o
   `char`.
2. Ogni `case` confronta un valore preciso, non un intervallo.
3. Dopo un `case` utile inserisci `break`, salvo un fall-through voluto.
4. Usa `if / else if` per soglie, intervalli, `double` o `std::string`.

---

### 🧭 Prima del laboratorio: il percorso della scelta

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi il codice della scelta;
switch (scelta)
case (1)
  :Prelievo;
  :break;
case (2)
  :Versamento;
  :break;
case (3)
  :Saldo;
  :break;
case (default)
  :Opzione non valida;
  :break;
endswitch
:Continua dopo lo switch;
stop
@enduml
```

Uno `switch` cerca il `case` corrispondente. Se lo trova, esegue quel blocco;
con `break` esce subito. Se non trova corrispondenze, entra in `default`.

---

### 🔬 Laboratorio PRIMM: menu ATM

Un menu ATM deve smistare quattro codici: prelievo, versamento, visualizzazione
del saldo e uscita.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma completo e osserva quale operazione viene selezionata.

```cpp
/**
 * @file menu_atm.cpp
 * @brief Smista una scelta tra le operazioni di uno sportello ATM.
 */
#include <iostream>

/**
 * @brief Esegue un'operazione in base a un codice intero.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il codice simula il tasto premuto dal cliente.
    int sceltaMenu = 2;

    std::cout << "=== SPORTELLO ATM ===\n";
    std::cout << "1. Prelievo\n";
    std::cout << "2. Versamento\n";
    std::cout << "3. Visualizza saldo\n";
    std::cout << "0. Esci\n";
    std::cout << "Scelta registrata: " << sceltaMenu << "\n";

    switch (sceltaMenu) {
        case 1:
            std::cout << "Prelievo selezionato.\n";
            break;
        case 2:
            std::cout << "Versamento selezionato.\n";
            break;
        case 3:
            std::cout << "Visualizzazione saldo selezionata.\n";
            break;
        case 0:
            std::cout << "Arrivederci.\n";
            break;
        default:
            std::cout << "Opzione non valida.\n";
            break;
    }

    return 0;
}
```
@LIA.cpp

Con `sceltaMenu = 2` compare `Versamento selezionato.`. Il `break` impedisce
di eseguire anche il `case 3`.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci il percorso seguito dal valore `2`.

[[ investigate_block() ]]

| Passo | Cosa accade | Risultato |
| :---: | :--- | :--- |
| 1 | `switch` legge `sceltaMenu` | Valore `2` |
| 2 | Confronta con `case 1` | Nessuna corrispondenza |
| 3 | Confronta con `case 2` | Corrispondenza |
| 4 | Esegue il messaggio | Versamento |
| 5 | Incontra `break` | Esce dallo switch |

Prova a cambiare `sceltaMenu` in `7`: nessun `case` coincide e viene eseguito
`default`.

Ora rimuovi temporaneamente il `break` dal `case 2`. Vedrai il fall-through:
dopo Versamento viene eseguito anche il codice del `case 3`, finché non viene
incontrato un `break`.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva il salto al
> `case` corrispondente.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
switch (sceltaMenu) {
    case 1:
        std::cout << "Prelievo\n";
        break;
    default:
        std::cout << "Opzione non valida\n";
        break;
}
```

</details>

**Modifica A — aggiungi il saldo**

Aggiungi `case 3`, stampa `Saldo selezionato.` e chiudi con `break`.

**Modifica B — due codici per uscire**

Fai eseguire lo stesso messaggio ai codici `0` e `9` con fall-through
intenzionale:

```cpp
case 0:
case 9:
    std::cout << "Arrivederci.\n";
    break;
```

**Modifica C — prova il tipo sbagliato**

Sostituisci temporaneamente la scelta con:

```cpp
double sceltaMenu = 2.0;
```

Ricompila e osserva l'errore: lo `switch` non accetta un numero decimale come
valore di selezione.

#### 5. MAKE (Crea)

**Scenario aziendale:** un POS deve convertire un importo estero in euro in
base al codice della valuta selezionata.

Crea `cambio_valute.cpp` rispettando tutti i requisiti:

1. Dichiara `double importoValutaEstera = 120.00`.
2. Dichiara `char codiceValuta = 'U'`.
3. Usa uno `switch` sul codice della valuta.
4. Gestisci `U/u` con tasso `0.92`, `G/g` con `1.18`, `J/j` con `0.0061`
   e `S/s` con `1.05`.
5. Usa il fall-through intenzionale per maiuscole e minuscole.
6. Usa `default` per stampare `Valuta non supportata`.
7. Per i codici validi, calcola e stampa il controvalore in euro.
8. Inserisci commenti `///` per spiegare perché i tassi sono associati ai case.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Conversione di una valuta estera in euro al POS.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché il tasso dipende dalla valuta selezionata.
    // TODO: dichiara importo e codice, poi scrivi lo switch.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `switch` seleziona valori discreti, come `int` e `char`.
- `case` rappresenta un valore preciso, non un intervallo.
- `break` chiude il ramo e previene il fall-through involontario.
- `default` gestisce i codici non previsti.
- Il fall-through può essere intenzionale, per esempio per `U` e `u`.
- Per soglie, intervalli, `double` e `std::string` usa `if / else if`.

---

### ➡️ Prossimo chunk

Finora il programma ha seguito un percorso oppure ha scelto un caso. Nel
prossimo capitolo imparerai a ripetere un'azione con il ciclo `while`.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra ATM e switch
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli già introdotti
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/09_selezione_multipla_switch.md
#-->
