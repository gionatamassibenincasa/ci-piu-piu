---
activity_id: "vector-01"
title: "Il magazzino elastico: usare std::vector (cliente del template)"
methodology: PRIMM
order: 36
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Dopo `v.push_back(3); v.push_back(5);`, quanto vale `v.size()`?"
    code: |
      std::vector<int> v;
      v.push_back(3);
      v.push_back(5);
    options:
      - text: "2"
        correct: true
      - text: "0"
        correct: false
      - text: "5"
        correct: false
      - text: "Indefinito"
        correct: false
files:
  - path: student_work/make/movimenti_vector.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <vector>
      int main() { return 0; }
    validation_rules:
      min_lines: 12
      must_contain:
      - "vector"
      - "push_back"
---


## 📦 Il magazzino elastico: usare `std::vector` (cliente del template)

> "Non prenotare 100 scaffali se oggi ne bastano 3: lo scaffale cresce con la merce."  
> — *Capacità operativa*

`std::vector<T>` è un array **dinamico** offerto dalla libreria: classe **template** già pronta.  
Qui sei **cliente**: la usi, non la riscrivi.

> 💡 **Metafora:** magazzino elastico — `push_back` aggiunge un pezzo, `size` dice quanti ce ne sono.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare `std::vector<T>`, usare `push_back`, `size`, indice e range-for
- Confrontare l’idea con l’array grezzo a dimensione fissa

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
Ogni <code>push_back</code> aggiunge un elemento: la size diventa 2.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file vector_importi.cpp
 * @brief vector di importi.
 */
#include <iostream>
#include <vector>

int main() {
    std::vector<double> importi;
    importi.push_back(10.0);
    importi.push_back(25.5);
    importi.push_back(7.0);

    double somma = 0.0;
    for (double x : importi) {
        somma += x;
    }
    std::cout << "N=" << importi.size() << " somma=" << somma << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Operazione | Significato |
|------------|-------------|
| `push_back` | Aggiunge in coda |
| `size()` | Quanti elementi |
| `v[i]` | Accesso (attenzione ai bounds) |
| range-for | Scorre tutti gli elementi |

#### 4. MODIFY (Modifica)
1. Stampa ogni importo su una riga.
2. Calcola il massimo con un ciclo.
3. Usa `std::vector<int>` per quantità pezzi.

#### 5. MAKE (Crea)
**Scenario SIA — Lista movimenti variabile**

`movimenti_vector.cpp`: `vector<double>` (o di `struct`/`class` se vuoi collegare il Blocco 3), caricamento di almeno 5 valori, somma e media.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <vector>
int main() {
    std::vector<double> v;
    // push_back ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- `vector` = sequenza dinamica
- `push_back` / `size` / range-for
- Preferibile all’array grezzo quando N non è fisso
- Sei utente di un template della std library

---

### ➡️ Prossimo chunk
Mettere insieme gli oggetti: **mini-progetto** gestionale.
