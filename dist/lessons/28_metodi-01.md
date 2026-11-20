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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/27_costruttori-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/29_const-metodi-01.md)

---



## 🛠️ Cosa sa fare il reparto: metodi e responsabilità

> "Il reparto non espone i cassetti: espone le *operazioni* consentite."  
> — *Servizi applicativi*

I **metodi** sono le mansioni dell’oggetto: caricare, scaricare, stampare la scheda.  
`main` coordina; l’oggetto applica le regole sul proprio stato.

> 💡 **Metafora: mansioni**  
> `carica(n)` e `scarica(n)` sono procedure interne al magazzino articolo, non calcoli sparsi in `main`.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Aggiungere metodi di istanza che modificano o leggono lo stato privato
- Assegnare responsabilità chiare all’oggetto (non al `main`)

---

### 🔬 Laboratorio PRIMM: Carico e scarico

#### 1. PREDICT (Prevedi)

Chi può chiamare un metodo public di Articolo?

```cpp
Articolo a("A", 1.0);
a.scheda();
```

[( )] Solo codice dentro la class
[(X)] Chiunque abbia un oggetto Articolo (es. main)
[( )] Solo il costruttore
[( )] Nessuno

<details>
<summary>💡 Spiegazione</summary>
I metodi public sono l’interfaccia usabile da <code>main</code> e da altre funzioni.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_metodi.cpp
 * @brief Metodi di business su Articolo.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    int giacenza;
public:
    Articolo(const std::string& c, int g) : codice(c), giacenza(g < 0 ? 0 : g) {}
    void carica(int n) {
        if (n > 0) giacenza += n;
    }
    bool scarica(int n) {
        if (n <= 0 || n > giacenza) return false;
        giacenza -= n;
        return true;
    }
    void scheda() const {
        std::cout << codice << " giacenza=" << giacenza << '\n';
    }
};

int main() {
    Articolo a("A-100", 10);
    a.carica(5);
    a.scarica(3);
    a.scheda();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Metodo | Responsabilità |
|--------|----------------|
| `carica` | Aumenta giacenza se n>0 |
| `scarica` | Diminuisce solo se c’è disponibilità |
| `scheda` | Presenta lo stato (sola lettura) |

#### 4. MODIFY (Modifica)
1. Fai restituire a `scarica` un messaggio stampato in `main` in base al `bool`.
2. Aggiungi `int getGiacenza() const`.
3. Impedisci `carica` oltre una soglia massima (es. 1000).

#### 5. MAKE (Crea)
**Scenario SIA — Articolo di magazzino operativo**

`magazzino_articolo.cpp`: costruttore, `carica`, `scarica`, `scheda`; in `main` una piccola storia di movimenti.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo { /* ... */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Metodi = operazioni sullo stato dell’oggetto
- Regole di business vicino ai dati
- `main` orchestra, non micromanage i campi
- Nomi verbo+oggetto (`scarica`, `carica`)

---

### ➡️ Prossimo chunk
Metodi che **non** modificano lo stato: `const`.
