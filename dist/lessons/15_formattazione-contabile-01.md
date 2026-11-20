<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-16
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_funzioni-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_scope-01.md)

---


## 🖨️ La Stampante Fiscale: formattare importi con `<iomanip>`

> "In contabilità due decimali non sono un vezzo: sono una regola."  
> — *Pratica di bilanci e scontrini*

`std::cout` di default non stampa sempre i centesimi come uno scontrino.  
Con **`<iomanip>`** imposti **virgola fissa** e **precisione**, così gli importi sono leggibili e confrontabili.

> 💡 **Metafora: stampante dello scontrino**  
> - `std::fixed` = “modo importi”, non notazione scientifica  
> - `std::setprecision(2)` = sempre **due cifre** dopo la virgola  
> - Risultato tipico: `19.50` e non `19.5`

Questo chunk è **solo formattazione output**. Non mescola `break`/`continue`.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Usare `std::fixed` e `std::setprecision(2)` su importi monetari
- Produrre un mini-prospetto allineato (imponibile, IVA, totale)

---

### ⚙️ In breve

```cpp
#include <iomanip>

std::cout << std::fixed << std::setprecision(2);
std::cout << 19.5;   // 19.50
```

La manipolazione resta attiva sulle stampe successive dello stesso stream finché non la cambi.

---

### 🔬 Laboratorio PRIMM: Riga di scontrino

#### 1. PREDICT (Prevedi)

Come appare 19.5 con `std::fixed` e `std::setprecision(2)`?

```cpp
std::cout << std::fixed << std::setprecision(2) << 19.5;
```

[(X)] 19.50
[( )] 19.5
[( )] 20
[( )] 1.95e1

<details>
<summary>💡 Spiegazione</summary>
<code>fixed</code> + precisione 2 forza due decimali: 19.5 diventa 19.50 in output.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scontrino_riga.cpp
 * @brief Importi con due decimali.
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

| Manipolatore | Effetto |
|--------------|---------|
| `std::fixed` | Notazione fissa |
| `std::setprecision(2)` | Due cifre decimali in modo fixed |

Prova a togliere `fixed` e osserva la differenza.

#### 4. MODIFY (Modifica)
1. Cambia l’imponibile a `100` e verifica i centesimi.
2. Aggiungi una riga “Totale arrotondato visualizzato” (stesso formato).
3. Estrai una funzione `void stampaImporto(const char* etichetta, double v)` già formattata.

#### 5. MAKE (Crea)
**Scenario SIA — Prospetto documento**

`prospetto_importi.cpp`: imponibile, aliquota, IVA, totale; tutte le righe con due decimali; etichette chiare.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <iomanip>
int main() {
    std::cout << std::fixed << std::setprecision(2);
    // ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- `#include <iomanip>` per la forma “scontrino”
- `fixed` + `setprecision(2)` = due decimali stabili
- Un chunk = solo output; la logica IVA resta nelle funzioni
- Utile in ogni Make contabile successivo

---

### ➡️ Prossimo chunk
Valore vs riferimento nei parametri di funzione: quando la modifica deve restare.
