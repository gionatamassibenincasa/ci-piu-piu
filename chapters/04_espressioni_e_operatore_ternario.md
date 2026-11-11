## 🧮 Capitolo 4: La Calcolatrice Fiscale (Espressioni, Operatori e Operatore Ternario)

> "I computer non sono intelligenti: sono solo calcolatori incredibilmente veloci e obbedienti."
> — *Principio dell'Elaborazione Dati*

Nel capitolo precedente abbiamo aperto i nostri "sportelli" (variabili) nella memoria per riporre dati statici. Ma l'informatica aziendale vive di **calcoli, confronti e logica**: calcolare l'IVA, applicare sconti percentuali, verificare se un cliente ha diritto a promozioni e decidere tariffe al volo.

Per trasformare i dati grezzi in informazioni utili usiamo le **espressioni**, gli **operatori** e uno strumento compatto ed elegante: l'**operatore ternario (`?:`)**.

---

### 💡 La Metafora: La Cassa Veloce con Smistamento Automatico

> 💡 **Metafora:**  
> Pensa alla cassa automatica di un supermercato moderno:
> - **Gli operatori aritmetici** sono i calcoli sui prodotti sul nastro (somma dei prezzi, moltiplicazione per i pezzi, calcolo della percentuale di sconto).
> - **Gli operatori di confronto e logici** sono i sensori della cassa: verificano se il peso della busta corrisponde (`==`), se l'importo supera i 50€ (`>`) e se hai scansionato sia la carta fedeltà **CHE** il coupon sconto (`&&`).
> - **L'operatore ternario (`?:`)** è il display rapido che, con una sola occhiata al carrello, decide all'istante:  
>   *"Spesa > 50€ ? Spedizione Gratuita : Paga 5.90€"*.

---

### ⚙️ Gli Operatori Fondamentali del C++

Un'**espressione** è una combinazione di variabili, valori e operatori che, una volta calcolata dal processore, **produce un singolo valore**.

#### 1. Operatori Aritmetici (I Calcoli)
- `+` (Somma) e `-` (Sottrazione)
- `*` (Moltiplicazione)
- `/` (Divisione): **attenzione al tranello della divisione intera!**
  - Se dividi due interi (`7 / 2`), il C++ esegue una divisione intera e il risultato è `3` (il resto viene perso).
  - Se almeno uno dei due è `double` (`7.0 / 2` o `7 / 2.0`), il risultato è `3.5`.
- `%` (Modulo o Resto): calcola il resto della divisione tra interi (`7 % 2` restituisce `1`). Fondamentale per sapere se un numero è pari o dispari o per gestire turni e periodicità.

