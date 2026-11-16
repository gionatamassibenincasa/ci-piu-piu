<!--
author:    Gionata Massi
email:     gionata.massi@savoiabenicasa.it
version:   2026-11-16
language:  it
narrator:  IT Italian Male
comment:   Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:    https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:    https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/35_vector-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · Succ. →

---



## 🏗️ Mini-progetto: gestionale a oggetti in memoria

> "Chiudi il corso applicando reparti-oggetto a un caso aziendale completo (in RAM)."  
> — *Obiettivo di sintesi Blocco 3*

Questo capitolo è un **laboratorio di progetto**, non un nuovo costrutto isolato.  
Integra: `class`, costruttori, metodi, (opzionale) composizione o ereditarietà leggera, `std::vector`, output leggibile.

> 💡 **Metafora:** piccolo sistema informativo aziendale che vive mentre il programma è in esecuzione.

---

### 🎯 Obiettivo di questo chunk
Alla fine del progetto sei in grado di:
- Progettare almeno due classi coerenti con un dominio SIA
- Usare una collezione dinamica di oggetti e produrre un report

---

### 📋 Rubrica minima (Must)

| Requisito | Dettaglio |
|-----------|-----------|
| Classi | ≥ 2 classi con dati `private` e interfaccia `public` |
| Costruzione | Almeno un costruttore con parametri su ciascuna classe principale |
| Collezione | `std::vector` di oggetti (o di puntatori se usi polimorfismo) |
| Report | Output formattato (anche semplice) di elenco + totale/i |
| Documentazione | `@brief` sulle classi o sui metodi pubblici principali |

**Plus (Should):** composizione *oppure* ereditarietà a 2 livelli; metodo `const`; `operator<<`.

---

### 🔬 Traccia consigliata (PRIMM leggero)

#### 1. PREDICT (Prevedi)

Nel mini-progetto, perché dati private + metodi public sono un requisito?

```cpp
// rubrica progetto OOP
```

[(X)] Per proteggere gli invarianti e definire un’interfaccia chiara
[( )] Perché altrimenti non compila mai
[( )] Solo per usare vector
[( )] Solo per i template

#### 2. RUN — scheletro di partenza

```cpp
/**
 * @file gestionale_oop_stub.cpp
 * @brief Punto di partenza progetto.
 */
#include <iostream>
#include <string>
#include <vector>

// TODO: class Cliente / Articolo / Movimento ...

int main() {
    std::cout << "Gestionale OOP — in costruzione\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE
Definisci su carta: elenco classi, attributi private, metodi public, relazioni (ha-un / è-un).

#### 4. MODIFY
Implementa a incrementi: prima una classe, poi la seconda, poi il `vector`, poi i totali.

#### 5. MAKE (consegna Classroom50)
**Scenario a scelta (uno):**
- Magazzino articoli + giacenze e valore inventario  
- Prima nota: movimenti di cassa e saldo  
- Listino clienti + ordini (composizione)

File di consegna: `gestionale_oop.cpp` (e header se li separi).

<details>
<summary>💡 Scaffold minimo</summary>

```cpp
#include <iostream>
#include <string>
#include <vector>
class Articolo { /* ... */ };
int main() {
    std::vector<Articolo> magazzino;
    // ...
    return 0;
}
```
</details>

---

### 📝 Riepilogo tascabile
- Il progetto **unisce** i chunk 26–35
- Meglio poche classi chiare che tante vuote
- Invarianti e interfaccia public prima della “fantasia”
- Consegna = codice leggibile + report dimostrativo

---

### ➡️ Fine Blocco 3
Hai un percorso da `struct` a oggetti, template da utente e un gestionale in memoria.  
I prossimi passi “mondo reale” (file, GUI, DB) restano fuori da questo corso di base.
