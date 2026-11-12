## 🎯 Capitolo 13: Il Cruscotto del Programmatore (break, continue e Formattazione con <iomanip>)

> "La precisione nella presentazione dei numeri è l'abito formale con cui il software si presenta all'azienda."
> — *Principio dei Sistemi Contabili*

Hai conquistato tutti i costrutti fondamentali del linguaggio C++: variabili, decisioni e cicli. Prima di salire al livello successivo e iniziare a progettare programmi complessi suddivisi in funzioni (Blocco 2), ci mancano due strumenti indispensabili per rendere il tuo codice **flessibile, sicuro e professionale**:

1. **Il controllo chirurgico dei cicli (`break` e `continue`):** come interrompere un'elaborazione prima del tempo o come saltare un singolo passaggio difettoso senza fermare l'intero programma.
2. **La formattazione dell'output con `<iomanip>`:** come stampare numeri monetari con esattamente due cifre decimali (`19.50 EUR` invece del brutto `19.5`) e allineare scontrini e fatture in perfette tabelle contabili.

---

### 💡 Le Metafore: Il Nastro di Confezionamento e la Stampante Fiscale

> 💡 **Metafora:**  
> - **Il tasto `break` (Il Pulsante Rosso di Emergenza):**  
>   Sulla linea di confezionamento automatica delle merci scatta un allarme grave (es. sensore di sicurezza violato). L'operatore preme il pulsante a fungo: **tutto il nastro si ferma immediatamente** e il ciclo di produzione viene interrotto all'istante.
> - **Il tasto `continue` (Il Braccio di Scarto):**  
>   Lungo il nastro passa un pacco vuoto o un codice a barre illeggibile. Un braccio pneumatico lo spinge nel cestino degli scarti: la macchina non si blocca, **salta quel singolo pacco difettoso** e passa subito a lavorare il pacco successivo!
> - **I manipolatori di `<iomanip>` (La Stampante Fiscale Professionale):**  
>   Il terminale di cassa non stampa numeri alla rinfusa sul rotolo di carta: usa un righello tipografico per incolonnare le descrizioni a sinistra, gli importi a destra e stampare sempre i due zeri dei centesimi.

---

### ⚙️ Controllo Chirurgico: `break` vs `continue`

| Istruzione | Cosa fa | Dove atterra il cursore? | Esempio Gestionale |
| :--- | :--- | :--- | :--- |
| **`break;`** | **Esce forzatamente e definitivamente dal ciclo**, interrompendo qualsiasi iterazione futura. | Salta alla prima riga **dopo la graffa di chiusura `}`** del ciclo. | Arresto per frode: se una carta risulta rubata, blocca l'elaborazione. |
| **`continue;`** | **Interrompe solo il giro corrente**, ignorando le righe rimanenti del blocco. | Salta **in testa al ciclo** per iniziare subito l'iterazione successiva (nel `for` esegue prima l'aggiornamento contatore). | Transazione annullata: se l'importo è 0€, salta la stampa dello scontrino e passa al cliente successivo. |

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
while (Elementi da elaborare?) is (SI)
  :Leggi transazione;
  if (Errore Bloccante?) then (SI)
    :break;
    detach
  elseif (Transazione Annullata?) then (SI)
    :continue;
  else (NO: Valida)
    :Aggiorna bilancio;
    :Stampa ricevuta;
  endif
endwhile (NO)
:Report finale;
stop
@enduml
```

---

### 📐 Formattare l'Output Aziendale con `<iomanip>`

Di default, `std::cout` stampa i numeri decimali nel modo più compatto possibile:
- Il numero `19.50` viene stampato come `19.5` (perde lo zero finale!).
- La divisione `100.0 / 3.0` stampa `33.3333` (un disastro estetico per un bilancio contabile).

Includendo la libreria `<iomanip>` (*Input/Output Manipulators*) possiamo istruire il flusso di stampa:

```cpp
#include <iomanip>

// 1. FORZARE 2 CIFRE DECIMALI (Standard Valuta / Euro):
std::cout << std::fixed << std::setprecision(2);
// Da questo punto in poi: 19.5 diventa "19.50", e 33.3333 diventa "33.33"!

// 2. IMPOSTARE LA LARGHEZZA DI UNA COLONNA:
// std::setw(10) riserva uno spazio di esattamente 10 caratteri per la stampa successiva
std::cout << std::setw(10) << 45.50;

// 3. ALLINEAMENTO CONTABILE (Sinistra per testi, Destra per importi):
std::cout << std::left  << std::setw(20) << "Monitor 24 Pollici" 
          << std::right << std::setw(10) << 149.99 << " EUR\n";
