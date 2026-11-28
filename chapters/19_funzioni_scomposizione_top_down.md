---
activity_id: "funzioni-01"
title: "Il Primo Reparto: funzioni che restituiscono un valore"
methodology: PRIMM
order: 19
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Quanto vale `calcolaIva(100.0)` con aliquota 0.22?"
    code: |
      double calcolaIva(double imponibile) {
          return imponibile * 0.22;
      }
    options:
      - text: "22"
        correct: true
      - text: "100"
        correct: false
      - text: "122"
        correct: false
      - text: "0.22"
        correct: false
  make_instructions: "Commissione POS con funzione dedicata"
files:
  - path: student_work/make/commissione_pos.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      double commissione(double importo) {
          return 0.0; // TODO
      }
      int main() { return 0; }
    validation_rules:
      min_lines: 15
      must_contain: ["return"]
---

## 🏢 Il Primo Reparto: funzioni che restituiscono un valore

Nel laboratorio di un gestionale, una schermata può calcolare IVA, sconti e
commissioni. Se tutta la logica resta in `main`, il programma diventa difficile
da leggere e da riusare.

Per questo estraiamo un reparto specializzato: una **funzione** con un nome,
parametri e un **valore di ritorno**. `main` coordina il lavoro, mentre ogni
funzione svolge un calcolo circoscritto.

> 💡 **Metafora: sportello specializzato**  
> - `calcolaIva(imponibile)` = sportello “ufficio IVA”  
> - Gli dai l’imponibile (documento in ingresso)  
> - Ti restituisce l’importo IVA (documento in uscita)  
> - `main` coordina: chiede, riceve, stampa

**Confini della lezione:** qui usi funzioni semplici che calcolano e restituiscono
un valore. Passaggio per riferimento e scope saranno affrontati nel capitolo
successivo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- dichiarare una funzione con parametri e tipo di ritorno;
- chiamarla da `main` e assegnare il risultato a una variabile;
- descrivere il percorso del dato dalla chiamata al `return`.

---

### ⚙️ Anatomia minima

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

// uso:
double iva = calcolaIva(100.0);
```

| Parte | Domanda guida | Esempio |
|-------|---------------|---------|
| Tipo di ritorno | Che tipo di dato esce? | `double` |
| Nome | Quale lavoro svolge? | `calcolaIva` |
| Parametri | Quali dati entrano? | `double imponibile` |
| `return` | Quale risultato torna al chiamante? | `imponibile * 0.22` |

---

### 🔬 Laboratorio PRIMM: Ufficio IVA

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
100 × 0.22 = 22. La funzione restituisce solo l’IVA, non il totale documento.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ufficio_iva.cpp
 * @brief Funzione che calcola l'IVA al 22%.
 */
#include <iostream>

double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

int main() {
    double imponibile = 100.0;
    double iva = calcolaIva(imponibile);
    double totale = imponibile + iva;

    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA:        " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Momento | Stato osservabile |
|---------|------------------|
| Prima della chiamata | `imponibile = 100.0`; `iva` non ha ancora il risultato |
| Chiamata | `main` sospende; `imponibile` entra nella funzione |
| `return` | `100.0 * 0.22` produce `22.0`, che torna in `iva` |
| Dopo la chiamata | `main` usa `iva` per calcolare `totale = 122.0` |

> 🔗 [Python Tutor C++](https://pythontutor.com/cpp.html): osserva lo stack frame della funzione.

#### 4. MODIFY (Modifica)
1. Cambia l’imponibile a `250.0` e verifica i tre importi.
2. Aggiungi `double calcolaTotale(double imponibile)` che usa `calcolaIva` al suo interno.
3. Documenta le funzioni con `@brief` e `@param` / `@return`.

#### 5. MAKE (Crea)
**Scenario SIA — Commissione POS**

`commissione_pos.cpp`:  
- `double commissione(double importo)` → 1.2% dell’importo (o soglia minima fissa a tua scelta, documentata)  
- `main` stampa importo, commissione e netto negoziante  

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
double commissione(double importo) {
    return 0.0; // TODO: calcola la commissione
}
int main() {
    // TODO: leggi un importo e stampa commissione e netto
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- [ ] Una funzione riceve dati, svolge un lavoro circoscritto e restituisce un risultato.
- [ ] Il tipo di ritorno descrive il dato prodotto dalla funzione.
- [ ] `return` consegna il risultato a chi ha chiamato.
- [ ] `main` orchestra; le funzioni specializzano.
- [ ] Un calcolo riusato diventa una funzione, non una copia-incolla.

---

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai assegnato ai dati ruoli precisi e riconosciuto
schemi ricorrenti nei cicli. Nel prossimo capitolo,
`20_documentazione_doxygen_funzioni`, renderai leggibili le funzioni per i
lettori e per il tuo editor.
le variabili del chiamante tramite il passaggio per riferimento.
