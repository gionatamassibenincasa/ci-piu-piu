<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-24
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_formattazione-contabile-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/17_funzioni-01.md)

---


## 🧭 Un ruolo per ogni variabile, uno schema per ogni ciclo

In un gestionale molte parti del codice sembrano ripetizioni. In realtà ogni
variabile svolge un lavoro preciso: sommare, contare, conservare l'ultimo dato,
tenere il migliore trovato finora o confrontare lo stato precedente.

Riconoscere questi ruoli ti permette di leggere una soluzione già nota e
riutilizzare lo schema corretto invece di partire ogni volta da zero.

> 💡 **Metafora:**  
> Immagina una scrivania di controllo fatture. Il **contatore** annota quante
> righe sono state esaminate; l'**accumulatore** tiene il totale aperto; il
> **valore più recente** registra l'ultima fattura letta; il **valore più
> desiderato** conserva il massimo; il **precedente** serve a confrontare due
> fatture consecutive. La sentinella è il segnale rosso che chiude la serie.

**In questa lezione non** introduciamo funzioni, array o puntatori. I pattern
sono applicati a dati letti in sequenza con `while`, `for`, `if` e `do-while`.

---

### 🎯 Obiettivi di apprendimento

Alla fine di questa lezione sei in grado di:

- assegnare un ruolo osservabile a variabili che accumulano, contano, conservano il valore recente o scelgono un massimo;
- riconoscere uno schema di ciclo con sentinella, accumulo, filtro o confronto adiacente;
- tracciare i valori delle variabili prima e dopo ogni iterazione;
- adattare uno schema noto a un problema gestionale diverso.

---

### ⚙️ Prima del laboratorio: ruoli e pattern

| Ruolo | Domanda guida | Aggiornamento tipico |
| :--- | :--- | :--- |
| Valore fissato | Quale dato resta invariato durante la sequenza? | `const` o inizializzazione |
| Contatore | Quante volte o quanti elementi sono stati osservati? | `++numero` |
| Accumulatore | Qual è il risultato aggregato finora? | `totale += importo` |
| Valore più recente | Qual è stato l'ultimo dato letto? | assegnazione dalla lettura |
| Valore più desiderato | Qual è il massimo o il minimo finora? | aggiornamento condizionale |
| Precedente | Quale valore è stato letto nel passo precedente? | salva dopo il confronto |
| Flag unidirezionale | Qualcosa è accaduto almeno una volta? | da `false` a `true` |

I pattern non sono nuovi costrutti: sono combinazioni ricorrenti di variabili
e istruzioni già conosciute.

| Pattern | Controllo del ciclo | Stato principale |
| :--- | :--- | :--- |
| Conteggio noto | `for` con un contatore | contatore / accumulatore |
| Scansione fino a sentinella | `while` finché il dato non è speciale | valore più recente |
| Accumulazione | ciclo + aggiornamento dipendente dallo stato precedente | accumulatore |
| Filtro e conteggio | ciclo + `if` | contatore filtrato |
| Selezione dell'estremo | ciclo + confronto condizionale | valore più desiderato |
| Confronto adiacente | ciclo + dato precedente | precedente |
| Ricerca lineare | ciclo + arresto o flag | trovato / indice |

---

### 🧭 Prima del laboratorio: stato per stato

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Inizializza totale, numero, massimo;
:Leggi il primo importo;
while (importo != sentinella?) is (sì)
  :Aggiorna totale;
  :Conta la fattura;
  if (è il primo o è maggiore del massimo?) then (sì)
    :Aggiorna massimo;
  endif
  :Leggi il prossimo importo;
endwhile (no)
:Stampa il riepilogo;
stop
@enduml
```

L'ordine delle inizializzazioni è parte del pattern. Un accumulatore deve partire
da zero prima del ciclo; un massimo può partire dal primo dato valido o usare
una condizione esplicita con la bandiera `primo`.

---

### 🔬 Laboratorio PRIMM: Registro fatture fornitore

Il programma legge importi fino alla sentinella `-1.0`. Per ogni fattura registra
il totale, il numero dei dati validi e il massimo ricevuto finora.

#### 1. PREDICT (Prevedi)

```cpp
double totale = 0.0;
double massimo = 0.0;
int numero = 0;
double importo;
bool primo = true;

