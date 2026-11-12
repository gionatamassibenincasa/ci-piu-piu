## 🛠️ Capitolo 1: Prepara la tua Officina di Sviluppo

> "Uno strumento non fa il mestiere, ma senza gli strumenti giusti il mestiere diventa impossibile."
> — *Principio di officina*

Prima di scrivere anche una sola riga di C++, hai bisogno di un **ambiente di lavoro** funzionante.  
Pensa a questo capitolo come all’allestimento di un’officina: senza banco, utensili e luce non puoi riparare niente. Allo stesso modo, senza compilatore, editor e debugger non puoi costruire programmi.

Alla fine di questa lezione avrai sul tuo computer Windows:
- Visual Studio Code (l’editor)
- l’estensione C/C++
- il compilatore **g++** e il debugger **gdb** forniti da **MinGW-w64** tramite **MSYS2**
- la variabile d’ambiente PATH impostata correttamente
- un programma di prova compilato ed eseguito con successo

> 💡 **Metafora:**  
> - **VS Code** = il tuo banco di lavoro (dove scrivi e organizzi i pezzi)  
> - **Estensione C/C++** = le lampade e gli utensili specializzati per il C++  
> - **MSYS2 + MinGW-w64** = il magazzino di pezzi di ricambio e il banco prove (compilatore + debugger)  
> - **PATH** = l’etichetta che dice a Windows “i tuoi utensili sono in questo cassetto”

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Installare e verificare un ambiente C++ completo su Windows 10/11
- Compilare ed eseguire da terminale un programma minimo
- Aprire e far girare lo stesso programma da Visual Studio Code

---

### 📋 Checklist di lavoro (segui l’ordine)

Lavora con calma. Ogni passo ha un punto di controllo.  
Se un controllo fallisce, **non andare avanti**: risolvi prima.

