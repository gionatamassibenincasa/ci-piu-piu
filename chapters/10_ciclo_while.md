## 🔄 Capitolo 10: L'Anello Fondamentale (L'Iterazione Indefinita con il Ciclo while)

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
