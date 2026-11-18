# Paper Pack – Specifiche (v0.1)

Verifiche cartacee PRIMM allineate ai capitoli, stampabili e integrabili con registro elettronico e workflow Classroom50.

**Stato**: specifica di prodotto (parzialmente implementato in CLI `print --template paper|registro`)  
**Dipende da**: frontmatter validato, Slice E (`print`), schema capitolo  
**Non sostituisce**: il compito digitale (`scaffold-assignment`) né il worksheet già generato da `print`
+**Prodotto**: P3 — vedi `docs/products.md`  

---

## 0. User Story (prodotto)

| ID | Storia |
|----|--------|
| US-D8 | Come **docente**, voglio generare un Paper Pack (verifica A/B, griglia, registro) da un capitolo con `assessment` e `registro`, così posso verificare in classe le stesse competenze del laboratorio digitale. |
| US-D9 | Come **docente**, voglio un file `registro.txt` con gli argomenti già formulati per il registro elettronico. |

Criterio di accettazione: `python -m tools.cipiupiu print 03 --template paper --emit json,typ,pdf --out-dir output` produce `verifica_A.pdf`, `verifica_B.pdf`, `griglia.pdf`, `registro.txt` (PDF se Typst è disponibile).

## 1. Obiettivo

Fornire al docente, per ogni capitolo PRIMM rilevante:

1. una **verifica in classe** stampabile (45–60 min), in una o più versioni parallele;
2. una **griglia di correzione** con punteggi e errori tipici;
3. un testo pronto per la sezione **Argomenti** del registro elettronico;
4. coerenza con obiettivi del capitolo, consegne digitali e artefatti `student_work/`.

Il Paper Pack è un **consumatore del modello di capitolo** (come `build` e `print`): non reinterpreta il Markdown didattico.

---

## 2. Integrazione con la progettazione didattica

| Elemento didattico | Ruolo del Paper Pack |
|--------------------|----------------------|
| Obiettivi del chunk | Diventano criteri osservabili in griglia |
| Predict (quiz + answers) | Una domanda Predict in verifica (codice + scelta o risposta breve) |
| Run | Di norma **non** in verifica formale (è pratica guidata); eventuale riflessione breve solo se serve |
| Investigate | 1–2 domande “cosa fa / a che serve” su frammenti noti |
| Modify | Un esercizio di modifica guidata su codice fornito nel foglio |
| Make | Un piccolo programma da scrivere da zero, requisiti chiusi |
| Assignment Classroom50 | Stessi obiettivi e lessico; la verifica misura in classe ciò che il repo esercita a casa |
| Registro elettronico | Campo `registro.argomenti` (e opzionale `registro.note`) copiabile nella lezione |

Flusso consigliato nel modulo:

```text
Lezione LiaScript (Predict→Run→Investigate)
    → lavoro su repo (Modify/Make) via Classroom50
    → verifica cartacea (campione delle stesse competenze)
    → registrazione voti + testo argomenti da frontmatter
```

Il Paper Pack **non** duplica l’intero laboratorio: seleziona un sottoinsieme valutabile in tempo limitato e in condizioni d’aula.

---

## 3. Contenuto di un Paper Pack (per capitolo)

### 3.1 Artefatti generati

```text
output/paper/
  <activity_id>/
    verifica_A.pdf          # foglio studente versione A
    verifica_B.pdf          # versione B (stessi obiettivi, dati diversi)
    griglia.pdf             # soluzioni + punteggi + errori tipici (solo docente)
    registro.txt            # testo argomenti (+ note) per copia-incolla
    pack.json               # modello intermedio (debug / altri exporter)
```

Formato di stampa: A4, margini scolastici, spazio risposte dimensionato, intestazione con `activity_id`, titolo breve, versione (A/B), campi Nome / Classe / Data.

### 3.2 Struttura della verifica studente

| Sezione | Durata indicativa | Fonte dati preferita |
|---------|-------------------|----------------------|
| Intestazione | — | `title`, `activity_id`, variante |
| 1. Predict | 5–8 min | `components.predict_quiz` e/o `assessment.predict` |
| 2. Investigate | 10–15 min | `components.investigate_questions` e/o `assessment.investigate` |
| 3. Modify | 10–15 min | codice da `files` phase modify + consegna da `assessment.modify` |
| 4. Make | 15–20 min | requisiti da `make_instructions` / `assessment.make` |
| Totale | 45–60 min | |

