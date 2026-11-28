---
activity_id: "db-memoria-01"
title: "Il Archivio in RAM: array di struct"
methodology: PRIMM
order: 29
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Cosa rappresenta `Record tabella[100];` se Record è una struct?"
    code: |
      struct Record { int id; double importo; };
      Record tabella[100];
    options:
      - text: "Fino a 100 righe con gli stessi campi"
        correct: true
      - text: "Un solo record con 100 campi"
        correct: false
      - text: "Una matrice 100×100 di int"
        correct: false
      - text: "Un file su disco"
        correct: false
  make_instructions: "Mini-archivio movimenti: carica, elenca, totale"
files:
  - path: student_work/make/archivio_movimenti.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <string>
      int main() { return 0; }
    validation_rules:
      min_lines: 30
      must_contain: ["struct"]
---

## 🗄️ L’Archivio in RAM: array di struct

> "Una tabella è un insieme di righe con le stesse colonne."  
> — *Modello relazionale in miniatura*

Un database vero sta su disco e parla SQL.  
In memoria, puoi simulare una **tabella** con un **array di struct**: ogni elemento è una riga; ogni campo della struct è una colonna.

> 💡 **Metafora: foglio clienti / movimenti**  
> - `struct Movimento` = colonne (id, descrizione, importo)  
> - `Movimento tab[100]` = fino a 100 righe  
> - `n` = quante righe sono **realmente** usate

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Definire una struct-record e un array di record
- Scorrere le righe “vive” (`0..n-1`) per elenchi e totali

---

### 🔬 Laboratorio PRIMM: Tre movimenti di cassa

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
Array di struct = molte righe, stesso schema di colonne. Non è un file: vive finché il programma è in esecuzione.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file movimenti_cassa.cpp
 * @brief Mini-archivio movimenti in RAM.
 */
#include <iostream>
#include <string>

struct Movimento {
    int id;
    std::string desc;
    double importo;
};

int main() {
    Movimento tab[10];
    int n = 0;

    tab[n++] = {1, "Vendita bancone", 25.0};
    tab[n++] = {2, "Reso cliente", -5.0};
    tab[n++] = {3, "Vendita online", 40.0};

    double saldo = 0.0;
    for (int i = 0; i < n; ++i) {
        std::cout << tab[i].id << " | " << tab[i].desc
                  << " | " << tab[i].importo << '\n';
        saldo = saldo + tab[i].importo;
    }
    std::cout << "Saldo movimenti: " << saldo << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Simbolo | Significato |
|---------|-------------|
| `tab[i]` | Riga i-esima |
| `tab[i].importo` | Campo della riga |
| `n` | Numero di righe valide (non confonderlo con la capacità 10) |

#### 4. MODIFY (Modifica)
1. Aggiungi un quarto movimento e verifica `n` e il saldo.
2. Funzione `double totale(const Movimento tab[], int n)`.
3. Stampa solo i movimenti con `importo < 0` (uscite).

#### 5. MAKE (Crea)
**Scenario SIA — Archivio movimenti contabili**

`archivio_movimenti.cpp`: struct, array, almeno 5 movimenti di esempio, elenco completo, totale, conteggio positivi/negativi. Doxygen se il file cresce.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
struct Movimento { /* ... */ };
double totale(const Movimento tab[], int n) { return 0.0; }
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Tabella in RAM ≈ array di struct
- Capacità ≠ numero di righe usate (`n`)
- Si scorre con `for` su `0..n-1`
- È il ponte concettuale verso i database veri

---

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai integrato dati e algoritmi in un database in memoria.
Nel prossimo capitolo, `30_ricorsione_e_strutture_ricorsive`, affronti i
problemi definiti in termini di una versione più piccola di se stessi:
**ricorsione**.
