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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_funzioni-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/18_array-01.md)

---


## 📄 Fotocopia o Originale: passaggio per valore e per riferimento

> "Se ti passo la fotocopia, le tue note non restano sul documento ufficiale."  
> — *Metafora di gestione documentale*

Una funzione può ricevere:
- una **copia** del valore (**per valore**) → modifiche locali non tornano al chiamante  
- un **alias** della variabile originale (**per riferimento**, `&`) → le modifiche restano  

> 💡 **Metafora**  
> - Per valore = fotocopia del listino  
> - Per riferimento (`double& prezzo`) = il listino **originale** sul bancone

Lo **scope**: una variabile locale esiste solo nel blocco/funzione dove è dichiarata.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Distinguere passaggio per valore e per riferimento
- Scrivere una funzione che aggiorna un `double` del chiamante tramite `double&`

---

### ⚙️ Confronto

```cpp
void aumentaCopia(int v) { v += 5; }      // fotocopia
void aumentaRef(int& v) { v += 5; }     // originale

int x = 10;
aumentaCopia(x);  // x resta 10
aumentaRef(x);    // x diventa 15
```

---

### 🔬 Laboratorio PRIMM: Aggiornare un prezzo

#### 1. PREDICT (Prevedi)

```cpp
void aumenta(int valore) { valore += 5; }
int x = 10;
aumenta(x);
```

Dopo `aumenta(x)` con parametro per valore, quanto vale `x` se partiva da 10?

[( )] 15
[( )] Crash
[( )] Errore di compilazione
[(X)] 10 (non modificato)

<details>
<summary>💡 Spiegazione</summary>
<code>valore</code> è una copia locale. Incrementarla non tocca <code>x</code> in <code>main</code>.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file prezzo_riferimento.cpp
 * @brief Valore vs riferimento.
 */
#include <iostream>

void scontoCopia(double prezzo, double perc) {
    prezzo = prezzo * (1.0 - perc / 100.0);
}

void scontoRef(double& prezzo, double perc) {
    prezzo = prezzo * (1.0 - perc / 100.0);
}

int main() {
    double p1 = 100.0;
    double p2 = 100.0;
    scontoCopia(p1, 10.0);
    scontoRef(p2, 10.0);
    std::cout << "Dopo copia: " << p1 << '\n';
    std::cout << "Dopo ref:   " << p2 << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Chiamata | Effetto su variabile in `main` |
|----------|---------------------------------|
| `scontoCopia` | Nessuno |
| `scontoRef` | Prezzo aggiornato |

In [Python Tutor](https://pythontutor.com/cpp.html) confronta i frame e l’alias `&`.

#### 4. MODIFY (Modifica)
1. Aggiungi `void scambia(double& a, double& b)`.
2. Usa `const double&` in una funzione che **solo legge** il prezzo per stamparlo.
3. Dimostra in `main` sconto + scambio.

#### 5. MAKE (Crea)
**Scenario SIA — Aggiornamento listino**

`aggiorna_listino.cpp`:  
- `applicaSconto(double& prezzo, double perc)`  
- `scambiaPrezzi(double& a, double& b)`  
- `main` con due prezzi di esempio  

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
void applicaSconto(double& prezzo, double perc) { /* ... */ }
void scambiaPrezzi(double& a, double& b) { /* ... */ }
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Per valore = fotocopia; per riferimento = originale
- `T&` nel parametro per modificare il chiamante
- `const T&` per leggere senza copiare
- Scope locale: fuori dal blocco la variabile non esiste

---

### ➡️ Prossimo chunk
Sequenze di dati dello stesso tipo: gli **array**.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/16_funzioni-01.md">Lezione precedente (16 — Il Primo Reparto: funzioni che restituiscono un valore)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/18_array-01.md">Lezione successiva (18 — La Batteria di Locker: gli array e le sequenze di dati)</a>
