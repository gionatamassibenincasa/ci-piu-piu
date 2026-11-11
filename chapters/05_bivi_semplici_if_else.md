## 🚦 Capitolo 5: Bivi e Decisioni (Il Costrutto if e if-else)

> "Le decisioni sono i binari su cui viaggiano i processi aziendali."
> — *Principio di Ingegneria Gestionale*

Fino ad ora i nostri programmi hanno marciato dritti come un treno su un unico binario: una riga dopo l'altra, dall'inizio alla fine. Ma il mondo reale non è mai una linea retta: un pagamento può essere **approvato o rifiutato**, una merce in magazzino può essere **esaurita o disponibile**, un cliente può avere o meno i requisiti per un prestito.

Per gestire queste situazioni, il C++ mette a disposizione il costrutto fondamentale di selezione: l'istruzione **`if`** (se) e la sua estensione **`if-else`** (se... altrimenti).

---

### 💡 La Metafora: Il Tornello Automatico di Sicurezza

> 💡 **Metafora:**  
> Pensa al **tornello d'accesso** all'ingresso della sede aziendale o della metropolitana:
> - **L'`if` semplice (senza `else`):** È un sensore di controllo "guardiano". Se rileva un'anomalia (es. allarme antincendio), attiva la sirena. Se non rileva nulla, non fa assolutamente niente e il flusso continua indisturbato.
> - **L'`if-else` (bivio a due vie):** È il lettore di badge al tornello:
>   - *SE (`if`)* passi un badge valido: il tornello si sblocca, la spia diventa verde e ti fa passare.
>   - *ALTRIMENTI (`else`)*: la spia diventa rossa, emette un segnale acustico d'errore e ti blocca l'ingresso.
>   - **Non esistono vie di mezzo:** o si attiva il ramo verde, o si attiva il ramo rosso. Mai entrambi contemporaneamente!

---

### 🔀 I Due Modelli di Selezione

#### 1. L'Istruzione `if` Semplice (Azione Condizionata)
Si usa quando vuoi eseguire un blocco di istruzioni **solo se si verifica una determinata condizione**. Se la condizione è falsa, l'azione viene semplicemente saltata.

```cpp
if (giacenzaMagazzino < LIVELLO_MINIMO) {
    std::cout << "ATTENZIONE: Scorte in esaurimento! Inviare ordine fornitore.\n";
}
```

#### 2. L'Istruzione `if-else` (Mutua Esclusione)
Si usa quando devi scegliere **esattamente una fra due strade alternative**:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
:Leggi Saldo e Importo Spesa;
if (Saldo >= Spesa?) then (VERO)
  :Transazione Approvata;
  :Scala importo dal Saldo;
else (FALSO)
  :Transazione Rifiutata;
  :Mostra avviso "Fondi Insufficienti";
endif
:Stampa scontrino finale;
stop
@enduml
```

---

### ⚠️ I Due Grandi Tranelli di Sintassi

I programmatori alle prime armi cadono spesso in due insidie classiche del C++:

1. **Il Punto e Virgola Traditore:**
   ```cpp
   // ERRORE GRAVISSIMO:
   if (saldo >= importo); // <-- QUEL PUNTO E VIRGOLA CHIUDE SUBITO L'IF!
   {
       std::cout << "Pagamento approvato!\n"; // Verrà eseguito SEMPRE!
   }
   ```
   Dopo la tonda della condizione dell'`if` **non va mai il punto e virgola**.

2. **Le Parentesi Graffe `{}` e lo "Scope" (Visibilità):**
   Se ometti le parentesi graffe, il C++ considera legata all'`if` **esclusivamente la prima istruzione successiva**. Per evitare bug nascosti e mantenere il codice sicuro, **usa sempre le graffe**, anche per una sola riga!
   Inoltre, qualsiasi variabile creata dentro un blocco `{}` nasce e muore lì dentro (non esiste al di fuori di quelle graffe).

---

### 🔬 Laboratorio PRIMM: Il Terminale Pagamenti POS

Sviluppiamo il sistema di autorizzazione dei pagamenti elettronici per un punto vendita.

#### 1. PREDICT (Prevedi)
? Osserva attentamente il seguente frammento di codice. Quali righe verranno stampate sul terminale?
```cpp
int scorte = 12;
if (scorte < 5)
    std::cout << "1. Ordina nuovi pezzi!\n";
    std::cout << "2. Notifica inviata al fornitore.\n";