```

> ⚠️ **Attenzione su `std::setw`:** Mentre `std::fixed` e `std::setprecision` restano attivi per tutte le stampe successive, **`std::setw` vale per una sola singola stampa** e va ripetuto per ogni colonna che desideri formattare!

---

### 🔬 Laboratorio PRIMM: Il Report Fiscale delle Vendite Giornaliere

Sviluppiamo un generatore di prospetti contabili tabellari per l'amministrazione aziendale.

#### 1. PREDICT (Prevedi)
? Osserva questo ciclo `for`. Quale sequenza numerica verrà stampata?
```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i << " ";
}
```
- [ ] `1 2 3 4 5 `
- [x] `1 3 `
- [ ] `1 2 3 `
- [ ] `3 `

<details>
<summary>💡 Spiegazione</summary>
Seguiamo il ciclo passo dopo passo:
1. <code>i = 1</code>: i due <code>if</code> sono falsi -> stampa <code>1 </code>.
2. <code>i = 2</code>: si attiva <code>continue;</code> -> il resto del corpo viene saltato e si passa subito a <code>i = 3</code> (non stampa nulla!).
3. <code>i = 3</code>: i due <code>if</code> sono falsi -> stampa <code>3 </code>.
4. <code>i = 4</code>: si attiva <code>break;</code> -> il ciclo viene <b>terminato all'istante</b> e il programma esce dal <code>for</code>.
Il risultato finale a video è esattamente <code>1 3 </code>!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `report_fiscale.cpp`. Nota come combina `continue` per saltare gli storni a importo zero, `break` per bloccare la cassa in caso di furto/anomalia, e i manipolatori di `<iomanip>` per generare una tabella contabile impeccabile:

```cpp
/**
 * @file report_fiscale.cpp
 * @brief Report vendite giornaliere con scarto transazioni e formattazione monetaria.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>
#include <iomanip>
#include <string>

/**
 * @brief Funzione principale: genera il prospetto contabile delle vendite.
 * @return int Codice di uscita (0 = esecuzione regolare).
 */
int main() {
    /// Incasso totale cumulato valido
    double totaleIncasso = 0.0;

    /// Numero di transazioni commerciali valide andate a buon fine
    int transazioniValide = 0;

    // Impostiamo una volta per tutte la precisione monetaria a 2 decimali
    std::cout << std::fixed << std::setprecision(2);

    std::cout << "========================================================" << "\n";
    std::cout << "        PROSPETTO FISCALE GIORNALIERO VENDITE          " << "\n";
    std::cout << "========================================================" << "\n";
    
    // Intestazione tabella allineata con larghezze fisse
    std::cout << std::left  << std::setw(6)  << "ID" 
              << std::left  << std::setw(28) << "Descrizione Prodotto" 
              << std::right << std::setw(12) << "Importo (EUR)" 
              << std::right << std::setw(10) << "Stato" << "\n";
    std::cout << "--------------------------------------------------------" << "\n";

    // Simulazione di una sequenza di 5 transazioni registrate
    for (int id = 1; id <= 5; ++id) {
        std::string descrizione;
        double importo = 0.0;

        // Dati simulati delle transazioni
        if (id == 1)      { descrizione = "Mouse Wireless Ottico";   importo = 19.50;  }
        else if (id == 2) { descrizione = "Storno Ordine Annullato"; importo = 0.00;   }
        else if (id == 3) { descrizione = "Tastiera Meccanica RGB";  importo = 59.90;  }
        else if (id == 4) { descrizione = "Toner Stampante Laser";   importo = 120.00; }
        else if (id == 5) { descrizione = "Allarme Blocco Fiscale";  importo = -999.0; }

        // 1. USO DI BREAK: Se c'e un codice di allarme critico, ferma tutto!
        if (importo == -999.0) {
            std::cout << ">>> ARRESTO D'EMERGENZA: Rilevata anomalia bloccante al n. " 
                      << id << " <<<\n";
            break;
        }

        // 2. USO DI CONTINUE: Se la transazione e uno storno nullo, scartala!
        if (importo == 0.0) {
            std::cout << std::left  << std::setw(6)  << id
                      << std::left  << std::setw(28) << descrizione
                      << std::right << std::setw(12) << importo
                      << std::right << std::setw(10) << "[SCARTATA]\n";
            continue; // Salta il resto del corpo e passa direttamente a id = 3!
        }

        // Se arriviamo qui, la transazione e valida: aggiorniamo i totali
        totaleIncasso += importo;
        transazioniValide++;

        // Stampa riga contabile con allineamento professionale
        std::cout << std::left  << std::setw(6)  << id
                  << std::left  << std::setw(28) << descrizione
                  << std::right << std::setw(12) << importo
                  << std::right << std::setw(10) << "[VALIDA]\n";
    }

    std::cout << "--------------------------------------------------------" << "\n";
    std::cout << std::left  << std::setw(34) << "TOTALE GENERALE INCASSATO:" 
              << std::right << std::setw(12) << totaleIncasso << " EUR\n";
    std::cout << "Transazioni valide registrate: " << transazioniValide << "\n";
    std::cout << "========================================================" << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Salti e Registri nello Stack)

