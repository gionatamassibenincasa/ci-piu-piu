<!--
  TEMPLATE DI LEZIONE — Ci Più Più
  Uso: copia questo file in chapters/XX_nome_argomento.md e sostituisci i
  placeholder. Ogni capitolo deve essere un "chunk" autonomo di 15-25 minuti.
  Riferimenti: SKILLS.md + docs/ (quiz, chunking, PRIMM, Head First).
-->

## 📌 Capitolo XX: [Titolo chiaro e concreto — es. "Il Tornello delle Decisioni"]

> "[Citazione breve e pertinente]"  
> — *Autore o Principio*

[2-4 frasi di contesto che collegano il nuovo concetto a ciò che lo studente già sa e al mondo aziendale. Tono conversazionale, "tu".]

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sarai in grado di:
- [Obiettivo unico e osservabile — un solo concetto principale]
- (opzionale) [Secondo micro-obiettivo strettamente collegato]

---

### 💡 La Metafora Guida

> 💡 **Metafora:**  
> [Analogia concreta e memorabile, preferibilmente dal mondo economico-aziendale o dalla vita quotidiana degli studenti.  
> Spiega chiaramente *cosa corrisponde a cosa* (es. "la variabile è una scatola etichettata nel magazzino della memoria").]

---

### 🔬 Laboratorio PRIMM: [Nome del programma / scenario aziendale]

#### 1. PREDICT (Prevedi)
Prima di eseguire qualsiasi cosa, guarda il codice e rispondi.

**Domanda di previsione (single-choice):**

Cosa pensi che succeda quando viene eseguito il programma qui sotto?

[( )] [Opzione plausibile ma sbagliata]
[(X)] [Opzione corretta]
[( )] [Opzione sbagliata]
[( )] [Opzione sbagliata]

<!-- Varianti quiz utili:
  Multiple-choice:
  [[X]] opzione corretta
  [[ ]] opzione sbagliata

  Text input:
  [[risposta esatta]]

  Selection (dropdown):
  La variabile di tipo intero si dichiara con [[ (int) | float | string | bool ]].
-->

#### 2. RUN (Esegui)
Copia il codice **a mano** (non fare copia-incolla) nel blocco qui sotto e premilo "Run". Confronta l'output con la tua previsione.

```cpp
/**
 * @file [nome_file].cpp
 * @brief [Descrizione breve del programma — cosa fa in termini aziendali]
 * @author [Nome]
 * @date [YYYY-MM-DD]
 */
#include <iostream>

/**
 * @brief Punto di ingresso del programma.
 * @return int 0 se tutto è andato bene.
 */
int main() {
    // --- codice del programma ---
    // Commenti /// solo sul "perché" (logica economica o motivo della scelta)
    
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
Analizziamo il codice come detective. Usa la tabella e, se utile, Python Tutor.

| Riga / Costrutto              | Cosa fa (spiegazione brain-friendly)                  | Perché è importante in azienda          |
|-------------------------------|-------------------------------------------------------|-----------------------------------------|
| `...`                         | ...                                                   | ...                                     |
| `...`                         | ...                                                   | ...                                     |

> 🔗 **Ispezione memoria:** Incolla il codice su [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva passo-passo come cambiano le variabili nello stack.

<!-- Opzionale: diagramma di flusso -->
```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
start
:Azione iniziale;
if (Condizione?) then (sì)
  :Ramo vero;
else (no)
  :Ramo falso;
endif
:Fine;
stop
@enduml
```

#### 4. MODIFY (Modifica)
Apporta **piccole modifiche guidate**. Ogni modifica deve avere uno scopo chiaro.

1. [Modifica semplice — es. cambia un valore letterale]
2. [Modifica media — es. aggiungi un input da tastiera]
3. [Modifica un po' più impegnativa]

<details>
<summary>💡 Scaffold / Suggerimento</summary>

```cpp
// Scheletro da completare — non guardare subito la soluzione completa
#include <iostream>

int main() {
    // TODO: ...
    return 0;
}
```

</details>

#### 5. MAKE (Crea)
Scrivi un **nuovo programma** partendo da zero (puoi riutilizzare idee e pezzi del laboratorio precedente).

**Scenario aziendale:**  
[Descrizione concreta di un piccolo problema gestionale realistico — es. "calcola se un ordine può essere evaso in base alla giacenza di magazzino"].

**Requisiti minimi:**
- [Requisito 1]
- [Requisito 2]
- [Requisito 3]
- Documentazione Doxygen se il programma supera le ~15 righe

<details>
<summary>💡 Scaffold di partenza (opzionale)</summary>

```cpp
/**
 * @brief [Descrizione]
 */
#include <iostream>

int main() {
    // Il tuo codice qui
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile
- [Punto chiave 1 — in una riga]
- [Punto chiave 2]
- [Punto chiave 3]
- [Eventuale "tranello" tipico da ricordare]

---

### ➡️ Prossimo chunk
Nel prossimo capitolo vedremo [anteprima motivante del concetto successivo, collegata al mondo aziendale].

---

<!-- 
  NOTE PER L'AUTORE / LLM (non visibili allo studente)
  - Un solo obiettivo principale per chunk.
  - Metafora obbligatoria e esplicita.
  - Quiz: usa SEMPRE la sintassi LiaScript corretta (vedi docs/quiz_liascript.md).
  - Codice eseguibile termina sempre con @LIA.cpp
  - Commenti /// solo sul "perché", mai tautologie.
  - Preferisci scenari di Economia Aziendale (magazzino, POS, clienti, IVA, ordini...).
  - Durata target: 15-25 minuti di lavoro studente.
-->
