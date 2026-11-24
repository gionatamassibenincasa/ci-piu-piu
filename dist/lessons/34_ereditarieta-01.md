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
[← Prec.](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/33_composizione-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/35_virtual-01.md)

---



## 🌳 Specializzazioni in organigramma: ereditarietà essenziale

> "Entrata e uscita di cassa *sono* movimenti, con qualcosa in più."  
> — *Tassonomie contabili*

L’**ereditarietà** modellare il rapporto **“è un”**: la derivata riusa e specializza la base.  
In 3ª SIA restiamo a **due livelli**, una sola gerarchia semplice.

> 💡 **Metafora: organigramma**  
> `Movimento` generico; `Entrata` e `Uscita` specializzano il segno o l’etichetta.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare una classe derivata `public` da una base
- Riusare attributi/metodi comuni senza duplicarli

---

### 🔬 Laboratorio PRIMM: Movimenti

#### 1. PREDICT (Prevedi)

```cpp
class Base { public: void f(); };
class Der : public Base {};
```

Una classe derivata public eredita i membri public della base?

[(X)] Sì, può usare f() su un oggetto Der
[( )] Solo se virtual
[( )] Solo nei template
[( )] No, mai

<details>
<summary>💡 Spiegazione</summary>
Con ereditarietà <code>public</code>, l’interfaccia public della base è usabile sulla derivata.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file movimenti_base.cpp
 * @brief Ereditarietà a due livelli.
 */
#include <iostream>
#include <string>

class Movimento {
protected:
    std::string desc;
    double importo;
public:
    Movimento(const std::string& d, double i) : desc(d), importo(i) {}
    void scheda() const {
        std::cout << desc << " " << importo << '\n';
    }
};

class Entrata : public Movimento {
public:
    Entrata(const std::string& d, double i) : Movimento(d, i < 0 ? -i : i) {}
};

class Uscita : public Movimento {
public:
    Uscita(const std::string& d, double i) : Movimento(d, i > 0 ? -i : i) {}
};

int main() {
    Entrata e("Vendita", 50);
    Uscita u("Affitto", 20);
    e.scheda();
    u.scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Classe | “È un” Movimento? |
|--------|-------------------|
| `Entrata` | Sì |
| `Uscita` | Sì |
| `protected` in base | Visibile alle derivate, non a `main` |

#### 4. MODIFY (Modifica)
1. Aggiungi `getImporto() const` nella base.
2. In `Uscita`, stampa prefisso `"USCITA"` sovrascrivendo `scheda` (senza virtual ancora: chiama solo su tipo statico Uscita).
3. Crea un terzo movimento di prova.

#### 5. MAKE (Crea)
**Scenario SIA — Prima nota semplificata**

`movimenti_ereditati.cpp`: base + due derivate; `main` elenca alcune entrate/uscite.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Movimento { /* ... */ };
class Entrata : public Movimento { /* ... */ };
class Uscita : public Movimento { /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Ereditarietà = “è un”
- Una gerarchia poco profonda
- `protected` per le derivate
- Non usare ereditarietà al posto della composizione

---

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai definito gerarchie con l'ereditarietà.
Nel prossimo capitolo, `35_polimorfismo_virtual`, otterrai comportamenti diversi
a runtime nello stesso sportello con `virtual`.

---

# Navigazione

Continua da qui:

- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md">Indice delle lezioni</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/33_composizione-01.md">Lezione precedente (33 — L’azienda è fatta di pezzi: composizione (ha un))</a>
- <a href="https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/35_virtual-01.md">Lezione successiva (35 — Stesso sportello, comportamenti diversi: virtual)</a>
