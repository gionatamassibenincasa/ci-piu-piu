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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/13_do-while-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_formattazione-contabile-01.md)

---


## ⏹️ Uscite Anticipate: `break` e `continue` nei cicli

> "La semplicità è la massima raffinatezza."
>
> — *Leonardo da Vinci*

In un controllo aziendale non tutti i dati meritano lo stesso trattamento:
un movimento vuoto può essere ignorato, mentre un importo anomalo può rendere
inutile continuare. In C++ puoi esprimere queste due decisioni dentro un ciclo.

> 💡 **Metafora:**  
> Immagina un nastro che trasporta fatture. `continue` è il pulsante
> **“salta questa fattura”**: il nastro riparte con la successiva. `break` è
> il pulsante **“ferma il nastro”**: il controllo del lotto termina subito.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- usare `continue` per saltare un’iterazione e `break` per terminare un ciclo in base a una regola aziendale.

---

### ⚙️ Prima del laboratorio: due uscite diverse

| Istruzione | Effetto nel ciclo | Regola tipica |
| :--- | :--- | :--- |
| `continue` | salta il resto del giro corrente e passa al prossimo | ignora un dato vuoto o non interessante |
| `break` | esce subito dal ciclo più interno | ferma l’analisi davanti a un dato anomalo |

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

Nel `for`, dopo `continue` viene comunque eseguito l’aggiornamento `++i`.
Dopo `break`, invece, il ciclo è terminato: non esiste un giro successivo.

---

### 🧭 Prima del laboratorio: leggere il flusso

Per ogni valore di `i`, il programma legge le condizioni dall’alto verso il
basso:

1. se `i == 2`, salta la stampa e passa al prossimo giro;
2. altrimenti, se `i == 4`, esce dal ciclo;
3. altrimenti, stampa `i`.

Il punto importante è **dove** si trova l’istruzione: un `continue` prima
della stampa impedisce a quella stampa di essere raggiunta.

---

### 🔬 Laboratorio PRIMM: Controllo scarti

Il ciclo simula una prima scansione di dati: alcuni valori vengono saltati,
un valore anomalo chiude il controllo.

#### 1. PREDICT (Prevedi)

Prima di eseguire il codice, scegli le risposte e spiega a parole la
differenza tra saltare un giro e terminare il ciclo:

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

**Domanda 1**

Qual è l’effetto di `continue` quando `i` vale 2?

[(X)] Salta il resto del giro corrente e passa al giro successivo
[( )] Ripete il giro corrente senza aggiornare `i`
[( )] Esce definitivamente dal ciclo

**Domanda 2**

Qual è l’effetto di `break` quando `i` vale 4?

[(X)] Esce subito dal ciclo e non raggiunge il giro con `i` uguale a 5
[( )] Riporta `i` a 1 e ricomincia il ciclo
[( )] Salta solo la stampa di 4 e continua con 5

**Domanda 3**

Quale output è più coerente con il flusso del ciclo?

[(X)] `13`, perché 2 viene saltato e il ciclo termina quando arriva a 4
[( )] `1345`, perché `break` salta soltanto il numero 4
[( )] `12345`, perché i due comandi non cambiano l’output

**Domanda 4**

Perché il ciclo non stampa `2`?

[( )] Perché `break` viene eseguito due volte nello stesso giro
[( )] Perché `i` diventa automaticamente uguale a 0
[(X)] Perché `continue` viene eseguito prima di `std::cout` nel giro con `i == 2`

**Domanda 5**

In quale situazione aziendale è più adatto `break`?

[(X)] Quando un dato anomalo rende inutile o rischiosa l’analisi dei dati successivi
[( )] Quando vuoi aumentare automaticamente il valore del contatore
[( )] Quando vuoi ignorare un solo dato ma continuare con tutti gli altri

#### 2. RUN (Esegui)

Digita il programma, eseguilo e confronta l’output con la tua previsione.

