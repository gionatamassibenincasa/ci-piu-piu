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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_break-continue-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_funzioni-01.md)

---


## 🖨️ La stampante fiscale: `std::fixed` e `std::setprecision`

Quando stampi un importo, `std::cout` mostra il valore in una forma tecnica. In un preventivo o in una fattura, invece, vuoi una forma regolare: due cifre dopo il punto decimale per ogni riga.

> 💡 **Metafora:**  
> Immagina una stampante fiscale. `std::fixed` seleziona la modalità “importo decimale”; `std::setprecision(2)` imposta due caselle per i centesimi. La stampante non cambia il valore del calcolo: cambia il modo in cui lo presenta.

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- formattare un prospetto di importi con `std::fixed` e `std::setprecision(2)`.

---

### ⚙️ Prima del laboratorio: i due manipolatori

| Elemento | Che cosa imposta | Perché serve in contabilità |
| :--- | :--- | :--- |
| `#include <iomanip>` | Rende disponibili i manipolatori di formattazione | Il compilatore conosce `std::fixed` e `std::setprecision` |
| `std::fixed` | Notazione decimale fissa | Evita una visualizzazione tecnica o variabile |
| `std::setprecision(2)` | Due cifre dopo il punto con `fixed` | Mantiene coerenti importi e totali |

```cpp
std::cout << std::fixed << std::setprecision(2);
std::cout << 19.5;  // 19.50
```

La configurazione resta attiva per le stampe successive dello stesso `std::cout`.

---

### 🔬 Laboratorio PRIMM: il prospetto di una vendita

Il negozio registra un imponibile di `19.5` euro e applica l'IVA al 22%. Prima di eseguire il programma, osserva come verranno stampate le tre righe.

#### 1. PREDICT (Prevedi)

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    std::cout << std::fixed << std::setprecision(2) << imponibile;
    return 0;
}
```

**Domanda 1**

Perché `std::fixed` è utile quando stampi un importo?

[( )] Arrotonda sempre il valore memorizzato nella variabile
[( )] Trasforma automaticamente l'importo da euro a centesimi
[(X)] Chiede di rappresentare il numero in forma decimale fissa, adatta a un prospetto

**Domanda 2**

Che cosa indica `std::setprecision(2)` insieme a `std::fixed`?

[(X)] Mostrare due cifre dopo il punto decimale
[( )] Mostrare al massimo due cifre complessive
[( )] Moltiplicare il numero per 2

**Domanda 3**

Prima del Run, quale output prevedi per `19.5`?

[(X)] 19.50
[( )] 20.00
[( )] 19.5

**Domanda 4**

Perché nel programma serve `#include <iomanip>`?

[(X)] Per rendere disponibili `std::fixed` e `std::setprecision`
[( )] Per sostituire `#include <iostream>` nelle stampe
[( )] Per dichiarare automaticamente tutte le variabili `double`

**Domanda 5**

Se scrivi `std::setprecision(2)` senza `std::fixed`, quale previsione è più corretta?

[( )] L'output avrà sempre esattamente due cifre dopo il punto
[(X)] La precisione riguarda le cifre significative, quindi non garantisce sempre due decimali
[( )] Il programma non può compilare perché `setprecision` richiede un intero positivo diverso da 2

Completa prima il quiz: concentrati sulla differenza tra **valore calcolato** e **valore visualizzato**.

#### 2. RUN (Esegui)

Ricopia ed esegui il programma. Confronta il risultato con la tua previsione.

```cpp
/**
 * @file prospetto_vendita.cpp
 * @brief Presenta un prospetto di vendita in un formato leggibile.
 */
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA 22%:    " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA:        " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```

**Domanda 1**

Perché anche `iva` e `totale` vengono stampate con due decimali?

[( )] La variabile `imponibile` trasferisce il suo formato alle altre variabili
[(X)] I manipolatori restano attivi per le stampe successive dello stesso `std::cout`
[( )] Ogni `double` viene sempre stampato con due decimali in C++

**Domanda 2**

Qual è l'ordine corretto nella riga di configurazione?

[( )] Prima `std::setprecision(2)`, poi si chiude `std::cout` con un punto e virgola
[(X)] Prima `std::fixed`, poi `std::setprecision(2)`, quindi il valore da stampare
[( )] Prima il valore, poi `std::fixed` e infine `std::setprecision(2)`

**Domanda 3**

Perché il risultato di `19.5 * 0.22` può essere visualizzato come `4.29`?

[( )] La moltiplicazione viene eseguita come testo e non come numero
[( )] Il programma sostituisce sempre il valore con il numero intero più vicino
[(X)] Il formato mostra due decimali e arrotonda la rappresentazione visualizzata

**Domanda 4**

Che cosa succede se togli `#include <iomanip>` ma lasci `std::setprecision(2)`?

[( )] Il programma compila, ma `std::cout` ignora soltanto la precisione
[( )] Il valore viene automaticamente stampato come intero
[(X)] Il compilatore può segnalare che `setprecision` non è dichiarata

**Domanda 5**

Se aggiungi una stampa dopo il prospetto senza cambiare il formato, che cosa accade?

