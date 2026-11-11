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
