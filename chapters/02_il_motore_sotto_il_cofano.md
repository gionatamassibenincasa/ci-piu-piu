---
activity_id: motore-compilazione-01
title: 'Il motore sotto il cofano: dalla sorgente all''eseguibile'
methodology: PRIMM
order: 2
version: '2026-11-20'
language: it
components:
  predict_quiz:
    code: |
      g++ -save-temps -O0 ridotto.cpp -o ridotto.exe
    items:
      - question: 'Quale risultato principale vuoi ottenere con questo comando?'
        options:
          - text: 'Un eseguibile `ridotto.exe` pronto da avviare'
            correct: true
          - text: 'Un file `.cpp` con il programma scritto automaticamente'
            correct: false
          - text: 'Solo una stampa a video, senza creare file'
            correct: false
      - question: 'Perché `-save-temps` è utile mentre studi la compilazione?'
        options:
          - text: 'Chiede a `g++` di conservare i file temporanei intermedi'
            correct: true
          - text: 'Rende il programma più veloce durante l''esecuzione'
            correct: false
          - text: 'Salva automaticamente una copia del programma su Internet'
            correct: false
      - question: 'Dopo la pre-elaborazione, quale file contiene ancora codice testuale vicino al C++?'
        options:
          - text: 'Il file `.ii`, con direttive espanse e commenti rimossi'
            correct: true
          - text: 'Il file `.o`, già composto solo da testo Assembly'
            correct: false
          - text: 'Il file `.exe`, che contiene il sorgente originale leggibile'
            correct: false
      - question: 'Quale sequenza descrive meglio il percorso verso l''eseguibile?'
        options:
          - text: '`.cpp` → `.ii` → `.s` → `.o` → `.exe`'
            correct: true
          - text: '`.cpp` → `.exe` → `.ii` → `.o` → `.s`'
            correct: false
          - text: '`.cpp` → `.o` → `.ii` → `.exe` → `.s`'
            correct: false
      - question: 'Perché il linker deve intervenire anche dopo la traduzione del tuo file?'
        options:
          - text: 'Per collegare il codice oggetto con librerie e codice di avvio'
            correct: true
          - text: 'Per correggere i punti e virgola dimenticati nel C++'
            correct: false
          - text: 'Per trasformare l''eseguibile di nuovo nel file sorgente'
            correct: false
  investigate_quiz:
    code: |
      int main() {
          return 0;
      }
    items:
      - question: 'Perché `ridotto.o` non è ancora l''eseguibile finale?'
        options:
          - text: 'È codice oggetto: può avere ancora collegamenti da risolvere con librerie e avvio'
            correct: true
          - text: 'È soltanto una copia del file `.cpp` con un''altra estensione'
            correct: false
          - text: 'È già l''eseguibile, ma Windows gli nasconde l''estensione'
            correct: false
      - question: 'Quale trasformazione avviene quando il compilatore produce il file `.s`?'
        options:
          - text: 'Il C++ viene tradotto in Assembly, un linguaggio a basso livello ancora leggibile'
            correct: true
          - text: 'Il programma viene eseguito e il risultato viene salvato in `.s`'
            correct: false
          - text: 'I file `.cpp` vengono compressi in un archivio di testo'
            correct: false
      - question: 'Quale ordine di osservazione è coerente con la catena di compilazione?'
        options:
          - text: 'Prima `.ii`, poi `.s`, poi `.o`, infine `.exe`'
            correct: true
          - text: 'Prima `.exe`, poi `.o`, poi `.s`, infine `.ii`'
            correct: false
          - text: '`.ii` e `.exe` vengono creati soltanto dopo l''esecuzione'
            correct: false
      - question: 'Nel file Assembly, perché puoi trovare un''istruzione che prepara il valore `0`?'
        options:
          - text: 'Perché `return 0;` deve consegnare al sistema operativo un codice di uscita'
            correct: true
          - text: 'Perché ogni programma deve stampare almeno uno zero'
            correct: false
          - text: 'Perché `-save-temps` sostituisce ogni istruzione con il numero zero'
            correct: false
      - question: 'Se il compilatore segnala un errore di sintassi nel `.cpp`, perché la catena non arriva al linker?'
        options:
          - text: 'Senza una traduzione valida non esiste un file oggetto affidabile da collegare'
            correct: true
          - text: 'Il linker lavora solo sui commenti e quindi ignora il programma'
            correct: false
          - text: 'Il linker viene eseguito prima del compilatore e non può ripartire'
            correct: false
  modify_quiz:
    code: |
      int main() {
          return 0;
      }
    items:
      - question: 'Se cambi `return 0;` in `return 7;`, quale effetto vuoi verificare?'
        options:
          - text: 'Il codice di uscita del programma cambia da `0` a `7`'
            correct: true
          - text: 'Il programma stampa automaticamente il numero `7`'
            correct: false
          - text: 'Il compilatore salta la fase di assemblaggio'
            correct: false
      - question: 'Quale modifica permette di ottenere il file finale con il nome `importazione.exe`?'
        options:
          - text: 'Sostituire il nome dopo `-o` con `importazione.exe`'
            correct: true
          - text: 'Cambiare l''estensione di `ridotto.cpp` in `.exe` prima di compilare'
            correct: false
          - text: 'Scrivere `importazione.exe` dentro `return`'
            correct: false
      - question: 'Se togli `-save-temps`, quale cambiamento è più probabile?'
        options:
          - text: 'Ottieni comunque l''eseguibile, ma i file intermedi possono essere rimossi'
            correct: true
          - text: 'Il C++ non può più essere compilato'
            correct: false
          - text: 'Il programma viene trasformato direttamente in Assembly e non in `.exe`'
            correct: false
      - question: 'Quale modifica rende l''Assembly più facile da collegare al sorgente durante l''ispezione?'
        options:
          - text: 'Aggiungere `-fverbose-asm` al comando'
            correct: true
          - text: 'Sostituire `-O0` con `return 0`'
            correct: false
          - text: 'Rinominare il file `.o` in `.cpp` dopo la compilazione'
            correct: false
      - question: 'Perché conviene modificare una sola cosa alla volta nel comando o nel codice?'
        options:
          - text: 'Per collegare con chiarezza ogni effetto alla modifica che lo ha causato'
            correct: true
          - text: 'Perché `g++` accetta una sola modifica per ogni esecuzione'
            correct: false
          - text: 'Perché i file intermedi non possono contenere più di una riga cambiata'
            correct: false
  make_instructions: >
    Crea `codice_uscita.cpp` per un importatore ordini: usa solo `main`, restituisci un
    codice tra 1 e 99 diverso da 0 e 42, documenta con `///` il significato aziendale,
    compila con `-save-temps -O0 -fverbose-asm` e verifica lo stesso codice con
    `echo %ERRORLEVEL%`.
  visualization:
    kind: plantuml
    note: 'Seguire il percorso `.cpp` → `.ii` → `.s` → `.o` → `.exe` e osservare il valore di return.'
