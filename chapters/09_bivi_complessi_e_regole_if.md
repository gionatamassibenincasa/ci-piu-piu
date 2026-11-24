---
activity_id: bivi-complessi-01
title: 'Scaglioni ordinati: if, else if ed else'
methodology: PRIMM
assignment_profile: full
order: 9
version: '2026-11-20'
last_update: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      double fatturato = 25000.0;

      if (fatturato >= 50000.0) {
          std::cout << "Platinum\n";
      } else if (fatturato >= 20000.0) {
          std::cout << "Gold\n";
      } else if (fatturato >= 5000.0) {
          std::cout << "Silver\n";
      } else {
          std::cout << "Nessuna fascia\n";
      }
    items:
      - question: 'Quale fascia viene scelta con `fatturato = 25000.0`?'
        options:
          - text: 'Gold, perché il fatturato non raggiunge 50000 ma supera 20000'
            correct: true
          - text: 'Platinum, perché ogni valore positivo entra nella fascia più alta'
            correct: false
          - text: 'Silver, perché il programma sceglie sempre l''ultima condizione vera'
            correct: false
      - question: 'Perché la soglia `50000.0` deve essere controllata prima di `20000.0`?'
        options:
          - text: 'Un fatturato di 60000 deve fermarsi nella fascia Platinum prima di raggiungere Gold'
            correct: true
          - text: 'Le soglie più piccole non possono essere scritte dopo quelle grandi'
            correct: false
          - text: 'Il compilatore esegue sempre le condizioni dall''alto verso il basso numerico'
            correct: false
      - question: 'Che cosa succede dopo che una condizione della catena risulta vera?'
        options:
          - text: 'Viene eseguito quel ramo e le condizioni successive vengono saltate'
            correct: true
          - text: 'Vengono eseguiti anche tutti gli `else if` successivi'
            correct: false
          - text: 'Il programma torna alla prima condizione per controllarla di nuovo'
            correct: false
      - question: 'Quale ruolo ha l''ultimo `else` nella scala?'
        options:
          - text: 'Gestisce il caso in cui nessuna soglia precedente sia stata raggiunta'
            correct: true
          - text: 'Ripete il controllo della soglia più alta'
            correct: false
          - text: 'Rende vere tutte le condizioni precedenti'
            correct: false
      - question: 'Perché le fasce di sconto sono un buon esempio di `else if`?'
        options:
          - text: 'Un cliente deve ricevere una sola fascia tra quelle definite'
            correct: true
          - text: 'Ogni cliente deve ricevere tutti gli sconti contemporaneamente'
            correct: false
          - text: 'Le fasce non hanno bisogno di confronti tra numeri'
            correct: false
  investigate_quiz:
    code: |
      double fatturato = 32500.0;
      double sconto = 0.0;

      if (fatturato >= 50000.0) {
          sconto = 0.15;
      } else if (fatturato >= 20000.0) {
          sconto = 0.10;
      } else if (fatturato >= 5000.0) {
          sconto = 0.05;
      } else {
          sconto = 0.0;
      }
    items:
      - question: 'Qual è il primo confronto eseguito con `fatturato = 32500.0`?'
        options:
          - text: '`32500.0 >= 50000.0`, che risulta falso'
            correct: true
          - text: '`32500.0 >= 5000.0`, perché è la soglia più vicina'
            correct: false
          - text: 'Il programma confronta tutte le soglie nello stesso momento'
            correct: false
      - question: 'Perché il valore finale di `sconto` è `0.10`?'
        options:
          - text: 'La prima condizione è falsa e la seconda è vera, quindi il ramo Gold assegna 0.10'
            correct: true
          - text: 'Tutte le percentuali vengono sommate e il risultato diventa 0.10'
            correct: false
          - text: 'Il valore iniziale 0.0 viene trasformato automaticamente in 0.10'
            correct: false
      - question: 'Quale ordine di verifica è corretto per `fatturato = 32500.0`?'
        options:
          - text: 'Platinum falso → Gold vero → Silver e `else` saltati'
            correct: true
          - text: 'Silver vero → Gold vero → Platinum falso'
            correct: false
          - text: 'Gold vero → Silver vero → `else` eseguito'
            correct: false
      - question: 'Che cosa accade se il fatturato vale `3000.0`?'
        options:
          - text: 'Tutte le soglie sono false e viene eseguito l''ultimo `else`'
            correct: true
          - text: 'Viene scelta Silver perché è la fascia più bassa'
            correct: false
          - text: 'Il programma non esegue nessuna istruzione della catena, compreso `else`'
            correct: false
      - question: 'Perché mettere `fatturato >= 20000.0` prima di `fatturato >= 50000.0` crea un errore logico?'
        options:
          - text: 'Un fatturato di 60000 soddisfa subito 20000 e viene classificato Gold'
            correct: true
          - text: 'Il compilatore rifiuta sempre le soglie scritte in ordine crescente'
            correct: false
          - text: 'La condizione 50000 diventerebbe automaticamente falsa'
            correct: false
  modify_quiz:
    code: |
      if (fatturato >= 50000.0) {
          fascia = "Platinum";
      } else if (fatturato >= 20000.0) {
          fascia = "Gold";
      } else {
          fascia = "Nessuna";
      }
    items:
      - question: 'Quale modifica aggiunge una fascia Diamond per fatturati da `100000.0` in su?'
        options:
          - text: 'Inserire un nuovo `if (fatturato >= 100000.0)` prima del controllo Platinum'
            correct: true
          - text: 'Aggiungere Diamond dopo l''ultimo `else`'
            correct: false
          - text: 'Sostituire `else if` con un secondo `else`'
            correct: false
      - question: 'Che effetto ha mettere il controllo `>= 20000.0` prima di `>= 50000.0`?'
        options:
          - text: 'I valori da 50000 in su vengono intercettati troppo presto e classificati Gold'
            correct: true
          - text: 'Le due fasce vengono assegnate insieme'
            correct: false
          - text: 'Il programma corregge automaticamente l''ordine'
            correct: false
      - question: 'Quale modifica assegna Silver anche al valore esattamente uguale a `5000.0`?'
        options:
          - text: 'Usare `fatturato >= 5000.0` nella condizione Silver'
            correct: true
          - text: 'Usare `fatturato > 5000.0` nella condizione Silver'
            correct: false
          - text: 'Spostare Silver nel ramo `else` senza una condizione'
            correct: false
      - question: 'Quale modifica calcola l''importo dello sconto dopo aver scelto la fascia?'
        options:
          - text: 'Moltiplicare il fatturato per `sconto` dopo la catena'
            correct: true
          - text: 'Moltiplicare ogni soglia prima di sapere quale ramo è vero'
            correct: false
          - text: 'Usare `std::cin` al posto della variabile `sconto`'
            correct: false
      - question: 'Perché conviene modificare una soglia alla volta?'
        options:
          - text: 'Per capire quale cambiamento ha alterato la classificazione ai confini'
            correct: true
          - text: 'Perché una catena può contenere una sola soglia in assoluto'
            correct: false
          - text: 'Perché `else if` funziona soltanto con valori non decimali'
            correct: false
  make_instructions: >
    Crea `imposte_reddito.cpp` per una ditta: leggi un reddito imponibile già
    assegnato al codice, scegli una sola aliquota con una catena ordinata
    `if / else if / else` e stampa reddito, fascia, aliquota e imposta stimata.
    Usa le soglie fiscali indicate nel capitolo.
  visualization:
    kind: plantuml
    note: 'Seguire la catena dall''alto verso il basso e fermarsi al primo ramo vero.'
