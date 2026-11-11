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
