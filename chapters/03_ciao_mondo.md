---
activity_id: ciao-mondo-01
title: 'Il Primo Dialogo con la Macchina: std::cout e il programma minimo'
methodology: PRIMM
order: 3
components:
  predict_quiz:
    code: 'std::cout << "Ciao, Mondo!\n";

      '
    items:
    - question: Cosa fa questa istruzione?
      options:
      - text: Stampa Ciao, Mondo! e va a capo
        correct: true
      - text: Legge da tastiera la stringa Ciao, Mondo!
        correct: false
      - text: Compila e avvia il programma
        correct: false
    - question: Il frammento, così com'è, è un programma C++ completo e sintatticamente
        corretto?
      options:
      - text: 'No: manca almeno la struttura di un programma (include, main, …)'
        correct: true
      - text: 'Sì: una sola istruzione basta se il file si chiama main.cpp'
        correct: false
      - text: Sì, purché si usi un IDE come Visual Studio Code
        correct: false
    - question: Per ottenere un eseguibile da compilare, serve altro codice oltre
        a questa riga?
      options:
      - text: 'Sì: servono almeno #include <iostream>, int main() e in genere return'
        correct: true
      - text: 'No: il compilatore aggiunge da solo main e le librerie'
        correct: false
      - text: Solo se si compila con g++; con clang non serve altro
        correct: false
  make_instructions: 'presentazione.cpp: tre std::cout per una schermata di benvenuto
    di un gestionale, commento /// sul perché, return 0

    '
  visualization:
    kind: pythontutor
    note: Osservare il flusso fino a return 0.
registro:
  argomenti: 'Programma C++ minimo; direttiva #include <iostream>; std::cout e sequenza
    di escape \n; funzione main e return 0; introduzione al namespace std. Laboratorio
    PRIMM sul programma Ciao Mondo.

    '
  note: 'Verifica scritta in classe (Predict, Investigate, Modify, Make). Compito
    digitale correlato su repository Classroom50.

    '
assessment:
  duration_min: 10
  total_points: 6
  versions:
  - A
  - B
  predict:
    points: 3
    context: 1) std::cout stampa e \n va a capo. 2) Una sola istruzione non è un programma
      completo. 3) Servono include, main (e di regola return) per compilare un eseguibile.
  investigate:
    points: 1
    questions:
    - 'A che serve #include <iostream> nel programma completo?'
    - Perché senza la funzione main il programma non parte?
    typical_errors:
    - Descrive include come se venisse eseguita a runtime
    - Ommette che main è il punto di ingresso obbligatorio
    context: iostream dichiara gli stream; main è il punto di ingresso richiesto dal
      runtime.
  modify:
    points: 1
    prompt: Nel listato sotto, aggiungi una seconda riga di output con la tua classe.
      Non cancellare la riga "Ciao, Mondo!".
    code: "#include <iostream>\n\nint main() {\n    std::cout << \"Ciao, Mondo!\\\
      n\";\n\n    // scrivi qui la nuova riga di output\n\n\n    return 0;\n}\n"
    typical_errors:
    - Rimuove la riga esistente invece di aggiungerne una
    context: Si aggiunge una seconda istruzione std::cout nelle righe libere, senza
      togliere la prima.
  make:
    points: 1
    prompt: In non più di cinque righe utili, completa mentalmente (poi scrivi) cosa
      manca al frammento std::cout per diventare un programma minimo compilabile.
      Elenca solo i pezzi obbligatori (include, main, return), senza scrivere un saggio.
    typical_errors:
    - Dimentica return 0 o include
    context: 'Obbligatori: #include <iostream>, int main(), return 0; il cout sta
      nel corpo di main.'
    must_include: []
    code: ''
  variants:
    B:
      modify:
        prompt: Nel listato sotto, aggiungi una seconda riga di output con il nome
          della scuola. Non cancellare la riga "Ciao, Mondo!".
        code: "#include <iostream>\n\nint main() {\n    std::cout << \"Ciao, Mondo!\\\
          n\";\n\n    // scrivi qui la nuova riga di output\n\n\n    return 0;\n}\n"
      make:
        prompt: Elenca in tre bullet i pezzi minimi che mancano a una sola istruzione
          std::cout per avere un programma C++ compilabile.