```cpp
/**
 * @file controllo_scarti.cpp
 * @brief Mostra come saltare un giro e terminare un controllo.
 * @return int Codice di uscita del programma.
 */
#include <iostream>

int main() {
    for (int i = 1; i <= 5; ++i) {
        if (i == 2) {
            continue;
        }
        if (i == 4) {
            break;
        }
        std::cout << i;
    }
    std::cout << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

Dopo il Run, ricostruisci il percorso di ogni iterazione:

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

**Domanda 1**

Quale sequenza di azioni avviene quando `i` vale 2?

[(X)] La prima condizione è vera, parte `continue`, non si stampa 2 e il `for` aggiorna il contatore
[( )] Si stampa 2, poi la seconda condizione interrompe il ciclo
[( )] Il ciclo termina e il valore 3 non viene mai controllato

**Domanda 2**

Perché il valore 3 viene stampato?

[( )] `break` trasforma 3 in un valore valido da stampare
[(X)] Entrambe le condizioni sono false, quindi il flusso raggiunge `std::cout`
[( )] `continue` stampa automaticamente il valore che segue quello saltato

**Domanda 3**

Dopo `continue` in questo `for`, cosa succede normalmente?

[( )] Il programma torna alla dichiarazione di `i` e la reinizializza a 1
[( )] Il programma salta direttamente alla riga dopo tutto il ciclo
[(X)] Viene eseguita l’espressione di aggiornamento `++i`, poi si controlla la condizione del ciclo

**Domanda 4**

Perché il valore 5 non viene mai stampato?

[(X)] Con `i == 4` viene eseguito `break`, che termina il ciclo prima del giro successivo
[( )] Il compilatore considera 5 un valore non stampabile dopo un `continue`
[( )] Il `for` arriva solo fino a 4 anche se la condizione dice `i <= 5`

**Domanda 5**

Se sostituisci `continue` con `break` nella condizione `i == 2`, perché l’output diventa `1`?

[( )] Il primo giro viene annullato insieme a tutti i valori già stampati
[( )] Il secondo comando `break` viene ignorato perché ce n’è già uno
[(X)] Il ciclo termina già al secondo giro, prima di poter controllare 3 e 4

| Valore di `i` | Istruzione decisiva | Effetto | Output |
| :---: | :--- | :--- | :--- |
| 1 | nessuna condizione vera | raggiunge la stampa | `1` |
| 2 | `continue` | salta la stampa e passa a `++i` | `1` |
| 3 | nessuna condizione vera | raggiunge la stampa | `13` |
| 4 | `break` | esce subito dal ciclo | `13` |
| 5 | nessun giro | il ciclo è già terminato | `13` |

Apri il programma in [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva che dopo `continue` il contatore del `for` avanza, mentre dopo
`break` il flusso va direttamente alla riga dopo il ciclo.

#### 4. MODIFY (Modifica)

Prima di modificare il listato, prevedi l’effetto di ogni cambiamento:

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

**Domanda 1**

Quale modifica stampa `124` e termina il ciclo dopo 4?

[( )] Cambiare `i == 4` in `i == 5` senza spostare la stampa
[(X)] Spostare `std::cout << i;` prima dei due controlli e lasciare `break` su 4
[( )] Sostituire `continue` su 2 con `break` e lasciare tutto il resto invariato

**Domanda 2**

Quale modifica salta gli importi pari ma continua a controllare gli altri?

[( )] Usare `if (importo % 2 == 0) break;` per ogni importo pari
[(X)] Usare `if (importo % 2 == 0) continue;` dentro il ciclo
[( )] Usare `if (importo / 2 == 0) continue;`

**Domanda 3**

Quale modifica fa terminare il ciclo quando trova un valore maggiore di 10000?

[( )] Inserire `if (importo > 10000) continue;` se vuoi fermare il ciclo
[(X)] Inserire `if (importo > 10000) break;` prima dell’elaborazione dell’importo
[( )] Cambiare il contatore in `importo > 10000`

**Domanda 4**

Per contare solo i movimenti effettivamente elaborati, dove conviene incrementare `validi`?

[( )] Prima di `continue`, così anche gli importi scartati vengono contati
[( )] Dopo il ciclo, una sola volta, perché il contatore si aggiorna da solo
[(X)] Dopo i controlli `continue` e `break`, nel punto in cui il movimento viene elaborato

**Domanda 5**

Perché conviene provare una modifica alla volta?

[(X)] Per capire se il cambiamento ha alterato il salto, l’uscita o il conteggio previsto
[( )] Perché in un ciclo può esistere una sola istruzione `if`
[( )] Perché `continue` e `break` funzionano solo nel primo tentativo

Parti da questo scaffold:

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    for (int i = 1; i <= 5; ++i) {
        if (i == 2) continue;
        if (i == 4) break;
        std::cout << i;
    }
    return 0;
}
```

</details>

**Modifica A — cambia il punto di stop**  
Cambia solo la condizione di `break` per terminare quando `i` vale `3`.

**Modifica B — conta i dati elaborati**  
Aggiungi `int elaborati = 0;`. Incrementalo solo dopo i due controlli,
nel punto in cui il valore viene davvero elaborato e stampato.

**Modifica C — ciclo sui movimenti**  
Usa una sequenza di importi e sostituisci le condizioni su `i` con:
`continue` per `importo == 0` e `break` per `importo > 10000`.

---

### 5. MAKE (Crea)

**Scenario aziendale — Analisi movimenti di cassa**

Scrivi `analizza_movimenti.cpp` con i seguenti requisiti chiusi:

1. Usa la sequenza `100.0, 0.0, 250.0, 12000.0, 80.0`.
2. Scorri i cinque importi con un ciclo.
3. Se l’importo vale `0.0`, usa `continue`: non stamparlo e non contarlo.
4. Se l’importo è maggiore di `10000.0`, usa `break`: interrompi l’analisi
   prima di elaborare quel movimento e quelli successivi.
5. Conta e stampa quanti movimenti validi sono stati elaborati prima dello stop.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double movimenti[] = {100.0, 0.0, 250.0, 12000.0, 80.0};
    int validi = 0;

    /// Gli zeri non rappresentano movimenti da registrare.
    // TODO: ciclo sui cinque elementi
    // TODO: continue per gli zeri
    // TODO: break per l'outlier
    // TODO: conta e stampa i movimenti validi

    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `continue` salta il resto dell’iterazione corrente.
- `break` termina subito il ciclo più interno.
- In un `for`, `continue` porta comunque all’aggiornamento del contatore.
- La posizione del comando rispetto alla stampa cambia il flusso osservato.
- Usa i due comandi per regole di business chiare, non per nascondere codice confuso.

---

### ➡️ Prossimo chunk

Ora sai controllare il flusso dentro un ciclo. Nel prossimo chunk sposterai
un’elaborazione in una **funzione**, un reparto specializzato che puoi
richiamare quando serve.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/13_do-while-01.md">Lezione precedente (13 — Garantire l'azione: validare con il ciclo do-while)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_formattazione-contabile-01.md">Lezione successiva (15 — La stampante fiscale: formattare importi con `<iomanip>`)</a>
