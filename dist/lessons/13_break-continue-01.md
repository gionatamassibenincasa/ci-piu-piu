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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/12_do-while-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/14_funzioni-01.md)

---


## ⏹️ Uscite Anticipate: `break` e `continue` nei cicli

> "Non tutte le iterazioni vanno completate: a volte si salta, a volte si chiude il banco."  
> — *Controllo operativo dei processi*

Nei cicli a volte serve **interrompere tutto** (`break`) o **saltare solo il giro corrente** (`continue`).  
Sono il cruscotto fine del programmatore: da usare con chiarezza, non per nascondere logica confusa.

> 💡 **Metafora: nastro di controllo fatture**  
> - **`continue`** = “questa fattura è a zero: **saltala**, passa alla successiva”  
> - **`break`** = “importo anomalo: **ferma** l’intero controllo e segnala”

In questo chunk **non** trattiamo la formattazione monetari (`iomanip`): ha un capitolo dedicato.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Usare `break` e `continue` in un `for`/`while` con intento chiaro
- Prevedere l’output di un ciclo che li combina

---

### ⚙️ In breve

| Parola | Effetto |
|--------|---------|
| `continue` | Salta al **prossimo** giro del ciclo più interno |
| `break` | Esce **subito** dal ciclo più interno |

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;  // non stampare 2
    if (i == 4) break;     // stop prima di 4,5
    std::cout << i;
}
// stampa: 13
```

---

### 🔬 Laboratorio PRIMM: Controllo scarti

#### 1. PREDICT (Prevedi)

Cosa stampa il ciclo?

```cpp
for (int i = 1; i <= 5; ++i) {
    if (i == 2) continue;
    if (i == 4) break;
    std::cout << i;
}
```

[( )] 12345
[( )] 1345
[(X)] 13
[( )] 1234

<details>
<summary>💡 Spiegazione</summary>
<code>i==2</code> → <code>continue</code> (niente stampa). <code>i==3</code> stampa. <code>i==4</code> → <code>break</code> (il 5 non si raggiunge). Resta <code>13</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scarti_ciclo.cpp
 * @brief continue salta, break interrompe.
 */
#include <iostream>

int main() {
    for (int i = 1; i <= 5; ++i) {
        if (i == 2) {
            continue;
        }
        if (i == 4) {
            break;
        }
        std::cout << i;
    }
    std::cout << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| `i` | Azione | Output accumulato |
|-----|--------|-------------------|
| 1 | stampa | `1` |
| 2 | `continue` | `1` |
| 3 | stampa | `13` |
| 4 | `break` | fine |

#### 4. MODIFY (Modifica)
1. Inverti: `break` su 2 e `continue` su 4 — cosa cambia?
2. Sostituisci il `for` con un `while` equivalente.
3. Conta quanti numeri **effettivamente stampati** con un contatore.

#### 5. MAKE (Crea)
**Scenario SIA — Analisi movimenti di cassa**

Sequenza fissa di importi (array piccolo o elenco in variabili).  
- `continue` se importo `== 0`  
- `break` se importo `> 10000` (outlier)  
- Stampa quanti movimenti validi sono stati elaborati prima dello stop  

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
int main() {
    double mov[] = {100.0, 0.0, 250.0, 12000.0, 80.0};
    // for + continue + break
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- `continue` = salta **questo** giro
- `break` = esci dal ciclo
- Usali quando la regola di business è chiara (scarto / stop)
- Non sostituiscono una buona condizione di ciclo

---

### ➡️ Prossimo chunk
Dal ciclo al **reparto**: introduciamo le **funzioni** che restituiscono un valore.
