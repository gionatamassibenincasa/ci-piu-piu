# PRIMM — Guida operativa per Ci Più Più

Riferimento: [PRIMM Portal](https://primmportal.com/) e ricerca di Sue Sentance & Jane Waite.

PRIMM = **P**redict → **R**un → **I**nvestigate → **M**odify → **M**ake  
È il modo in cui strutturiamo **ogni** nuovo concetto di programmazione.

## Perché PRIMM
Gli studenti principianti tendono a:
- copiare codice senza capirlo;
- scrivere prima di aver letto;
- concentrarsi sulla sintassi invece che sul comportamento.

PRIMM inverte l’ordine: prima si legge e si discute codice funzionante, poi si modifica, infine si crea.

## Le cinque fasi — cosa fare concretamente

### 1. PREDICT (Prevedi)
- Mostra un programma **già funzionante** (o un frammento significativo).
- Chiedi cosa farà **prima** di eseguirlo.
- Preferisci un quiz single-choice LiaScript (sintassi `[(X)]`).
- Obiettivo: far emergere modelli mentali e misconception.

**Buone domande Predict:**
- “Cosa verrà stampato?”
- “Quante volte verrà eseguito il corpo del ciclo?”
- “Il programma compilerà? Se no, perché?”

**Evitare:** domande generiche tipo “Cosa fa questo codice?”.

### 2. RUN (Esegui)
- Lo studente digita il codice **a mano** (no copia-incolla) nel blocco `@LIA.cpp` o in VS Code.
- Esegue e confronta l’output con la previsione.
- Discrepanza = momento didattico d’oro.

### 3. INVESTIGATE (Investiga)
- Guida l’analisi del *perché*.
- Strumenti obbligatori quando c’è manipolazione di variabili/memoria:
  - Tabella di traccia (valori delle variabili passo-passo).
  - Link a [Python Tutor C++](https://pythontutor.com/cpp.html).
  - Diagramma plantUML se il flusso è non banale.
- Domande tipiche: “Cosa succede allo stack quando…?”, “Perché quella variabile vale X dopo il ciclo?”.

### 4. MODIFY (Modifica)
- Piccole modifiche guidate e progressive.
- Ogni modifica ha uno scopo chiaro e non introduce costrutti nuovi.
- Fornisci sempre uno **scaffold** (scheletro) dentro `<details>`.
- Trasferisce gradualmente la proprietà del codice (“non è più del docente, è un po’ mio”).

Esempi di progressione:
1. Cambia un letterale.
2. Sostituisci un valore hardcoded con `std::cin`.
3. Aggiungi un secondo `if` o un contatore.

### 5. MAKE (Crea)
- Nuovo programma da zero su uno **scenario aziendale** diverso ma che riusa gli stessi costrutti.
- Fornisci requisiti chiari (3-5 punti) e, se utile, uno scaffold minimo.
- Non dare la soluzione completa a vista; nascondila o non fornirla affatto se è compito valutato.

## Come integrare PRIMM nel template
Il file `docs/template_lezione.md` contiene già le cinque sezioni nell’ordine corretto.  
Non saltare fasi. Non fondere Predict e Investigate. Non mettere il Make prima del Modify.

## Productive Failure + PRIMM
Prima di un concetto “potente” (array, funzioni, struct) si può inserire un mini-chunk di Productive Failure:
1. Problema apparentemente risolvibile con gli strumenti attuali.
2. Gli studenti falliscono in modo produttivo (tempo e fatica eccessivi).
3. Solo allora si introduce il nuovo costrutto con un ciclo PRIMM completo.

## Checklist PRIMM
- [ ] Predict ha un quiz o una domanda chiusa prima di qualsiasi esecuzione
- [ ] Run usa codice funzionante e `@LIA.cpp`
- [ ] Investigate contiene tabella e/o Python Tutor
- [ ] Modify ha almeno 2-3 modifiche progressive + scaffold
- [ ] Make è uno scenario aziendale nuovo con requisiti espliciti
- [ ] Nessuna fase introduce costrutti non ancora insegnati
