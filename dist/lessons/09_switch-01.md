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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/08_bivi-complessi-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/10_while-01.md)

---

## 🎛️ Lo Smistatore di Sportello (`switch-case`)

> "La semplicità è il prerequisito per l'affidabilità di un'interfaccia utente."
> — *Edsger W. Dijkstra*

`if / else if` gestisce bene scaglioni e confronti (`>`, `<`, intervalli).  
Quando invece la scelta è un **valore discreto fisso** — tasto di menu `1/2/3`, codice `'A'/'B'/'C'` — una lunga catena di `else if (x == …)` diventa verbosa.  
Per questi casi il C++ offre lo **`switch-case`**.

> 💡 **Metafora: tastiera del distributore / ATM**  
> - Digiti un **codice preciso** (tasto `1`, `2`, `'A'`…).  
> - Lo **`switch`** legge il tasto e attiva lo scomparto giusto (`case`).  
> - Il **`break`** è il freno di fine erogazione: senza di esso la macchina continua e fa scendere anche i prodotti dei cassetti successivi (*fall-through*).  
> - **`default`** = “codice non valido” sullo schermo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere uno `switch` su un codice discreto usando `case`, `break` e `default`

---

### ⚙️ Prima del laboratorio: anatomia dello switch

```cpp
switch (scelta) {
    case 1:
        // prelievo
        break;
    case 2:
        // versamento
        break;
    case 3:
        // saldo
        break;
    default:
        // opzione non valida
        break;  // consigliato anche qui
}
```

**Regole ferree in C++:**
1. L’espressione dello `switch` deve essere di tipo **intero o carattere** (non `double`, non `std::string`).
2. Ogni `case` confronta con una **costante** (letterale o `const`/`constexpr`), non con un intervallo.
3. Senza `break`, l’esecuzione **continua** nei `case` successivi (fall-through). Di solito è un bug; a volte è voluto (es. `'A'` e `'a'`).

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Leggi codice scelta;
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
endswitch
:Prosegui;
stop
@enduml
```

---

### 🧭 Prima del laboratorio: quando usare switch

| Situazione | Preferisci |
|------------|------------|
| Menu 1/2/3, codici carattere, stati numerici fissi | `switch` |
| Scaglioni (`>= 50`, intervalli), condizioni composte | `if / else if` |
| Confronti su `double` o `std::string` | `if / else if` |

---

### 🔬 Laboratorio PRIMM: Menu ATM

Un menu a tasti fissi smista prelievo, versamento e saldo.

#### 1. PREDICT (Prevedi)


```cpp
switch (tasto) {
    case 1:
        std::cout << "Saldo ";
    case 2:
        std::cout << "Estratto Conto ";
    default:
        std::cout << "Errore";
}
```

Con `tasto = 1`, cosa stampa questo frammento **senza** `break` dopo il primo case?

[( )] Stampa solo `Saldo `
[(X)] Stampa `Saldo Estratto Conto Errore`
[( )] Stampa `Saldo Estratto Conto `


<details>
<summary>💡 Spiegazione</summary>
Senza <code>break</code>, dopo <code>case 1</code> l’esecuzione “cade” nei case successivi (*fall-through*).  
Per fermarsi serve un <code>break</code> in ogni ramo (salvo quando il fall-through è intenzionale).
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file menu_atm.cpp
 * @brief Menu semplificato di uno sportello bancomat.
 */
#include <iostream>

/**
 * @brief Esegue un'operazione ATM in base al tasto scelto.
 * @return int 0 se ok.
 */
int main() {
    int sceltaMenu = 2;   // simula il tasto premuto dal cliente

    std::cout << "=== SPORTELLO ATM ===\n";
    std::cout << "1. Prelievo fisso 50 EUR\n";
    std::cout << "2. Versamento fisso 100 EUR\n";
    std::cout << "3. Visualizza saldo\n";
    std::cout << "0. Esci\n";
    std::cout << "Scelta: " << sceltaMenu << "\n\n";

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

#### 3. INVESTIGATE (Investiga)
Con `sceltaMenu = 2`:

| Passo | Cosa succede |
|-------|----------------|
| `switch` valuta `2` | salta direttamente a `case 2` |
| `case 2` | stampa l'operazione selezionata |
| `break` | esce dallo `switch` (non esegue case 3/default) |

Prova a togliere il `break` del `case 2` e riesegui: vedrai anche l’output del saldo (fall-through).

#### 4. MODIFY (Modifica)
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

1. **Ricarica telefonica**  
   Aggiungi `case 4:` con addebito fisso di `20.00` (se il saldo basta) e relativo `break`.

2. **Doppio tasto di uscita**  
   Fai sì che sia `0` sia `9` eseguano l’uscita, usando fall-through intenzionale:
   ```cpp
   case 0:
   case 9:
       std::cout << "Arrivederci.\n";
       break;
   ```

3. **Tipo sbagliato**  
   Prova `double sceltaMenu = 2.0;` nello `switch`: il compilatore segnala che la quantità non è intera.

   Un compilatore come g++ può segnalare:

   ```text
   error: switch quantity not an integer
   ```

#### 5. MAKE (Crea)
**Scenario SIA — Convertitore valute al POS**

Scrivi `cambio_valute.cpp`:

- `double importoValutaEstera` (es. `120.00`)
- `char codiceValuta`:
  - `'U'` / `'u'` → USD, tasso `0.92`
  - `'G'` / `'g'` → GBP, tasso `1.18`
  - `'J'` / `'j'` → JPY, tasso `0.0061`
  - `'S'` / `'s'` → CHF, tasso `1.05`
  - altro → `default`: “Valuta non supportata”
- Usa fall-through per maiuscole/minuscole
- Se valida: stampa importo originale, tasso, controvalore in euro

**Requisiti:** `///` sui tassi e `break` corretti; aggiungi Doxygen solo se il
programma supera circa 15 righe.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Conversione valuta estera in euro al POS.
 */
#include <iostream>

int main() {
    /// TODO: spiega perché ogni tasso dipende dalla valuta selezionata.
    // TODO: dichiara importo e codice, poi scrivi lo switch
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `switch` = selezione su valori **discreti** (`int`, `char`).
- Ogni ramo utile termina di solito con `break`.
- Senza `break` → fall-through (a volte voluto, spesso bug).
- `default` gestisce i codici non previsti.
- Per intervalli e confronti su `double`/`string` resta l’`if / else if`.

---

### ➡️ Prossimo chunk
Finora il flusso va avanti o sceglie un ramo, ma non **ripete**.  
Nel prossimo capitolo entra in scena il ciclo: il **`while`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: switch, break, default, fall-through
  [x] Metafora distributore/ATM
  [x] Quiz sintassi corretta
  [x] Predict sul fall-through
  [x] PRIMM menu ATM
  [x] Make cambio valute (SIA)
  [x] while solo annunciato
-->
