## ⏳ Capitolo 11: Il Contatore Compatto (Il Ciclo `for`)

> "La regolarità e la prevedibilità sono le migliori alleate della precisione contabile."
> — *Principio di Revisione Aziendale*

Il `while` è ideale quando **non sai quanti** giri farai (articoli al nastro, fatture fino alla sentinella).  
In azienda però molte ripetizioni sono **già note**: 5 anni di ammortamento, 12 mesi, 24 rate.

Con un `while` i tre ingredienti restano sparsi nel file: è facile dimenticare l’aggiornamento.  
Il ciclo **`for`** li raccoglie in **una sola riga**.

> 💡 **Metafora: timer del microonde / macchina industriale**  
> Imposti sul display: *“Parti da 1; fermati a 5; avanza di 1 a ogni scatto”*.  
> La macchina esegue la sequenza senza che tu debba ricordarti di far avanzare il contatore a mano.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un `for` con inizializzazione, condizione e aggiornamento nell’intestazione
- Usarlo quando il numero di ripetizioni è noto a priori
- Capire lo **scope** del contatore dichiarato nell’intestazione

---

### 🔍 `for` = `while` in forma compatta

```cpp
// while equivalente
int anno = 1;
while (anno <= 5) {
    // corpo
    anno = anno + 1;
}

// stessa logica con for
for (int anno = 1; anno <= 5; ++anno) {
    // corpo
}
```

| Parte nell’intestazione `for` | Ruolo |
|-------------------------------|--------|
| `int anno = 1` | **Inizializzazione** (una sola volta, all’ingresso) |
| `anno <= 5` | **Condizione** (prima di ogni iterazione) |
| `++anno` | **Aggiornamento** (dopo ogni corpo) |

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Init contatore;
while (Condizione?) is (sì)
  :Corpo;
  :Aggiorna contatore;
endwhile (no)
stop
@enduml
```

**Scope:** se dichiari il contatore nell’intestazione (`for (int anno = …)`), `anno` **non esiste** fuori dal ciclo.

---

### 🔬 Laboratorio PRIMM: Piano di ammortamento

#### 1. PREDICT (Prevedi)
Quante righe stampa questo ciclo?

```cpp
for (int i = 0; i < 5; ++i) {
    std::cout << i << "\n";
}
```

[( )] 5 righe: `1 2 3 4 5`
[(X)] 5 righe: `0 1 2 3 4`
[( )] 4 righe: `0 1 2 3`
[( )] Ciclo infinito

<details>
<summary>💡 Spiegazione</summary>
<code>i</code> parte da <code>0</code>; la condizione è <code>i &lt; 5</code>; dopo ogni giro <code>++i</code>.  
Valori stampati: 0, 1, 2, 3, 4 — cinque righe. In C++ i conteggi “da zero” sono la norma (come gli indici degli array che vedrai più avanti).
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ammortamento_cespite.cpp
 * @brief Piano di ammortamento a quote costanti su N anni.
 */
#include <iostream>

/**
 * @brief Stampa tabella anno / quota / valore residuo.
 * @return int 0 se ok.
 */
int main() {
    const double COSTO_CESPITE = 10000.0;
    const int NUMERO_ANNI = 5;
    const double QUOTA_ANNUA = COSTO_CESPITE / NUMERO_ANNI;

    double valoreResiduo = COSTO_CESPITE;

    std::cout << "Anno\tQuota\tResiduo\n";
    std::cout << "----\t-----\t-------\n";

    for (int anno = 1; anno <= NUMERO_ANNI; ++anno) {
        valoreResiduo -= QUOTA_ANNUA;
        std::cout << anno << "\t" << QUOTA_ANNUA << "\t" << valoreResiduo << "\n";
    }

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Con 5 anni e cespite 10000:

| anno | Quota | Residuo dopo |
|------|-------|--------------|
| 1 | 2000 | 8000 |
| 2 | 2000 | 6000 |
| … | … | … |
| 5 | 2000 | 0 |

Il contatore `anno` nasce nell’intestazione del `for` e **muore** alla graffa di chiusura.

> 🔗 Segui `anno` e `valoreResiduo` su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Fondo ammortamento**  
   Prima del ciclo: `double fondo = 0.0;`.  
   A ogni giro: `fondo += QUOTA_ANNUA;` e stampalo in tabella.

2. **Conto alla rovescia**  
   ```cpp
   for (int anniRimanenti = NUMERO_ANNI; anniRimanenti >= 1; --anniRimanenti)
   ```
   Adatta la stampa in modo coerente.

3. **Prova di scope**  
   Dopo il `for`, prova `std::cout << anno;`.  
   Il compilatore deve segnalare che `anno` non è dichiarato in quello scope.

#### 5. MAKE (Crea)
**Scenario SIA — Interesse composto su deposito aziendale**

Scrivi `interesse_composto.cpp`:

- `double capitale = 10000.00`
- `const double TASSO = 0.04` (4% annuo)
- `const int ANNI = 6`
- Ciclo `for` da anno 1 a `ANNI`:
  - interessi dell’anno = `capitale * TASSO`
  - aggiorna `capitale`
  - stampa: anno, interessi, nuovo capitale
- A fine ciclo: guadagno netto = capitale finale − 10000

**Requisiti:** Doxygen, `///` sulle grandezze finanziarie, tabella leggibile.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Simula capitalizzazione composta su N anni.
 */
#include <iostream>

int main() {
    // capitale, tasso, anni; for; stampa guadagno netto
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `for` = quando il numero di ripetizioni è **noto** (o facile da esprimere con un contatore).
- Intestazione: `init; condizione; aggiornamento`.
- Contatore dichiarato nel `for` → scope limitato al ciclo.
- Stesso potere del `while`; forma più sicura per i conteggi regolari.
- Per input a sentinella resta preferibile il `while`.

---

### ➡️ Prossimo chunk
A volte il corpo del ciclo deve girare **almeno una volta** (es. chiedere un dato finché non è valido).  
Entra in scena il **`do-while`**: controllo in coda.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: for, contatore, scope
  [x] Metafora timer
  [x] Quiz sintassi corretta
  [x] Predict conteggio da 0
  [x] PRIMM ammortamento cespite
  [x] Make interesse composto (SIA)
  [x] do-while solo annunciato
-->
