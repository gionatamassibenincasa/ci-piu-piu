<!--
  TEMPLATE DI LEZIONE — Ci Più Più
  Uso: copia questo file in chapters/XX_nome_argomento.md e sostituisci i
  placeholder. Ogni capitolo deve essere un "chunk" autonomo di 15-25 minuti.

  Riferimenti obbligatori:
  - SKILLS.md                          (profilo docente e regole generali)
  - docs/chunking.md                   (un solo obiettivo, durata, check)
  - docs/primm.md                      (le cinque fasi in dettaglio)
  - docs/head_first_style.md           (metafore, tono, scenari aziendali)
  - docs/quiz_liascript.md             (sintassi dei quiz LiaScript)
  - .agents/skills/liascript-syntax/   (sintassi ufficiale LiaScript)

  DIVIETI PER LLM (non negoziabili):
  - Non usare quiz in stile GitHub (`- [ ]` / `- [x]` o `? domanda`).
  - Usare solo: [(X)] [( )]   [[X]] [[ ]]   [[testo]]   [[ (a) | b | c ]]
  - Il codice ESEGUIBILE ha SEMPRE la riga @LIA.cpp subito dopo il fence di chiusura.
  - Il codice del PREDICT NON ha @LIA.cpp (è solo da osservare).
  - Non introdurre nel Modify/Make costrutti non ancora insegnati in questo o nei
    capitoli precedenti.
  - Un solo obiettivo principale per chunk; niente "anche ti spiego X, Y e Z".
  - Commenti /// solo sul "perché" (logica economica o motivo della scelta),
    mai tautologie del tipo "incrementa i di 1".
-->

## 📌 Capitolo N: [Titolo chiaro — es. Il Tornello delle Decisioni (`if` / `if-else`)]

