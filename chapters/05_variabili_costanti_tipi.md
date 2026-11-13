## 📦 Capitolo 5: Gli Sportelli della Memoria (Variabili, Costanti e Tipi)

> "Chi controlla il passato controlla il futuro: chi controlla il presente controlla il passato."
>
> — G. Orwell

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
