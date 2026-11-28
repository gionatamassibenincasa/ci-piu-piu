---
activity_id: doxygen-01
title: "Parlare al futuro te stesso: documentazione Doxygen"
methodology: convention
order: 8
version: "2026-11-28"
language: it
components: {}
files: []
---

## 📝 Parlare al futuro te stesso: documentazione Doxygen

> "Il codice non mente mai, i commenti sì."
>
> — Ron Jeffries

Un programma può funzionare e restare comunque difficile da leggere. Tra tre
mesi lo riaprirai tu; più avanti lo leggeranno un compagno, il docente o un
collega. Per questo adottiamo una convenzione leggera: **Doxygen**.

> 💡 **Metafora:** Il codice è il prodotto; i commenti Doxygen sono l'etichetta
> e il manuale d'uso. Spiegano lo scopo del prodotto senza costringere chi
> legge a smontare tutto il meccanismo.

In questo capitolo documentiamo file e programma principale. **Non usiamo
ancora `@param` e `@return`**: le funzioni con parametri e valori restituiti
arriveranno più avanti.

### 🎯 Obiettivi

Alla fine sai:

- scrivere un'intestazione Doxygen per un file;
- usare `@brief`, `@author` e `@date` con misura;
- usare `///` per spiegare un vincolo economico o logico;
- scegliere una documentazione proporzionata alla dimensione del codice.

### 📋 I tag di questa fase

| Tag | Uso | Esempio |
|---|---|---|
| `@file` | Nome del file | `@file presentazione.cpp` |
| `@brief` | Scopo in una riga | `@brief Stampa i dati dello studente.` |
| `@author` | Autore | `@author Alex` |
| `@date` | Data della revisione | `@date 2026-11-28` |

Per una scelta interna al programma basta un commento breve:

```cpp
/// Aliquota ordinaria vigente per beni e servizi.
const double ALIQUOTA_IVA = 0.22;
```

### ✅ Esempio minimo

```cpp
/**
 * @file presentazione.cpp
 * @brief Stampa nome, classe e hobby dello studente.
 * @author Alex
 * @date 2026-11-28
 */
#include <iostream>

/**
 * @brief Punto di ingresso del programma.
 */
int main() {
    /// Dato mostrato nel profilo iniziale dello studente.
    std::cout << "Nome: Alex\n";
    std::cout << "Classe: 3A SIA\n";
    std::cout << "Hobby: fotografia\n";
    return 0;
}
```

Non generiamo ancora pagine HTML con Doxygen: impariamo prima a scrivere
commenti standard e utili.

### ⚖️ Regola di proporzionalità

| Situazione | Documentazione |
|---|---|
| Programma completo più lungo di circa 15 righe | `@file` e `@brief`, più autore/data se richiesti |
| Snippet o esercizio breve | `///` solo quando chiarisce un perché |
| Sempre da evitare | Commenti tautologici che ripetono la sintassi |

```cpp
/// 0.22 è l'aliquota IVA ordinaria usata dal listino.
const double ALIQUOTA_IVA = 0.22;
```

Non scrivere invece:

```cpp
/// Dichiara una costante double.
const double ALIQUOTA_IVA = 0.22;
```

### 🧪 Mini-attività

Prendi un programma del capitolo precedente e:

1. aggiungi `@file` e `@brief` in testa;
2. aggiungi un `@brief` a `main`;
3. inserisci un solo `///` che spieghi un vincolo del caso aziendale;
4. verifica che l'output non sia cambiato.

### 📝 Riepilogo tascabile

- [ ] Doxygen usa commenti standard leggibili anche come semplice testo.
- [ ] In questa fase i tag principali sono `@file`, `@brief`, `@author` e `@date`.
- [ ] `///` spiega il perché, non il gesto ovvio del codice.
- [ ] La documentazione deve crescere insieme alla complessità del programma.

### ➡️ Prossimo passo

Ora prosegui con espressioni, confronti e decisioni; più avanti tornerai su
Doxygen quando avrai funzioni da descrivere davvero.
