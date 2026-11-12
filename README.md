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

## 🧭 Guida allo Studio: Come Imparare a Programmare


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

#### 2. RUN (Esegui)
- Copia il programma nel tuo ambiente di sviluppo (VS Code o blocco interattivo `@LIA.cpp`).
- **Attenzione:** **non fare copia e incolla!** Digitare il codice parola per parola è indispensabile per memorizzare la sintassi e accorgersi dei dettagli.
- Esegui il programma e confronta l'output ottenuto con la previsione che avevi fatto al passo 1.

#### 3. INVESTIGATE (Investiga)
- Copia il programma su [Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html) ed eseguilo **passo dopo passo**.
- Osserva visivamente come evolve lo stato della memoria (Stack, variabili locali, tipi) a ogni istruzione di assegnamento.
- Confronta l'evoluzione effettiva con la tabella di traccia che hai disegnato sul quaderno.

#### 4. MODIFY (Modifica)
- Modifica il codice sorgente procedendo a piccoli passi, per fare tuo il programma:
  - *Esempio 1:* se il programma usa valori prefissati (hardcoded), modificalo per chiedere i dati all'utente tramite istruzioni di input (`std::cin`).
  - *Esempio 2:* se usa numeri interi (`int`), prova a convertirli in numeri a virgola mobile (`double`) o viceversa, osservando come cambia il comportamento della divisione.
- Più modifichi il codice con cognizione di causa, più ne diventi padrone.

#### 5. MAKE (Crea)
- Scrivi un **nuovo programma autonomo** partendo da zero.
- Puoi prendere in prestito frammenti o strutture logiche dal programma appena studiato, applicandoli per risolvere un problema diverso o per realizzare una funzione nuova.
- Questo è il momento in cui passi da "lettore di codice" a "creatore di software".
## 🛠️ Capitolo 1: Prepara la tua Officina di Sviluppo

> "Uno strumento non fa il mestiere, ma senza gli strumenti giusti il mestiere diventa impossibile."
> — *Principio di officina*

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
Alla fine sei in grado di:
- Installare e verificare un ambiente C++ completo su Windows 10/11
- Compilare ed eseguire da terminale un programma minimo
- Eseguire e debuggare lo stesso programma da Visual Studio Code

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

#### Passo 7 — Primo programma di prova (ciclo leggero PRIMM)

Crea il file `prova.cpp` nella cartella del corso (`Documenti\Ci-Piu-Piu`) con questo contenuto:

```cpp
/**
 * @file prova.cpp
 * @brief Programma di verifica dell'ambiente di sviluppo.
 */
#include <iostream>

int main() {
    std::cout << "Ambiente C++ pronto!\n";
    return 0;
}
```

##### 1. PREDICT
Prima di compilare, rispondi:

Cosa pensi che succeda quando eseguirai il programma?

[( )] Comparirà una finestra grafica con un messaggio
[(X)] Nel terminale apparirà la scritta "Ambiente C++ pronto!"
[( )] Il computer si riavvierà
[( )] Comparirà un errore perché manca qualcosa

##### 2. RUN (da terminale)
Nel Prompt dei comandi (sempre dentro la cartella del progetto):

```bat
g++ prova.cpp -o prova.exe
prova.exe
```

**Controllo:** deve comparire esattamente `Ambiente C++ pronto!`.

##### 3. MODIFY
Cambia il messaggio stampato (es. metti il tuo nome o la tua classe) e ricompila.  
Verifica che la nuova frase appaia correttamente. Puoi usare il bottone "Esegui" sotto la finestra del codice sorgente per eseguire il codice.

```cpp[modificami.cpp]
/**
 * @file modificami.cpp
 * @brief Modifica la frase!
 */
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

2. Apri il file `ridotto.cpp`.

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
| `ridotto.cpp`           | Primo pezzo prodotto e collaudato                | Compila ed esegue             |
| Breakpoint + F5         | Ispezione interna del programma in esecuzione    | Il programma si ferma         |

---

### 📝 Riepilogo tascabile
- Questa è una **sessione di laboratorio**, non una lettura veloce.
- Senza compilatore non esiste programma eseguibile.
- Il PATH deve contenere `C:\msys64\ucrt64\bin` e va verificato in un **nuovo** terminale.
- `g++` traduce il codice sorgente in eseguibile; `gdb` ti fa guardare dentro mentre gira.
- Il programma `ridotto.cpp` è il tuo banco di prova: se compila, stampa e si debugga, l’officina è pronta.
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

---
## ⚙️ Capitolo 2: Il Motore Sotto il Cofano

> "La programmazione è l'arte di esprimere soluzioni ai problemi in modo che un computer possa eseguirle."
> — *Bjarne Stroustrup*

Hai appena allestito l’officina (VS Code + g++).  
Ora apriamo il cofano e guardiamo **cosa succede davvero** quando premi il pulsante di compilazione.

Il computer non capisce il C++. Capisce solo istruzioni macchina (sequenze di 0 e 1).  
Tra il file che scrivi tu (`.cpp`) e il programma che gira (`.exe`) c’è una **catena di montaggio** con quattro stazioni.

> 💡 **Metafora:**  
> Pensa a una **fabbrica di auto**.  
> - Il progetto su carta = il tuo file `.cpp`  
> - I reparti della fabbrica = pre-elaboratore, compilatore, assemblatore, linker  
> - L’auto finita che esce dal cancello = il file eseguibile  
> Ogni reparto fa un lavoro preciso. Se un pezzo è sbagliato, la catena si ferma e ti arriva una “multa” (errore di compilazione).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Descrivere le quattro fasi della compilazione C++ e il ruolo di ciascuna
- Usare `g++ -save-temps` per generare e ispezionare i file intermedi (`.ii`, `.s`, `.o`)
- Collegare una riga di C++ semplice al corrispondente frammento Assembly

---

### 🏭 La fabbrica del codice — le quattro stazioni

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

In realtà, dentro il “Compilatore” della figura ci sono **più stazioni**. Con `g++` le vediamo così:

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
/**
 * @file ridotto.cpp
 * @brief Programma minimo per ispezionare la catena di compilazione.
 */
int main() {
    return 0;   /// dice al sistema operativo: "tutto ok"
}
```