registro:
  argomenti: 'Catena di compilazione C++: pre-elaboratore, compilatore, assemblatore e linker; file intermedi `.ii`, `.s`, `.o`; codice di uscita restituito da `main`; uso di `g++ -save-temps`.'
  note: 'Laboratorio PRIMM di ispezione dei file intermedi in uno scenario di importazione ordini.'
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: 'Riconoscere il percorso dei file intermedi e il ruolo di `-save-temps` e del linker.'
  investigate:
    points: 2
    questions:
      - 'Perché il file `.o` non è ancora l''eseguibile finale?'
      - 'Quale trasformazione produce il file `.s`?'
      - 'Perché `return 0;` compare come valore di ritorno nell''Assembly?'
    typical_errors:
      - 'Confondere codice oggetto ed eseguibile'
      - 'Descrivere il linker come una fase che corregge la sintassi C++'
    context: 'Distinguere le fasi della catena e collegare `return` al codice di uscita.'
  modify:
    points: 1
    prompt: 'Modifica `return 0;` in `return 7;`, ricompila e indica quale valore verifichi con `echo %ERRORLEVEL%`.'
    code: |
      int main() {
          return 0;
      }
    typical_errors:
      - 'Aspettarsi che `return 7` stampi il numero a video'
    context: 'Il valore restituito da `main` è un codice per il sistema operativo, non output testuale.'
  make:
    points: 1
    prompt: 'Scrivi un programma per un importatore ordini che restituisca un codice di esito tra 1 e 99, diverso da 0 e 42, e spiega con `///` il significato scelto.'
    must_include:
      - 'return'
      - 'commento ///'
    typical_errors:
      - 'Scegliere 0 o 42 invece di un codice nuovo'
    context: 'Trasferire il significato del codice di uscita a un contesto aziendale.'
  variants:
    B:
      modify:
        prompt: 'Rinomina l''eseguibile in `ordini.exe`, mantieni `-save-temps` e indica quali file intermedi ti aspetti di trovare.'
        code: |
          int main() {
              return 0;
          }
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Il motore sotto il cofano

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Compila i programmi dal terminale e osserva i file intermedi creati da
      `g++ -save-temps`.
  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Catena di compilazione

      Rispondi prima di lanciare `g++`.

      1. Quale percorso seguono i file dal `.cpp` all'eseguibile?
      >

      2. Perché `-save-temps` può essere utile?
      >
  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Catena di compilazione

      1. Quali file ha creato `g++ -save-temps`?
      >

      2. Quale valore mostra `echo %ERRORLEVEL%`?
      >
  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Catena di compilazione

      1. Che differenza c'è tra `.ii`, `.s`, `.o` ed `.exe`?
      >

      2. Perché il valore di `return` può comparire nell'Assembly?
      >
  - path: student_work/modify/ridotto.cpp
    action: create
    phase: modify
    template_content: |
      int main() {
          return 0;
      }
    validation_rules:
      min_lines: 3
      must_contain:
        - return
  - path: student_work/make/codice_uscita.cpp
    action: create
    phase: make
    description: Programma per comunicare l'esito di un'importazione ordini.
    template_content: |
      int main() {
          /// TODO: spiega il significato aziendale del codice scelto.
          return 7;
      }
    validation_rules:
      min_lines: 4
      must_contain:
        - return
        - '///'
