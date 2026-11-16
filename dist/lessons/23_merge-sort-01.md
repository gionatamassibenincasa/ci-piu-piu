<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-16
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/22_selection-sort-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/24_db-memoria-01.md)

---


## 🧩 Dividere per Ordinare: idea del merge sort

> "Ordina i reparti separatamente, poi unisci i due elenchi già ordinati."  
> — *Divide et impera in magazzino*

Selection sort è chiaro ma, su tanti dati, fa molti confronti.  
Il **merge sort** applica *divide et impera*: spezza, ordina le parti, **fonde** (merge) due sequenze già ordinate.

In questo chunk ci concentriamo sull’idea e sulla **fase di merge** (il cuore comprensibile e utile anche da solo). Un’implementazione ricorsiva completa può seguire dopo aver visto la ricorsione.

> 💡 **Metafora: due pile di fatture già ordinate per data**  
> Unisci in un’unica pila ordinata confrontando sempre le due “teste”.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Spiegare l’idea divide-et-impera del merge sort
- Implementare la **fusione** di due array monodimensionali già ordinati

---

### 🔬 Laboratorio PRIMM: Unire due listini ordinati

#### 1. PREDICT (Prevedi)

Qual è il ruolo principale della fase di merge?

```cpp
// due metà già ordinate → una sequenza ordinata
```

[(X)] Fondere due sottosequenze già ordinate
[( )] Mescolare a caso gli elementi
[( )] Eliminare i duplicati obbligatoriamente
[( )] Ordinare solo con scambi adiacenti

<details>
<summary>💡 Spiegazione</summary>
Il merge non “riordina da zero”: sfrutta l’ordine già presente nelle due metà.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file merge_due_listini.cpp
 * @brief Fusione di due array ordinati in un terzo.
 */
#include <iostream>

int main() {
    int a[4] = {10, 30, 50, 70};
    int b[3] = {20, 40, 60};
    int c[7];
    int i = 0, j = 0, k = 0;

    while (i < 4 && j < 3) {
        if (a[i] <= b[j]) {
            c[k] = a[i];
            ++i;
        } else {
            c[k] = b[j];
            ++j;
        }
        ++k;
    }
    while (i < 4) { c[k] = a[i]; ++i; ++k; }
    while (j < 3) { c[k] = b[j]; ++j; ++k; }

    for (int t = 0; t < 7; ++t) {
        std::cout << c[t] << ' ';
    }
    std::cout << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Indice | Ruolo |
|--------|--------|
| `i` | Avanzamento su `a` |
| `j` | Avanzamento su `b` |
| `k` | Scrittura su `c` |

Traccia i primi tre passi a mano: quale testa (`a[i]` o `b[j]`) viene scelta?

#### 4. MODIFY (Modifica)
1. Cambia i valori (restando ordinati) e verifica `c`.
2. Estrai `void merge(const int a[], int na, const int b[], int nb, int c[])`.
3. Gestisci il caso in cui un array è vuoto (`na == 0`).

#### 5. MAKE (Crea)
**Scenario SIA — Unione di due listini codici**

`merge_listini.cpp`: due array di codici già ordinati, risultato fuso in un terzo array, stampa. Funzione `merge` dedicata.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void merge(const int a[], int na, const int b[], int nb, int c[]) {
    // ...
}
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Merge sort = dividi, ordina, **fondi**
- Merge di due sequenze ordinate: confronta le teste
- Serve spazio per l’array risultato
- Qui abbiamo padroneggiato il merge; la ricorsione completa è il passo successivo naturale

---

### ➡️ Prossimo chunk
Mettiamo insieme `struct` e array: un piccolo **database in memoria**.
