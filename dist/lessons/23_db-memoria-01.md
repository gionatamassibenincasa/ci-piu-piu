<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-15
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/22_merge-sort-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/24_ricorsione-01.md)

---




## 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Comprendere come rappresentare dati aziendali con array di struct in C++.
- Implementare funzioni di caricamento, visualizzazione, ordinamento e ricerca su un vettore di strutture.
- Realizzare un progetto mini‑ERP con menu interattivo.

---

### 💡 La Metafora Guida
> **Metafora:** *Il reparto amministrativo che gestisce migliaia di pratiche* – le pratiche sono i record dei prodotti, organizzati in un archivio (array di struct) e manipolati tramite funzioni modulari.

---

### ⚙️ Concetto in breve
| Aspetto | Dettaglio |
|---------|-----------|
| Dati | `struct Prodotto { int codice; std::string nome; double prezzo; int giacenza; }` |
| Operazioni | Caricamento, stampa tabellare, ordinamento per campo, ricerca binaria, aggiornamento giacenza |
| Complessità | Ordinamento `O(n log n)`, ricerca `O(log n)` su array ordinato |

---

### ⚠️ Tranelli tipici
- **Doxygen:** dimenticare di documentare le funzioni porta a mancanza di generazione automatica.
- **Input:** non validare l’interazione `switch` può causare loop infiniti o crash.

---

### 🔬 Laboratorio PRIMM: *Mini‑ERP di Magazzino*

#### 1. PREDICT (Prevedi)

Perché un array di struct può modellare una tabella in memoria?

```cpp
struct Record { /* campi */ };
Record tabella[100];
```

[(X)] Perché ogni elemento è una riga con gli stessi campi
[( )] Perché gli array non hanno indici
[( )] Perché le struct non possono contenere stringhe
> Quale struttura dati è più adatta per mantenere ordinato un archivio di prodotti grande?
- [(X)] `std::vector` con `std::sort`
- [( )] `std::list`
- [( )] `std::queue`

<details><summary>💡 Spiegazione</summary>
`std::vector` permette accesso diretto e uso di `std::sort`, ideale per ordinamento rapido.
</details>

#### 2. RUN (Esegui)
Esegui il codice base del progetto (caricamento, stampa, menu).
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

struct Prodotto {
    int codice;
    std::string nome;
    double prezzo;
    int giacenza;
};

// Funzioni prototype (da implementare) ...
int main(){
    std::vector<Prodotto> catalogo = {
        {101, "Penna", 1.20, 100},
        {102, "Quaderno", 2.50, 80},
        {103, "Zaino", 45.00, 20}
    };
    // TODO: menu interattivo
    for(const auto& p: catalogo)
        std::cout << p.codice << " " << p.nome << " " << p.prezzo << " " << p.giacenza << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
| Riga / Costrutto | Cosa fa | A cosa serve |
|------------------|---------|--------------|
| `struct Prodotto` | definisce il record prodotto | raggruppa dati eterogenei |
| `std::vector<Prodotto>` | contenitore dinamico | gestisce quantità variabile di record |
| `std::sort` | ordina il vettore | permette ricerca binaria efficiente |

🔗 [Python Tutor C++](https://pythontutor.com/cpp.html)

#### 4. MODIFY (Modifica)
1. Aggiungi validazione dell’input per il menu.
2. Implementa la ricerca binaria per codice prodotto.
3. Inserisci la funzione di calcolo del valore patrimoniale totale.

#### 5. MAKE (Crea)
**Scenario aziendale:** Un negozio deve gestire l’inventario di 20 articoli, consentendo stampa, ordinamento, ricerca e aggiornamento giacenza.
**Requisiti:**
- Documentazione Doxygen per ogni funzione.
- Nessuna variabile globale.
- Menu `switch` con loop principale.
- Funzione `makeReport` che stampa il valore totale del magazzino.

---

### 📝 Riepilogo tascabile
- Array di struct → modello di database in memoria.
- Operazioni chiave: caricamento, visualizzazione, ordinamento, ricerca, aggiornamento.
- Progetto mini‑ERP con menu interattivo e Doxygen.

---

➡️ Prossimo chunk: *Ricorsione e strutture ricorsive* (Cap. 24)
