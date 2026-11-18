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
> — Gregory Chaitin, *Alla ricerca di Omega*, Adelphi Edizioni

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

#### 1. PREDICT (Prevedi)

- Prima di eseguire il programma, esamina attentamente il codice sorgente e **ipotizza cosa farà**.
- Se il codice contiene condizioni, cicli o variabili che cambiano, costruisci sul quaderno una **tabella di traccia** (colonne con i valori assunti dalle variabili passo dopo passo).

#### Prima del Predict: orientati

- Leggi la breve teoria che presenta parole, struttura e regola indispensabili.
- Non cercare ancora la risposta del quiz: prepara soltanto gli strumenti per ragionare sul codice.

#### 2. RUN (Esegui)

- Copia il programma nel tuo ambiente di sviluppo (VS Code o blocco interattivo `@LIA.cpp`).
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

- Prima leggi il contesto, l'obiettivo e la micro-teoria: poi fai una previsione.
- Digita il codice a mano e confronta sempre output e Predict.
- Usa una tabella di traccia e Python Tutor quando cambiano variabili o memoria.
- Modifica poco alla volta; nel Make riusa l'idea in uno scenario nuovo.

---

### ➡️ Da dove si comincia

Prima di scrivere programmi, allestiamo l’**officina**: editor, compilatore e debugger.  
È una sessione di laboratorio, non una lettura di 20 minuti: senza utensili collaudati il resto del corso non parte.

## 🛠️ Prepara la tua Officina di Sviluppo: VS Code, MSYS2 e MinGW-w64

> "I programmi sono fatti per essere letti dagli esseri umani e solo incidentalmente per essere eseguiti dai computer."
> — Donald Knuth

Questo non è un capitolo da leggere in 20 minuti.  
È una **sessione di laboratorio**: allestire l’officina richiede tempo, pazienza e qualche tentativo. In classe può occupare un’ora intera (o più, se qualcuno ha imprevisti). Non correre.

Alla fine di questa sessione avrai:
- Visual Studio Code (il banco di lavoro)
- l’estensione C/C++ (gli utensili specializzati)
- il compilatore **g++** e il debugger **gdb** (tramite MSYS2 + MinGW-w64)
- la variabile PATH impostata correttamente
- un programma di prova compilato, eseguito e debuggato con successo

> 💡 **Metafora:**  
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


## ⚙️ Il Motore Sotto il Cofano: dalla sorgente all'eseguibile

> "La programmazione è l'arte di esprimere soluzioni ai problemi in modo che un computer possa eseguirle."
>
> — Bjarne Stroustrup

Hai appena allestito l’officina (VS Code + g++).  
Ora apriamo il cofano e guardiamo **cosa succede davvero** quando premi il pulsante di compilazione.

Il computer non capisce il C++. Capisce solo istruzioni macchina (sequenze di 0 e 1).  
Tra il file che scrivi tu (`.cpp`) e il programma che gira (`.exe`) c’è una **catena di montaggio** con quattro stazioni.

> 💡 **Metafora:**  
> Pensa a una **fabbrica di auto**.  
> - Il progetto su carta = il tuo file `.cpp`  
> - I reparti della fabbrica = pre-elaboratore, compilatore, assemblatore, linker  
> - L’auto finita che esce dal cancello = il file eseguibile  
> Ogni reparto fa un lavoro preciso. Se un pezzo è sbagliato, la catena si ferma e ti arriva una “notifica” (errore di compilazione).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Seguire il percorso di un programma C++ dal sorgente all'eseguibile e ispezionarne i file intermedi con `g++ -save-temps`

---

### ⚙️ Prima del laboratorio: dal sorgente all'eseguibile

Il percorso essenziale è questo:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
skinparam ArrowColor #000000
skinparam rectangle {
  BackgroundColor #DDDDDD
  BorderColor #000000
}
top to bottom direction

rectangle "ridotto.cpp\n(codice sorgente)" as SRC
rectangle "Compilatore" as COMP
rectangle "ridotto.o\n(codice oggetto)" as OBJ
rectangle "Linker" as LINK
rectangle "ridotto.exe\n(codice eseguibile)" as EXE

rectangle "codice di libreria" as LIB
rectangle "codice di avvio\n(start-up)" as START

SRC --> COMP
COMP --> OBJ
OBJ --> LINK
LIB --> LINK
START --> LINK
LINK --> EXE

SRC -[hidden]right-> LIB
COMP -[hidden]right-> START
@enduml
```

Il file `.cpp` che scrivi non viene eseguito direttamente: il compilatore e il
linker lo trasformano in un `.exe` pronto per Windows.

---

### 🧭 Prima del laboratorio: le quattro stazioni

Dentro la fase di traduzione ci sono quattro stazioni. Con `g++` le vediamo così:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center

rectangle ".cpp\nsorgente" as S
rectangle "Pre-elaboratore\n(.ii)" as P
rectangle "Compilatore\n(.s Assembly)" as C
rectangle "Assemblatore\n(.o oggetto)" as A
rectangle "Linker\n(+ librerie)\n.exe" as L

S -right-> P
P -right-> C
C -right-> A
A -right-> L
@enduml
```

| Stazione | Cosa fa | File tipico |
|----------|---------|-------------|
| **Pre-elaboratore** | Espande le direttive `#include`, rimuove i commenti, gestisce le macro | `.ii` |
| **Compilatore** | Controlla la sintassi e traduce il C++ in **Assembly** (linguaggio a basso livello ma ancora leggibile) | `.s` |
| **Assemblatore** | Traduce l’Assembly in codice macchina (oggetti non ancora eseguibili da soli) | `.o` |
| **Linker** | Unisce i file oggetto con le librerie (es. la parte di sistema che serve per `main`) e produce l’eseguibile finale | `.exe` |

> 💡 **Brain-friendly tip:** Il compilatore è un controllore pedante, non un indovino. Se dimentichi un punto e virgola, si ferma e ti segnala l’errore. Non cerca di “capire cosa volevi dire”.

---

### 🔬 Laboratorio PRIMM: Guarda sotto il cofano

Useremo il programma **più piccolo possibile** (senza ancora stampare nulla).  
Così concentriamo l’attenzione sulla catena di montaggio, non sull’output a video.

```cpp
int main() {
    return 0;
}
```

#### 1. PREDICT (Prevedi)


Dopo g++ -save-temps, quale file contiene il codice senza commenti?

```cpp
int main() { return 0; }
```

[( )] ridotto.o
[(X)] ridotto.ii
[( )] ridotto.exe
[( )] ridotto.s


#### 2. RUN (Esegui)
Prima esegui il programma minimo nel blocco, poi ripeti l'esperimento dal
terminale per lasciare visibili i file intermedi.

```cpp
int main() {
    return 0;
}
```
@LIA.cpp

Nella cartella del progetto digita:

```bat
g++ -save-temps -O0 -fverbose-asm ridotto.cpp -o ridotto.exe
```

Il flag `-save-temps` dice a g++: “non cancellare i file intermedi”.  
`-O0` disattiva le ottimizzazioni, così l’Assembly resta più leggibile.
`-fverbose-asm` annota ogni riga rilevante per mostrare la corrispondenza tra il codice assembly prodotto e quello C++ _sorgente_.


**Controllo:** nella cartella devono comparire almeno:
- `ridotto.ii`
- `ridotto.s`
- `ridotto.o`
- `ridotto.exe`

Prova anche:

```bat
ridotto.exe
echo %ERRORLEVEL%
```

(Su Windows `ERRORLEVEL` mostra il valore restituito da `main`. Dovresti vedere `0`.)

#### 3. INVESTIGATE (Investiga)
Apri i file intermedi con un editor di testo (o con `type ridotto.ii` / `type ridotto.s` nel Prompt).

| File | Cosa ci trovi | Perché è importante |
|------|---------------|---------------------|
| `ridotto.ii` | Codice "pulito" dopo il pre-elaboratore | Vedi cosa resta quando spariscono i commenti |
| `ridotto.s` | Assembly (ancora leggibile) | Colleghi una riga C++ a un'istruzione macchina |
| `ridotto.o` | Codice oggetto (binario) | Non è ancora un programma completo da solo |
| `ridotto.exe` | Eseguibile finale | È il prodotto della fabbrica, pronto da lanciare |

