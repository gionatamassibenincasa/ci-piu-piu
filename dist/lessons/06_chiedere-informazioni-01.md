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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/05_variabili-tipi-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/07_espressioni-ternario-01.md)

---


## 🧾 Chiedere informazioni: leggere dati con `std::cin`

Un gestionale non può lavorare soltanto con dati scritti in anticipo. Al POS
l'operatore inserisce una quantità; in un preventivo inserisce un prezzo; in
magazzino comunica quanti pezzi sono arrivati.

Con `std::cin` il tuo programma può aspettare un dato dalla tastiera e
conservarlo in una variabile.

> 💡 **Metafora:** Immagina un addetto allo sportello. `std::cout` è la voce
> con cui l'addetto fa una domanda; `std::cin` è il modulo su cui annota la
> risposta; la variabile è il campo del modulo destinato a quel dato. Se
> chiedi prima la quantità e poi il prezzo, devi registrare le risposte nello
> stesso ordine.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- leggere da tastiera quantità e prezzi con `std::cin` e usarli in un calcolo.

---

### ⚙️ Prima del laboratorio: input e output

| Istruzione | Direzione del dato | Esempio |
| :--- | :--- | :--- |
| `std::cout << valore` | Dal programma allo schermo | Mostra una richiesta o un risultato |
| `std::cin >> variabile` | Dalla tastiera alla variabile | Conserva ciò che l'utente inserisce |
| `int quantita;` | Prepara uno spazio per interi | Pezzi o confezioni |
| `double prezzo;` | Prepara uno spazio per decimali | Prezzi o importi |

La variabile deve esistere prima della lettura:

```cpp
int quantita;
std::cin >> quantita;
```

Il simbolo `>>` indica che il dato viaggia dalla tastiera verso la variabile.
Non confonderlo con `<<`, che usa la direzione opposta.

---

### 🧭 Prima del laboratorio: l'ordine del dialogo

Un dialogo utile segue questo percorso:

1. `std::cout` spiega quale dato inserire.
2. `std::cin` aspetta la risposta.
3. La variabile conserva il valore.
4. Il programma usa il valore nel calcolo o nel riepilogo.

Se il prezzo viene letto dopo la quantità, anche l'utente deve inserire prima la
quantità e poi il prezzo. Il computer non indovina l'ordine che avevi in mente.

---

### 🔬 Laboratorio PRIMM: un ordine al POS

Il POS deve leggere quantità e prezzo unitario per calcolare il totale di una
riga di vendita.

#### 1. PREDICT (Prevedi)

```cpp
int quantita;
double prezzo;
std::cin >> quantita;
std::cin >> prezzo;
```

**Domanda 1**

Che cosa fa `std::cin >> quantita;` quando il programma arriva a questa riga?

[(X)] Attende un valore da tastiera e lo memorizza nella variabile `quantita`
[( )] Stampa il nome `quantita` sullo schermo
[( )] Assegna automaticamente a `quantita` il valore zero

**Domanda 2**

Perché una variabile deve essere dichiarata prima di essere usata con `std::cin`?

[(X)] Il compilatore deve conoscere nome e tipo dello spazio in cui conservare il dato
[( )] La tastiera può inviare dati solo a variabili dichiarate come `const`
[( )] Senza dichiarazione `std::cin` stampa sempre un messaggio di errore a video

**Domanda 3**

Se il programma esegue prima `std::cin >> quantita;` e poi `std::cin >> prezzo;`, che cosa deve inserire l'utente?

[(X)] Prima un valore compatibile con `quantita`, poi uno compatibile con `prezzo`
[( )] Un solo testo che contiene contemporaneamente nome e prezzo
[( )] Prima il prezzo, perché `double` viene sempre letto per primo

**Domanda 4**

Perché il messaggio `Inserisci la quantità:` va scritto prima di `std::cin`?

[(X)] Per spiegare all'utente quale dato deve digitare prima che il programma attenda
[( )] Perché `std::cin` legge solo dopo aver stampato almeno tre righe
[( )] Per trasformare automaticamente un intero in una stringa

**Domanda 5**

Quale tipo è coerente con una quantità intera di prodotti?