std::cin >> importo;
while (importo != -1.0) {
    totale += importo;
    ++numero;
    if (primo || importo > massimo) {
        massimo = importo;
        primo = false;
    }
    std::cin >> importo;
}
```

**Domanda 1**

Quale ruolo ha `totale` nel codice?

[( )] Contatore: cambia un passo alla volta indipendentemente dagli importi
[(X)] Accumulatore: dipende dal suo valore precedente e da ogni nuovo importo
[( )] Sentinella: indica con quale valore termina il ciclo

**Domanda 2**

Perché `numero` viene incrementato con `++numero`?

[( )] È un accumulatore: somma gli importi inseriti
[(X)] È un contatore: conta quante fatture valide sono state elaborate
[( )] È una sentinella: termina il ciclo quando arriva a meno uno

**Domanda 3**

Quale ruolo ha `importo` prima di ogni lettura?

[(X)] Valore più recente: conserva l'ultimo dato letto
[( )] Valore fissato: non può cambiare dopo l'inizializzazione
[( )] Precedente: conserva sempre il dato letto due passi fa

**Domanda 4**

Perché `massimo` cambia solo in alcuni passaggi?

[(X)] È un valore più desiderato: conserva il candidato migliore trovato finora
[( )] È un contatore: avanza fino al limite della sequenza
[( )] È un accumulatore: somma tutti i valori confrontati

**Domanda 5**

Che cosa rende questo ciclo uno schema di scansione fino a sentinella?

[( )] `primo` viene controllato solo una volta
[( )] Il ciclo usa un numero fisso di iterazioni
[(X)] `-1.0` termina la lettura e non viene elaborato come fattura

Prima di eseguire, indovina il ruolo di ogni variabile; non limitarti a
prevedere il risultato numerico.

#### 2. RUN (Esegui)

Digita il programma completo e prova con `120.0`, `80.0`, `150.0`, `-1.0`.

```cpp
/**
 * @file registro_fatture.cpp
 * @brief Analizza una sequenza di fatture fino alla sentinella -1.0.
 * @return int 0 se il programma termina correttamente.
 */
#include <iostream>

