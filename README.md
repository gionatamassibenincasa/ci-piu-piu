<!--
author:   Gionata Massi
email:    gionata.massi@savoiabenicasa.it
version:  2026-11-11
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

Crea il file `ridotto.cpp` nella cartella del corso (`Documenti\Cpp-3SIA`) con questo contenuto:

```cpp
/**
 * @file ridotto.cpp
 * @brief Programma minimo di verifica dell'ambiente di sviluppo.
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
g++ ridotto.cpp -o ridotto.exe
ridotto.exe
```

**Controllo:** deve comparire esattamente `Ambiente C++ pronto!`.

##### 3. MODIFY
Cambia il messaggio stampato (es. metti il tuo nome o la tua classe) e ricompila.  
Verifica che la nuova frase appaia correttamente.

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
## ⚙️ Capitolo: Il Motore Sotto il Cofano

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

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

rectangle "1. Codice sorgente\n(.cpp)" as Source
rectangle "2. Pre-elaboratore\n(.ii)" as Pre
rectangle "3. Compilatore\n(.s Assembly)" as Comp
rectangle "4. Assemblatore\n(.o oggetto)" as Asm
rectangle "5. Linker\n(.exe eseguibile)" as Link

Source --> Pre : espande #include\nrimuove commenti
Pre --> Comp : controlla sintassi\ntraduce in Assembly
Comp --> Asm : traduce in\ncodice macchina
Asm --> Link : unisce librerie\nproduce l'eseguibile
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
g++ -save-temps -O0 ridotto.cpp -o ridotto.exe
```

Il flag `-save-temps` dice a g++: “non cancellare i file intermedi”.  
`-O0` disattiva le ottimizzazioni, così l’Assembly resta più leggibile.

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
   g++ -save-temps -O0 ridotto.cpp -o ridotto.exe
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
3. Viene compilato con `-save-temps`
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

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Un solo obiettivo principale: capire la catena di compilazione
  [x] Metafora fabbrica / catena di montaggio
  [x] Quiz con sintassi LiaScript corretta
  [x] PRIMM completo su programma minimo SENZA iostream
  [x] Nessuna sovrapposizione con Ciao Mondo (niente cout nel Make)
  [x] -save-temps e ispezione .ii / .s
  [x] Collegamento esplicito return N → movl $N
  [x] Riepilogo tascabile e ponte al capitolo successivo
-->
## 💬 Capitolo 2: Il Primo Dialogo con la Macchina

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
## 📦 Capitolo 3: Gli Sportelli della Memoria (Variabili, Costanti e Tipi)

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
## 🧮 Capitolo 4: La Calcolatrice Fiscale (Espressioni e Operatore Ternario)

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
## 🚦 Capitolo 5: Bivi e Decisioni (`if` e `if-else`)

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
## 🌲 Capitolo 6: Scaglioni e Labirinti (if-else if in Cascata, if Annidati e Guida alla Scelta)

> "La complessità di un problema si risolve dividendolo in livelli ordinati di decisioni."
> — *Principio dell'Analisi dei Sistemi*

Nel capitolo precedente abbiamo affrontato i bivi a due sole strade (`if-else`). Ma nei contesti gestionali ed economici le scelte raramente sono binarie:
- Il fatturato di un cliente non è solo "alto o basso": si divide in **scaglioni di sconto progressivi** (Silver, Gold, Platinum).
- L'approvazione di un prestito aziendale richiede una sequenza gerarchica di controlli: prima la maggiore età, poi il bilancio, infine le garanzie.

Per governare queste situazioni senza scrivere codice confuso e caotico, utilizziamo la scala **`if / else if / ... / else`**, gli **`if` annidati** e una **bussola decisionale** per scegliere sempre lo strumento giusto.

---

### 💡 La Metafora: Il Nastro di Smistamento Logistico

> 💡 **Metafora:**  
> Pensa al nastro trasportatore di un grande centro logistico con bilancia e scanner ottico:
> - **La scala `if - else if - else` (I Varchi Progressivi):**  
>   Il pacco scorre sul nastro e incontra una serie di sensori posti in ordine:
>   1. Se pesa meno di 2 kg (`if`), viene deviato sulla rampa dei colli leggeri.
>   2. Altrimenti, se pesa meno di 10 kg (`else if`), finisce nella rampa media.
>   3. Altrimenti, se pesa meno di 30 kg (`else if`), va nei colli pesanti.
>   4. Se fallisce tutti i controlli precedenti (`else`), viene spinto sul binario dei colli speciali fuori misura.
>   *Regola fondamentale:* non appena un sensore intercetta il pacco e lo devia, **nessun altro sensore successivo lo esaminerà più**!
>
> - **L'`if` annidato (La Stanza di Sicurezza con Doppia Porta):**  
>   Per entrare nel caveau devi prima superare la porta esterna (`if`). Solo se sei dentro quella stanza trovi la seconda porta blindata (`if` interno). Se la prima porta non si apre, la seconda non la vedrai nemmeno!

---

### 🪜 La Scala `if / else if / else` per Alternative Disgiunte

Quando hai più di due alternative mutuamente esclusive (se ne verifica una, tutte le altre si escludono), si collegano più `if` a cascata:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
:Leggi Volume Fatturato;
if (Fatturato >= 50.000€?) then (SI)
  :Fascia Platinum (Sconto 15%);
elseif (Fatturato >= 20.000€?) then (SI)
  :Fascia Gold (Sconto 10%);
elseif (Fatturato >= 5.000€?) then (SI)
  :Fascia Silver (Sconto 5%);
else (NO)
  :Fascia Base (Nessuno sconto);
endif
:Applica sconto alla fattura;
stop
@enduml
```

#### ⚠️ Il Tranello dell'Ordine delle Condizioni
In una scala `if - else if`, **l'ordine delle condizioni è vitale**! Il computer le valuta dall'alto verso il basso e si ferma alla **prima condizione vera**.
Se ordini male le condizioni (es. mettendo la più generica prima di quella specifica), le condizioni successive diventeranno "codice morto", ovvero non verranno mai raggiunte!

---

### 🧩 `if` Annidati e l'Anti-Pattern della Piramide

Un `if` è **annidato** quando si trova all'interno del blocco `{}` di un altro `if`:

```cpp
if (clienteMaggiorenne) {
    if (redditoCertificato >= 20000.0) {
        std::cout << "Finanziamento concesso.\n";
    }
}
```

> ⚠️ **Attenzione all'Anti-Pattern "Pyramid of Doom" (La Piramide del Caos):**  
> Annidare `if` dentro `if` per 4 o 5 livelli rende il codice illeggibile e difficile da manutenere (il codice scivola continuamente a destra).  
> **Regola di pulizia:** se due condizioni devono verificarsi contemporaneamente senza azioni intermedie, **uniscile con l'operatore logico `&&`**:
> ```cpp
> if (clienteMaggiorenne && redditoCertificato >= 20000.0) {
>     std::cout << "Finanziamento concesso.\n";
> }
> ```

---

### 🧭 La Bussola Decisionale: Quale `if` Scegliere?

Di fronte a un problema logico, consulta questa tabella per scegliere il costrutto ottimale:

| Situazione del Problema | Struttura da Utilizzare | Esempio Pratico |
| :--- | :--- | :--- |
| **Azione opzionale (filtro / guardia):** devo fare qualcosa solo se c'è un'anomalia, altrimenti continuo normalmente. | `if` semplice (senza `else`) | Allarme scorte basse: avvisa solo se `scorte < soglia`. |
| **Aut-aut secco:** esattamente una strada tra due possibili. | `if - else` | Pagamento POS: o autorizzato o negato. |
| **Scaglioni continui / intervalli numerici:** il dato ricade in una sola fascia tra 3 o più alternative. | `if - else if - else` | Scaglioni di fatturato, fasce di peso, sconti per età. |
| **Verifiche preliminari bloccanti:** il secondo controllo ha senso solo se il primo ha avuto successo. | `if` annidato o condizioni con `&&` | Accesso al conto: PIN corretto prima, poi saldo sufficiente. |

---

### 🔬 Laboratorio PRIMM: Il Calcolo Scaglioni Clienti B2B

Implementiamo la politica di fidelizzazione aziendale per clienti Business-to-Business (B2B).

#### 1. PREDICT (Prevedi)
? Osserva questo codice che assegna un giudizio scolastico. Cosa verrà stampato a video se `voto = 85`?
```cpp
int voto = 85;
if (voto >= 60) {
    std::cout << "Sufficiente";
} else if (voto >= 80) {
    std::cout << "Ottimo";
} else {
    std::cout << "Non sufficiente";
}
```
- [ ] `Ottimo`
- [x] `Sufficiente`
- [ ] Stampa sia `Sufficiente` che `Ottimo`
- [ ] Errore di compilazione

<details>
<summary>💡 Spiegazione</summary>
Il programma valuta la prima condizione: <code>85 >= 60</code>, che è <b>vera</b>!  
Stampa immediatamente <code>"Sufficiente"</code> e <b>ignora tutto il resto della catena</b> (anche se 85 è maggiore di 80).  
<b>Lezione fondamentale:</b> quando confronti intervalli con <code>>=</code>, devi partire sempre dallo scaglione <b>più alto e restrittivo</b> e scendere verso il più basso!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `politica_sconti.cpp` con gli scaglioni ordinati correttamente dal più alto al più basso:

```cpp
/**
 * @file politica_sconti.cpp
 * @brief Calcolo sconti B2B a scaglioni di fatturato e verifica fido cliente.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>
#include <string>

/**
 * @brief Funzione principale: determina la fascia cliente e il fido commerciale.
 * @return int Codice di stato (0 = successo).
 */
int main() {
    /// Ragione sociale dell'azienda cliente
    std::string cliente = "TechSolutions S.r.l.";

    /// Volume d'affari annuo cumulato dal cliente
    double fatturatoAnnuo = 32500.00;

    /// Anzianita del cliente in anni di collaborazione
    int anniCollaborazione = 4;

    /// Percentuale di sconto commerciale da applicare
    double percentualeSconto = 0.0;
    std::string livelloFascia;

    // SCALA DECISIONALE A SCAGLIONI ORDINATI (dal piu alto al piu basso)
    if (fatturatoAnnuo >= 50000.0) {
        percentualeSconto = 0.15; /// Sconto Platinum: 15%
        livelloFascia = "Platinum";
    } else if (fatturatoAnnuo >= 20000.0) {
        percentualeSconto = 0.10; /// Sconto Gold: 10%
        livelloFascia = "Gold";
    } else if (fatturatoAnnuo >= 5000.0) {
        percentualeSconto = 0.05; /// Sconto Silver: 5%
        livelloFascia = "Silver";
    } else {
        percentualeSconto = 0.00; /// Fascia Standard: nessun sconto
        livelloFascia = "Standard";
    }

    std::cout << "=== PROFILO COMMERCIALE CLIENTE ===" << "\n";
    std::cout << "Cliente       : " << cliente << "\n";
    std::cout << "Fatturato     : " << fatturatoAnnuo << " EUR" << "\n";
    std::cout << "Fascia premio : " << livelloFascia << "\n";
    std::cout << "Sconto listino: " << (percentualeSconto * 100) << "%\n\n";

    // DECISIONE ANNIDATA: Valutazione affidamento creditizio (Fido)
    std::cout << "--- Istruttoria Fido Bancario/Commerciale ---" << "\n";
    if (fatturatoAnnuo >= 20000.0) {
        // Solo per clienti con buon fatturato, controlliamo l'affidabilita storica
        if (anniCollaborazione >= 3) {
            /// Fido accordato per clienti storici ad alto volume
            std::cout << "Esito: FIDO AZIENDALE CONCESSO (Linea di credito: 10.000 EUR)\n";
        } else {
            /// Volume alto ma cliente troppo recente: fido prudenziale
            std::cout << "Esito: FIDO LIMITATO (Cliente recente, max 2.500 EUR)\n";
        }
    } else {
        std::cout << "Esito: FIDO NEGATO (Fatturato insufficiente)\n";
    }

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Cortocircuito della Cascata)

Ora osserviamo come il processore naviga la catena `else if` ed entra solo nel blocco corretto:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20fatturato%20%3D%2032500.0%3B%0A%20%20%20%20int%20anni%20%3D%204%3B%0A%20%20%20%20double%20sconto%20%3D%200.0%3B%0A%0A%20%20%20%20if%20%28fatturato%20%3E%3D%2050000.0%29%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.15%3B%0A%20%20%20%20%7D%20else%20if%20%28fatturato%20%3E%3D%2020000.0%29%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.10%3B%0A%20%20%20%20%7D%20else%20if%20%28fatturato%20%3E%3D%205000.0%29%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.05%3B%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.0%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Sconto%3A%20%22%20%3C%3C%20sconto%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"**:
1. Alla riga `if (fatturato >= 50000.0)`: la condizione è `false` (32500 < 50000). Il cursore salta al primo `else if`.
2. Alla riga `else if (fatturato >= 20000.0)`: la condizione è `true` (32500 >= 20000).
3. Il processore entra nel blocco ed esegue `sconto = 0.10;`.
4. **Guarda attentamente il passo successivo:** la freccia di esecuzione **salta direttamente alla fine di tutta la catena**, oltrepassando gli altri `else if` e l'`else` senza nemmeno leggerli!

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Nuovo Scaglione Diamond:** Aggiungi in cima alla scala lo scaglione *Diamond*: per fatturati pari o superiori a `100.000€`, applica uno sconto del `20%` (`0.20`). Verifica che un fatturato di `120000` riceva lo sconto Diamond e non Platinum!
2. **Rifattorizzazione dell'`if` annidato:** Sostituisci l'`if` annidato del fido bancario con un'unica istruzione `if` con operatore logico `&&`:
   ```cpp
   if (fatturatoAnnuo >= 20000.0 && anniCollaborazione >= 3) {
       std::cout << "Fido concesso!\n";
   }
   ```
   Rifletti: il codice è più corto e chiaro? Quali sono i vantaggi?

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Calcolo Scaglioni di Imposta sul Reddito Aziendale (IRES/IRPEF)**  
> Nel diritto tributario ed economico, le imposte dirette sul reddito sono calcolate ad aliquote progressive per scaglioni.
> 
> Scrivi un programma C++ autonomo (`imposte_reddito.cpp`) che calcoli l'aliquota e l'imposta presunta dovuta da una ditta individuale:
> - Dichiara `std::string nomeDitta`: denominazione dell'impresa.
> - Dichiara `double redditoImponibile`: il reddito netto annuale dichiarato (es. `38500.00€`).
> - **Regola di Calcolo ad Aliquote Progressive (usando `if - else if - else`):**
>   - Fino a `15.000€` -> Aliquota **23%** (`0.23`).
>   - Da `15.000,01€` a `28.000€` -> Aliquota **25%** (`0.25`).
>   - Da `28.000,01€` a `50.000€` -> Aliquota **35%** (`0.35`).
>   - Oltre `50.000€` -> Aliquota massima **43%** (`0.43`).
> - Calcola l'importo totale dell'imposta stimata moltiplicando `redditoImponibile * aliquotaApplicata`.
> - **Bonus di Sostenibilità:** Aggiungi un flag `bool certificazioneGreen = true;`. Se l'azienda possiede la certificazione ambientale, applica una detrazione secca di `1.000€` dall'imposta dovuta (usa un `if` semplice come filtro).
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti proporzionati `///` con le motivazioni delle aliquote vigenti.
> - Stampa elegante del prospetto fiscale aziendale con riepilogo delle imposte.
## 🎛️ Capitolo 7: Lo Smistatore di Sportello (Il Costrutto switch-case)

> "La semplicità è il prerequisito per l'affidabilità di un'interfaccia utente."
> — *Edsger W. Dijkstra*

Nei capitoli precedenti abbiamo visto come l'`if` e l'`else if` siano perfetti per valutare condizioni con confronti e scaglioni numerici (`>` o `<`).  
Tuttavia, quando un software gestionale deve gestire un **menu a scelte fisse** (es. i tasti del bancomat: *1. Prelievo*, *2. Versamento*, *3. Saldo*) o **codici a singolo carattere** (es. `'A'`, `'B'`, `'C'`), scrivere una sfilza di `else if (scelta == 1) ... else if (scelta == 2)` diventa verboso e poco leggibile.

Per queste selezioni puntuali e discrete, il C++ mette a disposizione un costrutto compatto e velocissimo: lo **`switch-case`**.

---

### 💡 La Metafora: La Tastiera del Distributore Automatico

> 💡 **Metafora:**  
> Pensa alla tastiera di un distributore automatico di bevande o a uno sportello Bancomat (ATM):
> - Non digiti una formula o un intervallo; digiti un **singolo codice preciso**: tasto `1`, tasto `2`, oppure tasto `'A'`.
> - Lo **`switch`** è il microcontrollore interno: legge il tasto premuto e invia all'istante l'impulso al motorino corrispondente (**`case`**).
> - L'istruzione **`break`** è il freno meccanico di fine erogazione: una volta rilasciata la bibita, il carrello si ferma ed esce dalla macchina. Se il freno fosse rotto (dimentichi il `break`), la macchina continuerebbe a far scendere a cascata anche tutte le bibite dei cassetti successivi!
> - Il ramo **`default`** è lo schermo che mostra *"Codice non valido"* se premi un numero che non corrisponde a nessuno scompartimento attivo.

---

### ⚙️ Anatomia dello `switch-case`

Lo `switch` confronta una singola variabile con una lista di valori costanti:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
:Leggi codice scelta;
switch (scelta)
case ( 1 )
  :Esegui Operazione Prelievo;
  :break;
case ( 2 )
  :Esegui Operazione Versamento;
  :break;
case ( 3 )
  :Stampa Estratto Conto;
  :break;
case ( default )
  :Messaggio "Opzione non valida";
