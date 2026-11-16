---
activity_id: "progetto-oop-01"
title: "Mini-progetto: gestionale a oggetti in memoria"
methodology: lab
order: 36
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Nel mini-progetto, perché dati private + metodi public sono un requisito?"
    code: |
      // rubrica progetto OOP
    options:
      - text: "Per proteggere gli invarianti e definire un’interfaccia chiara"
        correct: true
      - text: "Perché altrimenti non compila mai"
        correct: false
      - text: "Solo per usare vector"
        correct: false
      - text: "Solo per i template"
        correct: false
files:
  - path: student_work/make/gestionale_oop.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <string>
      #include <vector>
      int main() { return 0; }
    validation_rules:
      min_lines: 12
      must_contain:
      - "class"
      - "vector"
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

[[ predict_block() ]]

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