Nel file `.s` noterai istruzioni del tipo:
```asm
movl $0, %eax
```
Che, in pratica, prepara il valore di ritorno `0` (successo).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
int main() {
    return 0;
}
```

</details>

1. Cambia il programma in:
   ```cpp
   int main() {
       return 42;
   }
   ```
2. Ricompila con lo stesso comando:
   ```bat
   g++ -save-temps -O0 -fverbose-asm ridotto.cpp -o ridotto.exe
   ```
3. Riapri `ridotto.s` e cerca di nuovo l’istruzione `movl` / `mov`.

Cosa è cambiato?

[( )] È scomparsa l’istruzione di movimento
[(X)] Il valore letterale è passato da `$0` a `$42`
[( )] Il file `.s` è diventato molto più grande
[( )] Non viene più generato il file `.s`

<details>
<summary>💡 Spiegazione</summary>
Hai visto con i tuoi occhi la traduzione: una riga C++ ad alto livello (<code>return 42;</code>) diventa una precisa istruzione Assembly. Il compilatore non fa magia: fa <strong>traduzione</strong>.
</details>

Esegui di nuovo il programma e controlla il codice di uscita:

```bat
ridotto.exe
echo %ERRORLEVEL%
```

Dovresti vedere `42`.

#### 5. MAKE (Crea)
**Scenario aziendale:** un programma automatico importa gli ordini notturni.
Non deve ancora stampare nulla, ma deve restituire un codice di esito che un
altro programma possa leggere.

Crea `codice_uscita.cpp` che:
1. Contiene solo `main` e restituisce un codice tra 1 e 99 (diverso da 0 e 42).
2. Usa un commento `///` per spiegare cosa rappresenta il codice scelto.
3. Viene compilato con `-save-temps -fverbose-asm`.
4. Ti permette di verificare nel `.s` il numero scelto.
5. Mostra lo stesso numero con `echo %ERRORLEVEL%` dopo l'esecuzione.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
int main() {
    /// TODO: spiega l'esito dell'importazione.
    return 7;
}
```

</details>

**Non** usare ancora `#include <iostream>` né `std::cout`: restiamo concentrati sulla catena di compilazione.  
La stampa a video arriverà nel prossimo capitolo.

---

### 📝 Riepilogo tascabile
- C++ è un linguaggio **compilato**: il sorgente viene tradotto in eseguibile attraverso più stazioni.
- Le quattro fasi: **Pre-elaboratore → Compilatore → Assemblatore → Linker**.
- `g++ -save-temps` lascia i file intermedi (`.ii`, `.s`, `.o`) così puoi ispezionarli.
- `return N;` in `main` diventa, in Assembly, un’istruzione che mette `N` nel registro di ritorno.
- Gli errori di compilazione sono segnalazioni precise della fabbrica: imparare a leggerli è una competenza chiave.

---

### ➡️ Prossimo chunk
Finora il nostro programma non ha ancora *parlato* con noi.  
Nel prossimo capitolo gli daremo il megafono (`std::cout`) e scriveremo il primo vero dialogo: **Ciao, Mondo!**.

## 💬 Il Primo Dialogo con la Macchina: `std::cout` e il programma minimo

> "L'unico modo per imparare un nuovo linguaggio di programmazione è scrivere programmi in quel linguaggio."
>
> — *Brian Kernighan*

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
| `int main() { ... }` | Apri l'ufficio principale del programma. | L'esecuzione parte sempre da qui. |
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


Cosa fa std::cout << "Ciao, Mondo!\n"; ?

```cpp
std::cout << "Ciao, Mondo!\n";
```

[( )] Legge da tastiera
[(X)] Stampa Ciao, Mondo! e va a capo
[( )] Compila il programma


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

#### 3. INVESTIGATE (Investiga)

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
Nel prossimo capitolo gli daremo le **scatole** (le variabili) per ricordare i dati e gli insegneremo ad *ascoltare* (`std::cin`).


## 📝 Parlare al Futuro Te Stesso: documentazione Doxygen

> "Il codice non mente mai, i commenti sì."
>
> — *Ron Jeffries*

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




## 📦 Gli Sportelli della Memoria: variabili, costanti e tipi

> "Chi controlla il passato controlla il futuro: chi controlla il presente controlla il passato."
>
> — *George Orwell*

Finora abbiamo solo *stampato* testi fissi.  
Un software gestionale, però, deve **ricordare e aggiornare dati che cambiano**: prezzo di un articolo, giacenza di magazzino, saldo di un conto.

Per farlo usiamo **variabili** e **costanti**.

> 💡 **Metafora: i locker di ritiro pacchi**  
> La memoria RAM è una parete di **locker automatici** (come i punti di ritiro Amazon / InPost):
> - **La parete** = la RAM  
> - **Il numero dello sportello** = l’indirizzo di memoria (es. `0x7ffee4`) — lo usa il computer  
> - **L’etichetta sull’app** = il **nome della variabile** (`prezzo`, `giacenza`) — lo usi tu  
> - **La dimensione dello sportello** = il **tipo** (`int` piccolo, `double` medio, `string` variabile…)  
> - **La merce dentro** = il **valore**  
> - **Uno sportello sigillato** = una **costante (`const`)**: una volta inserito il valore, non si può più cambiare

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare e scegliere variabili e costanti con il tipo adatto a un dato aziendale

In questo chunk **non** chiediamo ancora dati da tastiera (`std::cin`): ci concentriamo su *ricordare* e *mostrare*. L’input arriverà quando servirà davvero nei laboratori successivi.

---

### ⚙️ Prima del laboratorio: i tipi di dato fondamentali

Prima di aprire uno sportello devi dire al compilatore **che tipo di merce** conterrà, così riserva lo spazio giusto.

| Tipo | Cosa contiene | Esempio | Note |
|------|---------------|-------------|------|
| `int` | Numeri interi (senza virgola) | `int giacenza = 42;` | Pezzi, quantità, conteggi |
| `double` | Numeri con la virgola | `double prezzo = 19.50;` | Prezzi, saldi, aliquote |
| `char` | Un solo carattere | `char reparto = 'A';` | Codici corti (tra apici singoli) |
| `bool` | Vero / falso | `bool inPromozione = true;` | Flag, condizioni |
| `std::string` | Testo di lunghezza variabile | `std::string nome = "Mouse";` | Serve `#include <string>` |
| `const T` | Valore **non modificabile** | `const double IVA = 0.22;` | Aliquote, limiti di legge, tassi |

> ⚠️ **Trappola classica:**  
> Se scrivi `int pezzi = 7.85;` il compilatore **non** arrotonda: **tronca** i decimali → diventa `7`.  
> Per i centesimi usa sempre `double`.

---

### 🧭 Prima del laboratorio: dichiarare e sigillare

Una dichiarazione unisce tre informazioni: **tipo**, **nome** e **valore**.
Il nome racconta il dato; il tipo dice al compilatore come conservarlo.

| Scrittura | Come leggerla |
|-----------|---------------|
| `int giacenza = 42;` | Uno sportello per un conteggio intero. |
| `double prezzo = 19.50;` | Uno sportello per un valore con centesimi. |
| `const double IVA = 0.22;` | Uno sportello sigillato: il valore non cambia durante il programma. |

Nel Predict osserva una conversione: il tipo scelto decide quale parte del valore
può essere conservata.

---

### 🔬 Laboratorio PRIMM: Scheda articolo di magazzino

Memorizziamo i dati di un articolo e li stampiamo: tipi diversi, uno sportello ciascuno.

#### 1. PREDICT (Prevedi)


Cosa stampa int pezzi = 7.85?

```cpp
int pezzi = 7.85;
std::cout << pezzi;
```

[( )] 7.85
[(X)] 7 (troncamento)
[( )] crash
[( )] 8 (arrotondamento)


<details>
<summary>💡 Spiegazione</summary>
<code>int</code> può contenere solo interi. Assegnare un valore con la virgola provoca <strong>troncamento</strong>, non arrotondamento. Per i prezzi e le quantità decimali serve <code>double</code>.
</details>

#### 2. RUN (Esegui)
Esegui il programma completo:

```cpp
/**
 * @file scheda_prodotto.cpp
 * @brief Anagrafica di un articolo di magazzino.
 */
#include <iostream>
#include <string>

/**
 * @brief Memorizza e stampa i dati di un prodotto.
 * @return int 0 se tutto è andato bene.
 */
int main() {
    /// Aliquota IVA ordinaria vigente (non modificabile)
    const double ALIQUOTA_IVA = 0.22;

    /// Denominazione commerciale
    std::string nomeArticolo = "Mouse Wireless Ottico";

    /// Codice reparto ('A' = Accessori, 'H' = Hardware)
    char codiceReparto = 'A';

    /// Pezzi presenti a magazzino
    int pezziInMagazzino = 42;

    /// Prezzo unitario al netto di IVA
    double prezzoNetto = 19.50;

    /// true se è attiva la garanzia estesa
    bool haGaranziaEstesa = true;

    std::cout << "=== SCHEDA ARTICOLO MAGAZZINO ===\n";
    std::cout << "Descrizione : " << nomeArticolo << "\n";
    std::cout << "Reparto     : " << codiceReparto << "\n";
    std::cout << "Giacenza    : " << pezziInMagazzino << " pezzi\n";
    std::cout << "Prezzo netto: " << prezzoNetto << " euro\n";
    std::cout << "Garanzia    : " << haGaranziaEstesa << "\n";  // 1 = true, 0 = false
    std::cout << "Aliquota IVA: " << ALIQUOTA_IVA << "\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Collega ogni “sportello” al suo ruolo.

| Nome nello sportello | Tipo | Perché quel tipo? | Si può cambiare dopo? |
|----------------------|------|-------------------|------------------------|
| `ALIQUOTA_IVA` | `const double` | È un valore di legge / listino, non deve essere modificato per sbaglio | No |
| `nomeArticolo` | `std::string` | Testo di lunghezza variabile | Sì |
| `codiceReparto` | `char` | Un solo carattere di classificazione | Sì |
| `pezziInMagazzino` | `int` | Si contano pezzi interi | Sì |
| `prezzoNetto` | `double` | Serve la virgola (centesimi) | Sì |
| `haGaranziaEstesa` | `bool` | Solo due stati: sì / no | Sì |

> 🔗 Apri il codice su [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva come nascono le variabili nello stack.

#### 4. MODIFY (Modifica)
Apporta le modifiche **una alla volta** e verifica.

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

1. **Calcolo IVA**  
   Dichiara `double importoIva = prezzoNetto * ALIQUOTA_IVA;`  
   e stampa il prezzo lordo (`prezzoNetto + importoIva`).

2. **Prova del lucchetto**  
   Aggiungi a metà programma la riga:
   ```cpp
   ALIQUOTA_IVA = 0.10;
   ```
   Cosa dice il compilatore?

   [( )] Compila e cambia l’aliquota
   [(X)] Segnala un errore (variabile di sola lettura)
   [( )] Ignora la riga in silenzio
   [( )] Stampa un avviso ma produce l’eseguibile

   Un compilatore come g++ può segnalare:

   ```text
   error: assignment of read-only variable 'ALIQUOTA_IVA'
   ```

   <details>
   <summary>💡 Spiegazione</summary>
   Una variabile dichiarata <code>const</code> è in sola lettura. Il compilatore rifiuta qualsiasi assegnamento successivo (es. <code>assignment of read-only variable</code>).
   </details>

3. **Inizializzazione moderna (opzionale)**  
   Prova la forma con graffe: `int scorte{100};`  
   È consigliata negli standard moderni perché è più sicura contro conversioni indesiderate.

#### 5. MAKE (Crea)
**Scenario SIA — Scheda conto corrente aziendale**

Scrivi da zero `conto_corrente.cpp` che memorizza e visualizza:

| Dato | Tipo suggerito |
|------|----------------|
| Nome della banca | `std::string` |
| Codice IBAN | `std::string` |
| Saldo contabile | `double` |
| Tasso di interesse annuo | `const double` |
| Fido concesso (sì/no) | `bool` |
| Classe di rating (es. `'A'`) | `char` |

**Requisiti:**
- Intestazione Doxygen del file e di `main`
- Commento `///` sul “perché” di ogni variabile importante
- Calcola e stampa la stima degli interessi annui: `saldo * tasso`
- Non modificare la costante del tasso dopo l’inizializzazione

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Scheda sintetica di un conto corrente aziendale.
 */
#include <iostream>
#include <string>

int main() {
    /// TODO: spiega perché il tasso è una costante del conto.
    // TODO: dichiara i dati e stampa gli interessi stimati
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- Variabile = sportello etichettato in memoria (nome + tipo + valore).
- Il **tipo** decide quanto spazio riservare e quali operazioni sono legali.
- `int` tronca i decimali; per i soldi usa `double`.
- `const` rende lo sportello **sigillato**: utile per aliquote, tassi, limiti.
- `std::string` richiede `#include <string>`.
- Scegli sempre il tipo in base al significato aziendale del dato, non a caso.

---

### ➡️ Prossimo chunk
Ora che sappiamo *memorizzare* i dati, impariamo a *calcolarli* e a prendere decisioni semplici con le espressioni e l’operatore ternario.


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


Cosa stampa int pezzi = 5; double t = pezzi / 2 * 10.0; ?

```cpp
int pezzi = 5;
double t = pezzi / 2 * 10.0;
std::cout << t;
```

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




## 🚦 Bivi e Decisioni: `if` e `if-else`

> "Le decisioni sono i binari su cui viaggiano i processi aziendali."
> — *Principio di Ingegneria Gestionale*

Finora i programmi correvano su un unico binario.  
Nel mondo reale un pagamento può essere **approvato o rifiutato**, una giacenza **sufficiente o sotto scorta**, un badge **valido o no**.

Per gestire i bivi usiamo **`if`** e **`if-else`**.

> 💡 **Metafora: il tornello aziendale**  
> - **`if` semplice** = sensore di allarme: se rileva un’anomalia fa qualcosa; se non rileva nulla, non fa niente e il flusso continua.  
> - **`if-else`** = lettore badge al tornello:  
>   - *SE* badge valido → verde, passa  
>   - *ALTRIMENTI* → rosso, bloccato  
>   Non esistono vie di mezzo: si attiva **un solo** ramo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un `if` o un `if-else` con graffe per scegliere il ramo corretto

---

### ⚙️ Prima del laboratorio: i due modelli

**`if` semplice** — esegui un blocco *solo se* la condizione è vera:

```cpp
if (giacenza < LIVELLO_MINIMO) {
    std::cout << "ATTENZIONE: scorte in esaurimento!\n";
}
```

**`if-else`** — scegli **esattamente uno** dei due rami:

```cpp
if (saldo >= importo) {
    std::cout << "Pagamento approvato\n";
} else {
    std::cout << "Fondi insufficienti\n";
}
```

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Leggi saldo e importo;
if (saldo >= importo?) then (sì)
  :Transazione approvata;
  :Aggiorna saldo;
else (no)
  :Transazione rifiutata;
  :Mostra importo mancante;
endif
:Stampa esito;
stop
@enduml
```

---

### 🧭 Prima del laboratorio: costruire una condizione

Una condizione produce `true` o `false`. Il tornello apre solo quando la sua
regola è vera; se servono due controlli, `&&` significa che devono superarsi
entrambi.

| Condizione | Significato al tornello |
|------------|-------------------------|
| `saldo >= importo` | Il credito basta per il pagamento. |
| `pinInserito == PIN_SEGRETO` | Il codice è corretto. |
| `pinInserito == PIN_SEGRETO && badgeDirigente` | PIN e badge sono validi. |

---

### ⚠️ I due grandi tranelli

**1. Il punto e virgola traditore**

```cpp
// SBAGLIATO: il ; chiude subito l'if
if (saldo >= importo);
{
    std::cout << "Approvato\n";  // viene eseguito SEMPRE
}
```

Dopo la `)` della condizione **non va mai** il `;`: il codice compila, ma il
blocco successivo non appartiene più all'`if` e viene eseguito sempre.

**2. Graffe**

Senza `{ }` l’`if` controlla **solo** la prima istruzione successiva.  
**Usa sempre le graffe**, anche per una sola riga.

---

### 🔬 Laboratorio PRIMM: Terminale pagamenti POS

Il terminale decide se autorizzare un pagamento confrontando saldo e importo.

#### 1. PREDICT (Prevedi)


Senza graffe, quante righe controlla l'if?

```cpp
if (scorte < 5)
    std::cout << "1\n";
    std::cout << "2\n";
```

[( )] Entrambe le cout
[(X)] Solo la prima cout
[( )] Nessuna


<details>
<summary>💡 Spiegazione</summary>
Senza graffe, l’<code>if</code> controlla solo la riga 1.  
Condizione falsa → riga 1 saltata.  
Riga 2 e 3 sono istruzioni indipendenti: vengono eseguite.  
<strong>Regola d’oro: graffe sempre.</strong>
</details>

#### 2. RUN (Esegui)
Digita e esegui:

```cpp
/**
 * @file autorizzazione_pos.cpp
 * @brief Verifica fondi e autorizza (o nega) un pagamento POS.
 */
#include <iostream>

/**
 * @brief Controlla saldo vs importo e aggiorna il saldo se possibile.
 * @return int 0 se la procedura è terminata.
 */