registro:
  argomenti: 'Catene `if / else if / else`; fasce esclusive; ordine delle soglie; classificazione di fatturato e aliquote fiscali in uno scenario aziendale.'
  note: 'Laboratorio PRIMM su fasce sconto e scaglioni ordinati.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Prevedere la fascia corretta e spiegare perché l''ordine delle soglie è decisivo.'
  investigate:
    points: 2
    questions:
      - 'Qual è il primo confronto per un fatturato di 32500?'
      - 'Perché il ramo Silver viene saltato dopo Gold vero?'
      - 'Che cosa accade se una soglia più bassa viene scritta prima?'
    typical_errors:
      - 'Pensare che tutte le condizioni vere vengano eseguite'
      - 'Ordinare le soglie dalla più bassa alla più alta senza analizzare l''effetto'
    context: 'Seguire il tracing della catena e riconoscere le alternative esclusive.'
  modify:
    points: 1
    prompt: 'Aggiungi una fascia Diamond per fatturato almeno pari a 100000, inserendola prima di Platinum.'
    code: |
      if (fatturato >= 50000.0) {
          fascia = "Platinum";
      } else if (fatturato >= 20000.0) {
          fascia = "Gold";
      } else {
          fascia = "Nessuna";
      }
    typical_errors:
      - 'Inserire Diamond dopo una condizione già vera'
      - 'Usare `else` senza una nuova condizione'
    context: 'Inserire una fascia più restrittiva nel punto corretto della catena.'
  make:
    points: 1
    prompt: 'Crea la classificazione di un reddito imponibile con quattro scaglioni fiscali e stampa aliquota e imposta stimata.'
    must_include:
      - 'else if'
      - 'double'
      - 'std::cout'
    typical_errors:
      - 'Dimenticare il caso oltre l''ultima soglia'
      - 'Usare soglie non ordinate'
    context: 'Trasferire il pattern delle fasce sconto a un prospetto fiscale semplificato.'
  variants:
    B:
      modify:
        prompt: 'Aggiungi una fascia Diamond per fatturato almeno pari a 90000, prima di Platinum, e verifica con 95000.'
        code: |
          if (fatturato >= 50000.0) {
              fascia = "Platinum";
          } else if (fatturato >= 20000.0) {
              fascia = "Gold";
          } else {
              fascia = "Nessuna";
          }
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Scaglioni ordinati

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Nelle fasce, scrivi sempre prima la soglia più alta.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Fasce

      Rispondi prima di eseguire il programma.

      1. Quale fascia ottiene un fatturato di 25000?
      >

      2. Perché le soglie devono essere ordinate?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Fasce sconto

      1. Quale ramo della scala è stato eseguito?
      >

      2. Quale valore ha ricevuto lo sconto?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Ordine delle soglie

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Qual è il primo confronto per un fatturato di 32500?
      >

      2. Perché il ramo Silver viene saltato dopo Gold vero?
      >

      3. Che cosa accade se una soglia più bassa viene scritta prima?
      >
  - path: student_work/modify/fasce_sconto.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          double fatturato = 32500.0;
          if (fatturato >= 50000.0) {
              std::cout << "Platinum\n";
          } else if (fatturato >= 20000.0) {
              std::cout << "Gold\n";
          } else {
              std::cout << "Altra fascia\n";
          }
          return 0;
      }
    validation_rules:
      min_lines: 11
      must_contain:
        - if
        - else if
  - path: student_work/make/scaglioni_imposta.cpp
    action: create
    phase: make
    description: Prospetto di imposta con scaglioni fiscali  ordinati.
    template_content: |
      /**
       * @brief Stima un'imposta con scaglioni fiscali.
       */
      #include <iostream>

      int main() {
          /// TODO: spiega perché la soglia più alta va controllata per prima.
          // TODO: dichiara reddito, aliquota e catena if / else if / else
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain:
        - else if
        - double
  - path: demos/fasce_sconto.cpp
    action: reference
    phase: run
    description: Programma del laboratorio Run sulle fasce sconto.
---

## 🌲 Scaglioni ordinati: `if`, `else if` ed `else`

Nel capitolo precedente hai imparato a scegliere tra due strade. Nei contesti
aziendali, però, le alternative possono essere più di due: fasce di sconto,
livelli di fido, classi di rischio o aliquote fiscali.

Una catena `if / else if / else` permette di controllare più fasce in ordine e
di sceglierne una sola.

> 💡 **Metafora:** Immagina un nastro di smistamento logistico. Ogni sensore
> controlla una soglia; il primo sensore che riconosce il pacco lo devia verso
> la sua corsia. I sensori successivi non vedono più quel pacco: per questo
> l'ordine delle soglie decide il risultato.

**In questa lezione non** gestiamo ancora cicli o ripetizioni e non introduciamo
`switch`. Ci concentriamo su una sola classificazione ordinata, controllata
dall'alto verso il basso.

---

### 🎯 Obiettivi di apprendimento

Alla fine di questa lezione sei in grado di:

- ordinare soglie in una catena `if / else if / else` dalla più alta alla più bassa;
- prevedere quale sia il primo ramo vero e tracciare i rami saltati;
- assegnare un solo risultato esclusivo a un dato in una fascia;
- verificare il comportamento ai confini delle soglie.

---

### ⚙️ Prima del laboratorio: la scala delle fasce

```cpp
if (fatturato >= 50000.0) {
    sconto = 0.15;
} else if (fatturato >= 20000.0) {
    sconto = 0.10;
} else if (fatturato >= 5000.0) {
    sconto = 0.05;
} else {
    sconto = 0.0;
}
```

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| Primo `if` | Controlla la soglia più alta | Protegge la fascia più restrittiva |
| `else if` | Prova la soglia successiva solo se prima era falsa | Aggiunge un'alternativa |
| Ultimo `else` | Gestisce tutti i valori rimasti | Evita casi senza classificazione |
| Primo ramo vero | Ferma la catena | Le fasce sono esclusive |

Con soglie `>= 50000`, `>= 20000` e `>= 5000`, l'ordine corretto è dal valore
più alto al più basso. Un cliente con fatturato `60000` deve essere classificato
Platinum, non fermarsi prima nella fascia Gold.

---

### 🧭 Prima del laboratorio: seguire il flusso

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi fatturato;
if (fatturato >= 50000?) then (sì)
  :Platinum;
elseif (fatturato >= 20000?) then (sì)
  :Gold;
elseif (fatturato >= 5000?) then (sì)
  :Silver;
else (no)
  :Nessuna fascia;
endif
:Stampa il risultato;
stop
@enduml
```

Il programma non cerca “tutte le condizioni vere”: cerca il primo ramo vero.
Questo rende la catena adatta a classificazioni in cui ogni dato deve ricevere
una sola fascia.

---

### 🔬 Laboratorio PRIMM: fasce sconto cliente

Un gestionale assegna una fascia sconto in base al fatturato annuale di un
cliente.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma completo e confronta la fascia ottenuta con la tua
previsione.

```cpp
/**
 * @file fasce_sconto_cliente.cpp
 * @brief Classifica un cliente in una fascia sconto esclusiva.
 */
#include <iostream>
#include <string>

/**
 * @brief Assegna una fascia in base al fatturato annuale.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il nome identifica il cliente nel prospetto aziendale.
    std::string ragioneSociale = "Alpha Logistica Srl";
    /// Il fatturato decide la fascia commerciale.
    double fatturato = 32500.0;
    double sconto = 0.0;
    std::string fascia = "Nessuna";

    if (fatturato >= 50000.0) {
        sconto = 0.15;
        fascia = "Platinum";
    } else if (fatturato >= 20000.0) {
        sconto = 0.10;
        fascia = "Gold";
    } else if (fatturato >= 5000.0) {
        sconto = 0.05;
        fascia = "Silver";
    } else {
        sconto = 0.0;
        fascia = "Nessuna";
    }

    std::cout << "Cliente: " << ragioneSociale << "\n";
    std::cout << "Fatturato: " << fatturato << " euro\n";
    std::cout << "Fascia: " << fascia << "\n";
    std::cout << "Sconto: " << sconto * 100 << "%\n";
    return 0;
}
```
@LIA.cpp

Con `fatturato = 32500.0` il programma stampa la fascia Gold e lo sconto del
10%.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine dei confronti e spiega perché Silver non
viene più controllata dopo Gold.

[[ investigate_block() ]]

| Passo | Condizione | Esito | Azione |
| :---: | :--- | :---: | :--- |
| 1 | `32500 >= 50000` | falso | Passa a `else if` |
| 2 | `32500 >= 20000` | vero | Assegna Gold e `0.10` |
| 3 | `32500 >= 5000` | non controllata | La catena è già conclusa |
| 4 | `else` | non controllato | Esiste solo come alternativa finale |

Prova a cambiare `fatturato` in `3000.0`: tutte le soglie sono false e viene
scelta la fascia Nessuna. Prova poi `60000.0`: la prima condizione è vera e la
catena si ferma subito su Platinum.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva il percorso
> della condizione fino al primo ramo vero.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
if (fatturato >= 50000.0) {
    fascia = "Platinum";
} else if (fatturato >= 20000.0) {
    fascia = "Gold";
} else {
    fascia = "Nessuna";
}
```

</details>

**Modifica A — aggiungi Diamond**

Inserisci una fascia `Diamond` per fatturati almeno pari a `100000.0`.
Controllala prima di Platinum e verifica con `120000.0`.

**Modifica B — osserva l'ordine sbagliato**

Sposta temporaneamente il controllo Gold prima di Platinum. Prova con
`60000.0` e osserva perché il cliente viene classificato Gold.

**Modifica C — prova il confine**

Imposta il fatturato a `5000.0`. Verifica che la condizione `>=` includa il
valore esattamente uguale alla soglia Silver.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio amministrativo prepara un prospetto
semplificato dell'imposta per una ditta.

Crea `imposte_reddito.cpp` rispettando tutti i requisiti:

1. Dichiara `std::string nomeDitta` e `double redditoImponibile`.
2. Usa una catena `if / else if / else`.
3. Usa queste fasce fiscali con aliquota unica:
   - fino a `15000`: `23%`;
   - fino a `28000`: `25%`;
   - fino a `50000`: `35%`;
   - oltre `50000`: `43%`.
4. Controlla le soglie dalla più alta alla più bassa, oppure usa condizioni
   equivalenti chiaramente ordinate.
5. Calcola `imposta = redditoImponibile * aliquota`.
6. Stampa nome ditta, reddito, aliquota e imposta stimata.
7. Inserisci un commento `///` che spieghi perché la soglia più alta deve essere considerata per prima.

Questo è un modello didattico: non rappresenta un calcolo fiscale reale
progressivo.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Stima un'imposta con scaglioni fiscali.
 */
#include <iostream>
#include <string>

int main() {
    /// TODO: spiega perché l'ordine delle soglie evita classificazioni premature.
    // TODO: dichiara i dati, scegli l'aliquota e stampa il prospetto.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- [ ] `if / else if / else` classifica un dato in alternative esclusive.
- [ ] La catena si ferma al primo ramo vero.
- [ ] Con soglie `>=`, ordino i controlli dalla soglia più alta alla più bassa.
- [ ] L'ultimo `else` gestisce tutti i valori rimasti.
- [ ] Testo sempre i confini: esattamente soglia, appena sotto e appena sopra.

---

### ➡️ Prossimo passo nel percorso

Quando la decisione dipende da un valore discreto, come un codice menu o uno
stato numerico, una lunga catena può diventare difficile da leggere. Nel
prossimo capitolo del percorso Fondamenti, `10_selezione_multipla_switch`,
organizzerai questi casi con `switch`.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra nastro logistico e catena if
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli già introdotti
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/09_bivi_complessi_e_regole_if.md
#-->