---

## ⚙️ Il motore sotto il cofano: dalla sorgente all'eseguibile

> "La programmazione è l'arte di esprimere soluzioni ai problemi in modo che un computer possa eseguirle."
>
> -- Bjarne Stroustrup

Hai appena allestito l'officina con VS Code e `g++`. Ora apri il cofano: quando
premi il pulsante di compilazione, il file che scrivi non diventa subito un
programma. Attraversa più stazioni, proprio come un ordine che passa da
controllo, preparazione e spedizione.

> 💡 **Metafora:** Immagina una catena di montaggio aziendale. Il file `.cpp` è
> il progetto dell'ordine; pre-elaboratore, compilatore, assemblatore e linker
> sono reparti specializzati; il file `.exe` è il prodotto finito pronto per il
> cliente. Se un reparto trova un problema, la catena si ferma e ricevi un
> messaggio d'errore.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- seguire il percorso di un programma C++ dal file `.cpp` all'eseguibile e
  riconoscere il ruolo dei file intermedi creati da `g++ -save-temps`.

---

### ⚙️ Prima del laboratorio: le stazioni essenziali

| Stazione | Che cosa trasforma | File tipico |
| :--- | :--- | :--- |
| Pre-elaboratore | Espande le direttive `#include` e prepara il sorgente | `.ii` |
| Compilatore | Traduce il C++ in Assembly | `.s` |
| Assemblatore | Traduce l'Assembly in codice oggetto | `.o` |
| Linker | Collega codice oggetto, librerie e codice di avvio | `.exe` |

Il comando che useremo è:

```bat
g++ -save-temps -O0 -fverbose-asm ridotto.cpp -o ridotto.exe
```

| Opzione | Effetto pratico |
| :--- | :--- |
| `-save-temps` | Conserva i file intermedi invece di eliminarli |
| `-O0` | Riduce le ottimizzazioni: l'Assembly è più facile da leggere |
| `-fverbose-asm` | Aggiunge indicazioni utili per collegare Assembly e C++ |
| `-o ridotto.exe` | Sceglie il nome dell'eseguibile finale |

---

### 🧭 Prima del laboratorio: il flusso

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
skinparam ArrowColor #000000
top to bottom direction

rectangle "ridotto.cpp\nsorgente" as SRC
rectangle "Pre-elaboratore\nridotto.ii" as PRE
rectangle "Compilatore\nridotto.s" as COMP
rectangle "Assemblatore\nridotto.o" as ASM
rectangle "Linker + librerie\nridotto.exe" as LINK

