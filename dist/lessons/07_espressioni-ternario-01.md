<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-22
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/06_chiedere-informazioni-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/08_if-else-01.md)

---


## 🧮 La Calcolatrice Fiscale: espressioni e operatore ternario

> "La semplicità è la sofisticazione suprema."
>
> — *Leonardo da Vinci*

Quando prepari uno scontrino, non fai un solo calcolo: parti dall'importo,
applichi uno sconto e poi decidi se la spedizione è gratuita. In C++ puoi
scrivere questi passaggi come **espressioni** e usare il ternario per una
scelta semplice che restituisce direttamente un valore.

> 💡 **Metafora:**  
> Un'espressione è una riga della calcolatrice della cassa: combina numeri,
> variabili e operatori e restituisce un risultato. Il ternario è il sensore
> della cassa: legge una condizione e apre uno dei due cassetti, quello del
> valore vero oppure quello del valore falso.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un'espressione che calcola un importo e usa l'operatore ternario per scegliere un valore.

---

### ⚙️ Prima del laboratorio: costruire un'espressione

Un'espressione combina valori, variabili e operatori e produce **un solo
risultato**.

| Operatore | Significato | Attenzione |
| :--- | :--- | :--- |
| `+`, `-`, `*` | somma, differenza, prodotto | il risultato dipende dai tipi |
| `/` | divisione | tra soli `int` perde la parte decimale |
| `%` | resto della divisione | utile per controllare pari/dispari |
| `>=`, `==` | confronto | producono `true` oppure `false` |

```cpp
int pezzi = 5;
double a = pezzi / 2;   // 2.0: la divisione è già stata fatta tra int
double b = pezzi / 2.0; // 2.5: almeno un operando è double
```

### 🧭 Prima del laboratorio: scegliere un valore

La forma del ternario è:

```text
condizione ? valore_se_vero : valore_se_falso
```

Il programma valuta prima la condizione e poi sceglie **un solo** ramo:

```cpp
double spedizione = (totale >= 60.0) ? 0.0 : 6.50;
```

Il ternario è adatto a una scelta breve che produce un valore da assegnare,
stampare o usare in un altro calcolo. Le decisioni con più istruzioni
arriveranno con `if` / `else`.

---

### 🔬 Laboratorio PRIMM: Scontrino e-commerce

Calcolerai lo sconto e le spese di spedizione di un ordine online.

#### 1. PREDICT (Prevedi)

Prima di eseguire, osserva l'esempio e scegli la spiegazione più convincente:

```cpp
double importoProdotti = 85.00;
double sconto = (importoProdotti >= 50.0) ? 0.10 : 0.02;
double netto = importoProdotti - importoProdotti * sconto;
double spedizione = (netto >= 60.0) ? 0.0 : 6.50;
```

**Domanda 1**

Perché `importoProdotti >= 50.0` è utile dentro il ternario?

[(X)] Produce una condizione `true` o `false` che permette di scegliere un valore
[( )] Converte automaticamente l’importo in euro interi
[( )] Ripete il calcolo finché l’importo raggiunge 50 euro

**Domanda 2**

Quale valore assume `sconto` con `importoProdotti = 85.00`?

[(X)] `0.10`, perché 85 soddisfa la condizione e viene scelto il valore dopo `?`
[( )] `0.02`, perché il ternario sceglie sempre il valore dopo `:`
[( )] `10.00`, perché il numero 10 rappresenta direttamente gli euro di sconto

**Domanda 3**

Perché `importoProdotti / 2 * 10.0` con `int importoProdotti = 5` non dà 25.0?

[(X)] La divisione tra due `int` viene eseguita prima e perde la parte decimale: 5 / 2 vale 2
[( )] Il simbolo `*` viene ignorato quando compare dopo `/`
[( )] Un `int` non può essere usato in nessuna espressione con `double`

**Domanda 4**

Quale valore completo restituisce `netto >= 60.0 ? 0.0 : 6.50` quando `netto` vale 76.50?

[(X)] `0.0`, perché la condizione è vera e si sceglie il primo valore
[( )] `6.50`, perché le spese standard vengono calcolate per prime
[( )] `true`, perché un confronto restituisce sempre un booleano stampabile

**Domanda 5**

Quale forma assegna correttamente al netto il prezzo lordo meno lo sconto?

[(X)] `netto = lordo - lordo * percentualeSconto;`
[( )] `netto = lordo - percentualeSconto;`
[( )] `netto = lordo * percentualeSconto - lordo;`

#### 2. RUN (Esegui)

Digita il programma, eseguilo e confronta l'output con le tue previsioni.

