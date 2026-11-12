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
