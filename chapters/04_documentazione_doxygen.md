## 📝 Capitolo 4: Parlare al Futuro Te Stesso (Documentazione Doxygen)

> "Il codice viene letto molto più spesso di quanto venga scritto."
> — *Principio di manutenibilità*

Hai già scritto `Ciao, Mondo!` e presto scriverai programmi più lunghi.  
Chi li leggerà tra tre mesi? Tu. Un compagno. Il docente.  

Per questo in azienda (e in questo corso) non basta che il programma *funzioni*: deve anche essere **comprensibile**.  
Usiamo uno standard leggero e diffusissimo: **Doxygen**.

> 💡 **Metafora:**  
> Il codice è il prodotto finito.  
> I commenti Doxygen sono l’**etichetta e il manuale d’uso** attaccati al prodotto: dicono *cosa fa*, *per chi*, *con quali dati*, senza costringere a smontare tutto.

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Scrivere un’intestazione di file e di `main` in stile Doxygen
- Usare il commento `///` per spiegare il **perché** (non il cosa ovvio)
- Applicare la **regola di proporzionalità** del corso

---

### 📋 I tag essenziali (solo quelli che usiamo)

| Tag | A cosa serve | Esempio |
|-----|--------------|---------|
| `@file` | Nome del file | `@file scheda_prodotto.cpp` |
| `@brief` | Una riga: cosa fa il programma / la funzione | `@brief Calcola il totale ivato.` |
| `@param` | Descrive un parametro (quando avremo le funzioni) | `@param prezzo Importo netto in euro` |
| `@return` | Cosa restituisce la funzione | `@return int 0 se successo` |

Commento di riga leggero:

```cpp
/// Aliquota IVA ordinaria vigente (non modificare a caso)
const double ALIQUOTA_IVA = 0.22;
```

---

### 🔬 Esempio minimo completo

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
    /// Identificativo dello studente per lo scontrino di presentazione
    std::cout << "Nome: Alex\n";
    std::cout << "Classe: 3A SIA\n";
    return 0;
}
```

---

### ⚖️ Regola di proporzionalità (obbligatoria nel corso)

| Situazione | Cosa scrivere |
|------------|----------------|
| Programma o funzione **> ~15 righe** | Intestazione Doxygen completa (`@file` / `@brief` / `@param` / `@return` dove servono) |
| Snippet o esercizio **breve** | Solo `///` sul **perché** economico o logico |
| Vietato | Commenti tautologici (`/// incrementa i di 1`) |

Esempio **buono**:
```cpp
/// 0.22 = aliquota IVA ordinaria vigente per beni e servizi
const double ALIQUOTA_IVA = 0.22;
```

Esempio **da evitare**:
```cpp
/// dichiara la costante aliquota
const double ALIQUOTA_IVA = 0.22;
```

---

### 🧪 Mini-esercizio (MAKE leggero)

Prendi il programma `presentazione.cpp` del capitolo precedente (o riscrivilo) e:
1. Aggiungi l’intestazione `@file` + `@brief` in testa al file
2. Aggiungi `@brief` e `@return` su `main`
3. Metti un `///` utile su almeno una riga di output

Non serve generare HTML con lo strumento Doxygen: per ora ci interessa **scrivere** i commenti nel modo giusto. Più avanti, quando i progetti cresceranno, potremo anche generarne la documentazione automatica.

---

### 📝 Riepilogo tascabile
- Doxygen = etichette standard per file e funzioni.
- Tag minimi: `@file`, `@brief`, `@param`, `@return`.
- `///` spiega il **perché**, non il cosa ovvio.
- Proporzionalità: completo sopra ~15 righe, leggero sotto.
- Da questo capitolo in poi i Make “ufficiali” richiederanno questi standard.

---

### ➡️ Prossimo chunk
Con l’officina pronta, il motore visto, il primo dialogo scritto e le etichette chiare, apriamo gli **sportelli della memoria**: variabili, tipi e costanti.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Chunk breve e monotematico (solo documentazione)
  [x] Allineato a SKILLS.md (proporzionalità)
  [x] Nessun costrutto nuovo di linguaggio
  [x] Ponte esplicito verso variabili
-->
