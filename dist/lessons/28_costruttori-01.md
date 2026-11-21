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
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/27_class-incapsulamento-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/29_metodi-01.md)

---


## 📋 Assunzione in organico: costruttori e oggetto ben formato

> "Non esiste un dipendente senza matricola: non dovrebbe esistere un articolo senza codice e prezzo coerente."  
> — *Anagrafica e qualità del dato*

Con soli setter, si può dimenticare di inizializzare.  
Il **costruttore** è il contratto di **creazione**: quando l'oggetto nasce, è già in uno stato sensato.

> 💡 **Metafora: assunzione**  
> All'ingresso in azienda compili i dati obbligatori.  
> Il costruttore fa lo stesso per l'oggetto: niente "mezze pratiche".

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Dichiarare e usare un costruttore con parametri
- Far nascere un oggetto già coerente con gli invarianti di base

---

### ⚙️ In breve

```cpp
class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) {
        codice = c;
        setPrezzo(p);
    }
    void setPrezzo(double p);
    double getPrezzo() const;
};
```

Creazione: `Articolo a("A-100", 12.5);`

---

### 🔬 Laboratorio PRIMM: Articolo costruito bene

#### 1. PREDICT (Prevedi)

```cpp
class Articolo {
public:
    Articolo(const std::string& c, double p);
};
Articolo a("A-1", 10.0);
```

Dopo la costruzione di un Articolo con codice e prezzo tramite costruttore, i campi sono già impostati?


[(X)] Sì: il costruttore inizializza lo stato
[( )] No: serve sempre setCodice dopo
[( )] Solo se c'è anche il distruttore
[( )] No: i private restano indefiniti

<details>
<summary>💡 Spiegazione</summary>
Il costruttore viene eseguito alla creazione: codice e prezzo partono già impostati.
</details>

#### 2. RUN (Esegui)

```cpp
/**
 * @file articolo_ctor.cpp
 * @brief Costruttore che impone uno stato iniziale.
 */
#include <iostream>
#include <string>

class Articolo {
private:
    std::string codice;
    double prezzo;
public:
    Articolo(const std::string& c, double p) {
        codice = c;
        if (p < 0.0) prezzo = 0.0;
        else prezzo = p;
    }
    double getPrezzo() const { return prezzo; }
    std::string getCodice() const { return codice; }
};

int main() {
    Articolo a("A-100", 12.5);
    Articolo b("B-200", -4.0);
    std::cout << a.getCodice() << " " << a.getPrezzo() << '\n';
    std::cout << b.getCodice() << " " << b.getPrezzo() << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

| Momento | Cosa succede |
|---------|----------------|
| `Articolo a(...)` | Alloca l'oggetto e chiama il costruttore |
| Corpo del ctor | Inizializza i campi private |
| Dopo | `main` usa solo metodi pubblici |

#### 4. MODIFY (Modifica)
1. Aggiungi `giacenza` al costruttore (default 0).
2. Costruttore a tre parametri: codice, prezzo, giacenza.
3. Metodo `scheda()` e usalo in `main` su due articoli.

#### 5. MAKE (Crea)
**Scenario SIA — Conto corrente ben formato**

`conto_costruttore.cpp`: classe `ContoCorrente` con IBAN, intestatario, saldo; costruttore che non lascia saldo iniziale negativo (o lo porta a 0); stampa riepilogo.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>
#include <string>
class ContoCorrente {
private:
    std::string iban;
    double saldo;
public:
    ContoCorrente(const std::string& i, double s);
};
int main() { return 0; }
```
</details>

---

### 📝 Riepilogo tascabile
- Costruttore = nascita controllata dell'oggetto
- Meglio invarianti rispettati **subito**
- Si può riusare la logica dei setter nel ctor
- Nome uguale alla classe, niente tipo di ritorno

---

### ➡️ Prossimo chunk
Cosa sa **fare** l'oggetto: metodi e responsabilità di reparto.
