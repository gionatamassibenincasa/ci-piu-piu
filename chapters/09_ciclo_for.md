## ⏳ Capitolo 9: Il Contatore Compatto (Il Ciclo for)

> "La regolarità e la prevedibilità sono le migliori alleate della precisione contabile."
> — *Principio di Revisione Aziendale*

Nel capitolo precedente abbiamo scoperto il ciclo `while`, ideale quando **non sappiamo a priori** quante volte dovremo ripetere un'azione (come la cassa che batte scontrini finché il cliente non ha finito gli articoli).

Tuttavia, in moltissimi contesti aziendali il numero di ripetizioni è **noto e prestabilito fin dall'inizio**:
- Calcolare l'ammortamento contabile di un cespite per **5 anni**.
- Elaborare le buste paga dei **12 mesi** dell'esercizio.
- Stampare il piano di rimborso di un finanziamento in **24 rate**.

Anche per questi problemi potremmo usare un `while`, ma c'è un rischio: i tre ingredienti vitali (inizializzazione, condizione e aggiornamento) si trovano sparpagliati in punti diversi del file. Dimenticare l'aggiornamento in fondo a un blocco lungo è un errore comunissimo.

Per risolvere questo problema, il C++ mette a disposizione il ciclo **`for`**: un costrutto compatto che raccoglie l'intero meccanismo di controllo in una sola riga chiara e ordinata.

---

### 💡 La Metafora: Il Cronometro di Precisione con Timer

> 💡 **Metafora:**  
> Pensa all'impostazione di un timer sul microonde o su una macchina industriale:
> - Nel `while`, dovevi ricordarti tu a mano di accendere il timer prima di entrare nella stanza, controllare l'orologio a ogni secondo e avanzare le lancette prima di uscire.
> - Nel **`for`**, imposti tutto direttamente sul display all'inizio:  
>   *"Parti da 1; fermati a 5; aumenta di 1 a ogni scatto"*.  
> - La macchina esegue la sequenza con precisione millimetrica senza che tu possa dimenticare di mandare avanti il contatore.

---

### 🔍 Il `for` come Forma Compatta del `while`

Dal punto di vista del calcolatore, il ciclo `for` non fa nulla che il `while` non sapesse già fare: è una forma di scrittura più comoda ed elegante (talvolta chiamata *zucchero sintattico*), pensata per aiutare la mente del programmatore a **non dimenticare i passaggi chiave**.

Osserva come i due costrutti si corrispondono riga per riga:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

rectangle "Con il ciclo WHILE" as W {
  [1. int i = 1; (Inizializzazione)]
  --> [2. while (i <= 5) (Condizione)]
  --> [Corpo: elabora dato]
  --> [3. i++; (Aggiornamento)]
}

