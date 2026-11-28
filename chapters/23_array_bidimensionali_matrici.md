---
activity_id: "matrici-01"
title: "Il Foglio Excel in Memoria: array bidimensionali"
methodology: PRIMM
order: 23
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "In `int m[2][3];`, quanti elementi ci sono e qual è l’ultimo indice di colonna?"
    code: |
      int m[2][3];
    options:
      - text: "6 elementi; colonne 0..2"
        correct: true
      - text: "5 elementi; colonne 1..3"
        correct: false
      - text: "6 elementi; colonne 1..3"
        correct: false
      - text: "2 elementi in tutto"
        correct: false
  make_instructions: "Tabella vendite 3 reparti × 4 trimestri"
files:
  - path: student_work/make/vendite_reparti.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      int main() {
          // TODO matrice 3x4
          return 0;
      }
    validation_rules:
      min_lines: 18
      must_contain: ["for"]
---

## 📊 Il Foglio Excel in Memoria: array bidimensionali

> "Una tabella è il modo più naturale di organizzare dati aziendali."  
> — *Pratica di reporting gestionale*

Un array monodimensionale è una **riga**.  
Spesso i report sono **griglie**: righe = reparti, colonne = mesi o trimestri.  
In C++ usiamo un **array bidimensionale** (matrice).

> 💡 **Metafora: foglio Excel**  
> - `vendite[r][c]` = cella all’incrocio **riga r**, **colonna c**  
> - Prima dimensione = righe (reparti)  
> - Seconda = colonne (periodi)  
> - Anche qui gli indici partono da **0**

**Confini della lezione:** qui lavori con matrici raw di dimensione fissa e con
due cicli `for` annidati. Non introduciamo ancora puntatori o strutture dati
dinamiche.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- dichiarare e inizializzare un array `tipo nome[RIGHE][COLONNE]`;
- distinguere indice di riga e indice di colonna;
- scorrere una matrice con due cicli `for` annidati;
- calcolare totali per riga, per colonna e complessivi.

---

### ⚙️ In breve

```cpp
// 2 reparti × 3 mesi
double vendite[2][3] = {
    {1000.0, 1200.0, 900.0},   // reparto 0
    {800.0,  950.0,  1100.0}   // reparto 1
};
```

Due cicli annidati: esterno sulle righe, interno sulle colonne.

> ⚠️ **Nota dal Mondo Reale:** le matrici raw servono qui per capire indici e
> cicli annidati. Nei programmi di produzione si preferiscono contenitori e
> strutture dati che gestiscono meglio dimensioni e controlli.

---

### 🔬 Laboratorio PRIMM: Due reparti, tre mesi

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
<code>int m[2][3]</code> ha 2×3 = 6 elementi. Le colonne sono indicizzate 0, 1, 2.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file matrice_vendite.cpp
 * @brief Totale per reparto su tre mesi.
 */
#include <iostream>

int main() {
    double vendite[2][3] = {
        {1000.0, 1200.0, 900.0},
        {800.0, 950.0, 1100.0}
    };

    for (int r = 0; r < 2; ++r) {
        double subtotale = 0.0;
        for (int c = 0; c < 3; ++c) {
            subtotale = subtotale + vendite[r][c];
        }
        std::cout << "Reparto " << r << " totale: " << subtotale << '\n';
    }
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Passo | Stato osservabile |
|-------|-------------------|
| Inizio riga | `r = 0`, `c = 0`, `subtotale = 0.0` |
| Ciclo interno | `c` visita le colonne della riga corrente |
| Fine riga | `subtotale` contiene il totale del reparto `r` |
| Nuova riga | `subtotale` si azzera e `r` aumenta |

Segui con [Python Tutor](https://pythontutor.com/cpp.html) l’ordine delle celle visitate.

#### 4. MODIFY (Modifica)
1. Aggiungi un terzo reparto (matrice `3×3`) e aggiorna i cicli.
2. Stampa anche il **totale generale** di tutta la matrice.
3. Stampa i totali **per colonna** (per mese).

#### 5. MAKE (Crea)
**Scenario SIA — Vendite per reparto e trimestre**

`vendite_reparti.cpp`: matrice **3 reparti × 4 trimestri**, totali per riga, per colonna e complessivo. Output leggibile.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    const int R = 3, C = 4;
    double v[R][C] = { /* ... */ };
    // cicli annidati
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- [ ] Una matrice organizza dati in righe e colonne.
- [ ] In `m[i][j]`, `i` indica prima la riga e `j` la colonna.
- [ ] Due `for` annidati visitano tutte le celle.
- [ ] I limiti vanno rispettati su entrambi gli assi.
- [ ] I totali parziali si inizializzano nel punto coerente con il risultato.

---

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai organizzato dati in righe e colonne.
Nel prossimo capitolo, `24_puntatori_e_memoria`, seguirai gli indirizzi in
memoria con i **puntatori**, in modo guidato e cauto.
