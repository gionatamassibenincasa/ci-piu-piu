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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/31_const-metodi-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/33_ereditarieta-01.md)

---



## 🧩 L’azienda è fatta di pezzi: composizione (“ha un”)

> "Un ordine *ha un* cliente e *ha* delle righe: non *è un* cliente."  
> — *Modellazione del dominio*

La **composizione** collega oggetti per contenimento: la parte è un membro della classe.  
È spesso più naturale dell’ereditarietà forzata.

> 💡 **Metafora:** la pratica d’ordine nel faldone *include* la scheda cliente (copia di lavoro) e le righe.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare una classe che **ha** un’altra classe come membro
- Costruire l’oggetto composto inizializzando le parti

---

### 🔬 Laboratorio PRIMM: Ordine con cliente

#### 1. PREDICT (Prevedi)

```cpp
class Ordine { Cliente cliente_; /* ... */ };
```

Se `Ordine` contiene un membro `Cliente cliente_`, la distruzione di `Ordine` coinvolge anche `cliente_`?

[(X)] Sì: il membro vive dentro l’oggetto composto
[( )] No: Cliente è sempre indipendente sullo heap
[( )] Solo con virtual
[( )] Solo con template

<details>
<summary>💡 Spiegazione</summary>
I membri oggetto hanno vita legata al contenitore: compositum e parte “value member”.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file ordine_composizione.cpp
 * @brief Ordine ha un Cliente.
 */
#include <iostream>
#include <string>

class Cliente {
private:
    std::string nome;
public:
    Cliente(const std::string& n) : nome(n) {}
    std::string getNome() const { return nome; }
};

class Ordine {
private:
    int id;
    Cliente cliente;
    double totale;
public:
    Ordine(int i, const Cliente& c, double t)
        : id(i), cliente(c), totale(t < 0 ? 0 : t) {}
    void scheda() const {
        std::cout << "Ordine " << id << " — "
                  << cliente.getNome() << " — € " << totale << '\n';
    }
};

int main() {
    Cliente cl("Rossi SRL");
    Ordine o(1001, cl, 250.0);
    o.scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Classe | Ruolo |
|--------|--------|
| `Cliente` | Parte riusabile |
| `Ordine` | Composto: ha id, cliente, totale |
| Costruttore di `Ordine` | Inizializza anche il membro `cliente` |

#### 4. MODIFY (Modifica)
1. Aggiungi `getTotale() const` su `Ordine`.
2. Aggiungi un campo `std::string note` all’ordine.
3. Crea due ordini per lo stesso cliente (due oggetti `Ordine`).

#### 5. MAKE (Crea)
**Scenario SIA — Ordine di vendita**

`ordine_cliente.cpp`: `Cliente` + `Ordine` in composizione; scheda leggibile; `main` dimostrativo.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Cliente { /* ... */ };
class Ordine { /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Composizione = “ha un”, non “è un”
- Membri oggetto costruiti col contenitore
- Preferisci composizione quando non c’è vera specializzazione
- Basi solide prima dell’ereditarietà

---

### ➡️ Prossimo chunk
Quando invece **è un** tipo specializzato: ereditarietà essenziale.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/31_const-metodi-01.md">Lezione precedente (31 — Consultare senza modificare: metodi const)</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/33_ereditarieta-01.md">Lezione successiva (33 — Specializzazioni in organigramma: ereditarietà essenziale)</a>
