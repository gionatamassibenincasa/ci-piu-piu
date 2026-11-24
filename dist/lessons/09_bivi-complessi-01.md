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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/08_if-else-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/10_switch-01.md)

---


## 🌲 Scaglioni ordinati: `if`, `else if` ed `else`

Nel capitolo precedente hai imparato a scegliere tra due strade. Nei contesti
aziendali, però, le alternative possono essere più di due: fasce di sconto,
livelli di fido, classi di rischio o aliquote didattiche.

Una catena `if / else if / else` permette di controllare più fasce in ordine e
di sceglierne una sola.

> 💡 **Metafora:** Immagina un nastro di smistamento logistico. Ogni sensore
> controlla una soglia; il primo sensore che riconosce il pacco lo devia verso
> la sua corsia. I sensori successivi non vedono più quel pacco: per questo
> l'ordine delle soglie decide il risultato.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere una catena `if / else if / else` ordinata per classificare un dato in fasce esclusive.

---

### ⚙️ Prima del laboratorio: la scala delle fasce

```cpp
if (fatturato >= 50000.0) {
    sconto = 0.15;
} else if (fatturato >= 20000.0) {
    sconto = 0.10;
} else if (fatturato >= 5000.0) {
    sconto = 0.05;
} else {
    sconto = 0.0;
}
```

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| Primo `if` | Controlla la soglia più alta | Protegge la fascia più restrittiva |
| `else if` | Prova la soglia successiva solo se prima era falsa | Aggiunge un'alternativa |
| Ultimo `else` | Gestisce tutti i valori rimasti | Evita casi senza classificazione |
| Primo ramo vero | Ferma la catena | Le fasce sono esclusive |

Con soglie `>= 50000`, `>= 20000` e `>= 5000`, l'ordine corretto è dal valore
più alto al più basso. Un cliente con fatturato `60000` deve essere classificato
Platinum, non fermarsi prima nella fascia Gold.

---

### 🧭 Prima del laboratorio: seguire il flusso

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi fatturato;
if (fatturato >= 50000?) then (sì)
  :Platinum;
elseif (fatturato >= 20000?) then (sì)
  :Gold;
elseif (fatturato >= 5000?) then (sì)
  :Silver;
else (no)
  :Nessuna fascia;
endif
:Stampa il risultato;
stop
@enduml
```

Il programma non cerca “tutte le condizioni vere”: cerca il primo ramo vero.
Questo rende la catena adatta a classificazioni in cui ogni dato deve ricevere
una sola fascia.

---

### 🔬 Laboratorio PRIMM: fasce sconto cliente

Un gestionale assegna una fascia sconto in base al fatturato annuale di un
cliente.

#### 1. PREDICT (Prevedi)

```cpp
double fatturato = 25000.0;

if (fatturato >= 50000.0) {
    std::cout << "Platinum\n";
} else if (fatturato >= 20000.0) {
    std::cout << "Gold\n";
} else if (fatturato >= 5000.0) {
    std::cout << "Silver\n";
} else {
    std::cout << "Nessuna fascia\n";
}
```

**Domanda 1**

Quale fascia viene scelta con `fatturato = 25000.0`?

[( )] Silver, perché il programma sceglie sempre l'ultima condizione vera
[( )] Platinum, perché ogni valore positivo entra nella fascia più alta
[(X)] Gold, perché il fatturato non raggiunge 50000 ma supera 20000

**Domanda 2**

Perché la soglia `50000.0` deve essere controllata prima di `20000.0`?

[( )] Le soglie più piccole non possono essere scritte dopo quelle grandi
[(X)] Un fatturato di 60000 deve fermarsi nella fascia Platinum prima di raggiungere Gold
[( )] Il compilatore esegue sempre le condizioni dall'alto verso il basso numerico

**Domanda 3**

Che cosa succede dopo che una condizione della catena risulta vera?

[(X)] Viene eseguito quel ramo e le condizioni successive vengono saltate
[( )] Il programma torna alla prima condizione per controllarla di nuovo
[( )] Vengono eseguiti anche tutti gli `else if` successivi

**Domanda 4**

Quale ruolo ha l'ultimo `else` nella scala?

[( )] Rende vere tutte le condizioni precedenti
[(X)] Gestisce il caso in cui nessuna soglia precedente sia stata raggiunta
[( )] Ripete il controllo della soglia più alta

**Domanda 5**

Perché le fasce di sconto sono un buon esempio di `else if`?

[( )] Le fasce non hanno bisogno di confronti tra numeri
[(X)] Un cliente deve ricevere una sola fascia tra quelle definite
[( )] Ogni cliente deve ricevere tutti gli sconti contemporaneamente

#### 2. RUN (Esegui)

Digita il programma completo e confronta la fascia ottenuta con la tua
previsione.

```cpp
/**
 * @file fasce_sconto_cliente.cpp
 * @brief Classifica un cliente in una fascia sconto esclusiva.
 */
