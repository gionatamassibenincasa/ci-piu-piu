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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/09_bivi-complessi-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/11_while-01.md)

---


## 🎛️ Lo smistatore di sportello: scegliere con `switch`

Nel capitolo precedente hai usato `if / else if` per classificare intervalli e
soglie. Quando invece la scelta è un codice preciso, come il tasto `1` di un
menu o il carattere `'U'` di una valuta, una lunga catena può diventare
verbosa.

In questi casi puoi usare `switch`: confronta un valore discreto con diversi
`case`.

> 💡 **Metafora:** Immagina un distributore ATM. Il tasto premuto è il codice
> della scelta; ogni `case` è lo sportello dell'operazione corrispondente;
> `break` è il freno che chiude lo sportello dopo l'erogazione; `default` è il
> messaggio “codice non valido” quando nessuno sportello corrisponde.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere uno `switch` su un codice discreto usando `case`, `break` e `default`.

---

### ⚙️ Prima del laboratorio: anatomia dello switch

```cpp
switch (scelta) {
    case 1:
        std::cout << "Prelievo\n";
        break;
    case 2:
        std::cout << "Versamento\n";
        break;
    default:
        std::cout << "Opzione non valida\n";
        break;
}
```

| Parte | Idea pratica | Perché c'è |
| :--- | :--- | :--- |
| `switch` | Legge un codice discreto | Organizza le alternative |
| `case` | Rappresenta un valore preciso | Collega codice e operazione |
| `break` | Esce dallo switch | Evita il fall-through involontario |
| `default` | Gestisce gli altri valori | Copre il codice non previsto |

Regole operative:

1. La scelta dello `switch` deve essere un tipo intero o carattere, come `int` o
   `char`.
2. Ogni `case` confronta un valore preciso, non un intervallo.
3. Dopo un `case` utile inserisci `break`, salvo un fall-through voluto.
4. Usa `if / else if` per soglie, intervalli, `double` o `std::string`.

---

### 🧭 Prima del laboratorio: il percorso della scelta

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
start
:Leggi il codice della scelta;
switch (scelta)
case (1)
  :Prelievo;
  :break;
case (2)
  :Versamento;
  :break;
case (3)
  :Saldo;
  :break;
case (default)
  :Opzione non valida;
  :break;
endswitch
:Continua dopo lo switch;
stop
@enduml
```

Uno `switch` cerca il `case` corrispondente. Se lo trova, esegue quel blocco;
con `break` esce subito. Se non trova corrispondenze, entra in `default`.

---

### 🔬 Laboratorio PRIMM: menu ATM

Un menu ATM deve smistare quattro codici: prelievo, versamento, visualizzazione
del saldo e uscita.

#### 1. PREDICT (Prevedi)

```cpp
int sceltaMenu = 2;

switch (sceltaMenu) {
    case 1:
        std::cout << "Prelievo\n";
        break;
    case 2:
        std::cout << "Versamento\n";
        break;
    default:
        std::cout << "Opzione non valida\n";
        break;
}
```

**Domanda 1**

Quale `case` viene selezionato con `sceltaMenu = 2`?

[(X)] `case 2`, perché il valore coincide con la sua costante
[( )] `case 1`, perché è il primo caso scritto
[( )] `default`, perché ogni scelta deve passare dall'alternativa finale

**Domanda 2**

Perché `break` è importante dopo il messaggio del `case 2`?

[(X)] Ferma lo switch e impedisce di eseguire i case successivi
[( )] Rende uguale il valore di tutti i case
[( )] Fa ripartire lo switch dal primo case

**Domanda 3**

Che cosa stampa il frammento se `sceltaMenu = 7`?

[(X)] Il messaggio del ramo `default`
[( )] Il messaggio del `case 1`, perché 7 è maggiore di 1
[( )] Tutti i messaggi dei case in ordine

**Domanda 4**

Per quale tipo di dato è adatto questo `switch`?

[(X)] Un codice discreto come un `int` o un `char`
[( )] Un intervallo continuo come un prezzo `double`
[( )] Una frase completa contenuta in `std::string`

**Domanda 5**

Che cosa può accadere se togli il `break` da `case 2`?

[(X)] L'esecuzione può continuare nel `case` successivo: è il fall-through
[( )] Il programma torna automaticamente a `case 1`
[( )] Il compilatore cancella il messaggio del `case 2`

#### 2. RUN (Esegui)

Digita il programma completo e osserva quale operazione viene selezionata.

```cpp
/**
 * @file menu_atm.cpp
 * @brief Smista una scelta tra le operazioni di uno sportello ATM.
 */
