---
activity_id: break-continue-01
title: 'Uscite Anticipate: `break` e `continue` nei cicli'
methodology: PRIMM
assignment_profile: full
order: 14
version: '2026-11-22'
language: it
components:
  predict_quiz:
    code: |
      for (int i = 1; i <= 5; ++i) {
          if (i == 2) continue;
          if (i == 4) break;
          std::cout << i;
      }
    items:
      - question: 'Qual è l’effetto di `continue` quando `i` vale 2?'
        options:
          - text: 'Salta il resto del giro corrente e passa al giro successivo'
            correct: true
          - text: 'Esce definitivamente dal ciclo'
            correct: false
          - text: 'Ripete il giro corrente senza aggiornare `i`'
            correct: false
      - question: 'Qual è l’effetto di `break` quando `i` vale 4?'
        options:
          - text: 'Esce subito dal ciclo e non raggiunge il giro con `i` uguale a 5'
            correct: true
          - text: 'Salta solo la stampa di 4 e continua con 5'
            correct: false
          - text: 'Riporta `i` a 1 e ricomincia il ciclo'
            correct: false
      - question: 'Quale output è più coerente con il flusso del ciclo?'
        options:
          - text: '`13`, perché 2 viene saltato e il ciclo termina quando arriva a 4'
            correct: true
          - text: '`1345`, perché `break` salta soltanto il numero 4'
            correct: false
          - text: '`12345`, perché i due comandi non cambiano l’output'
            correct: false
      - question: 'Perché il ciclo non stampa `2`?'
        options:
          - text: 'Perché `continue` viene eseguito prima di `std::cout` nel giro con `i == 2`'
            correct: true
          - text: 'Perché `i` diventa automaticamente uguale a 0'
            correct: false
          - text: 'Perché `break` viene eseguito due volte nello stesso giro'
            correct: false
      - question: 'In quale situazione aziendale è più adatto `break`?'
        options:
          - text: 'Quando un dato anomalo rende inutile o rischiosa l’analisi dei dati successivi'
            correct: true
          - text: 'Quando vuoi ignorare un solo dato ma continuare con tutti gli altri'
            correct: false
          - text: 'Quando vuoi aumentare automaticamente il valore del contatore'
            correct: false
  investigate_quiz:
    code: |
      for (int i = 1; i <= 5; ++i) {
          if (i == 2) continue;
          if (i == 4) break;
          std::cout << i;
      }
    items:
      - question: 'Quale sequenza di azioni avviene quando `i` vale 2?'
        options:
          - text: 'La prima condizione è vera, parte `continue`, non si stampa 2 e il `for` aggiorna il contatore'
            correct: true
          - text: 'Si stampa 2, poi la seconda condizione interrompe il ciclo'
            correct: false
          - text: 'Il ciclo termina e il valore 3 non viene mai controllato'
            correct: false
      - question: 'Perché il valore 3 viene stampato?'
        options:
          - text: 'Entrambe le condizioni sono false, quindi il flusso raggiunge `std::cout`'
            correct: true
          - text: '`continue` stampa automaticamente il valore che segue quello saltato'
            correct: false
          - text: '`break` trasforma 3 in un valore valido da stampare'
            correct: false
      - question: 'Dopo `continue` in questo `for`, cosa succede normalmente?'
        options:
          - text: 'Viene eseguita l’espressione di aggiornamento `++i`, poi si controlla la condizione del ciclo'
            correct: true
          - text: 'Il programma torna alla dichiarazione di `i` e la reinizializza a 1'
            correct: false
          - text: 'Il programma salta direttamente alla riga dopo tutto il ciclo'
            correct: false
      - question: 'Perché il valore 5 non viene mai stampato?'
        options:
          - text: 'Con `i == 4` viene eseguito `break`, che termina il ciclo prima del giro successivo'
            correct: true
          - text: 'Il `for` arriva solo fino a 4 anche se la condizione dice `i <= 5`'
            correct: false
          - text: 'Il compilatore considera 5 un valore non stampabile dopo un `continue`'
            correct: false
      - question: 'Se sostituisci `continue` con `break` nella condizione `i == 2`, perché l’output diventa `1`?'
        options:
          - text: 'Il ciclo termina già al secondo giro, prima di poter controllare 3 e 4'
            correct: true
          - text: 'Il secondo comando `break` viene ignorato perché ce n’è già uno'
            correct: false
          - text: 'Il primo giro viene annullato insieme a tutti i valori già stampati'
            correct: false
  modify_quiz:
    code: |
      for (int i = 1; i <= 5; ++i) {
          if (i == 2) continue;
          if (i == 4) break;
          std::cout << i;
      }
    items:
      - question: 'Quale modifica stampa `124` e termina il ciclo dopo 4?'
        options:
          - text: 'Spostare `std::cout << i;` prima dei due controlli e lasciare `break` su 4'
            correct: true
          - text: 'Sostituire `continue` su 2 con `break` e lasciare tutto il resto invariato'
            correct: false
          - text: 'Cambiare `i == 4` in `i == 5` senza spostare la stampa'
            correct: false
      - question: 'Quale modifica salta gli importi pari ma continua a controllare gli altri?'
        options:
          - text: 'Usare `if (importo % 2 == 0) continue;` dentro il ciclo'
            correct: true
          - text: 'Usare `if (importo % 2 == 0) break;` per ogni importo pari'
            correct: false
          - text: 'Usare `if (importo / 2 == 0) continue;`'
            correct: false
      - question: 'Quale modifica fa terminare il ciclo quando trova un valore maggiore di 10000?'
        options:
          - text: 'Inserire `if (importo > 10000) break;` prima dell’elaborazione dell’importo'
            correct: true
          - text: 'Inserire `if (importo > 10000) continue;` se vuoi fermare il ciclo'
            correct: false
          - text: 'Cambiare il contatore in `importo > 10000`'
            correct: false
      - question: 'Per contare solo i movimenti effettivamente elaborati, dove conviene incrementare `validi`?'
        options:
          - text: 'Dopo i controlli `continue` e `break`, nel punto in cui il movimento viene elaborato'
            correct: true
          - text: 'Prima di `continue`, così anche gli importi scartati vengono contati'
            correct: false
          - text: 'Dopo il ciclo, una sola volta, perché il contatore si aggiorna da solo'
            correct: false
      - question: 'Perché conviene provare una modifica alla volta?'
        options:
          - text: 'Per capire se il cambiamento ha alterato il salto, l’uscita o il conteggio previsto'
            correct: true
          - text: 'Perché in un ciclo può esistere una sola istruzione `if`'
            correct: false
          - text: 'Perché `continue` e `break` funzionano solo nel primo tentativo'
            correct: false
  make_instructions: >
    Scrivi un programma che analizzi cinque movimenti di cassa: ignora gli
    importi pari a zero con `continue`, interrompi l'analisi con `break` quando
    trovi un importo superiore a 10000 euro e conta i movimenti validi elaborati.
  visualization:
    kind: pythontutor
    note: Osservare il passaggio al giro successivo dopo continue e l’uscita definitiva dopo break.
