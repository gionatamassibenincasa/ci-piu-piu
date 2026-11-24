---
activity_id: ruoli-pattern-cicli-16
title: 'Un ruolo per ogni variabile, uno schema per ogni ciclo'
methodology: PRIMM
assignment_profile: full
order: 16
version: '2026-11-24'
language: it
components:
  predict_quiz:
    code: |
      double totale = 0.0;
      double massimo = 0.0;
      int numero = 0;
      double importo;
      bool primo = true;

      std::cin >> importo;
      while (importo != -1.0) {
          totale += importo;
          ++numero;
          if (primo || importo > massimo) {
              massimo = importo;
              primo = false;
          }
          std::cin >> importo;
      }
    items:
      - question: 'Quale ruolo ha `totale` nel codice?'
        options:
          - text: 'Accumulatore: dipende dal suo valore precedente e da ogni nuovo importo'
            correct: true
          - text: 'Contatore: cambia un passo alla volta indipendentemente dagli importi'
            correct: false
          - text: 'Sentinella: indica con quale valore termina il ciclo'
            correct: false
      - question: 'Perché `numero` viene incrementato con `++numero`?'
        options:
          - text: 'È un contatore: conta quante fatture valide sono state elaborate'
            correct: true
          - text: 'È un accumulatore: somma gli importi inseriti'
            correct: false
          - text: 'È una sentinella: termina il ciclo quando arriva a meno uno'
            correct: false
      - question: 'Quale ruolo ha `importo` prima di ogni lettura?'
        options:
          - text: 'Valore più recente: conserva l''ultimo dato letto'
            correct: true
          - text: 'Valore fissato: non può cambiare dopo l''inizializzazione'
            correct: false
          - text: 'Precedente: conserva sempre il dato letto due passi fa'
            correct: false
      - question: 'Perché `massimo` cambia solo in alcuni passaggi?'
        options:
          - text: 'È un valore più desiderato: conserva il candidato migliore trovato finora'
            correct: true
          - text: 'È un contatore: avanza fino al limite della sequenza'
            correct: false
          - text: 'È un accumulatore: somma tutti i valori confrontati'
            correct: false
      - question: 'Che cosa rende questo ciclo uno schema di scansione fino a sentinella?'
        options:
          - text: '`-1.0` termina la lettura e non viene elaborato come fattura'
            correct: true
          - text: 'Il ciclo usa un numero fisso di iterazioni'
            correct: false
          - text: '`primo` viene controllato solo una volta'
            correct: false
  investigate_quiz:
    code: |
      double totale = 0.0;
      double massimo = 0.0;
      int numero = 0;
      double importo;
      bool primo = true;

      std::cin >> importo;
      while (importo != -1.0) {
          totale += importo;
          ++numero;
          if (primo || importo > massimo) {
              massimo = importo;
              primo = false;
          }
          std::cin >> importo;
      }
    items:
      - question: 'Con input `120.0`, `80.0`, `-1.0`, quale stato assume `totale` alla fine?'
        options:
          - text: '`200.0`, perché la sentinella non viene sommata'
            correct: true
          - text: '`201.0`, perché vengono conteggiati due dati e la sentinella'
            correct: false
          - text: '`-1.0`, perché è l''ultimo valore letto'
            correct: false
      - question: 'Perché `massimo` vale `120.0` dopo i due importi?'
        options:
          - text: 'Il primo importo lo inizializza e il secondo non lo supera'
            correct: true
          - text: 'Il contatore `numero` restituisce direttamente il valore massimo'
            correct: false
          - text: 'Il ciclo sostituisce sempre il massimo con il dato successivo'
            correct: false
      - question: 'Che cosa accade se sposti `totale = 0.0` dentro il ciclo?'
        options:
          - text: 'Ogni importo cancella il totale precedente e il risultato finale è incompleto'
            correct: true
          - text: 'Il totale viene sommato una volta in più alla fine'
            correct: false
          - text: 'La sentinella viene contata come fattura'
            correct: false
      - question: 'Perché `primo` è una bandiera unidirezionale utile in questo esempio?'
        options:
          - text: 'Serve solo finché il primo candidato non è stato fissato'
            correct: true
          - text: 'Deve tornare vera dopo ogni nuovo massimo'
            correct: false
          - text: 'Serve a sommare due volte il primo importo'
            correct: false
      - question: 'Quale schema descrive meglio il ciclo completo?'
        options:
          - text: 'Scansione fino a sentinella con accumulo e selezione del massimo'
            correct: true
          - text: 'Scansione con conteggio noto tramite `for`'
            correct: false
          - text: 'Ricerca certa dopo un ordinamento'
            correct: false
  modify_quiz:
    code: |
      double totale = 0.0;
      double massimo = 0.0;
      int numero = 0;
      double importo;
      bool primo = true;
    items:
      - question: 'Quale modifica conta solo le fatture almeno pari a 100 euro?'
        options:
          - text: 'Dentro il ciclo, usare `if (importo >= 100.0)` prima di totale e contatore'
            correct: true
          - text: 'Cambiare la sentinella da `-1.0` a `100.0`'
            correct: false
          - text: 'Aumentare `massimo` dentro ogni iterazione'
            correct: false
      - question: 'Quale modifica trasforma il valore massimo in minimo mantenendo il primo candidato?'
        options:
          - text: 'Confrontare `importo < minimo` e aggiornare il minimo nel ramo vero'
            correct: true
          - text: 'Dichiarare `minimo` dentro il ciclo'
            correct: false
          - text: 'Sostituire la sentinella con `0.0`'
            correct: false
      - question: 'Come puoi tracciare una diminuzione rispetto all''importo precedente?'
        options:
          - text: 'Mantenere `precedente`, confrontare `importo < precedente` e aggiornarlo alla fine'
            correct: true
          - text: 'Usare `massimo` al posto di `precedente` senza aggiornamenti'
            correct: false
          - text: 'Sommare `precedente` al totale ad ogni giro'
            correct: false
      - question: 'Quale modifica rende `trovato` vero una sola volta senza annullarlo nei successivi giri?'
        options:
          - text: 'Usare `if (importo >= soglia) trovato = true;` senza assegnazioni false successive'
            correct: true
          - text: 'Porre `trovato = false` dopo ogni importo valido'
            correct: false
          - text: 'Azzerare `trovato` appena la sentinella viene letta'
            correct: false
      - question: 'Perché conviene modificare una sola parte del tracciare?'
        options:
          - text: 'Per collegare il nuovo stato osservato al ruolo modificato: accumulatore, massimo o precedente'
            correct: true
          - text: 'Perché una sola variabile può esistere in un ciclo'
            correct: false
          - text: 'Perché il compilatore accetta al massimo un aggiornamento per prova'
            correct: false
  make_instructions: >
    Crea registro_fatture.cpp per un ufficio fornitori: leggi importi fino alla
    sentinella -1.0, calcola totale e numero, trova il massimo, conta una
    diminuzione consecutiva usando un precedente e stampa una breve diagnosi.
  visualization:
    kind: pythontutor
    note: 'Osservare accumulatore, contatore, massimo, valore precedente e sentinella a ogni lettura.'