endswitch
:Prosegui programma;
stop
@enduml
```

#### Regole e Limiti Ferrei in C++
1. **Solo tipi discreti (interi e caratteri):** la variabile dello `switch` può essere solo di tipo `int`, `char`, `short` o `bool`. **Non si possono usare numeri con la virgola (`double`) né stringhe di testo (`std::string`)**!
2. **I valori dei `case` devono essere costanti:** non puoi scrivere `case variabile:` o `case x > 10:`. Solo valori fissi e noti a priori (es. `case 1:` o `case 'E':`).
3. **Il fenomeno del "Fall-Through" (Caduta a cascata):** se ometti l'istruzione `break;`, il C++ **non esce** dallo switch: prosegue ed esegue anche le istruzioni del `case` successivo, anche se la condizione non corrisponde!

#### Sfruttare il Fall-Through in Modo Intelligente
A volte la caduta a cascata è voluta. È utilissima per raggruppare più tasti che devono produrre lo stesso risultato (ad esempio maiuscolo e minuscolo):

```cpp
switch (risposta) {
    case 'S':
    case 's': // Se l'utente preme 'S' oppure 's', fa la stessa cosa!
        std::cout << "Operazione confermata.\n";
        break;
    case 'N':
    case 'n':
        std::cout << "Operazione annullata.\n";
        break;
}
```

---

### 🔬 Laboratorio PRIMM: Il Menu dello Sportello ATM

Realizziamo il terminale di gestione opzioni di uno sportello bancario automatico.

#### 1. PREDICT (Prevedi)
? Osserva questo frammento in cui è stato dimenticato un `break;`. Cosa verrà stampato se `tasto = 1`?
```cpp
int tasto = 1;
switch (tasto) {
    case 1:
        std::cout << "Saldo ";
    case 2:
        std::cout << "Estratto Conto ";
        break;
    default:
        std::cout << "Errore";
}
```
- [ ] Stampa solo `Saldo `
- [x] Stampa `Saldo Estratto Conto `
- [ ] Stampa `Saldo Estratto Conto Errore`
- [ ] Errore di compilazione

<details>
<summary>💡 Spiegazione</summary>
Il programma entra nel <code>case 1:</code> e stampa <code>"Saldo "</code>.  
Non trovando l'istruzione <code>break;</code>, il cursore "scivola giù" per inerzia (fall-through) ed esegue anche il <code>case 2:</code>, stampando <code>"Estratto Conto "</code>.  
Solo a quel punto incontra un <code>break;</code> ed esce dallo switch.  
<b>Regola d'oro:</b> a meno che tu non voglia intenzionalmente raggruppare due opzioni, ogni <code>case</code> deve terminare sempre con <code>break;</code>!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma gestionale per lo sportello ATM:

```cpp
/**
 * @file menu_atm.cpp
 * @brief Gestione menu interattivo per sportello bancario automatico (ATM).
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Funzione principale: simula la scelta dell'utente da tastierino ATM.
 * @return int Codice di stato (0 = esecuzione regolare).
 */
int main() {
    /// Saldo disponibile sul conto corrente del cliente
    double saldoConto = 1850.50;

    /// Tasto opzione simulato selezionato dal cliente (1, 2, 3 o 0)
    int sceltaMenu = 2;

    std::cout << "======================================" << "\n";
    std::cout << "       SPORTELLO BANCOMAT B2B        " << "\n";
    std::cout << "======================================" << "\n";
    std::cout << "1. Visualizza Saldo Disponibile" << "\n";
    std::cout << "2. Prelievo Rapido Standard (50 EUR)" << "\n";
    std::cout << "3. Versamento Contanti" << "\n";
    std::cout << "0. Restituisci Carta ed Esci" << "\n";
    std::cout << "--------------------------------------" << "\n";
    std::cout << "Scelta effettuata: " << sceltaMenu << "\n\n";

    // SMISTATORE AUTOMATICO A CASI DISCRETI
    switch (sceltaMenu) {
        case 1:
            /// Consultazione saldo contabile
            std::cout << ">>> SALDO DISPONIBILE: " << saldoConto << " EUR\n";
            break;

        case 2: {
            /// Prelievo predefinito con aggiornamento saldo
            const double PRELIEVO_RAPIDO = 50.00;
            if (saldoConto >= PRELIEVO_RAPIDO) {
                saldoConto -= PRELIEVO_RAPIDO;
                std::cout << ">>> EROGAZIONE IN CORSO: 50.00 EUR ritirati.\n";
                std::cout << ">>> NUOVO SALDO RESIDUO: " << saldoConto << " EUR\n";
            } else {
                std::cout << ">>> ERRORE: Fondi insufficienti per il prelievo.\n";
            }
            break;
        }

        case 3:
            /// Informativa versamento
            std::cout << ">>> SPORTELLO APERTO: Inserire le banconote nella fessura.\n";
            break;

        case 0:
            /// Chiusura sessione
            std::cout << ">>> Arrivederci. Ricordati di ritirare la tua carta!\n";
            break;

        default:
            /// Gestione di qualsiasi tasto non previsto
            std::cout << ">>> CODICE NON VALIDO: Scelta inesistente. Riprovare.\n";
            break;
    }

    std::cout << "\nOperazione conclusa. Grazie per aver scelto la nostra banca.\n";
    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Salto Diretto nello Stack)

Visualizziamo la rapidità con cui il computer raggiunge l'opzione corretta:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20saldo%20%3D%201850.50%3B%0A%20%20%20%20int%20scelta%20%3D%202%3B%0A%0A%20%20%20%20switch%20%28scelta%29%20%7B%0A%20%20%20%20%20%20%20%20case%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Saldo%3A%20%22%20%3C%3C%20saldo%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20break%3B%0A%20%20%20%20%20%20%20%20case%202%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20saldo%20-%3D%2050.0%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Ritirati%2050%2C%20nuovo%3A%20%22%20%3C%3C%20saldo%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20break%3B%0A%20%20%20%20%20%20%20%20default%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Altro%5Cn%22%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20break%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"**:
1. All'istruzione `switch (scelta)`:
   - Poiché `scelta` vale `2`, la freccia verde **non legge nemmeno** il `case 1:`.
   - Salta con un balzo secco direttamente alla riga del `case 2:`.
2. Esegue `saldo -= 50.0;` e la stampa a video.
3. Raggiunge l'istruzione `break;`: osserva come il cursore viene proiettato istantaneamente **fuori dalla parentesi graffa di chiusura** dello `switch`, senza toccare il `default`.

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Aggiungi l'opzione Ricarica Telefonica:** Aggiungi un `case 4:` per consentire una ricarica telefonica fissa da 20.00€. Ricordati di scalare l'importo dal saldo e di inserire il `break;`!
2. **Doppio Tasto di Uscita (Fall-Through utile):** Modifica il codice in modo che sia premendo `0` sia premendo `9` il programma esegua la procedura di uscita (`case 0:` seguito immediatamente da `case 9:` senza break in mezzo).
3. **Proviamo l'errore del tipo `double`:** Prova a cambiare `double sceltaMenu = 2.0;`. Cosa ti urla il compilatore?  
   <details>
   <summary>💡 Spiegazione dell'errore di compilazione</summary>
   Il compilatore rifiuterà il codice con:  
   <code>error: switch quantity not an integer</code>.  
   Questo ti ricorda che lo <code>switch</code> funziona solo su categorie discrete intere o caratteri, mai su numeri con la virgola!
   </details>

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Convertitore di Valuta del Terminale Cassa**  
> Nei negozi duty-free aeroportuali, i clienti possono pagare scegliendo tra diverse valute estere. La cassa calcola il controvalore in Euro applicando il tasso di cambio convenzionato.
> 
> Scrivi un programma C++ autonomo (`cambio_valute.cpp`):
> - Dichiara `double importoValutaEstera`: cifra pagata dal cliente (es. `120.00`).
> - Dichiara `char codiceValuta`: codice della moneta estera consegnata:
>   - `'U'` oppure `'u'`: Dollaro USA (USD) -> moltiplica per tasso `0.92` per ottenere gli Euro.
>   - `'G'` oppure `'g'`: Sterlina Inglese (GBP) -> moltiplica per tasso `1.18`.
>   - `'J'` oppure `'j'`: Yen Giapponese (JPY) -> moltiplica per tasso `0.0061`.
>   - `'S'` oppure `'s'`: Franco Svizzero (CHF) -> moltiplica per tasso `1.05`.
>   - Per qualsiasi altro carattere (`default`): stampa un messaggio d'errore: *"Valuta non supportata dal POS di cassa!"*.
> - Sfrutta la tecnica del *fall-through* per far funzionare lo `switch` sia con lettere maiuscole sia con minuscole.
> - Se la valuta è valida, calcola e visualizza:
>   - L'importo in valuta originale.
>   - Il tasso di cambio applicato.
>   - Il controvalore netto accreditato sul conto dell'azienda in Euro.
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti `///` proporzionati per documentare i tassi di cambio.
> - Gestione corretta dei `break;` su tutti i case.
## 🔄 Capitolo 8: L'Anello Fondamentale (L'Iterazione Indefinita con il Ciclo while)

> "Iterare è umano, automatizzare è informatica."
> — *Adattamento da L. Peter Deutsch*

Immagina di essere il cassiere di un supermercato. Un cliente si avvicina al nastro trasportatore: quanti articoli ha nel carrello? Possono essere 3, 12 oppure 75. Non puoi saperlo prima di iniziare!

Se dovessimo usare solo le istruzioni viste finora, saremmo bloccati: dovremmo dichiarare decine di variabili (`prezzo1`, `prezzo2`, `prezzo3`...) sperando che bastino.  
Questo è il vicolo cieco del codice lineare. La vera potenza di un computer sta nella sua capacità instancabile di **ripetere lo stesso blocco di istruzioni finché una determinata condizione rimane vera**.

Questo meccanismo si chiama **iterazione** (o ciclo), e la sua forma più pura ed essenziale è il ciclo **`while`**.

---

### 💡 La Metafora: Il Nastro della Cassa Continua

> 💡 **Metafora:**  
> Pensa al nastro scorrevole della cassa di un ipermercato:
> - Finché sul nastro c'è un articolo da scansionare (**condizione vera**), il nastro avanza, il laser legge il prezzo, il totale cresce e il cassiere mette il prodotto nella busta.
> - Quando arriva il blocchetto separatore con lo zero (**valore sentinella** di fine spesa), la condizione diventa **falsa**: il rullo si ferma all'istante e la cassa emette lo scontrino finale.
> - Se il cliente arriva con il carrello vuoto (**condizione falsa in partenza**), il nastro non fa neppure un solo giro: il ciclo viene eseguito **zero volte**!