registro:
  argomenti: >
    Cicli controllati con `break` e `continue`; differenza tra saltare il giro
    corrente e uscire dal ciclo; tracciamento di un controllo scarti in uno
    scenario aziendale.
  note: >
    Verifica formativa PRIMM: prevedere il flusso, motivare l’ordine delle
    istruzioni, modificare una regola e realizzare un controllo movimenti.
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: >
      Distinguere l’effetto di `continue` da quello di `break` e prevedere
      quali iterazioni raggiungono la stampa.
  investigate:
    points: 2
    questions:
      - Quali istruzioni vengono eseguite quando il contatore vale 2?
      - Perché il valore 5 non viene controllato dopo `break`?
      - Che cosa succede al contatore dopo `continue` in un `for`?
    typical_errors:
      - Interpreta `continue` come uscita definitiva dal ciclo.
      - Dimentica l’aggiornamento del contatore del `for`.
    context: >
      Ricostruire il flusso distinguendo salto del giro e uscita definitiva.
  modify:
    points: 1
    prompt: >
      Modifica il listato affinché il controllo termini al valore 3 invece
      che al valore 4, senza cambiare la condizione che salta il valore 2.
    code: |
      #include <iostream>

      int main() {
          for (int i = 1; i <= 5; ++i) {
              if (i == 2) continue;
              if (i == 4) break;
              std::cout << i;
          }
          return 0;
      }
    typical_errors:
      - Cambia la condizione del `continue` invece di quella del `break`.
      - Inserisce `continue` al posto di `break` e lascia proseguire il ciclo.
    context: >
      Va cambiato solo il valore confrontato dalla condizione che interrompe
      il ciclo.
  make:
    points: 1
    prompt: >
      Analizza i movimenti `100.0, 0.0, 250.0, 12000.0, 80.0`: salta gli
      zeri, interrompi oltre 10000 e stampa quanti movimenti validi hai
      elaborato prima dello stop.
    must_include:
      - Un ciclo su cinque movimenti.
      - '`continue` per gli importi uguali a zero.'
      - '`break` per gli importi superiori a 10000.'
      - Un contatore dei movimenti validi.
    typical_errors:
      - Conta anche l’importo zero.
      - Continua dopo l’outlier invece di interrompere il controllo.
    context: >
      Verificare che ogni comando di uscita anticipata corrisponda alla regola
      di business richiesta.
    code: ''
  variants:
    B:
      modify:
        prompt: >
          Modifica il listato affinché il controllo termini al valore 5 invece
          che al valore 4, senza cambiare la condizione che salta il valore 2.
        code: |
          #include <iostream>

          int main() {
              for (int i = 1; i <= 5; ++i) {
                  if (i == 2) continue;
                  if (i == 4) break;
                  std::cout << i;
              }
              return 0;
          }
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Uscite anticipate nei cicli

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Cambia una sola regola alla volta e ricompila dopo ogni modifica.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    description: Risposte alle previsioni sul flusso di break e continue
    template_content: |
      # Predict – Uscite anticipate

      Rispondi prima di compilare o eseguire il programma.

      1. Quale valore viene saltato da `continue`?
      >

      2. Quando termina il ciclo?
      >

      3. Quale output prevedi?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    description: Confronto tra previsione e output osservato
    template_content: |
      # Run – Controllo scarti

      Digita a mano il programma, compilalo ed eseguilo.

      1. Quale output hai ottenuto?
      >

      2. L'output corrisponde alla previsione? Se no, quale passaggio avevi interpretato diversamente?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    description: Traccia del flusso del ciclo con Python Tutor
    template_content: |
      # Investigate – Flusso del ciclo

      Usa il debugger oppure [Python Tutor C++](https://pythontutor.com/cpp.html).

      1. Quali istruzioni vengono eseguite quando il contatore vale 2?
      >

      2. Perché il valore 5 non viene controllato dopo `break`?
      >

      3. Che cosa succede al contatore dopo `continue` in un `for`?
      >
  - path: student_work/modify/controllo_modificato.cpp
    action: create
    phase: modify
    description: Modifiche progressive alle condizioni di salto e di uscita
    template_content: |
      #include <iostream>

      int main() {
          for (int i = 1; i <= 5; ++i) {
              if (i == 2) continue;
              if (i == 4) break;
              std::cout << i;
          }
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain:
        - break
        - continue
  - path: student_work/make/analizza_movimenti.cpp
    action: create
    phase: make
    description: Analisi di movimenti con continue e break
    template_content: |
      #include <iostream>

      int main() {
          double movimenti[] = {100.0, 0.0, 250.0, 12000.0, 80.0};
          int validi = 0;
          // TODO: ciclo, continue sugli zeri, break sull'outlier
          std::cout << "Movimenti validi: " << validi << "\n";
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain:
        - break
        - continue
---

## ⏹️ Uscite Anticipate: `break` e `continue` nei cicli

> "La semplicità è la massima raffinatezza."
>
> — *Leonardo da Vinci*

In un controllo aziendale non tutti i dati meritano lo stesso trattamento:
un movimento vuoto può essere ignorato, mentre un importo anomalo può rendere
inutile continuare. In C++ puoi esprimere queste due decisioni dentro un ciclo.

> 💡 **Metafora:**  
> Immagina un nastro che trasporta fatture. `continue` è il pulsante
> **“salta questa fattura”**: il nastro riparte con la successiva. `break` è
> il pulsante **“ferma il nastro”**: il controllo del lotto termina subito.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- usare `continue` per saltare un’iterazione e `break` per terminare un ciclo in base a una regola aziendale.

---

### ⚙️ Prima del laboratorio: due uscite diverse

| Istruzione | Effetto nel ciclo | Regola tipica |
| :--- | :--- | :--- |
| `continue` | salta il resto del giro corrente e passa al prossimo | ignora un dato vuoto o non interessante |
| `break` | esce subito dal ciclo più interno | ferma l’analisi davanti a un dato anomalo |

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

Nel `for`, dopo `continue` viene comunque eseguito l’aggiornamento `++i`.
Dopo `break`, invece, il ciclo è terminato: non esiste un giro successivo.

---

### 🧭 Prima del laboratorio: leggere il flusso

Per ogni valore di `i`, il programma legge le condizioni dall’alto verso il
basso:

1. se `i == 2`, salta la stampa e passa al prossimo giro;
2. altrimenti, se `i == 4`, esce dal ciclo;
3. altrimenti, stampa `i`.

Il punto importante è **dove** si trova l’istruzione: un `continue` prima
della stampa impedisce a quella stampa di essere raggiunta.

---

### 🔬 Laboratorio PRIMM: Controllo scarti

Il ciclo simula una prima scansione di dati: alcuni valori vengono saltati,
un valore anomalo chiude il controllo.

#### 1. PREDICT (Prevedi)

Prima di eseguire il codice, scegli le risposte e spiega a parole la
differenza tra saltare un giro e terminare il ciclo:

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma, eseguilo e confronta l’output con la tua previsione.

```cpp
/**
 * @file controllo_scarti.cpp
 * @brief Mostra come saltare un giro e terminare un controllo.
 * @return int Codice di uscita del programma.
 */
#include <iostream>

int main() {
    for (int i = 1; i <= 5; ++i) {
        if (i == 2) {
            continue;
        }
        if (i == 4) {
            break;
        }
        std::cout << i;
    }
    std::cout << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

Dopo il Run, ricostruisci il percorso di ogni iterazione:

[[ investigate_block() ]]

| Valore di `i` | Istruzione decisiva | Effetto | Output |
| :---: | :--- | :--- | :--- |
| 1 | nessuna condizione vera | raggiunge la stampa | `1` |
| 2 | `continue` | salta la stampa e passa a `++i` | `1` |
| 3 | nessuna condizione vera | raggiunge la stampa | `13` |
| 4 | `break` | esce subito dal ciclo | `13` |
| 5 | nessun giro | il ciclo è già terminato | `13` |

Apri il programma in [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva che dopo `continue` il contatore del `for` avanza, mentre dopo
`break` il flusso va direttamente alla riga dopo il ciclo.

#### 4. MODIFY (Modifica)

Prima di modificare il listato, prevedi l’effetto di ogni cambiamento:

[[ modify_block() ]]

Parti da questo scaffold:

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    for (int i = 1; i <= 5; ++i) {
        if (i == 2) continue;
        if (i == 4) break;
        std::cout << i;
    }
    return 0;
}
```

</details>

**Modifica A — cambia il punto di stop**  
Cambia solo la condizione di `break` per terminare quando `i` vale `3`.

**Modifica B — conta i dati elaborati**  
Aggiungi `int elaborati = 0;`. Incrementalo solo dopo i due controlli,
nel punto in cui il valore viene davvero elaborato e stampato.

**Modifica C — ciclo sui movimenti**  
Usa una sequenza di importi e sostituisci le condizioni su `i` con:
`continue` per `importo == 0` e `break` per `importo > 10000`.

---

### 5. MAKE (Crea)

**Scenario aziendale — Analisi movimenti di cassa**

Scrivi `analizza_movimenti.cpp` con i seguenti requisiti chiusi:

1. Usa la sequenza `100.0, 0.0, 250.0, 12000.0, 80.0`.
2. Scorri i cinque importi con un ciclo.
3. Se l’importo vale `0.0`, usa `continue`: non stamparlo e non contarlo.
4. Se l’importo è maggiore di `10000.0`, usa `break`: interrompi l’analisi
   prima di elaborare quel movimento e quelli successivi.
5. Conta e stampa quanti movimenti validi sono stati elaborati prima dello stop.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double movimenti[] = {100.0, 0.0, 250.0, 12000.0, 80.0};
    int validi = 0;

    /// Gli zeri non rappresentano movimenti da registrare.
    // TODO: ciclo sui cinque elementi
    // TODO: continue per gli zeri
    // TODO: break per l'outlier
    // TODO: conta e stampa i movimenti validi

    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `continue` salta il resto dell’iterazione corrente.
- `break` termina subito il ciclo più interno.
- In un `for`, `continue` porta comunque all’aggiornamento del contatore.
- La posizione del comando rispetto alla stampa cambia il flusso osservato.
- Usa i due comandi per regole di business chiare, non per nascondere codice confuso.

---

### ➡️ Prossimo chunk

Ora sai controllare il flusso dentro un ciclo. Nel prossimo chunk sposterai
un’elaborazione in una **funzione**, un reparto specializzato che puoi
richiamare quando serve.

<!--#
  Checklist autore / LLM (golden sample = chapters/03_ciao_mondo.md)
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra concetto e scenario
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, con perché / tracing / errore
  [x] modify_quiz.items ~5, sull'effetto delle modifiche
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Commenti /// solo sul perché
  [x] Investigate con tabella e link a Python Tutor
  [x] Make con scenario SIA, requisiti chiusi e scaffold in <details>
  [x] registro e assessment coerenti con il capitolo
  [x] activity_id e order conservati
  [ ] validate OK
#-->
