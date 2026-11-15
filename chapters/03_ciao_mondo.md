---
activity_id: ciao-mondo-01
title: 'Il Primo Dialogo con la Macchina: std::cout e il programma minimo'
methodology: PRIMM
order: 3
components:
  predict_quiz:
    question: Cosa fa std::cout << "Ciao, Mondo!\n"; ?
    code: |
      std::cout << "Ciao, Mondo!\n";
    options:
      - text: Legge da tastiera
        correct: false
      - text: Stampa Ciao, Mondo! e va a capo
        correct: true
      - text: Compila il programma
        correct: false
  make_instructions: >
    presentazione.cpp: tre std::cout (nome, classe, hobby),
    commenti ///, return 0
files:
  - path: student_work/README.md
    action: create
    description: Istruzioni per svolgere gli esercizi del capitolo
    template_content: |
      # Istruzioni – Ciao Mondo

      Lavora **in ordine** (PRIMM). Ogni fase ha un file dedicato.

      1. **Predict** → `student_work/predict/answers.md`
         (prima di eseguire qualsiasi codice)

      2. **Run** → digita a mano il programma del capitolo,
         poi rifletti in `student_work/run/answers.md`

      3. **Investigate** → debugger o Python Tutor,
         poi `student_work/investigate/answers.md`

      4. **Modify** → `student_work/modify/ciao_modificato.cpp`
         (modifiche A, B, C una alla volta)

      5. **Make** → `student_work/make/presentazione.cpp`
         (nome, classe, hobby)

  - path: student_work/predict/answers.md
    action: create
    phase: predict
    template_content: |
      # Predict – Ciao Mondo

      Rispondi **prima** di compilare o eseguire.

      Osserva il frammento:
      ```cpp
      std::cout << "Ciao, Mondo!\n";
      ```

      1. Cosa fa questa istruzione? Cosa ti aspetti a video?
      >

      2. Da dove inizia l'esecuzione di un programma C++?
      >

      3. In questo programma, quante volte viene eseguita ogni riga?
      >

      4. In quale ordine vengono eseguite le istruzioni?
      >

      5. C'è un output a video? Se sì, quale esattamente (includi eventuali andate a capo)?
      >

  - path: student_work/run/answers.md
    action: create
    phase: run
    template_content: |
      # Run – Ciao Mondo

      Digita a mano il programma del capitolo, compilalo ed eseguilo.
      Poi rispondi.

      1. Il programma compilava al primo tentativo o hai dovuto correggere qualcosa?
      >

      2. Quale output hai ottenuto?
      >

      3. L'output corrisponde a quello che avevi previsto in Predict? Se no, cosa era diverso?
      >

  - path: student_work/investigate/answers.md
    action: create
    phase: investigate
    template_content: |
      # Investigate – Ciao Mondo

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

  - path: student_work/modify/ciao_modificato.cpp
    action: create
    phase: modify
    description: >
      Parti da questo file. Applica le modifiche A, B e C
      descritte nel capitolo (una alla volta, ricompilando ogni volta).
    template_content: |
      #include <iostream>

      int main() {
          std::cout << "Ciao, Mondo!\n";
          return 0;
      }
    validation_rules:
      min_lines: 6
      must_contain:
        - std::cout

  - path: student_work/make/presentazione.cpp
    action: create
    phase: make
    description: >
      Programma da zero: tre righe (nome, classe, hobby),
      commenti ///, return 0.
    template_content: |
      #include <iostream>

      int main() {
          // TODO: tre std::cout (nome, classe, hobby)
          // usa commenti /// sul perché
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain:
        - std::cout
        - return 0
---
## 💬 Il Primo Dialogo con la Macchina: `std::cout` e il programma minimo

> "L'unico modo per imparare un nuovo linguaggio di programmazione è scrivere programmi in quel linguaggio."
>
> — *Brian Kernighan*

Un linguaggio di programmazione è come un linguaggio straniero con una grammatica rigidissima. Il computer non indovina: esegue **esattamente** quello che gli scrivi.

> 💡 **Metafora:** Scrivere codice è come scrivere una ricetta di cucina.  
> - Il **computer** è lo chef che la esegue alla lettera. Se dimentichi “aggiungi un pizzico di sale”, lui non lo indovina: si blocca o produce un risultato sbagliato.  
> - L’**essere umano** (tu tra sei mesi, un collega, il docente) è l’altro lettore: deve poter capire, modificare e mantenere la ricetta. Per questo usiamo commenti e codice ordinato.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere, compilare ed eseguire un programma C++ minimo che stampa testo a video
- Usare correttamente `#include <iostream>`, `std::cout`, `\n` e `return 0`
- Leggere e interpretare i messaggi di errore più comuni legati a sintassi e namespace

---

### 🔬 Laboratorio PRIMM: Il Programma “Ciao, Mondo!”

```cpp[ciao.cpp]
#include <iostream>

int main() {
    std::cout << "Ciao, Mondo!\n";

    return 0;
}
```


#### 1. PREDICT (Prevedi)


[[ predict_block() ]]


#### 2. RUN (Esegui)
Analizza il codice sotto. Creati un modello di esecuzione e predici quello che verrà stampato. Non ti fidare dei commenti, potrebbero essere sbagliati! Eseguilo premendo il bottone.  
Confronta l’output con la tua previsione.

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
    /// Stampa il messaggio di saluto e va a capo
    std::cout << "Ciao, Mondo!\n";

    return 0; /// 0 = successo per il sistema operativo
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Analizziamo il codice riga per riga come detective.

| Codice | Cosa fa (spiegazione brain-friendly) | A cosa serve |
| :--- | :--- | :--- |
| `#include <iostream>` | Il pre-elaboratore “incolla” qui le istruzioni necessarie per l’input/output. Senza di essa il compilatore non conosce `cout`. | È il passaporto per parlare con lo schermo (e con la tastiera). |
| `int main() { ... }` | Punto di partenza obbligatorio. Ogni programma C++ ha **esattamente una** funzione `main`. L’esecuzione inizia sempre da qui. | Senza `main` non c’è programma. |
| `std::cout << ...` | `cout` (si legge “si-out”) è il megafono del programma. `std::` è lo **spazio dei nomi**: dice “cerca `cout` nella libreria standard”. | Ti permette di scrivere testo a video. |
| `"Ciao, Mondo!\n"` | Una **stringa letterale**. `\n` è un carattere speciale che forza l’andata a capo. | Controlla esattamente cosa e come viene stampato. |
| `return 0;` | Dice al sistema operativo: “Ho finito e tutto è andato bene”. | Convenzione universale di successo. |

> 🔗 **Ispezione memoria (opzionale ma utile):**  
> Copia il codice su [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva come viene eseguita riga per riga.

> 💡 **Nota sui namespace (senza usarla ancora)**  
> Un **namespace** è un “reparto” di nomi: evita che due cose diverse si chiamino uguali e si confondano.  
> La libreria standard vive nel reparto `std`. Per questo scriviamo `std::cout` e non solo `cout`.  
> Esiste anche la scorciatoia `using namespace std;` (dopo gli `#include`), che permette di scrivere `cout` da solo.  
> **In questo corso, all’inizio, non la usiamo:** rende gli errori più chiari e ti abitua a vedere da dove arrivano i nomi. La rivedremo quando i programmi saranno più lunghi.

#### 4. MODIFY (Modifica)
Apporta queste modifiche **una alla volta** e osserva cosa succede.  
Dopo ogni modifica ricompila/esegui.

**Modifica A — Il punto e virgola traditore**
1. Togli il `;` alla fine della riga di `std::cout`.
2. Compila.

Cosa ti aspetti?

[( )] Funziona comunque
[(X)] Il compilatore segnala un errore di sintassi
[( )] Il programma stampa comunque il messaggio
[( )] Si crea un file eseguibile vuoto

<details>
<summary>💡 Spiegazione</summary>
Il punto e virgola è obbligatorio in C++ per terminare quasi tutte le istruzioni. Senza di esso il compilatore non sa dove finisce un’istruzione e dove ne inizia un’altra.
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

<details>
<summary>💡 Spiegazione</summary>
Senza <code>std::</code> il compilatore cerca una cosa chiamata <code>cout</code> nel tuo programma e non la trova: non sa che intendevi quella della libreria standard. Per ora scriviamo sempre <code>std::cout</code> per intero.
</details>

**Modifica C — Più messaggi**
Aggiungi una seconda riga di output che stampa il tuo nome o la tua classe.  
Verifica che appaiano su due righe separate.

#### 5. MAKE (Crea)
Scrivi da zero un nuovo programma chiamato `presentazione.cpp`.

**Scenario:** vuoi presentarti al computer (e a chi leggerà il codice).

**Requisiti:**
1. Includi la libreria corretta.
2. Hai una funzione `main` ben formattata.
3. Stampa **tre righe separate** con tre istruzioni `std::cout`:
   - riga 1 → il tuo nome
   - riga 2 → la tua classe (es. “3A SIA”)
   - riga 3 → una tua passione o hobby
4. Usa commenti `///` sul “perché” delle righe importanti.
5. Termina con `return 0;`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Programma di presentazione personale.
 */
#include <iostream>

int main() {
    /// Stampa il nome
    std::cout << "....................\n";

    /// Stampa la classe
    std::cout << "....................\n";

    /// Stampa l'hobby
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
Nel prossimo capitolo gli daremo le **scatole** (le variabili) per ricordare i dati e gli insegneremo ad *ascoltare* (`std::cin`).