files:
- path: README.md
  action: create
  description: Istruzioni per svolgere gli esercizi del capitolo
  template_content: "# Istruzioni – Ciao Mondo\n\nLavora **in ordine** (PRIMM). Ogni\
    \ fase ha un file dedicato.\n\n1. **Predict** → `student_work/predict/answers.md`\n\
    \   (prima di eseguire qualsiasi codice)\n\n2. **Run** → digita a mano il programma\
    \ del capitolo,\n   poi rifletti in `student_work/run/answers.md`\n\n3. **Investigate**\
    \ → debugger o Python Tutor,\n   poi `student_work/investigate/answers.md`\n\n\
    4. **Modify** → `student_work/modify/ciao_modificato.cpp`\n   (modifiche A, B,\
    \ C una alla volta)\n\n5. **Make** → `student_work/make/presentazione.cpp`\n \
    \  (schermata di benvenuto del gestionale)\n"
- path: student_work/predict/answers.md
  action: create
  phase: predict
  template_content: '# Predict – Ciao Mondo


    Rispondi **prima** di compilare o eseguire.


    Osserva il frammento:

    ```cpp

    std::cout << "Ciao, Mondo!\n";

    ```


    1. Cosa fa questa istruzione? Cosa ti aspetti a video?

    >


    2. Da dove inizia l''esecuzione di un programma C++?

    >


    3. In questo programma, quante volte viene eseguita ogni riga?

    >


    4. In quale ordine vengono eseguite le istruzioni?

    >


    5. C''è un output a video? Se sì, quale esattamente (includi eventuali andate
    a capo)?

    >

    '
- path: student_work/run/answers.md
  action: create
  phase: run
  template_content: '# Run – Ciao Mondo


    Digita a mano il programma del capitolo, compilalo ed eseguilo.

    Poi rispondi.


    1. Il programma compilava al primo tentativo o hai dovuto correggere qualcosa?

    >


    2. Quale output hai ottenuto?

    >


    3. L''output corrisponde a quello che avevi previsto in Predict? Se no, cosa era
    diverso?

    >

    '