```cpp
/**
 * @file scontrino_ecommerce.cpp
 * @brief Calcola sconto, spedizione e totale di un ordine online.
 * @return int Codice di uscita del programma.
 */
#include <iostream>

int main() {
    const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;
    const double COSTO_SPEDIZIONE_STANDARD = 6.50;
    double importoProdotti = 85.00;

    /// La soglia collega il vantaggio fedeltà al valore dell'ordine.
    double percentualeSconto =
        (importoProdotti >= 50.0) ? 0.10 : 0.02;
    double valoreSconto = importoProdotti * percentualeSconto;
    double nettoProdotti = importoProdotti - valoreSconto;

    /// La consegna gratuita riduce il costo per ordini abbastanza grandi.
    double speseSpedizione =
        (nettoProdotti >= SOGLIA_SPEDIZIONE_GRATIS)
            ? 0.0 : COSTO_SPEDIZIONE_STANDARD;
    double totaleDaPagare = nettoProdotti + speseSpedizione;

    std::cout << "=== SCONTRINO E-COMMERCE ===\n";
    std::cout << "Prodotti (lordo): " << importoProdotti << " euro\n";
    std::cout << "Sconto: " << valoreSconto << " euro\n";
    std::cout << "Prodotti (netto): " << nettoProdotti << " euro\n";
    std::cout << "Spedizione: " << speseSpedizione << " euro\n";
    std::cout << "TOTALE: " << totaleDaPagare << " euro\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

Dopo il Run, ricostruisci l'ordine dei valori:

```cpp
const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;
const double COSTO_SPEDIZIONE_STANDARD = 6.50;
double importoProdotti = 85.00;
double percentualeSconto =
    (importoProdotti >= 50.0) ? 0.10 : 0.02;
double valoreSconto = importoProdotti * percentualeSconto;
double nettoProdotti = importoProdotti - valoreSconto;
double speseSpedizione =
    (nettoProdotti >= SOGLIA_SPEDIZIONE_GRATIS)
        ? 0.0 : COSTO_SPEDIZIONE_STANDARD;
double totaleDaPagare = nettoProdotti + speseSpedizione;
```

**Domanda 1**

Quale ordine descrive correttamente il calcolo del totale?

[(X)] Prima si sceglie la percentuale, poi si calcola lo sconto, poi il netto e infine la spedizione
[( )] Prima si calcola il totale, poi si decide quale percentuale usare
[( )] I due ternari vengono eseguiti dopo la stampa, perché assegnano solo etichette

**Domanda 2**

Perché `valoreSconto` vale `8.5` in questo esempio?

[(X)] Perché l’espressione moltiplica 85.0 per 0.10, cioè il 10% scritto in forma decimale
[( )] Perché 0.10 viene interpretato come 10 euro fissi
[( )] Perché il programma divide 85 per 10 prima di moltiplicare

**Domanda 3**

Quale ramo del secondo ternario viene scelto?

[(X)] Il ramo `0.0`, perché `nettoProdotti` vale 76.5 ed è almeno 60.0
[( )] Il ramo `6.50`, perché il prezzo lordo è diverso dalla soglia
[( )] Nessun ramo, perché un `double` non può essere confrontato con una costante

**Domanda 4**

Perché il totale viene calcolato con `nettoProdotti + speseSpedizione` e non con l’importo lordo?

[(X)] Perché lo sconto è già stato sottratto e il cliente deve pagare il netto più l’eventuale spedizione
[( )] Perché il lordo contiene sempre un errore di divisione intera
[( )] Perché il ternario può sommare soltanto variabili chiamate `netto`

**Domanda 5**

Se il codice usa `nettoProdotti` prima della sua dichiarazione, perché il compilatore segnala un errore?

[(X)] Una variabile deve essere dichiarata e inizializzata prima di poter essere usata
[( )] Il compilatore esegue le righe in ordine alfabetico
[( )] I nomi con la parola `netto` sono riservati e non ammessi

| Passo | Espressione o variabile | Valore | Perché |
| :---: | :--- | ---: | :--- |
| 1 | `importoProdotti >= 50.0` | `true` | 85 è almeno 50 |
| 2 | `percentualeSconto` | `0.10` | viene scelto il ramo dopo `?` |
| 3 | `valoreSconto` | `8.5` | `85.0 * 0.10` |
| 4 | `nettoProdotti` | `76.5` | `85.0 - 8.5` |
| 5 | `nettoProdotti >= 60.0` | `true` | 76.5 supera la soglia |
| 6 | `speseSpedizione` | `0.0` | viene scelto il ramo dopo `?` |
| 7 | `totaleDaPagare` | `76.5` | netto più spedizione |

Apri il programma in [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva come ogni assegnazione crea o aggiorna una variabile prima della
stampa finale.

#### 4. MODIFY (Modifica)

Prima di cambiare il codice, prevedi l'effetto delle modifiche:

```cpp
double importoProdotti = 85.00;
double speseSpedizione =
    (importoProdotti >= 60.0) ? 0.0 : 6.50;