#include <iostream>
#include <string>

/**
 * @brief Assegna una fascia in base al fatturato annuale.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il nome identifica il cliente nel prospetto aziendale.
    std::string ragioneSociale = "Alpha Logistica Srl";
    /// Il fatturato decide la fascia commerciale.
    double fatturato = 32500.0;
    double sconto = 0.0;
    std::string fascia = "Nessuna";

    if (fatturato >= 50000.0) {
        sconto = 0.15;
        fascia = "Platinum";
    } else if (fatturato >= 20000.0) {
        sconto = 0.10;
        fascia = "Gold";
    } else if (fatturato >= 5000.0) {
        sconto = 0.05;
        fascia = "Silver";
    } else {
        sconto = 0.0;
        fascia = "Nessuna";
    }

    std::cout << "Cliente: " << ragioneSociale << "\n";
    std::cout << "Fatturato: " << fatturato << " euro\n";
    std::cout << "Fascia: " << fascia << "\n";
    std::cout << "Sconto: " << sconto * 100 << "%\n";
    return 0;
}
```
@LIA.cpp

Con `fatturato = 32500.0` il programma stampa la fascia Gold e lo sconto del
10%.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine dei confronti e spiega perché Silver non
viene più controllata dopo Gold.

```cpp
double fatturato = 32500.0;
double sconto = 0.0;

if (fatturato >= 50000.0) {
    sconto = 0.15;
} else if (fatturato >= 20000.0) {
    sconto = 0.10;
} else if (fatturato >= 5000.0) {
    sconto = 0.05;
} else {
    sconto = 0.0;
}
```

**Domanda 1**

Qual è il primo confronto eseguito con `fatturato = 32500.0`?

[(X)] `32500.0 >= 50000.0`, che risulta falso
[( )] `32500.0 >= 5000.0`, perché è la soglia più vicina
[( )] Il programma confronta tutte le soglie nello stesso momento

**Domanda 2**

Perché il valore finale di `sconto` è `0.10`?

[( )] Il valore iniziale 0.0 viene trasformato automaticamente in 0.10
[( )] Tutte le percentuali vengono sommate e il risultato diventa 0.10
[(X)] La prima condizione è falsa e la seconda è vera, quindi il ramo Gold assegna 0.10

**Domanda 3**

Quale ordine di verifica è corretto per `fatturato = 32500.0`?

[( )] Silver vero → Gold vero → Platinum falso
[( )] Gold vero → Silver vero → `else` eseguito
[(X)] Platinum falso → Gold vero → Silver e `else` saltati

**Domanda 4**

Che cosa accade se il fatturato vale `3000.0`?

[(X)] Tutte le soglie sono false e viene eseguito l'ultimo `else`
[( )] Il programma non esegue nessuna istruzione della catena, compreso `else`
[( )] Viene scelta Silver perché è la fascia più bassa

**Domanda 5**

Perché mettere `fatturato >= 20000.0` prima di `fatturato >= 50000.0` crea un errore logico?

[( )] La condizione 50000 diventerebbe automaticamente falsa
[(X)] Un fatturato di 60000 soddisfa subito 20000 e viene classificato Gold
[( )] Il compilatore rifiuta sempre le soglie scritte in ordine crescente

| Passo | Condizione | Esito | Azione |
| :---: | :--- | :---: | :--- |
| 1 | `32500 >= 50000` | falso | Passa a `else if` |
| 2 | `32500 >= 20000` | vero | Assegna Gold e `0.10` |
| 3 | `32500 >= 5000` | non controllata | La catena è già conclusa |
| 4 | `else` | non controllato | Esiste solo come alternativa finale |

Prova a cambiare `fatturato` in `3000.0`: tutte le soglie sono false e viene
scelta la fascia Nessuna. Prova poi `60000.0`: la prima condizione è vera e la
catena si ferma subito su Platinum.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva il percorso
> della condizione fino al primo ramo vero.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
if (fatturato >= 50000.0) {
    fascia = "Platinum";
} else if (fatturato >= 20000.0) {
    fascia = "Gold";
} else {
    fascia = "Nessuna";
}
```

**Domanda 1**

Quale modifica aggiunge una fascia Diamond per fatturati da `100000.0` in su?

[( )] Sostituire `else if` con un secondo `else`
[( )] Aggiungere Diamond dopo l'ultimo `else`
[(X)] Inserire un nuovo `if (fatturato >= 100000.0)` prima del controllo Platinum

**Domanda 2**

Che effetto ha mettere il controllo `>= 20000.0` prima di `>= 50000.0`?

[( )] Il programma corregge automaticamente l'ordine
[(X)] I valori da 50000 in su vengono intercettati troppo presto e classificati Gold
[( )] Le due fasce vengono assegnate insieme

**Domanda 3**

Quale modifica assegna Silver anche al valore esattamente uguale a `5000.0`?

[( )] Spostare Silver nel ramo `else` senza una condizione
[(X)] Usare `fatturato >= 5000.0` nella condizione Silver
[( )] Usare `fatturato > 5000.0` nella condizione Silver

**Domanda 4**

Quale modifica calcola l'importo dello sconto dopo aver scelto la fascia?

[( )] Moltiplicare ogni soglia prima di sapere quale ramo è vero
[( )] Usare `std::cin` al posto della variabile `sconto`
[(X)] Moltiplicare il fatturato per `sconto` dopo la catena

**Domanda 5**

Perché conviene modificare una soglia alla volta?

[(X)] Per capire quale cambiamento ha alterato la classificazione ai confini
[( )] Perché `else if` funziona soltanto con valori non decimali
[( )] Perché una catena può contenere una sola soglia in assoluto

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
if (fatturato >= 50000.0) {
    fascia = "Platinum";
} else if (fatturato >= 20000.0) {
    fascia = "Gold";
} else {
    fascia = "Nessuna";
}
```

</details>

**Modifica A — aggiungi Diamond**

Inserisci una fascia `Diamond` per fatturati almeno pari a `100000.0`.
Controllala prima di Platinum e verifica con `120000.0`.

**Modifica B — osserva l'ordine sbagliato**

Sposta temporaneamente il controllo Gold prima di Platinum. Prova con
`60000.0` e osserva perché il cliente viene classificato Gold.

**Modifica C — prova il confine**

Imposta il fatturato a `5000.0`. Verifica che la condizione `>=` includa il
valore esattamente uguale alla soglia Silver.

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio amministrativo prepara un prospetto
semplificato dell'imposta per una ditta.

Crea `imposte_reddito.cpp` rispettando tutti i requisiti:

1. Dichiara `std::string nomeDitta` e `double redditoImponibile`.
2. Usa una catena `if / else if / else`.
3. Usa queste fasce didattiche con aliquota unica:
   - fino a `15000`: `23%`;
   - fino a `28000`: `25%`;
   - fino a `50000`: `35%`;
   - oltre `50000`: `43%`.
4. Controlla le soglie dalla più alta alla più bassa, oppure usa condizioni
   equivalenti chiaramente ordinate.
5. Calcola `imposta = redditoImponibile * aliquota`.
6. Stampa nome ditta, reddito, aliquota e imposta stimata.
7. Inserisci un commento `///` che spieghi perché la soglia più alta deve essere considerata per prima.

Questo è un modello didattico: non rappresenta un calcolo fiscale reale
progressivo.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Stima un'imposta con scaglioni didattici.
 */
#include <iostream>
#include <string>

int main() {
    /// TODO: spiega perché l'ordine delle soglie evita classificazioni premature.
    // TODO: dichiara i dati, scegli l'aliquota e stampa il prospetto.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `if / else if / else` classifica un dato in alternative esclusive.
- La catena si ferma al primo ramo vero.
- Con soglie `>=`, ordina i controlli dalla soglia più alta alla più bassa.
- L'ultimo `else` gestisce tutti i valori rimasti.
- Testa sempre i confini: esattamente soglia, appena sotto e appena sopra.

---

### ➡️ Prossimo chunk

Quando la decisione dipende da un valore discreto, come un codice menu o uno
stato numerico, una lunga catena può diventare difficile da leggere. Nel
prossimo chunk userai `switch` per organizzare questi casi.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/08_if-else-01.md">Lezione precedente (8 — Bivi e decisioni: scegliere con if e if-else)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/10_switch-01.md">Lezione successiva (10 — Lo smistatore di sportello: scegliere con switch e case)</a>
