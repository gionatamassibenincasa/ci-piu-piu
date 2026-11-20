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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/09_switch-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/11_for-01.md)

---


## 🔄 Il nastro della cassa: ripetere con il ciclo `while`

Quanti articoli ha un cliente? Tre, dodici, settantacinque: spesso non lo sai
prima di iniziare. Con variabili separate dovresti preparare `prezzo1`,
`prezzo2`, `prezzo3` e sperare che bastino.

Il ciclo `while` permette di ripetere lo stesso blocco finché una condizione
rimane vera.

> 💡 **Metafora:** Immagina il nastro della cassa. Finché arriva un articolo,
> il nastro avanza e il totale cresce. Quando arriva il separatore con valore
> sentinella, il nastro si ferma e viene emesso lo scontrino. Se il carrello è
> già vuoto all'inizio, il nastro non fa neppure un giro.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un ciclo `while` che legge dati fino a una sentinella e aggiorna la condizione a ogni giro.

---

### ⚙️ Prima del laboratorio: i tre ingredienti

Il `while` controlla la condizione **prima** di entrare nel corpo:

```cpp
double prezzo = 0.0;
std::cin >> prezzo;

while (prezzo != 0.0) {
    totale = totale + prezzo;
    std::cin >> prezzo;
}
```

| Ingrediente | Ruolo | Se manca |
| :--- | :--- | :--- |
| Inizializzazione | Prepara il valore prima del ciclo | La condizione parte da uno stato imprevedibile |
| Condizione | Decide se entrare e ripetere | Il corpo non sa quando fermarsi |
| Aggiornamento | Cambia il valore controllato | Può nascere un ciclo infinito |

Una sentinella è un valore speciale che indica “basta”. Non è un dato da
elaborare, quindi non deve entrare nel totale.

---

### 🧭 Prima del laboratorio: controllo in testa

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi il primo prezzo;
while (prezzo != sentinella?) is (sì)
  :Somma il prezzo;
  :Incrementa il contatore;
  :Leggi il prezzo successivo;
endwhile (no)
:Stampa il riepilogo;
stop
@enduml
```

Con input `12.50`, `3.20`, `0.0`:

| Valore letto | Condizione | Azione |
| :---: | :---: | :--- |
| `12.50` | vera | Somma e conta |
| `3.20` | vera | Somma e conta |
| `0.0` | falsa | Ferma il ciclo, non sommare |

---

### 🔬 Laboratorio PRIMM: scontrino a nastro

Accumula i prezzi finché l'utente inserisce `0.0`, la sentinella di fine
spesa.

#### 1. PREDICT (Prevedi)

```cpp
int n = 0;

while (n > 5) {
    std::cout << "Elaborazione\n";
    n = n + 1;
}
```

**Domanda 1**

Quante volte viene stampata la parola `Elaborazione`?

[(X)] Zero volte, perché la condizione `0 > 5` è falsa già all'inizio
[( )] Una volta, perché ogni `while` esegue almeno un giro
[( )] Cinque volte, perché il ciclo arriva fino a 5

**Domanda 2**

Perché il corpo del `while` non viene eseguito in questo esempio?

[(X)] Il `while` controlla la condizione prima di entrare nel corpo
[( )] La stampa dentro il ciclo è vietata
[( )] La variabile `n` viene automaticamente cancellata

**Domanda 3**

Quale ruolo ha `n = n + 1;` dentro il ciclo?

[(X)] Fa evolvere la variabile che può rendere falsa la condizione
[( )] Riporta sempre `n` al valore iniziale
[( )] Decide da sola quale testo stampare

**Domanda 4**

Quale elemento serve per fermare un ciclo che legge articoli fino a `0`?

[(X)] Un valore sentinella e una condizione che lo riconosce
[( )] Un `switch` dentro ogni iterazione
[( )] Una costante che deve essere sempre uguale a 1

**Domanda 5**

Perché un `while` può eseguire zero iterazioni?

[(X)] La condizione può essere falsa prima del primo ingresso nel corpo
[( )] Il compilatore sceglie casualmente se saltare il primo giro
[( )] Un ciclo esegue il corpo solo quando contiene `std::cin`

#### 2. RUN (Esegui)

Digita il programma completo. Inserisci uno o più prezzi e termina con `0`.

```cpp
/**
 * @file scontrino_nastro.cpp
 * @brief Accumula prezzi fino alla sentinella 0.0.
 */
