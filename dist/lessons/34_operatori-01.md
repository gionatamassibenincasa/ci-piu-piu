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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/33_virtual-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/35_template-fun-01.md)

---



## 💬 Linguaggio del dominio: overloading essenziale (`<<`)

> "Meglio `std::cout << articolo` che quattro getter in fila."  
> — *API leggibile*

L’**overloading** degli operatori adatta la sintassi al dominio.  
In questo chunk un solo focus: **`operator<<`** per l’output.

> 💡 **Metafora:** il modulo di stampa dello scontrino sa come disporre i campi dell’articolo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare `operator<<` per una classe semplice
- Stampare un oggetto con `std::cout << obj`

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
std::cout << articolo;
```

A cosa serve tipicamente sovraccaricare `operator<<` per una classe?

[(X)] Stampare l’oggetto in modo leggibile su uno stream
[( )] Aprire un file in automatico
[( )] Creare template
[( )] Sostituire il costruttore

<details>
<summary>💡 Spiegazione</summary>
<code>operator&lt;&lt;</code> definisce come inserire l’oggetto in uno <code>ostream</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_ostream.cpp
 * @brief operator<< per Articolo.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) : codice(c), prezzo(p) {}
    friend std::ostream& operator<<(std::ostream& os, const Articolo& a) {
        os << a.codice << " €" << a.prezzo;
        return os;
    }
};

int main() {
    Articolo a("A-100", 12.5);
    std::cout << a << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Elemento | Ruolo |
|----------|--------|
| `friend` | Accesso ai private per la stampa |
| `return os` | Consente `cout << a << b` |
| `const Articolo&` | Non modifica l’oggetto |

#### 4. MODIFY (Modifica)
1. Formatta il prezzo con due decimali (`iomanip`).
2. Aggiungi la giacenza in stampa.
3. Stampa due articoli in sequenza.

#### 5. MAKE (Crea)
**Scenario SIA — Scheda stampabile**

`stampa_articolo_op.cpp`: classe con `operator<<`; `main` dimostra almeno due stampe.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo { /* friend operator<< */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Un operatore per chunk: qui solo `<<`
- Restituisci lo stream
- Preferisci `const&` sul parametro oggetto
- Leggibilità del dominio > acrobazie

---

### ➡️ Prossimo chunk
Procedure uguali su tipi diversi: **funzioni template**.
