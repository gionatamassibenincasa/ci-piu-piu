## 🔁 Capitolo 12: Garantire l'Azione (Il Ciclo `do-while`)

> "Fidarsi è bene, validare l'input prima di registrarlo è sicurezza informatica."
> — *Regola Aurea dello Sviluppo Software*

`while` e `for` hanno il **controllo in testa**: se la condizione è già falsa, il corpo non gira **mai**.

A volte però un’azione deve avvenire **almeno una volta** prima di poter controllare:
- chiedere un importo (non puoi validarlo prima che esista);
- mostrare un menu e poi decidere se uscire.

Per questo esiste il **`do-while`**: controllo **in coda**.

> 💡 **Metafora: modulo online con campi obbligatori**  
> 1. La pagina ti mostra il form e tu compili (**il `do` gira almeno una volta**).  
> 2. Premi “Invia”: il sistema controlla (*controllo in coda*).  
> 3. Se c’è un errore, il form torna indietro e riprovi.  
> 4. Si ripete **finché** i dati non sono validi.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un `do-while` e spiegare la differenza con il `while`
- Usarlo per **validare un input** (ripeti finché il dato non è accettabile)
- Evitare la duplicazione di codice tipica del `while` “con lettura prima e dentro”

---

### ⚙️ Anatomia e confronto con `while`

```cpp
// do-while: il corpo gira almeno una volta
double importo;
do {
    std::cout << "Importo (> 0): ";
    std::cin >> importo;
} while (importo <= 0.0);
```

Equivalente scomodo con `while` (codice di lettura **duplicato**):

```cpp
std::cout << "Importo (> 0): ";
std::cin >> importo;
while (importo <= 0.0) {
    std::cout << "Importo (> 0): ";
    std::cin >> importo;
}
```

| | `while` / `for` | `do-while` |
|--|-----------------|------------|
| Controllo | in **testa** | in **coda** |
| Iterazioni minime | 0 | **1** |
| Uso tipico | conteggi, sentinella già nota | validazione input, menu “almeno una volta” |

**Attenzione alla sintassi:** dopo il `while (...)` del `do-while` serve il **`;`**.

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Esegui corpo (do);
while (Condizione ancora vera?) is (sì)
  :Esegui di nuovo il corpo;
endwhile (no)
:Esci;
stop
@enduml
```

---

### 🔬 Laboratorio PRIMM: Validazione importo bonifico

#### 1. PREDICT (Prevedi)
Quante volte viene eseguito il corpo?

```cpp
int n = 10;
do {
    std::cout << "giro\n";
    n = n + 1;
} while (n < 5);
```

[( )] 0 volte
[(X)] 1 volta
[( )] 5 volte
[( )] Infinito

<details>
<summary>💡 Spiegazione</summary>
Il corpo viene eseguito <strong>prima</strong> del controllo.  
Anche se <code>n &lt; 5</code> è già falso (10 &lt; 5), stampi comunque una volta <code>giro</code>, poi la condizione fallisce e usci.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file valida_bonifico.cpp
 * @brief Chiede un importo di bonifico finché non e' nel range ammesso.
 */
#include <iostream>

/**
 * @brief Valida importo in [1, 5000] con do-while.
 * @return int 0 se ok.
 */
int main() {
    const double MIN_BONIFICO = 1.0;
    const double MAX_BONIFICO = 5000.0;

    double importo = 0.0;

    // Sequenza simulata per demo: -10, 0, 250  (in classe usa cin nel loop)
    double tentativi[] = {-10.0, 0.0, 250.0};
    int t = 0;

    do {
        importo = tentativi[t++];
        std::cout << "Tentativo importo: " << importo << " EUR\n";
        if (importo < MIN_BONIFICO || importo > MAX_BONIFICO) {
            std::cout << "  Non valido (ammessi " << MIN_BONIFICO
                      << " .. " << MAX_BONIFICO << ")\n";
        }
    } while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);

    std::cout << "Bonifico accettato: " << importo << " EUR\n";
    return 0;
}
```
@LIA.cpp

> In laboratorio reale:
> ```cpp
> do {
>     std::cout << "Importo bonifico: ";
>     std::cin >> importo;
> } while (importo < MIN_BONIFICO || importo > MAX_BONIFICO);
> ```

#### 3. INVESTIGATE (Investiga)
Sequenza: `-10` → `0` → `250`

| Giro | importo | Valido? | Continua? |
|------|---------|---------|-----------|
| 1 | -10 | no | sì |
| 2 | 0 | no | sì |
| 3 | 250 | sì | **no** (esce) |

Il controllo avviene **dopo** ogni tentativo: ecco perché il primo giro c’è sempre.

#### 4. MODIFY (Modifica)
1. **Limite 3 tentativi**  
   Contatore `tentativi`. Se dopo 3 errori non è ancora valido, esci dal ciclo e stampa “sessione bloccata”.

2. **Menu “altra operazione?”**  
   Dopo un bonifico accettato, chiedi `S/N` in un `do-while` esterno e ripeti finché la risposta è `S`/`s`.

3. **Dimenticare il `;`**  
   Togli il punto e virgola dopo `while (...)`: osserva l’errore del compilatore.

#### 5. MAKE (Crea)
**Scenario SIA — PIN sportello con tentativi limitati**

Scrivi `pin_sportello.cpp`:

- `const int PIN_CORRETTO = 4821`
- L’utente inserisce un PIN (`int`)
- `do-while`: ripeti finché il PIN è sbagliato **e** i tentativi sono `< 3`
- Se indovina entro 3 prove → “Accesso consentito”
- Se esaurisce i tentativi → “Carta bloccata”
- Non rivelare il PIN corretto nei messaggi di errore

**Requisiti:** Doxygen, messaggi chiari, niente ciclo infinito.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Validazione PIN sportello con massimo 3 tentativi.
 */
#include <iostream>

int main() {
    const int PIN_CORRETTO = 4821;
    // tentativi, do-while, esiti
    return 0;
}
```

</details>

**Variante di sintesi (opzionale, se avete tempo in lab):**  
un mini menu cassa con `do-while` esterno + `switch` (nuova spesa / uscita), riusando sentinella e scaglioni già visti. Non è obbligatorio per chiudere il capitolo.

---

### 📝 Riepilogo tascabile
- `do-while` = esegui **poi** controlla → **almeno un** giro.
- Ideale per validare input e menu che devono apparire subito.
- Dopo `while (...)` del `do-while` non dimenticare il **`;`**.
- `while`/`for` restano la scelta giusta quando 0 iterazioni è accettabile.

---

### ➡️ Prossimo chunk
Chiudiamo il Blocco 1 con gli strumenti di “guida fine” del ciclo: **`break`**, **`continue`** e la formattazione professionale dei numeri con **`<iomanip>`**.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: do-while, validazione, almeno una iterazione
  [x] Metafora form online
  [x] Quiz sintassi corretta
  [x] Predict: una iterazione anche se condizione già falsa
  [x] PRIMM validazione bonifico
  [x] Make PIN con 3 tentativi (più mirato del mega-terminale)
  [x] Sintesi menu lasciata opzionale
  [x] break/iomanip solo annunciati
-->
