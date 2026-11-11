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

> "Non si può insegnare niente a un uomo; si può solo aiutarlo a scoprire ciò che ha dentro di sé."
> — *Galileo Galilei*

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
## ⚙️ Il Motore Sotto il Cofano

> "La programmazione è l'arte di esprimere soluzioni ai problemi in modo che un computer possa eseguirle. Spesso un problema viene compreso appieno solo attraverso il processo di programmazione di una soluzione."
> — *Bjarne Stroustrup*

Sviluppare un programma non è "scrivere codice a caso sperando che funzioni". È un processo ingegneristico composto da 4 fasi:
1. **Analisi**: Qual è il problema? Cosa vuole l'utente?
2. **Progettazione**: Qual è la struttura? Come comunicano le parti?
3. **Programmazione**: Scrivere il codice rispettando i vincoli (tempo, spazio, affidabilità).
4. **Test**: Provare sistematicamente che tutto funzioni in ogni circostanza.

### 🇨🇭 Perché proprio il C++?
- **Espressivo**: Ti permette di tradurre le tue idee in codice in modo diretto.
- **Onnipresente**: È uno standard disponibile su quasi tutti i computer e dispositivi.
- **Formativo**: I concetti che impari qui (memoria, tipi, controllo) sono le fondamenta per *qualsiasi* altro linguaggio futuro.

---

### 🏭 La Fabbrica del Codice: La Compilazione

Il C++ è un linguaggio **compilato**. Il computer non capisce il C++ direttamente; capisce solo istruzioni macchina (zeri e uni). Dobbiamo quindi tradurre il nostro codice. Immagina una catena di montaggio in 4 passaggi:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

rectangle "Codice Sorgente\n(human readable)" as Source {
  [main.cpp]
}

rectangle "Pre-elaboratore\n(Preprocessor)" as Pre {
  note right: Espande gli #include\nRimuove i commenti
}

rectangle "Compilatore\n(Compiler)" as Comp {
  note right: Traduce in Assembly\n(controlla la sintassi!)
}

rectangle "Assemblatore\n(Assembler)" as Asm {
  note right: Traduce in Codice\nMacchina (file .o)
}

rectangle "Linker\n(Linker)" as Link {
  note right: Unisce i file .o\ne le librerie esterne
}

rectangle "Eseguibile\n(machine code)" as Exe {
  [a.out / main.exe]
}

Source --> Pre : 1. cpp
Pre --> Comp : 2. codice pulito
Comp --> Asm : 3. codice assembly (.s)
Asm --> Link : 4. file oggetto (.o)
Link --> Exe : 5. eseguibile finale
@enduml
```
*💡 Brain Friendly Tip: Il compilatore è un controllore pedante, non un indovino. Se dimentichi un punto e virgola, lui si ferma e ti fa la multa (errore di compilazione), non cerca di "indovinare" cosa volevi dire!*

---

### 🔬 PRIMM: Il Programma Più Piccolo Possibile

Il nostro obiettivo ora non è fare qualcosa di utile, ma **sperimentare la catena di montaggio**. Vogliamo vedere con i nostri occhi gli artefatti intermedi.

#### 1. PREDICT (Prevedi)
? Guarda questo codice. Secondo te, cosa succederà se proviamo a compilarlo ed eseguirlo?
- [ ] Darà un errore perché manca `#include <iostream>`
- [x] Si compilerà silenziosamente e non stamperà nulla a video
- [ ] Stamperà "Hello World" automaticamente

```cpp
// file: ridotto.cpp
int main() {}
```
<details>
<summary>🔍 Clicca per la spiegazione</summary>
Ogni programma C++ deve avere <b>esattamente una</b> funzione globale chiamata <code>main</code>. È il punto di ingresso. Le parentesi <code>{}</code> racchiudono il corpo della funzione. Essendo vuoto, non fa nulla e termina immediatamente, restituendo implicitamente 0 al sistema operativo (successo).
</details>

