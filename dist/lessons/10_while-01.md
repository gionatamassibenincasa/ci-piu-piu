<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-14
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/09_switch-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/11_for-01.md)

---


## 🔄 L'Anello Fondamentale (Il Ciclo `while`)

> "Iterare è umano, automatizzare è informatica."
> — *Adattamento da L. Peter Deutsch*

Quanti articoli ha un cliente al nastro della cassa? 3, 12, 75… non lo sai in anticipo.  
Con soli `if` e variabili fisse finiresti a dichiarare `prezzo1`, `prezzo2`, … sperando che bastino.

La potenza del computer sta nel **ripetere** lo stesso blocco **finché** una condizione resta vera.  
La forma più essenziale di questa ripetizione è il ciclo **`while`**.

> 💡 **Metafora: nastro della cassa**  
> - Finché c’è un articolo da scansionare (**condizione vera**), il nastro avanza e il totale cresce.  
> - Quando arriva il separatore con **valore sentinella** (es. `0`), la condizione diventa falsa: il rullo si ferma e si emette lo scontrino.  
> - Carrello vuoto già all’inizio → il nastro **non fa neppure un giro** (zero iterazioni).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un ciclo `while` che legge dati fino a una sentinella, aggiornando la condizione a ogni giro

---

### ⚙️ Prima del laboratorio: controllo in testa e tre ingredienti

Il `while` verifica la condizione **prima** di entrare nel corpo.

```cpp
// 1. Inizializzazione
double prezzo = 0.0;
std::cin >> prezzo;

// 2. Condizione di continuazione
while (prezzo != 0.0) {
    // corpo: accumula, conta, ...
    // 3. Aggiornamento (nuova lettura)
    std::cin >> prezzo;
}
```

| Ingrediente | Ruolo | Se manca… |
|-------------|-------|-----------|
| **Inizializzazione** | Valore di partenza *prima* del ciclo | Comportamento indefinito / non entra mai |
| **Condizione** | Decide se ripetere | Ciclo assente o infinito |
| **Aggiornamento** | Fa evolvere la variabile di controllo | **Ciclo infinito** |

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Inizializza variabile di controllo;
while (Condizione vera?) is (sì)
  :Corpo del ciclo;
  :Aggiorna variabile di controllo;
endwhile (no)
:Continua dopo il ciclo;
stop
@enduml
```

---

### 🧭 Prima del laboratorio: la sentinella ferma il nastro

La sentinella è un valore che non rappresenta un articolo: è il separatore
finale. Leggila prima del ciclo e alla fine di ogni giro, ma non sommarla mai.

| Valore letto | Il ciclo continua? | Va nel totale? |
|--------------|-------------------|----------------|
| `12.50` | sì | sì |
| `0.0` (sentinella) | no | no |

---

### 🔬 Laboratorio PRIMM: Scontrino a nastro

Accumuiamo i prezzi finché non arriva la sentinella di fine spesa.

#### 1. PREDICT (Prevedi)


Quante volte viene stampata la parola "Elaborazione"?

```cpp
int n = 0;
while (n > 5) {
    std::cout << "Elaborazione\n";
    n = n + 1;
}
```

[(X)] 0 volte (non viene mai stampata)
[( )] 1 volta
[( )] 5 volte
[( )] Il ciclo è infinito


<details>
<summary>💡 Spiegazione</summary>
All’ingresso <code>n > 5</code> è falso (<code>0 > 5</code>).  
Il <code>while</code> ha controllo in testa: se la condizione è già falsa, il corpo non viene eseguito mai.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scontrino_nastro.cpp
 * @brief Accumula i prezzi finché non arriva la sentinella 0.
 */
#include <iostream>

/**
 * @brief Legge prezzi da nastro (sentinella 0) e stampa totale e pezzi.
 * @return int 0 se ok.
 */
int main() {
    double totaleSpesa = 0.0;
    int numeroArticoli = 0;

    double prezzoArticolo = 0.0;
    std::cout << "Prezzo articolo (0 per terminare): ";
    std::cin >> prezzoArticolo;

    while (prezzoArticolo != 0.0) {
        totaleSpesa += prezzoArticolo;
        numeroArticoli += 1;
        std::cout << "  + " << prezzoArticolo << " EUR (pezzi: " << numeroArticoli << ")\n";

        std::cout << "Prezzo articolo (0 per terminare): ";
        std::cin >> prezzoArticolo;
    }

    std::cout << "=== SCONTRINO ===\n";
    std::cout << "Articoli: " << numeroArticoli << "\n";
    std::cout << "Totale  : " << totaleSpesa << " EUR\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Sequenza di esempio: `12.50` → `3.20` → `0.0`

| Iterazione | `prezzoArticolo` | Condizione | Totale dopo |
|------------|------------------|------------|-------------|
| ingresso | 12.50 | vero | 12.50 |
| 2ª | 3.20 | vero | 15.70 |
| 3ª lettura | 0.0 | **falso** → esce | 15.70 |

La sentinella `0` **non** viene sommata: il controllo avviene prima del corpo.

> 🔗 Osserva le variabili su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
double prezzoArticolo = 0.0;
std::cin >> prezzoArticolo;

while (prezzoArticolo != 0.0) {
    std::cin >> prezzoArticolo;
}
```