std::cout << "3. Controllo terminato.\n";
```
- [ ] Non stampa nulla
- [ ] Stampa tutte e tre le righe: 1, 2 e 3
- [x] Stampa solo le righe 2 e 3
- [ ] Stampa solo la riga 3

<details>
<summary>💡 Spiegazione</summary>
Poiché non sono state usate le parentesi graffe <code>{}</code>, l'istruzione <code>if (scorte < 5)</code> controlla <b>soltanto</b> la prima riga successiva (la riga 1).  
Dato che <code>scorte < 5</code> è <code>false</code> (12 non è minore di 5), la riga 1 viene saltata.  
Ma la riga 2 ("Notifica inviata...") è un'istruzione indipendente, non appartiene all'if! Viene quindi eseguita, seguita dalla riga 3.  
<b>Regola d'oro:</b> usa sempre le parentesi graffe <code>{}</code> per racchiudere i blocchi decisionali!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma gestionale `autorizzazione_pos.cpp`. Nota come l'`if-else` garantisce la sicurezza della transazione finanziaria:

```cpp
/**
 * @file autorizzazione_pos.cpp
 * @brief Sistema di verifica e autorizzazione per pagamenti con carta POS.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Punto di ingresso: verifica i fondi disponibili e processa il pagamento.
 * @return int Codice di stato (0 = transazione conclusa).
 */
int main() {
    /// Saldo disponibile sulla carta prepagata del cliente
    double saldoDisponibile = 45.00;

    /// Importo totale della spesa battuta in cassa
    double importoSpesa = 62.50;

    std::cout << "=== TERMINALE PAGAMENTI POS ===" << "\n";
    std::cout << "Importo richiesto: " << importoSpesa << " EUR" << "\n";
    std::cout << "Verifica disponibilita in corso...\n\n";

    // Bivio decisionale a due rami (if-else)
    if (saldoDisponibile >= importoSpesa) {
        // Ramo VERO: I fondi sono sufficienti
        /// Flag locale di autorizzazione: esiste SOLO all'interno di questo blocco if
        bool autorizzato = true;

        saldoDisponibile = saldoDisponibile - importoSpesa;
        std::cout << ">>> TRANSAZIONE APPROVATA (" << (autorizzato ? "ESITO POSITIVO" : "") << ") <<<" << "\n";
        std::cout << "Nuovo saldo residuo: " << saldoDisponibile << " EUR" << "\n";
    } else {
        // Ramo FALSO: Fondi insufficienti
        /// Variabile locale per il debito residuo: esiste SOLO dentro l'else
        double importoMancante = importoSpesa - saldoDisponibile;

        std::cout << ">>> TRANSAZIONE NEGATA <<<" << "\n";
        std::cout << "Motivo: Credito insufficiente sulla carta." << "\n";
        std::cout << "Importo mancante : " << importoMancante << " EUR" << "\n";
    }

    std::cout << "\nGrazie per aver utilizzato i nostri servizi bancari.\n";
    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Bivio e la Visibilità nello Stack)

Ora è **obbligatorio** aprire Python Tutor per toccare con mano uno dei concetti più importanti e fraintesi della programmazione: la **visibilità (scope)** delle variabili.

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20saldo%20%3D%20100.00%3B%0A%20%20%20%20double%20spesa%20%3D%2062.50%3B%0A%0A%20%20%20%20if%20%28saldo%20%3E%3D%20spesa%29%20%7B%0A%20%20%20%20%20%20%20%20bool%20autorizzato%20%3D%20true%3B%0A%20%20%20%20%20%20%20%20saldo%20-%3D%20spesa%3B%0A%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Approvato%3A%20%22%20%3C%3C%20autorizzato%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20double%20importoMancante%20%3D%20spesa%20-%20saldo%3B%0A%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Negato%5Cn%22%3B%0A%20%20%20%20%7D%0A%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi il tasto **"Next"** passo dopo passo, tenendo gli occhi fissi sul riquadro **Frames (Stack)** a destra.