#include <iostream>

/**
 * @brief Esegue un'operazione in base a un codice intero.
 * @return int Codice di uscita: 0 indica terminazione corretta.
 */
int main() {
    /// Il codice simula il tasto premuto dal cliente.
    int sceltaMenu = 2;

    std::cout << "=== SPORTELLO ATM ===\n";
    std::cout << "1. Prelievo\n";
    std::cout << "2. Versamento\n";
    std::cout << "3. Visualizza saldo\n";
    std::cout << "0. Esci\n";
    std::cout << "Scelta registrata: " << sceltaMenu << "\n";

    switch (sceltaMenu) {
        case 1:
            std::cout << "Prelievo selezionato.\n";
            break;
        case 2:
            std::cout << "Versamento selezionato.\n";
            break;
        case 3:
            std::cout << "Visualizzazione saldo selezionata.\n";
            break;
        case 0:
            std::cout << "Arrivederci.\n";
            break;
        default:
            std::cout << "Opzione non valida.\n";
            break;
    }

    return 0;
}
```
@LIA.cpp

Con `sceltaMenu = 2` compare `Versamento selezionato.`. Il `break` impedisce
di eseguire anche il `case 3`.

#### 3. INVESTIGATE (Indaga)

Dopo il Run, ricostruisci il percorso seguito dal valore `2`.

```cpp
int sceltaMenu = 2;

switch (sceltaMenu) {
    case 1:
        std::cout << "Prelievo\n";
        break;
    case 2:
        std::cout << "Versamento\n";
        break;
    case 3:
        std::cout << "Saldo\n";
        break;
    default:
        std::cout << "Opzione non valida\n";
        break;
}
```

**Domanda 1**

Qual è il primo passaggio eseguito quando il programma arriva allo `switch`?

[(X)] Confronta il valore di `sceltaMenu` con i valori dei `case`
[( )] Esegue sempre il primo blocco e poi cerca il valore
[( )] Esegue prima `default` come controllo di sicurezza

**Domanda 2**

Perché con `sceltaMenu = 2` non viene eseguito `case 3`?

[(X)] Il `break` di `case 2` fa uscire dallo switch
[( )] I case successivi vengono ignorati perché hanno sempre numeri maggiori
[( )] Il programma esegue solo i case che contengono numeri pari

**Domanda 3**

Che cosa succede senza `break` alla fine di `case 2`?

[(X)] Dopo il messaggio di `case 2`, l'esecuzione continua nel case successivo
[( )] Il programma si ferma sempre con un errore di compilazione
[( )] Viene eseguito soltanto `default`

**Domanda 4**

Perché `default` non viene eseguito con `sceltaMenu = 2`?

[(X)] Esiste già un case corrispondente e il suo `break` chiude lo switch
[( )] `default` funziona soltanto con valori negativi
[( )] Il compilatore elimina sempre `default` quando ci sono tre case

**Domanda 5**

Perché `double sceltaMenu = 2.0;` non è adatto come espressione dello switch?

[(X)] Lo switch richiede un valore intero o carattere, non un numero decimale
[( )] Un double può essere usato solo per stampare prezzi
[( )] I numeri con decimali non possono essere assegnati a variabili

| Passo | Cosa accade | Risultato |
| :---: | :--- | :--- |
| 1 | `switch` legge `sceltaMenu` | Valore `2` |
| 2 | Confronta con `case 1` | Nessuna corrispondenza |
| 3 | Confronta con `case 2` | Corrispondenza |
| 4 | Esegue il messaggio | Versamento |
| 5 | Incontra `break` | Esce dallo switch |

Prova a cambiare `sceltaMenu` in `7`: nessun `case` coincide e viene eseguito
`default`.

Ora rimuovi temporaneamente il `break` dal `case 2`. Vedrai il fall-through:
dopo Versamento viene eseguito anche il codice del `case 3`, finché non viene
incontrato un `break`.

> 🔗 **Ispezione facoltativa:** copia il programma in
> [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva il salto al
> `case` corrispondente.

#### 4. MODIFY (Modifica)

Prima di modificare, prevedi l'effetto di una sola modifica per volta.

```cpp
int sceltaMenu = 2;