---

### ⚙️ Il Controllo in Testa e i Tre Ingredienti Vitali

Il ciclo `while` è un costrutto con **controllo in testa**: la condizione viene verificata *prima* di eseguire qualsiasi istruzione all'interno del blocco.

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
:1. Inizializza Variabile di Controllo;
while (2. Condizione di Continuazione?) is (VERO)
  :Esegui azioni del corpo;
  :3. Aggiorna Variabile di Controllo;
endwhile (FALSO)
:Prosegui con il resto del programma;
stop
@enduml
```

Per costruire un ciclo sano e funzionante, servono **tassativamente tre ingredienti**:

1. **Inizializzazione:** la variabile di controllo deve avere un valore di partenza sensato *prima* di entrare nel ciclo (es. `int tentativi = 0;`).
2. **Condizione di continuazione (Predicato):** la domanda tra parentesi `while (condizione)`. Finché risponde `true`, il corpo continua a ripetersi.
3. **Aggiornamento:** all'interno del corpo del ciclo, deve esserci un'istruzione che modifica la variabile di controllo (es. `tentativi++;` oppure la lettura di un nuovo dato da tastiera).

> ☠️ **L'Incubo del Ciclo Infinito:**  
> Se dimentichi l'ingrediente 3 (l'aggiornamento), la condizione rimarrà per sempre vera! Il processore rimarrà intrappolato per l'eternità a eseguire le stesse righe, bloccando il programma (consumando il 100% della CPU).

---

### 🧮 Due Pattern Algoritmici Essenziali: Contatore e Accumulatore

Nel software gestionale, il ciclo `while` viene quasi sempre associato a due ruoli chiave:

| Pattern | Ruolo Aziendale | Come si scrive in C++ |
| :--- | :--- | :--- |
| **Il Contatore** | Conta **quante volte** accade un evento (es. numero di articoli comprati). | `conteggio++;` (oppure `conteggio = conteggio + 1;`) |
| **L'Accumulatore** | Calcola la **somma progressiva** di valori diversi (es. il totale in denaro). | `totale += prezzo;` (oppure `totale = totale + prezzo;`) |

#### Il Concetto di "Valore Sentinella"
In molti contesti non sai a priori quanti dati inserirà l'utente. Si adotta quindi un **valore sentinella**: un valore speciale e convenzionale (es. `0` per i prezzi, o `-1` per i giorni lavorati) che non rappresenta un dato reale, ma funge da segnale convenuto di chiusura dei lavori.

---

### 🔬 Laboratorio PRIMM: Il Registratore di Cassa Continua

Realizziamo il software di battitura scontrini di un punto vendita al dettaglio.

#### 1. PREDICT (Prevedi)
? Osserva attentamente questo ciclo con controllo in testa. Quante volte verrà stampata la parola `"Elaborazione"`?
```cpp
int pezzi = 10;
while (pezzi < 5) {
    std::cout << "Elaborazione\n";
    pezzi++;
}
std::cout << "Fine spesa\n";
```
- [x] 0 volte (non viene mai stampata)
- [ ] 1 volta
- [ ] 5 volte
- [ ] Il ciclo è infinito

<details>
<summary>💡 Spiegazione</summary>
Il ciclo <code>while</code> ha il <b>controllo in testa</b>: prima di eseguire il corpo, verifica la condizione.  
Dato che <code>pezzi</code> vale 10, la condizione <code>10 < 5</code> è <b>falsa fin dal primissimo istante</b>!  
Il computer scavalca immediatamente l'intero blocco ed esegue direttamente <code>std::cout << "Fine spesa\n";</code>.
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `cassa_continua.cpp`. Nota come la variabile `prezzoArticolo` viene inizializzata prima del ciclo, testata nella guardia del `while` e aggiornata ad ogni passaggio tramite `std::cin`:

```cpp
/**
 * @file cassa_continua.cpp
 * @brief Registratore di cassa per punto vendita con sentinella di fine spesa.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Funzione principale: batte scontrini fino all'inserimento dello 0.
 * @return int Codice di uscita (0 = cassa chiusa regolarmente).
 */
