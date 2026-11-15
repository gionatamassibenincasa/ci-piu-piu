<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-12
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/13_break-continue-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_formattazione-contabile-01.md)

---


## 🏢 Il Primo Reparto: una funzione che restituisce un valore

> 💡 **Metafora:** una funzione è un reparto: riceve un ordine, svolge un lavoro
> preciso e restituisce il risultato senza mostrare tutti i passaggi interni.

### 🎯 Obiettivo
Scrivere e chiamare una funzione che riceve un valore e ne restituisce uno.

---

### ⚙️ Prima del laboratorio: ingresso e uscita

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

`imponibile` è il dato che entra nel reparto; `return` consegna il valore
calcolato a chi ha chiamato la funzione.

---

### 🧭 Prima del laboratorio: chiamare il reparto

```cpp
double iva = calcolaIva(100.0);
```

Il valore `100.0` entra nella funzione; `22.0` torna e viene salvato in `iva`.

---

### 🔬 Laboratorio PRIMM: IVA di una fattura

#### 1. PREDICT

Quale valore restituisce calcolaIva(100.0)?

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

[(X)] 22
[( )] 100
[( )] 122

#### 2. RUN

```cpp
#include <iostream>

double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

int main() {
    double iva = calcolaIva(100.0);
    std::cout << "IVA: " << iva << "\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE

| Passo | Valore |
|---|---|
| Chiamata | `imponibile = 100.0` |
| `return` | `22.0` |
| In `main` | `iva = 22.0` |

> 🔗 Osserva i due frame su [Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY

<details><summary>💡 Scaffold</summary>

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

</details>

1. Calcola l'IVA di `250.0`.
2. Sostituisci `0.22` con `0.10` e osserva il risultato.
3. Rinomina `imponibile` in `importoNetto` in firma e corpo.

#### 5. MAKE

**Scenario SIA:** scrivi `commissione_pos.cpp` con una funzione
`calcolaCommissione(double importo)` che restituisce l'1% dell'importo e stampa
il risultato in `main`.

### 📝 Riepilogo tascabile
- Una funzione riceve dati, svolge un lavoro e può restituire un valore.
- `return` termina la funzione e consegna il risultato.
- La chiamata usa il valore restituito in un'espressione.

### ➡️ Prossimo chunk
Nel prossimo chunk separeremo programmi più grandi in più reparti.
