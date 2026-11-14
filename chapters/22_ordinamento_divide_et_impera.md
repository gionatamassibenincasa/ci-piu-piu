---
activity_id: merge-sort-01
title: 'Ordinamento divide et impera: merge sort'
methodology: PRIMM
order: 22
version: '2026-11-15'
language: it
components:
  predict_quiz:
    question: Nel merge sort, cosa fa la fase "merge"?
    code: // due metà già ordinate → una sequenza ordinata
    options:
    - text: Divide l'array a metà
      correct: false
    - text: Fonde due sottosequenze ordinate
      correct: true
    - text: Scambia solo due elementi
      correct: false
---



## 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Spiegare la differenza tra Merge Sort e Quick Sort e quando usarli.
- Implementare entrambi gli algoritmi in C++.
- Analizzare la complessità temporale e spaziale dei due algoritmi.

---

### 💡 La Metafora Guida
> **Metafora:** *Il reparto amministrativo che deve organizzare migliaia di pratiche* – per **Merge Sort** dividiamo le pratiche in pile più piccole, le ordiniamo singolarmente e poi le fondiamo; per **Quick Sort** scegliamo una pratica “pivot” e separiamo le pratiche minori e maggiori attorno a essa, ripetendo ricorsivamente.

---

### ⚙️ Concetto in breve
| Algoritmo | Principio | Complessità Media | Uso consigliato |
|----------|-----------|-------------------|-----------------|
| Merge Sort | Divide‑et‑impera, fusione di sotto‑array ordinati | `O(n log n)` tempo, `O(n)` spazio | Dati molto grandi, stabilità richiesta |
| Quick Sort | Sceglie un pivot e partiziona in‑place | `O(n log n)` medio, `O(n²)` peggiore | Quando lo spazio è critico e i dati sono casuali |

---

### ⚠️ Tranelli tipici
- **Merge Sort:** dimenticare di copiare gli elementi temporaneamente può corrompere l’array.
- **Quick Sort:** scegliere un pivot pessimo (es. il primo elemento in un array già ordinato) porta a degradazione quadratica.

---

### 🔬 Laboratorio PRIMM: *Ordinamento aziendale*

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]
> Quale dei seguenti casi peggiori può far degenerare Quick Sort a `O(n²)`?
- [( )] L'array è già ordinato ascendente
- [(X)] L'array è già ordinato discendente
- [( )] L'array è casuale

<details><summary>💡 Spiegazione</summary>
Il pivot scelto come primo elemento su un array ordinato (ascendente o discendente) crea partizioni squilibrate, provocando la degenerazione.
</details>

#### 2. RUN (Esegui)
Esegui il codice e osserva i passaggi di fusione.
```cpp
#include <iostream>
#include <vector>

void merge(std::vector<int>& a, int l, int m, int r) {
    std::vector<int> tmp(r - l + 1);
    int i = l, j = m + 1, k = 0;
    while (i <= m && j <= r) {
        if (a[i] <= a[j]) tmp[k++] = a[i++];
        else tmp[k++] = a[j++];
    }
    while (i <= m) tmp[k++] = a[i++];
    while (j <= r) tmp[k++] = a[j++];
    for (int p = 0; p < (r - l + 1); ++p) a[l + p] = tmp[p];
}

void mergeSort(std::vector<int>& a, int l, int r) {
    if (l >= r) return;
    int m = (l + r) / 2;
    mergeSort(a, l, m);
    mergeSort(a, m + 1, r);
    merge(a, l, m, r);
}

int main(){
    std::vector<int> v = {5,2,9,1,5,6};
    mergeSort(v,0,v.size()-1);
    for(int x: v) std::cout << x << ' ';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
| Riga / Costrutto | Cosa fa | A cosa serve |
|------------------|---------|--------------|
| `merge` | combina due sotto‑array ordinati in uno temporaneo | Unisce le parti ordinate preservando l’ordine |
| `mergeSort` | ricorsivamente divide l’array | Divide il problema in sottoproblemi più piccoli |

🔗 [Python Tutor C++](https://pythontutor.com/cpp.html)

#### 4. MODIFY (Modifica)
1. Cambia il pivot di Quick Sort scegliendo l’elemento centrale.
2. Aggiungi una variante di `merge` che utilizza un buffer statico per ridurre le allocazioni.
3. Implementa una versione iterativa di Merge Sort.

#### 5. MAKE (Crea)
**Scenario aziendale:** Un reparto risorse umane deve ordinare migliaia di record dipendente per stipendio.
**Requisiti:**
- Utilizzare Merge Sort per garantire stabilità.
- Documentare con Doxygen.
- Il programma deve stampare il top‑10 stipendi più alti.

---

### 📝 Riepilogo tascabile
- Merge Sort: divide, ordina, fonde (stabilità, `O(n log n)`).
- Quick Sort: partiziona in‑place, pivot critico (`O(n log n)` medio).
- Evita pivot pessimo e gestisci buffer temporaneo.

---

➡️ Prossimo chunk: *Ricorsione e strutture ricorsive* (Cap. 24)