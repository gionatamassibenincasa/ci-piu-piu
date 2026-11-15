<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-14
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/12_do-while-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_funzioni-01.md)

---


## 🎯 Il Cruscotto del Programmatore (`break` e `continue`)

> "La precisione nella presentazione dei numeri è l'abito formale con cui il software si presenta all'azienda."
> — *Principio dei Sistemi Contabili*

Prima di salire al Blocco 2 chiudiamo il Blocco 1 con due strumenti di controllo fine dei cicli.

> 💡 **Metafora:**
> - **`break`** = pulsante rosso di emergenza: il nastro si **ferma subito**.  
> - **`continue`** = braccio di scarto: salta **quel** pezzo difettoso e passa al successivo.  

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Usare `break` per uscire anticipatamente da un ciclo
- Usare `continue` per saltare il resto del corpo e passare all’iterazione successiva

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

### 🔬 Laboratorio PRIMM: Report con scarti e stop

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

[( )] 12345
[( )] 1345
[(X)] 13
[( )] 1234


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

/**
 * @brief Elabora 6 transazioni simulate: continue se <=0, break se >50000.
 * @return int 0 se ok.
 */
int main() {
    const double importi[] = {120.5, -3.0, 45.0, 12.75, 52000.0, 8.0};
    const int N = 6;

    double totale = 0.0;

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
        std::cout << "ID " << id << ": " << importo << "\n";
    }

    std::cout << "TOTALE: " << totale << "\n";

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
1. **Soglia micro-pagamenti**
   Con `continue`, scarta anche gli importi `< 5.00`.

2. **Soglia di allarme**
   Cambia l'allarme da `50000` a `1000` e verifica che `break` interrompa il report.

#### 5. MAKE (Crea)
**Scenario SIA — Controllo transazioni**

Scrivi `controllo_transazioni.cpp`:

- Ciclo su sei ID di transazione.
- `continue` per scartare un ID non valido.
- `break` quando incontri un ID di allarme.
- Stampa quali ID sono elaborati e il loro conteggio.

**Requisiti:** Doxygen se superi 15 righe, graffe e messaggi chiari.

<details>
<summary>💡 Scaffold</summary>

```cpp
/**
 * @brief Controlla transazioni con scarti e allarmi.
 */
#include <iostream>
int main() {
    // dati, ciclo, continue/break, conteggio
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- `break` = esci dal ciclo; `continue` = salta al giro successivo.
- In report contabili: scarti → `continue`; allarmi gravi → `break`.

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
