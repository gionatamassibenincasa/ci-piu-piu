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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/07_if-else-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/09_switch-01.md)

---


## 🌲 Scaglioni Ordinati: `if / else if / else`

> "La complessità di un problema si risolve dividendolo in livelli ordinati di decisioni."
> — *Principio dell'Analisi dei Sistemi*

Con `if-else` gestiamo un bivio a due strade.  
Nei contesti aziendali le scelte sono spesso **a scaglioni**: fasce di sconto, livelli di fido, aliquote fiscali.  
Serve una **scala** `if / else if / else`, che controlla le fasce in ordine.

> 💡 **Metafora: nastro di smistamento logistico**  
> - **Scala `if / else if / else`** = sensori in sequenza sul nastro: il primo che “prende” il pacco lo devia e **i successivi non lo vedono più**.  

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una scala `if / else if / else` ordinata per classificare un dato in fasce esclusive

---

### ⚙️ Prima del laboratorio: la scala `if / else if / else`

Per alternative **disgiunte** (se ne vale una, le altre no):

```cpp
if (fatturato >= 50000.0) {
    sconto = 0.15;          // Platinum
} else if (fatturato >= 20000.0) {
    sconto = 0.10;          // Gold
} else if (fatturato >= 5000.0) {
    sconto = 0.05;          // Silver
} else {
    sconto = 0.0;           // nessuna fascia
}
```

**Ordine critico:** metti prima le soglie più restrittive (es. ≥ 50000 prima di ≥ 20000).  
Se invertissi l’ordine, un cliente Platinum verrebbe classificato Gold.

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Leggi fatturato;
if (fatturato >= 50000?) then (sì)
  :Platinum 15%;
elseif (fatturato >= 20000?) then (sì)
  :Gold 10%;
elseif (fatturato >= 5000?) then (sì)
  :Silver 5%;
else (no)
  :Nessuno sconto;
endif
stop
@enduml
```

---

### 🧭 Prima del laboratorio: l'ordine decide il risultato

Per una scala, chiedi prima la fascia più difficile da raggiungere. Se mettessi
`>= 20000` prima di `>= 50000`, un cliente Platinum sarebbe fermato dal sensore
Gold e non arriverebbe mai al successivo.

---

### 🔬 Laboratorio PRIMM: Fasce sconto cliente

Assegniamo la fascia sconto del cliente con controlli in sequenza.

#### 1. PREDICT (Prevedi)


```cpp
double fatturato = 25000.0;
// if / else if / else sulle soglie
```

Con fatturato = 25000, quale fascia assegna la scala corretta (≥50000 / ≥20000 / ≥5000)?

[( )] Platinum 15%
[(X)] Gold 10%
[( )] Silver 5%
[( )] Nessuno sconto


<details>
<summary>💡 Spiegazione</summary>
<code>85 >= 90</code> è falso → si passa al primo <code>else if</code>.  
<code>85 >= 60</code> è vero → stampa <code>Sufficiente</code> e <strong>salta</strong> il resto della catena.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file fasce_sconto_cliente.cpp
 * @brief Assegna fascia sconto per fatturato e valuta un fido semplice.
 */
#include <iostream>
#include <string>

/**
 * @brief Classifica il cliente e stampa esito sconto/fido.
 * @return int 0 se ok.
 */
int main() {
    std::string ragioneSociale = "Alpha Logistica Srl";
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

    std::cout << "Cliente : " << ragioneSociale << "\n";
    std::cout << "Fatturato: " << fatturato << " euro\n";
    std::cout << "Fascia   : " << fascia << " (sconto " << sconto * 100 << "%)\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Con `fatturato = 32500`:

| Passo | Condizione | Esito |
|-------|------------|-------|
| `>= 50000` | falso | passa oltre |
| `>= 20000` | vero | `sconto = 0.10`, fascia Gold |
| resto della scala | — | **non eseguito** |

> 🔗 Segui il flusso su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
if (fatturato >= 50000.0) {
    sconto = 0.15;
} else if (fatturato >= 20000.0) {
    sconto = 0.10;
} else {
    sconto = 0.0;
}
```

</details>

1. **Fascia Diamond**  
   In cima alla scala: se `fatturato >= 100000` → sconto `0.20`.  
   Verifica con `120000` che non resti classificato Platinum.

2. **Ordine sbagliato (esperimento)**
   Inverti temporaneamente le soglie Gold e Platinum e osserva cosa succede a un fatturato di `60000`.

#### 5. MAKE (Crea)
**Scenario SIA — Scaglioni di imposta (modello didattico semplificato)**

Scrivi `imposte_reddito.cpp`:

- `std::string nomeDitta`
- `double redditoImponibile` (es. `38500`)
- **Aliquota unica per fascia** (semplificazione didattica, non il calcolo progressivo reale):
  - ≤ 15000 → 23%
  - ≤ 28000 → 25%
  - ≤ 50000 → 35%
  - oltre → 43%
- Imposta stimata = `redditoImponibile * aliquota`
- Output: prospetto con fascia, aliquota e imposta stimata

**Requisiti:** Doxygen, `///` sulle aliquote, scala `if / else if / else` ordinata.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Stima imposta per scaglioni (modello didattico).
 */
#include <iostream>
#include <string>

int main() {
    /// TODO: spiega perché la soglia più alta viene controllata per prima.
    // TODO: dichiara dati, scala aliquote e stampa prospetto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- Scala `if / else if / else` = alternative esclusive; **ordine delle soglie** decisivo.
- Al primo ramo vero il resto della catena viene saltato.
- Per molte costanti discrete (menu 1/2/3) nel prossimo capitolo useremo `switch`.

---

### ➡️ Prossimo chunk
Quando la decisione dipende da un **valore discreto** (tasto di menu, codice operazione, stato numerico), la scala di `else if` diventa verbosa.  
Entra in scena lo **`switch`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: scala else-if ordinata
  [x] Metafora nastro logistico
  [x] Quiz sintassi corretta
  [x] Predict sull'esclusività dei rami
  [x] PRIMM fasce sconto + fido
  [x] Make scaglioni imposta (modello semplificato esplicitato)
  [x] switch solo annunciato
-->
