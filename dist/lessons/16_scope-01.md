<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-14
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/15_formattazione-contabile-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/17_array-01.md)

---


## 🎯 La Fotocopia vs L'Originale: Scope e Passaggio per Riferimento (`&`)

> "Il segreto del valore è chi lo possiede realmente."
>
> — *Metafora di gestione dei dati*

### Obiettivo
- Distinguere passaggio per valore da passaggio per riferimento.
- Comprendere lo scope delle variabili locali e globali.
- Utilizzare `const &` per efficienza.

---

## 📚 Teoria
1. Passaggio per valore copia il dato.
2. Passaggio per riferimento (`&`) passa un alias alla variabile originale.
3. `const &` permette lettura senza copia.
4. Scope locale vs globale.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


Cosa succede se una funzione prende un parametro per valore invece che per riferimento (`&`) quando dovrebbe modificare la variabile originale?

```cpp
void aumenta(int valore) { valore += 5; }
void aumentaRef(int& valore) { valore += 5; }
int x = 10;
aumenta(x);
// x è ?
```

[(X)] x rimane 10 (non modificato)
[( )] x diventa 15
[( )] Compila con errore
[( )] Il programma crasha


<details>
<summary>💡 Spiegazione</summary>
Il parametro per valore è una copia locale; le modifiche non si riflettono sulla variabile originale.
</details>

### Run
```cpp
/**
 * @file aggiorna_listino.cpp
 * @brief Funzioni per sconto e scambio prezzi.
 */
#include <iostream>

void applicaScontoPromozionale(double& prezzo, double percentuale) {
    // implementazione
}

void scambiaPrezzi(double& p1, double& p2) {
    // implementazione
}

int main() {
    double a = 100.0, b = 150.0;
    applicaScontoPromozionale(a, 10.0);
    scambiaPrezzi(a, b);
    std::cout << "a=" << a << " b=" << b << std::endl;
    return 0;
}
```
@LIA.cpp

### Investigate
Usa Python Tutor per visualizzare le due variabili e l'alias dopo la chiamata.

### Modify
Aggiungi una versione `void applicaScontoCostante(const double& prezzo, double percentuale, double& risultato)`.

### Make
**Scenario SIA — Aggiornamento Listino e Scambio**

Scrivi `aggiorna_listino.cpp` con le funzioni richieste, includendo Doxygen (`@brief`, `@param`, `@return`). Il programma deve dimostrare sconto e scambio.

---

