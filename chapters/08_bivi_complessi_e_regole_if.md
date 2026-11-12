## 🌲 Capitolo 8: Scaglioni e Labirinti (`if / else if / else` e if annidati)

> "La complessità di un problema si risolve dividendolo in livelli ordinati di decisioni."
> — *Principio dell'Analisi dei Sistemi*

Con `if-else` gestiamo un bivio a due strade.  
Nei contesti aziendali le scelte sono spesso **a scaglioni**: fasce di sconto, livelli di fido, aliquote fiscali.  
Servono la **scala** `if / else if / else` e, quando un controllo dipende da un altro, gli **`if` annidati**.

> 💡 **Metafora: nastro di smistamento logistico**  
> - **Scala `if / else if / else`** = sensori in sequenza sul nastro: il primo che “prende” il pacco lo devia e **i successivi non lo vedono più**.  
> - **`if` annidato** = doppia porta di sicurezza: solo se apri la prima trovi la seconda. Se la prima resta chiusa, la seconda non la incontri.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una catena `if / else if / else` per alternative mutuamente esclusive
- Usare un `if` annidato quando un controllo ha senso solo dopo un altro
- Scegliere tra scala, annidamento e `&&` senza creare rami morti o condizioni fuori ordine

---

### 🪜 La scala `if / else if / else`

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

### 🚪 L’`if` annidato

Quando la seconda domanda ha senso **solo se** la prima è vera:

```cpp
if (anniCollaborazione >= 3) {
    if (fatturatoAnnuo >= 20000.0) {
        std::cout << "Fido concesso\n";
    } else {
        std::cout << "Fatturato insufficiente per il fido\n";
    }
} else {
    std::cout << "Anzianita insufficiente\n";
}
```

A volte la stessa logica si scrive più corta con `&&` (un solo messaggio di esito).  
L’annidamento resta utile quando i **messaggi di errore** devono essere distinti.

---

### 🧭 Bussola: quale strumento usare?

| Situazione | Strumento |
|------------|-----------|
| Due sole alternative | `if-else` |
| Tre o più fasce mutuamente esclusive | scala `if / else if / else` |
| Secondo controllo solo se il primo è superato, con messaggi diversi | `if` annidato |
| Tutte le condizioni devono essere vere, un solo esito | `if (A && B)` |

---

### 🔬 Laboratorio PRIMM: Fasce sconto e fido

#### 1. PREDICT (Prevedi)
Con `voto = 85`, cosa stampa questo codice?

```cpp
if (voto >= 90) {
    std::cout << "Ottimo\n";
} else if (voto >= 60) {
    std::cout << "Sufficiente\n";
} else {
    std::cout << "Insufficiente\n";
}
```

[( )] `Ottimo`
[(X)] `Sufficiente`
[( )] Stampa sia `Sufficiente` che `Ottimo`
[( )] Errore di compilazione

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
    int anniCollaborazione = 4;

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

    // Fido: doppia porta (annidato) per messaggi distinti
    if (anniCollaborazione >= 3) {
        if (fatturato >= 20000.0) {
            std::cout << "Fido: CONCESSO\n";
        } else {
            std::cout << "Fido: NEGATO (fatturato insufficiente)\n";
        }
    } else {
        std::cout << "Fido: NEGATO (anzianita insufficiente)\n";
    }

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

Poi, con `anniCollaborazione = 4`, si entra nel primo `if` del fido e, poiché `32500 >= 20000`, il fido è concesso.

> 🔗 Segui il flusso su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Fascia Diamond**  
   In cima alla scala: se `fatturato >= 100000` → sconto `0.20`.  
   Verifica con `120000` che non resti classificato Platinum.

2. **Fido in una riga**  
   Sostituisci l’annidamento con:
   ```cpp
   if (anniCollaborazione >= 3 && fatturato >= 20000.0) {
       std::cout << "Fido: CONCESSO\n";
   } else {
       std::cout << "Fido: NEGATO\n";
   }
   ```
   Più corto, ma perdi i messaggi distinti. Quando preferiresti l’annidamento?

3. **Ordine sbagliato (esperimento)**  
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
- `bool certificazioneGreen`: se `true`, detrai `1000` dall’imposta (non sotto zero)
- Output: prospetto con fascia, aliquota, imposta, eventuale detrazione, totale

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
    // dichiara dati, scala aliquote, detrazione green, stampa prospetto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- Scala `if / else if / else` = alternative esclusive; **ordine delle soglie** decisivo.
- Al primo ramo vero il resto della catena viene saltato.
- `if` annidato = seconda domanda solo se la prima è superata (messaggi diversi).
- `A && B` = stesso esito in forma compatta; meno flessibile sui messaggi.
- Per molte costanti discrete (menu 1/2/3) nel prossimo capitolo useremo `switch`.

---

### ➡️ Prossimo chunk
Quando la decisione dipende da un **valore discreto** (tasto di menu, codice operazione, stato numerico), la scala di `else if` diventa verbosa.  
Entra in scena lo **`switch`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: scala else-if + annidamento + bussola di scelta
  [x] Metafora nastro logistico
  [x] Quiz sintassi corretta
  [x] Predict sull'esclusività dei rami
  [x] PRIMM fasce sconto + fido
  [x] Make scaglioni imposta (modello semplificato esplicitato)
  [x] switch solo annunciato
-->
