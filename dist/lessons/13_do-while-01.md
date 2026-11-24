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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/12_for-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_break-continue-01.md)

---


## 🔁 Garantire l'azione: validare con il ciclo `do-while`

Il `while` e il `for` controllano la condizione prima di entrare nel corpo.
A volte, però, devi compiere un'azione almeno una volta prima di poterla
controllare: mostrare un modulo, chiedere un importo o leggere un PIN.

Il `do-while` serve proprio a questo: esegue il corpo e controlla la condizione
alla fine.

> 💡 **Metafora:** Immagina un modulo online con campi obbligatori. Prima devi
> visualizzarlo e compilare una risposta; solo dopo puoi premere “Invia” e
> controllare se i dati sono validi. Se c'è un errore, il modulo torna indietro
> e lo compili di nuovo.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un `do-while` per validare un input che deve essere richiesto almeno una volta.

---

### ⚙️ Prima del laboratorio: controllo in coda

```cpp
double importo;

do {
    std::cout << "Importo (> 0): ";
    std::cin >> importo;
} while (importo <= 0.0);
```

| Costrutto | Quando controlla? | Iterazioni minime |
| :--- | :--- | :---: |
| `while` | Prima del corpo | 0 |
| `for` | Prima del corpo | 0 |
| `do-while` | Dopo il corpo | 1 |

Il punto e virgola dopo `while (importo <= 0.0);` è obbligatorio: chiude la
struttura completa del `do-while`.

---

### 🧭 Prima del laboratorio: il modulo e la verifica

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Mostra la richiesta;
:Leggi il dato;
while (Dato ancora non valido?) is (sì)
  :Mostra errore;
  :Leggi un nuovo dato;
endwhile (no)
:Accetta il dato;
stop
@enduml
```

Per un importo ammesso tra `1.0` e `5000.0`, il ciclo deve continuare quando
l'importo è troppo piccolo **oppure** troppo grande:

```cpp
importo < MIN_BONIFICO || importo > MAX_BONIFICO
```

Quando entrambe le condizioni di errore sono false, l'importo è valido e il
programma esce.

---

### 🔬 Laboratorio PRIMM: validazione di un bonifico

L'ufficio pagamenti deve accettare un bonifico solo se l'importo è compreso
nell'intervallo ammesso.

#### 1. PREDICT (Prevedi)

```cpp
int n = 10;

do {
    std::cout << "giro\n";
    n = n + 1;
} while (n < 5);
```

**Domanda 1**

Quante volte viene eseguito il corpo?

[( )] Cinque volte, perché il ciclo arriva fino a 5
[(X)] Una volta, perché il corpo viene eseguito prima del controllo
[( )] Zero volte, perché `10 < 5` è falso

**Domanda 2**

Perché il `do-while` è utile per chiedere un dato valido?

[( )] Controlla sempre la condizione prima della prima lettura
[(X)] Permette di chiedere il dato almeno una volta prima di controllarlo
[( )] Impedisce all'utente di inserire più di un valore

**Domanda 3**

Dove viene controllata la condizione nel `do-while`?

[( )] Solo quando il programma arriva a `return 0`
[(X)] Dopo il corpo del ciclo
[( )] Prima del corpo, come nel `while`

**Domanda 4**

Quale elemento sintattico chiude il `do-while`?

[( )] La parola `break` obbligatoria fuori dalle graffe
[(X)] Il punto e virgola dopo `while (condizione)`
[( )] Un secondo `else` dopo la condizione

**Domanda 5**

Quale situazione richiede più naturalmente un `do-while` che un `while`?

[( )] Un conteggio noto da 1 a 12
[( )] Una classificazione tra fasce di fatturato
[(X)] Un modulo che deve essere mostrato e compilato almeno una volta

#### 2. RUN (Esegui)

Digita il programma completo. Prova con `-10`, poi `0`, infine `250`.

```cpp
/**
 * @file valida_bonifico.cpp
 * @brief Richiede un importo finché non rientra nel range ammesso.
 */
#include <iostream>