> ❓ **Domanda Guida Obbligatoria:**  
> **"Cosa succede alla variabile `autorizzato` quando il cursore di esecuzione esce dalla parentesi graffa di chiusura `}` dell'if?"**

Osserva cosa accade a schermo:
1. All'ingresso nel blocco `if`, nello stack viene riservato uno spazio per `autorizzato = true`.
2. Appena l'esecuzione raggiunge e supera la parentesi graffa `}`, **la variabile `autorizzato` scompare letteralmente dallo stack!**

> 💡 **La Metafora del Locker Temporaneo:**  
> Immagina che aprire una parentesi graffa `{` equivalga ad attivare uno **scomparto locker a noleggio istantaneo**:  
> - Ci depositi dentro il pacco (`bool autorizzato = true;`).  
> - Puoi usarlo liberamente finché rimani all'interno di quella stanza delimitata dalle graffe `{ ... }`.  
> - Ma non appena varchi la soglia della graffa di chiusura `}`, **lo scompartimento si sigilla e diventa inaccessibile**: la serratura scatta e il vano viene rimosso dal sistema.  
> 
> Se subito dopo la graffa provi a scrivere `std::cout << autorizzato;`, per il compilatore è come chiedere il pacco a uno sportello che **non esiste più nel magazzino**: riceverai l'errore bloccante:  
> `error: 'autorizzato' was not declared in this scope`.

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Aggiunta del Guardiano Sottoscorta (`if` semplice):** Aggiungi in testa al programma una variabile `int rotoloCartaTermica = 3;` (metri di carta rimasti nella stampante del POS). Se i metri sono inferiori a 5, stampa un messaggio di allarme: *"Attenzione: sostituire presto il rotolo di carta scontrini!"*. Usa un `if` semplice senza `else`.
2. **Commissione di Micro-Pagamento:** Se il pagamento è inferiore a `10.00€`, applica una commissione fissa di `0.30€` sommandola a `importoSpesa` prima di verificare se il saldo è sufficiente.
3. **La prova dell'errore di Scope:** Prova a scrivere `std::cout << autorizzato;` oppure `std::cout << importoMancante;` fuori dai rispettivi blocchi, subito prima di `return 0;`. Osserva l'errore del compilatore che rifiuta di compilare il programma!

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Controllo Accessi al Caveau Aziendale**  
> L'azienda di logistica custodisce merci di alto valore in un caveau blindato. L'accesso è regolato da una doppia verifica elettronica: codice PIN numerico e possesso del badge dirigente.
> 
> Scrivi un programma C++ autonomo (`controllo_caveau.cpp`):
> - Dichiara la costante con il PIN corretto: `const int PIN_SEGRETO = 4821;`.
> - Dichiara `int pinInserito`: il codice digitato dall'impiegato sul tastierino (es. `4821`).
> - Dichiara `bool badgeDirigente`: `true` se il dipendente ha passato il badge da supervisore.
> - **Regola di Sicurezza:**
>   - Con un `if-else`, autorizza l'apertura della porta solo se il PIN digitato è identico al PIN segreto **E** il badge dirigente è abilitato (`pinInserito == PIN_SEGRETO && badgeDirigente`).
>   - Se l'accesso è autorizzato, stampa a video: *"Sblocco serratura... Accesso al Caveau consentito. Benvenuto!"*.
>   - Nel ramo `else`, stampa: *"ACCESSO NEGATO: Credenziali errate! Attivazione telecamere di sicurezza."*.
>   - Inoltre, all'interno del ramo `else`, aggiungi un `if` semplice: se il PIN inserito era diverso da zero, stampa anche: *"Tentativo registrato nel log di sicurezza."*.
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti `///` sulle variabili e costanti.
> - Indentazione perfetta e graffe `{}` su tutti i blocchi.
