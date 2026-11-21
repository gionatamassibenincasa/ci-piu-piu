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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/34_operatori-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/36_vector-01.md)

---



## 🔧 Stessa procedura, tipi diversi: funzioni template

> "Il confronto ‘chi è maggiore’ vale per pezzi e per prezzi."  
> — *Riuso algoritmico*

Una **funzione template** descrive un algoritmo **generico**: il compilatore genera le versioni per i tipi usati.

> 💡 **Metafora:** modulo aziendale standard compilato per reparti diversi (stessa procedura, dati diversi).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere una funzione `template <typename T>` semplice
- Usarla con tipi diversi (`int`, `double`)

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
massimo(3, 5);
massimo(2.5, 2.7);
```

Una funzione `template <typename T> T massimo(T a, T b)` può essere usata su `int` e su `double`?

[(X)] Sì, il compilatore istanzia le versioni necessarie
[( )] No, solo su int
[( )] Solo se T è class
[( )] No, serve virtual

<details>
<summary>💡 Spiegazione</summary>
Il compilatore crea istanze distinte di <code>massimo</code> per i tipi dedotti dagli argomenti.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file massimo_template.cpp
 * @brief Funzione template massimo.
 */
#include <iostream>

template <typename T>
T massimo(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << massimo(3, 5) << '\n';
    std::cout << massimo(2.5, 2.7) << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Chiamata | T dedotto |
|----------|-----------|
| `massimo(3, 5)` | `int` |
| `massimo(2.5, 2.7)` | `double` |

I tipi devono supportare `>`.

#### 4. MODIFY (Modifica)
1. Scrivi `template <typename T> void scambia(T& a, T& b)`.
2. Usa `scambia` su due `double`.
3. Prova `massimo` su due `char`.

#### 5. MAKE (Crea)
**Scenario SIA — Utility generiche**

`util_template.cpp`: `massimo` e `scambia` template; demo su quantità (`int`) e prezzi (`double`).

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
template <typename T>
T massimo(T a, T b) { /* ... */ }
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Template = algoritmo generico
- Istanziazione a compile-time
- T deve offrire le operazioni usate
- Non è magia runtime: è generazione di codice

---

### ➡️ Prossimo chunk
Usare un contenitore template della libreria: `std::vector`.