[(X)] `int`, perché una quantità di confezioni può essere un numero intero
[( )] `double`, perché ogni dato inserito da tastiera contiene decimali
[( )] `char`, perché la quantità è sempre un singolo carattere

#### 2. RUN (Esegui)

Digita il programma completo. Quando compare una richiesta, inserisci un valore
e premi `Invio`; poi inserisci il valore successivo.

```cpp
/**
 * @file ordine_pos.cpp
 * @brief Legge quantità e prezzo per calcolare una riga di vendita.
 */
#include <iostream>

/**
 * @brief Acquisisce i dati di un ordine e calcola il totale.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// La quantità conta confezioni intere vendute.
    int quantita;
    /// Il prezzo deve conservare i centesimi dell'articolo.
    double prezzoUnitario;

    std::cout << "Quantita: ";
    std::cin >> quantita;

    std::cout << "Prezzo unitario: ";
    std::cin >> prezzoUnitario;

    double totale = quantita * prezzoUnitario;
    std::cout << "Totale: " << totale << " euro\n";

    return 0;
}
```
@LIA.cpp

Prova, per esempio, con:

```text
3
12.50
```

Il programma dovrebbe calcolare `37.5` euro.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci il percorso di ciascun dato. Concentrati sul
*perché* e sull'ordine, non soltanto sul totale.

```cpp
int quantita;
double prezzoUnitario;

std::cout << "Quantita: ";
std::cin >> quantita;
std::cout << "Prezzo: ";
std::cin >> prezzoUnitario;
```

**Domanda 1**

Qual è l'ordine corretto quando l'utente inserisce `3` e poi `12.50`?

[(X)] Il `3` entra in `quantita`, poi `12.50` entra in `prezzoUnitario`
[( )] Entrambi i valori entrano nella stessa variabile `quantita`
[( )] `12.50` viene letto per primo perché è un numero decimale

**Domanda 2**

Perché `std::cin` non mostra da solo la richiesta "Quantita:"?

[(X)] `std::cin` legge dati; il messaggio per l'utente deve essere scritto con `std::cout`
[( )] La tastiera non permette di visualizzare messaggi
[( )] Ogni variabile deve contenere il testo della richiesta

**Domanda 3**

Che cosa succede se inserisci `3` quando `std::cin` sta leggendo un `double`?

[(X)] Il valore può essere letto come `3.0`, perché un intero è compatibile con un numero decimale
[( )] Il programma si chiude sempre senza leggere nulla
[( )] Il numero viene trasformato in una parola composta da tre caratteri

**Domanda 4**

Perché l'istruzione `double totale = quantita * prezzoUnitario;` deve venire dopo le due letture?

[(X)] Prima di quel punto le variabili potrebbero non contenere ancora i dati inseriti dall'utente
[( )] Le moltiplicazioni in C++ sono permesse solo nell'ultima riga di `main`
[( )] `std::cin` cancella i valori se il calcolo viene scritto prima

**Domanda 5**

Se inserisci testo come `tre` quando `std::cin` attende un `int`, perché il calcolo successivo è inaffidabile?

[(X)] La lettura fallisce e la variabile non riceve il numero atteso
[( )] C++ converte sempre automaticamente ogni parola nel numero corretto
[( )] Il testo viene memorizzato nell'intero come se fosse un carattere

| Passo | Istruzione | Stato importante |
| :---: | :--- | :--- |
| 1 | `int quantita;` | Esiste uno spazio per un intero |
| 2 | `double prezzoUnitario;` | Esiste uno spazio per un decimale |
| 3 | `std::cin >> quantita;` | Il primo input entra in `quantita` |
| 4 | `std::cin >> prezzoUnitario;` | Il secondo input entra in `prezzoUnitario` |
| 5 | `double totale = ...` | Il calcolo usa i due valori letti |

`std::cin` non crea il messaggio per l'utente: legge soltanto. Per questo
`std::cout` deve precedere ogni lettura con una richiesta chiara.

Se inserisci `tre` quando il programma attende un `int`, la lettura non riceve
il numero previsto. Per ora non gestiamo ancora l'errore: impariamo prima il
percorso normale dei dati.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva come i valori
> inseriti sostituiscono il contenuto iniziale delle variabili.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
int quantita;
double prezzoUnitario;

