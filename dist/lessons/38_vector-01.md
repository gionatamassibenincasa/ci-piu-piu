<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-16
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/37_template-fun-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/39_progetto-oop-01.md)

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

```cpp
std::vector<int> v;
v.push_back(3);
v.push_back(5);
```

Dopo `v.push_back(3); v.push_back(5);`, quanto vale `v.size()`?

[( )] 0
[( )] 5
[( )] Indefinito
[(X)] 2

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

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai gestito collezioni con `std::vector`.
Nel prossimo capitolo, `39_progetto_oop_gestionale`, metterai insieme gli
oggetti in un mini-progetto gestionale.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/37_template-fun-01.md">Lezione precedente (37 — Stessa procedura, tipi diversi: funzioni template)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/39_progetto-oop-01.md">Lezione successiva (39 — Mini-progetto: gestionale a oggetti in memoria)</a>
