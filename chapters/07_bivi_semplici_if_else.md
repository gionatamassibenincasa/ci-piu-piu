## 🚦 Capitolo 7: Bivi e Decisioni (`if` e `if-else`)

> "Le decisioni sono i binari su cui viaggiano i processi aziendali."
> — *Principio di Ingegneria Gestionale*

Finora i programmi correvano su un unico binario.  
Nel mondo reale un pagamento può essere **approvato o rifiutato**, una giacenza **sufficiente o sotto scorta**, un badge **valido o no**.

Per gestire i bivi usiamo **`if`** e **`if-else`**.

> 💡 **Metafora: il tornello aziendale**  
> - **`if` semplice** = sensore di allarme: se rileva un’anomalia fa qualcosa; se non rileva nulla, non fa niente e il flusso continua.  
> - **`if-else`** = lettore badge al tornello:  
>   - *SE* badge valido → verde, passa  
>   - *ALTRIMENTI* → rosso, bloccato  
>   Non esistono vie di mezzo: si attiva **un solo** ramo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un `if` semplice e un `if-else` con graffe corrette
- Evitare i due tranelli classici (`;` dopo la condizione e graffe mancanti)
- Capire lo **scope**: una variabile dichiarata dentro `{ }` esiste solo lì

---

### 🔀 I due modelli

**`if` semplice** — esegui un blocco *solo se* la condizione è vera:

```cpp
if (giacenza < LIVELLO_MINIMO) {
    std::cout << "ATTENZIONE: scorte in esaurimento!\n";
}
```

**`if-else`** — scegli **esattamente uno** dei due rami:

```cpp
if (saldo >= importo) {
    std::cout << "Pagamento approvato\n";
} else {
    std::cout << "Fondi insufficienti\n";
}
```

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Leggi saldo e importo;
if (saldo >= importo?) then (sì)
  :Transazione approvata;
  :Aggiorna saldo;
else (no)
  :Transazione rifiutata;
  :Mostra importo mancante;
endif
:Stampa esito;
stop
@enduml
```

---

### ⚠️ I due grandi tranelli

**1. Il punto e virgola traditore**

```cpp
// SBAGLIATO: il ; chiude subito l'if
if (saldo >= importo);
{
    std::cout << "Approvato\n";  // viene eseguito SEMPRE
}
```

Dopo la `)` della condizione **non va mai** il `;`.

**2. Graffe e scope**

Senza `{ }` l’`if` controlla **solo** la prima istruzione successiva.  
**Usa sempre le graffe**, anche per una sola riga.

Inoltre: una variabile dichiarata dentro un blocco `{ }` **non esiste fuori** (scope locale).

---

### 🔬 Laboratorio PRIMM: Terminale pagamenti POS

Il terminale decide se autorizzare un pagamento confrontando saldo e importo.

#### 1. PREDICT (Prevedi)
Quali righe vengono stampate?

```cpp
int scorte = 12;
if (scorte < 5)
    std::cout << "1. Ordina nuovi pezzi!\n";
    std::cout << "2. Notifica inviata al fornitore.\n";
std::cout << "3. Controllo terminato.\n";
```

[( )] Non stampa nulla
[( )] Stampa 1, 2 e 3
[(X)] Stampa solo 2 e 3
[( )] Stampa solo 3

<details>
<summary>💡 Spiegazione</summary>
Senza graffe, l’<code>if</code> controlla solo la riga 1.  
Condizione falsa → riga 1 saltata.  
Riga 2 e 3 sono istruzioni indipendenti: vengono eseguite.  
<strong>Regola d’oro: graffe sempre.</strong>
</details>

#### 2. RUN (Esegui)
Digita e esegui:

```cpp
/**
 * @file autorizzazione_pos.cpp
 * @brief Verifica fondi e autorizza (o nega) un pagamento POS.
 */
#include <iostream>

/**
 * @brief Controlla saldo vs importo e aggiorna il saldo se possibile.
 * @return int 0 se la procedura è terminata.
 */
