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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/07_espressioni-ternario-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/09_bivi-complessi-01.md)

---


## 🚦 Bivi e decisioni: scegliere con `if` e `if-else`

Un gestionale non esegue sempre la stessa azione. Un pagamento può essere
approvato o rifiutato; una scorta può essere sufficiente o sotto il minimo; un
badge può essere valido oppure no.

Con `if` e `if-else` insegni al programma a scegliere un percorso.

> 💡 **Metafora:** Immagina un tornello aziendale. La condizione è il lettore
> che controlla il badge; il blocco `if` è il passaggio verde quando la regola
> è vera; il blocco `else` è il passaggio rosso quando la regola è falsa. Con
> `if-else` passa un solo percorso, mai entrambi.

**In questa lezione non** gestiamo ancora catene con più alternative, cicli
o selezioni tramite `switch`. Impariamo prima a controllare un singolo bivio
e a seguire il ramo realmente eseguito.

---

### 🎯 Obiettivi di apprendimento

Alla fine di questa lezione sei in grado di:

- distinguere l'esecuzione di un blocco `if` semplice da quella di un `if-else`;
- scrivere una condizione con gli operatori relazionali e organizzare i rami con le graffe;
- prevedere quale ramo viene attraversato e tracciare lo stato delle variabili;
- riconoscere l'errore causato da un punto e virgola subito dopo la condizione.

---

### ⚙️ Prima del laboratorio: i due modelli

Un `if` semplice esegue un blocco soltanto quando la condizione è vera:

```cpp
if (giacenza < 5) {
    std::cout << "Scorte in esaurimento\n";
}
```

Un `if-else` sceglie uno dei due blocchi:

```cpp
if (saldo >= importo) {
    std::cout << "Pagamento approvato\n";
} else {
    std::cout << "Fondi insufficienti\n";
}
```

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| Condizione | Un confronto che vale vero o falso | Decide il percorso |
| `if` | Ramo per il caso vero | Esegue l'azione consentita |
| `else` | Ramo per il caso falso | Gestisce l'alternativa |
| `{ }` | Confini del blocco | Tiene insieme tutte le istruzioni del ramo |

---

### 🧭 Prima del laboratorio: seguire il flusso

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi saldo e importo;
if (saldo >= importo?) then (vero)
  :Sottrai l'importo;
  :Mostra "Approvato";
else (falso)
  :Mostra "Negato";
endif
:Continua dopo il bivio;
stop
@enduml
```

Operatori utili per confrontare valori già noti:

| Operatore | Significato | Esempio |
| :---: | :--- | :--- |
| `>` | maggiore di | `scorte > 0` |
| `<` | minore di | `scorte < 5` |
| `==` | uguale a | `pinInserito == PIN_SEGRETO` |
| `>=` | maggiore o uguale | `saldo >= importo` |

Non confondere `==`, che confronta, con `=`, che assegna un valore.

---

### 🔬 Laboratorio PRIMM: autorizzazione di un pagamento POS

Il terminale deve decidere se il saldo disponibile basta per una spesa.

#### 1. PREDICT (Prevedi)

```cpp
double saldoDisponibile = 45.00;
double importoSpesa = 62.50;

if (saldoDisponibile >= importoSpesa) {
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
}
```

**Domanda 1**

Quale ramo viene eseguito con saldo `45.00` e spesa `62.50`?

[( )] Entrambi i rami, uno dopo l'altro
[( )] Il ramo `if`, perché ogni pagamento viene approvato
[(X)] Il ramo `else`, perché il saldo non è sufficiente

**Domanda 2**

Perché `saldoDisponibile >= importoSpesa` è una condizione utile per il POS?

[(X)] Confronta i due importi e produce vero solo quando il saldo basta
[( )] Trasforma i due importi in messaggi di testo
[( )] Somma automaticamente il saldo e la spesa

**Domanda 3**

Che cosa succede se saldo e importo valgono entrambi `45.00`?

[( )] La condizione è falsa perché due valori uguali non possono essere confrontati
[(X)] La condizione è vera perché `>=` include anche l'uguaglianza
[( )] Il programma esegue sempre il ramo `else` in caso di parità

**Domanda 4**

Perché le graffe sono importanti nell'esempio?

[(X)] Raggruppano tutte le istruzioni che appartengono a ciascun ramo
[( )] Sostituiscono la condizione tra parentesi
[( )] Servono solo a rendere il codice più colorato nell'editor

**Domanda 5**

Quale risultato produce un `if` semplice quando la condizione è falsa?

[( )] Ripete la condizione finché diventa vera
[( )] Esegue automaticamente il blocco `else`, anche se non esiste
[(X)] Salta il suo blocco e continua con l'istruzione successiva

#### 2. RUN (Esegui)

Digita il programma completo e confronta l'output con la tua previsione.

```cpp
/**
 * @file autorizzazione_pos.cpp
 * @brief Verifica se un pagamento può essere autorizzato.
 */
