<!--
author:   Gionata Massi
email:    gionata.massi@savoiabenicasa.it
version:  2026-11-12
language: it
narrator: IT Italian Male
comment:  Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
          Alcune frasi sono tratte da: Bjarne Stroustrup - Programming Principles and Practice Using C++
import:   https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:   https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->

# 🚀 C++ - AS 2026-27 - 3ze SIA

> "Programmare è capire."
> — *Kristen Nygaard*

Benvenuto nel corso! Questo non è un semplice libro di testo: è un **laboratorio interattivo**.  
Se non vedi le animazioni o i blocchi di codice eseguibili, assicurati di visualizzare questa pagina su LiaScript:

🔗 [Apri il corso su LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/refs/heads/main/README.md)

---


## 🧭 Guida allo Studio: come imparare a programmare

> Il calcolatore era (ed è ancora) un nuovo e meraviglioso concetto filosofico
> e matematico. Il calcolatore è ancora più rivoluzionario come idea che come
> congegno pratico che modifica la società -- e tutti sappiamo quanto abbia
> cambiato la nostra vita.
>
> Perché lo dico? Perché il calcolatore cambia l'epistemologia, modifica il
> significato del verbo «comprendere».
> A mio giudizio, si capisce qualcosa solo se si è capaci -- noi, non altri! --
> di scriverne il programma.
> Altrimenti non si ha una vera comprensione, si crede soltanto di capire.
>
> -- Gregory Chaitin, *Alla ricerca di Omega*, Adelphi Edizioni

Imparare a programmare non significa memorizzare comandi a memoria: significa sviluppare un **metodo di lavoro mentale**.

Questa guida raccoglie due strumenti metodologici complementari pensati per accompagnarti lungo tutto il corso:

1. **La visione d'insieme:** come studiare e assimilare i contenuti di ogni capitolo (metodo di lettura tecnica).
2. **Il lavoro pratico:** come affrontare ogni singolo programma ed esercizio di codice (metodo PRIMM).

---

### 🎯 Obiettivo

Alla fine della guida sai pianificare lo studio di un capitolo e affrontare un
programma seguendo il ciclo PRIMM.

---

### 📖 Consigli per ottenere il massimo da un testo tecnico