[( )] Il formato si annulla automaticamente dopo ogni riga
[( )] Il formato si applica solo alla variabile `imponibile`
[(X)] Anche quella stampa usa il formato corrente di `std::cout`, finché non lo modifichi

Perché l'impostazione compare una sola volta ma vale per tre stampe? Segui l'ordine delle istruzioni:

| Passo | Istruzione | Che cosa osservi |
| :---: | :--- | :--- |
| 1 | `imponibile = 19.5` | Il programma conserva il valore numerico |
| 2 | `iva = imponibile * 0.22` | Calcola l'IVA |
| 3 | `totale = imponibile + iva` | Calcola il totale |
| 4 | `fixed` + `setprecision(2)` | Configura la visualizzazione di `std::cout` |
| 5 | Le tre stampe | Ogni importo appare con due cifre decimali |

Con `fixed` e `setprecision(2)`, `19.5` viene mostrato come `19.50`. Il formato non arrotonda o riscrive la variabile in memoria: riguarda la stampa.

#### 4. MODIFY (Modifica)

```cpp
std::cout << std::fixed << std::setprecision(2);
std::cout << "Totale: " << totale << '\n';
```

**Domanda 1**

Quale modifica fa apparire tre cifre dopo il punto decimale?

[(X)] Sostituire `std::setprecision(2)` con `std::setprecision(3)`
[( )] Sostituire `std::fixed` con `std::setprecision(3)`
[( )] Moltiplicare `totale` per 3 prima della stampa

**Domanda 2**

Che effetto ha togliere `std::fixed` lasciando `std::setprecision(2)`?

[(X)] La precisione può indicare due cifre significative, non necessariamente due decimali
[( )] Il valore di `totale` viene cancellato
[( )] Il programma stampa sempre due zeri in più

**Domanda 3**

Quale modifica mantiene il prospetto a due decimali ma stampa prima l'etichetta `Totale`?

[( )] Mettere `std::fixed` dopo `totale` e prima dell'etichetta
[( )] Cambiare `totale` in una variabile `int`
[(X)] Spostare l'etichetta nella stessa espressione di output, prima di `totale`

**Domanda 4**

Se sostituisci `std::setprecision(2)` con `std::setprecision(0)`, quale effetto prevedi?

[( )] La stampa usa automaticamente due cifre perché gli importi sono monetari
[(X)] La stampa usa zero cifre dopo il punto e può arrotondare il valore visualizzato
[( )] Il programma entra in un ciclo infinito

**Domanda 5**

Quale modifica formatta anche la nuova variabile `sconto` con due decimali?

[( )] Inserire `std::setprecision(2)` solo dopo la stampa di `sconto`
[( )] Dichiarare `sconto` come `char`
[(X)] Stampare `sconto` con lo stesso `std::cout` dopo aver impostato `fixed` e `setprecision(2)`

Apporta una modifica alla volta e riesegui.

**Modifica A — Cambia la precisione**  
Sostituisci `std::setprecision(2)` con `std::setprecision(3)`. Controlla tutte le righe del prospetto.

**Modifica B — Togli `fixed`**  
Lascia `std::setprecision(2)` ma rimuovi `std::fixed`. Confronta il risultato e spiega perché non hai più la garanzia di due cifre dopo il punto.

**Modifica C — Aggiungi una riga**  
Dichiara `double sconto = 1.5;` e stampa `Sconto: 1.50` usando la stessa configurazione già attiva.

<details>
<summary>💡 Scaffold per le modifiche</summary>

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;
    double sconto = 1.5;

    std::cout << std::fixed << std::setprecision(2);
    // TODO: stampa il prospetto e la nuova riga Sconto
    return 0;
}
```

</details>

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio commerciale prepara un preventivo per un cliente.

**Requisiti**:

1. Dichiara `imponibile = 125.5` e `aliquota = 0.22`.
2. Calcola `iva` e `totale` con variabili `double`.
3. Configura `std::cout` con `std::fixed` e `std::setprecision(2)`.
4. Stampa le tre etichette `Imponibile`, `IVA 22%` e `Totale`, ciascuna su una riga.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 125.5;
    double aliquota = 0.22;
    double iva = imponibile * aliquota;
    double totale = imponibile + iva;

    /// Il formato uniforme rende il preventivo leggibile e confrontabile.
    // TODO: configura la stampa a due decimali
    // TODO: stampa imponibile, IVA e totale
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `#include <iomanip>` rende disponibili i manipolatori di formattazione.
- `std::fixed` imposta la notazione decimale fissa.
- Con `std::fixed`, `std::setprecision(2)` mostra due cifre dopo il punto.
- La configurazione resta attiva per le stampe successive dello stesso `std::cout`.
- Il formato cambia la rappresentazione visualizzata, non il valore memorizzato.

---

### ➡️ Prossimo chunk

Ora che sai presentare bene un risultato, puoi imparare a organizzare il calcolo in **funzioni** riutilizzabili.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_break-continue-01.md">Lezione precedente (14 — Uscite Anticipate: `break` e `continue` nei cicli)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_funzioni-01.md">Lezione successiva (16 — Il Primo Reparto: funzioni che restituiscono un valore)</a>