- path: student_work/investigate/answers.md
  action: create
  phase: investigate
  template_content: '# Investigate – Ciao Mondo


    Prima di rispondere: esegui il programma col debugger oppure copialo su

    [Python Tutor C++](https://pythontutor.com/cpp.html).


    1. A che serve `#include <iostream>`?

    >


    2. Qual è il ruolo della funzione `main`? Cosa succede se manca?

    >


    3. Cosa significa `std::` davanti a `cout`? Perché non scriviamo solo `cout`?

    >


    4. A che serve `\n` alla fine della stringa?

    >


    5. A che serve `return 0;`?

    >

    '
- path: student_work/modify/ciao_modificato.cpp
  action: create
  phase: modify
  description: 'Parti da questo file. Applica le modifiche A, B e C descritte nel
    capitolo (una alla volta, ricompilando ogni volta).

    '
  template_content: "#include <iostream>\n\nint main() {\n    std::cout << \"Ciao,\
    \ Mondo!\\n\";\n    return 0;\n}\n"
  validation_rules:
    min_lines: 6
    must_contain:
    - std::cout
- path: student_work/make/presentazione.cpp
  action: create
  phase: make
  description: 'Programma da zero: tre righe per la schermata di benvenuto di un gestionale,
    commento /// sul perché, return 0.

    '
  template_content: "#include <iostream>\n\nint main() {\n    /// TODO: spiega perché\
    \ la prima riga aiuta chi usa il gestionale.\n    // TODO: tre std::cout per il\
    \ messaggio di benvenuto\n    return 0;\n}\n"
  validation_rules:
    min_lines: 8
    must_contain:
    - std::cout
    - return 0
---
## 💬 Il Primo Dialogo con la Macchina: `std::cout` e il programma minimo

> "L'unico modo per imparare un nuovo linguaggio di programmazione è scrivere programmi in quel linguaggio."
>
> -- *Brian Kernighan*

Un linguaggio di programmazione è come un linguaggio straniero con una grammatica rigidissima. Il computer non indovina: esegue **esattamente** quello che gli scrivi.

> 💡 **Metafora:** Scrivere codice è come scrivere una ricetta di cucina.  
>
> - Il **computer** è lo chef che la esegue alla lettera. Se dimentichi “aggiungi un pizzico di sale”, lui non lo indovina: si blocca o produce un risultato sbagliato.  
> - L’**essere umano** (tu tra sei mesi, un collega, il docente) è l’altro lettore: deve poter capire, modificare e mantenere la ricetta. Per questo usiamo commenti e codice ordinato.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- Scrivere, compilare ed eseguire un programma C++ minimo che stampa testo a video con `std::cout`

---

### ⚙️ Prima del laboratorio: le quattro parti essenziali

Un programma C++ minimo non è una frase isolata: è un messaggio con indirizzo,
inizio e fine. Leggilo per blocchi, senza cercare di memorizzare tutto subito.

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| `#include <iostream>` | Prendi in prestito gli strumenti per parlare con lo schermo. | Senza questa libreria il compilatore non conosce `std::cout`. |
| `int main() { ... }` | Il punto d'ingresso del programma. | L'esecuzione parte sempre da qui. |
| `std::cout << "..."` | Invia un messaggio al monitor. | `std::` indica che usi uno strumento della libreria standard. |
| `return 0;` | Comunica che il lavoro è terminato bene. | Il sistema operativo riceve un esito di successo. |

Non serve ancora capire ogni dettaglio di `std::`: per ora ricordati di copiarlo
sempre insieme a `cout`.

---

### 🧭 Prima del laboratorio: come scorre l'esecuzione

Immagina l'avvio di un piccolo gestionale: il sistema apre `main`, esegue le
istruzioni dall'alto verso il basso, mostra il messaggio e poi chiude il lavoro.

| Ordine | Cosa avviene |
| :---: | :--- |
| 1 | Il sistema operativo entra in `main`. |
| 2 | `std::cout` invia i caratteri tra virgolette allo schermo. |
| 3 | `\n` sposta il cursore alla riga successiva. |
| 4 | `return 0;` conclude il programma senza errori. |

Adesso puoi fare una previsione: se cambia il testo tra virgolette, quale parte
del risultato cambierà a video?

---

### 🔬 Laboratorio PRIMM: Il Programma “Ciao, Mondo!”

```cpp
#include <iostream>

int main() {
    std::cout << "Ciao, Mondo!\n";

    return 0;
}
```

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il codice sotto nel tuo editor oppure eseguilo con il bottone.
Confronta l'output con la previsione: la differenza, se c'è, ti dice cosa investigare.

```cpp
/**
 * @file ciao_mondo.cpp
 * @brief Il primo programma in C++ che stampa un messaggio a video.
 */
#include <iostream>

/**
 * @brief Punto di ingresso del programma.
 * @return int 0 se tutto è andato bene.
 */
int main() {
    /// Il saluto rende riconoscibile l'avvio del programma.
    std::cout << "Ciao, Mondo!\n";

    return 0; /// 0 = successo per il sistema operativo
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

Analizziamo il codice riga per riga come detective.

| Fase | Cosa osservi a video |
| :--- | :--- |
| Il sistema operativo avvia `main` | Ancora niente: il programma è pronto a eseguire. |
| `std::cout` invia la stringa | Compare `Ciao, Mondo!` e `\n` porta il cursore alla riga successiva. |
| `return 0;` termina `main` | Nessun nuovo testo: il sistema riceve il segnale di successo. |

| Codice | Cosa fa (spiegazione brain-friendly) | A cosa serve |
| :--- | :--- | :--- |
| `#include <iostream>` | Il pre-elaboratore “incolla” qui le istruzioni necessarie per l’input/output. Senza di essa il compilatore non conosce `cout`. | È il passaporto per parlare con lo schermo (e con la tastiera). |
| `int main() { ... }` | Punto di partenza obbligatorio. Ogni programma C++ ha **esattamente una** funzione `main`. L’esecuzione inizia sempre da qui. | Senza `main` non c’è programma. |
| `std::cout << ...` | `cout` (si legge “si-out”) è il megafono del programma. `std::` è lo **spazio dei nomi**: dice “cerca `cout` nella libreria standard”. | Ti permette di scrivere testo a video. |
| `"Ciao, Mondo!\n"` | Una **stringa letterale**. `\n` è un carattere speciale che forza l’andata a capo. | Controlla esattamente cosa e come viene stampato. |
| `return 0;` | Dice al sistema operativo: “Ho finito e tutto è andato bene”. | Convenzione universale di successo. |

> 🔗 **Ispezione memoria (opzionale ma utile):**  
> Copia il codice su [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva come viene eseguita riga per riga.

#### 4. MODIFY (Modifica)

Apporta queste modifiche **una alla volta** e osserva cosa succede.  
Dopo ogni modifica ricompila/esegui.

<details>
<summary>💡 Scaffold di partenza per tutte le modifiche</summary>

```cpp
#include <iostream>

int main() {
    std::cout << "Ciao, Mondo!\n";
    return 0;
}
```

</details>

**Modifica A — Il punto e virgola traditore**

1. Togli il `;` alla fine della riga di `std::cout`.
2. Compila.

Cosa ti aspetti?

[( )] Funziona comunque
[(X)] Il compilatore segnala un errore di sintassi
[( )] Il programma stampa comunque il messaggio
[( )] Si crea un file eseguibile vuoto

Un compilatore come g++ può segnalare:

```text
error: expected ';' before 'return'
```

<details>
<summary>💡 Spiegazione</summary>
Leggi la parola chiave `expected`: il compilatore si aspettava un punto e virgola
prima di arrivare a `return`. Il testo preciso può cambiare, ma riga e parola
`error` sono il punto da cui iniziare.
</details>

**Modifica B — Lo spazio dei nomi**

1. Ripristina il `;`.
2. Cambia `std::cout` in solo `cout` (togli `std::`).
3. Compila.

Cosa succede?

[( )] Funziona lo stesso
[(X)] Errore: `'cout' was not declared in this scope`
[( )] Il programma stampa uno spazio vuoto
[( )] Stampa “Ciao, Mondo!” due volte

Un compilatore come g++ può segnalare:

```text
error: 'cout' was not declared in this scope; did you mean 'std::cout'?
```

<details>
<summary>💡 Spiegazione</summary>
Senza <code>std::</code> il compilatore cerca <code>cout</code> nel tuo programma
e non lo trova. Il suggerimento finale ti indica anche la correzione: per ora
scrivi sempre <code>std::cout</code> per intero.
</details>

**Modifica C — Più messaggi**
Aggiungi una seconda riga di output: `Gestionale ordini pronto`.
Verifica che appaiano su due righe separate.

#### 5. MAKE (Crea)

Scrivi da zero un nuovo programma chiamato `presentazione.cpp`.

**Scenario aziendale:** la tua classe sta preparando la prima schermata di un
piccolo gestionale ordini. Prima che l'operatore inizi a lavorare, il programma
deve comunicare con chiarezza dove si trova.

**Requisiti:**

1. Includi la libreria corretta.
2. Hai una funzione `main` ben formattata.
3. Stampa **tre righe separate** con tre istruzioni `std::cout`:
   - riga 1 → nome del gestionale;
   - riga 2 → reparto o funzione, per esempio “Gestione ordini”;
   - riga 3 → messaggio utile per l'operatore.
4. Usa un commento `///` per spiegare **perché** una riga aiuta l'operatore.
5. Termina con `return 0;`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    /// Fa capire subito all'operatore quale strumento sta usando.
    std::cout << "....................\n";

    std::cout << "....................\n";

    std::cout << "....................\n";

    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Ogni programma C++ parte da `int main()`.
- `#include <iostream>` è il passaporto per l’input/output.
- `std::cout <<` scrive sullo schermo; `\n` va a capo.
- `std::` indica il namespace della libreria standard; per ora lo scriviamo sempre esplicito (niente `using namespace std;` ancora).
- `return 0;` comunica “successo” al sistema operativo.
- Il codice ha **due lettori**: il compilatore (sintassi) e l’essere umano (chiarezza). I commenti servono al secondo.
- Gli errori di compilazione sono messaggi utili: imparare a leggerli è una competenza fondamentale.

---

### ➡️ Prossimo chunk

Finora il computer ha solo *parlato*.  
Nella prossima lezione gli daremo le **scatole** (le variabili) per ricordare i dati e gli insegneremo ad *ascoltare* (`std::cin`).
