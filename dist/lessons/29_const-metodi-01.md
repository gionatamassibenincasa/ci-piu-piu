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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/28_metodi-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/30_composizione-01.md)

---



## 👁️ Consultare senza modificare: metodi `const`

> "In audit puoi leggere la pratica, non alterarla."  
> — *Controllo interno*

Alcune operazioni sono di **sola lettura**: scheda, getter, report.  
In C++ si marca il metodo con **`const`**: promette di non modificare lo stato dell’oggetto.

> 💡 **Metafora: badge visitatore**  
> Entri in consultazione: vedi i documenti, non li firmi.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare metodi `const` per letture
- Usare oggetti `const` e capire perché servono getter `const`

---

### 🔬 Laboratorio PRIMM

#### 1. PREDICT (Prevedi)

Un metodo `void scheda() const` può assegnare `giacenza = 0` nel corpo?

```cpp
void scheda() const { giacenza = 0; }
```

[( )] Sì
[(X)] No: metodo const non modifica lo stato
[( )] Solo se giacenza è public
[( )] Solo in main

<details>
<summary>💡 Spiegazione</summary>
Il <code>const</code> dopo i parametri vieta di modificare i membri non mutable dell’oggetto.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file scheda_const.cpp
 * @brief Metodi const per sola lettura.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) : codice(c), prezzo(p < 0 ? 0 : p) {}
    double getPrezzo() const { return prezzo; }
    void scheda() const {
        std::cout << codice << " € " << prezzo << '\n';
    }
};

void stampa(const Articolo& a) {
    a.scheda();  // ok: scheda è const
}

int main() {
    const Articolo a("A-100", 9.5);
    stampa(a);
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Situazione | Consentito? |
|------------|-------------|
| `getPrezzo() const` su oggetto `const` | Sì |
| Metodo non-const su oggetto `const` | No |
| `const Articolo&` in lettura | Preferibile (niente copia, niente modifica) |

#### 4. MODIFY (Modifica)
1. Aggiungi `getCodice() const`.
2. Prova un metodo non-const su `const Articolo` e osserva l’errore del compilatore.
3. Formatta il prezzo con `iomanip` dentro `scheda() const`.

#### 5. MAKE (Crea)
**Scenario SIA — Scheda articolo in sola lettura**

`scheda_const.cpp`: classe con almeno due metodi `const`; funzione libera `stampa(const Articolo&)`.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo { /* getters const, scheda const */ };
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- `const` sul metodo = sola lettura
- Getter e report devono essere `const`
- Oggetti `const` e riferimenti `const&` collaborano
- Errori di const-correttezza li segnala il compilatore

---

### ➡️ Prossimo chunk
Oggetti fatti di altri oggetti: **composizione**.
