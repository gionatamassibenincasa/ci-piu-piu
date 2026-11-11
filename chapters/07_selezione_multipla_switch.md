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
