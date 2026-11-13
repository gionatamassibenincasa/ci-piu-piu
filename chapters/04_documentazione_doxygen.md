## 📝 Parlare al Futuro Te Stesso: documentazione Doxygen

> "Il codice non mente mai, i commenti sì."
>
> — *Ron Jeffries*

Hai già scritto `Ciao, Mondo!` e presto i programmi si allungheranno.  
Chi li leggerà tra tre mesi? Tu. Un compagno. Il docente. In azienda, un collega che non eri tu.

Non basta che il programma *funzioni*: deve essere **comprensibile**.  
In questo corso usiamo uno standard leggero e molto diffuso: **Doxygen**.

> 💡 **Metafora:**  
> Il codice è il prodotto.  
> I commenti Doxygen sono **etichetta e manuale d’uso**: dicono *cosa fa*, *per chi*, *con quali dati*, senza smontare tutto il meccanismo.

Questo non è un laboratorio PRIMM “classico”: è una **convenzione di lavoro** che userai da qui in poi nei Make e nei progetti.

---

### 🎯 Obiettivo
Alla fine di questa lezione sei in grado di:
- Scrivere un’intestazione di **file** e di **`main`** in stile Doxygen
- Usare `///` per spiegare il **perché** (non il cosa ovvio)
- Applicare la **regola di proporzionalità** del corso

---

### 📋 I tag che usiamo (e basta)

| Tag | A cosa serve | Esempio |
|-----|--------------|---------|
| `@file` | Nome del file | `@file presentazione.cpp` |
| `@brief` | Una riga: cosa fa il programma o la funzione | `@brief Stampa nome e classe.` |
| `@param` | Descrive un parametro (quando avremo le funzioni) | `@param prezzo Importo netto in euro` |
| `@return` | Cosa restituisce la funzione | `@return int 0 se successo` |

Commento di riga (tre slash):

```cpp
/// Aliquota IVA ordinaria vigente (non modificare a caso)
const double ALIQUOTA_IVA = 0.22;
```

`@param` lo terrai a mente: tornerà utile con le **funzioni**. Per ora ti servono soprattutto `@file`, `@brief` e `@return`.

---

### ✅ Esempio minimo completo

```cpp
/**
 * @file presentazione.cpp
 * @brief Stampa nome, classe e hobby dello studente.
 */
#include <iostream>

/**
 * @brief Punto di ingresso del programma.
 * @return int 0 se l'esecuzione termina correttamente.
 */
int main() {
    /// Identificativo per lo "scontrino" di presentazione in lab
    std::cout << "Nome: Alex\n";
    std::cout << "Classe: 3A SIA\n";
    std::cout << "Hobby: fotografia\n";
    return 0;
}
```

Nota: **non** generiamo ancora HTML con lo strumento Doxygen.  
L’obiettivo è **scrivere** i commenti nel modo giusto; l’eventuale generazione automatica arriverà quando i progetti saranno più grandi.

---

### ⚖️ Regola di proporzionalità (obbligatoria)

| Situazione | Cosa scrivere |
|------------|----------------|
| Programma o funzione **più lungo di ~15 righe** | Intestazione Doxygen (`@file` / `@brief` / `@param` / `@return` dove servono) |
| Snippet o esercizio **breve** | Solo `///` sul **perché** economico o logico, se serve |
| **Vietato** | Commenti tautologici (`/// incrementa i di 1`, `/// dichiara la variabile`) |

**Buono** (spiega una scelta di business o un vincolo):
```cpp
/// 0.22 = aliquota IVA ordinaria vigente per beni e servizi
const double ALIQUOTA_IVA = 0.22;
```

**Da evitare** (ripete solo la sintassi):
```cpp
/// dichiara la costante aliquota
const double ALIQUOTA_IVA = 0.22;
```

---

### 🧪 Mini-esercizio

Prendi il programma di presentazione del capitolo precedente (o riscrivilo) e:

1. Aggiungi in testa al file `@file` e `@brief`
2. Aggiungi su `main` `@brief` e `@return`
3. Metti **un** `///` utile (un perché, non un ovvio) su almeno una riga

Compila ed esegui: i commenti non cambiano l’output, ma cambiano quanto il codice è leggibile da un umano.

---

### 📝 Riepilogo tascabile
- Doxygen = etichette standard per file e funzioni.
- Tag minimi ora: `@file`, `@brief`, `@return` (più `@param` più avanti).
- `///` = perché / vincolo / regola di business, non il cosa ovvio.
- Proporzionalità: completo sopra ~15 righe, leggero sotto.
- Da qui in poi i Make “ufficiali” si aspettano questi standard.

---

### ➡️ Prossimo passo
Con officina, motore, primo dialogo e etichette chiare, apriamo gli **sportelli della memoria**: variabili, tipi e costanti.

---

<!--#
  NOTE AUTORE / LLM
  - Capitolo di convenzione, NON forzare le 5 fasi PRIMM complete
  - Nessun @LIA.cpp obbligatorio (non c'è un lab eseguibile centrale)
  - Titolo senza "Capitolo N"
  - Coerente con SKILLS.md (proporzionalità Doxygen)
#-->