registro:
  argomenti: 'Ruoli delle variabili; accumulatore, contatore, valore più recente, valore più desiderato, precedente e flag; pattern di scansione fino a sentinella, accumulo, filtro e ricerca del massimo.'
  note: 'Laboratorio PRIMM su un registro fatture aziendale e linguaggio semantico condiviso.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Riconoscere i ruoli delle variabili in un ciclo con accumulo e massimo.'
  investigate:
    points: 2
    questions:
      - 'Quale stato ha totale dopo la lettura di 120.0 e 80.0 seguiti dalla sentinella?'
      - 'Perché massimo vale 120.0 e non 80.0?'
      - 'Perché un accumulatore deve essere inizializzato fuori dal ciclo?'
    typical_errors:
      - 'Confondere accumulatore e contatore'
      - 'Sommare la sentinella o usare il suo valore come candidato massimo'
    context: 'Tracciare valori e motivare l''ordine delle inizializzazioni e degli aggiornamenti.'
  modify:
    points: 1
    prompt: 'Aggiungi un filtro per contare solo fatture di almeno 100 euro e conserva totale, massimo e numero separati.'
    code: |
      double totale = 0.0;
      double massimo = 0.0;
      int numero = 0;
      // inserisci qui la lettura e il ciclo
    typical_errors:
      - 'Aggiorna numero anche per fatture sotto soglia'
      - 'Azzera totale dentro il ciclo'
    context: 'Separare la condizione di filtro dagli aggiornamenti degli altri ruoli.'
  make:
    points: 1
    prompt: 'Crea registro_fatture.cpp: legge fatture fino a -1.0 e registra totale, numero, massimo e il numero di diminuzioni consecutive.'
    must_include:
      - 'sentinella -1.0'
      - 'accumulatore'
      - 'valore più desiderato'
      - 'precedente'
    typical_errors:
      - 'Somma la sentinella'
      - 'Aggiorna il precedente al primo giro senza inizializzarlo'
    context: 'Integrare accumulo, massimo e confronto tra dati adiacenti in una scansione reale.'
  variants:
    B:
      modify:
        prompt: 'Aggiungi il minimo al posto del massimo e filtra solo fatture superiori a 50 euro.'
        code: |
          double totale = 0.0;
          double minimo = 0.0;
          int numero = 0;
          // inserisci qui la lettura e il ciclo
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Un ruolo per ogni variabile

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Prima del codice, assegna a ogni variabile un ruolo e controlla dove viene inizializzata.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Ruoli e pattern

      Rispondi prima di eseguire il programma.

      1. Quale ruolo ha totale?
      >

      2. Quale ruolo ha numero?
      >

      3. Perché importo è il valore più recente?
      >

      4. Come viene selezionato massimo?
      >

      5. Perché -1.0 è una sentinella?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Registro fatture

      Esegui il programma con tre importi, poi termina con -1.0.

      1. Quali importi hai inserito?
      >

      2. Quali valori finali hanno totale, numero e massimo?
      >

      3. Quale importo è stato escluso dalla sentinella?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Stato delle variabili

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Quale stato ha totale dopo la lettura di 120.0 e 80.0 seguiti dalla sentinella?
      >

      2. Perché massimo vale 120.0 e non 80.0?
      >

      3. Perché un accumulatore deve essere inizializzato fuori dal ciclo?
      >
  - path: student_work/modify/registro_modificato.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          double totale = 0.0;
          double massimo = 0.0;
          int numero = 0;
          // TODO: leggi fino a -1.0
          // TODO: conta solo fatture da 100 euro
          return 0;
      }
    validation_rules:
      min_lines: 10
      must_contain:
        - while
        - -1.0
        - if
  - path: student_work/make/registro_fatture.cpp
    action: create
    phase: make
    description: Registro fatture con accumulo, massimo e confronto tra importi adiacenti.
    template_content: |
      /**
       * @brief Registra fatture fino alla sentinella e riassume i dati rilevati.
       */
      #include <iostream>

      int main() {
          /// TODO: spiega perché la sentinella deve restare fuori dai dati elaborati.
          // TODO: dichiara accumulatore, contatore, massimo, precedente e lettura.
          // TODO: scansione fino a -1.0, aggiorna i ruoli e stampa il riepilogo.
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain:
        - while
        - -1.0
        - if
---

## 🧭 Un ruolo per ogni variabile, uno schema per ogni ciclo

In un gestionale molte parti del codice sembrano ripetizioni. In realtà ogni
variabile svolge un lavoro preciso: sommare, contare, conservare l'ultimo dato,
tenere il migliore trovato finora o confrontare lo stato precedente.

Riconoscere questi ruoli ti permette di leggere una soluzione già nota e
riutilizzare lo schema corretto invece di partire ogni volta da zero.

> 💡 **Metafora:**  
> Immagina una scrivania di controllo fatture. Il **contatore** annota quante
> righe sono state esaminate; l'**accumulatore** tiene il totale aperto; il
> **valore più recente** registra l'ultima fattura letta; il **valore più
> desiderato** conserva il massimo; il **precedente** serve a confrontare due
> fatture consecutive. La sentinella è il segnale rosso che chiude la serie.

**In questa lezione non** introduciamo funzioni, array o puntatori. I pattern
sono applicati a dati letti in sequenza con `while`, `for`, `if` e `do-while`.

---

### 🎯 Obiettivi di apprendimento

Alla fine di questa lezione sei in grado di:

- assegnare un ruolo osservabile a variabili che accumulano, contano, conservano il valore recente o scelgono un massimo;
- riconoscere uno schema di ciclo con sentinella, accumulo, filtro o confronto adiacente;
- tracciare i valori delle variabili prima e dopo ogni iterazione;
- adattare uno schema noto a un problema gestionale diverso.

---

### ⚙️ Prima del laboratorio: ruoli e pattern

| Ruolo | Domanda guida | Aggiornamento tipico |
| :--- | :--- | :--- |
| Valore fissato | Quale dato resta invariato durante la sequenza? | `const` o inizializzazione |
| Contatore | Quante volte o quanti elementi sono stati osservati? | `++numero` |
| Accumulatore | Qual è il risultato aggregato finora? | `totale += importo` |
| Valore più recente | Qual è stato l'ultimo dato letto? | assegnazione dalla lettura |
| Valore più desiderato | Qual è il massimo o il minimo finora? | aggiornamento condizionale |
| Precedente | Quale valore è stato letto nel passo precedente? | salva dopo il confronto |
| Flag unidirezionale | Qualcosa è accaduto almeno una volta? | da `false` a `true` |

I pattern non sono nuovi costrutti: sono combinazioni ricorrenti di variabili
e istruzioni già conosciute.

| Pattern | Controllo del ciclo | Stato principale |
| :--- | :--- | :--- |
| Conteggio noto | `for` con un contatore | contatore / accumulatore |
| Scansione fino a sentinella | `while` finché il dato non è speciale | valore più recente |
| Accumulazione | ciclo + aggiornamento dipendente dallo stato precedente | accumulatore |
| Filtro e conteggio | ciclo + `if` | contatore filtrato |
| Selezione dell'estremo | ciclo + confronto condizionale | valore più desiderato |
| Confronto adiacente | ciclo + dato precedente | precedente |
| Ricerca lineare | ciclo + arresto o flag | trovato / indice |

---

### 🧭 Prima del laboratorio: stato per stato

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Inizializza totale, numero, massimo;
:Leggi il primo importo;
while (importo != sentinella?) is (sì)
  :Aggiorna totale;
  :Conta la fattura;
  if (è il primo o è maggiore del massimo?) then (sì)
    :Aggiorna massimo;
  endif
  :Leggi il prossimo importo;
endwhile (no)
:Stampa il riepilogo;
stop
@enduml
```

L'ordine delle inizializzazioni è parte del pattern. Un accumulatore deve partire
da zero prima del ciclo; un massimo può partire dal primo dato valido o usare
una condizione esplicita con la bandiera `primo`.

---

### 🔬 Laboratorio PRIMM: Registro fatture fornitore

Il programma legge importi fino alla sentinella `-1.0`. Per ogni fattura registra
il totale, il numero dei dati validi e il massimo ricevuto finora.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

Prima di eseguire, indovina il ruolo di ogni variabile; non limitarti a
prevedere il risultato numerico.

#### 2. RUN (Esegui)

Digita il programma completo e prova con `120.0`, `80.0`, `150.0`, `-1.0`.

```cpp
/**
 * @file registro_fatture.cpp
 * @brief Analizza una sequenza di fatture fino alla sentinella -1.0.
 * @return int 0 se il programma termina correttamente.
 */
#include <iostream>

int main() {
    /// Il totale aggrega solo gli importi letti prima della sentinella.
    double totale = 0.0;
    /// Il contatore registra il numero di fatture valide.
    int numero = 0;
    /// Il massimo viene aggiornato solo quando trova un candidato migliore.
    double massimo = 0.0;
    double importo = 0.0;
    bool primo = true;

    std::cout << "Importo fattura (-1 per terminare): ";
    std::cin >> importo;

    while (importo != -1.0) {
        totale += importo;
        ++numero;

        if (primo || importo > massimo) {
            massimo = importo;
            primo = false;
        }

        std::cout << "Importo fattura (-1 per terminare): ";
        std::cin >> importo;
    }

    std::cout << "Totale: " << totale << " euro\n";
    std::cout << "Numero fatture: " << numero << "\n";
    std::cout << "Massimo: " << massimo << " euro\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

Dopo il Run, confronta stato e ruolo di ogni variabile.

[[ investigate_block() ]]

| Input | `totale` | `numero` | `massimo` | Ruolo visibile |
| :---: | :---: | :---: | :---: | :--- |
| `120.0` | `120.0` | `1` | `120.0` | primo candidato |
| `80.0` | `200.0` | `2` | `120.0` | accumulo + massimo invariato |
| `150.0` | `350.0` | `3` | `150.0` | nuovo valore più desiderato |
| `-1.0` | `350.0` | `3` | `150.0` | sentinella, non elaborata |

Apri il programma in [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva in quale momento `totale`, `numero`, `massimo` e `primo` cambiano.

#### 4. MODIFY (Modifica)

Prima di modificare, usa il quiz per prevedere la nuova organizzazione dello stato.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double totale = 0.0;
    double massimo = 0.0;
    int numero = 0;
    double importo = 0.0;
    bool primo = true;

    // TODO: leggi fino a -1.0
    // TODO: aggiorna totale, numero e massimo
    // TODO: stampa il riepilogo
    return 0;
}
```

</details>

**Modifica A — filtro sulle fatture rilevanti**

Conta e somma solo gli importi almeno pari a `100.0`. Il massimo deve essere
calcolato sugli stessi dati filtrati.

**Modifica B — minimo invece di massimo**

Trasforma il valore più desiderato in un minimo. Mantieni la bandiera `primo`
finché non hai osservato il primo candidato.

**Modifica C — confronto tra fatture adiacenti**

Aggiungi `double precedente = 0.0;` e un contatore delle diminuzioni
consecutive. Aggiorna `precedente` solo dopo aver confrontato l'importo
corrente.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio fornitori controlla una sequenza di fatture
senza sapere in anticipo quante righe saranno inserite.

Crea `registro_fatture.cpp` rispettando tutti i requisiti:

1. Leggi importi finché l'utente inserisce `-1.0`.
2. Non sommare né conteggiare la sentinella.
3. Usa un accumulatore per il totale.
4. Usa un contatore per il numero di fatture valide.
5. Usa un valore più desiderato per conservare il massimo.
6. Usa un precedente per riconoscere una diminuzione rispetto alla fattura precedente.
7. Conta quante diminuzioni consecutive sono state rilevate.
8. Stampa totale, numero, massimo e numero di diminuzioni.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Riassume importi fatture con accumulo e confronto adiacente.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché la sentinella non rappresenta una fattura.
    // TODO: inizializza totale, numero, massimo, precedente e lettura
    // TODO: scansione fino a -1.0
    // TODO: aggiorna i ruoli e stampa il riepilogo
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- [ ] Valore fissato, contatore e accumulatore hanno responsabilita diverse.
- [ ] Il valore più recente conserva l'ultimo dato letto.
- [ ] Il valore più desiderato viene aggiornato solo da un candidato migliore.
- [ ] Il precedente serve a confrontare dati adiacenti.
- [ ] Un accumulatore si inizializza fuori dal ciclo e viene aggiornato dentro.
- [ ] Una sentinella termina la scansione e non viene elaborata.
- [ ] Chiamare una sequenza con il suo pattern rende il codice leggibile e prevedibile.

---

### ➡️ Prossimo passo nel percorso

Ora sai riconoscere il ruolo di ogni variabile e scegliere uno schema di ciclo.
Nel prossimo capitolo del percorso Fondamenti, `17_funzioni_scomposizione_top_down`,
metterai questa capacità dentro reparti software riutilizzabili: le funzioni.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo principale
  [x] Metafora esplicita con ruoli delle variabili
  [x] 5 domande Predict concettuali
  [x] 5 domande Investigate perché / tracing
  [x] 5 domande Modify sull'effetto delle modifiche
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Nessun array, puntatore o funzione anticipati
  [ ] validate da eseguire
#-->
