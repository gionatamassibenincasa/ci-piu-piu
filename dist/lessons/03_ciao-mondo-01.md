<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-12
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/02_motore-compilazione-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/04_doxygen-01.md)

---

## 💬 Il Primo Dialogo con la Macchina: `std::cout` e il programma minimo

> "L'unico modo per imparare un nuovo linguaggio di programmazione è scrivere programmi in quel linguaggio."
>
> -- Brian Kernighan

Questa lezione apre il **modulo Fondamenti**: impariamo a far comunicare un programma C++ con chi lo usa, in modo controllato e ripetibile. Il computer non indovina: esegue **esattamente** quello che gli scrivi, con una grammatica rigida.

In laboratorio e in verifica ti chiederemo le stesse cose in forme diverse (codice da prevedere, da modificare, da scrivere; domande sul *perché*). L'obiettivo non è memorizzare una ricetta, ma riconoscere le parti di un programma minimo e usarle con intenzione.

> 💡 **Metafora: messaggio all'operatore**
>
> - Il **programma** è la prima schermata di un piccolo gestionale: deve dire *cosa sta facendo* e *che il sistema è pronto*.
> - Il **computer** esegue le istruzioni nell'ordine scritto; se manca un pezzo obbligatorio, non "completa lui" il messaggio: segnala errore o si ferma.
> - L'**essere umano** (tu tra sei mesi, un collega, il docente) legge lo stesso codice: serve ordine e commenti per poterlo mantenere.

**In questa lezione non** introduciamo ancora variabili, input da tastiera né decisioni. Solo output testuale e struttura minima del programma.

---

### 🎯 Obiettivi di apprendimento

Alla fine di questa lezione sei in grado di:

- scrivere un programma C++ minimo con `#include <iostream>`, `main`, `std::cout` e `return 0;`;
- compilare ed eseguire il programma e riconoscere un messaggio di errore di sintassi frequente (punto e virgola, nome non dichiarato);
- spiegare, a parole tue, il ruolo di ciascuna delle quattro parti del programma minimo.

---

### 📚 Idea chiave

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

Il laboratorio segue il metodo **PRIMM** (Predict → Run → Investigate → Modify → Make).
Le stesse abilità possono ripresentarsi nel compito su GitHub e in una verifica scritta: allenati a *prevedere*, *spiegare* e *modificare*, non solo a far comparire una riga a schermo.

```cpp
#include <iostream>

int main() {
    std::cout << "Ciao, Mondo!\n";

    return 0;
}
```

#### 1. PREDICT (Prevedi)

```cpp
std::cout << "Ciao, Mondo!\n";
```

**Domanda 1**

Cosa fa l’istruzione `std::cout << "Ciao, Mondo!\n";` quando viene eseguita all’interno di un programma completo?

[(X)] Scrive il testo Ciao, Mondo! sullo schermo e va a capo
[( )] Legge da tastiera la stringa Ciao, Mondo!
[( )] Compila il file sorgente in un eseguibile

**Domanda 2**

Perché questo frammento, da solo, non è un programma C++ completo?

[( )] Perché il testo non è in inglese
[( )] Perché non usa la parola chiave `program`
[(X)] Manca il punto di ingresso (`main`) e in genere le dichiarazioni necessarie (es. `#include`)

**Domanda 3**

Cosa fa il carattere speciale `\n` all’interno della stringa?

[(X)] Inserisce un’andata a capo nell’output
[( )] Termina il programma
[( )] Apre una nuova finestra del terminale

**Domanda 4**

Quale affermazione spiega meglio il ruolo di `std::` davanti a `cout`?

[( )] `std::` è obbligatorio solo in Windows
[(X)] `std::` indica il namespace della libreria standard dove si trova `cout`
[( )] `std::` converte il testo in maiuscolo

**Domanda 5**

Se togli le virgolette e scrivi `std::cout << Ciao, Mondo!\n;` (senza `"`), perché il programma non è accettabile?

[( )] Perché `cout` funziona solo con numeri
[(X)] Senza virgolette il compilatore non tratta il testo come stringa letterale
[( )] Perché `\n` non può stare fuori dalle virgolette mai

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

Dopo aver eseguito il programma, rispondi a queste domande (*perché* e *ordine*, non solo “cosa stampa”).

```cpp
#include <iostream>

int main() {
    std::cout << "Ciao, Mondo!\n";
    return 0;
}
```

**Domanda 1**

Perché serve `#include <iostream>` in questo programma?

[( )] Perché stampa da sola “Ciao, Mondo!”
[(X)] Perché dichiara gli strumenti di input/output (come `std::cout`) usati dopo
[( )] Perché avvia automaticamente la funzione `main`