Punteggio complessivo consigliato: 10 punti (allineabile al registro), ripartiti esplicitamente in griglia.

### 3.3 Griglia docente

Per ogni esercizio:

- risposta / comportamento atteso;
- punteggio massimo e criteri di assegnazione parziale;
- 1–3 errori tipici (dal capitolo o da `assessment.*.typical_errors`).

La griglia **non** va stampata sul foglio studente.

---

## 4. Estensione frontmatter

Campi **opzionali** (il capitolo resta valido senza di essi).  
Schema: `schemas/chapter-frontmatter.schema.json` (versionare la modifica).

### 4.1 `registro` — testo per registro elettronico

```yaml
registro:
  argomenti: >
    Programma C++ minimo; direttiva #include <iostream>;
    std::cout e sequenze di escape (\n); funzione main e return 0;
    introduzione al namespace std. Metodologia PRIMM sul programma Ciao Mondo.
  note: >
    Verifica scritta in classe sulle fasi Predict, Investigate, Modify e Make.
    Lavoro digitale correlato su repository Classroom50.
```

- `argomenti` (string, consigliato se si usa il Paper Pack): testo unico, 1–4 frasi, adatto al campo “Argomenti” / “Contenuti” del registro (Argo, Spaggiari, Axios, ecc.).
- `note` (string, opzionale): indicazioni interne (tipo di prova, collegamento al compito GitHub).

Il comando di export scrive `registro.txt` concatenando questi campi in forma pronta al copia-incolla.

### 4.2 `assessment` — contenuto della verifica formale

```yaml
assessment:
  duration_min: 50
  total_points: 10
  versions: ["A", "B"]
  predict:
    points: 2
    # se assente, si riusa components.predict_quiz
  investigate:
    points: 3
    questions:
      - "A che serve #include <iostream>?"
      - "Qual è il ruolo di main? Cosa succede se manca?"
    typical_errors:
      - "Confonde include con una chiamata a runtime"
  modify:
    points: 2
    prompt: >
      Nel programma fornito, aggiungi una seconda istruzione di output
      che stampi la tua classe su una nuova riga. Non rimuovere la riga esistente.
    # il codice di partenza si prende dal file phase=modify action=create se presente
  make:
    points: 3
    prompt: >
      Scrivi un programma completo che stampi tre righe: nome, classe, hobby.
      Usa #include <iostream>, main, std::cout, \n e return 0.
    must_include:
      - "std::cout"
      - "return 0"
```

Regole:

- Se `assessment` è assente, `print --template paper` può rifiutare il capitolo o generare solo un *worksheet* ridotto (comportamento da dichiarare in CLI).
- Le versioni B (C, …) differiscono per letterali/codice/distrattori, non per obiettivi né punteggi.
- `typical_errors` alimenta solo la griglia docente.

### 4.3 Relazione con i campi già esistenti

| Bisogno stampa | Campo esistente | Campo assessment |
|----------------|-----------------|------------------|
| Quiz Predict | `components.predict_quiz` | override opzionale |
| Domande aperte | `investigate_questions`, template answers | `assessment.investigate.questions` |
| Codice Modify | `files[]` phase modify | `assessment.modify.prompt` |
| Requisiti Make | `make_instructions`, `files[]` make | `assessment.make.prompt` |
| Argomenti registro | — | `registro.argomenti` |

Una sola fonte di verità per il codice di partenza Modify: il file `action: create` con `phase: modify`. L’assessment aggiunge solo la consegna e i punti.

---

## 5. CLI (estensione Slice E)

```bash
# modello + PDF verifica (tutte le versioni) + griglia + registro.txt
python -m tools.cipiupiu print \
  --activity ciao-mondo-01 \
  --template paper \
  --emit pdf,json \
  --out output/paper

# solo testo registro
python -m tools.cipiupiu print \
  --activity ciao-mondo-01 \
  --template registro \
  --emit text
```

Contratto:

1. Valida il frontmatter con lo stesso validatore di `build`.
2. Costruisce `pack.json` (capitolo + assessment risolto + versioni).
3. Genera Typst → PDF per ogni versione e per la griglia.
4. Scrive `registro.txt` da `registro.*`.
5. Non legge il corpo Markdown per inventare esercizi: solo frontmatter (e file dichiarati).

