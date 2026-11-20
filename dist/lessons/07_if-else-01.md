<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-12
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/06_espressioni-ternario-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/08_bivi-complessi-01.md)

---


## 🚦 Bivi e Decisioni: `if` e `if-else`

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
- Scrivere un `if` o un `if-else` con graffe per scegliere il ramo corretto

---

### ⚙️ Prima del laboratorio: i due modelli

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

### 🧭 Prima del laboratorio: costruire una condizione

Una condizione produce `true` o `false`. Il tornello apre solo quando la sua
regola è vera; se servono due controlli, `&&` significa che devono superarsi
entrambi.

| Condizione | Significato al tornello |
|------------|-------------------------|
| `saldo >= importo` | Il credito basta per il pagamento. |
| `pinInserito == PIN_SEGRETO` | Il codice è corretto. |
| `pinInserito == PIN_SEGRETO && badgeDirigente` | PIN e badge sono validi. |

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

Dopo la `)` della condizione **non va mai** il `;`: il codice compila, ma il
blocco successivo non appartiene più all'`if` e viene eseguito sempre.

**2. Graffe**

Senza `{ }` l’`if` controlla **solo** la prima istruzione successiva.  
**Usa sempre le graffe**, anche per una sola riga.

---

### 🔬 Laboratorio PRIMM: Terminale pagamenti POS

Il terminale decide se autorizzare un pagamento confrontando saldo e importo.

#### 1. PREDICT (Prevedi)


Senza graffe, quante righe controlla l'if?

```cpp
if (scorte < 5)
    std::cout << "1\n";
    std::cout << "2\n";
```

[( )] Entrambe le cout
[(X)] Solo la prima cout
[( )] Nessuna


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
        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << ">>> TRANSAZIONE APPROVATA <<<\n";
        std::cout << "Nuovo saldo: " << saldoDisponibile << " EUR\n";
    } else {
        std::cout << ">>> TRANSAZIONE NEGATA <<<\n";
        std::cout << "Credito insufficiente.\n";
        std::cout << "Importo mancante: "
                  << importoSpesa - saldoDisponibile << " EUR\n";
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
| `importoSpesa - saldoDisponibile` | `17.50` |
| Dopo l’`if-else` | messaggio “Operazione conclusa” |

Prova a cambiare `importoSpesa` in `30.00` e riesegui: ora si attiva il ramo `if` e il saldo viene aggiornato.

> 🔗 Ispeziona lo stack su [Python Tutor C++](https://pythontutor.com/cpp.html):
> osserva saldo, importo e il ramo che viene eseguito.

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
if (saldoDisponibile >= importoSpesa) {
    std::cout << "Approvato\n";
} else {
    std::cout << "Negato\n";
}
```

</details>

1. **Guardiano sottoscorta**  
   Aggiungi `int rotoloCartaTermica = 3;`.  
   Con un `if` **semplice** (senza else): se `< 5`, stampa un allarme per sostituire il rotolo.

2. **Micro-pagamento**  
   Se `importoSpesa < 10.00`, aggiungi una commissione fissa di `0.30` **prima** del controllo sul saldo.

3. **Importo esatto**
   Cambia `importoSpesa` in `45.00`. Prevedi e verifica quale ramo si attiva:
   il confronto include anche il caso in cui saldo e importo sono uguali.

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
    /// TODO: spiega perché servono due controlli di sicurezza.
    // TODO: dichiara pinInserito e badgeDirigente, poi scrivi l'if-else
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `if` = azione opzionale; `if-else` = bivio a due vie (un solo ramo eseguito).
- **Mai** `;` subito dopo la condizione.
- **Sempre** le graffe `{ }`, anche per una sola istruzione.
- `&&` richiede che entrambe le condizioni siano vere.

---

### ➡️ Prossimo chunk
Quando i bivi diventano **più di due** (es. fasce di sconto, giudizi, stati di un ordine) un solo `if-else` non basta.  
Passeremo a catene `if / else if / else` e alle regole per non perdere il controllo del flusso.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: if e if-else con condizioni semplici o composte
  [x] Metafora tornello
  [x] Quiz sintassi corretta
  [x] Predict sulla trappola delle graffe mancanti
  [x] PRIMM su terminale POS
  [x] Make su caveau (SIA / sicurezza)
  [x] else-if non introdotto (solo annunciato)
-->


