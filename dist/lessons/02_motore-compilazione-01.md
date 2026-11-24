<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-20
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/01_ambiente-sviluppo-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/03_ciao-mondo-01.md)

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

```cpp
g++ -save-temps -O0 ridotto.cpp -o ridotto.exe
```

**Domanda 1**

Quale risultato principale vuoi ottenere con questo comando?

[( )] Un file `.cpp` con il programma scritto automaticamente
[( )] Solo una stampa a video, senza creare file
[(X)] Un eseguibile `ridotto.exe` pronto da avviare

**Domanda 2**

Perché `-save-temps` è utile mentre studi la compilazione?

[( )] Rende il programma più veloce durante l'esecuzione
[( )] Salva automaticamente una copia del programma su Internet
[(X)] Chiede a `g++` di conservare i file temporanei intermedi

**Domanda 3**

Dopo la pre-elaborazione, quale file contiene ancora codice testuale vicino al C++?

[( )] Il file `.o`, già composto solo da testo Assembly
[( )] Il file `.exe`, che contiene il sorgente originale leggibile
[(X)] Il file `.ii`, con direttive espanse e commenti rimossi

**Domanda 4**

Quale sequenza descrive meglio il percorso verso l'eseguibile?

[(X)] `.cpp` → `.ii` → `.s` → `.o` → `.exe`
[( )] `.cpp` → `.exe` → `.ii` → `.o` → `.s`
[( )] `.cpp` → `.o` → `.ii` → `.exe` → `.s`

**Domanda 5**

Perché il linker deve intervenire anche dopo la traduzione del tuo file?

[( )] Per correggere i punti e virgola dimenticati nel C++
[( )] Per trasformare l'eseguibile di nuovo nel file sorgente
[(X)] Per collegare il codice oggetto con librerie e codice di avvio

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

```cpp
int main() {
    return 0;
}
```

**Domanda 1**

Perché `ridotto.o` non è ancora l'eseguibile finale?

[(X)] È codice oggetto: può avere ancora collegamenti da risolvere con librerie e avvio
[( )] È soltanto una copia del file `.cpp` con un'altra estensione
[( )] È già l'eseguibile, ma Windows gli nasconde l'estensione

**Domanda 2**

Quale trasformazione avviene quando il compilatore produce il file `.s`?

[(X)] Il C++ viene tradotto in Assembly, un linguaggio a basso livello ancora leggibile
[( )] I file `.cpp` vengono compressi in un archivio di testo
[( )] Il programma viene eseguito e il risultato viene salvato in `.s`

**Domanda 3**

Quale ordine di osservazione è coerente con la catena di compilazione?

[( )] `.ii` e `.exe` vengono creati soltanto dopo l'esecuzione
[(X)] Prima `.ii`, poi `.s`, poi `.o`, infine `.exe`
[( )] Prima `.exe`, poi `.o`, poi `.s`, infine `.ii`

**Domanda 4**

Nel file Assembly, perché puoi trovare un'istruzione che prepara il valore `0`?

[(X)] Perché `return 0;` deve consegnare al sistema operativo un codice di uscita
[( )] Perché ogni programma deve stampare almeno uno zero
[( )] Perché `-save-temps` sostituisce ogni istruzione con il numero zero

**Domanda 5**

Se il compilatore segnala un errore di sintassi nel `.cpp`, perché la catena non arriva al linker?

[( )] Il linker lavora solo sui commenti e quindi ignora il programma
[(X)] Senza una traduzione valida non esiste un file oggetto affidabile da collegare
[( )] Il linker viene eseguito prima del compilatore e non può ripartire

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

```cpp
int main() {
    return 0;
}
```

**Domanda 1**

Se cambi `return 0;` in `return 7;`, quale effetto vuoi verificare?

[( )] Il compilatore salta la fase di assemblaggio
[( )] Il programma stampa automaticamente il numero `7`
[(X)] Il codice di uscita del programma cambia da `0` a `7`

**Domanda 2**

Quale modifica permette di ottenere il file finale con il nome `importazione.exe`?

[(X)] Sostituire il nome dopo `-o` con `importazione.exe`
[( )] Scrivere `importazione.exe` dentro `return`
[( )] Cambiare l'estensione di `ridotto.cpp` in `.exe` prima di compilare

**Domanda 3**

Se togli `-save-temps`, quale cambiamento è più probabile?

[( )] Il programma viene trasformato direttamente in Assembly e non in `.exe`
[( )] Il C++ non può più essere compilato
[(X)] Ottieni comunque l'eseguibile, ma i file intermedi possono essere rimossi

**Domanda 4**

Quale modifica rende l'Assembly più facile da collegare al sorgente durante l'ispezione?

[(X)] Aggiungere `-fverbose-asm` al comando
[( )] Sostituire `-O0` con `return 0`
[( )] Rinominare il file `.o` in `.cpp` dopo la compilazione

**Domanda 5**

Perché conviene modificare una sola cosa alla volta nel comando o nel codice?

[( )] Perché `g++` accetta una sola modifica per ogni esecuzione
[(X)] Per collegare con chiarezza ogni effetto alla modifica che lo ha causato
[( )] Perché i file intermedi non possono contenere più di una riga cambiata

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

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/01_ambiente-sviluppo-01.md">Lezione precedente (1 — Prepara la tua Officina di Sviluppo: VS Code, MSYS2 e MinGW-w64)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/03_ciao-mondo-01.md">Lezione successiva (3 — Il Primo Dialogo con la Macchina: std::cout e il programma minimo)</a>