/**
 * @brief Valida un importo compreso tra uno e cinquemila euro.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il limite minimo impedisce bonifici nulli o negativi.
    const double MIN_BONIFICO = 1.0;
    /// Il limite massimo mantiene il controllo entro la procedura aziendale.
    const double MAX_BONIFICO = 5000.0;
    double importo = 0.0;

    do {
        std::cout << "Importo bonifico: ";
        std::cin >> importo;
        if (importo < MIN_BONIFICO || importo > MAX_BONIFICO) {
            std::cout << "Importo non valido. Riprova.\n";
        }
    } while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);

    std::cout << "Bonifico accettato: " << importo << " EUR\n";
    return 0;
}
```
@LIA.cpp

Il corpo viene eseguito almeno una volta. Con `250`, il controllo finale è
falso e il programma stampa il messaggio di accettazione.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci il percorso di ogni tentativo.

```cpp
const double MIN_BONIFICO = 1.0;
const double MAX_BONIFICO = 5000.0;
double importo = 0.0;

do {
    std::cin >> importo;
} while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);
```

**Domanda 1**

Qual è il primo passaggio eseguito dal programma?

[( )] Controlla subito se `importo` è già valido
[(X)] Legge un importo dentro il corpo del `do`
[( )] Confronta prima le due costanti tra loro

**Domanda 2**

Perché con input `250` il ciclo termina dopo il primo giro?

[( )] Il primo valore inserito viene sempre considerato valido
[(X)] 250 non è minore di 1 e non è maggiore di 5000, quindi la condizione è falsa
[( )] Il `do-while` termina quando incontra un numero pari

**Domanda 3**

Che cosa succede con input `-10` seguito da `250`?

[( )] Il programma esegue il corpo solo una volta e ignora 250
[( )] Il programma accetta subito -10 perché è un numero inserito
[(X)] Il primo valore mantiene la condizione vera, quindi il programma ripete la lettura e poi accetta 250

**Domanda 4**

Perché l'operatore `||` mantiene il ciclo per un importo fuori intervallo?

[(X)] Basta che sia vera una delle due condizioni di errore: troppo piccolo o troppo grande
[( )] Converte l'importo in un valore booleano senza confrontarlo
[( )] Richiede che l'importo sia contemporaneamente minore e maggiore

**Domanda 5**

Che errore sintattico può nascere se togli il `;` dopo `while (...)`?

[( )] Il ciclo diventa automaticamente un `while` con controllo in testa
[(X)] Il compilatore segnala che manca il punto e virgola prima dell'istruzione successiva
[( )] Il programma accetta tutti gli importi senza controllarli

| Giro | `importo` | Condizione di errore | Azione |
| :---: | :---: | :---: | :--- |
| 1 | `-10` | vera | Mostra errore e ripete |
| 2 | `0` | vera | Mostra errore e ripete |
| 3 | `250` | falsa | Esce e accetta |

Il controllo arriva dopo la lettura: per questo il primo tentativo esiste anche
se il valore iniziale fosse già fuori intervallo.

Se togli il punto e virgola finale, il compilatore può segnalare un errore
simile a:

```text
error: expected ';' before 'return'
```

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva il primo
> tentativo garantito.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
double importo = 0.0;

do {
    std::cin >> importo;
} while (importo <= 0.0);
```

**Domanda 1**

Quale modifica restringe l'intervallo agli importi tra 10 e 1000?

[( )] Sostituire la condizione con `importo == 10.0`
[(X)] Usare `importo < 10.0 || importo > 1000.0` nella condizione
[( )] Usare `importo > 10.0 || importo < 1000.0`

**Domanda 2**

Quale modifica permette al PIN di essere provato al massimo tre volte?

[( )] Rimuovere il controllo del PIN e usare solo `break`
[(X)] Aggiungere un contatore e continuare finché PIN errato e tentativi minori di 3
[( )] Inserire tre `do` uno dentro l'altro senza contatore

**Domanda 3**

Che effetto ha cambiare `importo <= 0.0` in `importo < 0.0`?

[( )] Il ciclo non esegue più il primo giro
[(X)] L'importo 0.0 viene accettato, perché non è minore di zero
[( )] L'importo 0.0 viene sempre rifiutato come prima

**Domanda 4**

Quale modifica mantiene il messaggio di errore solo per valori non validi?

[( )] Mettere il messaggio dopo `return 0`
[( )] Sostituire `std::cin` con `std::cout` nel corpo
[(X)] Mettere un `if` nel corpo che controlla lo stesso intervallo

**Domanda 5**

Perché conviene modificare una sola parte del ciclo alla volta?

[(X)] Per capire se il problema riguarda il corpo, la condizione o il punto e virgola finale
[( )] Perché ogni modifica elimina la prima iterazione
[( )] Perché un `do-while` può contenere una sola lettura in assoluto

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
do {
    std::cin >> importo;
} while (importo <= 0.0);
```

</details>

**Modifica A — restringi l'intervallo**

Cambia l'intervallo ammesso da `[1, 5000]` a `[10, 1000]`. Aggiorna entrambe
le condizioni necessarie.

**Modifica B — prova un valore valido al primo tentativo**

Inserisci subito `250`. Verifica che il corpo giri una volta e che il controllo
permetta immediatamente l'uscita.

**Modifica C — osserva la sintassi**

Rimuovi temporaneamente il punto e virgola dopo la condizione finale, compila e
leggi il messaggio del compilatore. Poi ripristinalo.

#### 5. MAKE (Crea)

**Scenario aziendale:** uno sportello deve verificare un PIN prima di
permettere l'accesso, limitando i tentativi per sicurezza.

Crea `pin_sportello.cpp` rispettando tutti i requisiti:

1. Dichiara `const int PIN_CORRETTO = 4821`.
2. Dichiara un `int pinInserito` e un contatore dei tentativi.
3. Chiedi il PIN almeno una volta con un `do-while`.
4. Continua se il PIN è errato e i tentativi sono minori di `3`.
5. Se il PIN è corretto entro tre prove, stampa `Accesso consentito`.
6. Dopo tre errori, stampa `Carta bloccata`.
7. Non rivelare il PIN corretto nei messaggi di errore.
8. Inserisci un commento `///` che spieghi perché il numero di tentativi è limitato.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Validazione PIN sportello con massimo tre tentativi.
 */
#include <iostream>

int main() {
    const int PIN_CORRETTO = 4821;
    /// TODO: spiega perché i tentativi devono essere limitati.
    // TODO: dichiara PIN e contatore, poi scrivi il do-while.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `do-while` esegue il corpo e poi controlla la condizione.
- Il corpo viene eseguito almeno una volta.
- È adatto alla validazione di input e ai menu che devono apparire subito.
- Dopo `while (condizione)` del `do-while` serve `;`.
- Usa `while` o `for` quando zero iterazioni è un caso accettabile.

---

### ➡️ Prossimo chunk

Ora conosci i tre cicli fondamentali. Nel prossimo capitolo userai `break` e
`continue` per guidare con maggiore precisione il flusso dentro un ciclo.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/12_for-01.md">Lezione precedente (12 — Il contatore compatto: ripetere con il ciclo for)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_break-continue-01.md">Lezione successiva (14 — Uscite Anticipate: `break` e `continue` nei cicli)</a>
