## 🌲 Capitolo 6: Scaglioni e Labirinti (if-else if in Cascata, if Annidati e Guida alla Scelta)

> "La complessità di un problema si risolve dividendolo in livelli ordinati di decisioni."
> — *Principio dell'Analisi dei Sistemi*

Nel capitolo precedente abbiamo affrontato i bivi a due sole strade (`if-else`). Ma nei contesti gestionali ed economici le scelte raramente sono binarie:
- Il fatturato di un cliente non è solo "alto o basso": si divide in **scaglioni di sconto progressivi** (Silver, Gold, Platinum).
- L'approvazione di un prestito aziendale richiede una sequenza gerarchica di controlli: prima la maggiore età, poi il bilancio, infine le garanzie.

Per governare queste situazioni senza scrivere codice confuso e caotico, utilizziamo la scala **`if / else if / ... / else`**, gli **`if` annidati** e una **bussola decisionale** per scegliere sempre lo strumento giusto.

---

### 💡 La Metafora: Il Nastro di Smistamento Logistico

> 💡 **Metafora:**  
> Pensa al nastro trasportatore di un grande centro logistico con bilancia e scanner ottico:
> - **La scala `if - else if - else` (I Varchi Progressivi):**  
>   Il pacco scorre sul nastro e incontra una serie di sensori posti in ordine:
>   1. Se pesa meno di 2 kg (`if`), viene deviato sulla rampa dei colli leggeri.
>   2. Altrimenti, se pesa meno di 10 kg (`else if`), finisce nella rampa media.
>   3. Altrimenti, se pesa meno di 30 kg (`else if`), va nei colli pesanti.
>   4. Se fallisce tutti i controlli precedenti (`else`), viene spinto sul binario dei colli speciali fuori misura.
>   *Regola fondamentale:* non appena un sensore intercetta il pacco e lo devia, **nessun altro sensore successivo lo esaminerà più**!
>
> - **L'`if` annidato (La Stanza di Sicurezza con Doppia Porta):**  
>   Per entrare nel caveau devi prima superare la porta esterna (`if`). Solo se sei dentro quella stanza trovi la seconda porta blindata (`if` interno). Se la prima porta non si apre, la seconda non la vedrai nemmeno!

---

### 🪜 La Scala `if / else if / else` per Alternative Disgiunte

Quando hai più di due alternative mutuamente esclusive (se ne verifica una, tutte le altre si escludono), si collegano più `if` a cascata:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
:Leggi Volume Fatturato;
if (Fatturato >= 50.000€?) then (SI)
  :Fascia Platinum (Sconto 15%);
elseif (Fatturato >= 20.000€?) then (SI)
  :Fascia Gold (Sconto 10%);
elseif (Fatturato >= 5.000€?) then (SI)
  :Fascia Silver (Sconto 5%);
else (NO)
  :Fascia Base (Nessuno sconto);