#### 1. PREDICT (Prevedi)
Prima di compilare, rispondi:

Se compiliamo questo programma con `g++ -save-temps`, quale file conterrà il codice **dopo** che il pre-elaboratore ha rimosso i commenti?

[( )] `ridotto.o`
[(X)] `ridotto.ii`
[( )] `ridotto.s`
[( )] `ridotto.exe`

#### 2. RUN (Esegui)
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

| File | Cosa ci trovi | Cosa osservare |
|------|----------------|----------------|
| `ridotto.ii` | Codice “pulito” dopo il pre-elaboratore | I commenti sono spariti; possono comparire righe di sistema |
| `ridotto.s` | Assembly | Cerca una riga con `movl` o `mov` e il numero `0` |
| `ridotto.o` | Codice macchina (binario) | Non è leggibile come testo |
| `ridotto.exe` | Eseguibile finale | È il prodotto finito della fabbrica |

Nel file `.s` noterai istruzioni del tipo:
```asm
movl $0, %eax
```
Che, in pratica, prepara il valore di ritorno `0` (successo).

#### 4. MODIFY (Modifica)
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
<summary>💡 Perché è importante?</summary>
Hai visto con i tuoi occhi la traduzione: una riga C++ ad alto livello (<code>return 42;</code>) diventa una precisa istruzione Assembly. Il compilatore non fa magia: fa <strong>traduzione</strong>.
</details>

Esegui di nuovo il programma e controlla il codice di uscita:

```bat
ridotto.exe
echo %ERRORLEVEL%
```

Dovresti vedere `42`.

#### 5. MAKE (Crea)
Crea un nuovo file `codice_uscita.cpp` che:
1. Contiene solo la funzione `main`
2. Restituisce un numero a tua scelta tra 1 e 99 (diverso da 0 e da 42)
3. Viene compilato con `-save-temps -fverbose-asm`
4. Ti permette di verificare, aprendo il `.s`, che il numero scelto compaia nell’Assembly
5. Mostra lo stesso numero con `echo %ERRORLEVEL%` dopo l’esecuzione

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

---
## 💬 Capitolo 3: Il Primo Dialogo con la Macchina

> "S'impara a programmare scrivendo programmi."
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

#### 1. PREDICT (Prevedi)
Guarda attentamente la riga:
```cpp
std::cout << "Ciao, Mondo!\n";
```

Cosa fa il simbolo `\n` alla fine della frase?

[( )] Stampa esattamente i caratteri `\n` a video
[(X)] Va a capo, spostando il cursore alla riga successiva
[( )] Cancella tutto quello che è stato stampato prima
[( )] Inserisce uno spazio extra

#### 2. RUN (Esegui)
Digita il codice **a mano** (non fare copia-incolla) nel blocco qui sotto e premilo Run.  
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

| Codice | Spiegazione brain-friendly | Perché è importante |
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
Senza <code>std::</code> il compilatore cerca una cosa chiamata <code>cout</code> nel tuo codice e non la trova. Per ora resta esplicito con <code>std::</code>. Più avanti vedremo <code>using namespace std;</code>, ma all’inizio è meglio essere chiari.
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
- `return 0;` comunica “successo” al sistema operativo.
- Il codice ha **due lettori**: il compilatore (sintassi) e l’essere umano (chiarezza). I commenti servono al secondo.
- Gli errori di compilazione sono messaggi utili: imparare a leggerli è una competenza fondamentale.

---

### ➡️ Prossimo chunk
Finora il computer ha solo *parlato*.  
Nel prossimo capitolo gli daremo le **scatole** (le variabili) per ricordare i dati e gli insegneremo ad *ascoltare* (`std::cin`).

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo unico e osservabile
  [x] Metafora ricetta / chef
  [x] Quiz con sintassi LiaScript corretta
  [x] PRIMM completo
  [x] Investigate con tabella
  [x] Modify progressive + spiegazioni
  [x] Make con scaffold e requisiti chiari
  [x] Riepilogo tascabile
  [x] Nessun costrutto non ancora introdotto
-->
## 📝 Capitolo 4: Parlare al Futuro Te Stesso (Documentazione Doxygen)

> "Il codice viene letto molto più spesso di quanto venga scritto."
> — *Principio di manutenibilità*

Hai già scritto `Ciao, Mondo!` e presto scriverai programmi più lunghi.  
Chi li leggerà tra tre mesi? Tu. Un compagno. Il docente.  

Per questo in azienda (e in questo corso) non basta che il programma *funzioni*: deve anche essere **comprensibile**.  
Usiamo uno standard leggero e diffusissimo: **Doxygen**.

> 💡 **Metafora:**  
> Il codice è il prodotto finito.  
> I commenti Doxygen sono l’**etichetta e il manuale d’uso** attaccati al prodotto: dicono *cosa fa*, *per chi*, *con quali dati*, senza costringere a smontare tutto.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un’intestazione di file e di `main` in stile Doxygen
- Usare il commento `///` per spiegare il **perché** (non il cosa ovvio)
- Applicare la **regola di proporzionalità** del corso

---

### 📋 I tag essenziali (solo quelli che usiamo)

