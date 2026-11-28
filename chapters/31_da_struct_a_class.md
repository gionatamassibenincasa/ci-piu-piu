---
activity_id: "class-incapsulamento-01"
title: "Dal cartellino al reparto: struct → class e incapsulamento"
methodology: PRIMM
order: 31
version: "2026-11-16"
language: it
components:
  predict_quiz:
    question: "Se `prezzo` è `private` in una `class`, da `main` posso scrivere `a.prezzo = -5`?"
    code: |
      class Articolo {
      private:
          double prezzo;
      public:
          void setPrezzo(double p);
      };
      Articolo a;
      a.prezzo = -5;
    options:
      - text: "Sì, sempre"
        correct: false
      - text: "No: accesso vietato fuori dalla classe"
        correct: true
      - text: "Solo se il file si chiama main.cpp"
        correct: false
      - text: "Sì, ma solo con double"
        correct: false
files:
  - path: student_work/make/articolo_classe.cpp
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <string>
      // TODO: class Articolo con dati private e interfaccia public
      int main() {
          return 0;
      }
    validation_rules:
      min_lines: 12
      must_contain:
      - "class"
      - "private"
      - "public"
---


## 🏢 Dal cartellino al reparto: `struct` → `class` e incapsulamento

> "Non tutti possono modificare il listino: solo chi ha la responsabilità del reparto."  
> — *Governance dei dati aziendali*

Nel Blocco 2 l’`Articolo` era una **`struct`**: tutti i campi pubblici, come un cartellino lasciato sul bancone.  
Funziona, ma chiunque può scrivere `prezzo = -10` e rompere le regole di business.

Una **`class`** permette l’**incapsulamento**: stato **privato**, sportelli **pubblici** (metodi) che rispettano gli invarianti.

> 💡 **Metafora: reparto a porta chiusa**  
> - Dati `private` = archivio interno del reparto  
> - Metodi `public` = sportello unico (chiedi, non frugare nei cassetti)  
> - Invariante = “prezzo e giacenza non negativi”

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare una `class` con membri `private` e interfaccia `public`
- Spiegare perché l’incapsulamento protegge le regole aziendali sui dati

---

### ⚙️ In breve

```cpp
class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    void setPrezzo(double p);
    double getPrezzo() const;
};
```

Fuori dalla classe: solo i metodi pubblici. Niente `a.prezzo = …`.

---

### 🔬 Laboratorio PRIMM: Articolo protetto

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

<details>
<summary>💡 Spiegazione</summary>
I membri private non sono accessibili da <code>main</code>. Serve un metodo pubblico che validi il valore.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_class.cpp
 * @brief Incapsulamento minimo su un articolo di magazzino.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    void setCodice(const std::string& c) { codice = c; }
    void setPrezzo(double p) {
        if (p < 0.0) {
            prezzo = 0.0;
        } else {
            prezzo = p;
        }
    }
    std::string getCodice() const { return codice; }
    double getPrezzo() const { return prezzo; }
};

int main() {
    Articolo a;
    a.setCodice("A-100");
    a.setPrezzo(12.5);
    a.setPrezzo(-3.0);  // corretta a 0
    std::cout << a.getCodice() << " → " << a.getPrezzo() << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Elemento | Ruolo |
|----------|--------|
| `private` | Stato interno |
| `setPrezzo` | Unico punto che può cambiare il prezzo (con regola) |
| `getPrezzo` | Lettura controllata |

Prova a decommentare mentalmente `a.prezzo = 1`: non compila.

#### 4. MODIFY (Modifica)
1. Aggiungi `giacenza` privata con `setGiacenza` / `getGiacenza` (mai negativa).
2. Metodo `void scheda()` che stampa codice, prezzo, giacenza.
3. Se `giacenza == 0`, stampa anche `"ESAURITO"`.

#### 5. MAKE (Crea)
**Scenario SIA — Articolo di magazzino a interfaccia chiusa**

`articolo_classe.cpp`: classe `Articolo` completa (codice, prezzo, giacenza), setter con validazione, `scheda()`, dimostrazione in `main`.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class Articolo {
private:
    // ...
public:
    // setter / getter / scheda
};
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- `class` = dati privati + sportelli pubblici
- Incapsulamento = proteggere gli invarianti
- Fuori si usano i metodi, non i campi
- Stesso dominio del `struct`, responsabilità diverse

---

### ➡️ Prossimo passo nel percorso
Nel capitolo precedente hai visto il passaggio da `struct` a `class`.
Nel prossimo capitolo, `32_const_correttezza_oggetti`, costruirai oggetti
**già validi** con i costruttori.
