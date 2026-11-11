## 🔁 Capitolo 10: Garantire l'Azione (Il Ciclo do-while e la Validazione dell'Input)

> "Fidarsi è bene, validare l'input prima di registrarlo è sicurezza informatica."
> — *Regola Aurea dello Sviluppo Software*

Nei capitoli precedenti abbiamo esplorato il ciclo `while` e il ciclo `for`: entrambi hanno il **controllo in testa**, il che significa che se la condizione di partenza è falsa, il corpo del ciclo non viene eseguito nemmeno una volta (zero iterazioni).

Tuttavia, esistono situazioni in cui **un'azione deve essere eseguita per forza almeno una volta**, prima ancora di poter fare qualsiasi verifica:
- Chiedere all'utente di digitare un dato (es. l'importo di un bonifico): non puoi controllare se l'importo è corretto prima che l'utente l'abbia inserito!
- Mostrare un menu operativo a video: devi prima mostrare le opzioni, consentire la scelta e solo dopo verificare se l'utente desidera uscire.

Per queste esigenze, il C++ offre il ciclo **`do-while`**: il costrutto con **controllo in coda**.

---

### 💡 La Metafora: Il Modulo con Campi Obbligatori

> 💡 **Metafora:**  
> Pensa alla compilazione di un modulo di pagamento su un sito bancario:
> - Prima di tutto, la pagina ti presenta il modulo e ti chiede di compilare i dati (**il blocco `do` viene eseguito almeno una volta**).
> - Quando premi "Invia", il sistema controlla:  
>   *"I dati inseriti contengono errori?"* (**controllo in coda**).
> - Se c'è un errore (es. importo negativo o superiore al massimale), il modulo ti viene ripresentato e sei costretto a correggerlo.
> - La richiesta si ripete **finché la condizione di errore rimane vera** (cioè finché non inserisci un dato finalmente valido!).

---

### ⚙️ Il `do-while` come Comodità di Scrittura

Anche il `do-while` è una forma comoda ed elegante di scrittura che evita la duplicazione del codice.

Se volessimo validare un input usando solo un normale `while`, dovremmo copiare e incollare l'istruzione di lettura due volte (una volta prima del ciclo e una volta dentro):

```cpp
// VALIDAZIONE SCOMODA CON IL WHILE (codice duplicato):
std::cout << "Inserisci importo: ";
std::cin >> importo; // <-- 1a lettura duplicata
while (importo <= 0.0) {
    std::cout << "Errore! Inserisci importo: ";
    std::cin >> importo; // <-- 2a lettura duplicata
}
```

Con il `do-while`, la richiesta viene scritta **una sola volta**, garantendo che venga eseguita subito e poi ripetuta all'occorrenza:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

start
repeat
  :1. Esegui il corpo (es. Chiedi dato da tastiera);