rectangle "Con il ciclo FOR (Tutto in una riga!)" as F {
  [for ( 1. int i = 1 ;  2. i <= 5 ;  3. i++ )]
  --> [Corpo: elabora dato]
}
@enduml
```

#### Anatomia dell'Intestazione del `for`
L'intestazione è separata da **due punti e virgola `;` obbligatori**:

```cpp
for (inizializzazione ; condizione / predicato ; aggiornamento) {
    // Istruzioni da ripetere
}
```

1. **Inizializzazione (`int i = 1;`):** viene eseguita **una sola volta**, all'inizio assoluto del ciclo. In C++ moderno dichiariamo la variabile contatore direttamente qui dentro: in questo modo il contatore nasce e vive *solo* dentro il ciclo, evitando di sporcare la memoria esterna!
2. **Condizione / Predicato (`i <= 5;`):** viene testata **prima di ogni giro**. Se è vera, si esegue il blocco; se è falsa, si esce immediatamente.
3. **Aggiornamento (`i++`):** viene eseguito automaticamente **al termine di ogni giro**, subito prima di ritestare la condizione.

---

### 🔬 Laboratorio PRIMM: Il Piano di Ammortamento Cespiti

Nell'economia aziendale, i beni strumentali durevoli (computer, macchinari, veicoli) perdono valore ogni anno. Questo processo contabile si chiama **ammortamento a quote costanti**.

#### 1. PREDICT (Prevedi)
? Osserva questo ciclo `for`. Quante righe verranno stampate a video?
```cpp
for (int anno = 1; anno < 5; ++anno) {
    std::cout << "Esercizio contabile\n";
}
```
- [ ] 5 righe
- [x] 4 righe (per anno = 1, 2, 3, 4)
- [ ] 0 righe
- [ ] Il ciclo è infinito

<details>
<summary>💡 Spiegazione</summary>
Attenzione al classico errore <b>Off-by-One</b> (errore di uno):  
La condizione è <code>anno < 5</code> (strettamente minore), <b>non</b> <code>anno <= 5</code>!  
Il contatore assumerà i valori 1, 2, 3, 4 (esattamente <b>4 iterazioni</b>). Quando <code>anno</code> diventa 5, la condizione <code>5 < 5</code> è falsa e il ciclo si arresta prima di stampare la quinta volta.  
Se vuoi contare esattamente fino a 5, devi usare <code>anno <= 5</code>.
</details>

---

#### 2. RUN (Esegui)
Esamina il programma `piano_ammortamento.cpp`. Calcoliamo la quota e il valore residuo di un macchinario aziendale su un arco di 5 anni:

```cpp
/**
 * @file piano_ammortamento.cpp
 * @brief Calcolo del piano di ammortamento a quote costanti di un cespite aziendale.
 * @author Docente di Informatica - 3ª SIA
 * @date 2026-11-11
 */
#include <iostream>

/**
 * @brief Funzione principale: genera il prospetto contabile su N anni.
 * @return int Codice di uscita (0 = esecuzione regolare).
 */
