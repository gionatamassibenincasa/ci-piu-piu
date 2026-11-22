---
activity_id: while-01
title: 'Il nastro della cassa: ripetere con il ciclo while'
methodology: PRIMM
assignment_profile: full
order: 11
version: '2026-11-20'
last_update: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      int n = 0;

      while (n > 5) {
          std::cout << "Elaborazione\n";
          n = n + 1;
      }
    items:
      - question: 'Quante volte viene stampata la parola `Elaborazione`?'
        options:
          - text: 'Zero volte, perché la condizione `0 > 5` è falsa già all''inizio'
            correct: true
          - text: 'Una volta, perché ogni `while` esegue almeno un giro'
            correct: false
          - text: 'Cinque volte, perché il ciclo arriva fino a 5'
            correct: false
      - question: 'Perché il corpo del `while` non viene eseguito in questo esempio?'
        options:
          - text: 'Il `while` controlla la condizione prima di entrare nel corpo'
            correct: true
          - text: 'La stampa dentro il ciclo è vietata'
            correct: false
          - text: 'La variabile `n` viene automaticamente cancellata'
            correct: false
      - question: 'Quale ruolo ha `n = n + 1;` dentro il ciclo?'
        options:
          - text: 'Fa evolvere la variabile che può rendere falsa la condizione'
            correct: true
          - text: 'Riporta sempre `n` al valore iniziale'
            correct: false
          - text: 'Decide da sola quale testo stampare'
            correct: false
      - question: 'Quale elemento serve per fermare un ciclo che legge articoli fino a `0`?'
        options:
          - text: 'Un valore sentinella e una condizione che lo riconosce'
            correct: true
          - text: 'Un `switch` dentro ogni iterazione'
            correct: false
          - text: 'Una costante che deve essere sempre uguale a 1'
            correct: false
      - question: 'Perché un `while` può eseguire zero iterazioni?'
        options:
          - text: 'La condizione può essere falsa prima del primo ingresso nel corpo'
            correct: true
          - text: 'Il compilatore sceglie casualmente se saltare il primo giro'
            correct: false
          - text: 'Un ciclo esegue il corpo solo quando contiene `std::cin`'
            correct: false
  investigate_quiz:
    code: |
      double totaleSpesa = 0.0;
      int numeroArticoli = 0;
      double prezzoArticolo = 12.50;

      while (prezzoArticolo != 0.0) {
          totaleSpesa = totaleSpesa + prezzoArticolo;
          numeroArticoli = numeroArticoli + 1;
          prezzoArticolo = 0.0;
      }
    items:
      - question: 'Quale condizione permette al ciclo di entrare nel corpo al primo controllo?'
        options:
          - text: '`12.50 != 0.0`, che è vera'
            correct: true
          - text: '`0.0 != 12.50`, che viene controllata dopo il corpo'
            correct: false
          - text: 'La condizione non viene controllata al primo giro'
            correct: false
      - question: 'Perché dopo il giro il totale vale `12.50`?'
        options:
          - text: 'Il prezzo viene sommato prima che la variabile sia aggiornata a `0.0`'
            correct: true
          - text: 'Il ciclo aggiunge sempre due volte il primo prezzo'
            correct: false
          - text: 'La sentinella `0.0` viene conteggiata come prezzo'
            correct: false
      - question: 'Perché il secondo controllo non entra nel corpo?'
        options:
          - text: 'L''aggiornamento porta `prezzoArticolo` alla sentinella e rende falsa la condizione'
            correct: true
          - text: 'Il ciclo si ferma dopo un giro indipendentemente dalla condizione'
            correct: false
          - text: 'Il totale non può essere aggiornato più di una volta'
            correct: false
      - question: 'Quale valore non deve essere sommato in un ciclo con sentinella `0.0`?'
        options:
          - text: 'La sentinella `0.0`, perché serve solo a indicare la fine'
            correct: true
          - text: 'Ogni prezzo maggiore di zero'
            correct: false
          - text: 'Il primo prezzo valido inserito'
            correct: false
      - question: 'Che cosa rischi se rimuovi l''aggiornamento di `prezzoArticolo`?'
        options:
          - text: 'La condizione può restare vera e il ciclo può diventare infinito'
            correct: true
          - text: 'Il ciclo esegue automaticamente il ramo `else`'
            correct: false
          - text: 'La variabile diventa subito uguale alla sentinella'
            correct: false
  modify_quiz:
    code: |
      double prezzoArticolo = 12.50;
      double totaleSpesa = 0.0;

      while (prezzoArticolo != 0.0) {
          totaleSpesa = totaleSpesa + prezzoArticolo;
          std::cin >> prezzoArticolo;
      }
    items:
      - question: 'Quale modifica permette di contare anche il numero degli articoli?'
        options:
          - text: 'Dichiarare un contatore e incrementarlo dentro il corpo, prima della nuova lettura'
            correct: true
          - text: 'Aggiungere il contatore dopo il ciclo senza aggiornarlo'
            correct: false
          - text: 'Sostituire `while` con `switch`'
            correct: false
      - question: 'Dove devi inserire la nuova lettura se vuoi continuare a chiedere prezzi?'
        options:
          - text: 'Nel corpo del ciclo, così la condizione può cambiare al giro successivo'
            correct: true
          - text: 'Solo prima del `while`, perché il corpo non può leggere dati'
            correct: false
          - text: 'Dopo `return 0`, quando il programma è già terminato'
            correct: false
      - question: 'Che cosa succede se cambi la sentinella da `0.0` a `-1.0`?'
        options:
          - text: 'Il ciclo continua finché il prezzo non diventa `-1.0`, che non viene sommato'
            correct: true
          - text: 'Il ciclo termina sempre dopo il primo prezzo positivo'
            correct: false
          - text: 'Il valore `-1.0` viene automaticamente trasformato in `0.0`'
            correct: false
      - question: 'Quale modifica evita di sommare un prezzo negativo ma permette di continuare?'
        options:
          - text: 'Aggiungere un controllo nel corpo e aggiornare comunque il prossimo prezzo'
            correct: true
          - text: 'Usare `-1.0` come totale iniziale'
            correct: false
          - text: 'Mettere la lettura del prezzo fuori da `main`'
            correct: false
      - question: 'Perché conviene modificare una sola parte del ciclo alla volta?'
        options:
          - text: 'Per distinguere se l''errore riguarda condizione, corpo o aggiornamento'
            correct: true
          - text: 'Perché un `while` può contenere una sola istruzione'
            correct: false
          - text: 'Perché il compilatore impedisce di cambiare due righe consecutive'
            correct: false
  make_instructions: >
    Crea `fatture_fornitori.cpp`: leggi importi fino alla sentinella `-1.0`,
    non sommare la sentinella, accumula il totale, conta le fatture e conta quelle
    almeno pari a 1000 euro. Stampa un riepilogo finale.
  visualization:
    kind: pythontutor
    note: 'Seguire prezzo, totale e contatore a ogni iterazione e osservare quando la sentinella ferma il ciclo.'
