<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-20
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/04_doxygen-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/06_chiedere-informazioni-01.md)

---


## 📦 Gli sportelli della memoria: variabili, costanti e tipi

> "Chi controlla il passato controlla il futuro.
> Chi controlla il presente controlla il passato."
>
> -- George Orwell

Finora hai stampato testi fissi. Un software gestionale, però, deve ricordare
dati che cambiano: prezzo di un articolo, giacenza di magazzino, saldo di un
conto.

Per farlo usi variabili e costanti.

> 💡 **Metafora:** Immagina la memoria RAM come una parete di sportelli
> automatici. Il nome della variabile è l'etichetta che leggi tu; il tipo
> indica quale merce può entrare nello sportello; il valore è la merce
> conservata. Uno sportello `const` è sigillato: dopo averlo riempito non puoi
> cambiare il contenuto.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- dichiarare variabili e costanti scegliendo il tipo adatto a un dato aziendale.

In questo chunk non chiediamo ancora dati da tastiera con `std::cin`: ci
concentriamo sul ricordare, mostrare e modificare valori già scritti nel codice.

---

### ⚙️ Prima del laboratorio: i tipi fondamentali

| Tipo | Che cosa contiene | Esempio aziendale |
| :--- | :--- | :--- |
| `int` | Numeri interi | `int giacenza = 42;` |
| `double` | Numeri con parte decimale | `double prezzo = 19.50;` |
| `char` | Un solo carattere | `char reparto = 'A';` |
| `bool` | Uno tra due stati | `bool inPromozione = true;` |
| `std::string` | Testo di lunghezza variabile | `std::string nome = "Mouse";` |
| `const T` | Valore non modificabile | `const double IVA = 0.22;` |

Per usare `std::string` inserisci `#include <string>`.

> ⚠️ **Trappola classica:** `int pezzi = 7.85;` non arrotonda a `8`.
> Conserva `7`, perché `int` non può contenere la parte decimale. Per prezzi,
> saldi e aliquote usa `double`.

---

### 🧭 Prima del laboratorio: dichiarare e sigillare

Una dichiarazione unisce tipo, nome e valore iniziale:

| Scrittura | Come leggerla |
| :--- | :--- |
| `int giacenza = 42;` | Uno sportello per un conteggio intero |
| `double prezzo = 19.50;` | Uno sportello per un valore con centesimi |
| `const double IVA = 0.22;` | Uno sportello sigillato con un valore decimale |

Il tipo non è una decorazione: stabilisce quali valori possono essere
conservati e quali operazioni hanno senso.

---

### 🔬 Laboratorio PRIMM: la scheda articolo

Un magazzino deve mostrare i dati di un articolo: descrizione, reparto,
giacenza, prezzo e garanzia. Ogni dato usa uno sportello adatto.

#### 1. PREDICT (Prevedi)

```cpp
int pezzi = 7.85;
double prezzo = 19.50;
const double IVA = 0.22;
```

**Domanda 1**

Perché `int pezzi = 7.85;` non conserva tutti i decimali?

[( )] Perché ogni numero con la virgola produce un errore obbligatorio
[( )] Perché il compilatore arrotonda sempre i prezzi per difetto
[(X)] Perché `int` rappresenta numeri interi e la parte decimale viene troncata

**Domanda 2**

Quale tipo è più adatto per memorizzare un prezzo con i centesimi?

[( )] `char`, perché ogni prezzo è una singola cifra
[( )] `int`, perché i prezzi sono sempre conteggi di pezzi
[(X)] `double`, perché può rappresentare valori con parte decimale

**Domanda 3**

Perché `IVA` dovrebbe essere dichiarata `const`?

[(X)] Per impedire che il valore venga cambiato accidentalmente durante il programma
[( )] Per permettere al programma di modificarla più velocemente
[( )] Perché `const` trasforma automaticamente il numero in una stringa

**Domanda 4**

Quale tipo descrive meglio il codice di reparto `'A'`?

[(X)] `char`, perché contiene un solo carattere
[( )] `bool`, perché il reparto può essere vero o falso
[( )] `std::string`, perché ogni carattere è sempre una frase

**Domanda 5**

Che cosa indica la dichiarazione `bool haFido = true;`?

[(X)] Un dato con due stati possibili, qui impostato sul valore vero
[( )] Un numero decimale uguale a 1.0
[( )] Un testo composto dalle lettere `true`