#include <iostream>

/**
 * @brief Legge gli articoli e stampa totale e numero di pezzi.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il totale raccoglie solo i prezzi validi dello scontrino.
    double totaleSpesa = 0.0;
    /// Il contatore serve a descrivere quante righe sono state registrate.
    int numeroArticoli = 0;
    double prezzoArticolo = 0.0;

    std::cout << "Prezzo articolo (0 per terminare): ";
    std::cin >> prezzoArticolo;

    while (prezzoArticolo != 0.0) {
        totaleSpesa = totaleSpesa + prezzoArticolo;
        numeroArticoli = numeroArticoli + 1;
        std::cout << "Prezzo articolo (0 per terminare): ";
        std::cin >> prezzoArticolo;
    }

    std::cout << "=== SCONTRINO ===\n";
    std::cout << "Articoli: " << numeroArticoli << "\n";
    std::cout << "Totale: " << totaleSpesa << " EUR\n";
    return 0;
}
```
@LIA.cpp

Prova con:

```text
12.50
3.20
0
```

Il totale deve essere `15.70`: lo `0` serve a fermare il ciclo e non è un
prezzo.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine delle letture e degli aggiornamenti.

```cpp
double totaleSpesa = 0.0;
int numeroArticoli = 0;
double prezzoArticolo = 12.50;

while (prezzoArticolo != 0.0) {
    totaleSpesa = totaleSpesa + prezzoArticolo;
    numeroArticoli = numeroArticoli + 1;
    prezzoArticolo = 0.0;
}
```

**Domanda 1**

Quale condizione permette al ciclo di entrare nel corpo al primo controllo?

[(X)] `12.50 != 0.0`, che è vera
[( )] `0.0 != 12.50`, che viene controllata dopo il corpo
[( )] La condizione non viene controllata al primo giro

**Domanda 2**

Perché dopo il giro il totale vale `12.50`?

[(X)] Il prezzo viene sommato prima che la variabile sia aggiornata a `0.0`
[( )] Il ciclo aggiunge sempre due volte il primo prezzo
[( )] La sentinella `0.0` viene conteggiata come prezzo

**Domanda 3**

Perché il secondo controllo non entra nel corpo?

[(X)] L'aggiornamento porta `prezzoArticolo` alla sentinella e rende falsa la condizione
[( )] Il ciclo si ferma dopo un giro indipendentemente dalla condizione
[( )] Il totale non può essere aggiornato più di una volta

**Domanda 4**

Quale valore non deve essere sommato in un ciclo con sentinella `0.0`?

[(X)] La sentinella `0.0`, perché serve solo a indicare la fine
[( )] Ogni prezzo maggiore di zero
[( )] Il primo prezzo valido inserito

**Domanda 5**

Che cosa rischi se rimuovi l'aggiornamento di `prezzoArticolo`?

[(X)] La condizione può restare vera e il ciclo può diventare infinito
[( )] Il ciclo esegue automaticamente il ramo `else`
[( )] La variabile diventa subito uguale alla sentinella

| Momento | `prezzoArticolo` | Condizione | Totale |
| :--- | :---: | :---: | :---: |
| Primo controllo | `12.50` | vera | `0.00` |
| Dopo il primo corpo | `3.20` | prossimo controllo | `12.50` |
| Dopo il secondo corpo | `0.0` | prossimo controllo falsa | `15.70` |
| Uscita | `0.0` | falsa | `15.70` |

Il controllo è in testa: quando il valore è `0.0`, il corpo non viene più
eseguito. Se rimuovi la nuova lettura dentro il ciclo, `prezzoArticolo` resta
uguale e la condizione può rimanere vera per sempre.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva prezzo, totale
> e contatore a ogni iterazione.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
double prezzoArticolo = 12.50;
double totaleSpesa = 0.0;

while (prezzoArticolo != 0.0) {
    totaleSpesa = totaleSpesa + prezzoArticolo;
    std::cin >> prezzoArticolo;
}
```

**Domanda 1**

Quale modifica permette di contare anche il numero degli articoli?

[(X)] Dichiarare un contatore e incrementarlo dentro il corpo, prima della nuova lettura
[( )] Aggiungere il contatore dopo il ciclo senza aggiornarlo
[( )] Sostituire `while` con `switch`

**Domanda 2**

Dove devi inserire la nuova lettura se vuoi continuare a chiedere prezzi?

[(X)] Nel corpo del ciclo, così la condizione può cambiare al giro successivo
[( )] Solo prima del `while`, perché il corpo non può leggere dati
[( )] Dopo `return 0`, quando il programma è già terminato

**Domanda 3**

Che cosa succede se cambi la sentinella da `0.0` a `-1.0`?

[(X)] Il ciclo continua finché il prezzo non diventa `-1.0`, che non viene sommato
[( )] Il ciclo termina sempre dopo il primo prezzo positivo
[( )] Il valore `-1.0` viene automaticamente trasformato in `0.0`

**Domanda 4**

Quale modifica evita di sommare un prezzo negativo ma permette di continuare?

[(X)] Aggiungere un controllo nel corpo e aggiornare comunque il prossimo prezzo
[( )] Usare `-1.0` come totale iniziale
[( )] Mettere la lettura del prezzo fuori da `main`

**Domanda 5**

Perché conviene modificare una sola parte del ciclo alla volta?

[(X)] Per distinguere se l'errore riguarda condizione, corpo o aggiornamento
[( )] Perché un `while` può contenere una sola istruzione
[( )] Perché il compilatore impedisce di cambiare due righe consecutive

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
double prezzoArticolo = 0.0;
std::cin >> prezzoArticolo;

while (prezzoArticolo != 0.0) {
    totaleSpesa = totaleSpesa + prezzoArticolo;
    std::cin >> prezzoArticolo;
}
```

</details>

**Modifica A — conta gli articoli**

Dichiara `int numeroArticoli = 0` prima del ciclo e incrementalo dentro il
corpo, insieme al totale. La sentinella non deve aumentare il contatore.

**Modifica B — calcola la media**

Dopo il ciclo, se `numeroArticoli > 0`, calcola
`totaleSpesa / numeroArticoli`. Per ora puoi usare un `if` semplice per evitare
la divisione quando non è stato inserito alcun articolo.

**Modifica C — cambia sentinella**

Sostituisci `0.0` con `-1.0` in tutti i punti necessari. Il ciclo deve fermarsi
solo con `-1.0`, che non va sommato.

**Esperimento controllato — ciclo infinito**

Commenta temporaneamente la nuova lettura nel corpo. Il programma non riceverà
più un valore capace di fermare la condizione: interrompilo e ripristina la
lettura.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio amministrativo registra le fatture dei
fornitori fino alla fine dell'importazione.

Crea `fatture_fornitori.cpp` rispettando tutti i requisiti:

1. Usa `double importo` e la sentinella `-1.0`.
2. Leggi il primo importo prima del `while`.
3. Continua finché `importo != -1.0`.
4. Non sommare la sentinella.
5. Accumula `totaleDebiti`.
6. Conta tutte le fatture e quelle rilevanti, con importo almeno `1000.0`.
7. Stampa totale, numero fatture e numero rilevanti.
8. Inserisci un commento `///` che spieghi perché la sentinella non è una fattura.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Registra fatture fornitori fino alla sentinella -1.0.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché la sentinella non deve entrare nel totale.
    // TODO: inizializza totale e contatori, leggi il primo importo.
    // TODO: scrivi il while e stampa il riepilogo.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `while` ripete il corpo mentre la condizione è vera.
- Il controllo è in testa: sono possibili zero iterazioni.
- Ogni ciclo ha inizializzazione, condizione e aggiornamento.
- Una sentinella ferma il ciclo e non va elaborata.
- Senza aggiornamento della variabile controllata può nascere un ciclo infinito.

---

### ➡️ Prossimo chunk

Quando sai già quante volte ripetere, per esempio dodici mesi o trenta righe,
`while` può diventare verboso. Nel prossimo capitolo userai `for` per raccogliere
inizializzazione, condizione e aggiornamento in una sola riga.