**Domanda 2**

Perché ogni programma eseguibile ha bisogno di una funzione `main`?

[( )] Perché è solo un commento per il programmatore
[(X)] Perché è il punto di ingresso: da lì parte l’esecuzione
[( )] Perché sostituisce il compilatore

**Domanda 3**

Osserva l’ordine di esecuzione. Quale sequenza è corretta?

[( )] Esegue `return 0;` → poi stampa → poi entra in `main`
[( )] Stampa prima ancora di entrare in `main`
[(X)] Entra in `main` → esegue `std::cout` → esegue `return 0;`

**Domanda 4**

Cosa comunica `return 0;` al sistema operativo?

[( )] Che deve riavviare `main` da capo
[(X)] Che il programma è terminato con successo (codice di uscita 0)
[( )] Che deve stampare il numero 0 a video

**Domanda 5**

Se scrivi `cout` senza `std::`, perché compare un errore del tipo `cout was not declared in this scope`?

[(X)] Il nome `cout` non è visibile senza indicare il namespace `std` (o un using)
[( )] Perché `cout` esiste solo in Python
[( )] Perché manca il file `main.cpp`

Poi rivedi le tabelle di traccia qui sotto e confrontale con le tue risposte.


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

Prima di mettere mano al codice, verifica di saper prevedere **l’effetto di una modifica** (stesso spirito del Predict, ma sul cambiamento).

```cpp
#include <iostream>

int main() {
    std::cout << "Ciao, Mondo!\n";
    return 0;
}
```

**Domanda 1**

Cosa succede all’output se cambi solo il testo tra virgolette in `"Gestionale pronto\n"`?

[( )] Viene stampato due volte Ciao, Mondo!
[(X)] A video compare Gestionale pronto (e va a capo); il resto della struttura resta valido
[( )] Il programma non compila più

**Domanda 2**

Se rimuovi `\n` dalla stringa, quale effetto osservi?

[( )] Il programma non parte
[( )] Viene aggiunto automaticamente un secondo messaggio
[(X)] Il testo appare, ma il cursore non va a capo dopo il messaggio

**Domanda 3**

Vuoi una seconda riga di output. Quale modifica è corretta?

[(X)] Aggiungere un’altra istruzione `std::cout << "...\n";` dentro `main`, senza togliere la prima
[( )] Scrivere il secondo messaggio fuori da `main`
[( )] Sostituire `#include` con il secondo messaggio

**Domanda 4**

Se cancelli la riga `return 0;`, in un programma così semplice cosa succede di solito?

[( )] Il programma stampa necessariamente “errore”
[( )] È sempre un errore di compilazione obbligatorio
[(X)] Spesso compila comunque (return implicito da `main` in C++), ma è buona pratica lasciare `return 0;` esplicito

**Domanda 5**

Perché, in Modify, conviene cambiare **una cosa alla volta** e ricompilare?

[( )] Perché il compilatore accetta al massimo una modifica al giorno
[( )] Perché altrimenti `std::cout` smette di funzionare
[(X)] Per isolare causa ed effetto: se qualcosa si rompe, sai quale modifica l’ha provocato

Ora applica **una modifica alla volta** sul programma completo e ricompila.


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

Prima di chiudere, verifica di saper fare (o spiegare) quanto segue:

- [ ] Ogni programma eseguibile parte da `int main()`.
- [ ] `#include <iostream>` abilita l'input/output a console.
- [ ] `std::cout <<` scrive sullo schermo; `\n` va a capo.
- [ ] Scrivo sempre `std::cout` per intero (niente `using namespace std;` in questo modulo).
- [ ] `return 0;` comunica esito di successo al sistema operativo.
- [ ] Il codice ha **due lettori**: compilatore (sintassi) e essere umano (chiarezza); i commenti servono al secondo.
- [ ] Un messaggio di errore di compilazione si legge da riga e parola `error`, non si ignora.

---

### ➡️ Prossimo passo nel percorso

Dopo questa lezione, nel percorso Fondamenti, si lavora sulla **qualità del codice leggibile** (documentazione leggera con Doxygen) e poi sulle **variabili** e sull'input (`std::cin`): il programma non si limita a parlare, ma inizia a ricordare e ad ascoltare dati di lavoro.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/02_motore-compilazione-01.md">Lezione precedente (2 — Il motore sotto il cofano: dalla sorgente all'eseguibile)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/04_doxygen-01.md">Lezione successiva (4 — Parlare al Futuro Te Stesso: documentazione Doxygen)</a>