int main() {
    /// Accumulatore: somma monetaria progressiva degli articoli battuti
    double totaleSpesa = 0.0;

    /// Contatore: numero complessivo di articoli acquistati
    int numeroArticoli = 0;

    /// Variabile di controllo: prezzo dell'articolo corrente
    double prezzoArticolo = 0.0;

    std::cout << "======================================" << "\n";
    std::cout << "     CASSA CONTINUA PUNTO VENDITA    " << "\n";
    std::cout << " Inserisci i prezzi dei prodotti (EUR)\n";
    std::cout << " Digita 0 quando hai terminato la spesa\n";
    std::cout << "======================================" << "\n\n";

    // 1. Prima lettura (Inizializzazione esterna)
    std::cout << "Prezzo primo articolo: ";
    std::cin >> prezzoArticolo;

    // 2. Controllo in testa con Sentinella (0.0 indica la fine)
    while (prezzoArticolo != 0.0) {
        // Aggiornamento dell'accumulatore e del contatore
        totaleSpesa += prezzoArticolo;
        numeroArticoli++;

        std::cout << "-> Articolo n. " << numeroArticoli << " registrato (" 
                  << prezzoArticolo << " EUR). Totale provvisorio: " 
                  << totaleSpesa << " EUR\n";

        // 3. Nuova lettura per il prossimo giro (Aggiornamento della variabile)
        std::cout << "Prezzo prossimo articolo (0 per chiudere): ";
        std::cin >> prezzoArticolo;
    }

    // Chiusura e stampa dello scontrino fiscale
    std::cout << "\n========== SCONTRINO FISCALE ==========" << "\n";
    std::cout << "Pezzi battuti   : " << numeroArticoli << "\n";
    std::cout << "TOTALE DOVUTO   : " << totaleSpesa << " EUR\n";
    std::cout << "=======================================" << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: L'Anello nello Stack)

Ora apriamo Python Tutor per osservare come si comportano l'accumulatore e il contatore nello stack di memoria:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20totale%20%3D%200.0%3B%0A%20%20%20%20int%20articoli%20%3D%200%3B%0A%20%20%20%20double%20prezzo%20%3D%2015.50%3B%20//%20Simulazione%20primo%20articolo%0A%0A%20%20%20%20while%20%28prezzo%20%21%3D%200.0%29%20%7B%0A%20%20%20%20%20%20%20%20totale%20%2B%3D%20prezzo%3B%0A%20%20%20%20%20%20%20%20articoli%2B%2B%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20//%20Simuliamo%20l'avanzamento%20della%20cassa%0A%20%20%20%20%20%20%20%20if%20%28articoli%20%3D%3D%201%29%20prezzo%20%3D%204.50%3B%0A%20%20%20%20%20%20%20%20else%20prezzo%20%3D%200.0%3B%20//%20Sentinella%20di%20uscita%0A%20%20%20%20%7D%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"** osservando la colonna a destra:
1. Ad ogni iterazione, la freccia verde risale in alto fino alla riga del `while`: è questo l'**anello**!
2. Guarda come nello stack `totale` si aggiorna progressivamente (`0.0` -> `15.5` -> `20.0`), mentre `articoli` conta i passaggi (`0` -> `1` -> `2`).
3. Quando `prezzo` viene impostato a `0.0`, la condizione `prezzo != 0.0` diventa `false`: la freccia non entra più nel blocco e salta direttamente al `return 0;`.

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Calcolo della Spesa Media per Articolo:** Al termine del ciclo, prima di stampare lo scontrino, calcola e visualizza lo scontrino medio per pezzo (`totaleSpesa / numeroArticoli`).  
   *Attenzione:* usa un `if` per assicurarti che `numeroArticoli > 0`, evitando la divisione per zero se il cliente esce senza comprare nulla!
2. **Scarta i Prezzi Negativi:** Se il cassiere digita per errore un prezzo negativo (es. `-5.0`), non sommarlo alla spesa ma stampa: *"Errore: importo negativo non valido!"*.
3. **Simuliamo il Ciclo Infinito:** Prova a commentare la riga `std::cin >> prezzoArticolo;` all'interno del corpo del ciclo con `//`. Cosa succede quando premi Run?  
   <details>
   <summary>💡 Spiegazione dell'errore di esecuzione</summary>
   Dato che il valore di <code>prezzoArticolo</code> non cambia mai, la condizione resterà perennemente vera. Il programma continuerà a stampare all'infinito finché il sistema o il browser non interromperanno forzatamente il processo per timeout!
   </details>

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Registro Fatture Passive dei Fornitori**  
> L'ufficio contabilità deve registrare gli importi delle fatture passive arrivate dai fornitori durante la settimana per monitorare il fabbisogno di liquidità.
> 
> Scrivi un programma C++ autonomo (`fatture_fornitori.cpp`):
> - Utilizza un ciclo `while` per richiedere l'inserimento degli importi delle fatture (in Euro).
> - Usa il valore sentinella `-1.0` per terminare l'inserimento.
> - Durante il ciclo:
>   - Accumula il debito totale verso i fornitori (`totaleDebiti`).
>   - Conta quante fatture sono state registrate in totale.
>   - Conta anche quante fatture sono considerate "Fatture Rilevanti" (importo `>= 1000.00€`).
> - Al termine del ciclo, stampa il riepilogo contabile:
>   - Totale generale debiti da liquidare.
>   - Numero totale fatture.
>   - Numero fatture rilevanti oltre i 1.000€.
>   - Percentuale delle fatture rilevanti rispetto al totale.
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti proporzionati `///` per descrivere i contatori e gli accumulatori.
> - Gestione corretta dell'uscita con la sentinella senza sommare il `-1.0` al totale.
## ⏳ Capitolo 9: Il Contatore Compatto (Il Ciclo for)

> "La regolarità e la prevedibilità sono le migliori alleate della precisione contabile."
> — *Principio di Revisione Aziendale*

Nel capitolo precedente abbiamo scoperto il ciclo `while`, ideale quando **non sappiamo a priori** quante volte dovremo ripetere un'azione (come la cassa che batte scontrini finché il cliente non ha finito gli articoli).

Tuttavia, in moltissimi contesti aziendali il numero di ripetizioni è **noto e prestabilito fin dall'inizio**:
- Calcolare l'ammortamento contabile di un cespite per **5 anni**.
- Elaborare le buste paga dei **12 mesi** dell'esercizio.
- Stampare il piano di rimborso di un finanziamento in **24 rate**.

Anche per questi problemi potremmo usare un `while`, ma c'è un rischio: i tre ingredienti vitali (inizializzazione, condizione e aggiornamento) si trovano sparpagliati in punti diversi del file. Dimenticare l'aggiornamento in fondo a un blocco lungo è un errore comunissimo.

Per risolvere questo problema, il C++ mette a disposizione il ciclo **`for`**: un costrutto compatto che raccoglie l'intero meccanismo di controllo in una sola riga chiara e ordinata.

---

### 💡 La Metafora: Il Cronometro di Precisione con Timer

> 💡 **Metafora:**  
> Pensa all'impostazione di un timer sul microonde o su una macchina industriale:
> - Nel `while`, dovevi ricordarti tu a mano di accendere il timer prima di entrare nella stanza, controllare l'orologio a ogni secondo e avanzare le lancette prima di uscire.
> - Nel **`for`**, imposti tutto direttamente sul display all'inizio:  
>   *"Parti da 1; fermati a 5; aumenta di 1 a ogni scatto"*.  
> - La macchina esegue la sequenza con precisione millimetrica senza che tu possa dimenticare di mandare avanti il contatore.

---

### 🔍 Il `for` come Forma Compatta del `while`

Dal punto di vista del calcolatore, il ciclo `for` non fa nulla che il `while` non sapesse già fare: è una forma di scrittura più comoda ed elegante (talvolta chiamata *zucchero sintattico*), pensata per aiutare la mente del programmatore a **non dimenticare i passaggi chiave**.

Osserva come i due costrutti si corrispondono riga per riga:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

rectangle "Con il ciclo WHILE" as W {
  [1. int i = 1; (Inizializzazione)]
  --> [2. while (i <= 5) (Condizione)]
  --> [Corpo: elabora dato]
  --> [3. i++; (Aggiornamento)]
}

rectangle "Con il ciclo FOR (Tutto in una riga!)" as F {
  [for ( 1. int i = 1 ;  2. i <= 5 ;  3. i++ )]
  --> [Corpo: elabora dato]
}
@enduml
```

#### Anatomia dell'Intestazione del `for`
L'intestazione è separata da **due punti e virgola `;` obbligatori**:

```cpp
for (inizializzazione ; condizione / predicato ; aggiornamento) {
    // Istruzioni da ripetere
}
```

1. **Inizializzazione (`int i = 1;`):** viene eseguita **una sola volta**, all'inizio assoluto del ciclo. In C++ moderno dichiariamo la variabile contatore direttamente qui dentro: in questo modo il contatore nasce e vive *solo* dentro il ciclo, evitando di sporcare la memoria esterna!
2. **Condizione / Predicato (`i <= 5;`):** viene testata **prima di ogni giro**. Se è vera, si esegue il blocco; se è falsa, si esce immediatamente.
3. **Aggiornamento (`i++`):** viene eseguito automaticamente **al termine di ogni giro**, subito prima di ritestare la condizione.

---

### 🔬 Laboratorio PRIMM: Il Piano di Ammortamento Cespiti

Nell'economia aziendale, i beni strumentali durevoli (computer, macchinari, veicoli) perdono valore ogni anno. Questo processo contabile si chiama **ammortamento a quote costanti**.

#### 1. PREDICT (Prevedi)
? Osserva questo ciclo `for`. Quante righe verranno stampate a video?
```cpp
for (int anno = 1; anno < 5; ++anno) {
    std::cout << "Esercizio contabile\n";
}
```
- [ ] 5 righe
- [x] 4 righe (per anno = 1, 2, 3, 4)
- [ ] 0 righe
- [ ] Il ciclo è infinito

<details>
<summary>💡 Spiegazione</summary>
Attenzione al classico errore <b>Off-by-One</b> (errore di uno):  
La condizione è <code>anno < 5</code> (strettamente minore), <b>non</b> <code>anno <= 5</code>!  
Il contatore assumerà i valori 1, 2, 3, 4 (esattamente <b>4 iterazioni</b>). Quando <code>anno</code> diventa 5, la condizione <code>5 < 5</code> è falsa e il ciclo si arresta prima di stampare la quinta volta.  
Se vuoi contare esattamente fino a 5, devi usare <code>anno <= 5</code>.
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `piano_ammortamento.cpp`. Calcoliamo la quota e il valore residuo di un macchinario aziendale su un arco di 5 anni:

```cpp
/**
 * @file piano_ammortamento.cpp
 * @brief Calcolo del piano di ammortamento a quote costanti di un cespite aziendale.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Funzione principale: genera il prospetto contabile su N anni.
 * @return int Codice di uscita (0 = esecuzione regolare).
 */
int main() {
    /// Costo storico di acquisto del bene strumentale
    const double VALORE_INIZIALE = 20000.00;

    /// Numero di esercizi contabili di ammortamento previsti dal piano
    const int NUMERO_ANNI = 5;

    /// Quota annuale costante di ammortamento (ripartizione uniforme)
    const double QUOTA_ANNUA = VALORE_INIZIALE / NUMERO_ANNI;

    /// Valore contabile residuo del bene (decresce ogni anno)
    double valoreResiduo = VALORE_INIZIALE;

    std::cout << "=================================================" << "\n";
    std::cout << "    PIANO DI AMMORTAMENTO CESPITI AZIENDALI      " << "\n";
    std::cout << " Costo Storico: " << VALORE_INIZIALE << " EUR | Durata: " 
              << NUMERO_ANNI << " Anni" << "\n";
    std::cout << " Quota Annua  : " << QUOTA_ANNUA << " EUR/anno\n";
    std::cout << "=================================================" << "\n";
    std::cout << " Anno | Quota Ammortamento | Valore Residuo Fine Anno\n";
    std::cout << "-------------------------------------------------" << "\n";

    // CICLO FOR: Controllo compatto (inizializzazione, condizione, incremento)
    for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
        // Aggiorniamo il valore del bene scalando la quota annua
        valoreResiduo -= QUOTA_ANNUA;

        std::cout << "   " << anno << "  |     " 
                  << QUOTA_ANNUA << " EUR      |     " 
                  << valoreResiduo << " EUR\n";
    }

    std::cout << "-------------------------------------------------" << "\n";
    std::cout << "Cespite completamente ammortizzato. Valore finale: " 
              << valoreResiduo << " EUR\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Contatore e lo Scope nel `for`)

Visualizziamo passo dopo passo come il processore governa il contatore compatto del `for`:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20const%20int%20ANNI%20%3D%203%3B%0A%20%20%20%20double%20valore%20%3D%2015000.0%3B%0A%20%20%20%20double%20quota%20%3D%205000.0%3B%0A%0A%20%20%20%20for%20%28int%20anno%20%3D%201%3B%20anno%20%3C%3D%20ANNI%3B%20%2B%2Banno%29%20%7B%0A%20%20%20%20%20%20%20%20valore%20-%3D%20quota%3B%0A%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20anno%20%3C%3C%20%22%3A%20%22%20%3C%3C%20valore%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"** osservando lo stack a destra:
1. Quando l'esecuzione tocca la riga del `for`, nello stack viene creata la variabile `anno = 1`.
2. Il processore valuta la condizione `1 <= 3` (vera) ed entra nel corpo, aggiornando `valore`.
3. Al termine del corpo, la freccia torna alla riga del `for`: vedi che `anno` diventa `2`, e viene subito ritestata la condizione.
4. **Osserva cosa succede alla fine del 3° anno:** quando `anno` diventa `4`, la condizione `4 <= 3` è falsa.  
   La freccia esce dal ciclo e **la variabile `anno` scompare istantaneamente dallo stack!** Non esiste più al di fuori del ciclo (la regola dello scope del Locker!).

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Il Fondo Ammortamento Cumulativo:** Dichiara una variabile `double fondoAmmortamento = 0.0;` prima del ciclo. A ogni giro, somma la quota al fondo (`fondoAmmortamento += QUOTA_ANNUA;`) e visualizzala nella tabella accanto al valore residuo.
2. **Ammortamento a Ritroso:** Modifica l'intestazione del ciclo per contare alla rovescia, partendo dall'anno 5 fino all'anno 1:
   ```cpp
   for (int anniRimanenti = NUMERO_ANNI; anniRimanenti >= 1; --anniRimanenti)
   ```
3. **La prova dello Scope:** Prova a scrivere `std::cout << anno;` subito dopo la graffa di chiusura del `for`. Che errore ti segnala il compilatore?  
   <details>
   <summary>💡 Spiegazione dell'errore di compilazione</summary>
   Riceverai: <code>error: 'anno' was not declared in this scope</code>.  
   Questo conferma che dichiarare il contatore dentro l'intestazione del <code>for</code> garantisce che la variabile non resti attiva per errore nel resto del programma.
   </details>

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Piano di Crescita con Interesse Composto**  
> Un'impresa vincola un capitale di liquidità in un conto deposito remunerato per $N$ anni a tasso fisso. Ogni anno gli interessi maturati si sommano al capitale, generando a loro volta nuovi interessi (capitalizzazione composta).
> 
> Scrivi un programma C++ autonomo (`interesse_composto.cpp`):
> - Dichiara il capitale iniziale depositato: `double capitale = 10000.00;` (10.000 EUR).
> - Dichiara il tasso di interesse attivo annuo: `const double TASSO = 0.04;` (4%).
> - Dichiara la durata dell'investimento in anni: `const int ANNI_INVESTIMENTO = 6;`.
> - Utilizza un ciclo `for` a contatore (`anno = 1` fino a `ANNI_INVESTIMENTO`) per:
>   - Calcolare gli interessi maturati in quell'anno: `interessiAnno = capitale * TASSO;`.
>   - Incrementare il capitale: `capitale += interessiAnno;`.
>   - Stampare anno per anno: Anno, Interessi guadagnati nel periodo, e Nuovo Capitale Maturato.
> - Al termine del ciclo, calcola e visualizza il guadagno netto totale ottenuto dall'azienda al termine dei 6 anni (`capitaleFinale - 10000.00`).
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti proporzionati `///` per descrivere le variabili finanziarie.
> - Formattazione ordinata dei dati in tabella.
## 🔁 Capitolo 10: Garantire l'Azione (Il Ciclo do-while e la Validazione dell'Input)

> "Fidarsi è bene, validare l'input prima di registrarlo è sicurezza informatica."
> — *Regola Aurea dello Sviluppo Software*

Nei capitoli precedenti abbiamo esplorato il ciclo `while` e il ciclo `for`: entrambi hanno il **controllo in testa**, il che significa che se la condizione di partenza è falsa, il corpo del ciclo non viene eseguito nemmeno una volta (zero iterazioni).

Tuttavia, esistono situazioni in cui **un'azione deve essere eseguita per forza almeno una volta**, prima ancora di poter fare qualsiasi verifica:
- Chiedere all'utente di digitare un dato (es. l'importo di un bonifico): non puoi controllare se l'importo è corretto prima che l'utente l'abbia inserito!
- Mostrare un menu operativo a video: devi prima mostrare le opzioni, consentire la scelta e solo dopo verificare se l'utente desidera uscire.