int main() {
    double saldoDisponibile = 45.00;
    double importoSpesa = 62.50;

    std::cout << "=== TERMINALE PAGAMENTI POS ===\n";
    std::cout << "Importo richiesto: " << importoSpesa << " EUR\n";
    std::cout << "Verifica disponibilita...\n\n";

    if (saldoDisponibile >= importoSpesa) {
        /// Flag locale: esiste SOLO dentro questo blocco
        bool autorizzato = true;

        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << ">>> TRANSAZIONE APPROVATA <<<\n";
        std::cout << "Nuovo saldo: " << saldoDisponibile << " EUR\n";
    } else {
        /// Esiste SOLO dentro l'else
        double importoMancante = importoSpesa - saldoDisponibile;

        std::cout << ">>> TRANSAZIONE NEGATA <<<\n";
        std::cout << "Credito insufficiente.\n";
        std::cout << "Importo mancante: " << importoMancante << " EUR\n";
    }

    std::cout << "\nOperazione conclusa.\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Con i valori dell’esempio (`saldo = 45`, `importo = 62.50`):

| Punto | Cosa succede |
|-------|----------------|
| Condizione `saldo >= importo` | `false` |
| Ramo eseguito | `else` |
| `importoMancante` | `17.50` (visibile solo dentro l’else) |
| Dopo l’`if-else` | messaggio “Operazione conclusa” |

Prova a cambiare `importoSpesa` in `30.00` e riesegui: ora si attiva il ramo `if` e il saldo viene aggiornato.

> 🔗 Ispeziona lo stack su [Python Tutor C++](https://pythontutor.com/cpp.html): nota che `autorizzato` e `importoMancante` nascono e muoiono nei rispettivi blocchi.

#### 4. MODIFY (Modifica)
1. **Guardiano sottoscorta**  
   Aggiungi `int rotoloCartaTermica = 3;`.  
   Con un `if` **semplice** (senza else): se `< 5`, stampa un allarme per sostituire il rotolo.

2. **Micro-pagamento**  
   Se `importoSpesa < 10.00`, aggiungi una commissione fissa di `0.30` **prima** del controllo sul saldo.

3. **Prova di scope**  
   Prova a stampare `autorizzato` o `importoMancante` **dopo** la chiusura dell’`if-else`.  
   Il compilatore deve rifiutare (variabile non dichiarata in quello scope).

#### 5. MAKE (Crea)
**Scenario SIA — Controllo accessi al caveau**

Scrivi `controllo_caveau.cpp`:

- `const int PIN_SEGRETO = 4821;`
- `int pinInserito` (es. `4821`)
- `bool badgeDirigente` (`true` / `false`)
- **Regola:** apri il caveau **solo se** PIN corretto **e** badge dirigente (`&&`)
  - se ok → messaggio di benvenuto / sblocco
  - altrimenti → “ACCESSO NEGATO” + attivazione telecamere
- Nel ramo `else`, se `pinInserito != 0`, aggiungi anche: tentativo registrato nel log

**Requisiti:** Doxygen, commenti `///`, graffe su tutti i blocchi, indentazione chiara.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Controllo accessi caveau (PIN + badge dirigente).
 */
#include <iostream>

int main() {
    const int PIN_SEGRETO = 4821;
    // dichiara pinInserito e badgeDirigente
    // if-else con la regola di sicurezza
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `if` = azione opzionale; `if-else` = bivio a due vie (un solo ramo eseguito).
- **Mai** `;` subito dopo la condizione.
- **Sempre** le graffe `{ }`, anche per una sola istruzione.
- Variabili dichiarate dentro un blocco esistono **solo** lì (scope).
- Condizioni complesse: combina con `&&` e `||` (già visti nel capitolo sulle espressioni).

---

### ➡️ Prossimo chunk
Quando i bivi diventano **più di due** (es. fasce di sconto, giudizi, stati di un ordine) un solo `if-else` non basta.  
Passeremo a catene `if / else if / else` e alle regole per non perdere il controllo del flusso.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: if e if-else + tranelli + scope
  [x] Metafora tornello
  [x] Quiz sintassi corretta
  [x] Predict sulla trappola delle graffe mancanti
  [x] PRIMM su terminale POS
  [x] Make su caveau (SIA / sicurezza)
  [x] else-if non introdotto (solo annunciato)
-->