#### 2. RUN (Esegui)

Digita il programma completo oppure usa il bottone. Prima di eseguirlo, indica
accanto a ogni variabile quale tipo riconosci.

```cpp
/**
 * @file scheda_articolo.cpp
 * @brief Memorizza e mostra i dati di un articolo di magazzino.
 */
#include <iostream>
#include <string>

/**
 * @brief Mostra una scheda articolo con tipi di dato diversi.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// L'aliquota di legge deve restare uguale durante il calcolo.
    const double ALIQUOTA_IVA = 0.22;
    /// Il nome commerciale può cambiare tra articoli.
    std::string nomeArticolo = "Mouse Wireless Ottico";
    /// Un reparto aziendale può essere rappresentato da un codice breve.
    char codiceReparto = 'A';
    /// La giacenza conta pezzi interi presenti in magazzino.
    int pezziInMagazzino = 42;
    /// Il prezzo richiede i centesimi.
    double prezzoNetto = 19.50;
    /// La garanzia estesa ha soltanto due stati.
    bool haGaranziaEstesa = true;

    std::cout << "=== SCHEDA ARTICOLO MAGAZZINO ===\n";
    std::cout << "Descrizione : " << nomeArticolo << "\n";
    std::cout << "Reparto     : " << codiceReparto << "\n";
    std::cout << "Giacenza    : " << pezziInMagazzino << " pezzi\n";
    std::cout << "Prezzo netto: " << prezzoNetto << " euro\n";
    std::cout << "Garanzia    : " << haGaranziaEstesa << "\n";
    std::cout << "Aliquota IVA: " << ALIQUOTA_IVA << "\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

Ora collega ogni sportello al suo ruolo. Rispondi alle domande sul *perché*,
non solo sul valore stampato.

```cpp
const double ALIQUOTA_IVA = 0.22;
int pezzi = 42;
double prezzoNetto = 19.50;
```

**Domanda 1**

Perché `pezzi` è un `int` mentre `prezzoNetto` è un `double`?

[( )] `double` serve solo per dati più importanti di `int`
[(X)] I pezzi sono conteggi interi, mentre il prezzo può contenere centesimi
[( )] I nomi delle variabili decidono automaticamente il tipo

**Domanda 2**

Quale sequenza descrive la dichiarazione `double prezzoNetto = 19.50;`?

[( )] Il programma stampa subito 19.50 senza bisogno di `std::cout`
[( )] Il valore viene sigillato e non potrà mai cambiare
[(X)] Il compilatore riserva un dato decimale, gli assegna un nome e gli dà un valore iniziale

**Domanda 3**

Perché `ALIQUOTA_IVA` non può essere assegnata di nuovo?

[( )] Un `double` può essere assegnato una sola volta
[(X)] La parola `const` la rende di sola lettura dopo l'inizializzazione
[( )] I nomi scritti in maiuscolo sono sempre immutabili in C++

**Domanda 4**

Quale valore viene memorizzato in `int pezzi = 7.85;`?

[( )] `7.85`, perché il tipo dichiarato non influenza il valore
[(X)] `7`, perché la parte decimale non appartiene al tipo `int`
[( )] `8`, perché C++ arrotonda al numero intero più vicino

**Domanda 5**

Perché il programma ha bisogno di `#include <string>` quando usa `std::string`?

[( )] Per permettere a `int` di contenere più cifre
[( )] Per convertire automaticamente tutti i numeri in testo
[(X)] Per rendere disponibile la definizione del tipo per il testo

| Nome | Tipo | Perché quel tipo? | Si può cambiare? |
| :--- | :--- | :--- | :--- |
| `ALIQUOTA_IVA` | `const double` | È un valore di legge | No |
| `nomeArticolo` | `std::string` | Contiene testo variabile | Sì |
| `codiceReparto` | `char` | Contiene un carattere | Sì |
| `pezziInMagazzino` | `int` | Conta pezzi interi | Sì |
| `prezzoNetto` | `double` | Contiene centesimi | Sì |
| `haGaranziaEstesa` | `bool` | Rappresenta sì/no | Sì |

