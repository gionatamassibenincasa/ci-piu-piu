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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_formattazione-contabile-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_scope-01.md)

---


## 🏢 Il Primo Reparto: funzioni che restituiscono un valore

> "Un buon processo si scompone in reparti con responsabilità chiare."  
> — *Organizzazione aziendale e top-down*

Finora quasi tutto viveva in `main`.  
Quando la logica cresce (IVA, sconti, commissioni), conviene **estrarre un reparto**: una **funzione** con nome, parametri e **valore di ritorno**.

> 💡 **Metafora: sportello specializzato**  
> - `calcolaIva(imponibile)` = sportello “ufficio IVA”  
> - Gli dai l’imponibile (documento in ingresso)  
> - Ti restituisce l’importo IVA (documento in uscita)  
> - `main` coordina: chiede, riceve, stampa

In questo chunk: funzioni **semplici** che calcolano e `return`.  
Passaggio per riferimento e scope fine: capitolo successivo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare e chiamare una funzione con parametri e `return`
- Usare il risultato in `main` senza ripetere la formula

---

### ⚙️ Anatomia minima

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

// uso:
double iva = calcolaIva(100.0);
```

| Parte | Ruolo |
|-------|--------|
| Tipo di ritorno | Cosa esce dallo sportello (`double`, `int`, …) |
| Nome | Verbo + oggetto (`calcolaIva`) |
| Parametri | Dati in ingresso |
| `return` | Fine del lavoro + valore |

---

### 🔬 Laboratorio PRIMM: Ufficio IVA

#### 1. PREDICT (Prevedi)

```cpp
double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}
```

Quanto vale `calcolaIva(100.0)` con aliquota 0.22?

[(X)] 22
[( )] 100
[( )] 122
[( )] 0.22

<details>
<summary>💡 Spiegazione</summary>
100 × 0.22 = 22. La funzione restituisce solo l’IVA, non il totale documento.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ufficio_iva.cpp
 * @brief Funzione che calcola l'IVA al 22%.
 */
#include <iostream>

double calcolaIva(double imponibile) {
    return imponibile * 0.22;
}

int main() {
    double imponibile = 100.0;
    double iva = calcolaIva(imponibile);
    double totale = imponibile + iva;

    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA:        " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Momento | Cosa succede |
|---------|----------------|
| Chiamata | `main` sospende; parte `calcolaIva` |
| `return` | Il valore torna a `main` in `iva` |
| Dopo | `main` usa `iva` nel totale |

> 🔗 [Python Tutor C++](https://pythontutor.com/cpp.html): osserva lo stack frame della funzione.

#### 4. MODIFY (Modifica)
1. Cambia l’imponibile a `250.0` e verifica i tre importi.
2. Aggiungi `double calcolaTotale(double imponibile)` che usa `calcolaIva` al suo interno.
3. Documenta le funzioni con `@brief` e `@param` / `@return`.

#### 5. MAKE (Crea)
**Scenario SIA — Commissione POS**

`commissione_pos.cpp`:  
- `double commissione(double importo)` → 1.2% dell’importo (o soglia minima fissa a tua scelta, documentata)  
- `main` stampa importo, commissione e netto negoziante  

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
double commissione(double importo) {
    return importo * 0.012;
}
int main() {
    // ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Funzione = reparto con ingresso, lavoro, uscita
- `return` consegna il risultato a chi ha chiamato
- `main` orchestra; le funzioni specializzano
- Un calcolo riusato → una funzione, non copia-incolla

---

### ➡️ Prossimo chunk
Come far sì che una funzione **modifichi** le variabili del chiamante: passaggio per **riferimento**.