</details>

1. **Media per articolo**  
   Dopo il ciclo, se `numeroArticoli > 0`, stampa `totaleSpesa / numeroArticoli`.  
   Altrimenti messaggio “nessun articolo”.

2. **Scarta i negativi**  
   Se un prezzo è `< 0`, non accumularlo: stampa un avviso e continua.

3. **Ciclo infinito (esperimento controllato)**  
   Commenta l’aggiornamento di `prezzoArticolo` nel corpo.  
   La condizione resta vera per sempre → il programma non termina.  
   **Regola:** ogni ciclo deve aggiornare qualcosa che influisce sulla condizione.

#### 5. MAKE (Crea)
**Scenario SIA — Registro fatture fornitori**

Scrivi `fatture_fornitori.cpp`:

- Ciclo `while` che legge importi fattura
- Sentinella `-1.0` per terminare (**non** sommare la sentinella)
- Accumula `totaleDebiti`, conta fatture totali e quante sono “rilevanti” (`>= 1000`)
- A fine ciclo stampa:
  - totale debiti
  - numero fatture
  - numero rilevanti
  - percentuale rilevanti sul totale (se totale > 0)

**Requisiti:** Doxygen, `///` su contatori/accumulatori, sentinella gestita correttamente.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Registra fatture fornitori fino alla sentinella -1.
 */
#include <iostream>

int main() {
    // inizializza totali e contatori
    // leggi primo importo
    // while (importo != -1.0) { ... aggiorna ... leggi di nuovo }
    // stampa riepilogo
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `while` = ripeti **mentre** la condizione è vera (controllo in testa).
- Tre ingredienti: inizializza → controlla → aggiorna.
- Sentinella = valore speciale che dice “basta” (es. `0` o `-1`).
- Senza aggiornamento → ciclo infinito.
- Zero iterazioni è un comportamento normale se la condizione è già falsa.

---

### ➡️ Prossimo chunk
Quando sai già **quante** volte ripetere (es. 12 mesi, 30 giorni, 100 pezzi), il `while` funziona ma è verboso.  
Il ciclo **`for`** concentra inizializzazione, condizione e aggiornamento in una riga.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: while, sentinella, tre ingredienti, no infinito
  [x] Metafora nastro cassa
  [x] Quiz sintassi corretta
  [x] Predict: zero iterazioni
  [x] PRIMM scontrino (simulazione input per LiaScript)
  [x] Make fatture fornitori
  [x] for solo annunciato
-->