int main() {
    /// Costo storico di acquisto del bene strumentale
    const double VALORE_INIZIALE = 20000.00;

    /// Numero di esercizi contabili di ammortamento previsti dal piano
    const int NUMERO_ANNI = 5;

    /// Quota annuale costante di ammortamento (ripartizione uniforme)
    const double QUOTA_ANNUA = VALORE_INIZIALE / NUMERO_ANNI;

    /// Valore contabile residuo del bene (decresce ogni anno)
    double valoreResiduo = VALORE_INIZIALE;

    std::cout << "=================================================" << "\n";
    std::cout << "    PIANO DI AMMORTAMENTO CESPITI AZIENDALI      " << "\n";
    std::cout << " Costo Storico: " << VALORE_INIZIALE << " EUR | Durata: " 
              << NUMERO_ANNI << " Anni" << "\n";
    std::cout << " Quota Annua  : " << QUOTA_ANNUA << " EUR/anno\n";
    std::cout << "=================================================" << "\n";
    std::cout << " Anno | Quota Ammortamento | Valore Residuo Fine Anno\n";
    std::cout << "-------------------------------------------------" << "\n";

    // CICLO FOR: Controllo compatto (inizializzazione, condizione, incremento)
    for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
        // Aggiorniamo il valore del bene scalando la quota annua
        valoreResiduo -= QUOTA_ANNUA;

        std::cout << "   " << anno << "  |     " 
                  << QUOTA_ANNUA << " EUR      |     " 
                  << valoreResiduo << " EUR\n";
    }

    std::cout << "-------------------------------------------------" << "\n";
    std::cout << "Cespite completamente ammortizzato. Valore finale: " 
              << valoreResiduo << " EUR\n";

    return 0;
}
```
@LIA.cpp

---

#### 3. INVESTIGATE (Investiga: Il Contatore e lo Scope nel `for`)

Visualizziamo passo dopo passo come il processore governa il contatore compatto del `for`:

🔗 **[Apri questo codice su Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0Aint%20main%28%29%20%7B%0A%20%20%20%20const%20int%20ANNI%20%3D%203%3B%0A%20%20%20%20double%20valore%20%3D%2015000.0%3B%0A%20%20%20%20double%20quota%20%3D%205000.0%3B%0A%0A%20%20%20%20for%20%28int%20anno%20%3D%201%3B%20anno%20%3C%3D%20ANNI%3B%20%2B%2Banno%29%20%7B%0A%20%20%20%20%20%20%20%20valore%20-%3D%20quota%3B%0A%20%20%20%20%20%20%20%20std%3A%3Acout%20%3C%3C%20anno%20%3C%3C%20%22%3A%20%22%20%3C%3C%20valore%20%3C%3C%20%22%5Cn%22%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%200%3B%0A%7D&mode=edit)**

Clicca su **"Visualize Execution"** e premi **"Next"** osservando lo stack a destra:
1. Quando l'esecuzione tocca la riga del `for`, nello stack viene creata la variabile `anno = 1`.
2. Il processore valuta la condizione `1 <= 3` (vera) ed entra nel corpo, aggiornando `valore`.
3. Al termine del corpo, la freccia torna alla riga del `for`: vedi che `anno` diventa `2`, e viene subito ritestata la condizione.
4. **Osserva cosa succede alla fine del 3° anno:** quando `anno` diventa `4`, la condizione `4 <= 3` è falsa.  
   La freccia esce dal ciclo e **la variabile `anno` scompare istantaneamente dallo stack!** Non esiste più al di fuori del ciclo (la regola dello scope del Locker!).

---

#### 4. MODIFY (Modifica: Sperimenta e Cambia)

1. **Il Fondo Ammortamento Cumulativo:** Dichiara una variabile `double fondoAmmortamento = 0.0;` prima del ciclo. A ogni giro, somma la quota al fondo (`fondoAmmortamento += QUOTA_ANNUA;`) e visualizzala nella tabella accanto al valore residuo.
2. **Ammortamento a Ritroso:** Modifica l'intestazione del ciclo per contare alla rovescia, partendo dall'anno 5 fino all'anno 1:
   ```cpp
   for (int anniRimanenti = NUMERO_ANNI; anniRimanenti >= 1; --anniRimanenti)
   ```
3. **La prova dello Scope:** Prova a scrivere `std::cout << anno;` subito dopo la graffa di chiusura del `for`. Che errore ti segnala il compilatore?  
   <details>
   <summary>💡 Spiegazione dell'errore di compilazione</summary>
   Riceverai: <code>error: 'anno' was not declared in this scope</code>.  
   Questo conferma che dichiarare il contatore dentro l'intestazione del <code>for</code> garantisce che la variabile non resti attiva per errore nel resto del programma.
   </details>

---

#### 5. MAKE (Crea: La Tua Sfida Autonoma)

> 🎯 **Sfida SIA: Il Piano di Crescita con Interesse Composto**  
> Un'impresa vincola un capitale di liquidità in un conto deposito remunerato per $N$ anni a tasso fisso. Ogni anno gli interessi maturati si sommano al capitale, generando a loro volta nuovi interessi (capitalizzazione composta).
> 
> Scrivi un programma C++ autonomo (`interesse_composto.cpp`):
> - Dichiara il capitale iniziale depositato: `double capitale = 10000.00;` (10.000 EUR).
> - Dichiara il tasso di interesse attivo annuo: `const double TASSO = 0.04;` (4%).
> - Dichiara la durata dell'investimento in anni: `const int ANNI_INVESTIMENTO = 6;`.
> - Utilizza un ciclo `for` a contatore (`anno = 1` fino a `ANNI_INVESTIMENTO`) per:
>   - Calcolare gli interessi maturati in quell'anno: `interessiAnno = capitale * TASSO;`.
>   - Incrementare il capitale: `capitale += interessiAnno;`.
>   - Stampare anno per anno: Anno, Interessi guadagnati nel periodo, e Nuovo Capitale Maturato.
> - Al termine del ciclo, calcola e visualizza il guadagno netto totale ottenuto dall'azienda al termine dei 6 anni (`capitaleFinale - 10000.00`).
> 
> **Requisiti di qualità:**
> - Intestazione Doxygen del file e della funzione `main`.
> - Commenti proporzionati `///` per descrivere le variabili finanziarie.
> - Formattazione ordinata dei dati in tabella.
