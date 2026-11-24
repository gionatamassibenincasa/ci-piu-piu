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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/00_guida-studio-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/02_motore-compilazione-01.md)

---


## 🛠️ Prepara la tua Officina di Sviluppo: VS Code, MSYS2 e MinGW-w64

> "I programmi sono fatti per essere letti dagli esseri umani e solo incidentalmente per essere eseguiti dai computer."
> -- Donald Knuth

Questo non è un capitolo da leggere in 20 minuti.  
È una **sessione di laboratorio**: allestire l’officina richiede tempo, pazienza e qualche tentativo. In classe può occupare un’ora intera (o più, se qualcuno ha imprevisti). Non correre.

Alla fine di questa sessione avrai:

- Visual Studio Code configurato come banco di lavoro;
- l'estensione C/C++ installata e riconosciuta;
- il compilatore **g++** e il debugger **gdb** disponibili nel PATH;
- un programma minimo compilato, eseguito e fermato su un breakpoint.

> 💡 **Metafora:**  
>
> - **VS Code** = il tuo banco di lavoro (dove organizzi i pezzi e lavori)  
> - **Estensione C/C++** = le lampade e gli utensili specifici per il C++  
> - **MSYS2 + MinGW-w64** = il magazzino di pezzi di ricambio e il banco prove  
> - **PATH** = l’etichetta che dice a Windows “i tuoi utensili sono in *questo* cassetto”  
> - **Compilatore (g++)** = l’operaio che traduce il progetto in un pezzo finito (l’eseguibile)  
> - **Debugger (gdb)** = il tecnico che ti fa vedere cosa succede *dentro* il pezzo mentre funziona

---

**In questa sessione non** studiamo ancora la sintassi dei costrutti C++, la
catena di compilazione né la correzione degli algoritmi. Il risultato è avere
un ambiente verificato e un flusso di lavoro pronto per il laboratorio.

---

### 🎯 Obiettivi di questa sessione

Alla fine sei in grado di:

- installare e verificare VS Code, MSYS2, MinGW-w64, `g++` e `gdb`;
- configurare il PATH di Windows e leggere gli errori quando il terminale non trova un comando;
- compilare ed eseguire `prova.cpp` da terminale;
- avviare il debug in VS Code e fermare il programma su un breakpoint.

---

### ⚠️ Prima di iniziare — casi particolari

**Se sei in laboratorio a scuola** e i computer hanno già VS Code + MinGW installati:  
salta i passi di installazione e vai direttamente al **Passo 6** (programma di prova). Chiedi al docente il percorso corretto se `g++` non viene riconosciuto.

**Se a casa non hai diritti di amministratore** o l’antivirus / le policy bloccano l’installazione:

1. Prova comunque i passi (molte operazioni non richiedono admin).
2. Se fallisci, usa temporaneamente un compilatore online (es. [Online CPPC](https://www.online-cpp.com/) o [Online GDB](https://www.onlinegdb.com/)) per seguire le lezioni successive.
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

Crea il file `prova.cpp` nella cartella del corso (`Documenti\Cpp-3SIA`) con questo contenuto:

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
- [ ] Questa è una **sessione di laboratorio**, non una lettura veloce.
- [ ] Senza compilatore non esiste programma eseguibile.
- [ ] Il PATH contiene `C:\msys64\ucrt64\bin` e va verificato in un **nuovo** terminale.
- [ ] `g++` traduce il codice sorgente in eseguibile; `gdb` permette il debug.
- [ ] `prova.cpp` compila, stampa il messaggio atteso e si ferma su un breakpoint.
- [ ] Il terminale resta utile anche quando VS Code o l'estensione non trovano il toolchain.

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

### ➡️ Prossimo passo nel percorso

Ora che l'officina è allestita e collaudata, nel prossimo capitolo del
percorso Fondamenti, `02_il_motore_sotto_il_cofano`, seguirai la trasformazione
da sorgente C++ a eseguibile: pre-elaborazione, compilazione, assemblaggio e
linking.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/00_guida-studio-01.md">Lezione precedente (0 — Guida allo Studio: come imparare a programmare)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/02_motore-compilazione-01.md">Lezione successiva (2 — Il motore sotto il cofano: dalla sorgente all'eseguibile)</a>