int main() {
    double saldoDisponibile = 45.00;
    double importoSpesa = 62.50;

    std::cout << "=== TERMINALE PAGAMENTI POS ===\n";
    std::cout << "Importo richiesto: " << importoSpesa << " EUR\n";
    std::cout << "Verifica disponibilita...\n\n";

    if (saldoDisponibile >= importoSpesa) {
        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << ">>> TRANSAZIONE APPROVATA <<<\n";
        std::cout << "Nuovo saldo: " << saldoDisponibile << " EUR\n";
    } else {
        std::cout << ">>> TRANSAZIONE NEGATA <<<\n";
        std::cout << "Credito insufficiente.\n";
        std::cout << "Importo mancante: "
                  << importoSpesa - saldoDisponibile << " EUR\n";
    }

    std::cout << "\nOperazione conclusa.\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Con i valori dell’esempio (`saldo = 45`, `importo = 62.50`):

| Punto | Cosa succede |
|-------|----------------|
| Condizione `saldo >= importo` | `false` |
| Ramo eseguito | `else` |
| `importoSpesa - saldoDisponibile` | `17.50` |
| Dopo l’`if-else` | messaggio “Operazione conclusa” |

Prova a cambiare `importoSpesa` in `30.00` e riesegui: ora si attiva il ramo `if` e il saldo viene aggiornato.

> 🔗 Ispeziona lo stack su [Python Tutor C++](https://pythontutor.com/cpp.html):
> osserva saldo, importo e il ramo che viene eseguito.

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
if (saldoDisponibile >= importoSpesa) {
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
}
```

</details>

1. **Guardiano sottoscorta**  
   Aggiungi `int rotoloCartaTermica = 3;`.  
   Con un `if` **semplice** (senza else): se `< 5`, stampa un allarme per sostituire il rotolo.

2. **Micro-pagamento**  
   Se `importoSpesa < 10.00`, aggiungi una commissione fissa di `0.30` **prima** del controllo sul saldo.

3. **Importo esatto**
   Cambia `importoSpesa` in `45.00`. Prevedi e verifica quale ramo si attiva:
   il confronto include anche il caso in cui saldo e importo sono uguali.

#### 5. MAKE (Crea)
**Scenario SIA — Controllo accessi al caveau**

Scrivi `controllo_caveau.cpp`:

- `const int PIN_SEGRETO = 4821;`
- `int pinInserito` (es. `4821`)
- `bool badgeDirigente` (`true` / `false`)
- **Regola:** apri il caveau **solo se** PIN corretto **e** badge dirigente (`&&`)
  - se ok → messaggio di benvenuto / sblocco
  - altrimenti → “ACCESSO NEGATO” + attivazione telecamere
- Nel ramo `else`, se `pinInserito != 0`, aggiungi anche: tentativo registrato nel log

**Requisiti:** Doxygen, commenti `///`, graffe su tutti i blocchi, indentazione chiara.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Controllo accessi caveau (PIN + badge dirigente).
 */
#include <iostream>

int main() {
    const int PIN_SEGRETO = 4821;
    /// TODO: spiega perché servono due controlli di sicurezza.
    // TODO: dichiara pinInserito e badgeDirigente, poi scrivi l'if-else
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `if` = azione opzionale; `if-else` = bivio a due vie (un solo ramo eseguito).
- **Mai** `;` subito dopo la condizione.
- **Sempre** le graffe `{ }`, anche per una sola istruzione.
- `&&` richiede che entrambe le condizioni siano vere.

---

### ➡️ Prossimo chunk
Quando i bivi diventano **più di due** (es. fasce di sconto, giudizi, stati di un ordine) un solo `if-else` non basta.  
Passeremo a catene `if / else if / else` e alle regole per non perdere il controllo del flusso.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: if e if-else con condizioni semplici o composte
  [x] Metafora tornello
  [x] Quiz sintassi corretta
  [x] Predict sulla trappola delle graffe mancanti
  [x] PRIMM su terminale POS
  [x] Make su caveau (SIA / sicurezza)
  [x] else-if non introdotto (solo annunciato)
-->



## 🌲 Scaglioni Ordinati: `if / else if / else`

> "La complessità di un problema si risolve dividendolo in livelli ordinati di decisioni."
> — *Principio dell'Analisi dei Sistemi*

Con `if-else` gestiamo un bivio a due strade.  
Nei contesti aziendali le scelte sono spesso **a scaglioni**: fasce di sconto, livelli di fido, aliquote fiscali.  
Serve una **scala** `if / else if / else`, che controlla le fasce in ordine.

> 💡 **Metafora: nastro di smistamento logistico**  
> - **Scala `if / else if / else`** = sensori in sequenza sul nastro: il primo che “prende” il pacco lo devia e **i successivi non lo vedono più**.  

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una scala `if / else if / else` ordinata per classificare un dato in fasce esclusive

---

### ⚙️ Prima del laboratorio: la scala `if / else if / else`

Per alternative **disgiunte** (se ne vale una, le altre no):

```cpp
if (fatturato >= 50000.0) {
    sconto = 0.15;          // Platinum
} else if (fatturato >= 20000.0) {
    sconto = 0.10;          // Gold
} else if (fatturato >= 5000.0) {
    sconto = 0.05;          // Silver
} else {
    sconto = 0.0;           // nessuna fascia
}
```

**Ordine critico:** metti prima le soglie più restrittive (es. ≥ 50000 prima di ≥ 20000).  
Se invertissi l’ordine, un cliente Platinum verrebbe classificato Gold.

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Leggi fatturato;
if (fatturato >= 50000?) then (sì)
  :Platinum 15%;
elseif (fatturato >= 20000?) then (sì)
  :Gold 10%;
elseif (fatturato >= 5000?) then (sì)
  :Silver 5%;
else (no)
  :Nessuno sconto;
endif
stop
@enduml
```

---

### 🧭 Prima del laboratorio: l'ordine decide il risultato

Per una scala, chiedi prima la fascia più difficile da raggiungere. Se mettessi
`>= 20000` prima di `>= 50000`, un cliente Platinum sarebbe fermato dal sensore
Gold e non arriverebbe mai al successivo.

---

### 🔬 Laboratorio PRIMM: Fasce sconto cliente

Assegniamo la fascia sconto del cliente con controlli in sequenza.

#### 1. PREDICT (Prevedi)


Con fatturato = 25000, quale fascia assegna la scala corretta (≥50000 / ≥20000 / ≥5000)?

```cpp
double fatturato = 25000.0;
// if / else if / else sulle soglie
```

[( )] Platinum 15%
[(X)] Gold 10%
[( )] Silver 5%
[( )] Nessuno sconto


<details>
<summary>💡 Spiegazione</summary>
<code>85 >= 90</code> è falso → si passa al primo <code>else if</code>.  
<code>85 >= 60</code> è vero → stampa <code>Sufficiente</code> e <strong>salta</strong> il resto della catena.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file fasce_sconto_cliente.cpp
 * @brief Assegna fascia sconto per fatturato e valuta un fido semplice.
 */
#include <iostream>
#include <string>

/**
 * @brief Classifica il cliente e stampa esito sconto/fido.
 * @return int 0 se ok.
 */
int main() {
    std::string ragioneSociale = "Alpha Logistica Srl";
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

    std::cout << "Cliente : " << ragioneSociale << "\n";
    std::cout << "Fatturato: " << fatturato << " euro\n";
    std::cout << "Fascia   : " << fascia << " (sconto " << sconto * 100 << "%)\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Con `fatturato = 32500`:

| Passo | Condizione | Esito |
|-------|------------|-------|
| `>= 50000` | falso | passa oltre |
| `>= 20000` | vero | `sconto = 0.10`, fascia Gold |
| resto della scala | — | **non eseguito** |

> 🔗 Segui il flusso su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
if (fatturato >= 50000.0) {
    sconto = 0.15;
} else if (fatturato >= 20000.0) {
    sconto = 0.10;
} else {
    sconto = 0.0;
}
```

</details>

1. **Fascia Diamond**  
   In cima alla scala: se `fatturato >= 100000` → sconto `0.20`.  
   Verifica con `120000` che non resti classificato Platinum.

2. **Ordine sbagliato (esperimento)**
   Inverti temporaneamente le soglie Gold e Platinum e osserva cosa succede a un fatturato di `60000`.

#### 5. MAKE (Crea)
**Scenario SIA — Scaglioni di imposta (modello didattico semplificato)**

Scrivi `imposte_reddito.cpp`:

- `std::string nomeDitta`
- `double redditoImponibile` (es. `38500`)
- **Aliquota unica per fascia** (semplificazione didattica, non il calcolo progressivo reale):
  - ≤ 15000 → 23%
  - ≤ 28000 → 25%
  - ≤ 50000 → 35%
  - oltre → 43%
- Imposta stimata = `redditoImponibile * aliquota`
- Output: prospetto con fascia, aliquota e imposta stimata

**Requisiti:** Doxygen, `///` sulle aliquote, scala `if / else if / else` ordinata.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Stima imposta per scaglioni (modello didattico).
 */
#include <iostream>
#include <string>

int main() {
    /// TODO: spiega perché la soglia più alta viene controllata per prima.
    // TODO: dichiara dati, scala aliquote e stampa prospetto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- Scala `if / else if / else` = alternative esclusive; **ordine delle soglie** decisivo.
- Al primo ramo vero il resto della catena viene saltato.
- Per molte costanti discrete (menu 1/2/3) nel prossimo capitolo useremo `switch`.

---

### ➡️ Prossimo chunk
Quando la decisione dipende da un **valore discreto** (tasto di menu, codice operazione, stato numerico), la scala di `else if` diventa verbosa.  
Entra in scena lo **`switch`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: scala else-if ordinata
  [x] Metafora nastro logistico
  [x] Quiz sintassi corretta
  [x] Predict sull'esclusività dei rami
  [x] PRIMM fasce sconto + fido
  [x] Make scaglioni imposta (modello semplificato esplicitato)
  [x] switch solo annunciato
-->
## 🎛️ Lo Smistatore di Sportello (`switch-case`)

> "La semplicità è il prerequisito per l'affidabilità di un'interfaccia utente."
> — *Edsger W. Dijkstra*

`if / else if` gestisce bene scaglioni e confronti (`>`, `<`, intervalli).  
Quando invece la scelta è un **valore discreto fisso** — tasto di menu `1/2/3`, codice `'A'/'B'/'C'` — una lunga catena di `else if (x == …)` diventa verbosa.  
Per questi casi il C++ offre lo **`switch-case`**.

> 💡 **Metafora: tastiera del distributore / ATM**  
> - Digiti un **codice preciso** (tasto `1`, `2`, `'A'`…).  
> - Lo **`switch`** legge il tasto e attiva lo scomparto giusto (`case`).  
> - Il **`break`** è il freno di fine erogazione: senza di esso la macchina continua e fa scendere anche i prodotti dei cassetti successivi (*fall-through*).  
> - **`default`** = “codice non valido” sullo schermo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere uno `switch` su un codice discreto usando `case`, `break` e `default`

---

### ⚙️ Prima del laboratorio: anatomia dello switch

```cpp
switch (scelta) {
    case 1:
        // prelievo
        break;
    case 2:
        // versamento
        break;
    case 3:
        // saldo
        break;
    default:
        // opzione non valida
        break;  // consigliato anche qui
}
```

**Regole ferree in C++:**
1. L’espressione dello `switch` deve essere di tipo **intero o carattere** (non `double`, non `std::string`).
2. Ogni `case` confronta con una **costante** (letterale o `const`/`constexpr`), non con un intervallo.
3. Senza `break`, l’esecuzione **continua** nei `case` successivi (fall-through). Di solito è un bug; a volte è voluto (es. `'A'` e `'a'`).

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Leggi codice scelta;
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
endswitch
:Prosegui;
stop
@enduml
```

---

### 🧭 Prima del laboratorio: quando usare switch

| Situazione | Preferisci |
|------------|------------|
| Menu 1/2/3, codici carattere, stati numerici fissi | `switch` |
| Scaglioni (`>= 50`, intervalli), condizioni composte | `if / else if` |
| Confronti su `double` o `std::string` | `if / else if` |

---

### 🔬 Laboratorio PRIMM: Menu ATM

Un menu a tasti fissi smista prelievo, versamento e saldo.

#### 1. PREDICT (Prevedi)


Con `tasto = 1`, cosa stampa questo frammento **senza** `break` dopo il primo case?

```cpp
switch (tasto) {
    case 1:
        std::cout << "Saldo ";
    case 2:
        std::cout << "Estratto Conto ";
    default:
        std::cout << "Errore";
}
```

[( )] Stampa solo `Saldo `
[(X)] Stampa `Saldo Estratto Conto Errore`
[( )] Stampa `Saldo Estratto Conto `


<details>
<summary>💡 Spiegazione</summary>
Senza <code>break</code>, dopo <code>case 1</code> l’esecuzione “cade” nei case successivi (*fall-through*).  
Per fermarsi serve un <code>break</code> in ogni ramo (salvo quando il fall-through è intenzionale).
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file menu_atm.cpp
 * @brief Menu semplificato di uno sportello bancomat.
 */
#include <iostream>

/**
 * @brief Esegue un'operazione ATM in base al tasto scelto.
 * @return int 0 se ok.
 */
int main() {
    int sceltaMenu = 2;   // simula il tasto premuto dal cliente

    std::cout << "=== SPORTELLO ATM ===\n";
    std::cout << "1. Prelievo fisso 50 EUR\n";
    std::cout << "2. Versamento fisso 100 EUR\n";
    std::cout << "3. Visualizza saldo\n";
    std::cout << "0. Esci\n";
    std::cout << "Scelta: " << sceltaMenu << "\n\n";

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

#### 3. INVESTIGATE (Investiga)
Con `sceltaMenu = 2`:

| Passo | Cosa succede |
|-------|----------------|
| `switch` valuta `2` | salta direttamente a `case 2` |
| `case 2` | stampa l'operazione selezionata |
| `break` | esce dallo `switch` (non esegue case 3/default) |

Prova a togliere il `break` del `case 2` e riesegui: vedrai anche l’output del saldo (fall-through).

#### 4. MODIFY (Modifica)
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

1. **Ricarica telefonica**  
   Aggiungi `case 4:` con addebito fisso di `20.00` (se il saldo basta) e relativo `break`.

2. **Doppio tasto di uscita**  
   Fai sì che sia `0` sia `9` eseguano l’uscita, usando fall-through intenzionale:
   ```cpp
   case 0:
   case 9:
       std::cout << "Arrivederci.\n";
       break;
   ```

3. **Tipo sbagliato**  
   Prova `double sceltaMenu = 2.0;` nello `switch`: il compilatore segnala che la quantità non è intera.

   Un compilatore come g++ può segnalare:

   ```text
   error: switch quantity not an integer
   ```

#### 5. MAKE (Crea)
**Scenario SIA — Convertitore valute al POS**

Scrivi `cambio_valute.cpp`:

- `double importoValutaEstera` (es. `120.00`)
- `char codiceValuta`:
  - `'U'` / `'u'` → USD, tasso `0.92`
  - `'G'` / `'g'` → GBP, tasso `1.18`
  - `'J'` / `'j'` → JPY, tasso `0.0061`
  - `'S'` / `'s'` → CHF, tasso `1.05`
  - altro → `default`: “Valuta non supportata”
- Usa fall-through per maiuscole/minuscole
- Se valida: stampa importo originale, tasso, controvalore in euro

**Requisiti:** `///` sui tassi e `break` corretti; aggiungi Doxygen solo se il
programma supera circa 15 righe.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Conversione valuta estera in euro al POS.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché ogni tasso dipende dalla valuta selezionata.
    // TODO: dichiara importo e codice, poi scrivi lo switch
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `switch` = selezione su valori **discreti** (`int`, `char`).
- Ogni ramo utile termina di solito con `break`.
- Senza `break` → fall-through (a volte voluto, spesso bug).
- `default` gestisce i codici non previsti.
- Per intervalli e confronti su `double`/`string` resta l’`if / else if`.

---

### ➡️ Prossimo chunk
Finora il flusso va avanti o sceglie un ramo, ma non **ripete**.  
Nel prossimo capitolo entra in scena il ciclo: il **`while`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: switch, break, default, fall-through
  [x] Metafora distributore/ATM
  [x] Quiz sintassi corretta
  [x] Predict sul fall-through
  [x] PRIMM menu ATM
  [x] Make cambio valute (SIA)
  [x] while solo annunciato
-->

## 🔄 L'Anello Fondamentale (Il Ciclo `while`)

> "Iterare è umano, automatizzare è informatica."
> — *Adattamento da L. Peter Deutsch*

Quanti articoli ha un cliente al nastro della cassa? 3, 12, 75… non lo sai in anticipo.  
Con soli `if` e variabili fisse finiresti a dichiarare `prezzo1`, `prezzo2`, … sperando che bastino.

La potenza del computer sta nel **ripetere** lo stesso blocco **finché** una condizione resta vera.  
La forma più essenziale di questa ripetizione è il ciclo **`while`**.

> 💡 **Metafora: nastro della cassa**  
> - Finché c’è un articolo da scansionare (**condizione vera**), il nastro avanza e il totale cresce.  
> - Quando arriva il separatore con **valore sentinella** (es. `0`), la condizione diventa falsa: il rullo si ferma e si emette lo scontrino.  
> - Carrello vuoto già all’inizio → il nastro **non fa neppure un giro** (zero iterazioni).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un ciclo `while` che legge dati fino a una sentinella, aggiornando la condizione a ogni giro

---

### ⚙️ Prima del laboratorio: controllo in testa e tre ingredienti

Il `while` verifica la condizione **prima** di entrare nel corpo.

```cpp
// 1. Inizializzazione
double prezzo = 0.0;
std::cin >> prezzo;

// 2. Condizione di continuazione
while (prezzo != 0.0) {
    // corpo: accumula, conta, ...
    // 3. Aggiornamento (nuova lettura)
    std::cin >> prezzo;
}
```

| Ingrediente | Ruolo | Se manca… |
|-------------|-------|-----------|
| **Inizializzazione** | Valore di partenza *prima* del ciclo | Comportamento indefinito / non entra mai |
| **Condizione** | Decide se ripetere | Ciclo assente o infinito |
| **Aggiornamento** | Fa evolvere la variabile di controllo | **Ciclo infinito** |

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Inizializza variabile di controllo;
while (Condizione vera?) is (sì)
  :Corpo del ciclo;
  :Aggiorna variabile di controllo;
endwhile (no)
:Continua dopo il ciclo;
stop
@enduml
```

---

### 🧭 Prima del laboratorio: la sentinella ferma il nastro

La sentinella è un valore che non rappresenta un articolo: è il separatore
finale. Leggila prima del ciclo e alla fine di ogni giro, ma non sommarla mai.

| Valore letto | Il ciclo continua? | Va nel totale? |
|--------------|-------------------|----------------|
| `12.50` | sì | sì |
| `0.0` (sentinella) | no | no |

---

### 🔬 Laboratorio PRIMM: Scontrino a nastro

Accumuiamo i prezzi finché non arriva la sentinella di fine spesa.

#### 1. PREDICT (Prevedi)


Quante volte viene stampata la parola "Elaborazione"?

```cpp
int n = 0;
while (n > 5) {
    std::cout << "Elaborazione\n";
    n = n + 1;
}
```

[(X)] 0 volte (non viene mai stampata)
[( )] 1 volta
[( )] 5 volte
[( )] Il ciclo è infinito


<details>
<summary>💡 Spiegazione</summary>
All’ingresso <code>n > 5</code> è falso (<code>0 > 5</code>).  
Il <code>while</code> ha controllo in testa: se la condizione è già falsa, il corpo non viene eseguito mai.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scontrino_nastro.cpp
 * @brief Accumula i prezzi finché non arriva la sentinella 0.
 */
#include <iostream>

/**
 * @brief Legge prezzi da nastro (sentinella 0) e stampa totale e pezzi.
 * @return int 0 se ok.
 */
int main() {
    double totaleSpesa = 0.0;
    int numeroArticoli = 0;

    double prezzoArticolo = 0.0;
    std::cout << "Prezzo articolo (0 per terminare): ";
    std::cin >> prezzoArticolo;

    while (prezzoArticolo != 0.0) {
        totaleSpesa += prezzoArticolo;
        numeroArticoli += 1;
        std::cout << "  + " << prezzoArticolo << " EUR (pezzi: " << numeroArticoli << ")\n";

        std::cout << "Prezzo articolo (0 per terminare): ";
        std::cin >> prezzoArticolo;
    }

    std::cout << "=== SCONTRINO ===\n";
    std::cout << "Articoli: " << numeroArticoli << "\n";
    std::cout << "Totale  : " << totaleSpesa << " EUR\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Sequenza di esempio: `12.50` → `3.20` → `0.0`

| Iterazione | `prezzoArticolo` | Condizione | Totale dopo |
|------------|------------------|------------|-------------|
| ingresso | 12.50 | vero | 12.50 |
| 2ª | 3.20 | vero | 15.70 |
| 3ª lettura | 0.0 | **falso** → esce | 15.70 |

La sentinella `0` **non** viene sommata: il controllo avviene prima del corpo.

> 🔗 Osserva le variabili su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
double prezzoArticolo = 0.0;
std::cin >> prezzoArticolo;

while (prezzoArticolo != 0.0) {
    std::cin >> prezzoArticolo;
}
```

</details>

1. **Media per articolo**  
   Dopo il ciclo, se `numeroArticoli > 0`, stampa `totaleSpesa / numeroArticoli`.  
   Altrimenti messaggio “nessun articolo”.

2. **Scarta i negativi**  
   Se un prezzo è `< 0`, non accumularlo: stampa un avviso e continua.

3. **Ciclo infinito (esperimento controllato)**  
   Commenta l’aggiornamento di `prezzoArticolo` nel corpo.  
   La condizione resta vera per sempre → il programma non termina.  
   **Regola:** ogni ciclo deve aggiornare qualcosa che influisce sulla condizione.

#### 5. MAKE (Crea)
**Scenario SIA — Registro fatture fornitori**

Scrivi `fatture_fornitori.cpp`:

- Ciclo `while` che legge importi fattura
- Sentinella `-1.0` per terminare (**non** sommare la sentinella)
- Accumula `totaleDebiti`, conta fatture totali e quante sono “rilevanti” (`>= 1000`)
- A fine ciclo stampa:
  - totale debiti
  - numero fatture
  - numero rilevanti
  - percentuale rilevanti sul totale (se totale > 0)

**Requisiti:** Doxygen, `///` su contatori/accumulatori, sentinella gestita correttamente.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Registra fatture fornitori fino alla sentinella -1.
 */
#include <iostream>

int main() {
    // inizializza totali e contatori
    // leggi primo importo
    // while (importo != -1.0) { ... aggiorna ... leggi di nuovo }
    // stampa riepilogo
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `while` = ripeti **mentre** la condizione è vera (controllo in testa).
- Tre ingredienti: inizializza → controlla → aggiorna.
- Sentinella = valore speciale che dice “basta” (es. `0` o `-1`).
- Senza aggiornamento → ciclo infinito.
- Zero iterazioni è un comportamento normale se la condizione è già falsa.

---

### ➡️ Prossimo chunk
Quando sai già **quante** volte ripetere (es. 12 mesi, 30 giorni, 100 pezzi), il `while` funziona ma è verboso.  
Il ciclo **`for`** concentra inizializzazione, condizione e aggiornamento in una riga.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: while, sentinella, tre ingredienti, no infinito
  [x] Metafora nastro cassa
  [x] Quiz sintassi corretta
  [x] Predict: zero iterazioni
  [x] PRIMM scontrino (simulazione input per LiaScript)
  [x] Make fatture fornitori
  [x] for solo annunciato
-->

## ⏳ Il Contatore Compatto (Il Ciclo `for`)

> "La regolarità e la prevedibilità sono le migliori alleate della precisione contabile."
> — *Principio di Revisione Aziendale*

Il `while` è ideale quando **non sai quanti** giri farai (articoli al nastro, fatture fino alla sentinella).  
In azienda però molte ripetizioni sono **già note**: 5 anni di ammortamento, 12 mesi, 24 rate.

Con un `while` i tre ingredienti restano sparsi nel file: è facile dimenticare l’aggiornamento.  
Il ciclo **`for`** li raccoglie in **una sola riga**.

> 💡 **Metafora: timer del microonde / macchina industriale**  
> Imposti sul display: *“Parti da 1; fermati a 5; avanza di 1 a ogni scatto”*.  
> La macchina esegue la sequenza senza che tu debba ricordarti di far avanzare il contatore a mano.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un `for` per ripetere un calcolo un numero noto di volte

---

### ⚙️ Prima del laboratorio: `for` = `while` in forma compatta

```cpp
// while equivalente
int anno = 1;
while (anno <= 5) {
    // corpo
    anno = anno + 1;
}

// stessa logica con for
for (int anno = 1; anno <= 5; ++anno) {
    // corpo
}
```

| Parte nell’intestazione `for` | Ruolo |
|-------------------------------|--------|
| `int anno = 1` | **Inizializzazione** (una sola volta, all’ingresso) |
| `anno <= 5` | **Condizione** (prima di ogni iterazione) |
| `++anno` | **Aggiornamento** (dopo ogni corpo) |

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Init contatore;
while (Condizione?) is (sì)
  :Corpo;
  :Aggiorna contatore;
endwhile (no)
stop
@enduml
```

---

### 🧭 Prima del laboratorio: il timer conta prima di fermarsi

L'intestazione del `for` dice alla macchina industriale quando partire, quando
fermarsi e di quanto avanzare dopo ogni giro.

| Parte | Domanda a cui risponde |
|-------|-------------------------|
| Inizializzazione | Da quale numero parto? |
| Condizione | Posso fare un altro giro? |
| Aggiornamento | Come preparo il giro successivo? |

---

### 🔬 Laboratorio PRIMM: Piano di ammortamento

Costruiamo la tabella di ammortamento a quote costanti anno per anno.

#### 1. PREDICT (Prevedi)


Quante righe stampa questo ciclo?

```cpp
for (int i = 0; i < 5; ++i) {
    std::cout << i << "\n";
}
```

[( )] 5 righe: `1 2 3 4 5`
[(X)] 5 righe: `0 1 2 3 4`
[( )] 4 righe: `0 1 2 3`
[( )] Ciclo infinito


<details>
<summary>💡 Spiegazione</summary>
<code>i</code> parte da <code>0</code>; la condizione è <code>i &lt; 5</code>; dopo ogni giro <code>++i</code>.  
Valori stampati: 0, 1, 2, 3, 4 — cinque righe.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ammortamento_cespite.cpp
 * @brief Piano di ammortamento a quote costanti su N anni.
 */
#include <iostream>

/**
 * @brief Stampa tabella anno / quota / valore residuo.
 * @return int 0 se ok.
 */
int main() {
    const double COSTO_CESPITE = 10000.0;
    const int NUMERO_ANNI = 5;
    const double QUOTA_ANNUA = COSTO_CESPITE / NUMERO_ANNI;

    double valoreResiduo = COSTO_CESPITE;

    std::cout << "Anno\tQuota\tResiduo\n";
    std::cout << "----\t-----\t-------\n";

    for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
        valoreResiduo -= QUOTA_ANNUA;
        std::cout << anno << "\t" << QUOTA_ANNUA << "\t" << valoreResiduo << "\n";
    }

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Con 5 anni e cespite 10000:

| anno | Quota | Residuo dopo |
|------|-------|--------------|
| 1 | 2000 | 8000 |
| 2 | 2000 | 6000 |
| … | … | … |
| 5 | 2000 | 0 |

> 🔗 Segui `anno` e `valoreResiduo` su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
    valoreResiduo -= QUOTA_ANNUA;
}
```

</details>

1. **Fondo ammortamento**  
   Prima del ciclo: `double fondo = 0.0;`.  
   A ogni giro: `fondo += QUOTA_ANNUA;` e stampalo in tabella.

2. **Conto alla rovescia**  
   ```cpp
   for (int anniRimanenti = NUMERO_ANNI; anniRimanenti >= 1; --anniRimanenti)
   ```
   Adatta la stampa in modo coerente.

3. **Dodici mesi**
   Imposta `NUMERO_ANNI` a `12` e interpreta ogni giro come un mese: verifica che
   il timer esegua esattamente dodici scatti.

#### 5. MAKE (Crea)
**Scenario SIA — Interesse composto su deposito aziendale**

Scrivi `interesse_composto.cpp`:

- `double capitale = 10000.00`
- `const double TASSO = 0.04` (4% annuo)
- `const int ANNI = 6`
- Ciclo `for` da anno 1 a `ANNI`:
  - interessi dell’anno = `capitale * TASSO`
  - aggiorna `capitale`
  - stampa: anno, interessi, nuovo capitale
- A fine ciclo: guadagno netto = capitale finale − 10000

**Requisiti:** Doxygen, `///` sulle grandezze finanziarie, tabella leggibile.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Simula capitalizzazione composta su N anni.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché il tasso resta costante per tutta la simulazione.
    // TODO: capitale, tasso, anni; for; stampa guadagno netto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `for` = quando il numero di ripetizioni è **noto** (o facile da esprimere con un contatore).
- Intestazione: `init; condizione; aggiornamento`.
- Stesso potere del `while`; forma più sicura per i conteggi regolari.
- Per input a sentinella resta preferibile il `while`.

---

### ➡️ Prossimo chunk
A volte il corpo del ciclo deve girare **almeno una volta** (es. chiedere un dato finché non è valido).  
Entra in scena il **`do-while`**: controllo in coda.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: for e conteggio noto
  [x] Metafora timer
  [x] Quiz sintassi corretta
  [x] Predict conteggio da 0
  [x] PRIMM ammortamento cespite
  [x] Make interesse composto (SIA)
  [x] do-while solo annunciato
-->

## 🔁 Garantire l'Azione (Il Ciclo `do-while`)

> "Fidarsi è bene, validare l'input prima di registrarlo è sicurezza informatica."
> — *Regola Aurea dello Sviluppo Software*

`while` e `for` hanno il **controllo in testa**: se la condizione è già falsa, il corpo non gira **mai**.

A volte però un’azione deve avvenire **almeno una volta** prima di poter controllare:
- chiedere un importo (non puoi validarlo prima che esista);
- mostrare un menu e poi decidere se uscire.

Per questo esiste il **`do-while`**: controllo **in coda**.

> 💡 **Metafora: modulo online con campi obbligatori**  
> 1. La pagina ti mostra il form e tu compili (**il `do` gira almeno una volta**).  
> 2. Premi “Invia”: il sistema controlla (*controllo in coda*).  
> 3. Se c’è un errore, il form torna indietro e riprovi.  
> 4. Si ripete **finché** i dati non sono validi.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un `do-while` per validare un input che deve essere richiesto almeno una volta

---

### ⚙️ Prima del laboratorio: anatomia e confronto con `while`

```cpp
// do-while: il corpo gira almeno una volta
double importo;
do {
    std::cout << "Importo (> 0): ";
    std::cin >> importo;
} while (importo <= 0.0);
```

Equivalente scomodo con `while` (codice di lettura **duplicato**):

```cpp
std::cout << "Importo (> 0): ";
std::cin >> importo;
while (importo <= 0.0) {
    std::cout << "Importo (> 0): ";
    std::cin >> importo;
}
```

| | `while` / `for` | `do-while` |
|--|-----------------|------------|
| Controllo | in **testa** | in **coda** |
| Iterazioni minime | 0 | **1** |
| Uso tipico | conteggi, sentinella già nota | validazione input, menu “almeno una volta” |

**Attenzione alla sintassi:** dopo il `while (...)` del `do-while` serve il **`;`**.

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Esegui corpo (do);
while (Condizione ancora vera?) is (sì)
  :Esegui di nuovo il corpo;
endwhile (no)
:Esci;
stop
@enduml
```

---

### 🧭 Prima del laboratorio: il controllo arriva dopo il modulo

Il form viene mostrato, l'utente prova a inviarlo e solo dopo il sistema decide
se chiedere una nuova compilazione. Per questo il primo giro è garantito.

| Ciclo | Quando controlla? | Giri minimi |
|-------|------------------|-------------|
| `while` | prima del corpo | 0 |
| `do-while` | dopo il corpo | 1 |

---

### 🔬 Laboratorio PRIMM: Validazione importo bonifico

Chiediamo un importo finché non rientra nel range ammesso (almeno un tentativo).

#### 1. PREDICT (Prevedi)


Quante volte viene eseguito il corpo?

```cpp
int n = 10;
do {
    std::cout << "giro\n";
    n = n + 1;
} while (n < 5);
```

[( )] 0 volte
[(X)] 1 volta
[( )] 5 volte
[( )] Infinito


<details>
<summary>💡 Spiegazione</summary>
Il corpo viene eseguito <strong>prima</strong> del controllo.  
Anche se <code>n &lt; 5</code> è già falso (10 &lt; 5), stampi comunque una volta <code>giro</code>, poi la condizione fallisce e usci.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file valida_bonifico.cpp
 * @brief Chiede un importo di bonifico finché non e' nel range ammesso.
 */
#include <iostream>

/**
 * @brief Valida importo in [1, 5000] con do-while.
 * @return int 0 se ok.
 */
int main() {
    const double MIN_BONIFICO = 1.0;
    const double MAX_BONIFICO = 5000.0;

    double importo = 0.0;

    do {
        std::cout << "Importo bonifico: ";
        std::cin >> importo;
        if (importo < MIN_BONIFICO || importo > MAX_BONIFICO) {
            std::cout << "  Non valido (ammessi " << MIN_BONIFICO
                      << " .. " << MAX_BONIFICO << ")\n";
        }
    } while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);

    std::cout << "Bonifico accettato: " << importo << " EUR\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Sequenza di esempio: `-10` → `0` → `250`

| Giro | importo | Valido? | Continua? |
|------|---------|---------|-----------|
| 1 | -10 | no | sì |
| 2 | 0 | no | sì |
| 3 | 250 | sì | **no** (esce) |

Il controllo avviene **dopo** ogni tentativo: ecco perché il primo giro c’è sempre.

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
do {
    std::cin >> importo;
} while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);
```

</details>

1. **Range più stretto**
   Cambia l'intervallo ammesso da `[1, 5000]` a `[10, 1000]` e prova un importo
   fuori range prima di uno valido.

2. **Dimenticare il `;`**
   Togli il punto e virgola dopo `while (...)`: osserva l’errore del compilatore.

   Un compilatore come g++ può segnalare:

   ```text
   error: expected ';' before 'return'
   ```

3. **Valido al primo invio**
   Inserisci subito `250`: verifica che il corpo gira una volta e il controllo
   permette subito l'uscita.

#### 5. MAKE (Crea)
**Scenario SIA — PIN sportello con tentativi limitati**

Scrivi `pin_sportello.cpp`:

- `const int PIN_CORRETTO = 4821`
- L’utente inserisce un PIN (`int`)
- `do-while`: ripeti finché il PIN è sbagliato **e** i tentativi sono `< 3`
- Se indovina entro 3 prove → “Accesso consentito”
- Se esaurisce i tentativi → “Carta bloccata”
- Non rivelare il PIN corretto nei messaggi di errore

**Requisiti:** Doxygen, messaggi chiari, niente ciclo infinito.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Validazione PIN sportello con massimo 3 tentativi.
 */
#include <iostream>

int main() {
    const int PIN_CORRETTO = 4821;
    /// TODO: spiega perché i tentativi sono limitati.
    // TODO: tentativi, do-while, esiti
    return 0;
}
```

</details>

**Variante di sintesi (opzionale, se avete tempo in lab):**  
un mini menu cassa con `do-while` esterno + `switch` (nuova spesa / uscita), riusando sentinella e scaglioni già visti. Non è obbligatorio per chiudere il capitolo.

---

### 📝 Riepilogo tascabile
- `do-while` = esegui **poi** controlla → **almeno un** giro.
- Ideale per validare input e menu che devono apparire subito.
- Dopo `while (...)` del `do-while` non dimenticare il **`;`**.
- `while`/`for` restano la scelta giusta quando 0 iterazioni è accettabile.

---

### ➡️ Prossimo chunk
Chiudiamo il Blocco 1 con gli strumenti di “guida fine” del ciclo: **`break`**, **`continue`** e la formattazione professionale dei numeri con **`<iomanip>`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: do-while, validazione, almeno una iterazione
  [x] Metafora form online
  [x] Quiz sintassi corretta
  [x] Predict: una iterazione anche se condizione già falsa
  [x] PRIMM validazione bonifico
  [x] Make PIN con 3 tentativi (più mirato del mega-terminale)
  [x] Sintesi menu lasciata opzionale
  [x] break/iomanip solo annunciati
-->

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

Cosa stampa il ciclo?

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

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

## 🖨️ La Stampante Fiscale: formattare importi con `<iomanip>`

> "In contabilità due decimali non sono un vezzo: sono una regola."  
> — *Pratica di bilanci e scontrini*

`std::cout` di default non stampa sempre i centesimi come uno scontrino.  
Con **`<iomanip>`** imposti **virgola fissa** e **precisione**, così gli importi sono leggibili e confrontabili.

> 💡 **Metafora: stampante dello scontrino**  
> - `std::fixed` = “modo importi”, non notazione scientifica  
> - `std::setprecision(2)` = sempre **due cifre** dopo la virgola  
> - Risultato tipico: `19.50` e non `19.5`

Questo chunk è **solo formattazione output**. Non mescola `break`/`continue`.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Usare `std::fixed` e `std::setprecision(2)` su importi monetari
- Produrre un mini-prospetto allineato (imponibile, IVA, totale)

---

### ⚙️ In breve

```cpp
#include <iomanip>

std::cout << std::fixed << std::setprecision(2);
std::cout << 19.5;   // 19.50
```

La manipolazione resta attiva sulle stampe successive dello stesso stream finché non la cambi.

---

### 🔬 Laboratorio PRIMM: Riga di scontrino

#### 1. PREDICT (Prevedi)

Come appare 19.5 con `std::fixed` e `std::setprecision(2)`?

```cpp
std::cout << std::fixed << std::setprecision(2) << 19.5;
```

[(X)] 19.50
[( )] 19.5
[( )] 20
[( )] 1.95e1

<details>
<summary>💡 Spiegazione</summary>
<code>fixed</code> + precisione 2 forza due decimali: 19.5 diventa 19.50 in output.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scontrino_riga.cpp
 * @brief Importi con due decimali.
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

| Manipolatore | Effetto |
|--------------|---------|
| `std::fixed` | Notazione fissa |
| `std::setprecision(2)` | Due cifre decimali in modo fixed |

Prova a togliere `fixed` e osserva la differenza.

#### 4. MODIFY (Modifica)
1. Cambia l’imponibile a `100` e verifica i centesimi.
2. Aggiungi una riga “Totale arrotondato visualizzato” (stesso formato).
3. Estrai una funzione `void stampaImporto(const char* etichetta, double v)` già formattata.

#### 5. MAKE (Crea)
**Scenario SIA — Prospetto documento**

`prospetto_importi.cpp`: imponibile, aliquota, IVA, totale; tutte le righe con due decimali; etichette chiare.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <iomanip>
int main() {
    std::cout << std::fixed << std::setprecision(2);
    // ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- `#include <iomanip>` per la forma “scontrino”
- `fixed` + `setprecision(2)` = due decimali stabili
- Un chunk = solo output; la logica IVA resta nelle funzioni
- Utile in ogni Make contabile successivo

---

### ➡️ Prossimo chunk
Valore vs riferimento nei parametri di funzione: quando la modifica deve restare.

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

Quanto vale `calcolaIva(100.0)` con aliquota 0.22?

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

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

Dopo `aumenta(x)` con parametro per valore, quanto vale `x` se partiva da 10?

```cpp
void aumenta(int valore) { valore += 5; }
int x = 10;
aumenta(x);
```

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

Con `double vendite[30];`, cosa succede leggendo `vendite[30]`?

```cpp
double vendite[30];
double x = vendite[30];
```

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

In `int m[2][3];`, quanti elementi ci sono e qual è l’ultimo indice di colonna?

```cpp
int m[2][3];
```

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

Dopo `int x = 10; int* p = &x; *p = 25;`, quanto vale `x`?

```cpp
int x = 10;
int* p = &x;
*p = 25;
```

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

Con `enum class Stato { Attivo, Sospeso };`, cosa stampa il confronto tra due variabili entrambe `Attivo`?

```cpp
enum class Stato { Attivo, Sospeso };
Stato a = Stato::Attivo;
Stato b = Stato::Attivo;
// a == b ?
```

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

La ricerca binaria su un array disordinato è affidabile?

```cpp
// array NON ordinato
// binary_search(...)
```

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

Selection sort, a ogni passo esterno, cosa fa?

```cpp
// for i ...
//   cerca minimo in i..n-1
//   scambia con posizione i
```

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

Qual è il ruolo principale della fase di merge?

```cpp
// due metà già ordinate → una sequenza ordinata
```

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

Cosa rappresenta `Record tabella[100];` se Record è una struct?

```cpp
struct Record { int id; double importo; };
Record tabella[100];
```

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

Cosa deve avere ogni funzione ricorsiva corretta?

```cpp
int f(int n) {
    if (n <= 0) return 1; // ?
    return n * f(n - 1);
}
```

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

Se `prezzo` è `private` in una `class`, da `main` posso scrivere `a.prezzo = -5`?

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

Dopo la costruzione di un Articolo con codice e prezzo tramite costruttore, i campi sono già impostati?


```cpp
class Articolo {
public:
    Articolo(const std::string& c, double p);
};
Articolo a("A-1", 10.0);
```

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

Chi può chiamare un metodo public di Articolo?

```cpp
Articolo a("A", 1.0);
a.scheda();
```

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

Un metodo `void scheda() const` può assegnare `giacenza = 0` nel corpo?

```cpp
void scheda() const { giacenza = 0; }
```

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

Se `Ordine` contiene un membro `Cliente cliente_`, la distruzione di `Ordine` coinvolge anche `cliente_`?

```cpp
class Ordine { Cliente cliente_; /* ... */ };
```

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

Una classe derivata public eredita i membri public della base?

```cpp
class Base { public: void f(); };
class Der : public Base {};
```

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

Con `scheda` virtuale e puntatore a Base che punta a Derivata, quale `scheda` viene chiamata?

```cpp
Base* p = new Derivata();
p->scheda();
```

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

A cosa serve tipicamente sovraccaricare `operator<<` per una classe?

```cpp
std::cout << articolo;
```

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

Una funzione `template <typename T> T massimo(T a, T b)` può essere usata su `int` e su `double`?

```cpp
massimo(3, 5);
massimo(2.5, 2.7);
```

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

Dopo `v.push_back(3); v.push_back(5);`, quanto vale `v.size()`?

```cpp
std::vector<int> v;
v.push_back(3);
v.push_back(5);
```

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

Nel mini-progetto, perché dati private + metodi public sono un requisito?

```cpp
// rubrica progetto OOP
```

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
