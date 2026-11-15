---
activity_id: formattazione-contabile-01
title: "La Stampante Fiscale: formattare importi con <iomanip>"
methodology: PRIMM
order: 15
components:
  predict_quiz:
    question: "Come viene stampato 19.5 con fixed e setprecision(2)?"
    code: |
      std::cout << std::fixed << std::setprecision(2) << 19.5;
    options:
      - text: "19.50"
        correct: true
      - text: "19.5"
        correct: false
      - text: "20"
        correct: false
files:
  - path: README.md
    action: create
    template_content: |
      # Formattazione contabile
      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
  - path: student_work/make/prospetto_importi.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <iomanip>
      int main() {
          /// TODO: spiega perché gli importi hanno sempre due decimali.
          return 0;
      }
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

[[ predict_block() ]]

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
