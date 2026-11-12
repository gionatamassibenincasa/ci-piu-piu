# Chunking & Sequencing — Guida operativa

Riferimento: [NSW Education – Chunking and sequencing learning](https://education.nsw.gov.au/teaching-and-learning/curriculum/explicit-teaching/explicit-teaching-strategies/chunking-and-sequencing-learning)

## Perché chunking
La memoria di lavoro degli studenti (≈16 anni, primo linguaggio testuale) gestisce poche informazioni nuove alla volta.  
Un concetto complesso (es. “cicli + condizioni + I/O”) inserito tutto insieme provoca sovraccarico → frustrazione → apprendimento superficiale.

Il chunking spezza il materiale in **pezzi gestibili**, li consolida uno alla volta e solo dopo li collega.

## Regole operative per Ci Più Più

### 1. Un solo obiettivo principale per capitolo
Ogni file in `chapters/` deve rispondere a **una** domanda del tipo:
- “Alla fine di questa lezione so fare X”
- X deve essere osservabile e verificabile in 5-10 minuti di pratica.

Esempi buoni:
- Dichiarare e usare variabili `int` e `double` in un contesto di magazzino.
- Scrivere un `if-else` che decide se una transazione POS è approvata.

Esempi da evitare:
- “Capire le strutture di controllo” (troppo ampio).
- “Imparare i cicli” (va spezzato in while / for / do-while).

### 2. Durata target
- 15-25 minuti di lavoro studente (lettura + Predict + Run + Investigate + Modify).
- Il “Make” può sforare se è un compito da consegnare, ma il nucleo del chunk resta entro i 25 min.

### 3. Sequenza logica interna al chunk
1. Contesto + metafora (attiva conoscenza pregressa).
2. Obiettivo esplicito.
3. PRIMM (Predict → Run → Investigate → Modify → Make).
4. Riepilogo tascabile (3-5 punti).
5. Anteprima del chunk successivo (collegamento).

### 4. Check for understanding
Prima di passare al pezzo successivo (o al capitolo successivo) lo studente deve aver:
- Risposto correttamente al quiz di Predict (o aver capito l’errore).
- Eseguito almeno una Modify con successo.
- Visto lo stato della memoria su Python Tutor quando rilevante.

Se la classe intera fallisce il check → non avanzare, ritagliare o rifare il chunk.

### 5. Productive Failure come “chunk zero”
Prima di introdurre un costrutto potente (array, funzioni, puntatori) proponi un problema risolvibile *in teoria* con gli strumenti attuali ma *ingestibile in pratica*.  
Questo crea il bisogno cognitivo e rende il nuovo chunk desiderabile.

### 6. Dimensioni consigliate
| Elemento              | Dimensione massima consigliata |
|-----------------------|--------------------------------|
| Blocco di codice      | 25-30 righe (meglio di meno)   |
| Tabella Investigate   | 5-7 righe                      |
| Lista di requisiti Make | 3-5 punti                    |
| Riepilogo tascabile   | 4-6 bullet                     |

## Checklist rapida prima di chiudere un capitolo
- [ ] Un solo obiettivo principale scritto in cima
- [ ] Metafora presente e collegata all’obiettivo
- [ ] Nessun concetto “di passaggio” non necessario
- [ ] Quiz di Predict focalizzato sul concetto chiave
- [ ] Modify e Make non introducono nuovi costrutti non ancora visti
- [ ] Riepilogo tascabile rispecchia l’obiettivo