int main() {
    /// Il totale aggrega solo gli importi letti prima della sentinella.
    double totale = 0.0;
    /// Il contatore registra il numero di fatture valide.
    int numero = 0;
    /// Il massimo viene aggiornato solo quando trova un candidato migliore.
    double massimo = 0.0;
    double importo = 0.0;
    bool primo = true;

    std::cout << "Importo fattura (-1 per terminare): ";
    std::cin >> importo;

    while (importo != -1.0) {
        totale += importo;
        ++numero;

        if (primo || importo > massimo) {
            massimo = importo;
            primo = false;
        }

        std::cout << "Importo fattura (-1 per terminare): ";
        std::cin >> importo;
    }

    std::cout << "Totale: " << totale << " euro\n";
    std::cout << "Numero fatture: " << numero << "\n";
    std::cout << "Massimo: " << massimo << " euro\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

Dopo il Run, confronta stato e ruolo di ogni variabile.

```cpp
double totale = 0.0;
double massimo = 0.0;
int numero = 0;
double importo;
bool primo = true;

std::cin >> importo;
while (importo != -1.0) {
    totale += importo;
    ++numero;
    if (primo || importo > massimo) {
        massimo = importo;
        primo = false;
    }
    std::cin >> importo;
}
```

**Domanda 1**

Con input `120.0`, `80.0`, `-1.0`, quale stato assume `totale` alla fine?

[( )] `-1.0`, perché è l'ultimo valore letto
[( )] `201.0`, perché vengono conteggiati due dati e la sentinella
[(X)] `200.0`, perché la sentinella non viene sommata

**Domanda 2**

Perché `massimo` vale `120.0` dopo i due importi?

[( )] Il ciclo sostituisce sempre il massimo con il dato successivo
[(X)] Il primo importo lo inizializza e il secondo non lo supera
[( )] Il contatore `numero` restituisce direttamente il valore massimo

**Domanda 3**

Che cosa accade se sposti `totale = 0.0` dentro il ciclo?

[(X)] Ogni importo cancella il totale precedente e il risultato finale è incompleto
[( )] Il totale viene sommato una volta in più alla fine
[( )] La sentinella viene contata come fattura

**Domanda 4**

Perché `primo` è una bandiera unidirezionale utile in questo esempio?

[( )] Deve tornare vera dopo ogni nuovo massimo
[( )] Serve a sommare due volte il primo importo
[(X)] Serve solo finché il primo candidato non è stato fissato

**Domanda 5**

Quale schema descrive meglio il ciclo completo?

[( )] Ricerca certa dopo un ordinamento
[(X)] Scansione fino a sentinella con accumulo e selezione del massimo
[( )] Scansione con conteggio noto tramite `for`

| Input | `totale` | `numero` | `massimo` | Ruolo visibile |
| :---: | :---: | :---: | :---: | :--- |
| `120.0` | `120.0` | `1` | `120.0` | primo candidato |
| `80.0` | `200.0` | `2` | `120.0` | accumulo + massimo invariato |
| `150.0` | `350.0` | `3` | `150.0` | nuovo valore più desiderato |
| `-1.0` | `350.0` | `3` | `150.0` | sentinella, non elaborata |

Apri il programma in [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva in quale momento `totale`, `numero`, `massimo` e `primo` cambiano.

#### 4. MODIFY (Modifica)

Prima di modificare, usa il quiz per prevedere la nuova organizzazione dello stato.

```cpp
double totale = 0.0;
double massimo = 0.0;
int numero = 0;
double importo;
bool primo = true;
```

**Domanda 1**

Quale modifica conta solo le fatture almeno pari a 100 euro?

[( )] Cambiare la sentinella da `-1.0` a `100.0`
[( )] Aumentare `massimo` dentro ogni iterazione
[(X)] Dentro il ciclo, usare `if (importo >= 100.0)` prima di totale e contatore

**Domanda 2**

Quale modifica trasforma il valore massimo in minimo mantenendo il primo candidato?

[( )] Dichiarare `minimo` dentro il ciclo
[( )] Sostituire la sentinella con `0.0`
[(X)] Confrontare `importo < minimo` e aggiornare il minimo nel ramo vero

**Domanda 3**

Come puoi tracciare una diminuzione rispetto all'importo precedente?

[(X)] Mantenere `precedente`, confrontare `importo < precedente` e aggiornarlo alla fine
[( )] Usare `massimo` al posto di `precedente` senza aggiornamenti
[( )] Sommare `precedente` al totale ad ogni giro

**Domanda 4**

Quale modifica rende `trovato` vero una sola volta senza annullarlo nei successivi giri?

[( )] Porre `trovato = false` dopo ogni importo valido
[(X)] Usare `if (importo >= soglia) trovato = true;` senza assegnazioni false successive
[( )] Azzerare `trovato` appena la sentinella viene letta

**Domanda 5**

Perché conviene modificare una sola parte del tracciare?

[(X)] Per collegare il nuovo stato osservato al ruolo modificato: accumulatore, massimo o precedente
[( )] Perché il compilatore accetta al massimo un aggiornamento per prova
[( )] Perché una sola variabile può esistere in un ciclo

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double totale = 0.0;
    double massimo = 0.0;
    int numero = 0;
    double importo = 0.0;
    bool primo = true;

    // TODO: leggi fino a -1.0
    // TODO: aggiorna totale, numero e massimo
    // TODO: stampa il riepilogo
    return 0;
}
```

</details>

**Modifica A — filtro sulle fatture rilevanti**

Conta e somma solo gli importi almeno pari a `100.0`. Il massimo deve essere
calcolato sugli stessi dati filtrati.

**Modifica B — minimo invece di massimo**

Trasforma il valore più desiderato in un minimo. Mantieni la bandiera `primo`
finché non hai osservato il primo candidato.

**Modifica C — confronto tra fatture adiacenti**

Aggiungi `double precedente = 0.0;` e un contatore delle diminuzioni
consecutive. Aggiorna `precedente` solo dopo aver confrontato l'importo
corrente.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio fornitori controlla una sequenza di fatture
senza sapere in anticipo quante righe saranno inserite.

Crea `registro_fatture.cpp` rispettando tutti i requisiti:

1. Leggi importi finché l'utente inserisce `-1.0`.
2. Non sommare né conteggiare la sentinella.
3. Usa un accumulatore per il totale.
4. Usa un contatore per il numero di fatture valide.
5. Usa un valore più desiderato per conservare il massimo.
6. Usa un precedente per riconoscere una diminuzione rispetto alla fattura precedente.
7. Conta quante diminuzioni consecutive sono state rilevate.
8. Stampa totale, numero, massimo e numero di diminuzioni.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Riassume importi fatture con accumulo e confronto adiacente.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché la sentinella non rappresenta una fattura.
    // TODO: inizializza totale, numero, massimo, precedente e lettura
    // TODO: scansione fino a -1.0
    // TODO: aggiorna i ruoli e stampa il riepilogo
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- [ ] Valore fissato, contatore e accumulatore hanno responsabilita diverse.
- [ ] Il valore più recente conserva l'ultimo dato letto.
- [ ] Il valore più desiderato viene aggiornato solo da un candidato migliore.
- [ ] Il precedente serve a confrontare dati adiacenti.
- [ ] Un accumulatore si inizializza fuori dal ciclo e viene aggiornato dentro.
- [ ] Una sentinella termina la scansione e non viene elaborata.
- [ ] Chiamare una sequenza con il suo pattern rende il codice leggibile e prevedibile.

---

### ➡️ Prossimo passo nel percorso

Ora sai riconoscere il ruolo di ogni variabile e scegliere uno schema di ciclo.
Nel prossimo capitolo del percorso Fondamenti, `17_funzioni_scomposizione_top_down`,
metterai questa capacità dentro reparti software riutilizzabili: le funzioni.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_formattazione-contabile-01.md">Lezione precedente (15 — La stampante fiscale: formattare importi con `<iomanip>`)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/17_funzioni-01.md">Lezione successiva (17 — Il Primo Reparto: funzioni che restituiscono un valore)</a>
