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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/32_ereditarieta-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/34_operatori-01.md)

---



## 🎭 Stesso sportello, comportamenti diversi: `virtual`

> "Chiami ‘stampa movimento’ allo sportello unico: dietro, procedure diverse."  
> — *Servizi uniformi, implementazioni specializzate*

Il **polimorfismo** via `virtual` permette di usare un puntatore/riferimento alla **base** e ottenere il comportamento della **derivata**.

> 💡 **Metafora:** un solo sportello “scheda”; ogni tipo di movimento risponde a modo suo.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare un metodo `virtual` e fare override nella derivata
- Usare un puntatore alla base per invocare il comportamento dinamico

*Nota:* esempio didattico con puntatori; la gestione avanzata della memoria non è il focus.

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

```cpp
Base* p = new Derivata();
p->scheda();
```

Con `scheda` virtuale e puntatore a Base che punta a Derivata, quale `scheda` viene chiamata?

[(X)] Quella della Derivata se scheda è virtual
[( )] Sempre e solo quella di Base
[( )] Nessuna
[( )] Solo se template

<details>
<summary>💡 Spiegazione</summary>
Con <code>virtual</code>, il tipo dinamico dell’oggetto decide quale versione eseguire.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file virtual_scheda.cpp
 * @brief Override virtuale di scheda().
 */
#include <iostream>
#include <string>

class Movimento {
protected:
    std::string desc;
public:
    Movimento(const std::string& d) : desc(d) {}
    virtual void scheda() const {
        std::cout << "MOV " << desc << '\n';
    }
};

class Entrata : public Movimento {
public:
    Entrata(const std::string& d) : Movimento(d) {}
    void scheda() const override {
        std::cout << "ENTRATA " << desc << '\n';
    }
};

int main() {
    Entrata e("Vendita bancone");
    Movimento* p = &e;
    p->scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Tipo statico di `p` | Tipo dinamico | `scheda` chiamata |
|---------------------|---------------|-------------------|
| `Movimento*` | `Entrata` | `Entrata::scheda` se virtual |

Togli `virtual` mentalmente: cosa cambierebbe?

#### 4. MODIFY (Modifica)
1. Aggiungi `Uscita` con override di `scheda`.
2. Chiama `scheda` su due puntatori diversi.
3. Aggiungi un campo importo e stampalo negli override.

#### 5. MAKE (Crea)
**Scenario SIA — Report eterogeneo**

`report_movimenti_virtual.cpp`: base con `virtual scheda`, almeno due derivate, dimostrazione via puntatori alla base.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Movimento { public: virtual void scheda() const; /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- `virtual` abilita il binding dinamico
- `override` rende esplicita l’intenzione
- Utile per collezioni eterogenee di “stesso ruolo”
- Restare su esempi piccoli in 3ª SIA

---

### ➡️ Prossimo chunk
Far parlare il dominio con operatori (`+` o `<<`).