repeat while (2. Il dato e' ERRATO?) is (VERO: ripeti richiesta)
->FALSO: dato valido;
:Prosegui con l'operazione bancaria;
stop
@enduml
```

#### ⚠️ La Logica della Condizione: Ripetere Finché C'è un Errore
Fai molta attenzione alla domanda posta nel `while` in coda:
- La condizione tra parentesi **non indica quando il dato è valido**, ma stabilisce **quando il ciclo deve continuare a ripetersi**!
- Si ripete **finché la negazione della condizione di validità è soddisfatta** (cioè finché il dato inserito è errato).

```cpp
// Vogliamo che l'importo sia compreso tra 1€ e 5.000€ (dato valido: importo > 0 && importo <= 5000)
// Il ciclo deve ripetersi finche il dato e FUORI dai limiti:
do {
    std::cout << "Importo bonifico (max 5000 EUR): ";
    std::cin >> importo;
} while (importo <= 0.0 || importo > 5000.0); // <-- Ripeti finche e NON valido!
```

> ⚠️ **Sintassi: Il Punto e Virgola Finale Obbligatorio!**  
> A differenza dell'`if`, del `while` normale e del `for`, l'istruzione `do { ... } while (condizione);` **richiede tassativamente il punto e virgola `;` finale** dopo la parentesi tonda di chiusura. Se lo dimentichi, il compilatore segnalerà un errore di sintassi.

---

### 🧭 Quadro Comparativo Finale: Quale Ciclo Scegliere?

Con l'introduzione del `do-while`, hai completato la triade fondamentale dei cicli in C++. Ecco la guida rapida per scegliere a colpo sicuro:

| Situazione Operativa | Ciclo Consigliato | Perché questa scelta? |
| :--- | :--- | :--- |
| **Iterazione Definita:** Conosciamo già a priori il numero esatto di passaggi ($N$ anni, 12 mesi, dimensione nota). | **`for`** | Raccoglie contatore, limite e incremento in una riga compatta ed elegante. |
| **Iterazione Indefinita (0 o più volte):** Dipende da un evento esterno o sentinella, e potremmo non dover eseguire nulla se la condizione iniziale è già falsa. | **`while`** | Il controllo in testa garantisce la sicurezza prima di compiere qualsiasi azione. |
| **Validazione Input o Menu (almeno 1 volta):** L'azione deve essere necessariamente compiuta prima di poter verificare l'esito. | **`do-while`** | Garantisce la prima esecuzione senza duplicare il codice di richiesta. |

---

### 🔬 Laboratorio PRIMM: Il Bonifico Bancario Protetto

Realizziamo il modulo di acquisizione sicura dell'importo per un bonifico bancario aziendale.

#### 1. PREDICT (Prevedi)
? Osserva questo codice in cui la condizione è falsa fin dall'inizio. Cosa verrà stampato a video?
```cpp
int tentativi = 10;
do {
    std::cout << "Controllo eseguito ";
} while (tentativi < 3);
std::cout << "Fine";
```
- [ ] Stampa solo `Fine`
- [x] Stampa `Controllo eseguito Fine`
- [ ] Il ciclo è infinito
- [ ] Errore di compilazione per il punto e virgola

<details>
<summary>💡 Spiegazione</summary>
Il ciclo <code>do-while</code> ha il <b>controllo in coda</b>: il computer esegue prima il corpo del <code>do</code> (stampando <code>"Controllo eseguito "</code>) e solo <i>dopo</i> valuta la condizione <code>10 < 3</code>.  
Poiché 10 non è minore di 3, la condizione risulta <code>false</code> e il ciclo si interrompe, stampando infine <code>"Fine"</code>.  
Anche con una condizione falsa in partenza, il <code>do-while</code> garantisce <b>sempre almeno un'esecuzione</b>!
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `bonifico_sicuro.cpp`. L'algoritmo obbliga l'utente a reinserire l'importo finché non rispetta le regole aziendali di sicurezza:

```cpp
/**
 * @file bonifico_sicuro.cpp
 * @brief Acquisizione e validazione robusta dell'importo per un bonifico bancario.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Funzione principale: valida l'importo e conferma la disposizione bancaria.
 * @return int Codice di stato (0 = operazione autorizzata).
 */
int main() {
    /// Massimale di sicurezza giornaliero per bonifici online
    const double MASSIMALE_GIORNALIERO = 5000.00;

    /// Variabile per l'importo inserito dal cliente
    double importoBonifico = 0.0;

    std::cout << "==========================================" << "\n";
    std::cout << "      DISPOSIZIONE BONIFICO BANCARIO      " << "\n";
    std::cout << " Vincoli: importo > 0 e max 5.000,00 EUR  " << "\n";
    std::cout << "==========================================" << "\n\n";

    // CICLO DO-WHILE: La richiesta viene eseguita almeno una volta
    // e ripetuta finche la condizione di validita e violata (negazione)
    do {
        std::cout << "Inserisci l'importo da trasferire (EUR): ";
        std::cin >> importoBonifico;

        // Feedback immediato se il dato non rispetta i vincoli
        if (importoBonifico <= 0.0) {
            std::cout << ">>> ERRORE: L'importo deve essere positivo e maggiore di zero!\n\n";
        } else if (importoBonifico > MASSIMALE_GIORNALIERO) {
            std::cout << ">>> ERRORE: Importo superiore al massimale di " 
                      << MASSIMALE_GIORNALIERO << " EUR!\n\n";
        }

    } while (importoBonifico <= 0.0 || importoBonifico > MASSIMALE_GIORNALIERO);

    // Se arriviamo qui, il dato e matematicamente garantito come valido
    std::cout << "\n==========================================" << "\n";
    std::cout << ">>> DISPOSIZIONE ACQUISITA CON SUCCESSO <<<" << "\n";
    std::cout << "Importo autorizzato : " << importoBonifico << " EUR\n";
    std::cout << "Commissione servizio: 1.00 EUR\n";
    std::cout << "Totale addebitato   : " << (importoBonifico + 1.00) << " EUR\n";
    std::cout << "==========================================" << "\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Controllo in Coda nello Stack)

Visualizziamo passo dopo passo come il processore esegue il corpo prima di arrivare alla guardia in fondo:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20double%20importo%20%3D%200.0%3B%0A%20%20%20%20int%20passaggio%20%3D%200%3B%0A%0A%20%20%20%20do%20%7B%0A%20%20%20%20%20%20%20%20passaggio%2B%2B%3B%0A%20%20%20%20%20%20%20%20//%20Simuliamo%20l'inserimento%3A%20al%201%C2%B0%20giro%20dato%20errato%2C%20al%202%C2%B0%20valido%0A%20%20%20%20%20%20%20%20if%20%28passaggio%20%3D%3D%201%29%20importo%20%3D%20-20.0%3B%0A%20%20%20%20%20%20%20%20else%20importo%20%3D%20250.0%3B%0A%0A%20%20%20%20%7D%20while%20%28importo%20%3C%3D%200.0%20%7C%7C%20importo%20%3E%205000.0%29%3B%0A%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20%22Importo%20valido%3A%20%22%20%3C%3C%20importo%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"**:
1. All'avvio, il cursore entra direttamente nel blocco `do` senza fermarsi a controllare alcuna guardia.
2. Alla riga del `while (importo <= 0.0 || importo > 5000.0)`:
   - Al primo passaggio, `importo` vale `-20.0`. La condizione di errore è `true`.
   - Il cursore **risale alla parola `do`** per eseguire nuovamente il corpo.
3. Al secondo passaggio, `importo` vale `250.0`. La condizione di errore diventa `false`.
4. Il cursore supera il punto e virgola ed esce definitivamente dal ciclo!

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Limite Massimo di 3 Tentativi di Inserimento:** Aggiungi un contatore `int tentativi = 0;`. Incrementalo a ogni giro. Se l'utente sbaglia per 3 volte consecutive, interrompi il ciclo e stampa: *"SESSIONE BLOCCATA: Raggiunto il limite massimo di errori per motivi di sicurezza."*.
2. **Ciclo di Vita con Menu ("Vuoi fare un'altra operazione?"):** Avvolgi l'intero programma all'interno di un ulteriore ciclo `do-while` esterno con una variabile `char risposta;`. Al termine di ogni bonifico chiedi: *"Vuoi disporre un altro bonifico? (S/N): "* e ripeti finché `risposta == 'S' || risposta == 's'`.

---

#### 5. MAKE (Crea: Il Capolavoro di Fine Blocco 1)

> 🏆 **La Sfida Finale del Blocco 1: Il Terminale Cassa Integrato**  
> Metti a frutto **tutto ciò che hai imparato nel Blocco 1** (variabili, costanti, operatore ternario, `if-else`, `switch`, `while` e `do-while`) creando il prototipo del software di cassa per un negozio al dettaglio.
> 
> Scrivi un programma C++ completo (`terminale_cassa_completo.cpp`):
> 
> 1. **Loop Principale (`do-while`):** Il programma mostra il menu principale e continua a funzionare finché l'operatore non sceglie l'opzione di chiusura cassa (`0`).
> 2. **Menu di Selezione (`switch-case`):**
>    - `Tasto 1 - Nuova Spesa Cliente:`
>      - Usa un ciclo `while` con sentinella `0.0` per battere i prezzi degli articoli nel carrello e calcolare il totale spesa.
>      - Con un `if-else if-else`, applica gli scaglioni di sconto fedeltà sul totale:
>        - Spesa < 50€: 0% sconto.
>        - Tra 50€ e 100€: 5% sconto.
>        - Oltre 100€: 10% sconto.
>      - Usa l'**operatore ternario (`?:`)** per verificare se regalare una shopper ecologica (`spesaScontata > 30.0 ? "Shopper Omaggio" : "Nessun omaggio"`).
>    - `Tasto 2 - Ricarica Carta Prepagata Punto Vendita:`
>      - Usa un `do-while` per validare l'importo della ricarica (deve essere compreso tra 5€ e 200€).
>    - `Tasto 0 - Chiusura Giornaliera di Cassa ed Uscita:`
>      - Stampa il messaggio di arrivederci e termina.
>    - `default:`
>      - Avvisa che il tasto premuto non è valido.
> 
> **Requisiti di qualità professionale:**
> - Intestazione Doxygen completa su file e `main`.
> - Commenti proporzionati `///` sulle regole di business e sulle costanti.
> - Codice ben indentato e suddiviso logicamente in sezioni.