| Tag | A cosa serve | Esempio |
|-----|--------------|---------|
| `@file` | Nome del file | `@file scheda_prodotto.cpp` |
| `@brief` | Una riga: cosa fa il programma / la funzione | `@brief Calcola il totale ivato.` |
| `@param` | Descrive un parametro (quando avremo le funzioni) | `@param prezzo Importo netto in euro` |
| `@return` | Cosa restituisce la funzione | `@return int 0 se successo` |

Commento di riga leggero:

```cpp
/// Aliquota IVA ordinaria vigente (non modificare a caso)
const double ALIQUOTA_IVA = 0.22;
```

---

### 🔬 Esempio minimo completo

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
    /// Identificativo dello studente per lo scontrino di presentazione
    std::cout << "Nome: Alex\n";
    std::cout << "Classe: 3A SIA\n";
    return 0;
}
```

---

### ⚖️ Regola di proporzionalità (obbligatoria nel corso)

| Situazione | Cosa scrivere |
|------------|----------------|
| Programma o funzione **> ~15 righe** | Intestazione Doxygen completa (`@file` / `@brief` / `@param` / `@return` dove servono) |
| Snippet o esercizio **breve** | Solo `///` sul **perché** economico o logico |
| Vietato | Commenti tautologici (`/// incrementa i di 1`) |

Esempio **buono**:
```cpp
/// 0.22 = aliquota IVA ordinaria vigente per beni e servizi
const double ALIQUOTA_IVA = 0.22;
```

Esempio **da evitare**:
```cpp
/// dichiara la costante aliquota
const double ALIQUOTA_IVA = 0.22;
```

---

### 🧪 Mini-esercizio (MAKE leggero)

Prendi il programma `presentazione.cpp` del capitolo precedente (o riscrivilo) e:
1. Aggiungi l’intestazione `@file` + `@brief` in testa al file
2. Aggiungi `@brief` e `@return` su `main`
3. Metti un `///` utile su almeno una riga di output

Non serve generare HTML con lo strumento Doxygen: per ora ci interessa **scrivere** i commenti nel modo giusto. Più avanti, quando i progetti cresceranno, potremo anche generarne la documentazione automatica.

---

### 📝 Riepilogo tascabile
- Doxygen = etichette standard per file e funzioni.
- Tag minimi: `@file`, `@brief`, `@param`, `@return`.
- `///` spiega il **perché**, non il cosa ovvio.
- Proporzionalità: completo sopra ~15 righe, leggero sotto.
- Da questo capitolo in poi i Make “ufficiali” richiederanno questi standard.

---

### ➡️ Prossimo chunk
Con l’officina pronta, il motore visto, il primo dialogo scritto e le etichette chiare, apriamo gli **sportelli della memoria**: variabili, tipi e costanti.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Chunk breve e monotematico (solo documentazione)
  [x] Allineato a SKILLS.md (proporzionalità)
  [x] Nessun costrutto nuovo di linguaggio
  [x] Ponte esplicito verso variabili
-->
## 📦 Capitolo 5: Gli Sportelli della Memoria (Variabili, Costanti e Tipi)

> "La memoria è lo spazio in cui i dati attendono il loro turno per essere trasformati in valore."
> — *Principio dei Sistemi Informativi*

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
- Dichiarare variabili e costanti dei tipi fondamentali (`int`, `double`, `char`, `bool`, `std::string`)
- Scegliere il tipo adatto al dato aziendale che vuoi memorizzare
- Stampare i valori memorizzati e capire perché un `int` “taglia” i decimali

---

### 🗄️ I tipi di dato fondamentali

Prima di aprire uno sportello devi dire al compilatore **che tipo di merce** conterrà, così riserva lo spazio giusto.

| Tipo | Cosa contiene | Esempio SIA | Note |
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

### 🔬 Laboratorio PRIMM: Scheda articolo di magazzino

#### 1. PREDICT (Prevedi)
Osserva questo frammento:

```cpp
int pezziDisponibili = 7.85;
std::cout << pezziDisponibili;
```

Cosa viene stampato?

[( )] `7.85`
[(X)] `7` (la parte decimale viene troncata)
[( )] Il programma va in crash
[( )] `8` (arrotondamento)

<details>
<summary>💡 Spiegazione</summary>
<code>int</code> può contenere solo interi. Assegnare un valore con la virgola provoca <strong>troncamento</strong>, non arrotondamento. Per i prezzi e le quantità decimali serve <code>double</code>.
</details>

#### 2. RUN (Esegui)
Digita (a mano) e esegui il programma completo:

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
    // Dichiara qui le variabili e la costante
    // Stampa i dati e gli interessi stimati
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

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Un solo obiettivo principale: variabili, tipi, const
  [x] Metafora locker (Head First + contesto logistica/e-commerce)
  [x] Quiz sintassi LiaScript corretta
  [x] PRIMM completo con scenario magazzino
  [x] Modify progressivo (IVA, const, init moderna)
  [x] Make con scenario conto corrente (SIA)
  [x] cin/getline NON introdotti qui (troppa densità; eventuali in capitolo successivo)
  [x] Riepilogo tascabile e ponte al capitolo espressioni
-->
## 🧮 Capitolo 6: La Calcolatrice Fiscale (Espressioni e Operatore Ternario)

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
- Scrivere espressioni aritmetiche, di confronto e logiche corrette
- Evitare la trappola della **divisione intera**
- Usare l’**operatore ternario** per assegnare un valore in base a una condizione

---

### ⚙️ Gli operatori fondamentali

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

#### Confronto (producono `bool`)
`==`  `!=`  `<`  `<=`  `>`  `>=`

#### Logici
| Operatore | Nome | Vero quando… | Esempio SIA |
|-----------|------|--------------|-------------|
| `&&` | AND | **entrambe** le condizioni sono vere | `haTessera && spesa >= 50` |
| `\|\|` | OR | **almeno una** è vera | `isStudente \|\| isOver65` |
| `!` | NOT | ribalta il valore | `!contoBloccato` |