Per queste esigenze, il C++ offre il ciclo **`do-while`**: il costrutto con **controllo in coda**.

---

### 💡 La Metafora: Il Modulo con Campi Obbligatori

> 💡 **Metafora:**  
> Pensa alla compilazione di un modulo di pagamento su un sito bancario:
> - Prima di tutto, la pagina ti presenta il modulo e ti chiede di compilare i dati (**il blocco `do` viene eseguito almeno una volta**).
> - Quando premi "Invia", il sistema controlla:  
>   *"I dati inseriti contengono errori?"* (**controllo in coda**).
> - Se c'è un errore (es. importo negativo o superiore al massimale), il modulo ti viene ripresentato e sei costretto a correggerlo.
> - La richiesta si ripete **finché la condizione di errore rimane vera** (cioè finché non inserisci un dato finalmente valido!).

---

### ⚙️ Il `do-while` come Comodità di Scrittura

Anche il `do-while` è una forma comoda ed elegante di scrittura che evita la duplicazione del codice.

Se volessimo validare un input usando solo un normale `while`, dovremmo copiare e incollare l'istruzione di lettura due volte (una volta prima del ciclo e una volta dentro):

```cpp
// VALIDAZIONE SCOMODA CON IL WHILE (codice duplicato):
std::cout << "Inserisci importo: ";
std::cin >> importo; // <-- 1a lettura duplicata
while (importo <= 0.0) {
    std::cout << "Errore! Inserisci importo: ";
    std::cin >> importo; // <-- 2a lettura duplicata
}
```

Con il `do-while`, la richiesta viene scritta **una sola volta**, garantendo che venga eseguita subito e poi ripetuta all'occorrenza:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
repeat
  :1. Esegui il corpo (es. Chiedi dato da tastiera);
