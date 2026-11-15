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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/18_matrici-01.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/20_enum-01.md)

---


## 🎯 Il Biglietto di Ritiro: Indirizzi di Memoria, Operatori & e * e Puntatori

> "Un puntatore è un biglietto che indica dove si trova la merce."
>
> — *Metafora di memoria*

### Obiettivo
- Comprendere gli operatori `&` (indirizzo) e `*` (dereferenza).
- Usare `nullptr` e verificare la validità del puntatore.
- Visualizzare lo stack con Python Tutor per capire la relazione tra puntatore e variabile.

---

## 📚 Teoria
1. `int* p;` dichiara un puntatore a `int`.
2. `p = &var;` assegna l’indirizzo di `var`.
3. `*p` accede al valore puntato.
4. `nullptr` indica nessun puntatore valido.
5. Puntatori a array e passaggio a funzioni.

---

## 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)


Dati `int a = 10; int* p = &a; *p = 20;`, quanto vale `a`?

```cpp
int a = 10;
int* p = &a;
*p = 20; // modifica a
```

[(X)] 20
[( )] 10
[( )] Compila con errore
[( )] Il programma crasha


<details><summary>💡 Spiegazione</summary>Il dereferenziamento `*p = 20` modifica direttamente la variabile `a`.
</details>

### Run
```cpp
/**
 * @file gestione_fido.cpp
 * @brief Gestione di un fido bancario tramite puntatore.
 */
#include <iostream>

void aggiornaFido(double* fido, double importo) {
    if (fido && importo > 0) {
        *fido += importo;
    }
}

int main() {
    double fido = 5000.0;
    aggiornaFido(&fido, 1200.0);
    std::cout << "Fido aggiornato: " << fido << std::endl;
    return 0;
}
```
@LIA.cpp

### Investigate
Usa Python Tutor per visualizzare il collegamento tra `a` e `p`.

### Modify
Aggiungi una funzione `void resetFido(double* fido)` che imposta a zero, controllando `nullptr`.

### Make
**Scenario SIA — Gestione Fido Bancario tramite Puntatore**

Scrivi `gestione_fido.cpp` con Doxygen (`@brief`, `@param`, `@return`). Il programma deve incrementare il fido e stampare il risultato.

---