---

### ⚡ L’operatore ternario `?:`

Forma:
```text
condizione ? valore_se_vero : valore_se_falso
```

È un’**espressione**: calcola e restituisce un valore, pronto per essere assegnato o stampato.

```cpp
double speseSpedizione = (totaleSpesa >= 60.0) ? 0.0 : 6.50;
```

Utile quando la decisione è semplice e produce un valore.  
Per logiche lunghe o con più rami useremo `if` / `else` nei prossimi capitoli.

---

### 🔬 Laboratorio PRIMM: Scontrino e-commerce

#### 1. PREDICT (Prevedi)
Cosa stampa questo codice?

```cpp
int pezzi = 5;
double costoTotale = pezzi / 2 * 10.0;
std::cout << costoTotale;
```

[( )] `25`
[(X)] `20`
[( )] `25.5`
[( )] Errore di compilazione

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
    bool isClienteFedelta = true;

    /// 10% se tesserato e spesa >= 50, altrimenti 2%
    double percentualeSconto =
        (isClienteFedelta && importoProdotti >= 50.0) ? 0.10 : 0.02;

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
| `isClienteFedelta && importoProdotti >= 50.0` | `true` | entrambe vere |
| percentuale sconto | `0.10` | ramo `?` del ternario |
| `valoreSconto` | `8.5` | `85 * 0.10` |
| `nettoProdotti` | `76.5` | `85 - 8.5` |
| `nettoProdotti >= 60` | `true` | soglia superata |
| `speseSpedizione` | `0.0` | ramo `?` del secondo ternario |

> 🔗 Esegui il programma passo-passo su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Promozione weekend**  
   Concedi lo sconto del 10% se il cliente ha la tessera **oppure** la spesa (lordo) supera i 100€ (`||`).

2. **Consegna express**  
   Aggiungi `bool consegnaRapida = true;`.  
   Se è `true`, aggiungi un supplemento fisso di `3.00` alle spese di spedizione (anche se erano gratis), usando un ternario.

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

**Requisiti:** Doxygen, commenti `///` sulle aliquote, output chiaro tipo scontrino.

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
- `&&` = entrambe vere; `||` = almeno una vera; `!` = negazione.
- Ternario: `condizione ? se_vero : se_falso` — ideale per scelte semplici che restituiscono un valore.
- Per decisioni lunghe o a più rami → nei prossimi capitoli useremo `if` / `else`.

---

### ➡️ Prossimo chunk
Finora le decisioni tengono in una riga.  
Quando la logica diventa un **bivio** (fare A oppure fare B, con più istruzioni per ramo), entra in scena il costrutto `if` / `else`.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: espressioni + ternario (un focus)
  [x] Metafora cassa automatica
  [x] Quiz sintassi corretta
  [x] Trappola divisione intera in Predict
  [x] PRIMM su scontrino e-commerce
  [x] Make su commissioni POS (SIA)
  [x] if/else solo annunciato, non introdotto
-->
## 🚦 Capitolo 7: Bivi e Decisioni (`if` e `if-else`)

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
- Scrivere un `if` semplice e un `if-else` con graffe corrette
- Evitare i due tranelli classici (`;` dopo la condizione e graffe mancanti)
- Capire lo **scope**: una variabile dichiarata dentro `{ }` esiste solo lì

---

### 🔀 I due modelli

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

### ⚠️ I due grandi tranelli

**1. Il punto e virgola traditore**

```cpp
// SBAGLIATO: il ; chiude subito l'if
if (saldo >= importo);
{
    std::cout << "Approvato\n";  // viene eseguito SEMPRE
}
```

Dopo la `)` della condizione **non va mai** il `;`.

**2. Graffe e scope**

Senza `{ }` l’`if` controlla **solo** la prima istruzione successiva.  
**Usa sempre le graffe**, anche per una sola riga.

Inoltre: una variabile dichiarata dentro un blocco `{ }` **non esiste fuori** (scope locale).

---

### 🔬 Laboratorio PRIMM: Terminale pagamenti POS

#### 1. PREDICT (Prevedi)
Quali righe vengono stampate?

```cpp
int scorte = 12;
if (scorte < 5)
    std::cout << "1. Ordina nuovi pezzi!\n";
    std::cout << "2. Notifica inviata al fornitore.\n";
std::cout << "3. Controllo terminato.\n";
```

