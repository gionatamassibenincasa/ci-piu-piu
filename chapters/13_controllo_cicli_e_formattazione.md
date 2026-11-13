## 🎯 Capitolo 13: Il Cruscotto del Programmatore (`break`, `continue`, `<iomanip>`)

> "La precisione nella presentazione dei numeri è l'abito formale con cui il software si presenta all'azienda."
> — *Principio dei Sistemi Contabili*

Prima di salire al Blocco 2 (funzioni e strutture dati) chiudiamo il Blocco 1 con due strumenti da “cruscotto”:

1. **Controllo fine dei cicli:** `break` e `continue`
2. **Output contabile leggibile:** header `<iomanip>` (`fixed`, `setprecision`, `setw`)

> 💡 **Metafore**  
> - **`break`** = pulsante rosso di emergenza: il nastro si **ferma subito**.  
> - **`continue`** = braccio di scarto: salta **quel** pezzo difettoso e passa al successivo.  
> - **`<iomanip>`** = stampante fiscale: centesimi sempre a due cifre, colonne allineate.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Usare `break` per uscire anticipatamente da un ciclo
- Usare `continue` per saltare il resto del corpo e passare all’iterazione successiva
- Formattare importi e tabelle con `std::fixed`, `std::setprecision` e `std::setw`

---

### ⚙️ `break` vs `continue`

| Istruzione | Effetto | Dove va il flusso |
|------------|---------|-------------------|
| `break;` | Interrompe il ciclo | subito **dopo** il ciclo |
| `continue;` | Salta il resto del corpo di **questa** iterazione | alla condizione / aggiornamento del ciclo |

```cpp
for (int i = 1; i <= 10; ++i) {
    if (i == 3) continue;   // salta il 3
    if (i == 8) break;      // ferma tutto a 8
    std::cout << i << " ";
}
// stampa: 1 2 4 5 6 7
```

---

### 🖨️ Formattazione con `<iomanip>`

```cpp
#include <iomanip>

std::cout << std::fixed << std::setprecision(2);
std::cout << std::setw(10) << 19.5 << "\n";  // es. "     19.50"
```

| Manipolatore | Ruolo |
|--------------|--------|
| `std::fixed` | Notazione fissa (non scientifica) |
| `std::setprecision(2)` | Cifre **dopo la virgola** (con `fixed`) |
| `std::setw(n)` | Larghezza minima del **prossimo** campo |
| `std::left` / `std::right` | Allineamento (testo a sx, importi a dx) |

Senza `fixed`, `setprecision(2)` conta le cifre significative totali e può produrre notazione scientifica: in ambito monetario **`fixed` è obbligatorio**.

---

### 🔬 Laboratorio PRIMM: Report fiscale con scarti e stop

Elaboriamo un elenco di transazioni: scartiamo le invalide e fermiamo gli allarmi.

#### 1. PREDICT (Prevedi)
Cosa stampa?

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

[( )] `12345`
[( )] `1345`
[(X)] `13`
[( )] `1234`

<details>
<summary>💡 Spiegazione</summary>
<code>i=1</code> stampa; <code>i=2</code> → <code>continue</code> (niente stampa); <code>i=3</code> stampa; <code>i=4</code> → <code>break</code> (esce). Risultato: <code>13</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file report_fiscale.cpp
 * @brief Report di transazioni con scarto, stop di sicurezza e formattazione.
 */
#include <iostream>
#include <iomanip>

/**
 * @brief Elabora 6 transazioni simulate: continue se <=0, break se >50000.
 * @return int 0 se ok.
 */
int main() {
    const double importi[] = {120.5, -3.0, 45.0, 12.75, 52000.0, 8.0};
    const int N = 6;

    double totale = 0.0;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << std::setw(4) << "ID" << std::setw(12) << "Importo" << "\n";
    std::cout << "----  ----------\n";

    for (int id = 1; id <= N; ++id) {
        double importo = importi[id - 1];

        if (importo <= 0.0) {
            std::cout << "  (scarto ID " << id << ": non positivo)\n";
            continue;
        }
        if (importo > 50000.0) {
            std::cout << "  ALERT antiriciclaggio ID " << id
                      << " — interrompo il report\n";
            break;
        }

        totale += importo;
        std::cout << std::setw(4) << id << std::setw(12) << importo << "\n";
    }

    std::cout << "----  ----------\n";
    std::cout << std::setw(4) << "" << std::setw(12) << totale << "  TOTALE\n";

    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
| ID | Importo | Azione |
|----|---------|--------|
| 1 | 120.50 | accumula |
| 2 | -3.00 | `continue` (scarto) |
| 3 | 45.00 | accumula |
| 4 | 12.75 | accumula |
| 5 | 52000 | `break` (stop) |
| 6 | 8.00 | **non elaborato** |

> 🔗 Osserva il salto di `continue`/`break` su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)
1. **Colonna IVA**  
   Per ogni riga valida stampa anche `importo * 0.22` con `setw`.

2. **Soglia micro-pagamenti**  
   Con `continue`, scarta anche gli importi `< 5.00`.

3. **Senza `fixed`**  
   Rimuovi `std::fixed` e osserva come cambia la stampa con solo `setprecision(2)`.

#### 5. MAKE (Crea)
**Scenario SIA — Liquidazione IVA trimestrale (semplificata)**

Scrivi `liquidazione_iva.cpp`:

- Ciclo su 6 fatture (ID 1…6) con imponibile e codice aliquota simulati in array (o costanti)
- Aliquote: `'O'` 22%, `'R'` 10%, `'M'` 4%, `'E'` 0%
- `continue` se imponibile `<= 0` (messaggio “fattura annullata”)
- `break` se imponibile `> 50000` (alert)
- Tabella formattata: `ID | Imponibile | Aliq. | IVA`
- A fine ciclo (o allo stop): totale imponibile e totale IVA

**Requisiti:** `#include <iomanip>`, `fixed` + `setprecision(2)`, Doxygen, `///` sulle aliquote.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Prospetto semplificato liquidazione IVA.
 */
#include <iostream>
#include <iomanip>

int main() {
    // dati, ciclo, continue/break, tabella, totali
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `break` = esci dal ciclo; `continue` = salta al giro successivo.
- In report contabili: scarti → `continue`; allarmi gravi → `break`.
- `<iomanip>`: `fixed` + `setprecision(2)` per i soldi; `setw` per le colonne.
- Senza `fixed`, `setprecision` non significa “due decimali monetari”.

---

### ➡️ Fine Blocco 1 — Prossimo orizzonte
Hai il controllo di dati, decisioni, cicli e presentazione.  
Nel **Blocco 2** spezzeremo i programmi in **funzioni**, introdurremo **array** e **struct** e costruiremo piccoli sistemi gestionali in memoria.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Obiettivo: break, continue, iomanip monetario
  [x] Metafore nastro / stampante fiscale
  [x] Quiz sintassi corretta
  [x] PRIMM report con scarti e alert
  [x] Make liquidazione IVA
  [x] Ponte esplicito a Blocco 2
-->