> "[Citazione breve, pertinente e verificata]"  
> — *Autore (pioniere dell'informatica o voce nota tra gli sviluppatori)*

[2–4 frasi di contesto: collega il concetto a ciò che lo studente già sa e a uno scenario aziendale. Tono conversazionale, "tu".  
Esempio di tono: "Finora i programmi correvano su un unico binario. In magazzino invece un ordine può essere evaso oppure no: serve un bivio."]

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- [Obiettivo unico e osservabile — un solo concetto principale]
- (opzionale) [Secondo micro-obiettivo strettamente collegato allo stesso concetto]

---

### 💡 La Metafora Guida

> 💡 **Metafora:**  
> [Analogia concreta e memorabile, preferibilmente economico-aziendale o dalla vita quotidiana.  
> Spiega *cosa corrisponde a cosa* (es. "la variabile è uno sportello etichettato nel magazzino della memoria").]

---

<!-- Opzionale ma consigliato quando ci sono regole o trappole da fissare PRIMA del lab -->
### ⚙️ [Concetto in breve / regole essenziali]

[Tabella, elenco o 5–10 righe di teoria essenziale. Niente digressioni.]

<!-- Opzionale -->
### ⚠️ Tranelli tipici
- [Errore classico 1 e come evitarlo]
- [Errore classico 2]

---

### 🔬 Laboratorio PRIMM: [Nome del programma / scenario aziendale]

**Codice da osservare (non eseguire ancora — senza `@LIA.cpp`):**

```cpp
// Versione essenziale, senza commenti, solo per il Predict
#include <iostream>

int main() {
    // ...
    return 0;
}
```

#### 1. PREDICT (Prevedi)
Prima di eseguire, guarda il codice sopra e rispondi.

**Una domanda di previsione (obbligatoria, single-choice):**

Cosa succede quando viene eseguito il programma?

[( )] [Opzione plausibile ma sbagliata]
[(X)] [Opzione corretta]
[( )] [Opzione sbagliata]
[( )] [Opzione sbagliata]

<details>
<summary>💡 Spiegazione</summary>
[Perché l'opzione corretta è corretta; 2–4 frasi. Usa <code>…</code> per i frammenti di codice.]
</details>

<!--
  Quiz: UNA previsione obbligatoria nel Predict.
  Altre 1–2 domande (se servono) vanno in Investigate o Modify, non qui.
  Varianti ammesse (docs/quiz_liascript.md):
    Multiple-choice:  [[X]]  /  [[ ]]
    Text input:       [[risposta esatta]]
    Selection:        [[ (int) | float | string | bool ]]
-->

#### 2. RUN (Esegui)
Esegui il codice qui sotto e premi **Run**. Confronta l'output con la tua previsione.

```cpp
/**
 * @file [nome_file].cpp
 * @brief [Cosa fa, in termini aziendali — una riga]
 */
#include <iostream>

/**
 * @brief [Ruolo di main, se utile]
 * @return int 0 se ok.
 */
int main() {
    // Commenti /// solo sul "perché" (logica economica o motivo della scelta)

    return 0;
}
```
@LIA.cpp

<!--
  Contratto LiaScript:
  - Questo è lo STESSO programma del blocco "da osservare", eventualmente
    arricchito di commenti Doxygen / ///.
  - La riga @LIA.cpp deve stare SUBITO DOPO il fence di chiusura, da sola.
  - Senza @LIA.cpp il blocco non è eseguibile in LiaScript.
-->

#### 3. INVESTIGATE (Investiga)
Analizziamo il codice come detective. Usa la tabella e, se c'è stato di memoria, Python Tutor.

| Riga / Costrutto | Cosa fa (spiegazione brain-friendly) | Perché è importante |
|------------------|--------------------------------------|---------------------|
| `...`            | ...                                  | ...                 |
| `...`            | ...                                  | ...                 |

> 🔗 **Ispezione memoria:** incolla il codice su [Python Tutor C++](https://pythontutor.com/cpp.html) e osserva passo-passo stack e variabili.

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

<!-- Opzionale: 1–2 quiz di consolidamento (stessa sintassi LiaScript del Predict) -->

#### 4. MODIFY (Modifica)
Apporta **piccole modifiche guidate**. Ogni modifica ha uno scopo chiaro.  
**Non introdurre costrutti nuovi** rispetto a questo capitolo e ai precedenti.

1. [Modifica semplice — es. cambia un letterale]
2. [Modifica media — es. aggiungi un controllo o un messaggio]
3. [Modifica un po' più impegnativa — sempre con gli strumenti già visti]

<details>
<summary>💡 Scaffold / Suggerimento</summary>

```cpp
#include <iostream>

int main() {
    // TODO: ...
    return 0;
}
```

</details>

#### 5. MAKE (Crea)
Scrivi un **nuovo programma** da zero (puoi riutilizzare idee del laboratorio, non copiare e basta).

**Scenario aziendale:**  
[Problema gestionale realistico e piccolo — es. "verifica se un ordine può essere evaso data la giacenza"].

**Requisiti minimi:**
- [Requisito 1]
- [Requisito 2]
- [Requisito 3]
- Documentazione Doxygen se il programma supera le ~15 righe
- Commenti `///` solo sul perché

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
- [Punto chiave 1 — una riga]
- [Punto chiave 2]
- [Punto chiave 3]
- [Eventuale tranello tipico da ricordare]

---

### ➡️ Prossimo chunk
Nel prossimo capitolo vedremo [anteprima motivante del concetto successivo, collegata al mondo aziendale].

---

<!-- Opzionale: solo se il ponte al capitolo successivo è davvero "sbloccante" -->
### ⚔️ Sfida
[Problema che diventa naturale solo con il concetto del *prossimo* chunk — 1 paragrafo, non un secondo Make.]

<!-- Opzionale: al massimo a fine unità / fine blocco, non in ogni lezione -->
### ⚔️⚔️⚔️ Mini-Progetto
[Problema di ~30 minuti che riusa i chunk *fino a qui*. Requisiti numerati. Non sostituisce il Make del capitolo.]

---

<!--
  NOTE PER L'AUTORE / LLM (non finiscono nel testo studente se restano in commento HTML)

  Checklist rapida:
  [ ] Un solo obiettivo principale (docs/chunking.md)
  [ ] Metafora obbligatoria e mappata concetto↔immagine (docs/head_first_style.md)
  [ ] Predict: quiz LiaScript corretto PRIMA di qualsiasi Run (docs/primm.md, docs/quiz_liascript.md)
  [ ] Blocco "da osservare" SENZA @LIA.cpp; blocco RUN CON @LIA.cpp
  [ ] Investigate: tabella e/o Python Tutor se c'è stato di memoria
  [ ] Modify: scaffold progressivo, nessun costrutto futuro
  [ ] Make: scenario aziendale diverso + requisiti chiari + Doxygen se > ~15 righe
  [ ] Commenti /// solo sul "perché"
  [ ] Durata target del nucleo: 15–25 minuti
  [ ] Titolo nel formato: ## 📌 Capitolo N: ...
-->