#### Passo 1 — Installa Visual Studio Code
1. Vai su [https://code.visualstudio.com/](https://code.visualstudio.com/) e scarica la versione per Windows.
2. Esegui l’installer accettando le opzioni consigliate (in particolare “Aggiungi a PATH” se proposta).
3. Avvia VS Code almeno una volta.

**Controllo:** apri VS Code. Se vedi la schermata di benvenuto, il passo è ok.

#### Passo 2 — Installa l’estensione C/C++
1. In VS Code apri la vista Extensions (`Ctrl+Shift+X`).
2. Cerca `C++` e installa l’estensione ufficiale **C/C++** di Microsoft (`ms-vscode.cpptools`).
3. (Opzionale ma consigliato) Installa anche **C/C++ Extension Pack**.

**Controllo:** nell’elenco delle estensioni installate compare “C/C++”.

#### Passo 3 — Installa MSYS2
1. Scarica l’installer più recente da [https://www.msys2.org/](https://www.msys2.org/)  
   (oppure usa il link diretto presente nella documentazione ufficiale di VS Code).
2. Esegui l’installer. Lascia il percorso predefinito (`C:\msys64`) se non hai motivi particolari per cambiarlo.
3. Alla fine seleziona **Run MSYS2 now** e premi Finish. Si apre un terminale MSYS2.

**Controllo:** hai una finestra di terminale MSYS2 aperta.

#### Passo 4 — Installa la toolchain MinGW-w64 (ucrt)
Nel terminale MSYS2 digita **esattamente**:

```bash
pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
```

- Premi `Invio` per accettare il numero predefinito di pacchetti.
- Digita `Y` e premi `Invio` quando chiede conferma.
- Attendi la fine del download e dell’installazione (può richiedere alcuni minuti).

**Controllo:** il comando termina senza messaggi di errore in rosso.

#### Passo 5 — Aggiungi MinGW al PATH di Windows
1. Nella barra di ricerca di Windows digita **“Modifica le variabili di ambiente per l’account”** e aprilo.
2. Nella sezione **Variabili utente** seleziona `Path` → **Modifica**.
3. Premi **Nuovo** e aggiungi:
   ```
   C:\msys64\ucrt64\bin
   ```
   (Se hai installato MSYS2 in un percorso diverso, adatta di conseguenza).
4. Conferma con **OK** su tutte le finestre.
5. **Chiudi e riapri** qualsiasi Prompt dei comandi o PowerShell già aperti (il PATH viene letto all’avvio).

**Controllo:** apri un **nuovo** Prompt dei comandi e digita:

```bat
gcc --version
g++ --version
gdb --version
```

Devi vedere le versioni di gcc, g++ e gdb. Se compare “non riconosciuto come comando…” il PATH non è ancora corretto.

#### Passo 6 — Primo programma di prova da terminale
1. Crea una cartella di lavoro, ad esempio:
   ```bat
   mkdir %USERPROFILE%\progetti\prova_cpp
   cd %USERPROFILE%\progetti\prova_cpp
   ```
2. Crea un file `ridotto.cpp` con un editor di testo (o direttamente da VS Code) contenente:

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

3. Compila ed esegui dal Prompt dei comandi:

```bat
g++ ridotto.cpp -o ridotto.exe
ridotto.exe
```

**Controllo:** deve comparire la scritta `Ambiente C++ pronto!`.

#### Passo 7 — Stesso programma da Visual Studio Code
1. Dal Prompt dei comandi (sempre nella cartella del progetto):
   ```bat
   code .
   ```
2. Apri `ridotto.cpp`.
3. Premi il pulsante **Run** (o `F5` / play in alto a destra) e scegli **C/C++: g++.exe build and debug active file** quando richiesto.
4. La prima volta VS Code creerà i file di configurazione nella cartella `.vscode` (`tasks.json`, ecc.).

**Controllo:** nel Terminale integrato di VS Code compare di nuovo `Ambiente C++ pronto!`.

---

### 🔬 Cosa abbiamo appena costruito?

| Componente              | Ruolo nella “officina”                          | Comando / verifica tipica      |
|-------------------------|--------------------------------------------------|--------------------------------|
| VS Code                 | Banco di lavoro e organizzazione file           | `code .`                       |
| Estensione C/C++        | IntelliSense, build e debug integrati           | Extensions view                |
| MSYS2                   | Gestore di pacchetti e ambiente Unix-like       | Terminale MSYS2                |
| MinGW-w64 (ucrt64)      | Compilatore `g++` + debugger `gdb`              | `g++ --version`                |
| Variabile PATH          | Dice a Windows dove trovare gli utensili        | `where g++`                    |
| `ridotto.cpp`           | Primo pezzo prodotto e collaudato               | `g++ ridotto.cpp -o ridotto.exe` |

> 🔗 Documentazione ufficiale di riferimento:  
> [Using GCC with MinGW – Visual Studio Code](https://code.visualstudio.com/docs/cpp/config-mingw)

---

### 📝 Riepilogo tascabile
- Senza compilatore non esiste programma eseguibile.
- MSYS2 + MinGW-w64 è il modo consigliato da Microsoft per avere `g++` e `gdb` aggiornati su Windows.
- Il PATH deve contenere `C:\msys64\ucrt64\bin` (o il percorso equivalente).
- Verifica sempre con `g++ --version` **in un nuovo** terminale.
- Il programma `ridotto.cpp` è il tuo “banco di prova”: se compila e stampa, l’officina è pronta.

---

### ⚠️ Problemi frequenti e soluzioni rapide

| Sintomo                                      | Causa più probabile                     | Cosa fare                                      |
|----------------------------------------------|-----------------------------------------|------------------------------------------------|
| `g++` non è riconosciuto                     | PATH non aggiornato o terminale vecchio | Chiudi e riapri il Prompt; controlla il Path   |
| `pacman` non trova i pacchetti               | Connessione o mirror MSYS2              | Riprova più tardi o aggiorna con `pacman -Syu` |
| VS Code non trova il compilatore             | Estensione C/C++ non installata o PATH  | Reinstalla l’estensione e riavvia VS Code      |
| Messaggio su `miDebuggerPath`                | manca il pacchetto gdb                  | Reinstalla il gruppo toolchain da MSYS2        |

---

### ➡️ Prossimo chunk
Ora che l’officina è allestita, possiamo finalmente aprire il cofano e capire **come** il codice sorgente diventa un programma eseguibile (pre-processore, compilatore, linker).  
Nel prossimo capitolo entreremo nella “fabbrica del codice”.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [ ] Un solo obiettivo principale: ambiente funzionante
  [ ] Metafora officina / banco di lavoro
  [ ] Checklist sequenziale con punti di controllo (chunking)
  [ ] Nessun costrutto C++ avanzato (solo il minimo per il test)
  [ ] Link alla documentazione ufficiale VS Code
  [ ] Pronto per essere inserito dopo 00_guida_allo_studio
-->
