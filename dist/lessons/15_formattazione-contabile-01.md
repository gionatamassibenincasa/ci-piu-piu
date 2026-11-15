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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_funzioni-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_scope-01.md)

---

## 🖨️ La Stampante Fiscale: formattare importi con `<iomanip>`

> 💡 **Metafora:** una stampante fiscale rende ogni importo leggibile: centesimi
> sempre uguali e colonne allineate.

### 🎯 Obiettivo
Formattare importi monetari con `std::fixed`, `std::setprecision` e `std::setw`.

### ⚙️ Prima del laboratorio: due decimali

```cpp
std::cout << std::fixed << std::setprecision(2);
```

`fixed` usa notazione decimale; `setprecision(2)` mostra due cifre dopo la virgola.

### 🧭 Prima del laboratorio: colonne

`std::setw(10)` riserva la larghezza minima del prossimo campo.

### 🔬 Laboratorio PRIMM: mini prospetto

#### 1. PREDICT

Come viene stampato 19.5 con fixed e setprecision(2)?

```cpp
std::cout << std::fixed << std::setprecision(2) << 19.5;
```

[(X)] 19.50
[( )] 19.5
[( )] 20

#### 2. RUN

```cpp
#include <iostream>
#include <iomanip>
int main() {
    std::cout << std::fixed << std::setprecision(2);
    std::cout << std::setw(10) << 19.5 << "\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE

| Istruzione | Effetto |
|---|---|
| `fixed` | notazione decimale |
| `setprecision(2)` | due centesimi |
| `setw(10)` | colonna larga 10 |

#### 4. MODIFY
1. Stampa `1200.0` nella stessa colonna.
2. Cambia la larghezza in `15`.

#### 5. MAKE
Scrivi `prospetto_importi.cpp` che stampa tre importi con due decimali e colonne allineate.

### 📝 Riepilogo tascabile
- `fixed` + `setprecision(2)` formatta i soldi.
- `setw` allinea il campo successivo.
