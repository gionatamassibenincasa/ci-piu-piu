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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/17_funzioni-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/19_array-01.md)

---


## 📄 Fotocopia o Originale: passaggio per valore e per riferimento

Nel laboratorio di un gestionale, una funzione può calcolare uno sconto senza
modificare il listino oppure aggiornare direttamente il prezzo registrato.
La differenza dipende da come il dato entra nella funzione.

Una funzione può ricevere:
- una **copia** del valore (**per valore**) → modifiche locali non tornano al chiamante  
- un **alias** della variabile originale (**per riferimento**, `&`) → le modifiche restano  

> 💡 **Metafora**  
> - Per valore = fotocopia del listino  
> - Per riferimento (`double& prezzo`) = il listino **originale** sul bancone

Lo **scope** completa il quadro: una variabile locale esiste solo nel
blocco/funzione dove è dichiarata.

**Confini della lezione:** qui osservi scope locale, passaggio per valore e
passaggio per riferimento. Puntatori, oggetti e strutture dati non fanno parte
di questo laboratorio.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- distinguere passaggio per valore e per riferimento;
- prevedere se una chiamata modifica la variabile nel chiamante;
- scrivere una funzione che aggiorna un `double` tramite `double&`;
- riconoscere quando una variabile locale non è più visibile fuori dal suo scope.

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
| `scontoCopia(p1, 10.0)` | `p1` resta `100.0`; la copia locale diventa `90.0` |
| `scontoRef(p2, 10.0)` | `p2` diventa `90.0`; il parametro è un alias |

In [Python Tutor](https://pythontutor.com/cpp.html) confronta i frame, i due
prezzi e l’alias `&` dopo ogni chiamata.

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
- [ ] Per valore significa lavorare su una copia; per riferimento significa usare l'originale.
- [ ] `T&` nel parametro permette di modificare il dato del chiamante.
- [ ] `const T&` permette di leggere senza modificare il dato ricevuto.
- [ ] Una variabile locale è visibile solo nel proprio blocco o nella propria funzione.

---

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai visto funzioni per valore e per riferimento.
Nel prossimo capitolo, `19_array_sequenze_dati`, userai le sequenze dello
stesso tipo: gli **array**.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/17_funzioni-01.md">Lezione precedente (17 — Il Primo Reparto: funzioni che restituiscono un valore)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/19_array-01.md">Lezione successiva (19 — La Batteria di Locker: gli array e le sequenze di dati)</a>