#### 2. Operatori di Confronto (Le Domande)
Confrontano due valori e restituiscono sempre un valore booleano: `true` (vero) oppure `false` (falso).
- `==` (Uguale a — attenzione: **due segni uguale**, non confonderlo con l'assegnamento `=`!)
- `!=` (Diverso da)
- `<`, `>`, `<=`, `>=` (Minore, Maggiore, Minore o uguale, Maggiore o uguale)

#### 3. Operatori Logici Booleani (La Logica di Business)
Permettono di combinare più condizioni insieme:

| Operatore | Nome | Quando è `true`? | Esempio SIA |
| :--- | :--- | :--- | :--- |
| `&&` | **AND** (E logico) | Solo se **entrambe** le condizioni sono vere | `haTessera && spesa > 100` (sconto per tesserati con alta spesa) |
| `\|\|` | **OR** (O logico) | Se **almeno una** delle condizioni è vera | `isStudente \|\| isOver65` (tariffa agevolata) |
| `!` | **NOT** (Negazione) | Ribalta il valore: trasforma `true` in `false` | `!contoBloccato` (il conto è operativo) |

---

### ⚡ L'Operatore Condizionale Ternario: Decisioni in Una Riga

Spesso nei sistemi informativi dobbiamo assegnare un valore a una variabile in base a una semplice condizione. Invece di scrivere blocchi lunghi, il C++ offre una sintassi compatta chiamata **operatore ternario** (perché richiede 3 elementi):

```
condizione ? valore_se_vero : valore_se_falso;
```

```cpp
// Se la spesa supera 50€ la spedizione è gratis (0.0), altrimenti costa 5.90€
double speseSpedizione = (totaleSpesa >= 50.0) ? 0.0 : 5.90;
```

L'operatore ternario è una **espressione** (calcola e restituisce un valore pronto per essere assegnato o stampato), non una sequenza di istruzioni.

---

### 🔬 Laboratorio PRIMM: Il Totale Fiscale e la Spedizione

Mettiamo alla prova la logica di business di un software e-commerce.

#### 1. PREDICT (Prevedi)
? Quale sarà l'output a schermo delle seguenti due righe di codice C++?
```cpp
int pezzi = 5;
double costoTotale = pezzi / 2 * 10.0;
std::cout << costoTotale;
```
- [ ] `25`
- [x] `20`
- [ ] `25.5`
- [ ] Errore di compilazione

<details>
<summary>💡 Spiegazione</summary>
Attenzione all'ordine di esecuzione e ai tipi! Le operazioni con la stessa precedenza (moltiplicazione e divisione) si valutano da sinistra a destra:
1. Prima viene calcolato <code>pezzi / 2</code>. Poiché <code>pezzi</code> (5) e <code>2</code> sono entrambi numeri <b>interi</b>, il C++ esegue la <b>divisione intera</b>: <code>5 / 2 = 2</code> (il decimale .5 viene eliminato!).
2. Poi viene calcolato <code>2 * 10.0</code>: essendoci un <code>double</code>, il risultato finale diventa <code>20.0</code>.
Se avessimo scritto <code>pezzi / 2.0 * 10.0</code>, il risultato sarebbe stato correttamente <code>25.0</code>!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma gestionale per la cassa. Nota l'uso dell'operatore ternario per decidere la percentuale di sconto e le spese di trasporto:

```cpp
/**
 * @file cassa_fiscale.cpp
 * @brief Calcolo scontrino con sconti fedeltà e spese di trasporto con operatore ternario.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Calcola il totale carrello, lo sconto e le spese di consegna.
 * @return int Codice di stato (0 = successo).
 */
int main() {
    /// Costante: soglia di spesa minima per avere la spedizione gratuita
    const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;

    /// Costo standard della spedizione per ordini sotto soglia
    const double COSTO_SPEDIZIONE_STANDARD = 6.50;

    /// Importo totale lordo dei prodotti acquistati nel carrello
    double importoProdotti = 85.00;

    /// Il cliente possiede la tessera fedeltà aziendale?
    bool isClienteFedelta = true;

    // Calcolo percentuale di sconto: 10% se tesserato con spesa >= 50€, altrimenti 2%
    double percentualeSconto = (isClienteFedelta && importoProdotti >= 50.0) ? 0.10 : 0.02;

    /// Valore monetario dello sconto applicato
    double valoreSconto = importoProdotti * percentualeSconto;

    /// Importo effettivo dei prodotti al netto dello sconto
    double totaleMerceScontata = importoProdotti - valoreSconto;

    // Calcolo spese di spedizione tramite operatore ternario
    double speseConsegna = (totaleMerceScontata >= SOGLIA_SPEDIZIONE_GRATIS) ? 0.0 : COSTO_SPEDIZIONE_STANDARD;

    /// Importo complessivo finale dovuto dal cliente
    double totaleFattura = totaleMerceScontata + speseConsegna;

    // Visualizzazione dettagliata dello scontrino
    std::cout << "===== RIEPILOGO SCONTRINO CASSA =====" << "\n";
    std::cout << "Totale carrello : " << importoProdotti << " EUR" << "\n";
    std::cout << "Sconto applicato: -" << valoreSconto << " EUR (" << (percentualeSconto * 100) << "%)\n";
    std::cout << "Merce scontata  : " << totaleMerceScontata << " EUR" << "\n";
    std::cout << "Spese trasporto : " << speseConsegna << " EUR" << "\n";
    std::cout << "-------------------------------------" << "\n";
    std::cout << "TOTALE DA PAGARE: " << totaleFattura << " EUR" << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: La Valutazione dell'Espressione)

Vediamo passo dopo passo come il processore valuta l'operatore ternario e memorizza i dati:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20const%20double%20SOGLIA_GRATIS%20%3D%2060.0%3B%0A%20%20%20%20double%20spesa%20%3D%2085.0%3B%0A%20%20%20%20bool%20isFedele%20%3D%20true%3B%0A%0A%20%20%20%20double%20sconto%20%3D%20%28isFedele%20%26%26%20spesa%20%3E%3D%2050.0%29%20%3F%200.10%20%3A%200.02%3B%0A%20%20%20%20double%20trasporto%20%3D%20%28spesa%20%3E%3D%20SOGLIA_GRATIS%29%20%3F%200.0%20%3A%206.50%3B%0A%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Totale%3A%20%22%20%3C%3C%20%28spesa%20-%20%28spesa%20*%20sconto%29%20%2B%20trasporto%29%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e procedi con il tasto **"Next"**:
1. All'istruzione con `(isFedele && spesa >= 50.0) ? 0.10 : 0.02`:
   - Il processore controlla prima la condizione tra parentesi: `isFedele` è `true`, e `spesa >= 50.0` è `true`.
   - `true && true` produce `true`.
   - Il processore seleziona il ramo sinistro (`0.10`) e **ignora completamente** il ramo destro (`0.02`).
   - Il valore `0.10` viene scritto nello sportello della variabile `sconto`.
2. Nota come le espressioni complesse non occupano spazio permanente: vengono calcolate al volo nei registri della CPU e solo il risultato finale viene salvato nello stack.

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Promozione Weekend:** Modifica la condizione dello sconto usando l'operatore `||` (OR): concedi lo sconto del 10% se il cliente ha la tessera **OPPURE** se la spesa supera i 100€ (anche senza tessera).
2. **Supplemento Servizio Express:** Aggiungi un flag `bool consegnaRapida = true;`. Modifica il calcolo delle spese di trasporto in modo che, se la consegna è rapida, venga aggiunto un supplemento fisso di `3.00€` tramite un'espressione ternaria.
3. **Controllo Resto con il Modulo:** Dichiara una variabile `int articoli = 14;` e usa l'operatore modulo `%` con il ternario per stampare se il numero di articoli acquistati è pari o dispari:
   ```cpp
   std::cout << ((articoli % 2 == 0) ? "Numero pari" : "Numero dispari");
   ```

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: La Commissione Transazione POS Bancario**  
> Gli esercenti commerciali pagano una commissione alla banca per ogni pagamento ricevuto tramite POS (Point of Sale).
> 
> Scrivi un programma C++ autonomo (`commissioni_pos.cpp`) che calcoli il costo di una transazione per un negozio:
> - Dichiara `double importoPagamento`: l'incasso della vendita effettuata dal cliente (es. `45.00€`).
> - Dichiara `bool circuitoInternazionale`: `true` se la carta appartiene a un circuito internazionale (es. Visa/Mastercard estera), `false` se è un circuito PagoBANCOMAT nazionale.
> - **Regola di Business con Operatore Ternario:**
>   - Se il circuito è internazionale, la commissione percentuale è dell'**1.8%** (`0.018`).
>   - Se è PagoBANCOMAT, la commissione è dello **0.7%** (`0.007`).
> - **Commissione Minima Fissa (Operatore Ternario):**
>   - Calcola la commissione in euro. Se la commissione calcolata risulta inferiore a `0.15€`, la banca applica comunque una commissione minima fissa di `0.15€` (usa il ternario per verificare se la commissione calcolata è `< 0.15`).
> - Calcola l'**incasso netto effettivo** che rimane all'esercente (`importoPagamento - commissioneFinale`).
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti `///` sulle variabili con le relative aliquote.
> - Stampa chiara e professionale dello scontrino di cassa con i costi bancari esplicitati.