switch (sceltaMenu) {
    case 1:
        std::cout << "Prelievo\n";
        break;
    case 2:
        std::cout << "Versamento\n";
        break;
    default:
        std::cout << "Opzione non valida\n";
        break;
}
```

**Domanda 1**

Quale modifica aggiunge una voce per la visualizzazione del saldo?

[(X)] Aggiungere `case 3`, stampare il messaggio e chiudere con `break`
[( )] Aggiungere `default 3:` dopo il case 2
[( )] Cambiare `switch` in `std::cout`

**Domanda 2**

Quale modifica fa eseguire lo stesso messaggio sia con codice `0` sia con codice `9`?

[(X)] Scrivere `case 0:` seguito da `case 9:` prima delle stesse istruzioni
[( )] Scrivere `case 0 || 9:` come se fosse una condizione booleana
[( )] Duplicare `default` due volte

**Domanda 3**

Che effetto ha aggiungere `break` dopo `default`?

[(X)] Rende esplicita l'uscita dallo switch anche quando nessun case coincide
[( )] Fa eseguire di nuovo il case precedente
[( )] Trasforma `default` in un ciclo

**Domanda 4**

Quale modifica mantiene il prezzo di una ricarica con i centesimi?

[(X)] Usare una variabile `double` per l'importo dentro il case, senza usarla come scelta
[( )] Usare un `double` come espressione dello switch
[( )] Memorizzare l'importo nel nome del `case`

**Domanda 5**

Perché conviene modificare un case alla volta?

[(X)] Per distinguere quale case o break ha cambiato il percorso del menu
[( )] Perché uno switch può contenere un solo case in assoluto
[( )] Perché `break` funziona solo nel primo case scritto

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
switch (sceltaMenu) {
    case 1:
        std::cout << "Prelievo\n";
        break;
    default:
        std::cout << "Opzione non valida\n";
        break;
}
```

</details>

**Modifica A — aggiungi il saldo**

Aggiungi `case 3`, stampa `Saldo selezionato.` e chiudi con `break`.

**Modifica B — due codici per uscire**

Fai eseguire lo stesso messaggio ai codici `0` e `9` con fall-through
intenzionale:

```cpp
case 0:
case 9:
    std::cout << "Arrivederci.\n";
    break;
```

**Modifica C — prova il tipo sbagliato**

Sostituisci temporaneamente la scelta con:

```cpp
double sceltaMenu = 2.0;
```

Ricompila e osserva l'errore: lo `switch` non accetta un numero decimale come
valore di selezione.

#### 5. MAKE (Crea)

**Scenario aziendale:** un POS deve convertire un importo estero in euro in
base al codice della valuta selezionata.

Crea `cambio_valute.cpp` rispettando tutti i requisiti:

1. Dichiara `double importoValutaEstera = 120.00`.
2. Dichiara `char codiceValuta = 'U'`.
3. Usa uno `switch` sul codice della valuta.
4. Gestisci `U/u` con tasso `0.92`, `G/g` con `1.18`, `J/j` con `0.0061`
   e `S/s` con `1.05`.
5. Usa il fall-through intenzionale per maiuscole e minuscole.
6. Usa `default` per stampare `Valuta non supportata`.
7. Per i codici validi, calcola e stampa il controvalore in euro.
8. Inserisci commenti `///` per spiegare perché i tassi sono associati ai case.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
/**
 * @brief Conversione di una valuta estera in euro al POS.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché il tasso dipende dalla valuta selezionata.
    // TODO: dichiara importo e codice, poi scrivi lo switch.
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `switch` seleziona valori discreti, come `int` e `char`.
- `case` rappresenta un valore preciso, non un intervallo.
- `break` chiude il ramo e previene il fall-through involontario.
- `default` gestisce i codici non previsti.
- Il fall-through può essere intenzionale, per esempio per `U` e `u`.
- Per soglie, intervalli, `double` e `std::string` usa `if / else if`.

---

### ➡️ Prossimo chunk

Finora il programma ha seguito un percorso oppure ha scelto un caso. Nel
prossimo capitolo imparerai a ripetere un'azione con il ciclo `while`.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/09_bivi-complessi-01.md">Lezione precedente (9 — Scaglioni ordinati: if, else if ed else)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/11_while-01.md">Lezione successiva (11 — Il nastro della cassa: ripetere con il ciclo while)</a>