Visualizziamo come `break` e `continue` deviano istantaneamente il flusso di esecuzione:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20totale%20%3D%200.0%3B%0A%0A%20%20%20%20for%20%28int%20i%20%3D%201%3B%20i%20%3C%3D%204%3B%20%2B%2Bi%29%20%7B%0A%20%20%20%20%20%20%20%20if%20%28i%20%3D%3D%202%29%20continue%3B%20//%20Scarta%20il%20giro%202%0A%20%20%20%20%20%20%20%20if%20%28i%20%3D%3D%204%29%20break%3B%20%20%20%20//%20Esce%20al%20giro%204%0A%20%20%20%20%20%20%20%20totale%20%2B%3D%2010.0%3B%0A%20%20%20%20%7D%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Totale%3A%20%22%20%3C%3C%20totale%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"**:
1. A `i = 2`, quando la freccia tocca `continue;`:
   - Guarda come la freccia **salta all'insù** tornando alla riga del `for`, incrementa `i` a `3` ed esegue il test, **senza mai toccare la riga `totale += 10.0;`**.
2. A `i = 4`, quando la freccia tocca `break;`:
   - Guarda come la freccia viene **proiettata in avanti fuori dal ciclo**, atterrando direttamente sulla riga `std::cout`, senza neppure aggiornare `i` a 5!

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Aggiungi la Colonna dell'IVA:** Nel programma `report_fiscale.cpp`, aggiungi una nuova colonna calcolata: `double impostaIva = importo * 0.22;`. Usa `std::setw(10)` per visualizzare l'importo dell'IVA accanto a quello della merce.
2. **Scarta Transazioni Sotto Soglia:** Modifica il controllo con `continue`: fai in modo che scarti tutte le transazioni con importo inferiore a `5.00€` (considerate micro-pagamenti non rilevanti per il report).
3. **Cosa succede senza `std::fixed`?** Prova a rimuovere `std::fixed` lasciando solo `std::setprecision(2);`. Noterai che il C++ interpreterà il 2 come numero totale di cifre significative (es. `120.00` verrà stampato come `1.2e+02` in notazione scientifica!). Questo ti dimostra perché `std::fixed` è obbligatorio in ambito economico.

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Prospetto di Liquidazione IVA Trimestrale**  
> L'ufficio contabile deve predisporre il prospetto trimestrale per la liquidazione periodica dell'IVA.
> 
> Scrivi un programma C++ autonomo (`liquidazione_iva.cpp`):
> - Utilizza un ciclo `for` per elaborare 6 fatture registrate nel trimestre (ID da 1 a 6).
> - Ogni fattura ha un imponibile netto e un codice aliquota (`char`):
>   - `'O'`: Ordinaria 22% (`0.22`).
>   - `'R'`: Ridotta 10% (`0.10`).
>   - `'M'`: Minima 4% (`0.04`).
>   - `'E'`: Esente IVA (`0.00`).
> - **Regola di Controllo Flusso:**
>   - Se l'imponibile di una fattura è `<= 0.0`, usa `continue;` per ignorarla stampando un avviso *"Fattura annullata"*.
>   - Se l'imponibile supera `50.000€`, scatta un alert antiriciclaggio che interrompe il ciclo con `break;`.
> - **Formattazione Contabile (`<iomanip>`):**
>   - Imposta `std::fixed` e `std::setprecision(2)`.
>   - Stampa una tabella a 4 colonne perfettamente allineate con `std::setw`:
>     `Fattura ID` | `Imponibile (EUR)` | `Aliq.` | `Imposta IVA (EUR)`
> - Al termine del ciclo, calcola e stampa:
>   - L'imponibile complessivo.
>   - Il totale dell'IVA a debito da versare all'Erario.
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti `///` proporzionati sulle aliquote fiscali.
> - Allineamenti contabili ordinati (testo a sinistra, numeri e valute a destra).