registro:
  argomenti: 'Ciclo `while` con controllo in testa; inizializzazione, condizione e aggiornamento; sentinella; accumulatore e contatore; laboratorio PRIMM su uno scontrino a nastro.'
  note: 'Verifica formativa su ciclo controllato da sentinella e prevenzione dei cicli infiniti.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Riconoscere il controllo in testa e prevedere il caso di zero iterazioni.'
  investigate:
    points: 2
    questions:
      - 'Perché il corpo viene eseguito con il primo prezzo?'
      - 'Perché la sentinella non entra nel totale?'
      - 'Che cosa succede senza aggiornamento della variabile di controllo?'
    typical_errors:
      - 'Pensare che ogni while esegua almeno un giro'
      - 'Sommare anche la sentinella'
    context: 'Seguire il tracing di totale, contatore e variabile controllata.'
  modify:
    points: 1
    prompt: 'Aggiungi un contatore che aumenti di uno per ogni prezzo valido e stampa il numero di articoli dopo il ciclo.'
    code: |
      double prezzoArticolo = 12.50;
      double totaleSpesa = 0.0;

      while (prezzoArticolo != 0.0) {
          totaleSpesa = totaleSpesa + prezzoArticolo;
          std::cin >> prezzoArticolo;
      }
    typical_errors:
      - 'Incrementare il contatore dopo la lettura della sentinella'
      - 'Dimenticare di dichiarare il contatore'
    context: 'Aggiungere un contatore senza includere la sentinella.'
  make:
    points: 1
    prompt: 'Registra fatture fino a `-1.0`, calcola totale, numero fatture e numero di fatture rilevanti almeno pari a 1000 euro.'
    must_include:
      - 'while'
      - 'std::cin'
      - '-1.0'
      - 'double'
    typical_errors:
      - 'Somma la sentinella'
      - 'Dimentica la nuova lettura nel corpo del ciclo'
    context: 'Trasferire il pattern sentinella-accumulatore a un processo amministrativo.'
  variants:
    B:
      modify:
        prompt: 'Sostituisci la sentinella `0.0` con `-1.0` e mantieni il conteggio dei soli prezzi validi.'
        code: |
          double prezzoArticolo = 12.50;
          double totaleSpesa = 0.0;

          while (prezzoArticolo != 0.0) {
              totaleSpesa = totaleSpesa + prezzoArticolo;
              std::cin >> prezzoArticolo;
          }
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Ciclo while

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      In ogni ciclo verifica inizializzazione, condizione e aggiornamento.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – While

      Rispondi prima di eseguire il programma.

      1. Quante volte gira il ciclo se la condizione è falsa all'inizio?
      >

      2. Quale variabile deve cambiare?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Scontrino

      1. Quali prezzi hai inserito?
      >

      2. La sentinella è stata sommata?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Ciclo

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Perché il corpo viene eseguito con il primo prezzo?
      >

      2. Perché la sentinella non entra nel totale?
      >

      3. Che cosa succede senza aggiornamento della variabile di controllo?
      >
  - path: student_work/modify/scontrino_nastro.cpp
    action: create
    phase: modify
    template_content: |
      #include <iostream>

      int main() {
          double prezzoArticolo = 1.0;
          while (prezzoArticolo != 0.0) {
              std::cin >> prezzoArticolo;
          }
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain:
        - while
        - std::cin
  - path: student_work/make/fatture_fornitori.cpp
    action: create
    phase: make
    description: Registro delle fatture fornitori con sentinella -1.0.
    template_content: |
      /**
       * @brief Registra fatture fornitori fino alla sentinella -1.0.
       */
      #include <iostream>

      int main() {
          /// TODO: spiega perché la sentinella non deve entrare nel totale.
          // TODO: inizializza totali e contatori, poi scrivi il while.
          return 0;
      }
    validation_rules:
      min_lines: 10
      must_contain:
        - while
        - std::cin
        - '-1.0'
---

## 🔄 Il nastro della cassa: ripetere con il ciclo `while`

Quanti articoli ha un cliente? Tre, dodici, settantacinque: spesso non lo sai
prima di iniziare. Con variabili separate dovresti preparare `prezzo1`,
`prezzo2`, `prezzo3` e sperare che bastino.

Il ciclo `while` permette di ripetere lo stesso blocco finché una condizione
rimane vera.

> 💡 **Metafora:** Immagina il nastro della cassa. Finché arriva un articolo,
> il nastro avanza e il totale cresce. Quando arriva il separatore con valore
> sentinella, il nastro si ferma e viene emesso lo scontrino. Se il carrello è
> già vuoto all'inizio, il nastro non fa neppure un giro.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un ciclo `while` che legge dati fino a una sentinella e aggiorna la condizione a ogni giro.

---

### ⚙️ Prima del laboratorio: i tre ingredienti

Il `while` controlla la condizione **prima** di entrare nel corpo:

```cpp
double prezzo = 0.0;
std::cin >> prezzo;

while (prezzo != 0.0) {
    totale = totale + prezzo;
    std::cin >> prezzo;
}
```

| Ingrediente | Ruolo | Se manca |
| :--- | :--- | :--- |
| Inizializzazione | Prepara il valore prima del ciclo | La condizione parte da uno stato imprevedibile |
| Condizione | Decide se entrare e ripetere | Il corpo non sa quando fermarsi |
| Aggiornamento | Cambia il valore controllato | Può nascere un ciclo infinito |

Una sentinella è un valore speciale che indica “basta”. Non è un dato da
elaborare, quindi non deve entrare nel totale.

---

### 🧭 Prima del laboratorio: controllo in testa

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi il primo prezzo;
while (prezzo != sentinella?) is (sì)
  :Somma il prezzo;
  :Incrementa il contatore;
  :Leggi il prezzo successivo;
endwhile (no)
:Stampa il riepilogo;
stop
@enduml
```

Con input `12.50`, `3.20`, `0.0`:

| Valore letto | Condizione | Azione |
| :---: | :---: | :--- |
| `12.50` | vera | Somma e conta |
| `3.20` | vera | Somma e conta |
| `0.0` | falsa | Ferma il ciclo, non sommare |

---

### 🔬 Laboratorio PRIMM: scontrino a nastro

Accumula i prezzi finché l'utente inserisce `0.0`, la sentinella di fine
spesa.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma completo. Inserisci uno o più prezzi e termina con `0`.

```cpp
/**
 * @file scontrino_nastro.cpp
 * @brief Accumula prezzi fino alla sentinella 0.0.
 */
#include <iostream>

/**
 * @brief Legge gli articoli e stampa totale e numero di pezzi.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il totale raccoglie solo i prezzi validi dello scontrino.
    double totaleSpesa = 0.0;
    /// Il contatore serve a descrivere quante righe sono state registrate.
    int numeroArticoli = 0;
    double prezzoArticolo = 0.0;

    std::cout << "Prezzo articolo (0 per terminare): ";
    std::cin >> prezzoArticolo;

    while (prezzoArticolo != 0.0) {
        totaleSpesa = totaleSpesa + prezzoArticolo;
        numeroArticoli = numeroArticoli + 1;
        std::cout << "Prezzo articolo (0 per terminare): ";
        std::cin >> prezzoArticolo;
    }

    std::cout << "=== SCONTRINO ===\n";
    std::cout << "Articoli: " << numeroArticoli << "\n";
    std::cout << "Totale: " << totaleSpesa << " EUR\n";
    return 0;
}
```
@LIA.cpp

Prova con:

```text
12.50
3.20
0
```

Il totale deve essere `15.70`: lo `0` serve a fermare il ciclo e non è un
prezzo.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine delle letture e degli aggiornamenti.

[[ investigate_block() ]]

| Momento | `prezzoArticolo` | Condizione | Totale |
| :--- | :---: | :---: | :---: |
| Primo controllo | `12.50` | vera | `0.00` |
| Dopo il primo corpo | `3.20` | prossimo controllo | `12.50` |
| Dopo il secondo corpo | `0.0` | prossimo controllo falsa | `15.70` |
| Uscita | `0.0` | falsa | `15.70` |

Il controllo è in testa: quando il valore è `0.0`, il corpo non viene più
eseguito. Se rimuovi la nuova lettura dentro il ciclo, `prezzoArticolo` resta
uguale e la condizione può rimanere vera per sempre.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva prezzo, totale
> e contatore a ogni iterazione.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
double prezzoArticolo = 0.0;
std::cin >> prezzoArticolo;

while (prezzoArticolo != 0.0) {
    totaleSpesa = totaleSpesa + prezzoArticolo;
    std::cin >> prezzoArticolo;
}
```

</details>

**Modifica A — conta gli articoli**

Dichiara `int numeroArticoli = 0` prima del ciclo e incrementalo dentro il
corpo, insieme al totale. La sentinella non deve aumentare il contatore.

**Modifica B — calcola la media**

Dopo il ciclo, se `numeroArticoli > 0`, calcola
`totaleSpesa / numeroArticoli`. Per ora puoi usare un `if` semplice per evitare
la divisione quando non è stato inserito alcun articolo.

**Modifica C — cambia sentinella**

Sostituisci `0.0` con `-1.0` in tutti i punti necessari. Il ciclo deve fermarsi
solo con `-1.0`, che non va sommato.

**Esperimento controllato — ciclo infinito**

Commenta temporaneamente la nuova lettura nel corpo. Il programma non riceverà
più un valore capace di fermare la condizione: interrompilo e ripristina la
lettura.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio amministrativo registra le fatture dei
fornitori fino alla fine dell'importazione.

Crea `fatture_fornitori.cpp` rispettando tutti i requisiti:

1. Usa `double importo` e la sentinella `-1.0`.
2. Leggi il primo importo prima del `while`.
3. Continua finché `importo != -1.0`.
4. Non sommare la sentinella.
5. Accumula `totaleDebiti`.
6. Conta tutte le fatture e quelle rilevanti, con importo almeno `1000.0`.
7. Stampa totale, numero fatture e numero rilevanti.
8. Inserisci un commento `///` che spieghi perché la sentinella non è una fattura.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Registra fatture fornitori fino alla sentinella -1.0.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché la sentinella non deve entrare nel totale.
    // TODO: inizializza totale e contatori, leggi il primo importo.
    // TODO: scrivi il while e stampa il riepilogo.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `while` ripete il corpo mentre la condizione è vera.
- Il controllo è in testa: sono possibili zero iterazioni.
- Ogni ciclo ha inizializzazione, condizione e aggiornamento.
- Una sentinella ferma il ciclo e non va elaborata.
- Senza aggiornamento della variabile controllata può nascere un ciclo infinito.

---

### ➡️ Prossimo chunk

Quando sai già quante volte ripetere, per esempio dodici mesi o trenta righe,
`while` può diventare verboso. Nel prossimo capitolo userai `for` per raccogliere
inizializzazione, condizione e aggiornamento in una sola riga.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra nastro della cassa e while
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli già introdotti
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/10_ciclo_while.md
#-->