std::cout << speseSpedizione << "\n";
```

**Domanda 1**

Quale modifica fa pagare la spedizione gratis solo da 100 euro in su?

[(X)] Cambiare `importoProdotti >= 60.0` in `importoProdotti >= 100.0`
[( )] Cambiare `0.0` in `100.0`
[( )] Cambiare il simbolo `?` in `:`

**Domanda 2**

Con `importoProdotti = 45.00`, quale modifica produce 3.00 euro di supplemento express?

[(X)] Aggiungere `double supplemento = consegnaRapida ? 3.00 : 0.0;` e sommarlo alla spedizione
[( )] Sostituire la condizione con `consegnaRapida + 3.00`
[( )] Moltiplicare `speseSpedizione` per `consegnaRapida`

**Domanda 3**

Se sostituisci `0.0` con `0`, quale effetto corretto osservi?

[(X)] La scelta continua a funzionare e il risultato numerico è zero; `0.0` rende però esplicito il tipo decimale
[( )] Il ternario non compila perché il valore vero deve avere sempre due decimali
[( )] La condizione diventa automaticamente falsa

**Domanda 4**

Quale modifica stampa `"pari"` quando `articoli` vale 14?

[(X)] `std::cout << ((articoli % 2 == 0) ? "pari" : "dispari");`
[( )] `std::cout << ((articoli / 2 == 0) ? "pari" : "dispari");`
[( )] `std::cout << (articoli % 2 ? "pari" : "dispari");`

**Domanda 5**

Perché in Modify conviene cambiare una sola soglia o un solo valore alla volta?

[(X)] Per collegare ogni differenza nell’output alla modifica che l’ha provocata
[( )] Perché C++ permette una sola assegnazione per programma
[( )] Perché il ternario non può comparire due volte nello stesso file

Parti da questo scaffold:

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double importoProdotti = 85.00;
    double speseSpedizione =
        (importoProdotti >= 60.0) ? 0.0 : 6.50;
    std::cout << speseSpedizione << "\n";
    return 0;
}
```

</details>

**Modifica A — nuova soglia**  
Porta la soglia della spedizione gratuita a `100.0`. Cambia una sola parte,
ricompila e spiega perché ora compare il costo standard.

**Modifica B — consegna express**  
Aggiungi `bool consegnaRapida = true;`. Usa un ternario per calcolare un
supplemento di `3.00` se è vero e `0.0` altrimenti; somma il supplemento alla
spedizione.

**Modifica C — pari o dispari**  
Con `int articoli = 14;`, usa `%` e un ternario per stampare `"pari"` oppure
`"dispari"`.

#### 5. MAKE (Crea)

**Scenario aziendale — Commissione transazione POS**

Scrivi `commissioni_pos.cpp` per un esercente. I requisiti sono chiusi:

1. Dichiara `double importoPagamento = 45.00;`.
2. Dichiara `bool circuitoInternazionale = true;`.
3. Usa un ternario: circuito internazionale → aliquota `0.018`, altrimenti
   aliquota `0.007`.
4. Calcola la commissione; con un secondo ternario, se è minore di `0.15`,
   usa `0.15` come commissione finale.
5. Stampa commissione finale e incasso netto
   (`importoPagamento - commissioneFinale`) in un output leggibile.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double importoPagamento = 45.00;
    bool circuitoInternazionale = true;
    /// L'aliquota varia perché i circuiti applicano costi diversi.
    double aliquota = 0.0; // TODO: ternario sulle due aliquote
    double commissione = 0.0; // TODO: importo per aliquota
    double commissioneFinale = 0.0; // TODO: ternario sulla soglia minima
    double incassoNetto = 0.0; // TODO: importo meno commissione finale
    std::cout << "Commissione: " << commissioneFinale << " euro\n";
    std::cout << "Incasso netto: " << incassoNetto << " euro\n";
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Un'espressione produce un valore usando variabili, letterali e operatori.
- Tra soli `int`, `/` esegue una divisione intera: la parte decimale si perde.
- Un confronto come `totale >= 60.0` produce `true` o `false`.
- Il ternario ha la forma `condizione ? se_vero : se_falso` e restituisce un valore.
- Cambia una sola cosa alla volta: così colleghi l'output alla causa.

---

### ➡️ Prossimo chunk

Quando una scelta deve eseguire più istruzioni, una riga non basta più.
Nel prossimo chunk userai `if` / `else` per costruire un vero bivio nel
programma.