endif
:Applica sconto alla fattura;
stop
@enduml
```

#### ⚠️ Il Tranello dell'Ordine delle Condizioni
In una scala `if - else if`, **l'ordine delle condizioni è vitale**! Il computer le valuta dall'alto verso il basso e si ferma alla **prima condizione vera**.
Se ordini male le condizioni (es. mettendo la più generica prima di quella specifica), le condizioni successive diventeranno "codice morto", ovvero non verranno mai raggiunte!

---

### 🧩 `if` Annidati e l'Anti-Pattern della Piramide

Un `if` è **annidato** quando si trova all'interno del blocco `{}` di un altro `if`:

```cpp
if (clienteMaggiorenne) {
    if (redditoCertificato >= 20000.0) {
        std::cout << "Finanziamento concesso.\n";
    }
}
```

> ⚠️ **Attenzione all'Anti-Pattern "Pyramid of Doom" (La Piramide del Caos):**  
> Annidare `if` dentro `if` per 4 o 5 livelli rende il codice illeggibile e difficile da manutenere (il codice scivola continuamente a destra).  
> **Regola di pulizia:** se due condizioni devono verificarsi contemporaneamente senza azioni intermedie, **uniscile con l'operatore logico `&&`**:
> ```cpp
> if (clienteMaggiorenne && redditoCertificato >= 20000.0) {
>     std::cout << "Finanziamento concesso.\n";
> }
> ```

---

### 🧭 La Bussola Decisionale: Quale `if` Scegliere?

Di fronte a un problema logico, consulta questa tabella per scegliere il costrutto ottimale:

| Situazione del Problema | Struttura da Utilizzare | Esempio Pratico |
| :--- | :--- | :--- |
| **Azione opzionale (filtro / guardia):** devo fare qualcosa solo se c'è un'anomalia, altrimenti continuo normalmente. | `if` semplice (senza `else`) | Allarme scorte basse: avvisa solo se `scorte < soglia`. |
| **Aut-aut secco:** esattamente una strada tra due possibili. | `if - else` | Pagamento POS: o autorizzato o negato. |
| **Scaglioni continui / intervalli numerici:** il dato ricade in una sola fascia tra 3 o più alternative. | `if - else if - else` | Scaglioni di fatturato, fasce di peso, sconti per età. |
| **Verifiche preliminari bloccanti:** il secondo controllo ha senso solo se il primo ha avuto successo. | `if` annidato o condizioni con `&&` | Accesso al conto: PIN corretto prima, poi saldo sufficiente. |

---

### 🔬 Laboratorio PRIMM: Il Calcolo Scaglioni Clienti B2B

Implementiamo la politica di fidelizzazione aziendale per clienti Business-to-Business (B2B).

#### 1. PREDICT (Prevedi)
? Osserva questo codice che assegna un giudizio scolastico. Cosa verrà stampato a video se `voto = 85`?
```cpp
int voto = 85;
if (voto >= 60) {
    std::cout << "Sufficiente";
} else if (voto >= 80) {
    std::cout << "Ottimo";
} else {
    std::cout << "Non sufficiente";
}
```
- [ ] `Ottimo`
- [x] `Sufficiente`
- [ ] Stampa sia `Sufficiente` che `Ottimo`
- [ ] Errore di compilazione

<details>
<summary>💡 Spiegazione</summary>
Il programma valuta la prima condizione: <code>85 >= 60</code>, che è <b>vera</b>!  
Stampa immediatamente <code>"Sufficiente"</code> e <b>ignora tutto il resto della catena</b> (anche se 85 è maggiore di 80).  
<b>Lezione fondamentale:</b> quando confronti intervalli con <code>>=</code>, devi partire sempre dallo scaglione <b>più alto e restrittivo</b> e scendere verso il più basso!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `politica_sconti.cpp` con gli scaglioni ordinati correttamente dal più alto al più basso:

```cpp
/**
 * @file politica_sconti.cpp
 * @brief Calcolo sconti B2B a scaglioni di fatturato e verifica fido cliente.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>
#include <string>

/**
 * @brief Funzione principale: determina la fascia cliente e il fido commerciale.
 * @return int Codice di stato (0 = successo).
 */
int main() {
    /// Ragione sociale dell'azienda cliente
    std::string cliente = "TechSolutions S.r.l.";

    /// Volume d'affari annuo cumulato dal cliente
    double fatturatoAnnuo = 32500.00;

    /// Anzianita del cliente in anni di collaborazione
    int anniCollaborazione = 4;

    /// Percentuale di sconto commerciale da applicare
    double percentualeSconto = 0.0;
    std::string livelloFascia;

    // SCALA DECISIONALE A SCAGLIONI ORDINATI (dal piu alto al piu basso)
    if (fatturatoAnnuo >= 50000.0) {
        percentualeSconto = 0.15; /// Sconto Platinum: 15%
        livelloFascia = "Platinum";
    } else if (fatturatoAnnuo >= 20000.0) {
        percentualeSconto = 0.10; /// Sconto Gold: 10%
        livelloFascia = "Gold";
    } else if (fatturatoAnnuo >= 5000.0) {
        percentualeSconto = 0.05; /// Sconto Silver: 5%
        livelloFascia = "Silver";
    } else {
        percentualeSconto = 0.00; /// Fascia Standard: nessun sconto
        livelloFascia = "Standard";
    }

    std::cout << "=== PROFILO COMMERCIALE CLIENTE ===" << "\n";
    std::cout << "Cliente       : " << cliente << "\n";
    std::cout << "Fatturato     : " << fatturatoAnnuo << " EUR" << "\n";
    std::cout << "Fascia premio : " << livelloFascia << "\n";
    std::cout << "Sconto listino: " << (percentualeSconto * 100) << "%\n\n";

    // DECISIONE ANNIDATA: Valutazione affidamento creditizio (Fido)
    std::cout << "--- Istruttoria Fido Bancario/Commerciale ---" << "\n";
    if (fatturatoAnnuo >= 20000.0) {
        // Solo per clienti con buon fatturato, controlliamo l'affidabilita storica
        if (anniCollaborazione >= 3) {
            /// Fido accordato per clienti storici ad alto volume
            std::cout << "Esito: FIDO AZIENDALE CONCESSO (Linea di credito: 10.000 EUR)\n";
        } else {
            /// Volume alto ma cliente troppo recente: fido prudenziale
            std::cout << "Esito: FIDO LIMITATO (Cliente recente, max 2.500 EUR)\n";
        }
    } else {
        std::cout << "Esito: FIDO NEGATO (Fatturato insufficiente)\n";
    }

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Cortocircuito della Cascata)