Dipendenza PDF: binario Typst nel `PATH` (come per il worksheet attuale).

---

## 6. Esempio minimo – capitolo 03 (Ciao Mondo)

Frammento da unire al frontmatter esistente:

```yaml
registro:
  argomenti: >
    Programma C++ minimo; #include <iostream>; std::cout e \n;
    funzione main e return 0; namespace std. Laboratorio PRIMM su Ciao Mondo.
  note: >
    Verifica scritta (Predict, Investigate, Modify, Make). Compito digitale correlato su Classroom50.

assessment:
  duration_min: 50
  total_points: 10
  versions: ["A", "B"]
  predict:
    points: 2
  investigate:
    points: 3
    questions:
      - "A che serve `#include <iostream>`?"
      - "Qual è il ruolo della funzione `main`?"
      - "Cosa significa `std::` davanti a `cout`?"
    typical_errors:
      - "Descrive include come se venisse eseguita a runtime"
      - "Ommette che main è il punto di ingresso obbligatorio"
  modify:
    points: 2
    prompt: >
      Partendo dal codice stampato sul foglio, aggiungi una seconda riga di output
      con la tua classe. Lascia invariata la riga "Ciao, Mondo!".
  make:
    points: 3
    prompt: >
      Scrivi da zero un programma che stampi tre righe separate: nome, classe, hobby.
      Obbligatori: #include <iostream>, int main(), std::cout, \n, return 0.
    must_include:
      - "std::cout"
      - "return 0"
```

Versione B: stessi punti e prompt; letterali e ordine delle domande Investigate permutati; eventuale variante del frammento Predict.

---

## 7. Fuori scope v0.1

- Generazione automatica di infinite varianti via LLM (possibile assistente interno, non requisito)
- Correzione automatica della scansione del foglio
- Integrazione API diretta con registri elettronici commerciali
- Sostituzione del compito Classroom50

---

## 8. Criteri di accettazione

1. Schema aggiornato: `registro` e `assessment` opzionali, validati da `cipiupiu validate`.
2. Per un capitolo con `assessment` completo, `print --template paper` produce almeno `verifica_A.pdf`, `griglia.pdf`, `registro.txt`.
3. Il testo di `registro.argomenti` compare invariato (trim) in `registro.txt`.
4. Nessun esercizio della verifica è inventato dal corpo Markdown.
5. Documentazione collegata da `docs/SPEC.md` (obiettivo O7 / US-D7 e US-S6).

---

## 9. Riferimenti

- `docs/SPEC.md` — pipeline `print`, principi “stampa = consumatore”
- `schemas/chapter-frontmatter.schema.json`
- Worksheet esistente (Slice E): non eliminato; il template `paper` è un profilo aggiuntivo orientato alla **valutazione formale**

## 12. Qualità item e versioni A/B (obbligo di progetto)

### 12.1 Tipi di domanda preferiti
- **Tracing**: frammento di codice + domanda sullo stato (valori, quante copie, cosa punta dove).
- **Perché**: “perché non compila / perché questo output / perché questo invariante”.
- Evitare come unico item del pacchetto domande solo mnemonico-sintattiche.

### 12.2 ID stabili
Ogni item in `pack.json` espone `id` del tipo `{activity_id}/{phase}` o `{activity_id}/{phase}/{n}`.  
Gli id restano stabili tra edizioni se il significato dell’item non cambia.

### 12.3 Campo `context`
In `assessment.predict|investigate|modify|make`:

```yaml
context: >
  Spiegazione breve della risposta corretta (solo griglia docente).
```

La griglia mostra: risposta attesa (se nota), `context`, `typical_errors`.

### 12.4 Varianti A/B con contenuto diverso

```yaml
assessment:
  versions: ["A", "B"]
  variants:
    B:
      predict:
        prompt: "..."   # opzionale: override
        # code/dati diversi ammessi
      modify:
        prompt: "Stessi obiettivi, letterali/numeri diversi da A"
```

Se `variants.B` è assente, B riusa il contenuto base (solo etichetta diversa) — accettabile in bozza, **non** come obiettivo finale di qualità.

### 12.5 Visualizzazione processo
Il Paper Pack non sostituisce Investigate online; in verifica si può chiedere di **completare una tabella di traccia** già impostata sul foglio (tracing cartaceo).