#### 2. RUN (Esegui)
Copia e incolla questi comandi nel tuo terminale (o nell'ambiente di sviluppo). Stiamo chiedendo al compilatore (`g++`) di **salvare le tappe intermedie** (`-save-temps`) invece di cancellarle.

```bash
# 1. Compila salvando i file temporanei
g++ -save-temps -fverbose-asm -O0 ridotto.cpp -o ridotto

# 2. Lista i file generati
ls
```
**Output atteso:**
```text
ridotto  ridotto.cpp  ridotto.ii  ridotto.o  ridotto.s
```

#### 3. INVESTIGATE (Investiga)
Osserviamo cosa ha prodotto la "fabbrica".

? Quale di questi file contiene il codice dopo che il **Pre-elaboratore** ha rimosso i commenti e espanso le direttive?
- [ ] `ridotto.o`
- [x] `ridotto.ii`
- [ ] `ridotto.s`

Se esegui `cat ridotto.ii`, vedrai il tuo codice originale, ma con l'aggiunta di alcune righe di sistema (le "dichiarazioni d'obbligo" del compilatore).
Se esegui `cat ridotto.s`, vedrai il linguaggio **Assembly**, il ponte tra il C++ leggibile e il codice macchina. Noterai istruzioni come `pushq %rbp` e `movl $0, %eax` (che significa proprio "prepara il valore di ritorno 0").

#### 4. MODIFY (Modifica)
Modifichiamo il nostro programma minimo per vedere come cambia la catena di montaggio.

1. Apri `ridotto.cpp`.
2. Cambia il codice in:
   ```cpp
   int main() {
       return 42;
   }
   ```
3. Ricompila con lo stesso comando: `g++ -save-temps -O0 ridotto.cpp -o ridotto`
4. Esegui `cat ridotto.s` e cerca la riga che contiene `movl`.

? Cosa è cambiato nell'istruzione Assembly rispetto a prima?
- [ ] È scomparsa l'istruzione `movl`
- [x] Il valore è cambiato da `$0` a `$42`
- [ ] Il file `.s` è diventato molto più grande

<details>
<summary>💡 Perché è importante?</summary>
Hai appena visto con i tuoi occhi come un'istruzione C++ ad alto livello (<code>return 42;</code>) si traduce in una specifica istruzione macchina (<code>movl $42, %eax</code>). Il compilatore non fa magia, fa traduzione!
</details>

#### 5. MAKE (Crea)
Ora tocca a te. Crea un nuovo file chiamato `saluto.cpp`.
1. Scrivi il programma minimo `int main() {}`.
2. Aggiungi una riga per stampare "Ciao, Mondo!" usando `#include <iostream>` e `std::cout`. *(Suggerimento: guarda l'esempio qui sotto se sei bloccato)*.
3. Compilalo ed eseguilo.

```cpp
// Esempio di riferimento (non copiare subito, prova prima tu!)
#include <iostream>

int main() {
    // Stampa "Ciao, Mondo!" e va a capo con \n
    std::cout << "Ciao, Mondo!\n";
    return 0; // 0 = successo per il sistema operativo
}
```
@LIA.cpp

---
### 📝 Riepilogo "Tascabile"
- Un programma C++ parte **sempre** dalla funzione `int main()`.
- Il valore `return 0;` dice al sistema operativo: "Tutto ok, nessuna errore".
- La compilazione ha 4 fasi: **Pre-processing** → **Compiling** → **Assembling** → **Linking**.
- Il codice è scritto per **due lettori**: il computer (che lo esegue) e l'essere umano (che lo deve leggere e mantenere). Usa i commenti `//` per parlare con l'umano!

> **Sfida per la prossima volta:** Cosa succede se dimentichiamo il punto e virgola `;` dopo `std::cout << "Ciao"`? Provaci e porta l'errore in classe!
## 💬 Capitolo 2: Il Primo Dialogo con la Macchina

> "S'impara a programmare scrivendo programmi."
> — *Brian Kernighan*

Un *linguaggio di programmazione* è come un linguaggio straniero con una grammatica rigidissima e un vocabolario preciso, progettato per dare istruzioni a un computer. Ma ricorda una regola d'oro:

> 💡 **Metafora:** Scrivere codice è come scrivere una ricetta di cucina. 
> - Il **computer** è lo chef che la esegue alla lettera (se dimentichi "aggiungi un pizzico di sale", lui non lo indovina, si blocca!). 
> - L'**essere umano** è l'altro lettore: deve poter capire, modificare e mantenere la ricetta in futuro. Per questo usiamo i commenti e un codice ordinato.

---

### 🔬 PRIMM: Il Programma "Ciao, Mondo!"

#### 1. PREDICT (Prevedi)
? Prima di eseguire il codice qui sotto, osserva la riga `std::cout << "Ciao, Mondo!\n";`. Cosa pensi che faccia il simbolo `\n` alla fine della frase?
- [ ] Stampa esattamente i caratteri "\n" a video
- [x] Va a capo, spostando il cursore alla riga successiva
- [ ] Cancella tutto quello che è stato stampato prima

#### 2. RUN (Esegui)
Clicca sul pulsante "Run" qui sotto per vedere il codice in azione direttamente nel tuo browser.

```cpp
/**
 * @file ciao_mondo.cpp
 * @brief Il primo programma in C++ che stampa un messaggio a video.
 * @author Gionata Massi
 * @date 2024-10-10
 */
#include <iostream>

/**
 * @brief Punto di ingresso del programma.
 * @return int Codice di uscita (0 = successo).
 */
int main() {
    /// Stampa il messaggio di saluto e va a capo
    std::cout << "Ciao, Mondo!\n";
    
    return 0; /// 0 indica al sistema operativo che tutto è andato bene
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga: Analisi Linea per Linea)
Analizziamo il codice come se fossimo detective. Ogni riga ha un ruolo preciso:

| Codice | Spiegazione "Brain-Friendly" |
| :--- | :--- |
| `#include <iostream>` | **Il Pre-elaboratore** legge questa riga e "incolla" nel tuo codice tutte le istruzioni necessarie per gestire l'Input/Output (come `cout`). Senza di essa, il compilatore non sa cosa sia `cout`. |
| `int main() {` | Il **punto di partenza**. Ogni programma C++ deve avere *esattamente una* funzione chiamata `main`. L'esecuzione inizia sempre da qui. La `{` apre il blocco di istruzioni. |
| `std::cout << ...` | `cout` (si pronuncia *"si-out"*, abbreviazione di *Character Output Stream*) è il "megafono" del programma. `std::` è lo **spazio dei nomi** (namespace): dice al compilatore "cerca `cout` nella libreria standard". L'operatore `<<` è detto *"poni in"* (insertion operator) e spinge il testo verso il megafono. |
| `"Ciao, Mondo!\n"` | È un **letterale stringa** (testo tra doppi apici). `\n` è un carattere speciale di *escape* che significa "newline" (vai a capo). |
| `return 0;` | La funzione `main` restituisce un numero intero (`int`) al sistema operativo. `0` è la convenzione universale per dire: "Esecuzione completata con successo, nessun errore". |
| `}` | Chiude il blocco della funzione `main`. |
| `/// ...` o `// ...` | **Commenti**. Tutto ciò che segue `//` è ignorato dal compilatore. Serve *solo* agli esseri umani per capire il codice. |

#### 4. MODIFY (Modifica: Fallimento Produttivo)
Il miglior modo per imparare è vedere cosa succede quando le regole vengono infrante. Il compilatore non è cattivo, è solo un controllore molto pignolo.

**Sfida 1: Il punto e virgola dimenticato**
1. Copia il codice qui sopra in un file locale o nell'editor.
2. Rimuovi il punto e virgola `;` alla fine della riga `std::cout << "Ciao, Mondo!\n"`.
3. Prova a compilare.

? Quale tipo di errore ti aspetti dal compilatore?
- [ ] Un errore a runtime (il programma si chiude da solo)
- [x] Un errore di sintassi (il compilatore si rifiuta di creare l'eseguibile)
- [ ] Nessun errore, il compilatore lo aggiunge da solo

<details>
<summary>🔍 Clicca per vedere l'errore tipico del compilatore</summary>
Il compilatore ti dirà qualcosa come: <code>error: expected ';' before 'return'</code>. 
<strong>Lezione imparata:</strong> Il compilatore legge il codice riga per riga. Se manca il `;`, lui pensa che l'istruzione continui alla riga dopo, si confonde e si ferma.
</details>

**Sfida 2: Dimenticare lo spazio dei nomi**
1. Ripristina il `;`.
2. Cambia `std::cout` in solo `cout` (rimuovi `std::`).
3. Compila.

? Cosa succede?
- [ ] Funziona lo stesso
- [x] Errore: "'cout' was not declared in this scope"
- [ ] Il programma stampa uno spazio vuoto

<details>
<summary>🔍 Perché succede?</summary>
Senza <code>std::</code>, il compilatore cerca una funzione chiamata <code>cout</code> nel tuo codice, non la trova, e si arrende. (In futuro vedremo che esiste un'istruzione <code>using namespace std;</code> per evitare di scriverlo sempre, ma per ora è meglio essere espliciti!).
</details>

#### 5. MAKE (Crea)
Ora tocca a te. Non copiare e incollare: scrivi il codice da zero.

**Obiettivo:** Crea un programma chiamato `presentazione.cpp` che:
1. Include la libreria corretta.
2. Ha una funzione `main` correttamente formattata.
3. Stampa a video **tre righe separate** usando più istruzioni `std::cout`:
   - La prima riga deve contenere il tuo nome.
   - La seconda riga deve contenere la tua classe (es. "3A SIA").
   - La terza riga deve contenere una tua passione o hobby.
4. Utilizza i commenti Doxygen (`/** ... */` e `///`) per documentare il file e le righe di codice.
5. Restituisce `0` alla fine.

<details>
<summary>💡 Suggerimento (Scaffold)</summary>
Ecco lo scheletro da completare. Non guardare subito la soluzione completa, prova a riempire i puntini!
<br><br>
<code>
/**
 * @brief Programma di presentazione personale.
 */
#include &lt;iostream&gt;

int main() {
    /// Stampa il nome
    std::cout &lt;&lt; "....................\n";
    
    /// Stampa la classe
    std::cout &lt;&lt; "....................\n";
    
    /// Stampa l'hobby
    std::cout &lt;&lt; "....................\n";
    
    return 0;
}
</code>
</details>

---
### 📝 Riepilogo "Tascabile"
- Un programma C++ si legge in due direzioni: dal **compilatore** (che cerca errori di sintassi) e dall'**umano** (che cerca logica e chiarezza).
- `#include <iostream>` è il passaporto per usare l'input/output.
- `std::cout <<` è l'operatore per scrivere sullo schermo.
- `\n` dentro una stringa forza l'andata a capo.
- `return 0;` alla fine di `main` è il sigillo di "successo" per il sistema operativo.
- **I commenti (`//`) sono il tuo miglior amico per il futuro te stesso.**

> **🚀 Sfida per la prossima volta:** Come faresti a chiedere al computer di *ascoltare* invece che solo *parlare*? (Spoiler: ci serve un nuovo operatore e una nuova "scatola" per salvare i dati. Ne parleremo nel prossimo capitolo!)
## 📦 Capitolo 3: Gli Sportelli della Memoria (Variabili, Costanti e Tipi)

> "La memoria è lo spazio in cui i dati attendono il loro turno per essere trasformati in valore."
> — *Principio dei Sistemi Informativi*

Nei programmi precedenti abbiamo stampato a schermo testi fissi. Ma un vero software gestionale deve poter **memorizzare, ricordare e aggiornare dati che cambiano nel tempo**: il prezzo di un articolo, il saldo di un conto, la quantità di merci in magazzino.

Per fare questo usiamo le **variabili** e le **costanti**.

---

### 💡 La Metafora: Il "Locker" di E-Commerce

Immagina la memoria del computer (la RAM) come una gigantesca parete di **Locker automatici** per il ritiro dei pacchi (come i punti di ritiro Amazon o InPost):

> 💡 **Metafora:**  
> - **La parete dei Locker** è la memoria **RAM**.
> - **Il numero stampato sullo sportello** è l'**indirizzo di memoria** (es. `0x7ffee4`). Per il computer è una coordinata numerica esatta.
> - **L'etichetta sull'App** è il **nome della variabile** (es. `prezzo`, `quantita`). È il nome comodo che usi tu programmatore per non dover memorizzare indirizzi incomprensibili.
> - **La dimensione dello sportello** è il **tipo di dato**: uno scomparto piccolo basta per una busta sottile; uno scomparto medio serve per delle scarpe; un vano grande serve per uno schermo.
> - **La merce nel pacco** è il **valore** memorizzato all'interno.
> - **Uno sportello blindato e sigillato** è una **costante (`const`)**: una volta inserita la merce all'inizio, nessuno può più sostituirla!

---

### 🗄️ I Tipi di Dato Fondamentali in C++

Prima di aprire uno sportello in memoria, dobbiamo dire al compilatore **che tipo di merce conterrà**, così che possa riservare lo spazio esatto:

| Tipo C++ | Cosa contiene | Esempio nel contesto SIA | Dimensione tipica |
| :--- | :--- | :--- | :--- |
| `int` | Numeri interi (positivi o negativi, senza virgola) | `int giacenza = 15;` (pezzi a magazzino) | 4 byte |
| `double` | Numeri decimali (a virgola mobile, doppia precisione) | `double prezzo = 149.99;` (prezzo in euro) | 8 byte |
| `char` | Un **singolo carattere** (racchiuso tra apici singoli `' '`) | `char reparto = 'E';` (reparto Elettronica) | 1 byte |
| `bool` | Valore logico di verità: solo `true` oppure `false` | `bool disponibile = true;` (prodotto a catalogo) | 1 byte |
| `std::string` | Testo alfanumerico (racchiuso tra virgolette doppie `" "`) | `std::string nome = "Monitor 24";` | Variabile (richiede `<string>`) |

> ⚠️ **Regola d'oro del compilatore:** Un tipo non può contenere dati incompatibili. Se provi a forzare un numero con la virgola (`19.99`) dentro uno sportello `int`, il compilatore troncherà la parte decimale senza pietà, tenendo solo `19`!

---

### 🔬 Laboratorio PRIMM: La Scheda Prodotto di Magazzino

Mettiamo subito in pratica questi concetti realizzando il modulo anagrafico di un articolo gestionale.

#### 1. PREDICT (Prevedi)
? Osserva il seguente frammento di codice. Quale sarà l'output a schermo della variabile `pezziDisponibili`?
```cpp
int pezziDisponibili = 7.85;
std::cout << pezziDisponibili;
```
- [ ] Stampa `7.85`
- [x] Stampa `7` (la parte decimale viene troncata)
- [ ] Il programma va in crash immediato
- [ ] Stampa `8` per arrotondamento

<details>
<summary>💡 Spiegazione</summary>
In C++, la variabile di tipo <code>int</code> è progettata per contenere <b>esclusivamente numeri interi</b>. Se le assegni un valore con la virgola come <code>7.85</code>, il C++ non arrotonda al più vicino: <b>elimina direttamente tutti i decimali</b> (troncamento). Per memorizzare correttamente i centesimi è obbligatorio usare <code>double</code>.
</details>

---

#### 2. RUN (Esegui)
Esamina il programma completo qui sotto. Nota i commenti strutturati in standard **Doxygen** (`/** ... */` per l'intestazione e `///` per descrivere le singole variabili).

Clicca su **"Run"** per compilarlo ed eseguirlo nel browser:

```cpp
/**
 * @file scheda_prodotto.cpp
 * @brief Gestione anagrafica di un articolo di magazzino aziendale.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>
#include <string>

/**
 * @brief Funzione principale: memorizza e stampa i dati del prodotto.
 * @return int Codice di stato (0 = esecuzione corretta).
 */
int main() {
    /// Costante: aliquota IVA ordinaria al 22% (non modificabile)
    const double ALIQUOTA_IVA = 0.22;

    /// Denominazione commerciale dell'articolo
    std::string nomeArticolo = "Mouse Wireless Ottico";

    /// Reparto aziendale di appartenenza ('A' = Accessori, 'H' = Hardware)
    char codiceReparto = 'A';

    /// Quantità fisica presente sugli scaffali di magazzino
    int pezziInMagazzino = 42;

    /// Prezzo unitario di vendita al netto dell'IVA
    double prezzoNetto = 19.50;

    /// Flag booleano: true se il prodotto è coperto da garanzia estesa
    bool haGaranziaEstesa = true;

    // Visualizzazione dei dati del prodotto
    std::cout << "=== SCHEDA ARTICOLO MAGAZZINO ===" << "\n";
    std::cout << "Descrizione : " << nomeArticolo << "\n";
    std::cout << "Reparto     : " << codiceReparto << "\n";
    std::cout << "Giacenza    : " << pezziInMagazzino << " pezzi" << "\n";
    std::cout << "Prezzo netto: " << prezzoNetto << " EUR" << "\n";
    std::cout << "Aliquota IVA: " << (ALIQUOTA_IVA * 100) << "%" << "\n";
    std::cout << "Garanzia est: " << (haGaranziaEstesa ? "Si" : "No") << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: La Memoria Passo Passo)

Ora andiamo a vedere cosa succede realmente all'interno della memoria RAM del computer.

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%23include%20%3Cstring%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20const%20double%20ALIQUOTA_IVA%20%3D%200.22%3B%0A%20%20%20%20std%3A%3Astring%20nomeArticolo%20%3D%20%22Mouse%20Wireless%22%3B%0A%20%20%20%20char%20codiceReparto%20%3D%20'A'%3B%0A%20%20%20%20int%20pezziInMagazzino%20%3D%2042%3B%0A%20%20%20%20double%20prezzoNetto%20%3D%2019.50%3B%0A%20%20%20%20bool%20haGaranziaEstesa%20%3D%20true%3B%0A%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20nomeArticolo%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi il tasto **"Next"** un'istruzione alla volta. Osserva attentamente il riquadro **Frames (Stack)** sulla destra:
1. All'inizio dell'esecuzione di `main()`, lo stack riserva uno spazio ordinato per ogni variabile.
2. Man mano che la freccia verde avanza, ogni sportello del "locker" viene riempito con il valore assegnato.
3. Nota la differenza visiva tra una variabile numerica semplice (`int`, `double`) e un oggetto testuale come `std::string`.

> ⚠️ **Attenzione al "Locker con Spazzatura": l'Inizializzazione Obbligatoria!**  
> In C++, se scrivi semplicemente `int quantita;` senza assegnarle un valore iniziale, lo sportello **non è vuoto né azzerato**: contiene i residui binari casuali (detti *garbage values*) lasciati dai programmi eseguiti in precedenza!  
> **Buona pratica aziendale:** Inizializza sempre ogni variabile al momento della creazione (es. `int quantita = 0;` oppure `int quantita{0};`).

#### 🕳️ La Trappola Classica del C++: `std::cin` e le Stringhe con Spazi
Quando permetterai all'utente di digitare dati da tastiera, la tentazione immediata sarà usare `std::cin >> variabile;`.  
Per numeri (`int`, `double`) o singole parole va benissimo. Ma cosa accade se provi a leggere la descrizione di un articolo aziendale come `"Monitor 24 Pollici"`?

```cpp
std::string descrizione;
std::cout << "Inserisci descrizione: ";
std::cin >> descrizione; // ⚠️ TRAPPOLA IN AGGUATO!
```

> 💥 **Cosa si rompe:**  
> L'operatore `>>` considera lo spazio bianco come un separatore di fine lettura.  
> Risultato: `descrizione` conterrà **solo** `"Monitor"`, mentre `"24"` e `"Pollici"` resteranno incastrati nel "tubo" di input (il buffer di tastiera).  
> Quando il programma tenterà la lettura successiva (es. la quantità di pezzi o il prezzo), leggerà `"24"` al posto del numero atteso, mandando completamente in tilt la logica del programma!

> 🛡️ **Il Rito di Passaggio: La Soluzione `std::getline`**  
> Per leggere un'intera riga di testo con spazi fino a quando l'utente non preme il tasto Invio, usa sempre:
> ```cpp
> std::getline(std::cin, descrizione);
> ```
> Questo comando cattura tutta la riga (spazi inclusi) e la deposita in modo sicuro nel locker della stringa.

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

Ora mettiti alla prova modificando il codice precedente:

1. **Il calcolo dell'IVA:** Dichiara una nuova variabile `double importoIva;` e calcolala moltiplicando `prezzoNetto * ALIQUOTA_IVA`. Poi stampa a video il prezzo totale al lordo dell'IVA.
2. **La prova del lucchetto:** Prova ad aggiungere a metà programma la riga `ALIQUOTA_IVA = 0.10;`. Cosa dice il compilatore?  
   <details>
   <summary>💡 Mostra l'errore del compilatore</summary>
   Il compilatore si rifiuterà categoricamente di creare il programma, segnalando un errore del tipo:  
   <code>error: assignment of read-only variable 'ALIQUOTA_IVA'</code>.  
   Questo ti dimostra che una variabile marcata con <code>const</code> è blindata contro modifiche accidentali!
   </details>
3. **Inizializzazione uniforme (C++ Moderno):** Prova a inizializzare le variabili usando le parentesi graffe invece dell'uguale: `int scorte{100};`. Questa sintassi è consigliata dagli standard moderni perché protegge dai cambi di tipo involontari.
4. **La prova pratica della trappola (`cin` vs `getline`):** Aggiungi in testa a `main` la richiesta di digitare il nome del prodotto. Prova prima con `std::cin >> nomeArticolo;` inserendo `"Tastiera Meccanica RGB"` e osserva come lo scontrino tronchi il nome. Sostituiscilo poi con `std::getline(std::cin, nomeArticolo);` e verifica che l'intera frase venga conservata!

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: La Scheda Conto Corrente Aziendale**  
> Scrivi un nuovo programma C++ autonomo (`conto_corrente.cpp`) che rappresenti la situazione contabile del conto aziendale presso la banca d'affari.
> 
> Il programma deve memorizzare e visualizzare:
> - `std::string denominazioneBanca`: nome dell'istituto di credito.
> - `std::string codiceIban`: codice IBAN del conto (27 caratteri).
> - `double saldoContabile`: saldo monetario attuale (es. `12450.75`).
> - `const double TASSO_INTERESSE`: costante con il tasso annuo attivo (es. `0.015`, pari all'1.5%).
> - `bool fidoConcesso`: indica se la banca ha accordato una linea di fido aziendale (`true`/`false`).
> - `char classeRating`: lettera di rating creditizio dell'azienda (es. `'A'`).
> 
> **Requisiti di qualità:**
> - Inserisci l'intestazione Doxygen per il file e per la funzione `main`.
> - Commenta ogni variabile con `///`.
> - Calcola e visualizza la stima degli interessi maturati a fine anno moltiplicando `saldoContabile * TASSO_INTERESSE`.
## 🧮 Capitolo 4: La Calcolatrice Fiscale (Espressioni, Operatori e Operatore Ternario)

> "I computer non sono intelligenti: sono solo calcolatori incredibilmente veloci e obbedienti."
> — *Principio dell'Elaborazione Dati*

Nel capitolo precedente abbiamo aperto i nostri "sportelli" (variabili) nella memoria per riporre dati statici. Ma l'informatica aziendale vive di **calcoli, confronti e logica**: calcolare l'IVA, applicare sconti percentuali, verificare se un cliente ha diritto a promozioni e decidere tariffe al volo.

Per trasformare i dati grezzi in informazioni utili usiamo le **espressioni**, gli **operatori** e uno strumento compatto ed elegante: l'**operatore ternario (`?:`)**.

---

### 💡 La Metafora: La Cassa Veloce con Smistamento Automatico

> 💡 **Metafora:**  
> Pensa alla cassa automatica di un supermercato moderno:
> - **Gli operatori aritmetici** sono i calcoli sui prodotti sul nastro (somma dei prezzi, moltiplicazione per i pezzi, calcolo della percentuale di sconto).
> - **Gli operatori di confronto e logici** sono i sensori della cassa: verificano se il peso della busta corrisponde (`==`), se l'importo supera i 50€ (`>`) e se hai scansionato sia la carta fedeltà **CHE** il coupon sconto (`&&`).
> - **L'operatore ternario (`?:`)** è il display rapido che, con una sola occhiata al carrello, decide all'istante:  
>   *"Spesa > 50€ ? Spedizione Gratuita : Paga 5.90€"*.

---

### ⚙️ Gli Operatori Fondamentali del C++

Un'**espressione** è una combinazione di variabili, valori e operatori che, una volta calcolata dal processore, **produce un singolo valore**.

#### 1. Operatori Aritmetici (I Calcoli)
- `+` (Somma) e `-` (Sottrazione)
- `*` (Moltiplicazione)
- `/` (Divisione): **attenzione al tranello della divisione intera!**
  - Se dividi due interi (`7 / 2`), il C++ esegue una divisione intera e il risultato è `3` (il resto viene perso).
  - Se almeno uno dei due è `double` (`7.0 / 2` o `7 / 2.0`), il risultato è `3.5`.
- `%` (Modulo o Resto): calcola il resto della divisione tra interi (`7 % 2` restituisce `1`). Fondamentale per sapere se un numero è pari o dispari o per gestire turni e periodicità.

#### 2. Operatori di Confronto (Le Domande)
Confrontano due valori e restituiscono sempre un valore booleano: `true` (vero) oppure `false` (falso).
- `==` (Uguale a — attenzione: **due segni uguale**, non confonderlo con l'assegnamento `=`!)
- `!=` (Diverso da)
- `<`, `>`, `<=`, `>=` (Minore, Maggiore, Minore o uguale, Maggiore o uguale)

#### 3. Operatori Logici Booleani (La Logica di Business)
Permettono di combinare più condizioni insieme:

| Operatore | Nome | Quando è `true`? | Esempio SIA |
| :--- | :--- | :--- | :--- |
| `&&` | **AND** (E logico) | Solo se **entrambe** le condizioni sono vere | `haTessera && spesa > 100` (sconto per tesserati con alta spesa) |
| `\|\|` | **OR** (O logico) | Se **almeno una** delle condizioni è vera | `isStudente \|\| isOver65` (tariffa agevolata) |
| `!` | **NOT** (Negazione) | Ribalta il valore: trasforma `true` in `false` | `!contoBloccato` (il conto è operativo) |

---

### ⚡ L'Operatore Condizionale Ternario: Decisioni in Una Riga

Spesso nei sistemi informativi dobbiamo assegnare un valore a una variabile in base a una semplice condizione. Invece di scrivere blocchi lunghi, il C++ offre una sintassi compatta chiamata **operatore ternario** (perché richiede 3 elementi):

```
condizione ? valore_se_vero : valore_se_falso;
```

```cpp
// Se la spesa supera 50€ la spedizione è gratis (0.0), altrimenti costa 5.90€
double speseSpedizione = (totaleSpesa >= 50.0) ? 0.0 : 5.90;
```

L'operatore ternario è una **espressione** (calcola e restituisce un valore pronto per essere assegnato o stampato), non una sequenza di istruzioni.

---

### 🔬 Laboratorio PRIMM: Il Totale Fiscale e la Spedizione

Mettiamo alla prova la logica di business di un software e-commerce.

#### 1. PREDICT (Prevedi)
? Quale sarà l'output a schermo delle seguenti due righe di codice C++?
```cpp
int pezzi = 5;
double costoTotale = pezzi / 2 * 10.0;
std::cout << costoTotale;
```
- [ ] `25`
- [x] `20`
- [ ] `25.5`
- [ ] Errore di compilazione

<details>
<summary>💡 Spiegazione</summary>
Attenzione all'ordine di esecuzione e ai tipi! Le operazioni con la stessa precedenza (moltiplicazione e divisione) si valutano da sinistra a destra:
1. Prima viene calcolato <code>pezzi / 2</code>. Poiché <code>pezzi</code> (5) e <code>2</code> sono entrambi numeri <b>interi</b>, il C++ esegue la <b>divisione intera</b>: <code>5 / 2 = 2</code> (il decimale .5 viene eliminato!).
2. Poi viene calcolato <code>2 * 10.0</code>: essendoci un <code>double</code>, il risultato finale diventa <code>20.0</code>.
Se avessimo scritto <code>pezzi / 2.0 * 10.0</code>, il risultato sarebbe stato correttamente <code>25.0</code>!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma gestionale per la cassa. Nota l'uso dell'operatore ternario per decidere la percentuale di sconto e le spese di trasporto:

```cpp
/**
 * @file cassa_fiscale.cpp
 * @brief Calcolo scontrino con sconti fedeltà e spese di trasporto con operatore ternario.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Calcola il totale carrello, lo sconto e le spese di consegna.
 * @return int Codice di stato (0 = successo).
 */
int main() {
    /// Costante: soglia di spesa minima per avere la spedizione gratuita
    const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;

    /// Costo standard della spedizione per ordini sotto soglia
    const double COSTO_SPEDIZIONE_STANDARD = 6.50;

    /// Importo totale lordo dei prodotti acquistati nel carrello
    double importoProdotti = 85.00;

    /// Il cliente possiede la tessera fedeltà aziendale?
    bool isClienteFedelta = true;

    // Calcolo percentuale di sconto: 10% se tesserato con spesa >= 50€, altrimenti 2%
    double percentualeSconto = (isClienteFedelta && importoProdotti >= 50.0) ? 0.10 : 0.02;

    /// Valore monetario dello sconto applicato
    double valoreSconto = importoProdotti * percentualeSconto;

    /// Importo effettivo dei prodotti al netto dello sconto
    double totaleMerceScontata = importoProdotti - valoreSconto;

    // Calcolo spese di spedizione tramite operatore ternario
    double speseConsegna = (totaleMerceScontata >= SOGLIA_SPEDIZIONE_GRATIS) ? 0.0 : COSTO_SPEDIZIONE_STANDARD;

    /// Importo complessivo finale dovuto dal cliente
    double totaleFattura = totaleMerceScontata + speseConsegna;

    // Visualizzazione dettagliata dello scontrino
    std::cout << "===== RIEPILOGO SCONTRINO CASSA =====" << "\n";
    std::cout << "Totale carrello : " << importoProdotti << " EUR" << "\n";
    std::cout << "Sconto applicato: -" << valoreSconto << " EUR (" << (percentualeSconto * 100) << "%)\n";
    std::cout << "Merce scontata  : " << totaleMerceScontata << " EUR" << "\n";
    std::cout << "Spese trasporto : " << speseConsegna << " EUR" << "\n";
    std::cout << "-------------------------------------" << "\n";
    std::cout << "TOTALE DA PAGARE: " << totaleFattura << " EUR" << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: La Valutazione dell'Espressione)

Vediamo passo dopo passo come il processore valuta l'operatore ternario e memorizza i dati:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20const%20double%20SOGLIA_GRATIS%20%3D%2060.0%3B%0A%20%20%20%20double%20spesa%20%3D%2085.0%3B%0A%20%20%20%20bool%20isFedele%20%3D%20true%3B%0A%0A%20%20%20%20double%20sconto%20%3D%20%28isFedele%20%26%26%20spesa%20%3E%3D%2050.0%29%20%3F%200.10%20%3A%200.02%3B%0A%20%20%20%20double%20trasporto%20%3D%20%28spesa%20%3E%3D%20SOGLIA_GRATIS%29%20%3F%200.0%20%3A%206.50%3B%0A%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Totale%3A%20%22%20%3C%3C%20%28spesa%20-%20%28spesa%20*%20sconto%29%20%2B%20trasporto%29%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e procedi con il tasto **"Next"**:
1. All'istruzione con `(isFedele && spesa >= 50.0) ? 0.10 : 0.02`:
   - Il processore controlla prima la condizione tra parentesi: `isFedele` è `true`, e `spesa >= 50.0` è `true`.
   - `true && true` produce `true`.
   - Il processore seleziona il ramo sinistro (`0.10`) e **ignora completamente** il ramo destro (`0.02`).
   - Il valore `0.10` viene scritto nello sportello della variabile `sconto`.
2. Nota come le espressioni complesse non occupano spazio permanente: vengono calcolate al volo nei registri della CPU e solo il risultato finale viene salvato nello stack.

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Promozione Weekend:** Modifica la condizione dello sconto usando l'operatore `||` (OR): concedi lo sconto del 10% se il cliente ha la tessera **OPPURE** se la spesa supera i 100€ (anche senza tessera).
2. **Supplemento Servizio Express:** Aggiungi un flag `bool consegnaRapida = true;`. Modifica il calcolo delle spese di trasporto in modo che, se la consegna è rapida, venga aggiunto un supplemento fisso di `3.00€` tramite un'espressione ternaria.
3. **Controllo Resto con il Modulo:** Dichiara una variabile `int articoli = 14;` e usa l'operatore modulo `%` con il ternario per stampare se il numero di articoli acquistati è pari o dispari:
   ```cpp
   std::cout << ((articoli % 2 == 0) ? "Numero pari" : "Numero dispari");
   ```

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: La Commissione Transazione POS Bancario**  
> Gli esercenti commerciali pagano una commissione alla banca per ogni pagamento ricevuto tramite POS (Point of Sale).
> 
> Scrivi un programma C++ autonomo (`commissioni_pos.cpp`) che calcoli il costo di una transazione per un negozio:
> - Dichiara `double importoPagamento`: l'incasso della vendita effettuata dal cliente (es. `45.00€`).
> - Dichiara `bool circuitoInternazionale`: `true` se la carta appartiene a un circuito internazionale (es. Visa/Mastercard estera), `false` se è un circuito PagoBANCOMAT nazionale.
> - **Regola di Business con Operatore Ternario:**
>   - Se il circuito è internazionale, la commissione percentuale è dell'**1.8%** (`0.018`).
>   - Se è PagoBANCOMAT, la commissione è dello **0.7%** (`0.007`).
> - **Commissione Minima Fissa (Operatore Ternario):**
>   - Calcola la commissione in euro. Se la commissione calcolata risulta inferiore a `0.15€`, la banca applica comunque una commissione minima fissa di `0.15€` (usa il ternario per verificare se la commissione calcolata è `< 0.15`).
> - Calcola l'**incasso netto effettivo** che rimane all'esercente (`importoPagamento - commissioneFinale`).
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti `///` sulle variabili con le relative aliquote.
> - Stampa chiara e professionale dello scontrino di cassa con i costi bancari esplicitati.
## 🚦 Capitolo 5: Bivi e Decisioni (Il Costrutto if e if-else)

> "Le decisioni sono i binari su cui viaggiano i processi aziendali."
> — *Principio di Ingegneria Gestionale*

Fino ad ora i nostri programmi hanno marciato dritti come un treno su un unico binario: una riga dopo l'altra, dall'inizio alla fine. Ma il mondo reale non è mai una linea retta: un pagamento può essere **approvato o rifiutato**, una merce in magazzino può essere **esaurita o disponibile**, un cliente può avere o meno i requisiti per un prestito.

Per gestire queste situazioni, il C++ mette a disposizione il costrutto fondamentale di selezione: l'istruzione **`if`** (se) e la sua estensione **`if-else`** (se... altrimenti).

---

### 💡 La Metafora: Il Tornello Automatico di Sicurezza

> 💡 **Metafora:**  
> Pensa al **tornello d'accesso** all'ingresso della sede aziendale o della metropolitana:
> - **L'`if` semplice (senza `else`):** È un sensore di controllo "guardiano". Se rileva un'anomalia (es. allarme antincendio), attiva la sirena. Se non rileva nulla, non fa assolutamente niente e il flusso continua indisturbato.
> - **L'`if-else` (bivio a due vie):** È il lettore di badge al tornello:
>   - *SE (`if`)* passi un badge valido: il tornello si sblocca, la spia diventa verde e ti fa passare.
>   - *ALTRIMENTI (`else`)*: la spia diventa rossa, emette un segnale acustico d'errore e ti blocca l'ingresso.
>   - **Non esistono vie di mezzo:** o si attiva il ramo verde, o si attiva il ramo rosso. Mai entrambi contemporaneamente!

---

### 🔀 I Due Modelli di Selezione

#### 1. L'Istruzione `if` Semplice (Azione Condizionata)
Si usa quando vuoi eseguire un blocco di istruzioni **solo se si verifica una determinata condizione**. Se la condizione è falsa, l'azione viene semplicemente saltata.

```cpp
if (giacenzaMagazzino < LIVELLO_MINIMO) {
    std::cout << "ATTENZIONE: Scorte in esaurimento! Inviare ordine fornitore.\n";
}
```

#### 2. L'Istruzione `if-else` (Mutua Esclusione)
Si usa quando devi scegliere **esattamente una fra due strade alternative**:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
:Leggi Saldo e Importo Spesa;
if (Saldo >= Spesa?) then (VERO)
  :Transazione Approvata;
  :Scala importo dal Saldo;
else (FALSO)
  :Transazione Rifiutata;
  :Mostra avviso "Fondi Insufficienti";
endif
:Stampa scontrino finale;
stop
@enduml
```

---

### ⚠️ I Due Grandi Tranelli di Sintassi

I programmatori alle prime armi cadono spesso in due insidie classiche del C++:

1. **Il Punto e Virgola Traditore:**
   ```cpp
   // ERRORE GRAVISSIMO:
   if (saldo >= importo); // <-- QUEL PUNTO E VIRGOLA CHIUDE SUBITO L'IF!
   {
       std::cout << "Pagamento approvato!\n"; // Verrà eseguito SEMPRE!
   }
   ```
   Dopo la tonda della condizione dell'`if` **non va mai il punto e virgola**.

2. **Le Parentesi Graffe `{}` e lo "Scope" (Visibilità):**
   Se ometti le parentesi graffe, il C++ considera legata all'`if` **esclusivamente la prima istruzione successiva**. Per evitare bug nascosti e mantenere il codice sicuro, **usa sempre le graffe**, anche per una sola riga!
   Inoltre, qualsiasi variabile creata dentro un blocco `{}` nasce e muore lì dentro (non esiste al di fuori di quelle graffe).

---

### 🔬 Laboratorio PRIMM: Il Terminale Pagamenti POS

Sviluppiamo il sistema di autorizzazione dei pagamenti elettronici per un punto vendita.

#### 1. PREDICT (Prevedi)
? Osserva attentamente il seguente frammento di codice. Quali righe verranno stampate sul terminale?
```cpp
int scorte = 12;
if (scorte < 5)
    std::cout << "1. Ordina nuovi pezzi!\n";
    std::cout << "2. Notifica inviata al fornitore.\n";
std::cout << "3. Controllo terminato.\n";
```
- [ ] Non stampa nulla
- [ ] Stampa tutte e tre le righe: 1, 2 e 3
- [x] Stampa solo le righe 2 e 3
- [ ] Stampa solo la riga 3

<details>
<summary>💡 Spiegazione</summary>
Poiché non sono state usate le parentesi graffe <code>{}</code>, l'istruzione <code>if (scorte < 5)</code> controlla <b>soltanto</b> la prima riga successiva (la riga 1).  
Dato che <code>scorte < 5</code> è <code>false</code> (12 non è minore di 5), la riga 1 viene saltata.  
Ma la riga 2 ("Notifica inviata...") è un'istruzione indipendente, non appartiene all'if! Viene quindi eseguita, seguita dalla riga 3.  
<b>Regola d'oro:</b> usa sempre le parentesi graffe <code>{}</code> per racchiudere i blocchi decisionali!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma gestionale `autorizzazione_pos.cpp`. Nota come l'`if-else` garantisce la sicurezza della transazione finanziaria:

```cpp
/**
 * @file autorizzazione_pos.cpp
 * @brief Sistema di verifica e autorizzazione per pagamenti con carta POS.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Punto di ingresso: verifica i fondi disponibili e processa il pagamento.
 * @return int Codice di stato (0 = transazione conclusa).
 */
int main() {
    /// Saldo disponibile sulla carta prepagata del cliente
    double saldoDisponibile = 45.00;

    /// Importo totale della spesa battuta in cassa
    double importoSpesa = 62.50;

    std::cout << "=== TERMINALE PAGAMENTI POS ===" << "\n";
    std::cout << "Importo richiesto: " << importoSpesa << " EUR" << "\n";
    std::cout << "Verifica disponibilita in corso...\n\n";

    // Bivio decisionale a due rami (if-else)
    if (saldoDisponibile >= importoSpesa) {
        // Ramo VERO: I fondi sono sufficienti
        /// Flag locale di autorizzazione: esiste SOLO all'interno di questo blocco if
        bool autorizzato = true;

        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << ">>> TRANSAZIONE APPROVATA (" << (autorizzato ? "ESITO POSITIVO" : "") << ") <<<" << "\n";
        std::cout << "Nuovo saldo residuo: " << saldoDisponibile << " EUR" << "\n";
    } else {
        // Ramo FALSO: Fondi insufficienti
        /// Variabile locale per il debito residuo: esiste SOLO dentro l'else
        double importoMancante = importoSpesa - saldoDisponibile;

        std::cout << ">>> TRANSAZIONE NEGATA <<<" << "\n";
        std::cout << "Motivo: Credito insufficiente sulla carta." << "\n";
        std::cout << "Importo mancante : " << importoMancante << " EUR" << "\n";
    }

    std::cout << "\nGrazie per aver utilizzato i nostri servizi bancari.\n";
    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Bivio e la Visibilità nello Stack)

Ora è **obbligatorio** aprire Python Tutor per toccare con mano uno dei concetti più importanti e fraintesi della programmazione: la **visibilità (scope)** delle variabili.

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20saldo%20%3D%20100.00%3B%0A%20%20%20%20double%20spesa%20%3D%2062.50%3B%0A%0A%20%20%20%20if%20%28saldo%20%3E%3D%20spesa%29%20%7B%0A%20%20%20%20%20%20%20%20bool%20autorizzato%20%3D%20true%3B%0A%20%20%20%20%20%20%20%20saldo%20-%3D%20spesa%3B%0A%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Approvato%3A%20%22%20%3C%3C%20autorizzato%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20double%20importoMancante%20%3D%20spesa%20-%20saldo%3B%0A%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Negato%5Cn%22%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi il tasto **"Next"** passo dopo passo, tenendo gli occhi fissi sul riquadro **Frames (Stack)** a destra.

> ❓ **Domanda Guida Obbligatoria:**  
> **"Cosa succede alla variabile `autorizzato` quando il cursore di esecuzione esce dalla parentesi graffa di chiusura `}` dell'if?"**

Osserva cosa accade a schermo:
1. All'ingresso nel blocco `if`, nello stack viene riservato uno spazio per `autorizzato = true`.
2. Appena l'esecuzione raggiunge e supera la parentesi graffa `}`, **la variabile `autorizzato` scompare letteralmente dallo stack!**

> 💡 **La Metafora del Locker Temporaneo:**  
> Immagina che aprire una parentesi graffa `{` equivalga ad attivare uno **scomparto locker a noleggio istantaneo**:  
> - Ci depositi dentro il pacco (`bool autorizzato = true;`).  
> - Puoi usarlo liberamente finché rimani all'interno di quella stanza delimitata dalle graffe `{ ... }`.  
> - Ma non appena varchi la soglia della graffa di chiusura `}`, **lo scompartimento si sigilla e diventa inaccessibile**: la serratura scatta e il vano viene rimosso dal sistema.  
> 
> Se subito dopo la graffa provi a scrivere `std::cout << autorizzato;`, per il compilatore è come chiedere il pacco a uno sportello che **non esiste più nel magazzino**: riceverai l'errore bloccante:  
> `error: 'autorizzato' was not declared in this scope`.

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Aggiunta del Guardiano Sottoscorta (`if` semplice):** Aggiungi in testa al programma una variabile `int rotoloCartaTermica = 3;` (metri di carta rimasti nella stampante del POS). Se i metri sono inferiori a 5, stampa un messaggio di allarme: *"Attenzione: sostituire presto il rotolo di carta scontrini!"*. Usa un `if` semplice senza `else`.
2. **Commissione di Micro-Pagamento:** Se il pagamento è inferiore a `10.00€`, applica una commissione fissa di `0.30€` sommandola a `importoSpesa` prima di verificare se il saldo è sufficiente.
3. **La prova dell'errore di Scope:** Prova a scrivere `std::cout << autorizzato;` oppure `std::cout << importoMancante;` fuori dai rispettivi blocchi, subito prima di `return 0;`. Osserva l'errore del compilatore che rifiuta di compilare il programma!

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Controllo Accessi al Caveau Aziendale**  
> L'azienda di logistica custodisce merci di alto valore in un caveau blindato. L'accesso è regolato da una doppia verifica elettronica: codice PIN numerico e possesso del badge dirigente.
> 
> Scrivi un programma C++ autonomo (`controllo_caveau.cpp`):
> - Dichiara la costante con il PIN corretto: `const int PIN_SEGRETO = 4821;`.
> - Dichiara `int pinInserito`: il codice digitato dall'impiegato sul tastierino (es. `4821`).
> - Dichiara `bool badgeDirigente`: `true` se il dipendente ha passato il badge da supervisore.
> - **Regola di Sicurezza:**
>   - Con un `if-else`, autorizza l'apertura della porta solo se il PIN digitato è identico al PIN segreto **E** il badge dirigente è abilitato (`pinInserito == PIN_SEGRETO && badgeDirigente`).
>   - Se l'accesso è autorizzato, stampa a video: *"Sblocco serratura... Accesso al Caveau consentito. Benvenuto!"*.
>   - Nel ramo `else`, stampa: *"ACCESSO NEGATO: Credenziali errate! Attivazione telecamere di sicurezza."*.
>   - Inoltre, all'interno del ramo `else`, aggiungi un `if` semplice: se il PIN inserito era diverso da zero, stampa anche: *"Tentativo registrato nel log di sicurezza."*.
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti `///` sulle variabili e costanti.
> - Indentazione perfetta e graffe `{}` su tutti i blocchi.
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