> 💡 *Traduzione e adattamento per la classe del saggio di Sebastian Raschka: [How to Read Technical Books](https://sebastianraschka.com/blog/2025/reading-books.html).*

Ti suggeriamo vivamente di affrontare il materiale **in ordine**, poiché ogni capitolo costruisce sulle basi di quello precedente. Per ogni capitolo, ti raccomandiamo di seguire questi 5 passaggi:

#### 1. Prima lettura (offline e panoramica)

- Leggi il capitolo dall'inizio alla fine **senza ancora scrivere codice**. L'obiettivo è ottenere una visione d'insieme del quadro generale.
- Se possibile, leggi lontano dalle distrazioni del computer (una copia stampata o uno schermo senza notifiche, browser o social).
- Mantieni questa sessione breve e mirata (circa **20 minuti**): non bloccarti sui dettagli e non fare ricerche esterne adesso. Annota o evidenzia semplicemente i punti che ti incuriosiscono o ti sembrano confusi.

#### 2. Seconda lettura (con il codice tra le mani)

- Rileggi il capitolo, ma questa volta **digita ed esegui il codice**.
- **Regola d'oro:** riscrivere il codice a mano richiede più tempo rispetto al fare copia-incolla, ma costringe la mente a riflettere su ogni singola istruzione, sintassi e punteggiatura.
- Se ottieni un risultato inatteso o un errore del compilatore, cerca di capirne il motivo. Se dopo averci riflettuto non trovi la causa, confrontati con i compagni o chiedi al docente.

#### 3. Esercizi (mettersi alla prova)

- Dopo aver digitato e compreso il codice base, affronta gli esercizi proposti.
- Gli esercizi servono a consolidare la comprensione in modo guidato.
- Se un esercizio ti sembra troppo difficile, consulta i suggerimenti o la soluzione, ma **solo dopo aver fatto un tentativo serio**.

#### 4. Revisione delle note e approfondimenti

- Torna alle parti che avevi annotato o evidenziato durante le prime due letture: ci sono ancora dubbi irrisolti?
- Questo è il momento perfetto per consultare la documentazione, approfondire o chiedere chiarimenti in classe.
- Riporta sul tuo quaderno (o nella tua app di note) le intuizioni più importanti, gli schemi o i frammenti di codice riutilizzabili.

#### 5. Applicare le idee in un progetto personale

- I passaggi precedenti servono ad assorbire la conoscenza. Ora prova a chiederti: *"Come posso usare questo concetto in un progetto mio?"*
- Costruisci un piccolo programma partendo dagli esempi del capitolo. A volte basta una piccola idea per consolidare una grande competenza!

> 💬 **Considerazioni aggiuntive:**  
> Questo approccio non è scolpito nella pietra: se un argomento ti è già del tutto familiare, puoi velocizzare la lettura per dedicare più tempo ai concetti nuovi. Nei capitoli puramente concettuali, concentrati sulla comprensione logica senza forzare la scrittura di codice.

---

### 🔬 Il Metodo PRIMM: Come affrontare ogni programma

> 💡 *Adattato dalle linee guida pedagogiche di [primmportal.com](https://primmportal.com/).*

Ogni volta che incontri un programma nel libro di testo, negli appunti o durante le lezioni in laboratorio, non limitarti a guardarlo passivamente. Segui rigorosamente queste 5 tappe:

```
[ 1. Predict ]  ──►  [ 2. Run ]  ──►  [ 3. Investigate ]  ──►  [ 4. Modify ]  ──►  [ 5. Make ]
 (Prevedi & Traccia)  (Digita a mano)    (Debug & Memoria)     (Piccoli cambi)   (Crea da zero)
```

#### Prima del Predict: orientati

- Leggi la teoria che presenta parole, struttura e regole indispensabili.
- Non cercare ancora la risposta del quiz: prepara soltanto gli strumenti per ragionare sul codice.

#### 1. PREDICT (Prevedi)

- Prima di eseguire il programma, esamina attentamente il codice sorgente e **ipotizza cosa farà**.
- Se il codice contiene condizioni, cicli o variabili che cambiano, costruisci sul quaderno una **tabella di traccia** (colonne con i valori assunti dalle variabili passo dopo passo).

#### 2. RUN (Esegui)

- Copia il programma nel tuo ambiente di sviluppo (VS Code o un IDE online).
- **Attenzione:** **non fare copia e incolla!** Digitare il codice parola per parola è indispensabile per memorizzare la sintassi e accorgersi dei dettagli.
- Esegui il programma e confronta l'output ottenuto con la previsione che avevi fatto al passo 1.

#### 3. INVESTIGATE (Investiga)

- Quando il programma usa variabili o memoria, copialo su [Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html) ed eseguilo **passo dopo passo**.
- Osserva come evolve lo stato della memoria e confrontalo con la tabella di traccia.

#### 4. MODIFY (Modifica)

- Modifica il codice sorgente procedendo a piccoli passi, per fare tuo il programma:
  - *Esempio 1:* se il programma usa valori prefissati (hardcoded), modificalo per chiedere i dati all'utente tramite istruzioni di input (`std::cin`).
  - *Esempio 2:* se usa numeri interi (`int`), prova a convertirli in numeri a virgola mobile (`double`) o viceversa, osservando come cambia il comportamento della divisione.
- Più modifichi il codice con cognizione di causa, più ne diventi padrone.

#### 5. MAKE (Crea)

- Scrivi un **nuovo programma autonomo** partendo da zero.
- Puoi prendere in prestito frammenti o strutture logiche dal programma appena studiato, applicandoli per risolvere un problema diverso o per realizzare una funzione nuova.
- Questo è il momento in cui passi da "lettore di codice" a "creatore di software".

---

### 📝 Riepilogo tascabile

- Prima leggi il contesto, l'obiettivo e la teoria: poi fai una previsione.
- Digita il codice a mano, senza *copia-e-incolla*, e confronta sempre output e Predict.
- Usa una tabella di traccia e [Python Tutor](https://pythontutor.com/cpp.html#mode=edit) quando cambiano variabili o memoria.
- Modifica poco alla volta; nel Make riusa l'idea in uno scenario nuovo.

---

### ➡️ Da dove si comincia

Prima di scrivere programmi, allestiamo l’**officina**: editor, compilatore e debugger.  
È una sessione di laboratorio, non una lettura di 20 minuti: senza utensili collaudati il resto del corso non parte.

## 🛠️ Prepara la tua Officina di Sviluppo: VS Code, MSYS2 e MinGW-w64

> "I programmi sono fatti per essere letti dagli esseri umani e solo incidentalmente per essere eseguiti dai computer."
> -- Donald Knuth

Questo non è un capitolo da leggere in 20 minuti.  
È una **sessione di laboratorio**: allestire l’officina richiede tempo, pazienza e qualche tentativo. In classe può occupare un’ora intera (o più, se qualcuno ha imprevisti). Non correre.

Alla fine di questa sessione avrai:

- Visual Studio Code (il banco di lavoro)
- l’estensione C/C++ (gli utensili specializzati)
- il compilatore **g++** e il debugger **gdb** (tramite MSYS2 + MinGW-w64)
- la variabile PATH impostata correttamente
- un programma di prova compilato, eseguito e debuggato con successo

> 💡 **Metafora:**  
>
> - **VS Code** = il tuo banco di lavoro (dove organizzi i pezzi e lavori)  
> - **Estensione C/C++** = le lampade e gli utensili specifici per il C++  
> - **MSYS2 + MinGW-w64** = il magazzino di pezzi di ricambio e il banco prove  
> - **PATH** = l’etichetta che dice a Windows “i tuoi utensili sono in *questo* cassetto”  
> - **Compilatore (g++)** = l’operaio che traduce il progetto in un pezzo finito (l’eseguibile)  
> - **Debugger (gdb)** = il tecnico che ti fa vedere cosa succede *dentro* il pezzo mentre funziona

---

### 🎯 Obiettivo di questa sessione

Alla fine sei in grado di configurare e verificare un ambiente C++ che compila,
esegue e fa il debug di un programma minimo.

---

### ⚠️ Prima di iniziare — casi particolari

**Se sei in laboratorio a scuola** e i computer hanno già VS Code + MinGW installati:  
salta i passi di installazione e vai direttamente al **Passo 6** (programma di prova). Chiedi al docente il percorso corretto se `g++` non viene riconosciuto.

**Se a casa non hai diritti di amministratore** o l’antivirus / le policy bloccano l’installazione:

1. Prova comunque i passi (molte operazioni non richiedono admin).
2. Se fallisci, usa temporaneamente un compilatore online (es. [Compiler Explorer](https://godbolt.org/) o [OnlineGDB](https://www.onlinegdb.com/)) per seguire le lezioni successive.
3. Segnala il problema al docente: troveremo una soluzione (immagine di laboratorio, chiavetta, ecc.).

Hai bisogno di **connessione Internet** per i download iniziali.

---

### 📋 Checklist di lavoro (segui l’ordine)

Ogni passo ha un **punto di controllo**.  
Se il controllo fallisce, **fermati** e risolvi prima di proseguire.

#### Passo 1 — Crea la cartella di lavoro del corso
Apri il Prompt dei comandi e digita:

```bat
mkdir %USERPROFILE%\Documenti\Cpp-3SIA
cd %USERPROFILE%\Documenti\Cpp-3SIA
```

(Se preferisci un altro percorso, va bene: l’importante è averne uno dedicato e ricordartelo.)

**Controllo:** il comando `cd` ti porta dentro la cartella senza errori.

#### Passo 2 — Installa Visual Studio Code
1. Vai su [https://code.visualstudio.com/](https://code.visualstudio.com/) e scarica la versione per Windows.
2. Esegui l’installer. Accetta le opzioni consigliate (in particolare “Aggiungi a PATH” se proposta).
3. Avvia VS Code almeno una volta.

**Controllo:** vedi la schermata di benvenuto di VS Code.

#### Passo 3 — Installa l’estensione C/C++
1. In VS Code apri la vista Extensions (`Ctrl+Shift+X`).
2. Cerca `C++` e installa l’estensione ufficiale **C/C++** di Microsoft (`ms-vscode.cpptools`).
3. (Consigliato) Installa anche **C/C++ Extension Pack**.

**Controllo:** nell’elenco delle estensioni installate compare “C/C++”.

#### Passo 4 — Installa MSYS2
1. Scarica l’installer più recente da [https://www.msys2.org/](https://www.msys2.org/).
2. Esegui l’installer. Lascia il percorso predefinito `C:\msys64` se non hai motivi particolari per cambiarlo.
3. Alla fine seleziona **Run MSYS2 now** e premi Finish. Si apre un terminale MSYS2.

**Controllo:** hai una finestra di terminale MSYS2 aperta.

#### Passo 5 — Installa la toolchain MinGW-w64 (ucrt)
Nel terminale MSYS2 digita **esattamente**:

```bash
pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
```

- Premi `Invio` per accettare il numero predefinito di pacchetti.
- Digita `Y` e premi `Invio` quando chiede conferma.
- Attendi la fine (può richiedere diversi minuti).

**Controllo:** il comando termina senza messaggi di errore in rosso.

#### Passo 6 — Aggiungi MinGW al PATH di Windows (il punto più delicato)
1. Nella barra di ricerca di Windows digita:  
   **“Modifica le variabili di ambiente per l’account”** e aprilo.
2. Nella sezione **Variabili utente** seleziona la riga `Path` → clicca **Modifica**.
3. Clicca **Nuovo** e scrivi (o incolla):
   ```
   C:\msys64\ucrt64\bin
   ```
   (Se hai installato MSYS2 altrove, adatta il percorso.)
4. Premi **OK** su tutte le finestre.
5. **Chiudi completamente** ogni Prompt dei comandi o PowerShell già aperti.  
   Il PATH viene letto solo all’avvio del terminale.

**Controllo (fondamentale):** apri un **nuovo** Prompt dei comandi e digita:

```bat
g++ --version
gdb --version
```

Devi vedere le versioni. Se compare “non è riconosciuto come comando…” il PATH non è ancora corretto: ricontrolla il percorso e riavvia il terminale.

#### Passo 7 — Primo programma di prova

Crea il file `prova.cpp` nella cartella del corso (`Documenti\Ci-Piu-Piu`) con questo contenuto:

```cpp
#include <iostream>

int main() {
    std::cout << "Ambiente C++ pronto!\n";
    return 0;
}
```

##### 1. Prevedi
Prima di compilare, rispondi:

Cosa pensi che succeda quando eseguirai il programma?

[( )] Comparirà una finestra grafica con un messaggio
[(X)] Nel terminale apparirà la scritta "Ambiente C++ pronto!"
[( )] Il computer si riavvierà
[( )] Comparirà un errore perché manca qualcosa

##### 2. Esegui da terminale
Nel Prompt dei comandi (sempre dentro la cartella del progetto):

```bat
g++ prova.cpp -o prova.exe
prova.exe
```

**Controllo:** deve comparire esattamente `Ambiente C++ pronto!`.

##### 3. Modifica
Cambia il messaggio stampato (es. metti il tuo nome o la tua classe) e ricompila.  
Verifica che la nuova frase appaia correttamente. Puoi usare il bottone "Esegui" sotto la finestra del codice sorgente per eseguire il codice.

```cpp
#include <iostream>

int main() {
    std::cout << "Ambiente C++ pronto!\n";
    return 0;
}
```
@LIA.cpp

---

### ▶️ Esecuzione e Debug da Visual Studio Code

Ora che il compilatore funziona da terminale, usiamo il banco di lavoro completo.

1. Dalla cartella del progetto digita:
   ```bat
   code .
   ```
   (Si apre VS Code con la cartella già caricata.)

2. Apri il file `prova.cpp`.

3. **Esecuzione semplice**  
   - Clicca il pulsante **Run** (play) in alto a destra,  
     oppure premi `Ctrl+F5`.  
   - La prima volta ti chiederà il compilatore: scegli **C/C++: g++.exe build and debug active file** (o simile).  
   - VS Code creerà automaticamente i file di configurazione nella cartella `.vscode`.

4. **Debug (il vero potere del banco di lavoro)**  
   - Clicca nel margine sinistro accanto a una riga di codice per mettere un **breakpoint** (pallino rosso).  
   - Premi `F5` (o scegli “Debug C/C++ File”).  
   - L’esecuzione si ferma sul breakpoint.  
   - A sinistra vedi le variabili, il call stack e i controlli per andare avanti passo-passo (`F10` = Step Over, `F11` = Step Into).

**Controllo finale:** riesci a far fermare il programma su un breakpoint e a vedere le variabili.  
Se sì, l’officina è completamente operativa.

> 🔗 Guida ufficiale di riferimento:  
> [Using GCC with MinGW – Visual Studio Code](https://code.visualstudio.com/docs/cpp/config-mingw)

---

### 🔬 Cosa abbiamo costruito?

| Componente              | Ruolo nella “officina”                          | Come si verifica              |
|-------------------------|--------------------------------------------------|-------------------------------|
| Cartella del corso      | Il tuo laboratorio personale                     | `cd` nella cartella           |
| VS Code                 | Banco di lavoro                                  | `code .`                      |
| Estensione C/C++        | Utensili specializzati + IntelliSense            | Extensions view               |
| MSYS2 + MinGW-w64       | Compilatore `g++` e debugger `gdb`               | `g++ --version`               |
| Variabile PATH          | Dice a Windows dove sono gli utensili            | `where g++`                   |
| `prova.cpp`             | Primo pezzo prodotto e collaudato                | Compila ed esegue             |
| Breakpoint + F5         | Ispezione interna del programma in esecuzione    | Il programma si ferma         |

---

### 📝 Riepilogo tascabile
- Questa è una **sessione di laboratorio**, non una lettura veloce.
- Senza compilatore non esiste programma eseguibile.
- Il PATH deve contenere `C:\msys64\ucrt64\bin` e va verificato in un **nuovo** terminale.
- `g++` traduce il codice sorgente in eseguibile; `gdb` ti fa guardare dentro mentre gira.
- Il programma `prova.cpp` è il tuo banco di prova: se compila, stampa e si debugga, l’officina è pronta.
- Da ora in poi lavorerai quasi sempre da VS Code, ma sapere usare il terminale ti salva quando qualcosa non va.

---

### ⚠️ Problemi frequenti e soluzioni rapide

| Sintomo                                      | Causa più probabile                          | Cosa fare                                              |
|----------------------------------------------|----------------------------------------------|--------------------------------------------------------|
| `g++` non è riconosciuto                     | PATH non aggiornato o terminale vecchio      | Chiudi **tutti** i terminali, ricontrolla Path, riapri |
| `pacman` non trova i pacchetti               | Connessione o mirror MSYS2                   | `pacman -Syu` e riprova più tardi                      |
| VS Code non trova il compilatore             | Estensione assente o PATH non visto          | Reinstalla estensione C/C++ e riavvia VS Code          |
| Messaggio su `miDebuggerPath`                | manca gdb                                    | Reinstalla il gruppo toolchain da MSYS2                |
| Antivirus blocca `g++.exe` o `ridotto.exe`   | Falso positivo                               | Aggiungi un’eccezione per la cartella del corso        |
| Non hai diritti di amministratore            | Policy di scuola o account limitato          | Usa il laboratorio o un compilatore online temporaneo  |

---

### ➡️ Prossimo chunk
Ora che l’officina è allestita e collaudata, possiamo finalmente aprire il cofano e capire **come** il codice sorgente diventa un programma eseguibile (pre-processore, compilatore, linker).  
Nel prossimo capitolo entreremo nella “fabbrica del codice”.


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

[(X)] Un eseguibile `ridotto.exe` pronto da avviare
[( )] Un file `.cpp` con il programma scritto automaticamente
[( )] Solo una stampa a video, senza creare file

**Domanda 2**

Perché `-save-temps` è utile mentre studi la compilazione?

[(X)] Chiede a `g++` di conservare i file temporanei intermedi
[( )] Rende il programma più veloce durante l'esecuzione
[( )] Salva automaticamente una copia del programma su Internet

**Domanda 3**

Dopo la pre-elaborazione, quale file contiene ancora codice testuale vicino al C++?

[(X)] Il file `.ii`, con direttive espanse e commenti rimossi
[( )] Il file `.o`, già composto solo da testo Assembly
[( )] Il file `.exe`, che contiene il sorgente originale leggibile

**Domanda 4**

Quale sequenza descrive meglio il percorso verso l'eseguibile?

[(X)] `.cpp` → `.ii` → `.s` → `.o` → `.exe`
[( )] `.cpp` → `.exe` → `.ii` → `.o` → `.s`
[( )] `.cpp` → `.o` → `.ii` → `.exe` → `.s`

**Domanda 5**

Perché il linker deve intervenire anche dopo la traduzione del tuo file?

[(X)] Per collegare il codice oggetto con librerie e codice di avvio
[( )] Per correggere i punti e virgola dimenticati nel C++
[( )] Per trasformare l'eseguibile di nuovo nel file sorgente

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
[( )] Il programma viene eseguito e il risultato viene salvato in `.s`
[( )] I file `.cpp` vengono compressi in un archivio di testo

**Domanda 3**

Quale ordine di osservazione è coerente con la catena di compilazione?

[(X)] Prima `.ii`, poi `.s`, poi `.o`, infine `.exe`
[( )] Prima `.exe`, poi `.o`, poi `.s`, infine `.ii`
[( )] `.ii` e `.exe` vengono creati soltanto dopo l'esecuzione

**Domanda 4**

Nel file Assembly, perché puoi trovare un'istruzione che prepara il valore `0`?

[(X)] Perché `return 0;` deve consegnare al sistema operativo un codice di uscita
[( )] Perché ogni programma deve stampare almeno uno zero
[( )] Perché `-save-temps` sostituisce ogni istruzione con il numero zero

**Domanda 5**

Se il compilatore segnala un errore di sintassi nel `.cpp`, perché la catena non arriva al linker?

[(X)] Senza una traduzione valida non esiste un file oggetto affidabile da collegare
[( )] Il linker lavora solo sui commenti e quindi ignora il programma
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

[(X)] Il codice di uscita del programma cambia da `0` a `7`
[( )] Il programma stampa automaticamente il numero `7`
[( )] Il compilatore salta la fase di assemblaggio

**Domanda 2**

Quale modifica permette di ottenere il file finale con il nome `importazione.exe`?

[(X)] Sostituire il nome dopo `-o` con `importazione.exe`
[( )] Cambiare l'estensione di `ridotto.cpp` in `.exe` prima di compilare
[( )] Scrivere `importazione.exe` dentro `return`

**Domanda 3**

Se togli `-save-temps`, quale cambiamento è più probabile?

[(X)] Ottieni comunque l'eseguibile, ma i file intermedi possono essere rimossi
[( )] Il C++ non può più essere compilato
[( )] Il programma viene trasformato direttamente in Assembly e non in `.exe`

**Domanda 4**

Quale modifica rende l'Assembly più facile da collegare al sorgente durante l'ispezione?

[(X)] Aggiungere `-fverbose-asm` al comando
[( )] Sostituire `-O0` con `return 0`
[( )] Rinominare il file `.o` in `.cpp` dopo la compilazione

**Domanda 5**

Perché conviene modificare una sola cosa alla volta nel comando o nel codice?

[(X)] Per collegare con chiarezza ogni effetto alla modifica che lo ha causato
[( )] Perché `g++` accetta una sola modifica per ogni esecuzione
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

## 💬 Il Primo Dialogo con la Macchina: `std::cout` e il programma minimo

> "L'unico modo per imparare un nuovo linguaggio di programmazione è scrivere programmi in quel linguaggio."
>
> -- Brian Kernighan

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

[(X)] Manca il punto di ingresso (`main`) e in genere le dichiarazioni necessarie (es. `#include`)
[( )] Perché non usa la parola chiave `program`
[( )] Perché il testo non è in inglese

**Domanda 3**

Cosa fa il carattere speciale `\n` all’interno della stringa?

[(X)] Inserisce un’andata a capo nell’output
[( )] Termina il programma
[( )] Apre una nuova finestra del terminale

**Domanda 4**

Quale affermazione spiega meglio il ruolo di `std::` davanti a `cout`?

[(X)] `std::` indica il namespace della libreria standard dove si trova `cout`
[( )] `std::` è obbligatorio solo in Windows
[( )] `std::` converte il testo in maiuscolo

**Domanda 5**

Se togli le virgolette e scrivi `std::cout << Ciao, Mondo!\n;` (senza `"`), perché il programma non è accettabile?

[(X)] Senza virgolette il compilatore non tratta il testo come stringa letterale
[( )] Perché `\n` non può stare fuori dalle virgolette mai
[( )] Perché `cout` funziona solo con numeri

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

[(X)] Perché dichiara gli strumenti di input/output (come `std::cout`) usati dopo
[( )] Perché avvia automaticamente la funzione `main`
[( )] Perché stampa da sola “Ciao, Mondo!”

**Domanda 2**

Perché ogni programma eseguibile ha bisogno di una funzione `main`?

[(X)] Perché è il punto di ingresso: da lì parte l’esecuzione
[( )] Perché è solo un commento per il programmatore
[( )] Perché sostituisce il compilatore

**Domanda 3**

Osserva l’ordine di esecuzione. Quale sequenza è corretta?

[(X)] Entra in `main` → esegue `std::cout` → esegue `return 0;`
[( )] Esegue `return 0;` → poi stampa → poi entra in `main`
[( )] Stampa prima ancora di entrare in `main`

**Domanda 4**

Cosa comunica `return 0;` al sistema operativo?

[(X)] Che il programma è terminato con successo (codice di uscita 0)
[( )] Che deve stampare il numero 0 a video
[( )] Che deve riavviare `main` da capo

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

[(X)] A video compare Gestionale pronto (e va a capo); il resto della struttura resta valido
[( )] Il programma non compila più
[( )] Viene stampato due volte Ciao, Mondo!

**Domanda 2**

Se rimuovi `\n` dalla stringa, quale effetto osservi?

[(X)] Il testo appare, ma il cursore non va a capo dopo il messaggio
[( )] Il programma non parte
[( )] Viene aggiunto automaticamente un secondo messaggio

**Domanda 3**

Vuoi una seconda riga di output. Quale modifica è corretta?

[(X)] Aggiungere un’altra istruzione `std::cout << "...\n";` dentro `main`, senza togliere la prima
[( )] Scrivere il secondo messaggio fuori da `main`
[( )] Sostituire `#include` con il secondo messaggio

**Domanda 4**

Se cancelli la riga `return 0;`, in un programma così semplice cosa succede di solito?

[(X)] Spesso compila comunque (return implicito da `main` in C++), ma è buona pratica lasciare `return 0;` esplicito
[( )] È sempre un errore di compilazione obbligatorio
[( )] Il programma stampa necessariamente “errore”

**Domanda 5**

Perché, in Modify, conviene cambiare **una cosa alla volta** e ricompilare?

[(X)] Per isolare causa ed effetto: se qualcosa si rompe, sai quale modifica l’ha provocato
[( )] Perché il compilatore accetta al massimo una modifica al giorno
[( )] Perché altrimenti `std::cout` smette di funzionare

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

## 📝 Parlare al Futuro Te Stesso: documentazione Doxygen

> "Il codice non mente mai, i commenti sì."
>
> —- Ron Jeffries

Hai già scritto `Ciao, Mondo!` e presto i programmi si allungheranno.  
Chi li leggerà tra tre mesi? Tu. Un compagno. Il docente. In azienda, un collega che non eri tu.

Non basta che il programma *funzioni*: deve essere **comprensibile**.  
In questo corso usiamo uno standard leggero e molto diffuso: **Doxygen**.

> 💡 **Metafora:**  
> Il codice è il prodotto.  
> I commenti Doxygen sono **etichetta e manuale d’uso**: dicono *cosa fa*, *per chi*, *con quali dati*, senza smontare tutto il meccanismo.

Questo non è un laboratorio PRIMM “classico”: è una **convenzione di lavoro** che userai da qui in poi nei Make e nei progetti.

---

### 🎯 Obiettivo
Alla fine di questa lezione sei in grado di:
- Scrivere un’intestazione di **file** e di **`main`** in stile Doxygen
- Usare `///` per spiegare il **perché** (non il cosa ovvio)
- Applicare la **regola di proporzionalità** del corso

---

### 📋 I tag che usiamo (e basta)

| Tag | A cosa serve | Esempio |
|-----|--------------|---------|
| `@file` | Nome del file | `@file presentazione.cpp` |
| `@brief` | Una riga: cosa fa il programma o la funzione | `@brief Stampa nome e classe.` |
| `@author` | L'autore del programma | `@author Gionata Massi` |
| `@date` | La data | `@date 2026-11-03` |
| `@param` | Descrive un parametro (quando avremo le funzioni) | `@param prezzo Importo netto in euro` |
| `@return` | Cosa restituisce la funzione | `@return int 0 se successo` |

Commento di riga (tre slash):

```cpp
/// Aliquota IVA ordinaria vigente (non modificare a caso)
const double ALIQUOTA_IVA = 0.22;
```

`@param` lo terrai a mente: tornerà utile con le **funzioni**. Per ora ti servono soprattutto `@file`, `@brief` e `@return`.

---

### ✅ Esempio minimo completo

```cpp
/**
 * @file presentazione.cpp
 * @brief Stampa nome, classe e hobby dello studente.
 */
#include <iostream>

/**
 * @brief Punto di ingresso del programma.
 * @return int 0 se l'esecuzione termina correttamente.
 */
int main() {
    /// Identificativo per lo "scontrino" di presentazione in lab
    std::cout << "Nome: Alex\n";
    std::cout << "Classe: 3A SIA\n";
    std::cout << "Hobby: fotografia\n";
    return 0;
}
```

Nota: **non** generiamo ancora HTML con lo strumento Doxygen.  
L’obiettivo è **scrivere** i commenti nel modo giusto; l’eventuale generazione automatica arriverà quando i progetti saranno più grandi.

---

### ⚖️ Regola di proporzionalità (obbligatoria)

| Situazione | Cosa scrivere |
|------------|----------------|
| Programma o funzione **più lungo di ~15 righe** | Intestazione Doxygen (`@file` / `@brief` / `@param` / `@return` dove servono) |
| Snippet o esercizio **breve** | Solo `///` sul **perché** economico o logico, se serve |
| **Vietato** | Commenti tautologici (`/// incrementa i di 1`, `/// dichiara la variabile`) |

**Buono** (spiega una scelta di business o un vincolo):
```cpp
/// 0.22 = aliquota IVA ordinaria vigente per beni e servizi
const double ALIQUOTA_IVA = 0.22;
```

**Da evitare** (ripete solo la sintassi):
```cpp
/// dichiara la costante aliquota
const double ALIQUOTA_IVA = 0.22;
```

---

### 🧪 Mini-esercizio

Prendi il programma di presentazione del capitolo precedente (o riscrivilo) e:

1. Aggiungi in testa al file `@file` e `@brief`
2. Aggiungi su `main` `@brief` e `@return`
3. Metti **un** `///` utile (un perché, non un ovvio) su almeno una riga

Compila ed esegui: i commenti non cambiano l’output, ma cambiano quanto il codice è leggibile da un umano.

---

### 📝 Riepilogo tascabile
- Doxygen = etichette standard per file e funzioni.
- Tag minimi ora: `@file`, `@brief`, `@return` (più `@param` più avanti).
- `///` = perché / vincolo / regola di business, non il cosa ovvio.
- Proporzionalità: completo sopra ~15 righe, leggero sotto.
- Da qui in poi i Make “ufficiali” si aspettano questi standard.

---

### ➡️ Prossimo passo
Con officina, motore, primo dialogo e etichette chiare, apriamo gli **sportelli della memoria**: variabili, tipi e costanti.

---




## 📦 Gli sportelli della memoria: variabili, costanti e tipi

> "Chi controlla il passato controlla il futuro.
> Chi controlla il presente controlla il passato."
>
> -- George Orwell

Finora hai stampato testi fissi. Un software gestionale, però, deve ricordare
dati che cambiano: prezzo di un articolo, giacenza di magazzino, saldo di un
conto.

Per farlo usi variabili e costanti.

> 💡 **Metafora:** Immagina la memoria RAM come una parete di sportelli
> automatici. Il nome della variabile è l'etichetta che leggi tu; il tipo
> indica quale merce può entrare nello sportello; il valore è la merce
> conservata. Uno sportello `const` è sigillato: dopo averlo riempito non puoi
> cambiare il contenuto.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- dichiarare variabili e costanti scegliendo il tipo adatto a un dato aziendale.

In questo chunk non chiediamo ancora dati da tastiera con `std::cin`: ci
concentriamo sul ricordare, mostrare e modificare valori già scritti nel codice.

---

### ⚙️ Prima del laboratorio: i tipi fondamentali

| Tipo | Che cosa contiene | Esempio aziendale |
| :--- | :--- | :--- |
| `int` | Numeri interi | `int giacenza = 42;` |
| `double` | Numeri con parte decimale | `double prezzo = 19.50;` |
| `char` | Un solo carattere | `char reparto = 'A';` |
| `bool` | Uno tra due stati | `bool inPromozione = true;` |
| `std::string` | Testo di lunghezza variabile | `std::string nome = "Mouse";` |
| `const T` | Valore non modificabile | `const double IVA = 0.22;` |

Per usare `std::string` inserisci `#include <string>`.

> ⚠️ **Trappola classica:** `int pezzi = 7.85;` non arrotonda a `8`.
> Conserva `7`, perché `int` non può contenere la parte decimale. Per prezzi,
> saldi e aliquote usa `double`.

---

### 🧭 Prima del laboratorio: dichiarare e sigillare

Una dichiarazione unisce tipo, nome e valore iniziale:

| Scrittura | Come leggerla |
| :--- | :--- |
| `int giacenza = 42;` | Uno sportello per un conteggio intero |
| `double prezzo = 19.50;` | Uno sportello per un valore con centesimi |
| `const double IVA = 0.22;` | Uno sportello sigillato con un valore decimale |

Il tipo non è una decorazione: stabilisce quali valori possono essere
conservati e quali operazioni hanno senso.

---

### 🔬 Laboratorio PRIMM: la scheda articolo

Un magazzino deve mostrare i dati di un articolo: descrizione, reparto,
giacenza, prezzo e garanzia. Ogni dato usa uno sportello adatto.

#### 1. PREDICT (Prevedi)

```cpp
int pezzi = 7.85;
double prezzo = 19.50;
const double IVA = 0.22;
```

**Domanda 1**

Perché `int pezzi = 7.85;` non conserva tutti i decimali?

[(X)] Perché `int` rappresenta numeri interi e la parte decimale viene troncata
[( )] Perché il compilatore arrotonda sempre i prezzi per difetto
[( )] Perché ogni numero con la virgola produce un errore obbligatorio

**Domanda 2**

Quale tipo è più adatto per memorizzare un prezzo con i centesimi?

[(X)] `double`, perché può rappresentare valori con parte decimale
[( )] `int`, perché i prezzi sono sempre conteggi di pezzi
[( )] `char`, perché ogni prezzo è una singola cifra

**Domanda 3**

Perché `IVA` dovrebbe essere dichiarata `const`?

[(X)] Per impedire che il valore venga cambiato accidentalmente durante il programma
[( )] Per permettere al programma di modificarla più velocemente
[( )] Perché `const` trasforma automaticamente il numero in una stringa

**Domanda 4**

Quale tipo descrive meglio il codice di reparto `'A'`?

[(X)] `char`, perché contiene un solo carattere
[( )] `std::string`, perché ogni carattere è sempre una frase
[( )] `bool`, perché il reparto può essere vero o falso

**Domanda 5**

Che cosa indica la dichiarazione `bool haFido = true;`?

[(X)] Un dato con due stati possibili, qui impostato sul valore vero
[( )] Un testo composto dalle lettere `true`
[( )] Un numero decimale uguale a 1.0

#### 2. RUN (Esegui)

Digita il programma completo oppure usa il bottone. Prima di eseguirlo, indica
accanto a ogni variabile quale tipo riconosci.

```cpp
/**
 * @file scheda_articolo.cpp
 * @brief Memorizza e mostra i dati di un articolo di magazzino.
 */
#include <iostream>
#include <string>

/**
 * @brief Mostra una scheda articolo con tipi di dato diversi.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// L'aliquota di legge deve restare uguale durante il calcolo.
    const double ALIQUOTA_IVA = 0.22;
    /// Il nome commerciale può cambiare tra articoli.
    std::string nomeArticolo = "Mouse Wireless Ottico";
    /// Un reparto aziendale può essere rappresentato da un codice breve.
    char codiceReparto = 'A';
    /// La giacenza conta pezzi interi presenti in magazzino.
    int pezziInMagazzino = 42;
    /// Il prezzo richiede i centesimi.
    double prezzoNetto = 19.50;
    /// La garanzia estesa ha soltanto due stati.
    bool haGaranziaEstesa = true;

    std::cout << "=== SCHEDA ARTICOLO MAGAZZINO ===\n";
    std::cout << "Descrizione : " << nomeArticolo << "\n";
    std::cout << "Reparto     : " << codiceReparto << "\n";
    std::cout << "Giacenza    : " << pezziInMagazzino << " pezzi\n";
    std::cout << "Prezzo netto: " << prezzoNetto << " euro\n";
    std::cout << "Garanzia    : " << haGaranziaEstesa << "\n";
    std::cout << "Aliquota IVA: " << ALIQUOTA_IVA << "\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

Ora collega ogni sportello al suo ruolo. Rispondi alle domande sul *perché*,
non solo sul valore stampato.

```cpp
const double ALIQUOTA_IVA = 0.22;
int pezzi = 42;
double prezzoNetto = 19.50;
```

**Domanda 1**

Perché `pezzi` è un `int` mentre `prezzoNetto` è un `double`?

[(X)] I pezzi sono conteggi interi, mentre il prezzo può contenere centesimi
[( )] I nomi delle variabili decidono automaticamente il tipo
[( )] `double` serve solo per dati più importanti di `int`

**Domanda 2**

Quale sequenza descrive la dichiarazione `double prezzoNetto = 19.50;`?

[(X)] Il compilatore riserva un dato decimale, gli assegna un nome e gli dà un valore iniziale
[( )] Il programma stampa subito 19.50 senza bisogno di `std::cout`
[( )] Il valore viene sigillato e non potrà mai cambiare

**Domanda 3**

Perché `ALIQUOTA_IVA` non può essere assegnata di nuovo?

[(X)] La parola `const` la rende di sola lettura dopo l'inizializzazione
[( )] I nomi scritti in maiuscolo sono sempre immutabili in C++
[( )] Un `double` può essere assegnato una sola volta

**Domanda 4**

Quale valore viene memorizzato in `int pezzi = 7.85;`?

[(X)] `7`, perché la parte decimale non appartiene al tipo `int`
[( )] `8`, perché C++ arrotonda al numero intero più vicino
[( )] `7.85`, perché il tipo dichiarato non influenza il valore

**Domanda 5**

Perché il programma ha bisogno di `#include <string>` quando usa `std::string`?

[(X)] Per rendere disponibile la definizione del tipo per il testo
[( )] Per convertire automaticamente tutti i numeri in testo
[( )] Per permettere a `int` di contenere più cifre

| Nome | Tipo | Perché quel tipo? | Si può cambiare? |
| :--- | :--- | :--- | :--- |
| `ALIQUOTA_IVA` | `const double` | È un valore di legge | No |
| `nomeArticolo` | `std::string` | Contiene testo variabile | Sì |
| `codiceReparto` | `char` | Contiene un carattere | Sì |
| `pezziInMagazzino` | `int` | Conta pezzi interi | Sì |
| `prezzoNetto` | `double` | Contiene centesimi | Sì |
| `haGaranziaEstesa` | `bool` | Rappresenta sì/no | Sì |

Apri il programma su [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva come ogni variabile entra nello stack con un tipo e un valore.

Ricorda: senza `std::boolalpha`, `true` viene normalmente mostrato come `1` e
`false` come `0`.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
const double ALIQUOTA_IVA = 0.22;
double prezzoNetto = 19.50;
```

**Domanda 1**

Quale modifica permette di calcolare l'importo dell'IVA?

[(X)] Dichiarare `double importoIva = prezzoNetto * ALIQUOTA_IVA;`
[( )] Dichiarare `int importoIva = prezzoNetto + ALIQUOTA_IVA;`
[( )] Cambiare `const` in `std::string` senza eseguire un calcolo

**Domanda 2**

Che cosa succede se aggiungi `ALIQUOTA_IVA = 0.10;`?

[(X)] Il compilatore segnala un errore perché la costante è di sola lettura
[( )] L'aliquota cambia solo per la riga successiva
[( )] Il programma ignora sempre la nuova assegnazione e compila

**Domanda 3**

Quale modifica è corretta se la giacenza deve diventare 100 pezzi?

[(X)] Cambiare il valore iniziale in `int pezziInMagazzino = 100;`
[( )] Cambiare il tipo in `char` e lasciare il valore `100`
[( )] Dichiarare la giacenza come `const` per poterla aggiornare

**Domanda 4**

Quale effetto ha cambiare `bool haGaranziaEstesa = true;` in `false`?

[(X)] Il dato rappresenta l'assenza della garanzia estesa e l'output numerico diventa `0`
[( )] Il programma non può più compilare perché `bool` accetta solo `true`
[( )] La variabile diventa automaticamente una stringa vuota

**Domanda 5**

Perché conviene modificare un tipo o un valore alla volta?

[(X)] Per distinguere quale modifica ha prodotto il nuovo comportamento o l'errore
[( )] Perché ogni programma C++ può avere una sola variabile
[( )] Perché il compilatore non sa leggere due righe consecutive

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    const double ALIQUOTA_IVA = 0.22;
    double prezzoNetto = 19.50;
    return 0;
}
```

</details>

**Modifica A — calcola l'IVA**

Dichiara una nuova variabile:

```cpp
double importoIva = prezzoNetto * ALIQUOTA_IVA;
```

Poi stampa `importoIva` e il prezzo lordo, ottenuto sommando
`prezzoNetto + importoIva`.

**Modifica B — prova il lucchetto**

Aggiungi questa riga dopo la dichiarazione della costante:

```cpp
ALIQUOTA_IVA = 0.10;
```

Ricompila e osserva l'errore:

```text
error: assignment of read-only variable 'ALIQUOTA_IVA'
```

La parola `const` ha impedito un'assegnazione successiva: il compilatore
protegge il valore sigillato.

**Modifica C — cambia il dato aziendale**

Sostituisci `19.50` con `125.75`, ricompila e osserva come cambiano IVA e
prezzo lordo senza cambiare il tipo.

#### 5. MAKE (Crea)

**Scenario aziendale:** devi preparare una scheda sintetica di un conto
corrente aziendale.

Scrivi `conto_corrente.cpp` rispettando tutti i requisiti:

1. Memorizza banca e IBAN con `std::string`.
2. Memorizza saldo e interesse con `double`.
3. Usa `const double` per il tasso annuo.
4. Usa `bool` per indicare se il conto ha un fido.
5. Usa `char` per la classe di rating.
6. Stampa tutti i dati e calcola `saldo * tasso`.
7. Non modificare la costante del tasso dopo l'inizializzazione.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Scheda sintetica di un conto corrente aziendale.
 */
#include <iostream>
#include <string>

int main() {
    /// Il tasso è costante perché rappresenta la condizione del conto.
    // TODO: dichiara banca, IBAN, saldo, tasso, fido e rating.
    // TODO: stampa i dati e l'interesse annuo stimato.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Una variabile è uno sportello con nome, tipo e valore.
- `int` serve per conteggi interi; `double` per valori con decimali.
- `char` contiene un carattere; `bool` rappresenta due stati; `std::string` contiene testo.
- `const` sigilla un valore dopo l'inizializzazione.
- Scegli il tipo in base al significato aziendale del dato.

---

### ➡️ Prossimo chunk

Ora che sai memorizzare dati con il tipo corretto, userai operatori ed
espressioni per calcolare totali, IVA e differenze in modo controllato.


## 🧾 Chiedere informazioni: leggere dati con `std::cin`

Un gestionale non può lavorare soltanto con dati scritti in anticipo. Al POS
l'operatore inserisce una quantità; in un preventivo inserisce un prezzo; in
magazzino comunica quanti pezzi sono arrivati.

Con `std::cin` il tuo programma può aspettare un dato dalla tastiera e
conservarlo in una variabile.

> 💡 **Metafora:** Immagina un addetto allo sportello. `std::cout` è la voce
> con cui l'addetto fa una domanda; `std::cin` è il modulo su cui annota la
> risposta; la variabile è il campo del modulo destinato a quel dato. Se
> chiedi prima la quantità e poi il prezzo, devi registrare le risposte nello
> stesso ordine.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- leggere da tastiera quantità e prezzi con `std::cin` e usarli in un calcolo.

---

### ⚙️ Prima del laboratorio: input e output

| Istruzione | Direzione del dato | Esempio |
| :--- | :--- | :--- |
| `std::cout << valore` | Dal programma allo schermo | Mostra una richiesta o un risultato |
| `std::cin >> variabile` | Dalla tastiera alla variabile | Conserva ciò che l'utente inserisce |
| `int quantita;` | Prepara uno spazio per interi | Pezzi o confezioni |
| `double prezzo;` | Prepara uno spazio per decimali | Prezzi o importi |

La variabile deve esistere prima della lettura:

```cpp
int quantita;
std::cin >> quantita;
```

Il simbolo `>>` indica che il dato viaggia dalla tastiera verso la variabile.
Non confonderlo con `<<`, che usa la direzione opposta.

---

### 🧭 Prima del laboratorio: l'ordine del dialogo

Un dialogo utile segue questo percorso:

1. `std::cout` spiega quale dato inserire.
2. `std::cin` aspetta la risposta.
3. La variabile conserva il valore.
4. Il programma usa il valore nel calcolo o nel riepilogo.

Se il prezzo viene letto dopo la quantità, anche l'utente deve inserire prima la
quantità e poi il prezzo. Il computer non indovina l'ordine che avevi in mente.

---

### 🔬 Laboratorio PRIMM: un ordine al POS

Il POS deve leggere quantità e prezzo unitario per calcolare il totale di una
riga di vendita.

#### 1. PREDICT (Prevedi)

```cpp
int quantita;
double prezzo;
std::cin >> quantita;
std::cin >> prezzo;
```

**Domanda 1**

Che cosa fa `std::cin >> quantita;` quando il programma arriva a questa riga?

[(X)] Attende un valore da tastiera e lo memorizza nella variabile `quantita`
[( )] Stampa il nome `quantita` sullo schermo
[( )] Assegna automaticamente a `quantita` il valore zero

**Domanda 2**

Perché una variabile deve essere dichiarata prima di essere usata con `std::cin`?

[(X)] Il compilatore deve conoscere nome e tipo dello spazio in cui conservare il dato
[( )] La tastiera può inviare dati solo a variabili dichiarate come `const`
[( )] Senza dichiarazione `std::cin` stampa sempre un messaggio di errore a video

**Domanda 3**

Se il programma esegue prima `std::cin >> quantita;` e poi `std::cin >> prezzo;`, che cosa deve inserire l'utente?

[(X)] Prima un valore compatibile con `quantita`, poi uno compatibile con `prezzo`
[( )] Un solo testo che contiene contemporaneamente nome e prezzo
[( )] Prima il prezzo, perché `double` viene sempre letto per primo

**Domanda 4**

Perché il messaggio `Inserisci la quantità:` va scritto prima di `std::cin`?

[(X)] Per spiegare all'utente quale dato deve digitare prima che il programma attenda
[( )] Perché `std::cin` legge solo dopo aver stampato almeno tre righe
[( )] Per trasformare automaticamente un intero in una stringa

**Domanda 5**

Quale tipo è coerente con una quantità intera di prodotti?

[(X)] `int`, perché una quantità di confezioni può essere un numero intero
[( )] `double`, perché ogni dato inserito da tastiera contiene decimali
[( )] `char`, perché la quantità è sempre un singolo carattere

#### 2. RUN (Esegui)

Digita il programma completo. Quando compare una richiesta, inserisci un valore
e premi `Invio`; poi inserisci il valore successivo.

```cpp
/**
 * @file ordine_pos.cpp
 * @brief Legge quantità e prezzo per calcolare una riga di vendita.
 */
#include <iostream>

/**
 * @brief Acquisisce i dati di un ordine e calcola il totale.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// La quantità conta confezioni intere vendute.
    int quantita;
    /// Il prezzo deve conservare i centesimi dell'articolo.
    double prezzoUnitario;

    std::cout << "Quantita: ";
    std::cin >> quantita;

    std::cout << "Prezzo unitario: ";
    std::cin >> prezzoUnitario;

    double totale = quantita * prezzoUnitario;
    std::cout << "Totale: " << totale << " euro\n";

    return 0;
}
```
@LIA.cpp

Prova, per esempio, con:

```text
3
12.50
```

Il programma dovrebbe calcolare `37.5` euro.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci il percorso di ciascun dato. Concentrati sul
*perché* e sull'ordine, non soltanto sul totale.

```cpp
int quantita;
double prezzoUnitario;

std::cout << "Quantita: ";
std::cin >> quantita;
std::cout << "Prezzo: ";
std::cin >> prezzoUnitario;
```

**Domanda 1**

Qual è l'ordine corretto quando l'utente inserisce `3` e poi `12.50`?

[(X)] Il `3` entra in `quantita`, poi `12.50` entra in `prezzoUnitario`
[( )] Entrambi i valori entrano nella stessa variabile `quantita`
[( )] `12.50` viene letto per primo perché è un numero decimale

**Domanda 2**

Perché `std::cin` non mostra da solo la richiesta "Quantita:"?

[(X)] `std::cin` legge dati; il messaggio per l'utente deve essere scritto con `std::cout`
[( )] La tastiera non permette di visualizzare messaggi
[( )] Ogni variabile deve contenere il testo della richiesta

**Domanda 3**

Che cosa succede se inserisci `3` quando `std::cin` sta leggendo un `double`?

[(X)] Il valore può essere letto come `3.0`, perché un intero è compatibile con un numero decimale
[( )] Il programma si chiude sempre senza leggere nulla
[( )] Il numero viene trasformato in una parola composta da tre caratteri

**Domanda 4**

Perché l'istruzione `double totale = quantita * prezzoUnitario;` deve venire dopo le due letture?

[(X)] Prima di quel punto le variabili potrebbero non contenere ancora i dati inseriti dall'utente
[( )] Le moltiplicazioni in C++ sono permesse solo nell'ultima riga di `main`
[( )] `std::cin` cancella i valori se il calcolo viene scritto prima

**Domanda 5**

Se inserisci testo come `tre` quando `std::cin` attende un `int`, perché il calcolo successivo è inaffidabile?

[(X)] La lettura fallisce e la variabile non riceve il numero atteso
[( )] C++ converte sempre automaticamente ogni parola nel numero corretto
[( )] Il testo viene memorizzato nell'intero come se fosse un carattere

| Passo | Istruzione | Stato importante |
| :---: | :--- | :--- |
| 1 | `int quantita;` | Esiste uno spazio per un intero |
| 2 | `double prezzoUnitario;` | Esiste uno spazio per un decimale |
| 3 | `std::cin >> quantita;` | Il primo input entra in `quantita` |
| 4 | `std::cin >> prezzoUnitario;` | Il secondo input entra in `prezzoUnitario` |
| 5 | `double totale = ...` | Il calcolo usa i due valori letti |

`std::cin` non crea il messaggio per l'utente: legge soltanto. Per questo
`std::cout` deve precedere ogni lettura con una richiesta chiara.

Se inserisci `tre` quando il programma attende un `int`, la lettura non riceve
il numero previsto. Per ora non gestiamo ancora l'errore: impariamo prima il
percorso normale dei dati.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva come i valori
> inseriti sostituiscono il contenuto iniziale delle variabili.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
int quantita;
double prezzoUnitario;

std::cout << "Quantita: ";
std::cin >> quantita;
std::cout << "Prezzo: ";
std::cin >> prezzoUnitario;
```

**Domanda 1**

Quale modifica permette di leggere anche uno sconto percentuale?

[(X)] Dichiarare `double sconto;` e aggiungere `std::cin >> sconto;` dopo il prezzo
[( )] Scrivere `std::cin << sconto;` senza dichiarare la variabile
[( )] Cambiare `quantita` in `const double` per ricevere un nuovo dato

**Domanda 2**

Se vuoi leggere prima il prezzo e poi la quantità, quale modifica è necessaria?

[(X)] Invertire sia i messaggi sia l'ordine delle due istruzioni `std::cin`
[( )] Cambiare solo i nomi delle variabili, lasciando invariato il codice
[( )] Usare `std::cout` al posto di entrambe le istruzioni di lettura

**Domanda 3**

Che effetto ha aggiungere `std::cout << " euro\n";` dopo il totale?

[(X)] Aggiunge l'unità di misura all'output, senza cambiare il calcolo
[( )] Converte il totale in un intero arrotondato
[( )] Fa inserire un altro prezzo all'utente

**Domanda 4**

Quale modifica conserva i centesimi del prezzo inserito?

[(X)] Dichiarare il prezzo come `double` e leggerlo con `std::cin`
[( )] Dichiarare il prezzo come `int` perché è più semplice
[( )] Leggere il prezzo in un `char` e poi moltiplicarlo

**Domanda 5**

Perché conviene aggiungere una sola lettura o modifica alla volta?

[(X)] Per capire quale passaggio ha causato un errore o un ordine di input inatteso
[( )] Perché `std::cin` può leggere una sola variabile in tutta la funzione
[( )] Perché ogni nuova variabile cancella automaticamente la precedente

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    int quantita;
    double prezzoUnitario;

    std::cout << "Quantita: ";
    std::cin >> quantita;

    std::cout << "Prezzo unitario: ";
    std::cin >> prezzoUnitario;

    double totale = quantita * prezzoUnitario;
    std::cout << "Totale: " << totale << " euro\n";
    return 0;
}
```

</details>

**Modifica A — aggiungi uno sconto**

Dichiara `double sconto;`, mostra una richiesta e leggi la percentuale dopo il
prezzo unitario. Per ora stampa il valore inserito senza cambiare il totale.

**Modifica B — cambia l'ordine**

Fai chiedere prima il prezzo e poi la quantità. Inverti sia i messaggi sia le
istruzioni `std::cin`, così il dialogo resta coerente.

**Modifica C — aggiungi l'unità di misura**

Completa la stampa del totale con il testo `euro`. Il testo cambia l'output,
non il calcolo.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio commerciale deve creare un piccolo
preventivo per un cliente.

Crea `preventivo.cpp` rispettando tutti i requisiti:

1. Dichiara `int quantita` e `double prezzoUnitario` prima delle letture.
2. Chiedi e leggi quantità e prezzo con `std::cin`.
3. Mantieni lo stesso ordine tra messaggi, input e variabili.
4. Calcola `totale = quantita * prezzoUnitario`.
5. Stampa quantità, prezzo unitario e totale.
6. Usa un commento `///` per spiegare perché il prezzo è `double`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    /// TODO: spiega perché il prezzo deve conservare i centesimi.
    // TODO: dichiara quantità e prezzo, leggili e calcola il totale.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `std::cout <<` porta dati dal programma allo schermo.
- `std::cin >>` porta dati dalla tastiera a una variabile.
- Dichiara una variabile prima di usarla per la lettura.
- L'ordine di prompt e letture deve corrispondere all'ordine degli input.
- Usa `int` per quantità intere e `double` per prezzi con centesimi.

---

### ➡️ Prossimo chunk

Ora il programma sa chiedere dati. Nel prossimo chunk imparerai a scegliere tra
due percorsi con `if`, così il gestionale potrà reagire ai valori inseriti.


## 🧮 La Calcolatrice Fiscale: espressioni e operatore ternario

> "I computer non sono intelligenti: sono solo calcolatori incredibilmente veloci e obbedienti."
> — *Principio dell'Elaborazione Dati*

Nel capitolo precedente abbiamo riempito gli sportelli della memoria.  
Ora impariamo a **calcolare** e a **decidere in una riga**: IVA, sconti, spese di spedizione, commissioni POS.

> 💡 **Metafora: la cassa automatica**  
> - **Operatori aritmetici** = i calcoli sul nastro (somme, sconti %, quantità × prezzo)  
> - **Operatori di confronto e logici** = i sensori (“spesa > 50?”, “ha tessera E spesa alta?”)  
> - **Operatore ternario `?:`** = il display che decide all’istante:  
>   *“Spesa ≥ 60€ ? Spedizione gratis : paghi 6,50€”*

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un'espressione che calcola oppure sceglie un valore per uno scontrino

---

### ⚙️ Prima del laboratorio: calcolare un valore

Un’**espressione** combina valori, variabili e operatori e produce **un solo risultato**.

#### Aritmetici
| Operatore | Significato | Attenzione |
|-----------|-------------|------------|
| `+` `-` `*` | somma, sottrazione, moltiplicazione | — |
| `/` | divisione | Se **entrambi** gli operandi sono `int` → **divisione intera** (i decimali si perdono) |
| `%` | resto (modulo) | Solo su interi: `14 % 2 == 0` → pari |

```cpp
int pezzi = 5;
double a = pezzi / 2;      // 2  (divisione intera!)
double b = pezzi / 2.0;    // 2.5 (almeno un operando double)
```

---

### 🧭 Prima del laboratorio: scegliere un valore

Un confronto come `totaleSpesa >= 60.0` produce `true` o `false`. Il ternario
usa quel risultato come un sensore alla cassa: sceglie uno dei due prezzi.

```text
condizione ? valore_se_vero : valore_se_falso
```

È un’**espressione**: calcola e restituisce un valore, pronto per essere assegnato o stampato.

```cpp
double speseSpedizione = (totaleSpesa >= 60.0) ? 0.0 : 6.50;
```

Usalo per una scelta semplice che restituisce un valore. Per logiche con più
istruzioni useremo `if` / `else` nel prossimo capitolo.

---

### 🔬 Laboratorio PRIMM: Scontrino e-commerce

Calcoliamo sconto e spese di spedizione di un ordine online con espressioni e operatore ternario.

#### 1. PREDICT (Prevedi)


```cpp
int pezzi = 5;
double t = pezzi / 2 * 10.0;
std::cout << t;
```

Cosa stampa int pezzi = 5; double t = pezzi / 2 * 10.0; ?

[( )] 25
[(X)] 20
[( )] 2.5


<details>
<summary>💡 Spiegazione</summary>
<code>pezzi / 2</code> è divisione tra interi → risultato <code>2</code> (troncato).  
Poi <code>2 * 10.0</code> → <code>20.0</code>.  
Con <code>pezzi / 2.0 * 10.0</code> otterresti <code>25.0</code>.
</details>

#### 2. RUN (Esegui)
Digita e esegui:

```cpp
/**
 * @file cassa_fiscale.cpp
 * @brief Scontrino con sconto fedeltà e spese di spedizione (ternario).
 */
#include <iostream>

/**
 * @brief Calcola totale carrello, sconto e spedizione.
 * @return int 0 se successo.
 */
int main() {
    const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;
    const double COSTO_SPEDIZIONE_STANDARD = 6.50;

    double importoProdotti = 85.00;

    /// La soglia premia un ordine abbastanza grande con lo sconto maggiore.
    double percentualeSconto =
        (importoProdotti >= 50.0) ? 0.10 : 0.02;

    double valoreSconto = importoProdotti * percentualeSconto;
    double nettoProdotti = importoProdotti - valoreSconto;

    /// Spedizione gratis oltre soglia
    double speseSpedizione =
        (nettoProdotti >= SOGLIA_SPEDIZIONE_GRATIS) ? 0.0 : COSTO_SPEDIZIONE_STANDARD;

    double totaleDaPagare = nettoProdotti + speseSpedizione;

    std::cout << "=== SCONTRINO E-COMMERCE ===\n";
    std::cout << "Prodotti (lordo) : " << importoProdotti << " euro\n";
    std::cout << "Sconto applicato : " << valoreSconto << " euro\n";
    std::cout << "Prodotti (netto) : " << nettoProdotti << " euro\n";
    std::cout << "Spedizione       : " << speseSpedizione << " euro\n";
    std::cout << "TOTALE DA PAGARE : " << totaleDaPagare << " euro\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Segui il flusso dei valori (con i numeri dell’esempio).

| Espressione | Risultato | Perché |
|-------------|-----------|--------|
| `importoProdotti >= 50.0` | `true` | 85 è maggiore della soglia |
| percentuale sconto | `0.10` | ramo `?` del ternario |
| `valoreSconto` | `8.5` | `85 * 0.10` |
| `nettoProdotti` | `76.5` | `85 - 8.5` |
| `nettoProdotti >= 60` | `true` | soglia superata |
| `speseSpedizione` | `0.0` | ramo `?` del secondo ternario |

> 🔗 Esegui il programma passo-passo su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double importoProdotti = 85.00;
    double speseSpedizione = (importoProdotti >= 60.0) ? 0.0 : 6.50;
    std::cout << speseSpedizione << "\n";
    return 0;
}
```

</details>

1. **Promozione weekend**  
   Porta la soglia per lo sconto del 10% da `50.0` a `100.0`. Ricompila e
   osserva quale valore sceglie il ternario.

2. **Consegna express**  
   Aggiungi `bool consegnaRapida = true;`. Con un ternario assegna un
   supplemento di `3.00` se è vero, `0.0` altrimenti, poi sommalo alla spedizione.

3. **Pari o dispari**  
   Con `int articoli = 14;` stampa se il numero è pari o dispari:
   ```cpp
   std::cout << ((articoli % 2 == 0) ? "pari" : "dispari");
   ```

#### 5. MAKE (Crea)
**Scenario SIA — Commissione transazione POS**

Scrivi `commissioni_pos.cpp` per un esercente:

- `double importoPagamento` (es. `45.00`)
- `bool circuitoInternazionale` (`true` = Visa/MC estera, `false` = PagoBANCOMAT)
- **Regola con ternario:**
  - circuito internazionale → commissione **1,8%** (`0.018`)
  - altrimenti → **0,7%** (`0.007`)
- **Commissione minima:** se la commissione calcolata è `< 0.15`, applica comunque `0.15` (secondo ternario)
- Calcola e stampa l’**incasso netto** dell’esercente (`importo - commissioneFinale`)

**Requisiti:** commenti `///` sulle aliquote, output chiaro tipo scontrino;
aggiungi Doxygen solo se il programma supera circa 15 righe.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Calcolo commissione POS e incasso netto esercente.
 */
#include <iostream>

int main() {
    // dichiara importo, flag circuito, calcola commissione e netto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- Espressione = calcoli/confronti che producono **un** valore.
- Divisione tra soli `int` → risultato intero (trappola classica).
- Ternario: `condizione ? se_vero : se_falso` — ideale per scelte semplici che restituiscono un valore.
- Per decisioni lunghe o a più rami → nei prossimi capitoli useremo `if` / `else`.

---

### ➡️ Prossimo chunk
Finora le decisioni tengono in una riga.  
Quando la logica diventa un **bivio** (fare A oppure fare B, con più istruzioni per ramo), entra in scena il costrutto `if` / `else`.

---




## 🚦 Bivi e decisioni: scegliere con `if` e `if-else`

Un gestionale non esegue sempre la stessa azione. Un pagamento può essere
approvato o rifiutato; una scorta può essere sufficiente o sotto il minimo; un
badge può essere valido oppure no.

Con `if` e `if-else` insegni al programma a scegliere un percorso.

> 💡 **Metafora:** Immagina un tornello aziendale. La condizione è il lettore
> che controlla il badge; il blocco `if` è il passaggio verde quando la regola
> è vera; il blocco `else` è il passaggio rosso quando la regola è falsa. Con
> `if-else` passa un solo percorso, mai entrambi.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un `if` o un `if-else` con graffe per scegliere il ramo corretto in base a una condizione.

---

### ⚙️ Prima del laboratorio: i due modelli

Un `if` semplice esegue un blocco soltanto quando la condizione è vera:

```cpp
if (giacenza < 5) {
    std::cout << "Scorte in esaurimento\n";
}
```

Un `if-else` sceglie uno dei due blocchi:

```cpp
if (saldo >= importo) {
    std::cout << "Pagamento approvato\n";
} else {
    std::cout << "Fondi insufficienti\n";
}
```

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| Condizione | Un confronto che vale vero o falso | Decide il percorso |
| `if` | Ramo per il caso vero | Esegue l'azione consentita |
| `else` | Ramo per il caso falso | Gestisce l'alternativa |
| `{ }` | Confini del blocco | Tiene insieme tutte le istruzioni del ramo |

---

### 🧭 Prima del laboratorio: seguire il flusso

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi saldo e importo;
if (saldo >= importo?) then (vero)
  :Sottrai l'importo;
  :Mostra "Approvato";
else (falso)
  :Mostra "Negato";
endif
:Continua dopo il bivio;
stop
@enduml
```

Operatori utili per confrontare valori già noti:

| Operatore | Significato | Esempio |
| :---: | :--- | :--- |
| `>` | maggiore di | `scorte > 0` |
| `<` | minore di | `scorte < 5` |
| `==` | uguale a | `pinInserito == PIN_SEGRETO` |
| `>=` | maggiore o uguale | `saldo >= importo` |

Non confondere `==`, che confronta, con `=`, che assegna un valore.

---

### 🔬 Laboratorio PRIMM: autorizzazione di un pagamento POS

Il terminale deve decidere se il saldo disponibile basta per una spesa.

#### 1. PREDICT (Prevedi)

```cpp
double saldoDisponibile = 45.00;
double importoSpesa = 62.50;

if (saldoDisponibile >= importoSpesa) {
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
}
```

**Domanda 1**

Quale ramo viene eseguito con saldo `45.00` e spesa `62.50`?

[(X)] Il ramo `else`, perché il saldo non è sufficiente
[( )] Il ramo `if`, perché ogni pagamento viene approvato
[( )] Entrambi i rami, uno dopo l'altro

**Domanda 2**

Perché `saldoDisponibile >= importoSpesa` è una condizione utile per il POS?

[(X)] Confronta i due importi e produce vero solo quando il saldo basta
[( )] Somma automaticamente il saldo e la spesa
[( )] Trasforma i due importi in messaggi di testo

**Domanda 3**

Che cosa succede se saldo e importo valgono entrambi `45.00`?

[(X)] La condizione è vera perché `>=` include anche l'uguaglianza
[( )] La condizione è falsa perché due valori uguali non possono essere confrontati
[( )] Il programma esegue sempre il ramo `else` in caso di parità

**Domanda 4**

Perché le graffe sono importanti nell'esempio?

[(X)] Raggruppano tutte le istruzioni che appartengono a ciascun ramo
[( )] Servono solo a rendere il codice più colorato nell'editor
[( )] Sostituiscono la condizione tra parentesi

**Domanda 5**

Quale risultato produce un `if` semplice quando la condizione è falsa?

[(X)] Salta il suo blocco e continua con l'istruzione successiva
[( )] Esegue automaticamente il blocco `else`, anche se non esiste
[( )] Ripete la condizione finché diventa vera

#### 2. RUN (Esegui)

Digita il programma completo e confronta l'output con la tua previsione.

```cpp
/**
 * @file autorizzazione_pos.cpp
 * @brief Verifica se un pagamento può essere autorizzato.
 */
#include <iostream>

/**
 * @brief Controlla il saldo e comunica l'esito della transazione.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il saldo rappresenta il credito realmente disponibile sul conto.
    double saldoDisponibile = 45.00;
    /// L'importo è decimale perché un pagamento può avere centesimi.
    double importoSpesa = 62.50;

    std::cout << "=== TERMINALE PAGAMENTI POS ===\n";
    std::cout << "Importo richiesto: " << importoSpesa << " EUR\n";

    if (saldoDisponibile >= importoSpesa) {
        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << "TRANSAZIONE APPROVATA\n";
        std::cout << "Nuovo saldo: " << saldoDisponibile << " EUR\n";
    } else {
        std::cout << "TRANSAZIONE NEGATA\n";
        std::cout << "Credito insufficiente\n";
    }

    std::cout << "Operazione conclusa.\n";
    return 0;
}
```
@LIA.cpp

Con i valori iniziali la condizione è falsa, quindi compare
`TRANSAZIONE NEGATA`.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine delle istruzioni e spiega perché il saldo
non cambia nel caso negato.

```cpp
double saldoDisponibile = 45.00;
double importoSpesa = 62.50;

if (saldoDisponibile >= importoSpesa) {
    saldoDisponibile = saldoDisponibile - importoSpesa;
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
    std::cout << "Mancano " << importoSpesa - saldoDisponibile << " euro\n";
}
```

**Domanda 1**

Qual è il primo passaggio eseguito quando il programma arriva all'if?

[(X)] Confronta `saldoDisponibile` con `importoSpesa`
[( )] Sottrae sempre la spesa dal saldo
[( )] Esegue prima tutte le istruzioni dentro le graffe

**Domanda 2**

Perché il saldo non viene sottratto nel caso `45.00` contro `62.50`?

[(X)] La sottrazione si trova nel ramo `if`, che non viene eseguito quando la condizione è falsa
[( )] I numeri decimali non possono essere sottratti in C++
[( )] Il ramo `else` annulla sempre tutte le variabili del programma

**Domanda 3**

Quale valore viene calcolato dall'espressione `importoSpesa - saldoDisponibile`?

[(X)] `17.50`, cioè l'importo ancora mancante
[( )] `107.50`, perché i due importi vengono sommati
[( )] `-17.50`, perché il saldo viene sempre scritto per primo

**Domanda 4**

Perché, dopo il blocco `if-else`, il programma può eseguire altre istruzioni?

[(X)] Il bivio sceglie un ramo, poi il flusso continua dopo le graffe
[( )] Il programma esce da `main` ogni volta che incontra `else`
[( )] Le graffe trasformano il bivio in un ciclo

**Domanda 5**

Che cosa accade con questo codice? `if (saldoDisponibile >= importoSpesa); { std::cout << "Approvato"; }`

[(X)] Il punto e virgola chiude subito l'if, quindi il blocco successivo non è più controllato
[( )] Il punto e virgola rende la condizione più precisa
[( )] Il compilatore interpreta il punto e virgola come un ramo `else`

| Passo | Cosa osservi | Stato |
| :---: | :--- | :--- |
| 1 | Il programma confronta `45.00 >= 62.50` | `false` |
| 2 | Salta il blocco `if` | Nessuna sottrazione |
| 3 | Entra nel blocco `else` | Stampa transazione negata |
| 4 | Esce dal bivio | Stampa operazione conclusa |

La sottrazione è dentro il ramo `if`: viene eseguita soltanto quando il
confronto è vero. Le istruzioni dopo le graffe appartengono invece al flusso
comune e vengono eseguite dopo il ramo scelto.

Evita questo errore logico:

```cpp
if (saldoDisponibile >= importoSpesa);
{
    std::cout << "Approvato\n";
}
```

Il punto e virgola chiude subito l'`if`; il blocco successivo non è più
controllato dalla condizione. Il programma può compilare, ma il comportamento
non è quello desiderato.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva quale ramo
> viene attraversato.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
double saldoDisponibile = 45.00;
double importoSpesa = 62.50;

if (saldoDisponibile >= importoSpesa) {
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
}
```

**Domanda 1**

Quale modifica fa approvare la spesa di `62.50` con saldo `100.00`?

[(X)] Cambiare `saldoDisponibile` in `100.00`
[( )] Cambiare `>=` in `<=`
[( )] Spostare il messaggio "Negato" dentro il ramo `if`

**Domanda 2**

Quale modifica permette di mostrare anche il nuovo saldo dopo un pagamento approvato?

[(X)] Aggiungere una stampa nel ramo `if` dopo la sottrazione
[( )] Aggiungere la stampa nel ramo `else` prima del confronto
[( )] Sostituire `std::cout` con `std::cin`

**Domanda 3**

Che effetto ha cambiare `>=` in `>` quando saldo e spesa sono uguali?

[(X)] Il pagamento diventa negato, perché l'uguaglianza non soddisfa più la condizione
[( )] Il pagamento resta approvato perché i due operatori sono equivalenti
[( )] Il programma esegue entrambi i rami

**Domanda 4**

Quale modifica aggiunge un avviso per una scorta sotto cinque pezzi senza creare un secondo ramo obbligatorio?

[(X)] Aggiungere un secondo `if` semplice con condizione `scorte < 5`
[( )] Aggiungere sempre `else` al primo `if` del pagamento
[( )] Mettere la quantità dentro una stringa stampata

**Domanda 5**

Perché conviene modificare una sola condizione alla volta?

[(X)] Per capire quale cambiamento ha prodotto il nuovo ramo eseguito
[( )] Perché un programma C++ può contenere una sola condizione
[( )] Perché `if` funziona soltanto prima della prima modifica

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double saldoDisponibile = 45.00;
    double importoSpesa = 62.50;

    if (saldoDisponibile >= importoSpesa) {
        std::cout << "Approvato\n";
    } else {
        std::cout << "Negato\n";
    }

    return 0;
}
```

</details>

**Modifica A — pagamento approvato**

Cambia `saldoDisponibile` in `100.00`. Ricompila e verifica che venga eseguito
il ramo `if`.

**Modifica B — mostra il nuovo saldo**

Nel ramo `if`, sottrai l'importo e stampa `saldoDisponibile` dopo la
sottrazione. Non aggiungere la stampa nel ramo `else`.

**Modifica C — prova il caso di uguaglianza**

Imposta entrambi i valori a `45.00`. Prevedi il risultato: `>=` include anche
il caso in cui saldo e importo siano uguali.

#### 5. MAKE (Crea)

**Scenario aziendale:** il responsabile sicurezza deve controllare l'accesso
a un caveau aziendale.

Crea `controllo_caveau.cpp` rispettando tutti i requisiti:

1. Dichiara `const int PIN_SEGRETO = 4821`.
2. Dichiara `int pinInserito = 4821`.
3. Confronta i due valori con `==`.
4. Usa un solo `if-else` con graffe.
5. Se il PIN è corretto, stampa `ACCESSO CONSENTITO`.
6. Altrimenti, stampa `ACCESSO NEGATO`.
7. Inserisci un commento `///` che spieghi perché il PIN deve essere confrontato prima dell'accesso.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Controllo accessi a un caveau aziendale.
 */
#include <iostream>

int main() {
    const int PIN_SEGRETO = 4821;
    /// TODO: spiega perché il codice deve essere confrontato prima dell'accesso.
    // TODO: dichiara pinInserito e scrivi l'if-else.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `if` esegue un blocco solo quando la condizione è vera.
- `if-else` sceglie un solo ramo tra vero e falso.
- Usa sempre le graffe per rendere chiaro il blocco controllato.
- `==` confronta; `=` assegna.
- Non mettere `;` subito dopo la condizione.
- Dopo il ramo scelto, il flusso continua con le istruzioni successive.

---

### ➡️ Prossimo chunk

Quando le alternative diventano più di due, un solo bivio non basta. Nel
prossimo chunk userai catene `if / else if / else` per gestire fasce di
sconto e stati diversi di un ordine.


## 🌲 Scaglioni ordinati: `if`, `else if` ed `else`

Nel capitolo precedente hai imparato a scegliere tra due strade. Nei contesti
aziendali, però, le alternative possono essere più di due: fasce di sconto,
livelli di fido, classi di rischio o aliquote didattiche.

Una catena `if / else if / else` permette di controllare più fasce in ordine e
di sceglierne una sola.

> 💡 **Metafora:** Immagina un nastro di smistamento logistico. Ogni sensore
> controlla una soglia; il primo sensore che riconosce il pacco lo devia verso
> la sua corsia. I sensori successivi non vedono più quel pacco: per questo
> l'ordine delle soglie decide il risultato.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere una catena `if / else if / else` ordinata per classificare un dato in fasce esclusive.

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

```cpp
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
```

**Domanda 1**

Quale fascia viene scelta con `fatturato = 25000.0`?

[(X)] Gold, perché il fatturato non raggiunge 50000 ma supera 20000
[( )] Platinum, perché ogni valore positivo entra nella fascia più alta
[( )] Silver, perché il programma sceglie sempre l'ultima condizione vera

**Domanda 2**

Perché la soglia `50000.0` deve essere controllata prima di `20000.0`?

[(X)] Un fatturato di 60000 deve fermarsi nella fascia Platinum prima di raggiungere Gold
[( )] Le soglie più piccole non possono essere scritte dopo quelle grandi
[( )] Il compilatore esegue sempre le condizioni dall'alto verso il basso numerico

**Domanda 3**

Che cosa succede dopo che una condizione della catena risulta vera?

[(X)] Viene eseguito quel ramo e le condizioni successive vengono saltate
[( )] Vengono eseguiti anche tutti gli `else if` successivi
[( )] Il programma torna alla prima condizione per controllarla di nuovo

**Domanda 4**

Quale ruolo ha l'ultimo `else` nella scala?

[(X)] Gestisce il caso in cui nessuna soglia precedente sia stata raggiunta
[( )] Ripete il controllo della soglia più alta
[( )] Rende vere tutte le condizioni precedenti

**Domanda 5**

Perché le fasce di sconto sono un buon esempio di `else if`?

[(X)] Un cliente deve ricevere una sola fascia tra quelle definite
[( )] Ogni cliente deve ricevere tutti gli sconti contemporaneamente
[( )] Le fasce non hanno bisogno di confronti tra numeri

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

```cpp
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
```

**Domanda 1**

Qual è il primo confronto eseguito con `fatturato = 32500.0`?

[(X)] `32500.0 >= 50000.0`, che risulta falso
[( )] `32500.0 >= 5000.0`, perché è la soglia più vicina
[( )] Il programma confronta tutte le soglie nello stesso momento

**Domanda 2**

Perché il valore finale di `sconto` è `0.10`?

[(X)] La prima condizione è falsa e la seconda è vera, quindi il ramo Gold assegna 0.10
[( )] Tutte le percentuali vengono sommate e il risultato diventa 0.10
[( )] Il valore iniziale 0.0 viene trasformato automaticamente in 0.10

**Domanda 3**

Quale ordine di verifica è corretto per `fatturato = 32500.0`?

[(X)] Platinum falso → Gold vero → Silver e `else` saltati
[( )] Silver vero → Gold vero → Platinum falso
[( )] Gold vero → Silver vero → `else` eseguito

**Domanda 4**

Che cosa accade se il fatturato vale `3000.0`?

[(X)] Tutte le soglie sono false e viene eseguito l'ultimo `else`
[( )] Viene scelta Silver perché è la fascia più bassa
[( )] Il programma non esegue nessuna istruzione della catena, compreso `else`

**Domanda 5**

Perché mettere `fatturato >= 20000.0` prima di `fatturato >= 50000.0` crea un errore logico?

[(X)] Un fatturato di 60000 soddisfa subito 20000 e viene classificato Gold
[( )] Il compilatore rifiuta sempre le soglie scritte in ordine crescente
[( )] La condizione 50000 diventerebbe automaticamente falsa

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

```cpp
if (fatturato >= 50000.0) {
    fascia = "Platinum";
} else if (fatturato >= 20000.0) {
    fascia = "Gold";
} else {
    fascia = "Nessuna";
}
```

**Domanda 1**

Quale modifica aggiunge una fascia Diamond per fatturati da `100000.0` in su?

[(X)] Inserire un nuovo `if (fatturato >= 100000.0)` prima del controllo Platinum
[( )] Aggiungere Diamond dopo l'ultimo `else`
[( )] Sostituire `else if` con un secondo `else`

**Domanda 2**

Che effetto ha mettere il controllo `>= 20000.0` prima di `>= 50000.0`?

[(X)] I valori da 50000 in su vengono intercettati troppo presto e classificati Gold
[( )] Le due fasce vengono assegnate insieme
[( )] Il programma corregge automaticamente l'ordine

**Domanda 3**

Quale modifica assegna Silver anche al valore esattamente uguale a `5000.0`?

[(X)] Usare `fatturato >= 5000.0` nella condizione Silver
[( )] Usare `fatturato > 5000.0` nella condizione Silver
[( )] Spostare Silver nel ramo `else` senza una condizione

**Domanda 4**

Quale modifica calcola l'importo dello sconto dopo aver scelto la fascia?

[(X)] Moltiplicare il fatturato per `sconto` dopo la catena
[( )] Moltiplicare ogni soglia prima di sapere quale ramo è vero
[( )] Usare `std::cin` al posto della variabile `sconto`

**Domanda 5**

Perché conviene modificare una soglia alla volta?

[(X)] Per capire quale cambiamento ha alterato la classificazione ai confini
[( )] Perché una catena può contenere una sola soglia in assoluto
[( )] Perché `else if` funziona soltanto con valori non decimali

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
3. Usa queste fasce didattiche con aliquota unica:
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
 * @brief Stima un'imposta con scaglioni didattici.
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

- `if / else if / else` classifica un dato in alternative esclusive.
- La catena si ferma al primo ramo vero.
- Con soglie `>=`, ordina i controlli dalla soglia più alta alla più bassa.
- L'ultimo `else` gestisce tutti i valori rimasti.
- Testa sempre i confini: esattamente soglia, appena sotto e appena sopra.

---

### ➡️ Prossimo chunk

Quando la decisione dipende da un valore discreto, come un codice menu o uno
stato numerico, una lunga catena può diventare difficile da leggere. Nel
prossimo chunk userai `switch` per organizzare questi casi.


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

```cpp
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
```

**Domanda 1**

Quale `case` viene selezionato con `sceltaMenu = 2`?

[(X)] `case 2`, perché il valore coincide con la sua costante
[( )] `case 1`, perché è il primo caso scritto
[( )] `default`, perché ogni scelta deve passare dall'alternativa finale

**Domanda 2**

Perché `break` è importante dopo il messaggio del `case 2`?

[(X)] Ferma lo switch e impedisce di eseguire i case successivi
[( )] Rende uguale il valore di tutti i case
[( )] Fa ripartire lo switch dal primo case

**Domanda 3**

Che cosa stampa il frammento se `sceltaMenu = 7`?

[(X)] Il messaggio del ramo `default`
[( )] Il messaggio del `case 1`, perché 7 è maggiore di 1
[( )] Tutti i messaggi dei case in ordine

**Domanda 4**

Per quale tipo di dato è adatto questo `switch`?

[(X)] Un codice discreto come un `int` o un `char`
[( )] Un intervallo continuo come un prezzo `double`
[( )] Una frase completa contenuta in `std::string`

**Domanda 5**

Che cosa può accadere se togli il `break` da `case 2`?

[(X)] L'esecuzione può continuare nel `case` successivo: è il fall-through
[( )] Il programma torna automaticamente a `case 1`
[( )] Il compilatore cancella il messaggio del `case 2`

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

```cpp
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
```

**Domanda 1**

Qual è il primo passaggio eseguito quando il programma arriva allo `switch`?

[(X)] Confronta il valore di `sceltaMenu` con i valori dei `case`
[( )] Esegue sempre il primo blocco e poi cerca il valore
[( )] Esegue prima `default` come controllo di sicurezza

**Domanda 2**

Perché con `sceltaMenu = 2` non viene eseguito `case 3`?

[(X)] Il `break` di `case 2` fa uscire dallo switch
[( )] I case successivi vengono ignorati perché hanno sempre numeri maggiori
[( )] Il programma esegue solo i case che contengono numeri pari

**Domanda 3**

Che cosa succede senza `break` alla fine di `case 2`?

[(X)] Dopo il messaggio di `case 2`, l'esecuzione continua nel case successivo
[( )] Il programma si ferma sempre con un errore di compilazione
[( )] Viene eseguito soltanto `default`

**Domanda 4**

Perché `default` non viene eseguito con `sceltaMenu = 2`?

[(X)] Esiste già un case corrispondente e il suo `break` chiude lo switch
[( )] `default` funziona soltanto con valori negativi
[( )] Il compilatore elimina sempre `default` quando ci sono tre case

**Domanda 5**

Perché `double sceltaMenu = 2.0;` non è adatto come espressione dello switch?

[(X)] Lo switch richiede un valore intero o carattere, non un numero decimale
[( )] Un double può essere usato solo per stampare prezzi
[( )] I numeri con decimali non possono essere assegnati a variabili

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

```cpp
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
```

**Domanda 1**

Quale modifica aggiunge una voce per la visualizzazione del saldo?

[(X)] Aggiungere `case 3`, stampare il messaggio e chiudere con `break`
[( )] Aggiungere `default 3:` dopo il case 2
[( )] Cambiare `switch` in `std::cout`

**Domanda 2**

Quale modifica fa eseguire lo stesso messaggio sia con codice `0` sia con codice `9`?

[(X)] Scrivere `case 0:` seguito da `case 9:` prima delle stesse istruzioni
[( )] Scrivere `case 0 || 9:` come se fosse una condizione booleana
[( )] Duplicare `default` due volte

**Domanda 3**

Che effetto ha aggiungere `break` dopo `default`?

[(X)] Rende esplicita l'uscita dallo switch anche quando nessun case coincide
[( )] Fa eseguire di nuovo il case precedente
[( )] Trasforma `default` in un ciclo

**Domanda 4**

Quale modifica mantiene il prezzo di una ricarica con i centesimi?

[(X)] Usare una variabile `double` per l'importo dentro il case, senza usarla come scelta
[( )] Usare un `double` come espressione dello switch
[( )] Memorizzare l'importo nel nome del `case`

**Domanda 5**

Perché conviene modificare un case alla volta?

[(X)] Per distinguere quale case o break ha cambiato il percorso del menu
[( )] Perché uno switch può contenere un solo case in assoluto
[( )] Perché `break` funziona solo nel primo case scritto

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

```cpp
int n = 0;

while (n > 5) {
    std::cout << "Elaborazione\n";
    n = n + 1;
}
```

**Domanda 1**

Quante volte viene stampata la parola `Elaborazione`?

[(X)] Zero volte, perché la condizione `0 > 5` è falsa già all'inizio
[( )] Una volta, perché ogni `while` esegue almeno un giro
[( )] Cinque volte, perché il ciclo arriva fino a 5

**Domanda 2**

Perché il corpo del `while` non viene eseguito in questo esempio?

[(X)] Il `while` controlla la condizione prima di entrare nel corpo
[( )] La stampa dentro il ciclo è vietata
[( )] La variabile `n` viene automaticamente cancellata

**Domanda 3**

Quale ruolo ha `n = n + 1;` dentro il ciclo?

[(X)] Fa evolvere la variabile che può rendere falsa la condizione
[( )] Riporta sempre `n` al valore iniziale
[( )] Decide da sola quale testo stampare

**Domanda 4**

Quale elemento serve per fermare un ciclo che legge articoli fino a `0`?

[(X)] Un valore sentinella e una condizione che lo riconosce
[( )] Un `switch` dentro ogni iterazione
[( )] Una costante che deve essere sempre uguale a 1

**Domanda 5**

Perché un `while` può eseguire zero iterazioni?

[(X)] La condizione può essere falsa prima del primo ingresso nel corpo
[( )] Il compilatore sceglie casualmente se saltare il primo giro
[( )] Un ciclo esegue il corpo solo quando contiene `std::cin`

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

```cpp
double totaleSpesa = 0.0;
int numeroArticoli = 0;
double prezzoArticolo = 12.50;

while (prezzoArticolo != 0.0) {
    totaleSpesa = totaleSpesa + prezzoArticolo;
    numeroArticoli = numeroArticoli + 1;
    prezzoArticolo = 0.0;
}
```

**Domanda 1**

Quale condizione permette al ciclo di entrare nel corpo al primo controllo?

[(X)] `12.50 != 0.0`, che è vera
[( )] `0.0 != 12.50`, che viene controllata dopo il corpo
[( )] La condizione non viene controllata al primo giro

**Domanda 2**

Perché dopo il giro il totale vale `12.50`?

[(X)] Il prezzo viene sommato prima che la variabile sia aggiornata a `0.0`
[( )] Il ciclo aggiunge sempre due volte il primo prezzo
[( )] La sentinella `0.0` viene conteggiata come prezzo

**Domanda 3**

Perché il secondo controllo non entra nel corpo?

[(X)] L'aggiornamento porta `prezzoArticolo` alla sentinella e rende falsa la condizione
[( )] Il ciclo si ferma dopo un giro indipendentemente dalla condizione
[( )] Il totale non può essere aggiornato più di una volta

**Domanda 4**

Quale valore non deve essere sommato in un ciclo con sentinella `0.0`?

[(X)] La sentinella `0.0`, perché serve solo a indicare la fine
[( )] Ogni prezzo maggiore di zero
[( )] Il primo prezzo valido inserito

**Domanda 5**

Che cosa rischi se rimuovi l'aggiornamento di `prezzoArticolo`?

[(X)] La condizione può restare vera e il ciclo può diventare infinito
[( )] Il ciclo esegue automaticamente il ramo `else`
[( )] La variabile diventa subito uguale alla sentinella

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

```cpp
double prezzoArticolo = 12.50;
double totaleSpesa = 0.0;

while (prezzoArticolo != 0.0) {
    totaleSpesa = totaleSpesa + prezzoArticolo;
    std::cin >> prezzoArticolo;
}
```

**Domanda 1**

Quale modifica permette di contare anche il numero degli articoli?

[(X)] Dichiarare un contatore e incrementarlo dentro il corpo, prima della nuova lettura
[( )] Aggiungere il contatore dopo il ciclo senza aggiornarlo
[( )] Sostituire `while` con `switch`

**Domanda 2**

Dove devi inserire la nuova lettura se vuoi continuare a chiedere prezzi?

[(X)] Nel corpo del ciclo, così la condizione può cambiare al giro successivo
[( )] Solo prima del `while`, perché il corpo non può leggere dati
[( )] Dopo `return 0`, quando il programma è già terminato

**Domanda 3**

Che cosa succede se cambi la sentinella da `0.0` a `-1.0`?

[(X)] Il ciclo continua finché il prezzo non diventa `-1.0`, che non viene sommato
[( )] Il ciclo termina sempre dopo il primo prezzo positivo
[( )] Il valore `-1.0` viene automaticamente trasformato in `0.0`

**Domanda 4**

Quale modifica evita di sommare un prezzo negativo ma permette di continuare?

[(X)] Aggiungere un controllo nel corpo e aggiornare comunque il prossimo prezzo
[( )] Usare `-1.0` come totale iniziale
[( )] Mettere la lettura del prezzo fuori da `main`

**Domanda 5**

Perché conviene modificare una sola parte del ciclo alla volta?

[(X)] Per distinguere se l'errore riguarda condizione, corpo o aggiornamento
[( )] Perché un `while` può contenere una sola istruzione
[( )] Perché il compilatore impedisce di cambiare due righe consecutive

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


## ⏳ Il contatore compatto: ripetere con il ciclo `for`

Il `while` è utile quando non sai in anticipo quanti giri farai, come nel
registro delle fatture che termina con una sentinella. In azienda, però, molte
ripetizioni sono già note: dodici mesi, cinque anni di ammortamento, ventiquattro
rate.

Il ciclo `for` raccoglie in una sola riga inizializzazione, condizione e
aggiornamento del contatore.

> 💡 **Metafora:** Immagina il timer di una macchina industriale. Imposti:
> “parti da 1, fermati a 5, avanza di 1 a ogni scatto”. La macchina ripete il
> lavoro senza che tu debba ricordarti di aggiornare manualmente il contatore.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un `for` per ripetere un calcolo un numero noto di volte.

---

### ⚙️ Prima del laboratorio: `for` e `while`

Questi due cicli possono esprimere la stessa logica:

```cpp
int anno = 1;
while (anno <= 5) {
    std::cout << anno << "\n";
    anno = anno + 1;
}

for (int anno = 1; anno <= 5; ++anno) {
    std::cout << anno << "\n";
}
```

| Parte del `for` | Ruolo | Quando avviene |
| :--- | :--- | :--- |
| `int anno = 1` | Inizializzazione | Una volta, prima del primo controllo |
| `anno <= 5` | Condizione | Prima di ogni iterazione |
| `++anno` | Aggiornamento | Dopo il corpo di ogni iterazione |

---

### 🧭 Prima del laboratorio: il timer dei periodi

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Inizializza il contatore;
while (Condizione vera?) is (sì)
  :Esegui il corpo;
  :Aggiorna il contatore;
endwhile (no)
:Continua dopo il ciclo;
stop
@enduml
```

Con `for (int anno = 1; anno <= 5; ++anno)`:

| Iterazione | Valore usato nel corpo |
| :---: | :---: |
| 1 | `1` |
| 2 | `2` |
| 3 | `3` |
| 4 | `4` |
| 5 | `5` |

Quando il contatore diventa `6`, la condizione `anno <= 5` è falsa e il corpo
non viene più eseguito.

---

### 🔬 Laboratorio PRIMM: piano di ammortamento

Un'azienda distribuisce il costo di un cespite in cinque quote annuali uguali.

#### 1. PREDICT (Prevedi)

```cpp
for (int i = 0; i < 5; ++i) {
    std::cout << i << "\n";
}
```

**Domanda 1**

Quali valori vengono stampati dal ciclo?

[(X)] `0, 1, 2, 3, 4`, perché il ciclo si ferma prima di 5
[( )] `1, 2, 3, 4, 5`, perché il contatore parte sempre da 1
[( )] `0, 1, 2, 3`, perché il ciclo esegue quattro giri

**Domanda 2**

Quante volte viene eseguito il corpo del `for`?

[(X)] Cinque volte, per i valori da 0 a 4
[( )] Sei volte, perché il valore 5 viene incluso
[( )] Una sola volta, perché `i` viene dichiarata nell'intestazione

**Domanda 3**

Perché la condizione è `i < 5` e non `i <= 5` se vuoi cinque iterazioni?

[(X)] Con `i < 5` i valori validi sono 0, 1, 2, 3 e 4
[( )] Perché `<=` non può mai essere usato in un ciclo
[( )] Perché il contatore viene aggiornato prima del primo giro

**Domanda 4**

Quale ruolo ha `++i` nell'intestazione?

[(X)] Aumenta il contatore dopo ogni esecuzione del corpo
[( )] Imposta `i` a zero prima di ogni giro
[( )] Decide quale testo deve stampare `std::cout`

**Domanda 5**

Perché un `for` è adatto a dodici mesi di un report?

[(X)] Il numero di ripetizioni è noto e il contatore può avanzare da 1 a 12
[( )] Un `for` è obbligatorio ogni volta che si usano numeri interi
[( )] Il `for` serve soltanto per leggere dati fino a una sentinella

#### 2. RUN (Esegui)

Digita il programma completo e osserva una riga per ogni anno.

```cpp
/**
 * @file ammortamento_cespite.cpp
 * @brief Calcola un piano di ammortamento a quote costanti.
 */
#include <iostream>

/**
 * @brief Stampa quota annuale e valore residuo di un cespite.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il costo è la base economica da distribuire negli anni.
    const double COSTO_CESPITE = 10000.0;
    /// Il numero di anni è noto prima di iniziare il piano.
    const int NUMERO_ANNI = 5;
    /// La quota costante rende confrontabili gli anni del piano.
    const double QUOTA_ANNUA = COSTO_CESPITE / NUMERO_ANNI;
    double valoreResiduo = COSTO_CESPITE;

    std::cout << "Anno  Quota  Residuo\n";

    for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
        valoreResiduo = valoreResiduo - QUOTA_ANNUA;
        std::cout << anno << "     " << QUOTA_ANNUA
                  << "    " << valoreResiduo << "\n";
    }

    return 0;
}
```
@LIA.cpp

Il programma stampa cinque righe. Nell'ultima, il valore residuo arriva a
`0.0`.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine tra contatore, quota e residuo.

```cpp
const int NUMERO_ANNI = 5;
double valoreResiduo = 10000.0;
const double QUOTA_ANNUA = 2000.0;

for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
    valoreResiduo = valoreResiduo - QUOTA_ANNUA;
}
```

**Domanda 1**

Quando viene eseguita l'inizializzazione `int anno = 1`?

[(X)] Una sola volta, prima del primo controllo della condizione
[( )] Dopo ogni iterazione, per riportare l'anno a 1
[( )] Solo quando il valore residuo diventa zero

**Domanda 2**

Quale sequenza descrive correttamente un giro del `for`?

[(X)] Controllo condizione → corpo → aggiornamento del contatore
[( )] Corpo → inizializzazione → condizione → aggiornamento
[( )] Aggiornamento → corpo → condizione, senza controllo iniziale

**Domanda 3**

Perché dopo cinque iterazioni `valoreResiduo` vale `0.0`?

[(X)] Ogni giro sottrae 2000 dal valore iniziale di 10000
[( )] Il `for` azzera automaticamente tutte le variabili alla fine
[( )] La costante `QUOTA_ANNUA` viene sottratta due volte al primo giro

**Domanda 4**

Che cosa succede quando `anno` diventa `6`?

[(X)] La condizione `anno <= 5` è falsa e il ciclo termina
[( )] Il corpo viene eseguito ancora una volta per il valore finale
[( )] Il contatore torna automaticamente a 1

**Domanda 5**

Perché il numero di iterazioni è prevedibile in `for (int anno = 1; anno <= 5; ++anno)`?

[(X)] Inizializzazione, limite e aggiornamento definiscono un percorso chiuso
[( )] Il compilatore conta le righe stampate invece dei valori di `anno`
[( )] Il ciclo termina quando una variabile decimale diventa negativa

| Anno | Quota sottratta | Residuo dopo il giro |
| :---: | :---: | :---: |
| 1 | `2000` | `8000` |
| 2 | `2000` | `6000` |
| 3 | `2000` | `4000` |
| 4 | `2000` | `2000` |
| 5 | `2000` | `0` |

L'inizializzazione di `anno` avviene una sola volta. Dopo ogni riga del corpo
viene eseguito `++anno`; solo allora il programma verifica se può fare un altro
giro.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva `anno` e
> `valoreResiduo` dopo ogni iterazione.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
for (int anno = 1; anno <= 5; ++anno) {
    std::cout << anno << "\n";
}
```

**Domanda 1**

Quale modifica stampa dodici mesi invece di cinque anni?

[(X)] Sostituire il limite `5` con `12` mantenendo `anno = 1` e `++anno`
[( )] Cambiare `++anno` in `--anno`
[( )] Spostare `anno = 1` dentro il corpo

**Domanda 2**

Quale modifica fa partire il conteggio da 0 e arrivare fino a 4?

[(X)] Usare `int anno = 0; anno < 5; ++anno`
[( )] Usare `int anno = 1; anno <= 4; --anno`
[( )] Usare `int anno = 5; anno < 0; ++anno`

**Domanda 3**

Che effetto ha cambiare `anno <= 5` in `anno < 5` in un ciclo che parte da 1?

[(X)] Il ciclo esegue gli anni da 1 a 4, quindi una iterazione in meno
[( )] Il ciclo esegue gli anni da 1 a 5 come prima
[( )] Il ciclo parte da zero senza modificare l'inizializzazione

**Domanda 4**

Quale modifica permette un conto alla rovescia da 5 a 1?

[(X)] Usare `int anno = 5; anno >= 1; --anno`
[( )] Usare `int anno = 1; anno <= 5; ++anno`
[( )] Usare `int anno = 5; anno <= 1; ++anno`

**Domanda 5**

Perché conviene modificare una sola parte dell'intestazione alla volta?

[(X)] Per capire se il risultato è cambiato per inizializzazione, condizione o aggiornamento
[( )] Perché un `for` può contenere una sola modifica in tutto il programma
[( )] Perché il corpo del ciclo non può essere eseguito dopo una modifica

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
    valoreResiduo = valoreResiduo - QUOTA_ANNUA;
}
```

</details>

**Modifica A — aggiungi il fondo ammortamento**

Dichiara `double fondo = 0.0` prima del ciclo. A ogni giro aggiungi
`QUOTA_ANNUA` al fondo e stampalo insieme al residuo.

**Modifica B — usa dodici periodi**

Imposta `NUMERO_ANNI` a `12` e interpreta ogni iterazione come un mese.
Verifica che il ciclo produca esattamente dodici righe.

**Modifica C — conto alla rovescia**

Sostituisci l'intestazione con:

```cpp
for (int periodo = NUMERO_ANNI; periodo >= 1; --periodo)
```

Adatta la stampa in modo che il numero del periodo sia comprensibile.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio finanziario simula la capitalizzazione
composta di un deposito aziendale.

Crea `interesse_composto.cpp` rispettando tutti i requisiti:

1. Dichiara `double capitale = 10000.00`.
2. Dichiara `const double TASSO = 0.04`.
3. Dichiara `const int ANNI = 6`.
4. Usa un `for` da `1` a `ANNI`.
5. A ogni giro calcola `interessi = capitale * TASSO`.
6. Aggiorna `capitale` aggiungendo gli interessi.
7. Stampa anno, interessi e nuovo capitale.
8. Stampa il guadagno netto finale rispetto a `10000.00`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Simula la capitalizzazione composta su un deposito aziendale.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché il tasso resta costante nella simulazione.
    // TODO: dichiara capitale, tasso, anni e scrivi il for.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Usa `for` quando il numero di ripetizioni è noto.
- L'intestazione contiene inizializzazione, condizione e aggiornamento.
- La condizione viene controllata prima di ogni iterazione.
- Con `<` il valore limite non viene incluso; con `<=` può essere incluso.
- Per dati a sentinella e numero di giri sconosciuto resta adatto il `while`.

---

### ➡️ Prossimo chunk

A volte il corpo deve essere eseguito almeno una volta, per esempio quando
chiedi un dato prima di poter controllare se è valido. Nel prossimo capitolo
userai il ciclo `do-while`, con il controllo in coda.


## 🔁 Garantire l'azione: validare con il ciclo `do-while`

Il `while` e il `for` controllano la condizione prima di entrare nel corpo.
A volte, però, devi compiere un'azione almeno una volta prima di poterla
controllare: mostrare un modulo, chiedere un importo o leggere un PIN.

Il `do-while` serve proprio a questo: esegue il corpo e controlla la condizione
alla fine.

> 💡 **Metafora:** Immagina un modulo online con campi obbligatori. Prima devi
> visualizzarlo e compilare una risposta; solo dopo puoi premere “Invia” e
> controllare se i dati sono validi. Se c'è un errore, il modulo torna indietro
> e lo compili di nuovo.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un `do-while` per validare un input che deve essere richiesto almeno una volta.

---

### ⚙️ Prima del laboratorio: controllo in coda

```cpp
double importo;

do {
    std::cout << "Importo (> 0): ";
    std::cin >> importo;
} while (importo <= 0.0);
```

| Costrutto | Quando controlla? | Iterazioni minime |
| :--- | :--- | :---: |
| `while` | Prima del corpo | 0 |
| `for` | Prima del corpo | 0 |
| `do-while` | Dopo il corpo | 1 |

Il punto e virgola dopo `while (importo <= 0.0);` è obbligatorio: chiude la
struttura completa del `do-while`.

---

### 🧭 Prima del laboratorio: il modulo e la verifica

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Mostra la richiesta;
:Leggi il dato;
while (Dato ancora non valido?) is (sì)
  :Mostra errore;
  :Leggi un nuovo dato;
endwhile (no)
:Accetta il dato;
stop
@enduml
```

Per un importo ammesso tra `1.0` e `5000.0`, il ciclo deve continuare quando
l'importo è troppo piccolo **oppure** troppo grande:

```cpp
importo < MIN_BONIFICO || importo > MAX_BONIFICO
```

Quando entrambe le condizioni di errore sono false, l'importo è valido e il
programma esce.

---

### 🔬 Laboratorio PRIMM: validazione di un bonifico

L'ufficio pagamenti deve accettare un bonifico solo se l'importo è compreso
nell'intervallo ammesso.

#### 1. PREDICT (Prevedi)

```cpp
int n = 10;

do {
    std::cout << "giro\n";
    n = n + 1;
} while (n < 5);
```

**Domanda 1**

Quante volte viene eseguito il corpo?

[(X)] Una volta, perché il corpo viene eseguito prima del controllo
[( )] Zero volte, perché `10 < 5` è falso
[( )] Cinque volte, perché il ciclo arriva fino a 5

**Domanda 2**

Perché il `do-while` è utile per chiedere un dato valido?

[(X)] Permette di chiedere il dato almeno una volta prima di controllarlo
[( )] Impedisce all'utente di inserire più di un valore
[( )] Controlla sempre la condizione prima della prima lettura

**Domanda 3**

Dove viene controllata la condizione nel `do-while`?

[(X)] Dopo il corpo del ciclo
[( )] Prima del corpo, come nel `while`
[( )] Solo quando il programma arriva a `return 0`

**Domanda 4**

Quale elemento sintattico chiude il `do-while`?

[(X)] Il punto e virgola dopo `while (condizione)`
[( )] Un secondo `else` dopo la condizione
[( )] La parola `break` obbligatoria fuori dalle graffe

**Domanda 5**

Quale situazione richiede più naturalmente un `do-while` che un `while`?

[(X)] Un modulo che deve essere mostrato e compilato almeno una volta
[( )] Un conteggio noto da 1 a 12
[( )] Una classificazione tra fasce di fatturato

#### 2. RUN (Esegui)

Digita il programma completo. Prova con `-10`, poi `0`, infine `250`.

```cpp
/**
 * @file valida_bonifico.cpp
 * @brief Richiede un importo finché non rientra nel range ammesso.
 */
#include <iostream>

/**
 * @brief Valida un importo compreso tra uno e cinquemila euro.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il limite minimo impedisce bonifici nulli o negativi.
    const double MIN_BONIFICO = 1.0;
    /// Il limite massimo mantiene il controllo entro la procedura aziendale.
    const double MAX_BONIFICO = 5000.0;
    double importo = 0.0;

    do {
        std::cout << "Importo bonifico: ";
        std::cin >> importo;
        if (importo < MIN_BONIFICO || importo > MAX_BONIFICO) {
            std::cout << "Importo non valido. Riprova.\n";
        }
    } while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);

    std::cout << "Bonifico accettato: " << importo << " EUR\n";
    return 0;
}
```
@LIA.cpp

Il corpo viene eseguito almeno una volta. Con `250`, il controllo finale è
falso e il programma stampa il messaggio di accettazione.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci il percorso di ogni tentativo.

```cpp
const double MIN_BONIFICO = 1.0;
const double MAX_BONIFICO = 5000.0;
double importo = 0.0;

do {
    std::cin >> importo;
} while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);
```

**Domanda 1**

Qual è il primo passaggio eseguito dal programma?

[(X)] Legge un importo dentro il corpo del `do`
[( )] Controlla subito se `importo` è già valido
[( )] Confronta prima le due costanti tra loro

**Domanda 2**

Perché con input `250` il ciclo termina dopo il primo giro?

[(X)] 250 non è minore di 1 e non è maggiore di 5000, quindi la condizione è falsa
[( )] Il primo valore inserito viene sempre considerato valido
[( )] Il `do-while` termina quando incontra un numero pari

**Domanda 3**

Che cosa succede con input `-10` seguito da `250`?

[(X)] Il primo valore mantiene la condizione vera, quindi il programma ripete la lettura e poi accetta 250
[( )] Il programma accetta subito -10 perché è un numero inserito
[( )] Il programma esegue il corpo solo una volta e ignora 250

**Domanda 4**

Perché l'operatore `||` mantiene il ciclo per un importo fuori intervallo?

[(X)] Basta che sia vera una delle due condizioni di errore: troppo piccolo o troppo grande
[( )] Richiede che l'importo sia contemporaneamente minore e maggiore
[( )] Converte l'importo in un valore booleano senza confrontarlo

**Domanda 5**

Che errore sintattico può nascere se togli il `;` dopo `while (...)`?

[(X)] Il compilatore segnala che manca il punto e virgola prima dell'istruzione successiva
[( )] Il ciclo diventa automaticamente un `while` con controllo in testa
[( )] Il programma accetta tutti gli importi senza controllarli

| Giro | `importo` | Condizione di errore | Azione |
| :---: | :---: | :---: | :--- |
| 1 | `-10` | vera | Mostra errore e ripete |
| 2 | `0` | vera | Mostra errore e ripete |
| 3 | `250` | falsa | Esce e accetta |

Il controllo arriva dopo la lettura: per questo il primo tentativo esiste anche
se il valore iniziale fosse già fuori intervallo.

Se togli il punto e virgola finale, il compilatore può segnalare un errore
simile a:

```text
error: expected ';' before 'return'
```

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva il primo
> tentativo garantito.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
double importo = 0.0;

do {
    std::cin >> importo;
} while (importo <= 0.0);
```

**Domanda 1**

Quale modifica restringe l'intervallo agli importi tra 10 e 1000?

[(X)] Usare `importo < 10.0 || importo > 1000.0` nella condizione
[( )] Usare `importo > 10.0 || importo < 1000.0`
[( )] Sostituire la condizione con `importo == 10.0`

**Domanda 2**

Quale modifica permette al PIN di essere provato al massimo tre volte?

[(X)] Aggiungere un contatore e continuare finché PIN errato e tentativi minori di 3
[( )] Rimuovere il controllo del PIN e usare solo `break`
[( )] Inserire tre `do` uno dentro l'altro senza contatore

**Domanda 3**

Che effetto ha cambiare `importo <= 0.0` in `importo < 0.0`?

[(X)] L'importo 0.0 viene accettato, perché non è minore di zero
[( )] L'importo 0.0 viene sempre rifiutato come prima
[( )] Il ciclo non esegue più il primo giro

**Domanda 4**

Quale modifica mantiene il messaggio di errore solo per valori non validi?

[(X)] Mettere un `if` nel corpo che controlla lo stesso intervallo
[( )] Mettere il messaggio dopo `return 0`
[( )] Sostituire `std::cin` con `std::cout` nel corpo

**Domanda 5**

Perché conviene modificare una sola parte del ciclo alla volta?

[(X)] Per capire se il problema riguarda il corpo, la condizione o il punto e virgola finale
[( )] Perché un `do-while` può contenere una sola lettura in assoluto
[( )] Perché ogni modifica elimina la prima iterazione

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
do {
    std::cin >> importo;
} while (importo <= 0.0);
```

</details>

**Modifica A — restringi l'intervallo**

Cambia l'intervallo ammesso da `[1, 5000]` a `[10, 1000]`. Aggiorna entrambe
le condizioni necessarie.

**Modifica B — prova un valore valido al primo tentativo**

Inserisci subito `250`. Verifica che il corpo giri una volta e che il controllo
permetta immediatamente l'uscita.

**Modifica C — osserva la sintassi**

Rimuovi temporaneamente il punto e virgola dopo la condizione finale, compila e
leggi il messaggio del compilatore. Poi ripristinalo.

#### 5. MAKE (Crea)

**Scenario aziendale:** uno sportello deve verificare un PIN prima di
permettere l'accesso, limitando i tentativi per sicurezza.

Crea `pin_sportello.cpp` rispettando tutti i requisiti:

1. Dichiara `const int PIN_CORRETTO = 4821`.
2. Dichiara un `int pinInserito` e un contatore dei tentativi.
3. Chiedi il PIN almeno una volta con un `do-while`.
4. Continua se il PIN è errato e i tentativi sono minori di `3`.
5. Se il PIN è corretto entro tre prove, stampa `Accesso consentito`.
6. Dopo tre errori, stampa `Carta bloccata`.
7. Non rivelare il PIN corretto nei messaggi di errore.
8. Inserisci un commento `///` che spieghi perché il numero di tentativi è limitato.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Validazione PIN sportello con massimo tre tentativi.
 */
#include <iostream>

int main() {
    const int PIN_CORRETTO = 4821;
    /// TODO: spiega perché i tentativi devono essere limitati.
    // TODO: dichiara PIN e contatore, poi scrivi il do-while.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `do-while` esegue il corpo e poi controlla la condizione.
- Il corpo viene eseguito almeno una volta.
- È adatto alla validazione di input e ai menu che devono apparire subito.
- Dopo `while (condizione)` del `do-while` serve `;`.
- Usa `while` o `for` quando zero iterazioni è un caso accettabile.

---

### ➡️ Prossimo chunk

Ora conosci i tre cicli fondamentali. Nel prossimo capitolo userai `break` e
`continue` per guidare con maggiore precisione il flusso dentro un ciclo.


## ⏹️ Uscite Anticipate: `break` e `continue` nei cicli

> "Non tutte le iterazioni vanno completate: a volte si salta, a volte si chiude il banco."  
> — *Controllo operativo dei processi*

Nei cicli a volte serve **interrompere tutto** (`break`) o **saltare solo il giro corrente** (`continue`).  
Sono il cruscotto fine del programmatore: da usare con chiarezza, non per nascondere logica confusa.

> 💡 **Metafora: nastro di controllo fatture**  
> - **`continue`** = “questa fattura è a zero: **saltala**, passa alla successiva”  
> - **`break`** = “importo anomalo: **ferma** l’intero controllo e segnala”

In questo chunk **non** trattiamo la formattazione monetari (`iomanip`): ha un capitolo dedicato.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Usare `break` e `continue` in un `for`/`while` con intento chiaro
- Prevedere l’output di un ciclo che li combina

---

### ⚙️ In breve

| Parola | Effetto |
|--------|---------|
| `continue` | Salta al **prossimo** giro del ciclo più interno |
| `break` | Esce **subito** dal ciclo più interno |

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;  // non stampare 2
    if (i == 4) break;     // stop prima di 4,5
    std::cout << i;
}
// stampa: 13
```

---

### 🔬 Laboratorio PRIMM: Controllo scarti

#### 1. PREDICT (Prevedi)

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

Cosa stampa il ciclo?

[( )] 12345
[( )] 1345
[(X)] 13
[( )] 1234

<details>
<summary>💡 Spiegazione</summary>
<code>i==2</code> → <code>continue</code> (niente stampa). <code>i==3</code> stampa. <code>i==4</code> → <code>break</code> (il 5 non si raggiunge). Resta <code>13</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scarti_ciclo.cpp
 * @brief continue salta, break interrompe.
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

| `i` | Azione | Output accumulato |
|-----|--------|-------------------|
| 1 | stampa | `1` |
| 2 | `continue` | `1` |
| 3 | stampa | `13` |
| 4 | `break` | fine |

#### 4. MODIFY (Modifica)
1. Inverti: `break` su 2 e `continue` su 4 — cosa cambia?
2. Sostituisci il `for` con un `while` equivalente.
3. Conta quanti numeri **effettivamente stampati** con un contatore.

#### 5. MAKE (Crea)
**Scenario SIA — Analisi movimenti di cassa**

Sequenza fissa di importi (array piccolo o elenco in variabili).  
- `continue` se importo `== 0`  
- `break` se importo `> 10000` (outlier)  
- Stampa quanti movimenti validi sono stati elaborati prima dello stop  

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    double mov[] = {100.0, 0.0, 250.0, 12000.0, 80.0};
    // for + continue + break
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- `continue` = salta **questo** giro
- `break` = esci dal ciclo
- Usali quando la regola di business è chiara (scarto / stop)
- Non sostituiscono una buona condizione di ciclo

---

### ➡️ Prossimo chunk
Dal ciclo al **reparto**: introduciamo le **funzioni** che restituiscono un valore.

## 🖨️ La stampante fiscale: `std::fixed` e `std::setprecision`

Quando stampi un importo, `std::cout` mostra il valore in una forma tecnica. In un preventivo o in una fattura, invece, vuoi una forma regolare: due cifre dopo il punto decimale per ogni riga.

> 💡 **Metafora:**  
> Immagina una stampante fiscale. `std::fixed` seleziona la modalità “importo decimale”; `std::setprecision(2)` imposta due caselle per i centesimi. La stampante non cambia il valore del calcolo: cambia il modo in cui lo presenta.

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- formattare un prospetto di importi con `std::fixed` e `std::setprecision(2)`.

---

### ⚙️ Prima del laboratorio: i due manipolatori

| Elemento | Che cosa imposta | Perché serve in contabilità |
| :--- | :--- | :--- |
| `#include <iomanip>` | Rende disponibili i manipolatori di formattazione | Il compilatore conosce `std::fixed` e `std::setprecision` |
| `std::fixed` | Notazione decimale fissa | Evita una visualizzazione tecnica o variabile |
| `std::setprecision(2)` | Due cifre dopo il punto con `fixed` | Mantiene coerenti importi e totali |

```cpp
std::cout << std::fixed << std::setprecision(2);
std::cout << 19.5;  // 19.50
```

La configurazione resta attiva per le stampe successive dello stesso `std::cout`.

---

### 🔬 Laboratorio PRIMM: il prospetto di una vendita

Il negozio registra un imponibile di `19.5` euro e applica l'IVA al 22%. Prima di eseguire il programma, osserva come verranno stampate le tre righe.

#### 1. PREDICT (Prevedi)

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    std::cout << std::fixed << std::setprecision(2) << imponibile;
    return 0;
}
```

**Domanda 1**

Perché `std::fixed` è utile quando stampi un importo?

[(X)] Chiede di rappresentare il numero in forma decimale fissa, adatta a un prospetto
[( )] Trasforma automaticamente l'importo da euro a centesimi
[( )] Arrotonda sempre il valore memorizzato nella variabile

**Domanda 2**

Che cosa indica `std::setprecision(2)` insieme a `std::fixed`?

[(X)] Mostrare due cifre dopo il punto decimale
[( )] Moltiplicare il numero per 2
[( )] Mostrare al massimo due cifre complessive

**Domanda 3**

Prima del Run, quale output prevedi per `19.5`?

[(X)] 19.50
[( )] 19.5
[( )] 20.00

**Domanda 4**

Perché nel programma serve `#include <iomanip>`?

[(X)] Per rendere disponibili `std::fixed` e `std::setprecision`
[( )] Per dichiarare automaticamente tutte le variabili `double`
[( )] Per sostituire `#include <iostream>` nelle stampe

**Domanda 5**

Se scrivi `std::setprecision(2)` senza `std::fixed`, quale previsione è più corretta?

[(X)] La precisione riguarda le cifre significative, quindi non garantisce sempre due decimali
[( )] Il programma non può compilare perché `setprecision` richiede un intero positivo diverso da 2
[( )] L'output avrà sempre esattamente due cifre dopo il punto

Completa prima il quiz: concentrati sulla differenza tra **valore calcolato** e **valore visualizzato**.

#### 2. RUN (Esegui)

Ricopia ed esegui il programma. Confronta il risultato con la tua previsione.

```cpp
/**
 * @file prospetto_vendita.cpp
 * @brief Presenta un prospetto di vendita in un formato leggibile.
 */
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA 22%:    " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA:        " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```

**Domanda 1**

Perché anche `iva` e `totale` vengono stampate con due decimali?

[(X)] I manipolatori restano attivi per le stampe successive dello stesso `std::cout`
[( )] Ogni `double` viene sempre stampato con due decimali in C++
[( )] La variabile `imponibile` trasferisce il suo formato alle altre variabili

**Domanda 2**

Qual è l'ordine corretto nella riga di configurazione?

[(X)] Prima `std::fixed`, poi `std::setprecision(2)`, quindi il valore da stampare
[( )] Prima il valore, poi `std::fixed` e infine `std::setprecision(2)`
[( )] Prima `std::setprecision(2)`, poi si chiude `std::cout` con un punto e virgola

**Domanda 3**

Perché il risultato di `19.5 * 0.22` può essere visualizzato come `4.29`?

[(X)] Il formato mostra due decimali e arrotonda la rappresentazione visualizzata
[( )] Il programma sostituisce sempre il valore con il numero intero più vicino
[( )] La moltiplicazione viene eseguita come testo e non come numero

**Domanda 4**

Che cosa succede se togli `#include <iomanip>` ma lasci `std::setprecision(2)`?

[(X)] Il compilatore può segnalare che `setprecision` non è dichiarata
[( )] Il programma compila, ma `std::cout` ignora soltanto la precisione
[( )] Il valore viene automaticamente stampato come intero

**Domanda 5**

Se aggiungi una stampa dopo il prospetto senza cambiare il formato, che cosa accade?

[(X)] Anche quella stampa usa il formato corrente di `std::cout`, finché non lo modifichi
[( )] Il formato si annulla automaticamente dopo ogni riga
[( )] Il formato si applica solo alla variabile `imponibile`

Perché l'impostazione compare una sola volta ma vale per tre stampe? Segui l'ordine delle istruzioni:

| Passo | Istruzione | Che cosa osservi |
| :---: | :--- | :--- |
| 1 | `imponibile = 19.5` | Il programma conserva il valore numerico |
| 2 | `iva = imponibile * 0.22` | Calcola l'IVA |
| 3 | `totale = imponibile + iva` | Calcola il totale |
| 4 | `fixed` + `setprecision(2)` | Configura la visualizzazione di `std::cout` |
| 5 | Le tre stampe | Ogni importo appare con due cifre decimali |

Con `fixed` e `setprecision(2)`, `19.5` viene mostrato come `19.50`. Il formato non arrotonda o riscrive la variabile in memoria: riguarda la stampa.

#### 4. MODIFY (Modifica)

```cpp
std::cout << std::fixed << std::setprecision(2);
std::cout << "Totale: " << totale << '\n';
```

**Domanda 1**

Quale modifica fa apparire tre cifre dopo il punto decimale?

[(X)] Sostituire `std::setprecision(2)` con `std::setprecision(3)`
[( )] Sostituire `std::fixed` con `std::setprecision(3)`
[( )] Moltiplicare `totale` per 3 prima della stampa

**Domanda 2**

Che effetto ha togliere `std::fixed` lasciando `std::setprecision(2)`?

[(X)] La precisione può indicare due cifre significative, non necessariamente due decimali
[( )] Il programma stampa sempre due zeri in più
[( )] Il valore di `totale` viene cancellato

**Domanda 3**

Quale modifica mantiene il prospetto a due decimali ma stampa prima l'etichetta `Totale`?

[(X)] Spostare l'etichetta nella stessa espressione di output, prima di `totale`
[( )] Mettere `std::fixed` dopo `totale` e prima dell'etichetta
[( )] Cambiare `totale` in una variabile `int`

**Domanda 4**

Se sostituisci `std::setprecision(2)` con `std::setprecision(0)`, quale effetto prevedi?

[(X)] La stampa usa zero cifre dopo il punto e può arrotondare il valore visualizzato
[( )] La stampa usa automaticamente due cifre perché gli importi sono monetari
[( )] Il programma entra in un ciclo infinito

**Domanda 5**

Quale modifica formatta anche la nuova variabile `sconto` con due decimali?

[(X)] Stampare `sconto` con lo stesso `std::cout` dopo aver impostato `fixed` e `setprecision(2)`
[( )] Dichiarare `sconto` come `char`
[( )] Inserire `std::setprecision(2)` solo dopo la stampa di `sconto`

Apporta una modifica alla volta e riesegui.

**Modifica A — Cambia la precisione**  
Sostituisci `std::setprecision(2)` con `std::setprecision(3)`. Controlla tutte le righe del prospetto.

**Modifica B — Togli `fixed`**  
Lascia `std::setprecision(2)` ma rimuovi `std::fixed`. Confronta il risultato e spiega perché non hai più la garanzia di due cifre dopo il punto.

**Modifica C — Aggiungi una riga**  
Dichiara `double sconto = 1.5;` e stampa `Sconto: 1.50` usando la stessa configurazione già attiva.

<details>
<summary>💡 Scaffold per le modifiche</summary>

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;
    double sconto = 1.5;

    std::cout << std::fixed << std::setprecision(2);
    // TODO: stampa il prospetto e la nuova riga Sconto
    return 0;
}
```

</details>

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio commerciale prepara un preventivo per un cliente.

**Requisiti**:

1. Dichiara `imponibile = 125.5` e `aliquota = 0.22`.
2. Calcola `iva` e `totale` con variabili `double`.
3. Configura `std::cout` con `std::fixed` e `std::setprecision(2)`.
4. Stampa le tre etichette `Imponibile`, `IVA 22%` e `Totale`, ciascuna su una riga.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 125.5;
    double aliquota = 0.22;
    double iva = imponibile * aliquota;
    double totale = imponibile + iva;

    /// Il formato uniforme rende il preventivo leggibile e confrontabile.
    // TODO: configura la stampa a due decimali
    // TODO: stampa imponibile, IVA e totale
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `#include <iomanip>` rende disponibili i manipolatori di formattazione.
- `std::fixed` imposta la notazione decimale fissa.
- Con `std::fixed`, `std::setprecision(2)` mostra due cifre dopo il punto.
- La configurazione resta attiva per le stampe successive dello stesso `std::cout`.
- Il formato cambia la rappresentazione visualizzata, non il valore memorizzato.

---

### ➡️ Prossimo chunk

Ora che sai presentare bene un risultato, puoi imparare a organizzare il calcolo in **funzioni** riutilizzabili.


## 🏢 Il Primo Reparto: funzioni che restituiscono un valore

> "Un buon processo si scompone in reparti con responsabilità chiare."  
> — *Organizzazione aziendale e top-down*

Finora quasi tutto viveva in `main`.  
Quando la logica cresce (IVA, sconti, commissioni), conviene **estrarre un reparto**: una **funzione** con nome, parametri e **valore di ritorno**.

> 💡 **Metafora: sportello specializzato**  
> - `calcolaIva(imponibile)` = sportello “ufficio IVA”  
> - Gli dai l’imponibile (documento in ingresso)  
> - Ti restituisce l’importo IVA (documento in uscita)  
> - `main` coordina: chiede, riceve, stampa

In questo chunk: funzioni **semplici** che calcolano e `return`.  
Passaggio per riferimento e scope fine: capitolo successivo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare e chiamare una funzione con parametri e `return`
- Usare il risultato in `main` senza ripetere la formula

---

### ⚙️ Anatomia minima

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

// uso:
double iva = calcolaIva(100.0);
```

| Parte | Ruolo |
|-------|--------|
| Tipo di ritorno | Cosa esce dallo sportello (`double`, `int`, …) |
| Nome | Verbo + oggetto (`calcolaIva`) |
| Parametri | Dati in ingresso |
| `return` | Fine del lavoro + valore |

---

### 🔬 Laboratorio PRIMM: Ufficio IVA

#### 1. PREDICT (Prevedi)

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

Quanto vale `calcolaIva(100.0)` con aliquota 0.22?

[(X)] 22
[( )] 100
[( )] 122
[( )] 0.22

<details>
<summary>💡 Spiegazione</summary>
100 × 0.22 = 22. La funzione restituisce solo l’IVA, non il totale documento.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ufficio_iva.cpp
 * @brief Funzione che calcola l'IVA al 22%.
 */
#include <iostream>

double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

int main() {
    double imponibile = 100.0;
    double iva = calcolaIva(imponibile);
    double totale = imponibile + iva;

    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA:        " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Momento | Cosa succede |
|---------|----------------|
| Chiamata | `main` sospende; parte `calcolaIva` |
| `return` | Il valore torna a `main` in `iva` |
| Dopo | `main` usa `iva` nel totale |

> 🔗 [Python Tutor C++](https://pythontutor.com/cpp.html): osserva lo stack frame della funzione.

#### 4. MODIFY (Modifica)
1. Cambia l’imponibile a `250.0` e verifica i tre importi.
2. Aggiungi `double calcolaTotale(double imponibile)` che usa `calcolaIva` al suo interno.
3. Documenta le funzioni con `@brief` e `@param` / `@return`.

#### 5. MAKE (Crea)
**Scenario SIA — Commissione POS**

`commissione_pos.cpp`:  
- `double commissione(double importo)` → 1.2% dell’importo (o soglia minima fissa a tua scelta, documentata)  
- `main` stampa importo, commissione e netto negoziante  

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
double commissione(double importo) {
    return importo * 0.012;
}
int main() {
    // ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Funzione = reparto con ingresso, lavoro, uscita
- `return` consegna il risultato a chi ha chiamato
- `main` orchestra; le funzioni specializzano
- Un calcolo riusato → una funzione, non copia-incolla

---

### ➡️ Prossimo chunk
Come far sì che una funzione **modifichi** le variabili del chiamante: passaggio per **riferimento**.

## 📄 Fotocopia o Originale: passaggio per valore e per riferimento

> "Se ti passo la fotocopia, le tue note non restano sul documento ufficiale."  
> — *Metafora di gestione documentale*

Una funzione può ricevere:
- una **copia** del valore (**per valore**) → modifiche locali non tornano al chiamante  
- un **alias** della variabile originale (**per riferimento**, `&`) → le modifiche restano  

> 💡 **Metafora**  
> - Per valore = fotocopia del listino  
> - Per riferimento (`double& prezzo`) = il listino **originale** sul bancone

Lo **scope**: una variabile locale esiste solo nel blocco/funzione dove è dichiarata.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Distinguere passaggio per valore e per riferimento
- Scrivere una funzione che aggiorna un `double` del chiamante tramite `double&`

---

### ⚙️ Confronto

```cpp
void aumentaCopia(int v) { v += 5; }      // fotocopia
void aumentaRef(int& v) { v += 5; }     // originale

int x = 10;
aumentaCopia(x);  // x resta 10
aumentaRef(x);    // x diventa 15
```

---

### 🔬 Laboratorio PRIMM: Aggiornare un prezzo

#### 1. PREDICT (Prevedi)

```cpp
void aumenta(int valore) { valore += 5; }
int x = 10;
aumenta(x);
```

Dopo `aumenta(x)` con parametro per valore, quanto vale `x` se partiva da 10?

[(X)] 10 (non modificato)
[( )] 15
[( )] Errore di compilazione
[( )] Crash

<details>
<summary>💡 Spiegazione</summary>
<code>valore</code> è una copia locale. Incrementarla non tocca <code>x</code> in <code>main</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file prezzo_riferimento.cpp
 * @brief Valore vs riferimento.
 */
#include <iostream>

void scontoCopia(double prezzo, double perc) {
    prezzo = prezzo * (1.0 - perc / 100.0);
}

void scontoRef(double& prezzo, double perc) {
    prezzo = prezzo * (1.0 - perc / 100.0);
}

int main() {
    double p1 = 100.0;
    double p2 = 100.0;
    scontoCopia(p1, 10.0);
    scontoRef(p2, 10.0);
    std::cout << "Dopo copia: " << p1 << '\n';
    std::cout << "Dopo ref:   " << p2 << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Chiamata | Effetto su variabile in `main` |
|----------|---------------------------------|
| `scontoCopia` | Nessuno |
| `scontoRef` | Prezzo aggiornato |

In [Python Tutor](https://pythontutor.com/cpp.html) confronta i frame e l’alias `&`.

#### 4. MODIFY (Modifica)
1. Aggiungi `void scambia(double& a, double& b)`.
2. Usa `const double&` in una funzione che **solo legge** il prezzo per stamparlo.
3. Dimostra in `main` sconto + scambio.

#### 5. MAKE (Crea)
**Scenario SIA — Aggiornamento listino**

`aggiorna_listino.cpp`:  
- `applicaSconto(double& prezzo, double perc)`  
- `scambiaPrezzi(double& a, double& b)`  
- `main` con due prezzi di esempio  

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void applicaSconto(double& prezzo, double perc) { /* ... */ }
void scambiaPrezzi(double& a, double& b) { /* ... */ }
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Per valore = fotocopia; per riferimento = originale
- `T&` nel parametro per modificare il chiamante
- `const T&` per leggere senza copiare
- Scope locale: fuori dal blocco la variabile non esiste

---

### ➡️ Prossimo chunk
Sequenze di dati dello stesso tipo: gli **array**.

## 📦 La Batteria di Locker: gli array e le sequenze di dati

> "I dati non vivono isolati: vivono in elenchi."  
> — *Principio di progettazione dei sistemi informativi*

Finora ogni variabile era **uno sportello**.  
In azienda, però, i dati arrivano a **serie**: 12 mesi di vendite, 50 codici prodotto, 100 movimenti di cassa.  
Aprire 100 variabili diverse è insostenibile. Serve una **fila ordinata di sportelli**: l’**array**.

> 💡 **Metafora: batteria di locker InPost**  
> - L’**array** = una fila di locker **identici** e **numerati**  
> - L’**indice** (`0`, `1`, `2`…) = il numero sullo sportello (parte da **zero**)  
> - La **dimensione** = quanti locker hai prenotato (fissa, in C++ “grezzo”)  
> - `vendite[3]` = “apri il locker numero 3” (il **quarto** della fila)  
> - `vendite[30]` su 30 locker (`0`…`29`) = chiedi un locker che **non esiste** → caos

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare un array monodimensionale, indicizzarlo correttamente e scorrerlo con un `for`
- Riconoscere e evitare l’accesso **fuori dai limiti** (out-of-bounds)

---

### ⚙️ In breve

```cpp
double vendite[12];          // 12 locker: indici 0..11
vendite[0] = 1500.0;         // gennaio
vendite[11] = 2100.0;        // dicembre

for (int i = 0; i < 12; ++i) {
    std::cout << vendite[i] << '\n';
}
```

| Idea | Regola |
|------|--------|
| Indice legale | Da `0` a `N - 1` |
| `vendite[N]` | **Fuori**: il compilatore spesso **non** ti ferma |
| Tipo | Tutti gli elementi dello stesso tipo |

---

### 🔬 Laboratorio PRIMM: Vendite mensili

Registriamo 6 mesi di fatturato e calcoliamo un totale.

#### 1. PREDICT (Prevedi)

```cpp
double vendite[30];
double x = vendite[30];
```

Con `double vendite[30];`, cosa succede leggendo `vendite[30]`?

[( )] Compila e legge 0
[(X)] Compila ma comportamento indefinito (indice fuori range)
[( )] Errore di compilazione obbligatorio
[( )] Il programma non parte

<details>
<summary>💡 Spiegazione</summary>
Con dimensione 30 gli indici validi sono 0…29. L’indice 30 è fuori: il C++ non obbliga un controllo a runtime; il risultato è indefinito.
</details>

#### 2. RUN (Esegui)

Digita e premi **Run**.

```cpp
/**
 * @file vendite_semestre.cpp
 * @brief Totale vendite su sei mesi (array).
 */
#include <iostream>

int main() {
    double vendite[6] = {1200.0, 980.0, 1500.0, 1100.0, 1300.0, 1600.0};
    double totale = 0.0;

    for (int i = 0; i < 6; ++i) {
        totale = totale + vendite[i];
        std::cout << "Mese " << (i + 1) << ": " << vendite[i] << '\n';
    }
    std::cout << "Totale semestre: " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Elemento | Ruolo |
|----------|--------|
| `vendite[6]` | Sei celle contigue di `double` |
| `i` da 0 a 5 | Visita ogni locker una volta |
| `totale = totale + vendite[i]` | Accumulo (stesso schema del `while` contabile) |

> 🔗 Copia il programma su [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva l’array nella memoria.

#### 4. MODIFY (Modifica)
1. Cambia un valore in inizializzazione e verifica il nuovo totale.
2. Stampa anche la **media** (`totale / 6`).
3. Trova e stampa il **mese con fatturato massimo** (indice + valore).

#### 5. MAKE (Crea)
**Scenario SIA — Controllo vendite annuali**

Scrivi `controllo_vendite.cpp`:
- Array di **12** `double` (un anno)
- Inizializza con valori di esempio (o input se preferisci)
- Stampa totale, media, mese di massimo fatturato (1–12, non 0–11 in output)
- Documentazione Doxygen se superi ~15 righe

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    double vendite[12] = {/* ... */};
    // totale, media, max
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Array = fila di sportelli **stesso tipo**, indici da **0**
- L’ultimo indice valido è **N − 1**
- Fuori range = bug silenzioso tipico
- Si scorre quasi sempre con un `for`

---

### ➡️ Prossimo chunk
Quando i dati sono a **griglia** (reparti × mesi), serve un array a **due dimensioni**.

## 📊 Il Foglio Excel in Memoria: array bidimensionali

> "Una tabella è il modo più naturale di organizzare dati aziendali."  
> — *Pratica di reporting gestionale*

Un array monodimensionale è una **riga**.  
Spesso i report sono **griglie**: righe = reparti, colonne = mesi o trimestri.  
In C++ usiamo un **array bidimensionale** (matrice).

> 💡 **Metafora: foglio Excel**  
> - `vendite[r][c]` = cella all’incrocio **riga r**, **colonna c**  
> - Prima dimensione = righe (reparti)  
> - Seconda = colonne (periodi)  
> - Anche qui gli indici partono da **0**

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare e scorrere un array `tipo nome[RIGHE][COLONNE]`
- Calcolare totali per riga (o per colonna) su dati tabellari

---

### ⚙️ In breve

```cpp
// 2 reparti × 3 mesi
double vendite[2][3] = {
    {1000.0, 1200.0, 900.0},   // reparto 0
    {800.0,  950.0,  1100.0}   // reparto 1
};
```

Due cicli annidati: esterno sulle righe, interno sulle colonne.

---

### 🔬 Laboratorio PRIMM: Due reparti, tre mesi

#### 1. PREDICT (Prevedi)

```cpp
int m[2][3];
```

In `int m[2][3];`, quanti elementi ci sono e qual è l’ultimo indice di colonna?

[(X)] 6 elementi; colonne 0..2
[( )] 5 elementi; colonne 1..3
[( )] 6 elementi; colonne 1..3
[( )] 2 elementi in tutto

<details>
<summary>💡 Spiegazione</summary>
<code>int m[2][3]</code> ha 2×3 = 6 elementi. Le colonne sono indicizzate 0, 1, 2.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file matrice_vendite.cpp
 * @brief Totale per reparto su tre mesi.
 */
#include <iostream>

int main() {
    double vendite[2][3] = {
        {1000.0, 1200.0, 900.0},
        {800.0, 950.0, 1100.0}
    };

    for (int r = 0; r < 2; ++r) {
        double subtotale = 0.0;
        for (int c = 0; c < 3; ++c) {
            subtotale = subtotale + vendite[r][c];
        }
        std::cout << "Reparto " << r << " totale: " << subtotale << '\n';
    }
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Variabile | Significato |
|-----------|-------------|
| `r` | Indice di riga (reparto) |
| `c` | Indice di colonna (mese) |
| `subtotale` | Si azzera a ogni nuova riga |

Segui con [Python Tutor](https://pythontutor.com/cpp.html) l’ordine delle celle visitate.

#### 4. MODIFY (Modifica)
1. Aggiungi un terzo reparto (matrice `3×3`) e aggiorna i cicli.
2. Stampa anche il **totale generale** di tutta la matrice.
3. Stampa i totali **per colonna** (per mese).

#### 5. MAKE (Crea)
**Scenario SIA — Vendite per reparto e trimestre**

`vendite_reparti.cpp`: matrice **3 reparti × 4 trimestri**, totali per riga, per colonna e complessivo. Output leggibile.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    const int R = 3, C = 4;
    double v[R][C] = { /* ... */ };
    // cicli annidati
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Matrice = foglio a righe e colonne
- `m[i][j]`: prima riga, poi colonna
- Quasi sempre **due** `for` annidati
- Stessi pericoli di out-of-bounds, su due assi

---

### ➡️ Prossimo chunk
Dietro ogni array c’è un indirizzo in memoria: introduciamo i **puntatori** in modo guidato e cauto.

## 🔑 Il Numero dello Sportello: puntatori e indirizzi

> "Non ti do la merce: ti do la chiave del locker."  
> — *Metafora operativa*

Finora passavamo **valori** (copie) o **riferimenti** (`&` nei parametri).  
Un **puntatore** è una variabile che memorizza l’**indirizzo** di un’altra variabile: il *numero dello sportello*, non la merce.

> 💡 **Metafora**  
> - `x` = merce nel locker  
> - `&x` = numero civico dello sportello  
> - `int* p` = foglietto su cui è scritto un numero di sportello  
> - `p = &x` = “annota l’indirizzo di x”  
> - `*p` = “apri lo sportello indicato e usa la merce”

In questo chunk **non** usiamo ancora `new`/`delete`: solo puntatori a variabili automatiche.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare un puntatore, assegnargli `&variabile` e usare `*` per leggere/scrivere
- Spiegare la differenza tra l’indirizzo (`p`) e il valore puntato (`*p`)

---

### ⚙️ In breve

```cpp
int giacenza = 40;
int* p = &giacenza;   // p contiene l'indirizzo di giacenza
std::cout << *p;      // 40
*p = 35;              // modifica giacenza tramite il puntatore
```

---

### 🔬 Laboratorio PRIMM: Aggiornare la giacenza via puntatore

#### 1. PREDICT (Prevedi)

```cpp
int x = 10;
int* p = &x;
*p = 25;
```

Dopo `int x = 10; int* p = &x; *p = 25;`, quanto vale `x`?

[( )] 10
[(X)] 25
[( )] Indefinito
[( )] L’indirizzo di x

<details>
<summary>💡 Spiegazione</summary>
<code>*p = 25</code> scrive nello sportello di <code>x</code>, perché <code>p</code> punta a <code>x</code>. Quindi <code>x</code> diventa 25.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file puntatore_giacenza.cpp
 * @brief Modifica di una variabile tramite puntatore.
 */
#include <iostream>

int main() {
    int giacenza = 40;
    int* p = &giacenza;

    std::cout << "Prima: " << giacenza << '\n';
    *p = *p - 5;  // scarico 5 pezzi
    std::cout << "Dopo:  " << giacenza << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Espressione | Cosa rappresenta |
|-------------|------------------|
| `giacenza` | Valore (merce) |
| `&giacenza` | Indirizzo |
| `p` | Copia dell’indirizzo |
| `*p` | Merce nello sportello puntato |

Osserva in [Python Tutor](https://pythontutor.com/cpp.html) le frecce tra `p` e `giacenza`.

#### 4. MODIFY (Modifica)
1. Stampa anche l’indirizzo con `std::cout << p;` (vedrai un hex).
2. Crea `double prezzo` e un `double*` che lo aggiorna (+IVA 22%).
3. Scrivi una funzione `void azzera(int* q)` che mette a 0 la variabile puntata.

#### 5. MAKE (Crea)
**Scenario SIA — Scambio prezzi listino**

`scambia_prezzi_ptr.cpp`: funzione `void scambia(double* a, double* b)` che scambia due prezzi **via puntatori**. In `main`, dimostra lo scambio su due variabili.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void scambia(double* a, double* b) {
    double tmp = *a;
    // ...
}
int main() {
    double p1 = 10.0, p2 = 20.0;
    scambia(&p1, &p2);
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Puntatore = variabile che tiene un **indirizzo**
- `&x` indirizzo; `*p` valore puntato
- `*p = …` modifica la variabile originale
- In questo corso: prima i puntatori “semplici”, allocazione dinamica più avanti se serve

---

### ➡️ Prossimo chunk
Raggruppiamo dati eterogenei (`struct`) e stati discreti (`enum`) come in un record anagrafico.

## 🏷️ Stati e Schede Anagrafiche: `enum` e `struct`

> "Un codice magazzino non è un intero a caso: è un *significato*."  
> — *Disciplina dei dati master*

`int stato = 2` è opaco: 2 cosa?  
Un **`enum class`** dà **nomi** agli stati.  
Una **`struct`** unisce campi eterogenei in una **scheda** (come una riga di anagrafica).

> 💡 **Metafora: cartellino prodotto + semaforo stato**  
> - `struct Articolo` = cartellino (codice, descrizione, prezzo)  
> - `enum class Stato` = semaforo (`Disponibile`, `Esaurito`, `Sospeso`)

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Definire un `enum class` e una `struct` semplice
- Creare variabili struct, assegnare campi e stamparli

---

### ⚙️ In breve

```cpp
enum class Stato { Disponibile, Esaurito, Sospeso };

struct Articolo {
    std::string codice;
    std::string nome;
    double prezzo;
    Stato stato;
};
```

Accesso ai campi: `a.prezzo`, `a.stato = Stato::Disponibile`.

---

### 🔬 Laboratorio PRIMM: Scheda articolo

#### 1. PREDICT (Prevedi)

```cpp
enum class Stato { Attivo, Sospeso };
Stato a = Stato::Attivo;
Stato b = Stato::Attivo;
// a == b ?
```

Con `enum class Stato { Attivo, Sospeso };`, cosa stampa il confronto tra due variabili entrambe `Attivo`?

[(X)] Sono uguali (true)
[( )] Non si possono confrontare
[( )] Sono sempre diversi
[( )] Compila solo con int

<details>
<summary>💡 Spiegazione</summary>
I valori dello stesso <code>enum class</code> si confrontano con <code>==</code>. Due variabili <code>Attivo</code> risultano uguali.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scheda_articolo.cpp
 * @brief Struct + enum class per anagrafica di magazzino.
 */
#include <iostream>
#include <string>

enum class Stato { Disponibile, Esaurito, Sospeso };

struct Articolo {
    std::string codice;
    std::string nome;
    double prezzo;
    Stato stato;
};

int main() {
    Articolo a;
    a.codice = "A-100";
    a.nome = "Carta A4";
    a.prezzo = 4.50;
    a.stato = Stato::Disponibile;

    std::cout << a.codice << " — " << a.nome
              << " — € " << a.prezzo << '\n';
    if (a.stato == Stato::Disponibile) {
        std::cout << "Stato: disponibile\n";
    }
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Costrutto | Perché usarlo |
|-----------|----------------|
| `enum class` | Evita numeri magici; scope proprio (`Stato::…`) |
| `struct` | Un solo nome per più campi correlati |
| `a.campo` | Accesso diretto al campo |

#### 4. MODIFY (Modifica)
1. Aggiungi il campo `int giacenza`.
2. Se `giacenza == 0`, imposta `stato = Stato::Esaurito`.
3. Scrivi una funzione `void stampa(const Articolo& x)` (passaggio per riferimento const).

#### 5. MAKE (Crea)
**Scenario SIA — Anagrafica articolo completa**

`anagrafica_articolo.cpp`: `struct` + `enum class`, almeno due articoli in `main`, stampa formattata, stato coerente con la giacenza.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
enum class Stato { /* ... */ };
struct Articolo { /* ... */ };
void stampa(const Articolo& x) { /* ... */ }
int main() { /* ... */ return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- `enum class` = stati con nome
- `struct` = scheda con più campi
- `oggetto.campo` per leggere/scrivere
- Preferisci `const Struct&` in lettura (niente copia inutile)

---

### ➡️ Prossimo chunk
Cercare un codice in un listino ordinato: **ricerca dicotomica**.

## 🔍 Trovare il Codice nel Listino: ricerca dicotomica

> "Non sfogliare tutto il catalogo se è già in ordine alfabetico."  
> — *Efficienza operativa*

Cercare un codice prodotto scorrendo **tutto** l’array funziona, ma su listini lunghi è costoso.  
Se il listino è **ordinato**, possiamo usare la **ricerca dicotomica** (binaria): a ogni passo dimezziamo l’intervallo.

> 💡 **Metafora: elenco telefonico (o catalogo a pagine)**  
> Apri a metà: il nome cercato è prima o dopo?  
> Scarti metà elenco e ripeti.  
> **Precondizione:** l’elenco deve essere **già ordinato**.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Implementare una ricerca binaria su un array di interi **ordinato**
- Spiegare perché l’ordine dei dati è obbligatorio

---

### ⚙️ Idea dell’algoritmo
1. `low = 0`, `high = N - 1`
2. Finché `low <= high`: guarda il centro `mid`
3. Se `a[mid] == chiave` → trovato  
4. Se `a[mid] < chiave` → cerca a destra (`low = mid + 1`)  
5. Altrimenti cerca a sinistra (`high = mid - 1`)

---

### 🔬 Laboratorio PRIMM: Codici prodotto ordinati

#### 1. PREDICT (Prevedi)

```cpp
// array NON ordinato
// binary_search(...)
```

La ricerca binaria su un array disordinato è affidabile?

[( )] Sì, sempre
[(X)] No: richiede array ordinato
[( )] Solo se tutti pari
[( )] Solo su stringhe

<details>
<summary>💡 Spiegazione</summary>
La dicotomica assume ordinamento. Su dati disordinati può “perdere” elementi ancora presenti.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ricerca_codice.cpp
 * @brief Ricerca binaria su codici prodotto ordinati.
 */
#include <iostream>

int main() {
    int codici[8] = {100, 150, 200, 250, 300, 350, 400, 450};
    int chiave = 300;
    int low = 0;
    int high = 7;
    int trovato = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (codici[mid] == chiave) {
            trovato = mid;
            break;
        } else if (codici[mid] < chiave) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    if (trovato >= 0) {
        std::cout << "Trovato in posizione " << trovato << '\n';
    } else {
        std::cout << "Non presente\n";
    }
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Passo | Cosa osservare |
|-------|----------------|
| `mid` | Sempre un indice nell’intervallo corrente |
| `low` / `high` | Si restringono; non devono “incrociarsi” senza uscita |
| Array | Deve restare ordinato in modo non decrescente |

Simula a mano 2–3 iterazioni su carta, poi [Python Tutor](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. Cambia `chiave` in un valore assente e verifica il messaggio.
2. Estrai una funzione `int cerca(const int a[], int n, int chiave)` che restituisce l’indice o `-1`.
3. Conta quante volte si esegue il corpo del `while` (confronti).

#### 5. MAKE (Crea)
**Scenario SIA — Verifica codice EAN interno**

`cerca_codice.cpp`: array ordinato di codici, input della chiave (o costante), stampa posizione o “non trovato”. Funzione dedicata alla ricerca.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int cerca(const int a[], int n, int chiave) {
    // binary search
    return -1;
}
int main() { /* ... */ return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Dicotomica = dimezza l’intervallo a ogni passo
- **Solo** su sequenze ordinate
- Restituisci indice o `-1`
- Molto più scalabile della scansione lineare su listini lunghi

---

### ➡️ Prossimo chunk
Per usare la ricerca binaria serve spesso **ordinare** prima i dati: selection sort.

## 🗂️ Riordinare il Listino: selection sort

> "Metti in ordine i prezzi prima di cercare il migliore."  
> — *Pratica di listino*

La ricerca binaria chiede dati ordinati.  
Un algoritmo semplice da capire (non il più veloce in assoluto) è il **selection sort**: a ogni passo **seleziona il minimo** della parte non ancora ordinata e lo mette al suo posto.

> 💡 **Metafora: riorganizzare scaffali**  
> Scaffale disordinato di prezzi.  
> 1) Trova il più basso tra quelli ancora fuori posto  
> 2) Scambialo con la prima posizione libera  
> 3) Avanza e ripeti

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Implementare selection sort su un array di `double` (o `int`)
- Spiegare il ruolo del doppio ciclo e dello scambio

---

### 🔬 Laboratorio PRIMM: Prezzi da ordinare

#### 1. PREDICT (Prevedi)

```cpp
// for i ...
//   cerca minimo in i..n-1
//   scambia con posizione i
```

Selection sort, a ogni passo esterno, cosa fa?

[(X)] Sceglie il minimo della parte non ordinata e lo mette in posizione i
[( )] Divide sempre a metà l’array
[( )] Ordina solo i numeri pari
[( )] Usa obbligatoriamente un secondo array

<details>
<summary>💡 Spiegazione</summary>
A ogni iterazione esterna il minimo della coda non ordinata viene portato in testa a quella coda.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file selection_prezzi.cpp
 * @brief Ordinamento crescenti di prezzi con selection sort.
 */
#include <iostream>

int main() {
    double prezzi[6] = {12.5, 4.0, 9.9, 3.5, 20.0, 7.25};
    const int n = 6;

    for (int i = 0; i < n - 1; ++i) {
        int iMin = i;
        for (int j = i + 1; j < n; ++j) {
            if (prezzi[j] < prezzi[iMin]) {
                iMin = j;
            }
        }
        if (iMin != i) {
            double tmp = prezzi[i];
            prezzi[i] = prezzi[iMin];
            prezzi[iMin] = tmp;
        }
    }

    for (int i = 0; i < n; ++i) {
        std::cout << prezzi[i] << ' ';
    }
    std::cout << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Ciclo | Compito |
|-------|---------|
| Esterno `i` | Posizione da “fissare” |
| Interno `j` | Cerca l’indice del minimo in `i..n-1` |
| Scambio | Porta il minimo in posizione `i` |

Esegui a mano il primo passaggio su un array di 4 elementi.

#### 4. MODIFY (Modifica)
1. Ordina in **ordine decrescente**.
2. Estrai `void selectionSort(double a[], int n)`.
3. Conta quanti scambi effettivi (quando `iMin != i`).

#### 5. MAKE (Crea)
**Scenario SIA — Listino prezzi ordinato**

`ordina_prezzi.cpp`: almeno 8 prezzi, selection sort, stampa prima/dopo. Funzione dedicata all’ordinamento.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void selectionSort(double a[], int n) { /* ... */ }
int main() { /* ... */ return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Selection sort: minimo → posizione successiva
- Due `for` annidati; scambi semplici
- Facile da spiegare; non è il più efficiente su grandi N
- Utile per listini piccoli e per capire l’idea di ordinamento

---

### ➡️ Prossimo chunk
Strategie *divide et impera* (merge sort) per ordinamenti più scalabili.

## 🧩 Dividere per Ordinare: idea del merge sort

> "Ordina i reparti separatamente, poi unisci i due elenchi già ordinati."  
> — *Divide et impera in magazzino*

Selection sort è chiaro ma, su tanti dati, fa molti confronti.  
Il **merge sort** applica *divide et impera*: spezza, ordina le parti, **fonde** (merge) due sequenze già ordinate.

In questo chunk ci concentriamo sull’idea e sulla **fase di merge** (il cuore comprensibile e utile anche da solo). Un’implementazione ricorsiva completa può seguire dopo aver visto la ricorsione.

> 💡 **Metafora: due pile di fatture già ordinate per data**  
> Unisci in un’unica pila ordinata confrontando sempre le due “teste”.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Spiegare l’idea divide-et-impera del merge sort
- Implementare la **fusione** di due array monodimensionali già ordinati

---

### 🔬 Laboratorio PRIMM: Unire due listini ordinati

#### 1. PREDICT (Prevedi)

```cpp
// due metà già ordinate → una sequenza ordinata
```

Qual è il ruolo principale della fase di merge?

[(X)] Fondere due sottosequenze già ordinate
[( )] Mescolare a caso gli elementi
[( )] Eliminare i duplicati obbligatoriamente
[( )] Ordinare solo con scambi adiacenti

<details>
<summary>💡 Spiegazione</summary>
Il merge non “riordina da zero”: sfrutta l’ordine già presente nelle due metà.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file merge_due_listini.cpp
 * @brief Fusione di due array ordinati in un terzo.
 */
#include <iostream>

int main() {
    int a[4] = {10, 30, 50, 70};
    int b[3] = {20, 40, 60};
    int c[7];
    int i = 0, j = 0, k = 0;

    while (i < 4 && j < 3) {
        if (a[i] <= b[j]) {
            c[k] = a[i];
            ++i;
        } else {
            c[k] = b[j];
            ++j;
        }
        ++k;
    }
    while (i < 4) { c[k] = a[i]; ++i; ++k; }
    while (j < 3) { c[k] = b[j]; ++j; ++k; }

    for (int t = 0; t < 7; ++t) {
        std::cout << c[t] << ' ';
    }
    std::cout << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Indice | Ruolo |
|--------|--------|
| `i` | Avanzamento su `a` |
| `j` | Avanzamento su `b` |
| `k` | Scrittura su `c` |

Traccia i primi tre passi a mano: quale testa (`a[i]` o `b[j]`) viene scelta?

#### 4. MODIFY (Modifica)
1. Cambia i valori (restando ordinati) e verifica `c`.
2. Estrai `void merge(const int a[], int na, const int b[], int nb, int c[])`.
3. Gestisci il caso in cui un array è vuoto (`na == 0`).

#### 5. MAKE (Crea)
**Scenario SIA — Unione di due listini codici**

`merge_listini.cpp`: due array di codici già ordinati, risultato fuso in un terzo array, stampa. Funzione `merge` dedicata.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void merge(const int a[], int na, const int b[], int nb, int c[]) {
    // ...
}
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Merge sort = dividi, ordina, **fondi**
- Merge di due sequenze ordinate: confronta le teste
- Serve spazio per l’array risultato
- Qui abbiamo padroneggiato il merge; la ricorsione completa è il passo successivo naturale

---

### ➡️ Prossimo chunk
Mettiamo insieme `struct` e array: un piccolo **database in memoria**.

## 🗄️ L’Archivio in RAM: array di struct

> "Una tabella è un insieme di righe con le stesse colonne."  
> — *Modello relazionale in miniatura*

Un database vero sta su disco e parla SQL.  
In memoria, puoi simulare una **tabella** con un **array di struct**: ogni elemento è una riga; ogni campo della struct è una colonna.

> 💡 **Metafora: foglio clienti / movimenti**  
> - `struct Movimento` = colonne (id, descrizione, importo)  
> - `Movimento tab[100]` = fino a 100 righe  
> - `n` = quante righe sono **realmente** usate

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Definire una struct-record e un array di record
- Scorrere le righe “vive” (`0..n-1`) per elenchi e totali

---

### 🔬 Laboratorio PRIMM: Tre movimenti di cassa

#### 1. PREDICT (Prevedi)

```cpp
struct Record { int id; double importo; };
Record tabella[100];
```

Cosa rappresenta `Record tabella[100];` se Record è una struct?

[(X)] Fino a 100 righe con gli stessi campi
[( )] Un solo record con 100 campi
[( )] Una matrice 100×100 di int
[( )] Un file su disco

<details>
<summary>💡 Spiegazione</summary>
Array di struct = molte righe, stesso schema di colonne. Non è un file: vive finché il programma è in esecuzione.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file movimenti_cassa.cpp
 * @brief Mini-archivio movimenti in RAM.
 */
#include <iostream>
#include <string>

struct Movimento {
    int id;
    std::string desc;
    double importo;
};

int main() {
    Movimento tab[10];
    int n = 0;

    tab[n++] = {1, "Vendita bancone", 25.0};
    tab[n++] = {2, "Reso cliente", -5.0};
    tab[n++] = {3, "Vendita online", 40.0};

    double saldo = 0.0;
    for (int i = 0; i < n; ++i) {
        std::cout << tab[i].id << " | " << tab[i].desc
                  << " | " << tab[i].importo << '\n';
        saldo = saldo + tab[i].importo;
    }
    std::cout << "Saldo movimenti: " << saldo << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Simbolo | Significato |
|---------|-------------|
| `tab[i]` | Riga i-esima |
| `tab[i].importo` | Campo della riga |
| `n` | Numero di righe valide (non confonderlo con la capacità 10) |

#### 4. MODIFY (Modifica)
1. Aggiungi un quarto movimento e verifica `n` e il saldo.
2. Funzione `double totale(const Movimento tab[], int n)`.
3. Stampa solo i movimenti con `importo < 0` (uscite).

#### 5. MAKE (Crea)
**Scenario SIA — Archivio movimenti contabili**

`archivio_movimenti.cpp`: struct, array, almeno 5 movimenti di esempio, elenco completo, totale, conteggio positivi/negativi. Doxygen se il file cresce.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
struct Movimento { /* ... */ };
double totale(const Movimento tab[], int n) { return 0.0; }
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Tabella in RAM ≈ array di struct
- Capacità ≠ numero di righe usate (`n`)
- Si scorre con `for` su `0..n-1`
- È il ponte concettuale verso i database veri

---

### ➡️ Prossimo chunk
Quando un problema si definisce in termini di una versione più piccola di se stesso: **ricorsione**.

## 🔁 Il Problema che Chiama Se Stesso: ricorsione

> "Per capire n, capisci n−1; poi combina."  
> — *Schema divide et impera*

Una funzione **ricorsiva** si richiama su un’istanza **più piccola** dello stesso problema, finché raggiunge un **caso base**.

> 💡 **Metafora: matrioske contabili**  
> Per chiudere il totale di n movimenti: prendi l’importo dell’ultimo e **aggiungilo** al totale dei primi n−1.  
> Caso base: zero movimenti → totale 0.

Attenzione: senza caso base si ottiene **ricorsione infinita** (stack overflow).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una funzione ricorsiva con caso base chiaro
- Tracciare le chiamate su un esempio piccolo (fattoriale o somma)

*Non* affrontiamo qui liste collegate complete: restiamo su problemi numerici/array.

---

### 🔬 Laboratorio PRIMM: Fattoriale (per vedere lo stack)

#### 1. PREDICT (Prevedi)

```cpp
int f(int n) {
    if (n <= 0) return 1; // ?
    return n * f(n - 1);
}
```

Cosa deve avere ogni funzione ricorsiva corretta?

[( )] Solo chiamate ricorsive, senza mai fermarsi
[(X)] Almeno un caso base che interrompe la ricorsione
[( )] Obbligo di variabili globali
[( )] Niente `return`

<details>
<summary>💡 Spiegazione</summary>
Senza un if di arresto la catena di chiamate non termina. Il caso base è obbligatorio.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file fattoriale.cpp
 * @brief Esempio didattico di ricorsione con caso base.
 */
#include <iostream>

int fattoriale(int n) {
    if (n <= 1) {
        return 1;  // caso base
    }
    return n * fattoriale(n - 1);
}

int main() {
    std::cout << fattoriale(5) << '\n';  // 120
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Chiamata | Ritorna |
|----------|---------|
| `fattoriale(1)` | `1` |
| `fattoriale(2)` | `2 * 1` |
| `fattoriale(3)` | `3 * 2` |
| … | … |

Usa [Python Tutor](https://pythontutor.com/cpp.html) e osserva i **frame** sullo stack.

#### 4. MODIFY (Modifica)
1. Calcola `fattoriale(0)` e `fattoriale(1)`.
2. Scrivi `int potenza(int base, int exp)` ricorsiva (`exp == 0` → 1).
3. Versione **iterativa** equivalente del fattoriale e confronta leggibilità.

#### 5. MAKE (Crea)
**Scenario SIA — Totale ricorsivo di importi**

`somma_ricorsiva.cpp`: funzione `double somma(const double a[], int n)` ricorsiva  
(`n == 0` → 0; altrimenti `a[n-1] + somma(a, n-1)`). Dimostrazione in `main` su un piccolo array di movimenti.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
double somma(const double a[], int n) {
    if (n <= 0) return 0.0;
    return a[n - 1] + somma(a, n - 1);
}
int main() { /* ... */ return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Ricorsione = caso base + passo che riduce il problema
- Ogni chiamata ha il proprio frame sullo stack
- Senza caso base → ricorsione infinita
- Utile quando il problema ha struttura naturale “a pezzi più piccoli”

---

### ➡️ Prossimo passo
Con array, struct, ricerca, ordinamento e ricorsione hai gli strumenti del **secondo blocco** del corso: dati e algoritmi di base in chiave aziendale.



## 🏢 Dal cartellino al reparto: `struct` → `class` e incapsulamento

> "Non tutti possono modificare il listino: solo chi ha la responsabilità del reparto."  
> — *Governance dei dati aziendali*

Nel Blocco 2 l’`Articolo` era una **`struct`**: tutti i campi pubblici, come un cartellino lasciato sul bancone.  
Funziona, ma chiunque può scrivere `prezzo = -10` e rompere le regole di business.

Una **`class`** permette l’**incapsulamento**: stato **privato**, sportelli **pubblici** (metodi) che rispettano gli invarianti.

> 💡 **Metafora: reparto a porta chiusa**  
> - Dati `private` = archivio interno del reparto  
> - Metodi `public` = sportello unico (chiedi, non frugare nei cassetti)  
> - Invariante = “prezzo e giacenza non negativi”

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare una `class` con membri `private` e interfaccia `public`
- Spiegare perché l’incapsulamento protegge le regole aziendali sui dati

---

### ⚙️ In breve

```cpp
class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    void setPrezzo(double p);
    double getPrezzo() const;
};
```

Fuori dalla classe: solo i metodi pubblici. Niente `a.prezzo = …`.

---

### 🔬 Laboratorio PRIMM: Articolo protetto

#### 1. PREDICT (Prevedi)

```cpp
class Articolo {
private:
    double prezzo;
public:
    void setPrezzo(double p);
};
Articolo a;
a.prezzo = -5;
```

Se `prezzo` è `private` in una `class`, da `main` posso scrivere `a.prezzo = -5`?

[( )] Sì, sempre
[(X)] No: accesso vietato fuori dalla classe
[( )] Solo se il file si chiama main.cpp
[( )] Sì, ma solo con double

<details>
<summary>💡 Spiegazione</summary>
I membri private non sono accessibili da <code>main</code>. Serve un metodo pubblico che validi il valore.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_class.cpp
 * @brief Incapsulamento minimo su un articolo di magazzino.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    void setCodice(const std::string& c) { codice = c; }
    void setPrezzo(double p) {
        if (p < 0.0) {
            prezzo = 0.0;
        } else {
            prezzo = p;
        }
    }
    std::string getCodice() const { return codice; }
    double getPrezzo() const { return prezzo; }
};

int main() {
    Articolo a;
    a.setCodice("A-100");
    a.setPrezzo(12.5);
    a.setPrezzo(-3.0);  // corretta a 0
    std::cout << a.getCodice() << " → " << a.getPrezzo() << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Elemento | Ruolo |
|----------|--------|
| `private` | Stato interno |
| `setPrezzo` | Unico punto che può cambiare il prezzo (con regola) |
| `getPrezzo` | Lettura controllata |

Prova a decommentare mentalmente `a.prezzo = 1`: non compila.

#### 4. MODIFY (Modifica)
1. Aggiungi `giacenza` privata con `setGiacenza` / `getGiacenza` (mai negativa).
2. Metodo `void scheda()` che stampa codice, prezzo, giacenza.
3. Se `giacenza == 0`, stampa anche `"ESAURITO"`.

#### 5. MAKE (Crea)
**Scenario SIA — Articolo di magazzino a interfaccia chiusa**

`articolo_classe.cpp`: classe `Articolo` completa (codice, prezzo, giacenza), setter con validazione, `scheda()`, dimostrazione in `main`.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo {
private:
    // ...
public:
    // setter / getter / scheda
};
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- `class` = dati privati + sportelli pubblici
- Incapsulamento = proteggere gli invarianti
- Fuori si usano i metodi, non i campi
- Stesso dominio del `struct`, responsabilità diverse

---

### ➡️ Prossimo chunk
Come nasce un oggetto **già valido**: i **costruttori**.

## 📋 Assunzione in organico: costruttori e oggetto ben formato

> "Non esiste un dipendente senza matricola: non dovrebbe esistere un articolo senza codice e prezzo coerente."  
> — *Anagrafica e qualità del dato*

Con soli setter, si può dimenticare di inizializzare.  
Il **costruttore** è il contratto di **creazione**: quando l'oggetto nasce, è già in uno stato sensato.

> 💡 **Metafora: assunzione**  
> All'ingresso in azienda compili i dati obbligatori.  
> Il costruttore fa lo stesso per l'oggetto: niente "mezze pratiche".

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare e usare un costruttore con parametri
- Far nascere un oggetto già coerente con gli invarianti di base

---

### ⚙️ In breve

```cpp
class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) {
        codice = c;
        setPrezzo(p);
    }
    void setPrezzo(double p);
    double getPrezzo() const;
};
```

Creazione: `Articolo a("A-100", 12.5);`

---

### 🔬 Laboratorio PRIMM: Articolo costruito bene

#### 1. PREDICT (Prevedi)

```cpp
class Articolo {
public:
    Articolo(const std::string& c, double p);
};
Articolo a("A-1", 10.0);
```

Dopo la costruzione di un Articolo con codice e prezzo tramite costruttore, i campi sono già impostati?


[(X)] Sì: il costruttore inizializza lo stato
[( )] No: serve sempre setCodice dopo
[( )] Solo se c'è anche il distruttore
[( )] No: i private restano indefiniti

<details>
<summary>💡 Spiegazione</summary>
Il costruttore viene eseguito alla creazione: codice e prezzo partono già impostati.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_ctor.cpp
 * @brief Costruttore che impone uno stato iniziale.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) {
        codice = c;
        if (p < 0.0) prezzo = 0.0;
        else prezzo = p;
    }
    double getPrezzo() const { return prezzo; }
    std::string getCodice() const { return codice; }
};

int main() {
    Articolo a("A-100", 12.5);
    Articolo b("B-200", -4.0);
    std::cout << a.getCodice() << " " << a.getPrezzo() << '\n';
    std::cout << b.getCodice() << " " << b.getPrezzo() << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Momento | Cosa succede |
|---------|----------------|
| `Articolo a(...)` | Alloca l'oggetto e chiama il costruttore |
| Corpo del ctor | Inizializza i campi private |
| Dopo | `main` usa solo metodi pubblici |

#### 4. MODIFY (Modifica)
1. Aggiungi `giacenza` al costruttore (default 0).
2. Costruttore a tre parametri: codice, prezzo, giacenza.
3. Metodo `scheda()` e usalo in `main` su due articoli.

#### 5. MAKE (Crea)
**Scenario SIA — Conto corrente ben formato**

`conto_costruttore.cpp`: classe `ContoCorrente` con IBAN, intestatario, saldo; costruttore che non lascia saldo iniziale negativo (o lo porta a 0); stampa riepilogo.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class ContoCorrente {
private:
    std::string iban;
    double saldo;
public:
    ContoCorrente(const std::string& i, double s);
};
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Costruttore = nascita controllata dell'oggetto
- Meglio invarianti rispettati **subito**
- Si può riusare la logica dei setter nel ctor
- Nome uguale alla classe, niente tipo di ritorno

---

### ➡️ Prossimo chunk
Cosa sa **fare** l'oggetto: metodi e responsabilità di reparto.


## 🛠️ Cosa sa fare il reparto: metodi e responsabilità

> "Il reparto non espone i cassetti: espone le *operazioni* consentite."  
> — *Servizi applicativi*

I **metodi** sono le mansioni dell’oggetto: caricare, scaricare, stampare la scheda.  
`main` coordina; l’oggetto applica le regole sul proprio stato.

> 💡 **Metafora: mansioni**  
> `carica(n)` e `scarica(n)` sono procedure interne al magazzino articolo, non calcoli sparsi in `main`.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Aggiungere metodi di istanza che modificano o leggono lo stato privato
- Assegnare responsabilità chiare all’oggetto (non al `main`)

---

### 🔬 Laboratorio PRIMM: Carico e scarico

#### 1. PREDICT (Prevedi)

```cpp
Articolo a("A", 1.0);
a.scheda();
```

Chi può chiamare un metodo public di Articolo?

[( )] Solo codice dentro la class
[(X)] Chiunque abbia un oggetto Articolo (es. main)
[( )] Solo il costruttore
[( )] Nessuno

<details>
<summary>💡 Spiegazione</summary>
I metodi public sono l’interfaccia usabile da <code>main</code> e da altre funzioni.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_metodi.cpp
 * @brief Metodi di business su Articolo.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    int giacenza;
public:
    Articolo(const std::string& c, int g) : codice(c), giacenza(g < 0 ? 0 : g) {}
    void carica(int n) {
        if (n > 0) giacenza += n;
    }
    bool scarica(int n) {
        if (n <= 0 || n > giacenza) return false;
        giacenza -= n;
        return true;
    }
    void scheda() const {
        std::cout << codice << " giacenza=" << giacenza << '\n';
    }
};

int main() {
    Articolo a("A-100", 10);
    a.carica(5);
    a.scarica(3);
    a.scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Metodo | Responsabilità |
|--------|----------------|
| `carica` | Aumenta giacenza se n>0 |
| `scarica` | Diminuisce solo se c’è disponibilità |
| `scheda` | Presenta lo stato (sola lettura) |

#### 4. MODIFY (Modifica)
1. Fai restituire a `scarica` un messaggio stampato in `main` in base al `bool`.
2. Aggiungi `int getGiacenza() const`.
3. Impedisci `carica` oltre una soglia massima (es. 1000).

#### 5. MAKE (Crea)
**Scenario SIA — Articolo di magazzino operativo**

`magazzino_articolo.cpp`: costruttore, `carica`, `scarica`, `scheda`; in `main` una piccola storia di movimenti.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo { /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Metodi = operazioni sullo stato dell’oggetto
- Regole di business vicino ai dati
- `main` orchestra, non micromanage i campi
- Nomi verbo+oggetto (`scarica`, `carica`)

---

### ➡️ Prossimo chunk
Metodi che **non** modificano lo stato: `const`.


## 👁️ Consultare senza modificare: metodi `const`

> "In audit puoi leggere la pratica, non alterarla."  
> — *Controllo interno*

Alcune operazioni sono di **sola lettura**: scheda, getter, report.  
In C++ si marca il metodo con **`const`**: promette di non modificare lo stato dell’oggetto.

> 💡 **Metafora: badge visitatore**  
> Entri in consultazione: vedi i documenti, non li firmi.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare metodi `const` per letture
- Usare oggetti `const` e capire perché servono getter `const`

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
void scheda() const { giacenza = 0; }
```

Un metodo `void scheda() const` può assegnare `giacenza = 0` nel corpo?

[( )] Sì
[(X)] No: metodo const non modifica lo stato
[( )] Solo se giacenza è public
[( )] Solo in main

<details>
<summary>💡 Spiegazione</summary>
Il <code>const</code> dopo i parametri vieta di modificare i membri non mutable dell’oggetto.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scheda_const.cpp
 * @brief Metodi const per sola lettura.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) : codice(c), prezzo(p < 0 ? 0 : p) {}
    double getPrezzo() const { return prezzo; }
    void scheda() const {
        std::cout << codice << " € " << prezzo << '\n';
    }
};

void stampa(const Articolo& a) {
    a.scheda();  // ok: scheda è const
}

int main() {
    const Articolo a("A-100", 9.5);
    stampa(a);
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Situazione | Consentito? |
|------------|-------------|
| `getPrezzo() const` su oggetto `const` | Sì |
| Metodo non-const su oggetto `const` | No |
| `const Articolo&` in lettura | Preferibile (niente copia, niente modifica) |

#### 4. MODIFY (Modifica)
1. Aggiungi `getCodice() const`.
2. Prova un metodo non-const su `const Articolo` e osserva l’errore del compilatore.
3. Formatta il prezzo con `iomanip` dentro `scheda() const`.

#### 5. MAKE (Crea)
**Scenario SIA — Scheda articolo in sola lettura**

`scheda_const.cpp`: classe con almeno due metodi `const`; funzione libera `stampa(const Articolo&)`.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo { /* getters const, scheda const */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- `const` sul metodo = sola lettura
- Getter e report devono essere `const`
- Oggetti `const` e riferimenti `const&` collaborano
- Errori di const-correttezza li segnala il compilatore

---

### ➡️ Prossimo chunk
Oggetti fatti di altri oggetti: **composizione**.


## 🧩 L’azienda è fatta di pezzi: composizione (“ha un”)

> "Un ordine *ha un* cliente e *ha* delle righe: non *è un* cliente."  
> — *Modellazione del dominio*

La **composizione** collega oggetti per contenimento: la parte è un membro della classe.  
È spesso più naturale dell’ereditarietà forzata.

> 💡 **Metafora:** la pratica d’ordine nel faldone *include* la scheda cliente (copia di lavoro) e le righe.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare una classe che **ha** un’altra classe come membro
- Costruire l’oggetto composto inizializzando le parti

---

### 🔬 Laboratorio PRIMM: Ordine con cliente

#### 1. PREDICT (Prevedi)

```cpp
class Ordine { Cliente cliente_; /* ... */ };
```

Se `Ordine` contiene un membro `Cliente cliente_`, la distruzione di `Ordine` coinvolge anche `cliente_`?

[(X)] Sì: il membro vive dentro l’oggetto composto
[( )] No: Cliente è sempre indipendente sullo heap
[( )] Solo con virtual
[( )] Solo con template

<details>
<summary>💡 Spiegazione</summary>
I membri oggetto hanno vita legata al contenitore: compositum e parte “value member”.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ordine_composizione.cpp
 * @brief Ordine ha un Cliente.
 */
#include <iostream>
#include <string>

class Cliente {
private:
    std::string nome;
public:
    Cliente(const std::string& n) : nome(n) {}
    std::string getNome() const { return nome; }
};

class Ordine {
private:
    int id;
    Cliente cliente;
    double totale;
public:
    Ordine(int i, const Cliente& c, double t)
        : id(i), cliente(c), totale(t < 0 ? 0 : t) {}
    void scheda() const {
        std::cout << "Ordine " << id << " — "
                  << cliente.getNome() << " — € " << totale << '\n';
    }
};

int main() {
    Cliente cl("Rossi SRL");
    Ordine o(1001, cl, 250.0);
    o.scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Classe | Ruolo |
|--------|--------|
| `Cliente` | Parte riusabile |
| `Ordine` | Composto: ha id, cliente, totale |
| Costruttore di `Ordine` | Inizializza anche il membro `cliente` |

#### 4. MODIFY (Modifica)
1. Aggiungi `getTotale() const` su `Ordine`.
2. Aggiungi un campo `std::string note` all’ordine.
3. Crea due ordini per lo stesso cliente (due oggetti `Ordine`).

#### 5. MAKE (Crea)
**Scenario SIA — Ordine di vendita**

`ordine_cliente.cpp`: `Cliente` + `Ordine` in composizione; scheda leggibile; `main` dimostrativo.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Cliente { /* ... */ };
class Ordine { /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Composizione = “ha un”, non “è un”
- Membri oggetto costruiti col contenitore
- Preferisci composizione quando non c’è vera specializzazione
- Basi solide prima dell’ereditarietà

---

### ➡️ Prossimo chunk
Quando invece **è un** tipo specializzato: ereditarietà essenziale.


## 🌳 Specializzazioni in organigramma: ereditarietà essenziale

> "Entrata e uscita di cassa *sono* movimenti, con qualcosa in più."  
> — *Tassonomie contabili*

L’**ereditarietà** modellare il rapporto **“è un”**: la derivata riusa e specializza la base.  
In 3ª SIA restiamo a **due livelli**, una sola gerarchia semplice.

> 💡 **Metafora: organigramma**  
> `Movimento` generico; `Entrata` e `Uscita` specializzano il segno o l’etichetta.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare una classe derivata `public` da una base
- Riusare attributi/metodi comuni senza duplicarli

---

### 🔬 Laboratorio PRIMM: Movimenti

#### 1. PREDICT (Prevedi)

```cpp
class Base { public: void f(); };
class Der : public Base {};
```

Una classe derivata public eredita i membri public della base?

[(X)] Sì, può usare f() su un oggetto Der
[( )] No, mai
[( )] Solo se virtual
[( )] Solo nei template

<details>
<summary>💡 Spiegazione</summary>
Con ereditarietà <code>public</code>, l’interfaccia public della base è usabile sulla derivata.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file movimenti_base.cpp
 * @brief Ereditarietà a due livelli.
 */
#include <iostream>
#include <string>

class Movimento {
protected:
    std::string desc;
    double importo;
public:
    Movimento(const std::string& d, double i) : desc(d), importo(i) {}
    void scheda() const {
        std::cout << desc << " " << importo << '\n';
    }
};

class Entrata : public Movimento {
public:
    Entrata(const std::string& d, double i) : Movimento(d, i < 0 ? -i : i) {}
};

class Uscita : public Movimento {
public:
    Uscita(const std::string& d, double i) : Movimento(d, i > 0 ? -i : i) {}
};

int main() {
    Entrata e("Vendita", 50);
    Uscita u("Affitto", 20);
    e.scheda();
    u.scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Classe | “È un” Movimento? |
|--------|-------------------|
| `Entrata` | Sì |
| `Uscita` | Sì |
| `protected` in base | Visibile alle derivate, non a `main` |

#### 4. MODIFY (Modifica)
1. Aggiungi `getImporto() const` nella base.
2. In `Uscita`, stampa prefisso `"USCITA"` sovrascrivendo `scheda` (senza virtual ancora: chiama solo su tipo statico Uscita).
3. Crea un terzo movimento di prova.

#### 5. MAKE (Crea)
**Scenario SIA — Prima nota semplificata**

`movimenti_ereditati.cpp`: base + due derivate; `main` elenca alcune entrate/uscite.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Movimento { /* ... */ };
class Entrata : public Movimento { /* ... */ };
class Uscita : public Movimento { /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Ereditarietà = “è un”
- Una gerarchia poco profonda
- `protected` per le derivate
- Non usare ereditarietà al posto della composizione

---

### ➡️ Prossimo chunk
Stesso sportello, comportamento diverso a runtime: `virtual`.


## 🎭 Stesso sportello, comportamenti diversi: `virtual`

> "Chiami ‘stampa movimento’ allo sportello unico: dietro, procedure diverse."  
> — *Servizi uniformi, implementazioni specializzate*

Il **polimorfismo** via `virtual` permette di usare un puntatore/riferimento alla **base** e ottenere il comportamento della **derivata**.

> 💡 **Metafora:** un solo sportello “scheda”; ogni tipo di movimento risponde a modo suo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare un metodo `virtual` e fare override nella derivata
- Usare un puntatore alla base per invocare il comportamento dinamico

*Nota:* esempio didattico con puntatori; la gestione avanzata della memoria non è il focus.

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
Base* p = new Derivata();
p->scheda();
```

Con `scheda` virtuale e puntatore a Base che punta a Derivata, quale `scheda` viene chiamata?

[(X)] Quella della Derivata se scheda è virtual
[( )] Sempre e solo quella di Base
[( )] Nessuna
[( )] Solo se template

<details>
<summary>💡 Spiegazione</summary>
Con <code>virtual</code>, il tipo dinamico dell’oggetto decide quale versione eseguire.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file virtual_scheda.cpp
 * @brief Override virtuale di scheda().
 */
#include <iostream>
#include <string>

class Movimento {
protected:
    std::string desc;
public:
    Movimento(const std::string& d) : desc(d) {}
    virtual void scheda() const {
        std::cout << "MOV " << desc << '\n';
    }
};

class Entrata : public Movimento {
public:
    Entrata(const std::string& d) : Movimento(d) {}
    void scheda() const override {
        std::cout << "ENTRATA " << desc << '\n';
    }
};

int main() {
    Entrata e("Vendita bancone");
    Movimento* p = &e;
    p->scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Tipo statico di `p` | Tipo dinamico | `scheda` chiamata |
|---------------------|---------------|-------------------|
| `Movimento*` | `Entrata` | `Entrata::scheda` se virtual |

Togli `virtual` mentalmente: cosa cambierebbe?

#### 4. MODIFY (Modifica)
1. Aggiungi `Uscita` con override di `scheda`.
2. Chiama `scheda` su due puntatori diversi.
3. Aggiungi un campo importo e stampalo negli override.

#### 5. MAKE (Crea)
**Scenario SIA — Report eterogeneo**

`report_movimenti_virtual.cpp`: base con `virtual scheda`, almeno due derivate, dimostrazione via puntatori alla base.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Movimento { public: virtual void scheda() const; /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- `virtual` abilita il binding dinamico
- `override` rende esplicita l’intenzione
- Utile per collezioni eterogenee di “stesso ruolo”
- Restare su esempi piccoli in 3ª SIA

---

### ➡️ Prossimo chunk
Far parlare il dominio con operatori (`+` o `<<`).


## 💬 Linguaggio del dominio: overloading essenziale (`<<`)

> "Meglio `std::cout << articolo` che quattro getter in fila."  
> — *API leggibile*

L’**overloading** degli operatori adatta la sintassi al dominio.  
In questo chunk un solo focus: **`operator<<`** per l’output.

> 💡 **Metafora:** il modulo di stampa dello scontrino sa come disporre i campi dell’articolo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare `operator<<` per una classe semplice
- Stampare un oggetto con `std::cout << obj`

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
std::cout << articolo;
```

A cosa serve tipicamente sovraccaricare `operator<<` per una classe?

[(X)] Stampare l’oggetto in modo leggibile su uno stream
[( )] Aprire un file in automatico
[( )] Creare template
[( )] Sostituire il costruttore

<details>
<summary>💡 Spiegazione</summary>
<code>operator&lt;&lt;</code> definisce come inserire l’oggetto in uno <code>ostream</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_ostream.cpp
 * @brief operator<< per Articolo.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) : codice(c), prezzo(p) {}
    friend std::ostream& operator<<(std::ostream& os, const Articolo& a) {
        os << a.codice << " €" << a.prezzo;
        return os;
    }
};

int main() {
    Articolo a("A-100", 12.5);
    std::cout << a << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Elemento | Ruolo |
|----------|--------|
| `friend` | Accesso ai private per la stampa |
| `return os` | Consente `cout << a << b` |
| `const Articolo&` | Non modifica l’oggetto |

#### 4. MODIFY (Modifica)
1. Formatta il prezzo con due decimali (`iomanip`).
2. Aggiungi la giacenza in stampa.
3. Stampa due articoli in sequenza.

#### 5. MAKE (Crea)
**Scenario SIA — Scheda stampabile**

`stampa_articolo_op.cpp`: classe con `operator<<`; `main` dimostra almeno due stampe.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo { /* friend operator<< */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Un operatore per chunk: qui solo `<<`
- Restituisci lo stream
- Preferisci `const&` sul parametro oggetto
- Leggibilità del dominio > acrobazie

---

### ➡️ Prossimo chunk
Procedure uguali su tipi diversi: **funzioni template**.


## 🔧 Stessa procedura, tipi diversi: funzioni template

> "Il confronto ‘chi è maggiore’ vale per pezzi e per prezzi."  
> — *Riuso algoritmico*

Una **funzione template** descrive un algoritmo **generico**: il compilatore genera le versioni per i tipi usati.

> 💡 **Metafora:** modulo aziendale standard compilato per reparti diversi (stessa procedura, dati diversi).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una funzione `template <typename T>` semplice
- Usarla con tipi diversi (`int`, `double`)

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
massimo(3, 5);
massimo(2.5, 2.7);
```

Una funzione `template <typename T> T massimo(T a, T b)` può essere usata su `int` e su `double`?

[(X)] Sì, il compilatore istanzia le versioni necessarie
[( )] No, solo su int
[( )] Solo se T è class
[( )] No, serve virtual

<details>
<summary>💡 Spiegazione</summary>
Il compilatore crea istanze distinte di <code>massimo</code> per i tipi dedotti dagli argomenti.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file massimo_template.cpp
 * @brief Funzione template massimo.
 */
#include <iostream>

template <typename T>
T massimo(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << massimo(3, 5) << '\n';
    std::cout << massimo(2.5, 2.7) << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Chiamata | T dedotto |
|----------|-----------|
| `massimo(3, 5)` | `int` |
| `massimo(2.5, 2.7)` | `double` |

I tipi devono supportare `>`.

#### 4. MODIFY (Modifica)
1. Scrivi `template <typename T> void scambia(T& a, T& b)`.
2. Usa `scambia` su due `double`.
3. Prova `massimo` su due `char`.

#### 5. MAKE (Crea)
**Scenario SIA — Utility generiche**

`util_template.cpp`: `massimo` e `scambia` template; demo su quantità (`int`) e prezzi (`double`).

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
template <typename T>
T massimo(T a, T b) { /* ... */ }
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Template = algoritmo generico
- Istanziazione a compile-time
- T deve offrire le operazioni usate
- Non è magia runtime: è generazione di codice

---

### ➡️ Prossimo chunk
Usare un contenitore template della libreria: `std::vector`.


## 📦 Il magazzino elastico: usare `std::vector` (cliente del template)

> "Non prenotare 100 scaffali se oggi ne bastano 3: lo scaffale cresce con la merce."  
> — *Capacità operativa*

`std::vector<T>` è un array **dinamico** offerto dalla libreria: classe **template** già pronta.  
Qui sei **cliente**: la usi, non la riscrivi.

> 💡 **Metafora:** magazzino elastico — `push_back` aggiunge un pezzo, `size` dice quanti ce ne sono.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare `std::vector<T>`, usare `push_back`, `size`, indice e range-for
- Confrontare l’idea con l’array grezzo a dimensione fissa

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
std::vector<int> v;
v.push_back(3);
v.push_back(5);
```

Dopo `v.push_back(3); v.push_back(5);`, quanto vale `v.size()`?

[(X)] 2
[( )] 0
[( )] 5
[( )] Indefinito

<details>
<summary>💡 Spiegazione</summary>
Ogni <code>push_back</code> aggiunge un elemento: la size diventa 2.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file vector_importi.cpp
 * @brief vector di importi.
 */
#include <iostream>
#include <vector>

int main() {
    std::vector<double> importi;
    importi.push_back(10.0);
    importi.push_back(25.5);
    importi.push_back(7.0);

    double somma = 0.0;
    for (double x : importi) {
        somma += x;
    }
    std::cout << "N=" << importi.size() << " somma=" << somma << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Operazione | Significato |
|------------|-------------|
| `push_back` | Aggiunge in coda |
| `size()` | Quanti elementi |
| `v[i]` | Accesso (attenzione ai bounds) |
| range-for | Scorre tutti gli elementi |

#### 4. MODIFY (Modifica)
1. Stampa ogni importo su una riga.
2. Calcola il massimo con un ciclo.
3. Usa `std::vector<int>` per quantità pezzi.

#### 5. MAKE (Crea)
**Scenario SIA — Lista movimenti variabile**

`movimenti_vector.cpp`: `vector<double>` (o di `struct`/`class` se vuoi collegare il Blocco 3), caricamento di almeno 5 valori, somma e media.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <vector>
int main() {
    std::vector<double> v;
    // push_back ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- `vector` = sequenza dinamica
- `push_back` / `size` / range-for
- Preferibile all’array grezzo quando N non è fisso
- Sei utente di un template della std library

---

### ➡️ Prossimo chunk
Mettere insieme gli oggetti: **mini-progetto** gestionale.


## 🏗️ Mini-progetto: gestionale a oggetti in memoria

> "Chiudi il corso applicando reparti-oggetto a un caso aziendale completo (in RAM)."  
> — *Obiettivo di sintesi Blocco 3*

Questo capitolo è un **laboratorio di progetto**, non un nuovo costrutto isolato.  
Integra: `class`, costruttori, metodi, (opzionale) composizione o ereditarietà leggera, `std::vector`, output leggibile.

> 💡 **Metafora:** piccolo sistema informativo aziendale che vive mentre il programma è in esecuzione.

---

### 🎯 Obiettivo di questo chunk
Alla fine del progetto sei in grado di:
- Progettare almeno due classi coerenti con un dominio SIA
- Usare una collezione dinamica di oggetti e produrre un report

---

### 📋 Rubrica minima (Must)

| Requisito | Dettaglio |
|-----------|-----------|
| Classi | ≥ 2 classi con dati `private` e interfaccia `public` |
| Costruzione | Almeno un costruttore con parametri su ciascuna classe principale |
| Collezione | `std::vector` di oggetti (o di puntatori se usi polimorfismo) |
| Report | Output formattato (anche semplice) di elenco + totale/i |
| Documentazione | `@brief` sulle classi o sui metodi pubblici principali |

**Plus (Should):** composizione *oppure* ereditarietà a 2 livelli; metodo `const`; `operator<<`.

---

### 🔬 Traccia consigliata (PRIMM leggero)

#### 1. PREDICT (Prevedi)

```cpp
// rubrica progetto OOP
```

Nel mini-progetto, perché dati private + metodi public sono un requisito?

[(X)] Per proteggere gli invarianti e definire un’interfaccia chiara
[( )] Perché altrimenti non compila mai
[( )] Solo per usare vector
[( )] Solo per i template

#### 2. RUN — scheletro di partenza

```cpp
/**
 * @file gestionale_oop_stub.cpp
 * @brief Punto di partenza progetto.
 */
#include <iostream>
#include <string>
#include <vector>

// TODO: class Cliente / Articolo / Movimento ...

int main() {
    std::cout << "Gestionale OOP — in costruzione\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE
Definisci su carta: elenco classi, attributi private, metodi public, relazioni (ha-un / è-un).

#### 4. MODIFY
Implementa a incrementi: prima una classe, poi la seconda, poi il `vector`, poi i totali.

#### 5. MAKE (consegna Classroom50)
**Scenario a scelta (uno):**
- Magazzino articoli + giacenze e valore inventario  
- Prima nota: movimenti di cassa e saldo  
- Listino clienti + ordini (composizione)

File di consegna: `gestionale_oop.cpp` (e header se li separi).

<details>
<summary>💡 Scaffold minimo</summary>

```cpp
#include <iostream>
#include <string>
#include <vector>
class Articolo { /* ... */ };
int main() {
    std::vector<Articolo> magazzino;
    // ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Il progetto **unisce** i chunk 26–35
- Meglio poche classi chiare che tante vuote
- Invarianti e interfaccia public prima della “fantasia”
- Consegna = codice leggibile + report dimostrativo

---

### ➡️ Fine Blocco 3
Hai un percorso da `struct` a oggetti, template da utente e un gestionale in memoria.  
I prossimi passi “mondo reale” (file, GUI, DB) restano fuori da questo corso di base.
