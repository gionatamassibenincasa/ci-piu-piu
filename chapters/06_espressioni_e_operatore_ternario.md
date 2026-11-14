## 🧮 La Calcolatrice Fiscale: espressioni e operatore ternario

> "I computer non sono intelligenti: sono solo calcolatori incredibilmente veloci e obbedienti."
> — *Principio dell'Elaborazione Dati*

Nel capitolo precedente abbiamo riempito gli sportelli della memoria.  
Ora impariamo a **calcolare** e a **decidere in una riga**: IVA, sconti, spese di spedizione, commissioni POS.

> 💡 **Metafora: la cassa automatica**  
> - **Operatori aritmetici** = i calcoli sul nastro (somme, sconti %, quantità × prezzo)  
> - **Operatori di confronto e logici** = i sensori (“spesa > 50?”, “ha tessera E spesa alta?”)  
> - **Operatore ternario `?:`** = il display che decide all’istante:  
>   *“Spesa ≥ 60€ ? Spedizione gratis : paghi 6,50€”*

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere espressioni aritmetiche, di confronto e logiche corrette
- Evitare la trappola della **divisione intera**
- Usare l’**operatore ternario** per assegnare un valore in base a una condizione

---

### ⚙️ Gli operatori fondamentali

Un’**espressione** combina valori, variabili e operatori e produce **un solo risultato**.

#### Aritmetici
| Operatore | Significato | Attenzione |
|-----------|-------------|------------|
| `+` `-` `*` | somma, sottrazione, moltiplicazione | — |
| `/` | divisione | Se **entrambi** gli operandi sono `int` → **divisione intera** (i decimali si perdono) |
| `%` | resto (modulo) | Solo su interi: `14 % 2 == 0` → pari |

```cpp
int pezzi = 5;
double a = pezzi / 2;      // 2  (divisione intera!)
double b = pezzi / 2.0;    // 2.5 (almeno un operando double)
```

#### Confronto (producono `bool`)
`==`  `!=`  `<`  `<=`  `>`  `>=`

#### Logici
| Operatore | Nome | Vero quando… | Esempio SIA |
|-----------|------|--------------|-------------|
| `&&` | AND | **entrambe** le condizioni sono vere | `haTessera && spesa >= 50` |
| `||` | OR | **almeno una** è vera | `isStudente || isOver65` |
| `!` | NOT | ribalta il valore | `!contoBloccato` |

---

### ⚡ L’operatore ternario `?:`

Forma:
```text
condizione ? valore_se_vero : valore_se_falso
```

È un’**espressione**: calcola e restituisce un valore, pronto per essere assegnato o stampato.

```cpp
double speseSpedizione = (totaleSpesa >= 60.0) ? 0.0 : 6.50;
```

Utile quando la decisione è semplice e produce un valore.  
Per logiche lunghe o con più rami useremo `if` / `else` nei prossimi capitoli.

---

### 🔬 Laboratorio PRIMM: Scontrino e-commerce

Calcoliamo sconto e spese di spedizione di un ordine online con espressioni e operatore ternario.

#### 1. PREDICT (Prevedi)
Cosa stampa questo codice?

```cpp
int pezzi = 5;
double costoTotale = pezzi / 2 * 10.0;
std::cout << costoTotale;
```

[( )] `25`
[(X)] `20`
[( )] `25.5`
[( )] Errore di compilazione

<details>
<summary>💡 Spiegazione</summary>
<code>pezzi / 2</code> è divisione tra interi → risultato <code>2</code> (troncato).  
Poi <code>2 * 10.0</code> → <code>20.0</code>.  
Con <code>pezzi / 2.0 * 10.0</code> otterresti <code>25.0</code>.
</details>

#### 2. RUN (Esegui)
Digita e esegui:

```cpp
/**
 * @file cassa_fiscale.cpp
 * @brief Scontrino con sconto fedeltà e spese di spedizione (ternario).
 */
#include <iostream>

/**
 * @brief Calcola totale carrello, sconto e spedizione.
 * @return int 0 se successo.
 */
int main() {
    const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;
    const double COSTO_SPEDIZIONE_STANDARD = 6.50;

    double importoProdotti = 85.00;
    bool isClienteFedelta = true;

    /// 10% se tesserato e spesa >= 50, altrimenti 2%
    double percentualeSconto =
        (isClienteFedelta && importoProdotti >= 50.0) ? 0.10 : 0.02;

    double valoreSconto = importoProdotti * percentualeSconto;
    double nettoProdotti = importoProdotti - valoreSconto;

    /// Spedizione gratis oltre soglia
    double speseSpedizione =
        (nettoProdotti >= SOGLIA_SPEDIZIONE_GRATIS) ? 0.0 : COSTO_SPEDIZIONE_STANDARD;

    double totaleDaPagare = nettoProdotti + speseSpedizione;

    std::cout << "=== SCONTRINO E-COMMERCE ===\n";
    std::cout << "Prodotti (lordo) : " << importoProdotti << " euro\n";
    std::cout << "Sconto applicato : " << valoreSconto << " euro\n";
    std::cout << "Prodotti (netto) : " << nettoProdotti << " euro\n";
    std::cout << "Spedizione       : " << speseSpedizione << " euro\n";
    std::cout << "TOTALE DA PAGARE : " << totaleDaPagare << " euro\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Segui il flusso dei valori (con i numeri dell’esempio).

| Espressione | Risultato | Perché |
|-------------|-----------|--------|
| `isClienteFedelta && importoProdotti >= 50.0` | `true` | entrambe vere |
| percentuale sconto | `0.10` | ramo `?` del ternario |
| `valoreSconto` | `8.5` | `85 * 0.10` |
| `nettoProdotti` | `76.5` | `85 - 8.5` |
| `nettoProdotti >= 60` | `true` | soglia superata |
| `speseSpedizione` | `0.0` | ramo `?` del secondo ternario |

> 🔗 Esegui il programma passo-passo su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Promozione weekend**  
   Concedi lo sconto del 10% se il cliente ha la tessera **oppure** la spesa (lordo) supera i 100€ (`||`).

2. **Consegna express**  
   Aggiungi `bool consegnaRapida = true;`.  
   Se è `true`, aggiungi un supplemento fisso di `3.00` alle spese di spedizione (anche se erano gratis), usando un ternario.

3. **Pari o dispari**  
   Con `int articoli = 14;` stampa se il numero è pari o dispari:
   ```cpp
   std::cout << ((articoli % 2 == 0) ? "pari" : "dispari");
   ```

#### 5. MAKE (Crea)
**Scenario SIA — Commissione transazione POS**

Scrivi `commissioni_pos.cpp` per un esercente:

- `double importoPagamento` (es. `45.00`)
- `bool circuitoInternazionale` (`true` = Visa/MC estera, `false` = PagoBANCOMAT)
- **Regola con ternario:**
  - circuito internazionale → commissione **1,8%** (`0.018`)
  - altrimenti → **0,7%** (`0.007`)
- **Commissione minima:** se la commissione calcolata è `< 0.15`, applica comunque `0.15` (secondo ternario)
- Calcola e stampa l’**incasso netto** dell’esercente (`importo - commissioneFinale`)

**Requisiti:** Doxygen, commenti `///` sulle aliquote, output chiaro tipo scontrino.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Calcolo commissione POS e incasso netto esercente.
 */
#include <iostream>

int main() {
    // dichiara importo, flag circuito, calcola commissione e netto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- Espressione = calcoli/confronti che producono **un** valore.
- Divisione tra soli `int` → risultato intero (trappola classica).
- `&&` = entrambe vere; `||` = almeno una vera; `!` = negazione.
- Ternario: `condizione ? se_vero : se_falso` — ideale per scelte semplici che restituiscono un valore.
- Per decisioni lunghe o a più rami → nei prossimi capitoli useremo `if` / `else`.

---

### ➡️ Prossimo chunk
Finora le decisioni tengono in una riga.  
Quando la logica diventa un **bivio** (fare A oppure fare B, con più istruzioni per ramo), entra in scena il costrutto `if` / `else`.

---

<!--#
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: espressioni + ternario (un focus)
  [x] Metafora cassa automatica
  [x] Quiz sintassi corretta
  [x] Trappola divisione intera in Predict
  [x] PRIMM su scontrino e-commerce
  [x] Make su commissioni POS (SIA)
  [x] if/else solo annunciato, non introdotto
#-->