[( )] Non stampa nulla
[( )] Stampa 1, 2 e 3
[(X)] Stampa solo 2 e 3
[( )] Stampa solo 3

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
        /// Flag locale: esiste SOLO dentro questo blocco
        bool autorizzato = true;

        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << ">>> TRANSAZIONE APPROVATA <<<\n";
        std::cout << "Nuovo saldo: " << saldoDisponibile << " EUR\n";
    } else {
        /// Esiste SOLO dentro l'else
        double importoMancante = importoSpesa - saldoDisponibile;

        std::cout << ">>> TRANSAZIONE NEGATA <<<\n";
        std::cout << "Credito insufficiente.\n";
        std::cout << "Importo mancante: " << importoMancante << " EUR\n";
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
| `importoMancante` | `17.50` (visibile solo dentro l’else) |
| Dopo l’`if-else` | messaggio “Operazione conclusa” |

Prova a cambiare `importoSpesa` in `30.00` e riesegui: ora si attiva il ramo `if` e il saldo viene aggiornato.

> 🔗 Ispeziona lo stack su [Python Tutor C++](https://pythontutor.com/cpp.html): nota che `autorizzato` e `importoMancante` nascono e muoiono nei rispettivi blocchi.

#### 4. MODIFY (Modifica)
1. **Guardiano sottoscorta**  
   Aggiungi `int rotoloCartaTermica = 3;`.  
   Con un `if` **semplice** (senza else): se `< 5`, stampa un allarme per sostituire il rotolo.

2. **Micro-pagamento**  
   Se `importoSpesa < 10.00`, aggiungi una commissione fissa di `0.30` **prima** del controllo sul saldo.

3. **Prova di scope**  
   Prova a stampare `autorizzato` o `importoMancante` **dopo** la chiusura dell’`if-else`.  
   Il compilatore deve rifiutare (variabile non dichiarata in quello scope).

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
    // dichiara pinInserito e badgeDirigente
    // if-else con la regola di sicurezza
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `if` = azione opzionale; `if-else` = bivio a due vie (un solo ramo eseguito).
- **Mai** `;` subito dopo la condizione.
- **Sempre** le graffe `{ }`, anche per una sola istruzione.
- Variabili dichiarate dentro un blocco esistono **solo** lì (scope).
- Condizioni complesse: combina con `&&` e `||` (già visti nel capitolo sulle espressioni).

---

### ➡️ Prossimo chunk
Quando i bivi diventano **più di due** (es. fasce di sconto, giudizi, stati di un ordine) un solo `if-else` non basta.  
Passeremo a catene `if / else if / else` e alle regole per non perdere il controllo del flusso.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: if e if-else + tranelli + scope
  [x] Metafora tornello
  [x] Quiz sintassi corretta
  [x] Predict sulla trappola delle graffe mancanti
  [x] PRIMM su terminale POS
  [x] Make su caveau (SIA / sicurezza)
  [x] else-if non introdotto (solo annunciato)
-->
## 🌲 Capitolo 8: Scaglioni e Labirinti (`if / else if / else` e if annidati)

> "La complessità di un problema si risolve dividendolo in livelli ordinati di decisioni."
> — *Principio dell'Analisi dei Sistemi*

Con `if-else` gestiamo un bivio a due strade.  
Nei contesti aziendali le scelte sono spesso **a scaglioni**: fasce di sconto, livelli di fido, aliquote fiscali.  
Servono la **scala** `if / else if / else` e, quando un controllo dipende da un altro, gli **`if` annidati**.

> 💡 **Metafora: nastro di smistamento logistico**  
> - **Scala `if / else if / else`** = sensori in sequenza sul nastro: il primo che “prende” il pacco lo devia e **i successivi non lo vedono più**.  
> - **`if` annidato** = doppia porta di sicurezza: solo se apri la prima trovi la seconda. Se la prima resta chiusa, la seconda non la incontri.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una catena `if / else if / else` per alternative mutuamente esclusive
- Usare un `if` annidato quando un controllo ha senso solo dopo un altro
- Scegliere tra scala, annidamento e `&&` senza creare rami morti o condizioni fuori ordine

---

### 🪜 La scala `if / else if / else`

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

### 🚪 L’`if` annidato

Quando la seconda domanda ha senso **solo se** la prima è vera:

```cpp
if (anniCollaborazione >= 3) {
    if (fatturatoAnnuo >= 20000.0) {
        std::cout << "Fido concesso\n";
    } else {
        std::cout << "Fatturato insufficiente per il fido\n";
    }
} else {
    std::cout << "Anzianita insufficiente\n";
}
```

A volte la stessa logica si scrive più corta con `&&` (un solo messaggio di esito).  
L’annidamento resta utile quando i **messaggi di errore** devono essere distinti.

---

### 🧭 Bussola: quale strumento usare?

| Situazione | Strumento |
|------------|-----------|
| Due sole alternative | `if-else` |
| Tre o più fasce mutuamente esclusive | scala `if / else if / else` |
| Secondo controllo solo se il primo è superato, con messaggi diversi | `if` annidato |
| Tutte le condizioni devono essere vere, un solo esito | `if (A && B)` |

---

### 🔬 Laboratorio PRIMM: Fasce sconto e fido

#### 1. PREDICT (Prevedi)
Con `voto = 85`, cosa stampa questo codice?

```cpp
if (voto >= 90) {
    std::cout << "Ottimo\n";
} else if (voto >= 60) {
    std::cout << "Sufficiente\n";
} else {
    std::cout << "Insufficiente\n";
}
```

[( )] `Ottimo`
[(X)] `Sufficiente`
[( )] Stampa sia `Sufficiente` che `Ottimo`
[( )] Errore di compilazione

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
    int anniCollaborazione = 4;

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

    // Fido: doppia porta (annidato) per messaggi distinti
    if (anniCollaborazione >= 3) {
        if (fatturato >= 20000.0) {
            std::cout << "Fido: CONCESSO\n";
        } else {
            std::cout << "Fido: NEGATO (fatturato insufficiente)\n";
        }
    } else {
        std::cout << "Fido: NEGATO (anzianita insufficiente)\n";
    }

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

Poi, con `anniCollaborazione = 4`, si entra nel primo `if` del fido e, poiché `32500 >= 20000`, il fido è concesso.

> 🔗 Segui il flusso su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Fascia Diamond**  
   In cima alla scala: se `fatturato >= 100000` → sconto `0.20`.  
   Verifica con `120000` che non resti classificato Platinum.

2. **Fido in una riga**  
   Sostituisci l’annidamento con:
   ```cpp
   if (anniCollaborazione >= 3 && fatturato >= 20000.0) {
       std::cout << "Fido: CONCESSO\n";
   } else {
       std::cout << "Fido: NEGATO\n";
   }
   ```
   Più corto, ma perdi i messaggi distinti. Quando preferiresti l’annidamento?

3. **Ordine sbagliato (esperimento)**  
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
- `bool certificazioneGreen`: se `true`, detrai `1000` dall’imposta (non sotto zero)
- Output: prospetto con fascia, aliquota, imposta, eventuale detrazione, totale

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
    // dichiara dati, scala aliquote, detrazione green, stampa prospetto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- Scala `if / else if / else` = alternative esclusive; **ordine delle soglie** decisivo.
- Al primo ramo vero il resto della catena viene saltato.
- `if` annidato = seconda domanda solo se la prima è superata (messaggi diversi).
- `A && B` = stesso esito in forma compatta; meno flessibile sui messaggi.
- Per molte costanti discrete (menu 1/2/3) nel prossimo capitolo useremo `switch`.

---

### ➡️ Prossimo chunk
Quando la decisione dipende da un **valore discreto** (tasto di menu, codice operazione, stato numerico), la scala di `else if` diventa verbosa.  
Entra in scena lo **`switch`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: scala else-if + annidamento + bussola di scelta
  [x] Metafora nastro logistico
  [x] Quiz sintassi corretta
  [x] Predict sull'esclusività dei rami
  [x] PRIMM fasce sconto + fido
  [x] Make scaglioni imposta (modello semplificato esplicitato)
  [x] switch solo annunciato
-->
## 🎛️ Capitolo 9: Lo Smistatore di Sportello (`switch-case`)

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
- Scrivere uno `switch` su `int` o `char` con `case`, `break` e `default`
- Spiegare e usare (o evitare) il *fall-through*
- Scegliere tra `switch` e scala `if / else if` in base al tipo di decisione

---

### ⚙️ Anatomia

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

### 🧭 Bussola: `switch` o `if / else if`?

| Situazione | Preferisci |
|------------|------------|
| Menu 1/2/3, codici carattere, stati numerici fissi | `switch` |
| Scaglioni (`>= 50`, intervalli), condizioni composte | `if / else if` |
| Confronti su `double` o `std::string` | `if / else if` |

---

### 🔬 Laboratorio PRIMM: Menu ATM

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
[( )] Errore di compilazione

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
    double saldo = 1250.00;
    int sceltaMenu = 2;   // simula il tasto premuto dal cliente

    std::cout << "=== SPORTELLO ATM ===\n";
    std::cout << "1. Prelievo fisso 50 EUR\n";
    std::cout << "2. Versamento fisso 100 EUR\n";
    std::cout << "3. Visualizza saldo\n";
    std::cout << "0. Esci\n";
    std::cout << "Scelta: " << sceltaMenu << "\n\n";

    switch (sceltaMenu) {
        case 1: {
            const double PRELIEVO = 50.0;
            if (saldo >= PRELIEVO) {
                saldo -= PRELIEVO;
                std::cout << "Prelievo effettuato. Nuovo saldo: " << saldo << " EUR\n";
            } else {
                std::cout << "Fondi insufficienti.\n";
            }
            break;
        }
        case 2: {
            const double VERSAMENTO = 100.0;
            saldo += VERSAMENTO;
            std::cout << "Versamento effettuato. Nuovo saldo: " << saldo << " EUR\n";
            break;
        }
        case 3:
            std::cout << "Saldo disponibile: " << saldo << " EUR\n";
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
| Versamento | `saldo` diventa `1350` |
| `break` | esce dallo `switch` (non esegue case 3/default) |

Prova a togliere il `break` del `case 2` e riesegui: vedrai anche l’output del saldo (fall-through).

#### 4. MODIFY (Modifica)
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

**Requisiti:** Doxygen, `///` sui tassi, `break` corretti.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Conversione valuta estera in euro al POS.
 */
#include <iostream>

int main() {
    // dichiara importo e codice, switch sui char, stampa risultato
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
## 🔄 Capitolo 10: L'Anello Fondamentale (Il Ciclo `while`)

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
- Scrivere un `while` con i tre ingredienti (inizializzazione, condizione, aggiornamento)
- Usare un **valore sentinella** per terminare l’input
- Riconoscere e evitare il ciclo infinito

---

### ⚙️ Controllo in testa e tre ingredienti

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

### 🔬 Laboratorio PRIMM: Scontrino a nastro

#### 1. PREDICT (Prevedi)
Quante volte viene stampata la parola `"Elaborazione"`?

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

    /// Prima lettura (inizializzazione della condizione)
    double prezzoArticolo = 0.0;
    std::cout << "Prezzo articolo (0 per terminare): ";
    // In questo laboratorio simuliamo tre letture fisse:
    // 12.50, 3.20, 0  — in classe userai std::cin in loop

    // Simulazione input per ambiente interattivo
    double letture[] = {12.50, 3.20, 0.0};
    int i = 0;
    prezzoArticolo = letture[i++];

    while (prezzoArticolo != 0.0) {
        totaleSpesa += prezzoArticolo;
        numeroArticoli += 1;
        std::cout << "  + " << prezzoArticolo << " EUR (pezzi: " << numeroArticoli << ")\n";

        /// Aggiornamento: prossimo prezzo (sentinella inclusa)
        prezzoArticolo = letture[i++];
    }

    std::cout << "=== SCONTRINO ===\n";
    std::cout << "Articoli: " << numeroArticoli << "\n";
    std::cout << "Totale  : " << totaleSpesa << " EUR\n";

    return 0;
}
```
@LIA.cpp

> In laboratorio con tastiera reale sostituisci l’array di simulazione con:
> ```cpp
> std::cin >> prezzoArticolo;
> // ... nel while, di nuovo: std::cin >> prezzoArticolo;
> ```

#### 3. INVESTIGATE (Investiga)
Sequenza simulata: `12.50` → `3.20` → `0.0`

| Iterazione | `prezzoArticolo` | Condizione | Totale dopo |
|------------|------------------|------------|-------------|
| ingresso | 12.50 | vero | 12.50 |
| 2ª | 3.20 | vero | 15.70 |
| 3ª lettura | 0.0 | **falso** → esce | 15.70 |

La sentinella `0` **non** viene sommata: il controllo avviene prima del corpo.

> 🔗 Osserva le variabili su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
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
## ⏳ Capitolo 11: Il Contatore Compatto (Il Ciclo `for`)

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
- Scrivere un `for` con inizializzazione, condizione e aggiornamento nell’intestazione
- Usarlo quando il numero di ripetizioni è noto a priori
- Capire lo **scope** del contatore dichiarato nell’intestazione

---

### 🔍 `for` = `while` in forma compatta

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

**Scope:** se dichiari il contatore nell’intestazione (`for (int anno = …)`), `anno` **non esiste** fuori dal ciclo.

---

### 🔬 Laboratorio PRIMM: Piano di ammortamento

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
Valori stampati: 0, 1, 2, 3, 4 — cinque righe. In C++ i conteggi “da zero” sono la norma (come gli indici degli array che vedrai più avanti).
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

Il contatore `anno` nasce nell’intestazione del `for` e **muore** alla graffa di chiusura.

> 🔗 Segui `anno` e `valoreResiduo` su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Fondo ammortamento**  
   Prima del ciclo: `double fondo = 0.0;`.  
   A ogni giro: `fondo += QUOTA_ANNUA;` e stampalo in tabella.

2. **Conto alla rovescia**  
   ```cpp
   for (int anniRimanenti = NUMERO_ANNI; anniRimanenti >= 1; --anniRimanenti)
   ```
   Adatta la stampa in modo coerente.

3. **Prova di scope**  
   Dopo il `for`, prova `std::cout << anno;`.  
   Il compilatore deve segnalare che `anno` non è dichiarato in quello scope.

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
    // capitale, tasso, anni; for; stampa guadagno netto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `for` = quando il numero di ripetizioni è **noto** (o facile da esprimere con un contatore).
- Intestazione: `init; condizione; aggiornamento`.
- Contatore dichiarato nel `for` → scope limitato al ciclo.
- Stesso potere del `while`; forma più sicura per i conteggi regolari.
- Per input a sentinella resta preferibile il `while`.

---

### ➡️ Prossimo chunk
A volte il corpo del ciclo deve girare **almeno una volta** (es. chiedere un dato finché non è valido).  
Entra in scena il **`do-while`**: controllo in coda.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: for, contatore, scope
  [x] Metafora timer
  [x] Quiz sintassi corretta
  [x] Predict conteggio da 0
  [x] PRIMM ammortamento cespite
  [x] Make interesse composto (SIA)
  [x] do-while solo annunciato
-->
## 🔁 Capitolo 12: Garantire l'Azione (Il Ciclo `do-while`)

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
- Scrivere un `do-while` e spiegare la differenza con il `while`
- Usarlo per **validare un input** (ripeti finché il dato non è accettabile)
- Evitare la duplicazione di codice tipica del `while` “con lettura prima e dentro”

---

### ⚙️ Anatomia e confronto con `while`

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

### 🔬 Laboratorio PRIMM: Validazione importo bonifico

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

    // Sequenza simulata per demo: -10, 0, 250  (in classe usa cin nel loop)
    double tentativi[] = {-10.0, 0.0, 250.0};
    int t = 0;

    do {
        importo = tentativi[t++];
        std::cout << "Tentativo importo: " << importo << " EUR\n";
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

> In laboratorio reale:
> ```cpp
> do {
>     std::cout << "Importo bonifico: ";
>     std::cin >> importo;
> } while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);
> ```

#### 3. INVESTIGATE (Investiga)
Sequenza: `-10` → `0` → `250`

| Giro | importo | Valido? | Continua? |
|------|---------|---------|-----------|
| 1 | -10 | no | sì |
| 2 | 0 | no | sì |
| 3 | 250 | sì | **no** (esce) |

Il controllo avviene **dopo** ogni tentativo: ecco perché il primo giro c’è sempre.

#### 4. MODIFY (Modifica)
1. **Limite 3 tentativi**  
   Contatore `tentativi`. Se dopo 3 errori non è ancora valido, esci dal ciclo e stampa “sessione bloccata”.

2. **Menu “altra operazione?”**  
   Dopo un bonifico accettato, chiedi `S/N` in un `do-while` esterno e ripeti finché la risposta è `S`/`s`.

3. **Dimenticare il `;`**  
   Togli il punto e virgola dopo `while (...)`: osserva l’errore del compilatore.

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
    // tentativi, do-while, esiti
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
## 🎯 Capitolo 13: Il Cruscotto del Programmatore (`break`, `continue`, `<iomanip>`)

> "La precisione nella presentazione dei numeri è l'abito formale con cui il software si presenta all'azienda."
> — *Principio dei Sistemi Contabili*

Prima di salire al Blocco 2 (funzioni e strutture dati) chiudiamo il Blocco 1 con due strumenti da “cruscotto”:

1. **Controllo fine dei cicli:** `break` e `continue`
2. **Output contabile leggibile:** header `<iomanip>` (`fixed`, `setprecision`, `setw`)

> 💡 **Metafore**  
> - **`break`** = pulsante rosso di emergenza: il nastro si **ferma subito**.  
> - **`continue`** = braccio di scarto: salta **quel** pezzo difettoso e passa al successivo.  
> - **`<iomanip>`** = stampante fiscale: centesimi sempre a due cifre, colonne allineate.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Usare `break` per uscire anticipatamente da un ciclo
- Usare `continue` per saltare il resto del corpo e passare all’iterazione successiva
- Formattare importi e tabelle con `std::fixed`, `std::setprecision` e `std::setw`

---

### ⚙️ `break` vs `continue`

| Istruzione | Effetto | Dove va il flusso |
|------------|---------|-------------------|
| `break;` | Interrompe il ciclo | subito **dopo** il ciclo |
| `continue;` | Salta il resto del corpo di **questa** iterazione | alla condizione / aggiornamento del ciclo |

```cpp
for (int i = 1; i <= 10; ++i) {
    if (i == 3) continue;   // salta il 3
    if (i == 8) break;      // ferma tutto a 8
    std::cout << i << " ";
}
// stampa: 1 2 4 5 6 7
```

---

### 🖨️ Formattazione con `<iomanip>`

```cpp
#include <iomanip>

std::cout << std::fixed << std::setprecision(2);
std::cout << std::setw(10) << 19.5 << "\n";  // es. "     19.50"
```

| Manipolatore | Ruolo |
|--------------|--------|
| `std::fixed` | Notazione fissa (non scientifica) |
| `std::setprecision(2)` | Cifre **dopo la virgola** (con `fixed`) |
| `std::setw(n)` | Larghezza minima del **prossimo** campo |
| `std::left` / `std::right` | Allineamento (testo a sx, importi a dx) |

Senza `fixed`, `setprecision(2)` conta le cifre significative totali e può produrre notazione scientifica: in ambito monetario **`fixed` è obbligatorio**.

---

### 🔬 Laboratorio PRIMM: Report fiscale con scarti e stop

#### 1. PREDICT (Prevedi)
Cosa stampa?

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

[( )] `12345`
[( )] `1345`
[(X)] `13`
[( )] `1234`

<details>
<summary>💡 Spiegazione</summary>
<code>i=1</code> stampa; <code>i=2</code> → <code>continue</code> (niente stampa); <code>i=3</code> stampa; <code>i=4</code> → <code>break</code> (esce). Risultato: <code>13</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file report_fiscale.cpp
 * @brief Report di transazioni con scarto, stop di sicurezza e formattazione.
 */
#include <iostream>
#include <iomanip>

/**
 * @brief Elabora 6 transazioni simulate: continue se <=0, break se >50000.
 * @return int 0 se ok.
 */
int main() {
    const double importi[] = {120.5, -3.0, 45.0, 12.75, 52000.0, 8.0};
    const int N = 6;

    double totale = 0.0;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << std::setw(4) << "ID" << std::setw(12) << "Importo" << "\n";
    std::cout << "----  ----------\n";

    for (int id = 1; id <= N; ++id) {
        double importo = importi[id - 1];

        if (importo <= 0.0) {
            std::cout << "  (scarto ID " << id << ": non positivo)\n";
            continue;
        }
        if (importo > 50000.0) {
            std::cout << "  ALERT antiriciclaggio ID " << id
                      << " — interrompo il report\n";
            break;
        }

        totale += importo;
        std::cout << std::setw(4) << id << std::setw(12) << importo << "\n";
    }

    std::cout << "----  ----------\n";
    std::cout << std::setw(4) << "" << std::setw(12) << totale << "  TOTALE\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
| ID | Importo | Azione |
|----|---------|--------|
| 1 | 120.50 | accumula |
| 2 | -3.00 | `continue` (scarto) |
| 3 | 45.00 | accumula |
| 4 | 12.75 | accumula |
| 5 | 52000 | `break` (stop) |
| 6 | 8.00 | **non elaborato** |

> 🔗 Osserva il salto di `continue`/`break` su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Colonna IVA**  
   Per ogni riga valida stampa anche `importo * 0.22` con `setw`.

2. **Soglia micro-pagamenti**  
   Con `continue`, scarta anche gli importi `< 5.00`.

3. **Senza `fixed`**  
   Rimuovi `std::fixed` e osserva come cambia la stampa con solo `setprecision(2)`.

#### 5. MAKE (Crea)
**Scenario SIA — Liquidazione IVA trimestrale (semplificata)**

Scrivi `liquidazione_iva.cpp`:

- Ciclo su 6 fatture (ID 1…6) con imponibile e codice aliquota simulati in array (o costanti)
- Aliquote: `'O'` 22%, `'R'` 10%, `'M'` 4%, `'E'` 0%
- `continue` se imponibile `<= 0` (messaggio “fattura annullata”)
- `break` se imponibile `> 50000` (alert)
- Tabella formattata: `ID | Imponibile | Aliq. | IVA`
- A fine ciclo (o allo stop): totale imponibile e totale IVA

**Requisiti:** `#include <iomanip>`, `fixed` + `setprecision(2)`, Doxygen, `///` sulle aliquote.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Prospetto semplificato liquidazione IVA.
 */
#include <iostream>
#include <iomanip>

int main() {
    // dati, ciclo, continue/break, tabella, totali
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `break` = esci dal ciclo; `continue` = salta al giro successivo.
- In report contabili: scarti → `continue`; allarmi gravi → `break`.
- `<iomanip>`: `fixed` + `setprecision(2)` per i soldi; `setw` per le colonne.
- Senza `fixed`, `setprecision` non significa “due decimali monetari”.

---

### ➡️ Fine Blocco 1 — Prossimo orizzonte
Hai il controllo di dati, decisioni, cicli e presentazione.  
Nel **Blocco 2** spezzeremo i programmi in **funzioni**, introdurremo **array** e **struct** e costruiremo piccoli sistemi gestionali in memoria.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: break, continue, iomanip monetario
  [x] Metafore nastro / stampante fiscale
  [x] Quiz sintassi corretta
  [x] PRIMM report con scarti e alert
  [x] Make liquidazione IVA
  [x] Ponte esplicito a Blocco 2
-->