repeat while (2. Il dato e' ERRATO?) is (VERO: ripeti richiesta)
->FALSO: dato valido;
:Prosegui con l'operazione bancaria;
stop
@enduml
```

#### ⚠️ La Logica della Condizione: Ripetere Finché C'è un Errore
Fai molta attenzione alla domanda posta nel `while` in coda:
- La condizione tra parentesi **non indica quando il dato è valido**, ma stabilisce **quando il ciclo deve continuare a ripetersi**!
- Si ripete **finché la negazione della condizione di validità è soddisfatta** (cioè finché il dato inserito è errato).

```cpp
// Vogliamo che l'importo sia compreso tra 1€ e 5.000€ (dato valido: importo > 0 && importo <= 5000)
// Il ciclo deve ripetersi finche il dato e FUORI dai limiti:
do {
    std::cout << "Importo bonifico (max 5000 EUR): ";
    std::cin >> importo;
} while (importo <= 0.0 || importo > 5000.0); // <-- Ripeti finche e NON valido!
```

> ⚠️ **Sintassi: Il Punto e Virgola Finale Obbligatorio!**  
> A differenza dell'`if`, del `while` normale e del `for`, l'istruzione `do { ... } while (condizione);` **richiede tassativamente il punto e virgola `;` finale** dopo la parentesi tonda di chiusura. Se lo dimentichi, il compilatore segnalerà un errore di sintassi.

---

### 🧭 Quadro Comparativo Finale: Quale Ciclo Scegliere?

Con l'introduzione del `do-while`, hai completato la triade fondamentale dei cicli in C++. Ecco la guida rapida per scegliere a colpo sicuro:

| Situazione Operativa | Ciclo Consigliato | Perché questa scelta? |
| :--- | :--- | :--- |
| **Iterazione Definita:** Conosciamo già a priori il numero esatto di passaggi ($N$ anni, 12 mesi, dimensione nota). | **`for`** | Raccoglie contatore, limite e incremento in una riga compatta ed elegante. |
| **Iterazione Indefinita (0 o più volte):** Dipende da un evento esterno o sentinella, e potremmo non dover eseguire nulla se la condizione iniziale è già falsa. | **`while`** | Il controllo in testa garantisce la sicurezza prima di compiere qualsiasi azione. |
| **Validazione Input o Menu (almeno 1 volta):** L'azione deve essere necessariamente compiuta prima di poter verificare l'esito. | **`do-while`** | Garantisce la prima esecuzione senza duplicare il codice di richiesta. |

---

### 🔬 Laboratorio PRIMM: Il Bonifico Bancario Protetto

Realizziamo il modulo di acquisizione sicura dell'importo per un bonifico bancario aziendale.

#### 1. PREDICT (Prevedi)
? Osserva questo codice in cui la condizione è falsa fin dall'inizio. Cosa verrà stampato a video?
```cpp
int tentativi = 10;
do {
    std::cout << "Controllo eseguito ";
} while (tentativi < 3);
std::cout << "Fine";
```
- [ ] Stampa solo `Fine`
- [x] Stampa `Controllo eseguito Fine`
- [ ] Il ciclo è infinito
- [ ] Errore di compilazione per il punto e virgola

<details>
<summary>💡 Spiegazione</summary>
Il ciclo <code>do-while</code> ha il <b>controllo in coda</b>: il computer esegue prima il corpo del <code>do</code> (stampando <code>"Controllo eseguito "</code>) e solo <i>dopo</i> valuta la condizione <code>10 < 3</code>.  
Poiché 10 non è minore di 3, la condizione risulta <code>false</code> e il ciclo si interrompe, stampando infine <code>"Fine"</code>.  
Anche con una condizione falsa in partenza, il <code>do-while</code> garantisce <b>sempre almeno un'esecuzione</b>!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `bonifico_sicuro.cpp`. L'algoritmo obbliga l'utente a reinserire l'importo finché non rispetta le regole aziendali di sicurezza:

```cpp
/**
 * @file bonifico_sicuro.cpp
 * @brief Acquisizione e validazione robusta dell'importo per un bonifico bancario.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Funzione principale: valida l'importo e conferma la disposizione bancaria.
 * @return int Codice di stato (0 = operazione autorizzata).
 */
int main() {
    /// Massimale di sicurezza giornaliero per bonifici online
    const double MASSIMALE_GIORNALIERO = 5000.00;

    /// Variabile per l'importo inserito dal cliente
    double importoBonifico = 0.0;

    std::cout << "==========================================" << "\n";
    std::cout << "      DISPOSIZIONE BONIFICO BANCARIO      " << "\n";
    std::cout << " Vincoli: importo > 0 e max 5.000,00 EUR  " << "\n";
    std::cout << "==========================================" << "\n\n";

    // CICLO DO-WHILE: La richiesta viene eseguita almeno una volta
    // e ripetuta finche la condizione di validita e violata (negazione)
    do {
        std::cout << "Inserisci l'importo da trasferire (EUR): ";
        std::cin >> importoBonifico;

        // Feedback immediato se il dato non rispetta i vincoli
        if (importoBonifico <= 0.0) {
            std::cout << ">>> ERRORE: L'importo deve essere positivo e maggiore di zero!\n\n";
        } else if (importoBonifico > MASSIMALE_GIORNALIERO) {
            std::cout << ">>> ERRORE: Importo superiore al massimale di " 
                      << MASSIMALE_GIORNALIERO << " EUR!\n\n";
        }

    } while (importoBonifico <= 0.0 || importoBonifico > MASSIMALE_GIORNALIERO);

    // Se arriviamo qui, il dato e matematicamente garantito come valido
    std::cout << "\n==========================================" << "\n";
    std::cout << ">>> DISPOSIZIONE ACQUISITA CON SUCCESSO <<<" << "\n";
    std::cout << "Importo autorizzato : " << importoBonifico << " EUR\n";
    std::cout << "Commissione servizio: 1.00 EUR\n";
    std::cout << "Totale addebitato   : " << (importoBonifico + 1.00) << " EUR\n";
    std::cout << "==========================================" << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Controllo in Coda nello Stack)

Visualizziamo passo dopo passo come il processore esegue il corpo prima di arrivare alla guardia in fondo:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20importo%20%3D%200.0%3B%0A%20%20%20%20int%20passaggio%20%3D%200%3B%0A%0A%20%20%20%20do%20%7B%0A%20%20%20%20%20%20%20%20passaggio%2B%2B%3B%0A%20%20%20%20%20%20%20%20//%20Simuliamo%20l'inserimento%3A%20al%201%C2%B0%20giro%20dato%20errato%2C%20al%202%C2%B0%20valido%0A%20%20%20%20%20%20%20%20if%20%28passaggio%20%3D%3D%201%29%20importo%20%3D%20-20.0%3B%0A%20%20%20%20%20%20%20%20else%20importo%20%3D%20250.0%3B%0A%0A%20%20%20%20%7D%20while%20%28importo%20%3C%3D%200.0%20%7C%7C%20importo%20%3E%205000.0%29%3B%0A%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Importo%20valido%3A%20%22%20%3C%3C%20importo%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"**:
1. All'avvio, il cursore entra direttamente nel blocco `do` senza fermarsi a controllare alcuna guardia.
2. Alla riga del `while (importo <= 0.0 || importo > 5000.0)`:
   - Al primo passaggio, `importo` vale `-20.0`. La condizione di errore è `true`.
   - Il cursore **risale alla parola `do`** per eseguire nuovamente il corpo.
3. Al secondo passaggio, `importo` vale `250.0`. La condizione di errore diventa `false`.
4. Il cursore supera il punto e virgola ed esce definitivamente dal ciclo!

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Limite Massimo di 3 Tentativi di Inserimento:** Aggiungi un contatore `int tentativi = 0;`. Incrementalo a ogni giro. Se l'utente sbaglia per 3 volte consecutive, interrompi il ciclo e stampa: *"SESSIONE BLOCCATA: Raggiunto il limite massimo di errori per motivi di sicurezza."*.
2. **Ciclo di Vita con Menu ("Vuoi fare un'altra operazione?"):** Avvolgi l'intero programma all'interno di un ulteriore ciclo `do-while` esterno con una variabile `char risposta;`. Al termine di ogni bonifico chiedi: *"Vuoi disporre un altro bonifico? (S/N): "* e ripeti finché `risposta == 'S' || risposta == 's'`.

---

#### 5. MAKE (Crea: Il Capolavoro di Fine Blocco 1)

> 🏆 **La Sfida Finale del Blocco 1: Il Terminale Cassa Integrato**  
> Metti a frutto **tutto ciò che hai imparato nel Blocco 1** (variabili, costanti, operatore ternario, `if-else`, `switch`, `while` e `do-while`) creando il prototipo del software di cassa per un negozio al dettaglio.
> 
> Scrivi un programma C++ completo (`terminale_cassa_completo.cpp`):
> 
> 1. **Loop Principale (`do-while`):** Il programma mostra il menu principale e continua a funzionare finché l'operatore non sceglie l'opzione di chiusura cassa (`0`).
> 2. **Menu di Selezione (`switch-case`):**
>    - `Tasto 1 - Nuova Spesa Cliente:`
>      - Usa un ciclo `while` con sentinella `0.0` per battere i prezzi degli articoli nel carrello e calcolare il totale spesa.
>      - Con un `if-else if-else`, applica gli scaglioni di sconto fedeltà sul totale:
>        - Spesa < 50€: 0% sconto.
>        - Tra 50€ e 100€: 5% sconto.
>        - Oltre 100€: 10% sconto.
>      - Usa l'**operatore ternario (`?:`)** per verificare se regalare una shopper ecologica (`spesaScontata > 30.0 ? "Shopper Omaggio" : "Nessun omaggio"`).
>    - `Tasto 2 - Ricarica Carta Prepagata Punto Vendita:`
>      - Usa un `do-while` per validare l'importo della ricarica (deve essere compreso tra 5€ e 200€).
>    - `Tasto 0 - Chiusura Giornaliera di Cassa ed Uscita:`
>      - Stampa il messaggio di arrivederci e termina.
>    - `default:`
>      - Avvisa che il tasto premuto non è valido.
> 
> **Requisiti di qualità professionale:**
> - Intestazione Doxygen completa su file e `main`.
> - Commenti proporzionati `///` sulle regole di business e sulle costanti.
> - Codice ben indentato e suddiviso logicamente in sezioni.
## 🎯 Capitolo 11: Il Cruscotto del Programmatore (break, continue e Formattazione con <iomanip>)

> "La precisione nella presentazione dei numeri è l'abito formale con cui il software si presenta all'azienda."
> — *Principio dei Sistemi Contabili*

Hai conquistato tutti i costrutti fondamentali del linguaggio C++: variabili, decisioni e cicli. Prima di salire al livello successivo e iniziare a progettare programmi complessi suddivisi in funzioni (Blocco 2), ci mancano due strumenti indispensabili per rendere il tuo codice **flessibile, sicuro e professionale**:

1. **Il controllo chirurgico dei cicli (`break` e `continue`):** come interrompere un'elaborazione prima del tempo o come saltare un singolo passaggio difettoso senza fermare l'intero programma.
2. **La formattazione dell'output con `<iomanip>`:** come stampare numeri monetari con esattamente due cifre decimali (`19.50 EUR` invece del brutto `19.5`) e allineare scontrini e fatture in perfette tabelle contabili.

---

### 💡 Le Metafore: Il Nastro di Confezionamento e la Stampante Fiscale

> 💡 **Metafora:**  
> - **Il tasto `break` (Il Pulsante Rosso di Emergenza):**  
>   Sulla linea di confezionamento automatica delle merci scatta un allarme grave (es. sensore di sicurezza violato). L'operatore preme il pulsante a fungo: **tutto il nastro si ferma immediatamente** e il ciclo di produzione viene interrotto all'istante.
> - **Il tasto `continue` (Il Braccio di Scarto):**  
>   Lungo il nastro passa un pacco vuoto o un codice a barre illeggibile. Un braccio pneumatico lo spinge nel cestino degli scarti: la macchina non si blocca, **salta quel singolo pacco difettoso** e passa subito a lavorare il pacco successivo!
> - **I manipolatori di `<iomanip>` (La Stampante Fiscale Professionale):**  
>   Il terminale di cassa non stampa numeri alla rinfusa sul rotolo di carta: usa un righello tipografico per incolonnare le descrizioni a sinistra, gli importi a destra e stampare sempre i due zeri dei centesimi.

---

### ⚙️ Controllo Chirurgico: `break` vs `continue`

| Istruzione | Cosa fa | Dove atterra il cursore? | Esempio Gestionale |
| :--- | :--- | :--- | :--- |
| **`break;`** | **Esce forzatamente e definitivamente dal ciclo**, interrompendo qualsiasi iterazione futura. | Salta alla prima riga **dopo la graffa di chiusura `}`** del ciclo. | Arresto per frode: se una carta risulta rubata, blocca l'elaborazione. |
| **`continue;`** | **Interrompe solo il giro corrente**, ignorando le righe rimanenti del blocco. | Salta **in testa al ciclo** per iniziare subito l'iterazione successiva (nel `for` esegue prima l'aggiornamento contatore). | Transazione annullata: se l'importo è 0€, salta la stampa dello scontrino e passa al cliente successivo. |

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
while (Elementi da elaborare?) is (SI)
  :Leggi transazione;
  if (Errore Bloccante?) then (SI)
    :break;
    detach
  elseif (Transazione Annullata?) then (SI)
    :continue;
  else (NO: Valida)
    :Aggiorna bilancio;
    :Stampa ricevuta;
  endif
endwhile (NO)
:Report finale;
stop
@enduml
```

---

### 📐 Formattare l'Output Aziendale con `<iomanip>`

Di default, `std::cout` stampa i numeri decimali nel modo più compatto possibile:
- Il numero `19.50` viene stampato come `19.5` (perde lo zero finale!).
- La divisione `100.0 / 3.0` stampa `33.3333` (un disastro estetico per un bilancio contabile).

Includendo la libreria `<iomanip>` (*Input/Output Manipulators*) possiamo istruire il flusso di stampa:

```cpp
#include <iomanip>

// 1. FORZARE 2 CIFRE DECIMALI (Standard Valuta / Euro):
std::cout << std::fixed << std::setprecision(2);
// Da questo punto in poi: 19.5 diventa "19.50", e 33.3333 diventa "33.33"!

