# Etichette semantiche (ruoli e pattern)

**Stato:** vocabolario didattico e guida per autori / LLM (stadio 0–1).  
**Non** è ancora una pipeline AST obbligatoria in `cipiupiu`.

Le etichette non descrivono solo la *sintassi* (`for`, `int&`), ma l’**intento** (accumulare, confrontare, leggere senza copiare). Servono a scrivere domande PRIMM migliori e, in prospettiva, a una proposta editoriale distintiva.

## Riferimenti

| Fonte | Contenuto |
|-------|-----------|
| [Ruoli delle variabili (CSEd UniBo)](https://csed-unibo.github.io/#!pages/ruoli_variabili.md) | Tassonomia Sajaniemi in italiano, uso didattico |
| [Pattern dei cicli (CSEd UniBo)](https://csed-unibo.github.io/#!pages/pattern_cicli.md) | Scansioni e ricerche lineari |
| Sajaniemi et al. | Ruoli che coprono la quasi totalità dei programmi introduttivi |
| Golden sample / quiz | [`GOLDEN_SAMPLE.md`](GOLDEN_SAMPLE.md), [`quiz_design.md`](quiz_design.md) |

**Principio UniBo (da rispettare):** non insegnare i ruoli in astratto all’inizio; **osservarli e nominarli** quando compaiono istanze concrete nel codice.

---

## 1. Ruoli delle variabili (Livello A)

Nomi **in italiano** (standard di progetto). Tra parentesi: equivalenti inglesi frequenti in letteratura.

| Ruolo (IT) | Idea | Esempio C++ tipico |
|------------|------|-------------------|
| **Valore fissato** | Dopo l’inizializzazione non cambia più | `const double ALIQUOTA = 0.22;`, parametro letto e non riassegnato |
| **Contatore** / **Indice** | Avanza in modo sistematico su una sequenza | `for (int i = 0; i < n; ++i)`, `size_t i` |
| **Valore più recente** | Ultimo valore letto o calcolato di una serie | `std::cin >> voto;` in un ciclo di validazione |
| **Valore più desiderato** | “Miglior” candidato finora (max, min, migliore offerta…) | `if (x > massimo) massimo = x;` |
| **Accumulatore** | Aggrega stato con dipendenza dal passo precedente | `somma += importo;`, `conteggio++` filtrato |
| **Precedente** | Memoria del passo *t−1* | `prec = corrente;` prima di avanzare |
| **Flag unidirezionale** | Booleano che, una volta vero (o falso), non torna indietro | `bool trovato = false; … trovato = true;` |
| **Temporanea** | Appoggio a breve vita (swap, calcolo intermedio) | `auto tmp = a; a = b; b = tmp;` |
| **Attraversatore** | Cursore / iteratore sul contenitore | `auto it = v.begin();`, range-`for` sulla variabile di elemento |
| **Organizer** / **Container** | Struttura che organizza o contiene altri dati (uso avanzato) | `std::vector<Riga> righe;` come tabella in RAM |

In 3ª SIA introdurre **pochi ruoli per volta** (prima valore fissato, contatore, accumulatore, valore più desiderato; poi flag, precedente, ecc.).

---

## 2. Semantica dei parametri e riferimenti (Livello B, C++ )

Specifico del C++; non sostituisce i ruoli, li affianca sulla **firma**.

| Etichetta (IT) | Forma tipica | Intento |
|----------------|--------------|---------|
| **In ingresso per valore** | `T x` | Copia locale; le modifiche non escono |
| **In ingresso in sola lettura** | `const T& x`, `std::string_view` | Osserva senza copia (*view*) |
| **Parametro di uscita** | `T& x` / `T* x` usato solo in scrittura | Canale di output |
| **In-out (mutatore)** | `T& x` letto e scritto | Trasformazione sul posto |
| **Bersaglio opzionale** | `T* x` che può essere `nullptr` | Assenza ammissibile |

Usarle nelle domande Investigate/Modify quando si trattano funzioni e `&` / `const`.

---

## 3. Pattern sui cicli (Livello C)

Allineati a [pattern_cicli UniBo](https://csed-unibo.github.io/#!pages/pattern_cicli.md):

| Pattern (IT) | Idea | Ruoli spesso coinvolti |
|--------------|------|-------------------------|
| **Scansione lineare semplice** | Si visitano tutti gli elementi; azione per elemento | Indice / attraversatore |
| **Scansione lineare con accumulo** | Si costruisce un risultato aggregato | Accumulatore (+ eventuale filtro) |
| **Ricerca lineare certa** | Si sa che l’elemento c’è; uscita al ritrovamento | Flag unidirezionale o `break` |
| **Ricerca lineare incerta** | Potrebbe non esserci; gestire “non trovato” | Flag + valore sentinella / optional |
| **Scansione fino a sentinella** | Input o sequenza termina con valore speciale | Valore più recente + guardia |
| **Validazione in input** | Rilegge finché il valore non è accettabile | Valore più recente |

---

## 4. Uso nelle fasi PRIMM

| Fase | Uso delle etichette |
|------|---------------------|
| **Predict** | Chiedere l’effetto o il ruolo *prima* del Run (anche con nomi neutri `a`, `b`, `c`) |
| **Run** | Casi di test che rendono visibile un ruolo (es. stato prima/dopo se in-out) |
| **Investigate** | Etichettatura inversa; domande *perché* su `const&`, inizializzazione dell’accumulatore, ordine |
| **Modify** | Transizione di ruolo (es. da accumulatore-conteggio a valore più desiderato) |
| **Make** | Specifica a “ricetta”: “usa un accumulatore e un valore fissato soglia” |

**Non** applicare un vocabolario pieno al cap. 03 (`cout` / `main`): lì non ci sono ancora cicli né parametri significativi. Il golden sample resta valido; le etichette entrano da **variabili, selezione, cicli, funzioni**.

---

## 5. Frontmatter opzionale (stadio 1)

`components` ammette proprietà aggiuntive. Esempio:

```yaml
components:
  semantic_labels:
    - name: somma
      role: accumulatore
      note: "somma += riga.importo in scansione con accumulo"
    - name: soglia
      role: valore fissato
    - name: catalogo
      role: in ingresso in sola lettura
      signature: "const std::vector<Articolo>&"
  investigate_quiz:
    items:
      - question: >
          `somma` è un accumulatore. Cosa succede se la azzeri *dentro* il `for`
          invece che prima del ciclo?
        options:
          - text: "A ogni iterazione si perde l'aggregato precedente; il totale finale è sbagliato"
            correct: true
          - text: "Nulla: l'accumulatore si ricostruisce da solo"
            correct: false
          - text: "Il programma non compila"
            correct: false
```

Le macro `[[ investigate_block() ]]` non espongono ancora le etichette in automatico: servono all’autore/LLM per **calibrare** le domande. Una futura estensione potrà elencarle in Investigate.

---

## 6. Checklist autore / LLM

- [ ] Ho nominato i ruoli solo quando il codice li rende visibili
- [ ] Uso i **termini italiani** UniBo (non solo `GATHERER` / `STEPPER`)
- [ ] Almeno una domanda Investigate o Modify sfrutta un ruolo o un pattern di ciclo
- [ ] Make (se presente) può citare 1–3 vincoli di ruolo, non un saggio di teoria
- [ ] Nessuna dipendenza da Clang/AST richiesta per validare il capitolo

---

## 7. Fuori scope (per ora)

- Analyzer automatico Clang / Tree-sitter in `cipiupiu validate`
- Sostituzione dei nomi parlanti in tutti i Predict senza revisione umana
- Rubrica di correzione automatica basata solo sui ruoli

Quando servirà scala editoriale, l’estrazione semi-automatica (Livello B sulle firme, candidati di ruolo sui cicli) potrà *proporre* etichette; la decisione didattica resta umana.