Apri il programma su [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva come ogni variabile entra nello stack con un tipo e un valore.

Ricorda: senza `std::boolalpha`, `true` viene normalmente mostrato come `1` e
`false` come `0`.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
const double ALIQUOTA_IVA = 0.22;
double prezzoNetto = 19.50;
```

**Domanda 1**

Quale modifica permette di calcolare l'importo dell'IVA?

[(X)] Dichiarare `double importoIva = prezzoNetto * ALIQUOTA_IVA;`
[( )] Cambiare `const` in `std::string` senza eseguire un calcolo
[( )] Dichiarare `int importoIva = prezzoNetto + ALIQUOTA_IVA;`

**Domanda 2**

Che cosa succede se aggiungi `ALIQUOTA_IVA = 0.10;`?

[( )] Il programma ignora sempre la nuova assegnazione e compila
[(X)] Il compilatore segnala un errore perché la costante è di sola lettura
[( )] L'aliquota cambia solo per la riga successiva

**Domanda 3**

Quale modifica è corretta se la giacenza deve diventare 100 pezzi?

[( )] Cambiare il tipo in `char` e lasciare il valore `100`
[( )] Dichiarare la giacenza come `const` per poterla aggiornare
[(X)] Cambiare il valore iniziale in `int pezziInMagazzino = 100;`

**Domanda 4**

Quale effetto ha cambiare `bool haGaranziaEstesa = true;` in `false`?

[(X)] Il dato rappresenta l'assenza della garanzia estesa e l'output numerico diventa `0`
[( )] Il programma non può più compilare perché `bool` accetta solo `true`
[( )] La variabile diventa automaticamente una stringa vuota

**Domanda 5**

Perché conviene modificare un tipo o un valore alla volta?

[( )] Perché il compilatore non sa leggere due righe consecutive
[(X)] Per distinguere quale modifica ha prodotto il nuovo comportamento o l'errore
[( )] Perché ogni programma C++ può avere una sola variabile

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    const double ALIQUOTA_IVA = 0.22;
    double prezzoNetto = 19.50;
    return 0;
}
```

</details>

**Modifica A — calcola l'IVA**

Dichiara una nuova variabile:

```cpp
double importoIva = prezzoNetto * ALIQUOTA_IVA;
```

Poi stampa `importoIva` e il prezzo lordo, ottenuto sommando
`prezzoNetto + importoIva`.

**Modifica B — prova il lucchetto**

Aggiungi questa riga dopo la dichiarazione della costante:

```cpp
ALIQUOTA_IVA = 0.10;
```

Ricompila e osserva l'errore:

```text
error: assignment of read-only variable 'ALIQUOTA_IVA'
```

La parola `const` ha impedito un'assegnazione successiva: il compilatore
protegge il valore sigillato.

**Modifica C — cambia il dato aziendale**

Sostituisci `19.50` con `125.75`, ricompila e osserva come cambiano IVA e
prezzo lordo senza cambiare il tipo.

#### 5. MAKE (Crea)

**Scenario aziendale:** devi preparare una scheda sintetica di un conto
corrente aziendale.

Scrivi `conto_corrente.cpp` rispettando tutti i requisiti:

1. Memorizza banca e IBAN con `std::string`.
2. Memorizza saldo e interesse con `double`.
3. Usa `const double` per il tasso annuo.
4. Usa `bool` per indicare se il conto ha un fido.
5. Usa `char` per la classe di rating.
6. Stampa tutti i dati e calcola `saldo * tasso`.
7. Non modificare la costante del tasso dopo l'inizializzazione.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Scheda sintetica di un conto corrente aziendale.
 */
#include <iostream>
#include <string>

int main() {
    /// Il tasso è costante perché rappresenta la condizione del conto.
    // TODO: dichiara banca, IBAN, saldo, tasso, fido e rating.
    // TODO: stampa i dati e l'interesse annuo stimato.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Una variabile è uno sportello con nome, tipo e valore.
- `int` serve per conteggi interi; `double` per valori con decimali.
- `char` contiene un carattere; `bool` rappresenta due stati; `std::string` contiene testo.
- `const` sigilla un valore dopo l'inizializzazione.
- Scegli il tipo in base al significato aziendale del dato.

---

### ➡️ Prossimo chunk

Ora che sai memorizzare dati con il tipo corretto, userai operatori ed
espressioni per calcolare totali, IVA e differenze in modo controllato.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/04_doxygen-01.md">Lezione precedente (4 — Parlare al Futuro Te Stesso: documentazione Doxygen)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/06_chiedere-informazioni-01.md">Lezione successiva (6 — Chiedere informazioni: leggere dati con std::cin)</a>