// 2. IMPOSTARE LA LARGHEZZA DI UNA COLONNA:
// std::setw(10) riserva uno spazio di esattamente 10 caratteri per la stampa successiva
std::cout << std::setw(10) << 45.50;

// 3. ALLINEAMENTO CONTABILE (Sinistra per testi, Destra per importi):
std::cout << std::left  << std::setw(20) << "Monitor 24 Pollici" 
          << std::right << std::setw(10) << 149.99 << " EUR\n";
```

> ⚠️ **Attenzione su `std::setw`:** Mentre `std::fixed` e `std::setprecision` restano attivi per tutte le stampe successive, **`std::setw` vale per una sola singola stampa** e va ripetuto per ogni colonna che desideri formattare!

---

### 🔬 Laboratorio PRIMM: Il Report Fiscale delle Vendite Giornaliere

Sviluppiamo un generatore di prospetti contabili tabellari per l'amministrazione aziendale.

#### 1. PREDICT (Prevedi)
? Osserva questo ciclo `for`. Quale sequenza numerica verrà stampata?
```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i << " ";
}
```
- [ ] `1 2 3 4 5 `
- [x] `1 3 `
- [ ] `1 2 3 `
- [ ] `3 `

<details>
<summary>💡 Spiegazione</summary>
Seguiamo il ciclo passo dopo passo:
1. <code>i = 1</code>: i due <code>if</code> sono falsi -> stampa <code>1 </code>.
2. <code>i = 2</code>: si attiva <code>continue;</code> -> il resto del corpo viene saltato e si passa subito a <code>i = 3</code> (non stampa nulla!).
3. <code>i = 3</code>: i due <code>if</code> sono falsi -> stampa <code>3 </code>.
4. <code>i = 4</code>: si attiva <code>break;</code> -> il ciclo viene <b>terminato all'istante</b> e il programma esce dal <code>for</code>.
Il risultato finale a video è esattamente <code>1 3 </code>!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `report_fiscale.cpp`. Nota come combina `continue` per saltare gli storni a importo zero, `break` per bloccare la cassa in caso di furto/anomalia, e i manipolatori di `<iomanip>` per generare una tabella contabile impeccabile:

```cpp
/**
 * @file report_fiscale.cpp
 * @brief Report vendite giornaliere con scarto transazioni e formattazione monetaria.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>
#include <iomanip>
#include <string>

/**
 * @brief Funzione principale: genera il prospetto contabile delle vendite.
 * @return int Codice di uscita (0 = esecuzione regolare).
 */
int main() {
    /// Incasso totale cumulato valido
    double totaleIncasso = 0.0;

    /// Numero di transazioni commerciali valide andate a buon fine
    int transazioniValide = 0;

    // Impostiamo una volta per tutte la precisione monetaria a 2 decimali
    std::cout << std::fixed << std::setprecision(2);

    std::cout << "========================================================" << "\n";
    std::cout << "        PROSPETTO FISCALE GIORNALIERO VENDITE          " << "\n";
    std::cout << "========================================================" << "\n";
    
    // Intestazione tabella allineata con larghezze fisse
    std::cout << std::left  << std::setw(6)  << "ID" 
              << std::left  << std::setw(28) << "Descrizione Prodotto" 
              << std::right << std::setw(12) << "Importo (EUR)" 
              << std::right << std::setw(10) << "Stato" << "\n";
    std::cout << "--------------------------------------------------------" << "\n";

    // Simulazione di una sequenza di 5 transazioni registrate
    for (int id = 1; id <= 5; ++id) {
        std::string descrizione;
        double importo = 0.0;

        // Dati simulati delle transazioni
        if (id == 1)      { descrizione = "Mouse Wireless Ottico";   importo = 19.50;  }
        else if (id == 2) { descrizione = "Storno Ordine Annullato"; importo = 0.00;   }
        else if (id == 3) { descrizione = "Tastiera Meccanica RGB";  importo = 59.90;  }
        else if (id == 4) { descrizione = "Toner Stampante Laser";   importo = 120.00; }
        else if (id == 5) { descrizione = "Allarme Blocco Fiscale";  importo = -999.0; }

        // 1. USO DI BREAK: Se c'e un codice di allarme critico, ferma tutto!
        if (importo == -999.0) {
            std::cout << ">>> ARRESTO D'EMERGENZA: Rilevata anomalia bloccante al n. " 
                      << id << " <<<\n";
            break;
        }

        // 2. USO DI CONTINUE: Se la transazione e uno storno nullo, scartala!
        if (importo == 0.0) {
            std::cout << std::left  << std::setw(6)  << id
                      << std::left  << std::setw(28) << descrizione
                      << std::right << std::setw(12) << importo
                      << std::right << std::setw(10) << "[SCARTATA]\n";
            continue; // Salta il resto del corpo e passa direttamente a id = 3!
        }

        // Se arriviamo qui, la transazione e valida: aggiorniamo i totali
        totaleIncasso += importo;
        transazioniValide++;

        // Stampa riga contabile con allineamento professionale
        std::cout << std::left  << std::setw(6)  << id
                  << std::left  << std::setw(28) << descrizione
                  << std::right << std::setw(12) << importo
                  << std::right << std::setw(10) << "[VALIDA]\n";
    }

    std::cout << "--------------------------------------------------------" << "\n";
    std::cout << std::left  << std::setw(34) << "TOTALE GENERALE INCASSATO:" 
              << std::right << std::setw(12) << totaleIncasso << " EUR\n";
    std::cout << "Transazioni valide registrate: " << transazioniValide << "\n";
    std::cout << "========================================================" << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Salti e Registri nello Stack)

Visualizziamo come `break` e `continue` deviano istantaneamente il flusso di esecuzione:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20totale%20%3D%200.0%3B%0A%0A%20%20%20%20for%20%28int%20i%20%3D%201%3B%20i%20%3C%3D%204%3B%20%2B%2Bi%29%20%7B%0A%20%20%20%20%20%20%20%20if%20%28i%20%3D%3D%202%29%20continue%3B%20//%20Scarta%20il%20giro%202%0A%20%20%20%20%20%20%20%20if%20%28i%20%3D%3D%204%29%20break%3B%20%20%20%20//%20Esce%20al%20giro%204%0A%20%20%20%20%20%20%20%20totale%20%2B%3D%2010.0%3B%0A%20%20%20%20%7D%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Totale%3A%20%22%20%3C%3C%20totale%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"**:
1. A `i = 2`, quando la freccia tocca `continue;`:
   - Guarda come la freccia **salta all'insù** tornando alla riga del `for`, incrementa `i` a `3` ed esegue il test, **senza mai toccare la riga `totale += 10.0;`**.
2. A `i = 4`, quando la freccia tocca `break;`:
   - Guarda come la freccia viene **proiettata in avanti fuori dal ciclo**, atterrando direttamente sulla riga `std::cout`, senza neppure aggiornare `i` a 5!

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Aggiungi la Colonna dell'IVA:** Nel programma `report_fiscale.cpp`, aggiungi una nuova colonna calcolata: `double impostaIva = importo * 0.22;`. Usa `std::setw(10)` per visualizzare l'importo dell'IVA accanto a quello della merce.
2. **Scarta Transazioni Sotto Soglia:** Modifica il controllo con `continue`: fai in modo che scarti tutte le transazioni con importo inferiore a `5.00€` (considerate micro-pagamenti non rilevanti per il report).
3. **Cosa succede senza `std::fixed`?** Prova a rimuovere `std::fixed` lasciando solo `std::setprecision(2);`. Noterai che il C++ interpreterà il 2 come numero totale di cifre significative (es. `120.00` verrà stampato come `1.2e+02` in notazione scientifica!). Questo ti dimostra perché `std::fixed` è obbligatorio in ambito economico.

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Prospetto di Liquidazione IVA Trimestrale**  
> L'ufficio contabile deve predisporre il prospetto trimestrale per la liquidazione periodica dell'IVA.
> 
> Scrivi un programma C++ autonomo (`liquidazione_iva.cpp`):
> - Utilizza un ciclo `for` per elaborare 6 fatture registrate nel trimestre (ID da 1 a 6).
> - Ogni fattura ha un imponibile netto e un codice aliquota (`char`):
>   - `'O'`: Ordinaria 22% (`0.22`).
>   - `'R'`: Ridotta 10% (`0.10`).
>   - `'M'`: Minima 4% (`0.04`).
>   - `'E'`: Esente IVA (`0.00`).
> - **Regola di Controllo Flusso:**
>   - Se l'imponibile di una fattura è `<= 0.0`, usa `continue;` per ignorarla stampando un avviso *"Fattura annullata"*.
>   - Se l'imponibile supera `50.000€`, scatta un alert antiriciclaggio che interrompe il ciclo con `break;`.
> - **Formattazione Contabile (`<iomanip>`):**
>   - Imposta `std::fixed` e `std::setprecision(2)`.
>   - Stampa una tabella a 4 colonne perfettamente allineate con `std::setw`:
>     `Fattura ID` | `Imponibile (EUR)` | `Aliq.` | `Imposta IVA (EUR)`
> - Al termine del ciclo, calcola e stampa:
>   - L'imponibile complessivo.
>   - Il totale dell'IVA a debito da versare all'Erario.
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti `///` proporzionati sulle aliquote fiscali.
> - Allineamenti contabili ordinati (testo a sinistra, numeri e valute a destra).