Ora osserviamo come il processore naviga la catena `else if` ed entra solo nel blocco corretto:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20fatturato%20%3D%2032500.0%3B%0A%20%20%20%20int%20anni%20%3D%204%3B%0A%20%20%20%20double%20sconto%20%3D%200.0%3B%0A%0A%20%20%20%20if%20%28fatturato%20%3E%3D%2050000.0%29%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.15%3B%0A%20%20%20%20%7D%20else%20if%20%28fatturato%20%3E%3D%2020000.0%29%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.10%3B%0A%20%20%20%20%7D%20else%20if%20%28fatturato%20%3E%3D%205000.0%29%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.05%3B%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20sconto%20%3D%200.0%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Sconto%3A%20%22%20%3C%3C%20sconto%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"**:
1. Alla riga `if (fatturato >= 50000.0)`: la condizione è `false` (32500 < 50000). Il cursore salta al primo `else if`.
2. Alla riga `else if (fatturato >= 20000.0)`: la condizione è `true` (32500 >= 20000).
3. Il processore entra nel blocco ed esegue `sconto = 0.10;`.
4. **Guarda attentamente il passo successivo:** la freccia di esecuzione **salta direttamente alla fine di tutta la catena**, oltrepassando gli altri `else if` e l'`else` senza nemmeno leggerli!

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Nuovo Scaglione Diamond:** Aggiungi in cima alla scala lo scaglione *Diamond*: per fatturati pari o superiori a `100.000€`, applica uno sconto del `20%` (`0.20`). Verifica che un fatturato di `120000` riceva lo sconto Diamond e non Platinum!
2. **Rifattorizzazione dell'`if` annidato:** Sostituisci l'`if` annidato del fido bancario con un'unica istruzione `if` con operatore logico `&&`:
   ```cpp
   if (fatturatoAnnuo >= 20000.0 && anniCollaborazione >= 3) {
       std::cout << "Fido concesso!\n";
   }
   ```
   Rifletti: il codice è più corto e chiaro? Quali sono i vantaggi?

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Calcolo Scaglioni di Imposta sul Reddito Aziendale (IRES/IRPEF)**  
> Nel diritto tributario ed economico, le imposte dirette sul reddito sono calcolate ad aliquote progressive per scaglioni.
> 
> Scrivi un programma C++ autonomo (`imposte_reddito.cpp`) che calcoli l'aliquota e l'imposta presunta dovuta da una ditta individuale:
> - Dichiara `std::string nomeDitta`: denominazione dell'impresa.
> - Dichiara `double redditoImponibile`: il reddito netto annuale dichiarato (es. `38500.00€`).
> - **Regola di Calcolo ad Aliquote Progressive (usando `if - else if - else`):**
>   - Fino a `15.000€` -> Aliquota **23%** (`0.23`).
>   - Da `15.000,01€` a `28.000€` -> Aliquota **25%** (`0.25`).
>   - Da `28.000,01€` a `50.000€` -> Aliquota **35%** (`0.35`).
>   - Oltre `50.000€` -> Aliquota massima **43%** (`0.43`).
> - Calcola l'importo totale dell'imposta stimata moltiplicando `redditoImponibile * aliquotaApplicata`.
> - **Bonus di Sostenibilità:** Aggiungi un flag `bool certificazioneGreen = true;`. Se l'azienda possiede la certificazione ambientale, applica una detrazione secca di `1.000€` dall'imposta dovuta (usa un `if` semplice come filtro).
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti proporzionati `///` con le motivazioni delle aliquote vigenti.
> - Stampa elegante del prospetto fiscale aziendale con riepilogo delle imposte.