std::cout << "Quantita: ";
std::cin >> quantita;
std::cout << "Prezzo: ";
std::cin >> prezzoUnitario;
```

**Domanda 1**

Quale modifica permette di leggere anche uno sconto percentuale?

[(X)] Dichiarare `double sconto;` e aggiungere `std::cin >> sconto;` dopo il prezzo
[( )] Scrivere `std::cin << sconto;` senza dichiarare la variabile
[( )] Cambiare `quantita` in `const double` per ricevere un nuovo dato

**Domanda 2**

Se vuoi leggere prima il prezzo e poi la quantità, quale modifica è necessaria?

[(X)] Invertire sia i messaggi sia l'ordine delle due istruzioni `std::cin`
[( )] Cambiare solo i nomi delle variabili, lasciando invariato il codice
[( )] Usare `std::cout` al posto di entrambe le istruzioni di lettura

**Domanda 3**

Che effetto ha aggiungere `std::cout << " euro\n";` dopo il totale?

[(X)] Aggiunge l'unità di misura all'output, senza cambiare il calcolo
[( )] Converte il totale in un intero arrotondato
[( )] Fa inserire un altro prezzo all'utente

**Domanda 4**

Quale modifica conserva i centesimi del prezzo inserito?

[(X)] Dichiarare il prezzo come `double` e leggerlo con `std::cin`
[( )] Dichiarare il prezzo come `int` perché è più semplice
[( )] Leggere il prezzo in un `char` e poi moltiplicarlo

**Domanda 5**

Perché conviene aggiungere una sola lettura o modifica alla volta?

[(X)] Per capire quale passaggio ha causato un errore o un ordine di input inatteso
[( )] Perché `std::cin` può leggere una sola variabile in tutta la funzione
[( )] Perché ogni nuova variabile cancella automaticamente la precedente

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    int quantita;
    double prezzoUnitario;

    std::cout << "Quantita: ";
    std::cin >> quantita;

    std::cout << "Prezzo unitario: ";
    std::cin >> prezzoUnitario;

    double totale = quantita * prezzoUnitario;
    std::cout << "Totale: " << totale << " euro\n";
    return 0;
}
```

</details>

**Modifica A — aggiungi uno sconto**

Dichiara `double sconto;`, mostra una richiesta e leggi la percentuale dopo il
prezzo unitario. Per ora stampa il valore inserito senza cambiare il totale.

**Modifica B — cambia l'ordine**

Fai chiedere prima il prezzo e poi la quantità. Inverti sia i messaggi sia le
istruzioni `std::cin`, così il dialogo resta coerente.

**Modifica C — aggiungi l'unità di misura**

Completa la stampa del totale con il testo `euro`. Il testo cambia l'output,
non il calcolo.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio commerciale deve creare un piccolo
preventivo per un cliente.

Crea `preventivo.cpp` rispettando tutti i requisiti:

1. Dichiara `int quantita` e `double prezzoUnitario` prima delle letture.
2. Chiedi e leggi quantità e prezzo con `std::cin`.
3. Mantieni lo stesso ordine tra messaggi, input e variabili.
4. Calcola `totale = quantita * prezzoUnitario`.
5. Stampa quantità, prezzo unitario e totale.
6. Usa un commento `///` per spiegare perché il prezzo è `double`.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    /// TODO: spiega perché il prezzo deve conservare i centesimi.
    // TODO: dichiara quantità e prezzo, leggili e calcola il totale.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `std::cout <<` porta dati dal programma allo schermo.
- `std::cin >>` porta dati dalla tastiera a una variabile.
- Dichiara una variabile prima di usarla per la lettura.
- L'ordine di prompt e letture deve corrispondere all'ordine degli input.
- Usa `int` per quantità intere e `double` per prezzi con centesimi.

---

### ➡️ Prossimo chunk

Ora il programma sa chiedere dati. Nel prossimo chunk imparerai a scegliere tra
due percorsi con `if`, così il gestionale potrà reagire ai valori inseriti.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/05_variabili-tipi-01.md">Lezione precedente (5 — Gli sportelli della memoria: variabili, costanti e tipi)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/07_espressioni-ternario-01.md">Lezione successiva (7 — La Calcolatrice Fiscale: espressioni e operatore ternario)</a>