SRC --> PRE
PRE --> COMP
COMP --> ASM
ASM --> LINK
@enduml
```

Prima dell'esecuzione, prova a prevedere che cosa troverai nella cartella e
perché il file `.o` non può ancora essere avviato da solo.

---

### 🔬 Laboratorio PRIMM: l'ordine notturno

Un importatore di ordini deve comunicare al sistema operativo se il lavoro è
terminato correttamente. Per ora non stampa nulla: osserviamo solo la catena.

```cpp
int main() {
    return 0;
}
```

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma nel tuo editor oppure usa il bottone. Poi esegui il comando
dal terminale nella cartella del file:

```cpp
int main() {
    return 0;
}
```
@LIA.cpp

```bat
g++ -save-temps -O0 -fverbose-asm ridotto.cpp -o ridotto.exe
ridotto.exe
echo %ERRORLEVEL%
```

Con `-save-temps` dovresti trovare almeno:

- `ridotto.ii`
- `ridotto.s`
- `ridotto.o`
- `ridotto.exe`

Confronta il valore mostrato da `echo %ERRORLEVEL%` con la tua previsione.

#### 3. INVESTIGATE (Indaga)

Ora che hai eseguito il comando, rispondi alle domande sul *perché* e
sull'ordine, non soltanto sull'elenco dei file.

[[ investigate_block() ]]

| File | Che cosa contiene | Perché ti serve |
| :--- | :--- | :--- |
| `ridotto.ii` | Sorgente preparato dal pre-elaboratore | Mostra il risultato delle direttive iniziali |
| `ridotto.s` | Istruzioni Assembly testuali | Fa vedere una traduzione a basso livello |
| `ridotto.o` | Codice oggetto binario | È un pezzo compilato, ma non ancora completo |
| `ridotto.exe` | Programma eseguibile | È il prodotto finale della catena |

Apri `ridotto.s` con un editor. Cerca un'istruzione che prepara il valore
`0`: è il collegamento visibile tra `return 0;` e il codice di uscita che hai
letto con `echo %ERRORLEVEL%`.

> 🔗 **Ispezione facoltativa:** puoi incollare il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) per seguire l'ingresso in
> `main` e l'esecuzione di `return`.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

[[ modify_block() ]]

Applica ora le modifiche in ordine e ricompila ogni volta.

**Modifica A — cambia il codice di uscita**

Sostituisci `return 0;` con `return 7;`. Esegui di nuovo il programma e
controlla `echo %ERRORLEVEL%`. Cerca nel file `.s` il nuovo valore.

**Modifica B — cambia il nome del prodotto**

Ricompila con:

```bat
g++ -save-temps -O0 -fverbose-asm ridotto.cpp -o importazione.exe
```

Controlla che l'eseguibile finale si chiami `importazione.exe`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
int main() {
    return 0;
}
```

</details>

#### 5. MAKE (Crea)

**Scenario aziendale:** un programma automatico importa gli ordini notturni.
Un altro programma deve poter leggere un codice numerico per capire l'esito.

Crea `codice_uscita.cpp` rispettando tutti i requisiti:

1. Usa solo `main`; non aggiungere ancora `#include` o `std::cout`.
2. Restituisci un codice tra `1` e `99`, diverso da `0` e `42`.
3. Inserisci un commento `///` che spieghi il significato aziendale del codice.
4. Compila con `-save-temps -O0 -fverbose-asm`.
5. Verifica lo stesso numero con `echo %ERRORLEVEL%`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
int main() {
    /// TODO: spiega l'esito dell'importazione per il sistema che lo riceve.
    return 7;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Il file `.cpp` è il progetto; il `.exe` è il prodotto eseguibile.
- Il percorso osservabile è `.cpp` → `.ii` → `.s` → `.o` → `.exe`.
- Il linker collega il codice oggetto con librerie e codice di avvio.
- `-save-temps` conserva i file intermedi per poterli ispezionare.
- `return N;` comunica un codice di uscita al sistema operativo: non stampa `N`.

---

### ➡️ Prossimo chunk

Il programma sa già comunicare un esito al sistema, ma non parla ancora con la
persona che lo usa. Nel prossimo capitolo gli daremo un megafono: `std::cout`.

<!--#
  Checklist autore / LLM
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra azienda e compilazione
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, perché / tracing / errori
  [x] modify_quiz.items ~5, effetto della modifica
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Make con scenario SIA, requisiti chiusi e scaffold
  [x] Commenti /// usati solo per il perché
  [x] Nessun costrutto oltre quelli già necessari al capitolo
  [ ] validate da eseguire: python -m tools.cipiupiu validate chapters/02_il_motore_sotto_il_cofano.md
#-->