#include <iostream>

/**
 * @brief Controlla il saldo e comunica l'esito della transazione.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il saldo rappresenta il credito realmente disponibile sul conto.
    double saldoDisponibile = 45.00;
    /// L'importo è decimale perché un pagamento può avere centesimi.
    double importoSpesa = 62.50;

    std::cout << "=== TERMINALE PAGAMENTI POS ===\n";
    std::cout << "Importo richiesto: " << importoSpesa << " EUR\n";

    if (saldoDisponibile >= importoSpesa) {
        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << "TRANSAZIONE APPROVATA\n";
        std::cout << "Nuovo saldo: " << saldoDisponibile << " EUR\n";
    } else {
        std::cout << "TRANSAZIONE NEGATA\n";
        std::cout << "Credito insufficiente\n";
    }

    std::cout << "Operazione conclusa.\n";
    return 0;
}
```
@LIA.cpp

Con i valori iniziali la condizione è falsa, quindi compare
`TRANSAZIONE NEGATA`.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci l'ordine delle istruzioni e spiega perché il saldo
non cambia nel caso negato.

```cpp
double saldoDisponibile = 45.00;
double importoSpesa = 62.50;

if (saldoDisponibile >= importoSpesa) {
    saldoDisponibile = saldoDisponibile - importoSpesa;
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
    std::cout << "Mancano " << importoSpesa - saldoDisponibile << " euro\n";
}
```

**Domanda 1**

Qual è il primo passaggio eseguito quando il programma arriva all'if?

[( )] Esegue prima tutte le istruzioni dentro le graffe
[(X)] Confronta `saldoDisponibile` con `importoSpesa`
[( )] Sottrae sempre la spesa dal saldo

**Domanda 2**

Perché il saldo non viene sottratto nel caso `45.00` contro `62.50`?

[( )] Il ramo `else` annulla sempre tutte le variabili del programma
[( )] I numeri decimali non possono essere sottratti in C++
[(X)] La sottrazione si trova nel ramo `if`, che non viene eseguito quando la condizione è falsa

**Domanda 3**

Quale valore viene calcolato dall'espressione `importoSpesa - saldoDisponibile`?

[( )] `-17.50`, perché il saldo viene sempre scritto per primo
[(X)] `17.50`, cioè l'importo ancora mancante
[( )] `107.50`, perché i due importi vengono sommati

**Domanda 4**

Perché, dopo il blocco `if-else`, il programma può eseguire altre istruzioni?

[(X)] Il bivio sceglie un ramo, poi il flusso continua dopo le graffe
[( )] Il programma esce da `main` ogni volta che incontra `else`
[( )] Le graffe trasformano il bivio in un ciclo

**Domanda 5**

Che cosa accade con questo codice? `if (saldoDisponibile >= importoSpesa); { std::cout << "Approvato"; }`

[(X)] Il punto e virgola chiude subito l'if, quindi il blocco successivo non è più controllato
[( )] Il compilatore interpreta il punto e virgola come un ramo `else`
[( )] Il punto e virgola rende la condizione più precisa

| Passo | Cosa osservi | Stato |
| :---: | :--- | :--- |
| 1 | Il programma confronta `45.00 >= 62.50` | `false` |
| 2 | Salta il blocco `if` | Nessuna sottrazione |
| 3 | Entra nel blocco `else` | Stampa transazione negata |
| 4 | Esce dal bivio | Stampa operazione conclusa |

La sottrazione è dentro il ramo `if`: viene eseguita soltanto quando il
confronto è vero. Le istruzioni dopo le graffe appartengono invece al flusso
comune e vengono eseguite dopo il ramo scelto.

Evita questo errore logico:

```cpp
if (saldoDisponibile >= importoSpesa);
{
    std::cout << "Approvato\n";
}
```

Il punto e virgola chiude subito l'`if`; il blocco successivo non è più
controllato dalla condizione. Il programma può compilare, ma il comportamento
non è quello desiderato.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva quale ramo
> viene attraversato.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
double saldoDisponibile = 45.00;
double importoSpesa = 62.50;

if (saldoDisponibile >= importoSpesa) {
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
}
```

**Domanda 1**

Quale modifica fa approvare la spesa di `62.50` con saldo `100.00`?

[( )] Spostare il messaggio "Negato" dentro il ramo `if`
[(X)] Cambiare `saldoDisponibile` in `100.00`
[( )] Cambiare `>=` in `<=`

**Domanda 2**

Quale modifica permette di mostrare anche il nuovo saldo dopo un pagamento approvato?

[(X)] Aggiungere una stampa nel ramo `if` dopo la sottrazione
[( )] Aggiungere la stampa nel ramo `else` prima del confronto
[( )] Sostituire `std::cout` con `std::cin`

**Domanda 3**

Che effetto ha cambiare `>=` in `>` quando saldo e spesa sono uguali?

[( )] Il pagamento resta approvato perché i due operatori sono equivalenti
[(X)] Il pagamento diventa negato, perché l'uguaglianza non soddisfa più la condizione
[( )] Il programma esegue entrambi i rami

**Domanda 4**

Quale modifica aggiunge un avviso per una scorta sotto cinque pezzi senza creare un secondo ramo obbligatorio?

[(X)] Aggiungere un secondo `if` semplice con condizione `scorte < 5`
[( )] Mettere la quantità dentro una stringa stampata
[( )] Aggiungere sempre `else` al primo `if` del pagamento

**Domanda 5**

Perché conviene modificare una sola condizione alla volta?

[( )] Perché `if` funziona soltanto prima della prima modifica
[( )] Perché un programma C++ può contenere una sola condizione
[(X)] Per capire quale cambiamento ha prodotto il nuovo ramo eseguito

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double saldoDisponibile = 45.00;
    double importoSpesa = 62.50;

    if (saldoDisponibile >= importoSpesa) {
        std::cout << "Approvato\n";
    } else {
        std::cout << "Negato\n";
    }

    return 0;
}
```

</details>

**Modifica A — pagamento approvato**

Cambia `saldoDisponibile` in `100.00`. Ricompila e verifica che venga eseguito
il ramo `if`.

**Modifica B — mostra il nuovo saldo**

Nel ramo `if`, sottrai l'importo e stampa `saldoDisponibile` dopo la
sottrazione. Non aggiungere la stampa nel ramo `else`.

**Modifica C — prova il caso di uguaglianza**

Imposta entrambi i valori a `45.00`. Prevedi il risultato: `>=` include anche
il caso in cui saldo e importo siano uguali.

#### 5. MAKE (Crea)

**Scenario aziendale:** il responsabile sicurezza deve controllare l'accesso
a un caveau aziendale.

Crea `controllo_caveau.cpp` rispettando tutti i requisiti:

1. Dichiara `const int PIN_SEGRETO = 4821`.
2. Dichiara `int pinInserito = 4821`.
3. Confronta i due valori con `==`.
4. Usa un solo `if-else` con graffe.
5. Se il PIN è corretto, stampa `ACCESSO CONSENTITO`.
6. Altrimenti, stampa `ACCESSO NEGATO`.
7. Inserisci un commento `///` che spieghi perché il PIN deve essere confrontato prima dell'accesso.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Controllo accessi a un caveau aziendale.
 */
#include <iostream>

int main() {
    const int PIN_SEGRETO = 4821;
    /// TODO: spiega perché il codice deve essere confrontato prima dell'accesso.
    // TODO: dichiara pinInserito e scrivi l'if-else.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- [ ] `if` esegue un blocco solo quando la condizione è vera.
- [ ] `if-else` sceglie un solo ramo tra vero e falso.
- [ ] Uso sempre le graffe per rendere chiaro il blocco controllato.
- [ ] `==` confronta; `=` assegna.
- [ ] Non metto `;` subito dopo la condizione.
- [ ] Dopo il ramo scelto, il flusso continua con le istruzioni successive.

---

### ➡️ Prossimo passo nel percorso

Quando le alternative diventano più di due, un solo bivio non basta. Nel
prossimo capitolo del percorso Fondamenti, `09_bivi_complessi_e_regole_if`,
costruirai catene `if / else if / else` per gestire fasce di sconto e stati
diversi di un ordine.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/07_espressioni-ternario-01.md">Lezione precedente (7 — La Calcolatrice Fiscale: espressioni e operatore ternario)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/09_bivi-complessi-01.md">Lezione successiva (9 — Scaglioni ordinati: if, else if ed else)</a>
