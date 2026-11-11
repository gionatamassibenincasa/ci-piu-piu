## 🧭 Guida allo Studio: Come Imparare a Programmare

> "Non si può insegnare niente a un uomo; si può solo aiutarlo a scoprire ciò che ha dentro di sé."
> — *Galileo Galilei*

Imparare a programmare non significa memorizzare comandi a memoria: significa sviluppare un **metodo di lavoro mentale**.

Questa guida raccoglie due strumenti metodologici complementari pensati per accompagnarti lungo tutto il corso:
1. **La visione d'insieme:** come studiare e assimilare i contenuti di ogni capitolo (metodo di lettura tecnica).
2. **Il lavoro pratico:** come affrontare ogni singolo programma ed esercizio di codice (metodo PRIMM).

---

### 📖 Consigli per ottenere il massimo da un testo tecnico

> 💡 *Traduzione e adattamento per la classe del saggio di Sebastian Raschka: [How to Read Technical Books](https://sebastianraschka.com/blog/2025/reading-books.html).*

Ti suggeriamo vivamente di affrontare il materiale **in ordine**, poiché ogni capitolo costruisce sulle basi di quello precedente. Per ogni capitolo, ti raccomandiamo di seguire questi 5 passaggi:

#### 1. Prima lettura (offline e panoramica)
- Leggi il capitolo dall'inizio alla fine **senza ancora scrivere codice**. L'obiettivo è ottenere una visione d'insieme del quadro generale.
- Se possibile, leggi lontano dalle distrazioni del computer (una copia stampata o uno schermo senza notifiche, browser o social).
- Mantieni questa sessione breve e mirata (circa **20 minuti**): non bloccarti sui dettagli e non fare ricerche esterne adesso. Annota o evidenzia semplicemente i punti che ti incuriosiscono o ti sembrano confusi.

#### 2. Seconda lettura (con il codice tra le mani)
- Rileggi il capitolo, ma questa volta **digita ed esegui il codice**.
- **Regola d'oro:** riscrivere il codice a mano richiede più tempo rispetto al fare copia-incolla, ma costringe la mente a riflettere su ogni singola istruzione, sintassi e punteggiatura.
- Se ottieni un risultato inatteso o un errore del compilatore, cerca di capirne il motivo. Se dopo averci riflettuto non trovi la causa, confrontati con i compagni o chiedi al docente.

#### 3. Esercizi (mettersi alla prova)
- Dopo aver digitato e compreso il codice base, affronta gli esercizi proposti.
- Gli esercizi servono a consolidare la comprensione in modo guidato.
- Se un esercizio ti sembra troppo difficile, consulta i suggerimenti o la soluzione, ma **solo dopo aver fatto un tentativo serio**.

#### 4. Revisione delle note e approfondimenti
- Torna alle parti che avevi annotato o evidenziato durante le prime due letture: ci sono ancora dubbi irrisolti?
- Questo è il momento perfetto per consultare la documentazione, approfondire o chiedere chiarimenti in classe.
- Riporta sul tuo quaderno (o nella tua app di note) le intuizioni più importanti, gli schemi o i frammenti di codice riutilizzabili.

#### 5. Applicare le idee in un progetto personale
- I passaggi precedenti servono ad assorbire la conoscenza. Ora prova a chiederti: *"Come posso usare questo concetto in un progetto mio?"*
- Costruisci un piccolo programma partendo dagli esempi del capitolo. A volte basta una piccola idea per consolidare una grande competenza!

> 💬 **Considerazioni aggiuntive:**  
> Questo approccio non è scolpito nella pietra: se un argomento ti è già del tutto familiare, puoi velocizzare la lettura per dedicare più tempo ai concetti nuovi. Nei capitoli puramente concettuali, concentrati sulla comprensione logica senza forzare la scrittura di codice.

---

### 🔬 Il Metodo PRIMM: Come affrontare ogni programma

> 💡 *Adattato dalle linee guida pedagogiche di [primmportal.com](https://primmportal.com/).*

Ogni volta che incontri un programma nel libro di testo, negli appunti o durante le lezioni in laboratorio, non limitarti a guardarlo passivamente. Segui rigorosamente queste 5 tappe:

```
[ 1. Predict ]  ──►  [ 2. Run ]  ──►  [ 3. Investigate ]  ──►  [ 4. Modify ]  ──►  [ 5. Make ]
 (Prevedi & Traccia)  (Digita a mano)    (Debug & Memoria)     (Piccoli cambi)   (Crea da zero)
```

#### 1. PREDICT (Prevedi)
- Prima di eseguire il programma, esamina attentamente il codice sorgente e **ipotizza cosa farà**.
- Se il codice contiene condizioni, cicli o variabili che cambiano, costruisci sul quaderno una **tabella di traccia** (colonne con i valori assunti dalle variabili passo dopo passo).

#### 2. RUN (Esegui)
- Copia il programma nel tuo ambiente di sviluppo (VS Code o blocco interattivo `@LIA.cpp`).
- **Attenzione:** **non fare copia e incolla!** Digitare il codice parola per parola è indispensabile per memorizzare la sintassi e accorgersi dei dettagli.
- Esegui il programma e confronta l'output ottenuto con la previsione che avevi fatto al passo 1.

#### 3. INVESTIGATE (Investiga)
- Copia il programma su [Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html) ed eseguilo **passo dopo passo**.
- Osserva visivamente come evolve lo stato della memoria (Stack, variabili locali, tipi) a ogni istruzione di assegnamento.
- Confronta l'evoluzione effettiva con la tabella di traccia che hai disegnato sul quaderno.

#### 4. MODIFY (Modifica)
- Modifica il codice sorgente procedendo a piccoli passi, per fare tuo il programma:
  - *Esempio 1:* se il programma usa valori prefissati (hardcoded), modificalo per chiedere i dati all'utente tramite istruzioni di input (`std::cin`).
  - *Esempio 2:* se usa numeri interi (`int`), prova a convertirli in numeri a virgola mobile (`double`) o viceversa, osservando come cambia il comportamento della divisione.
- Più modifichi il codice con cognizione di causa, più ne diventi padrone.

#### 5. MAKE (Crea)
- Scrivi un **nuovo programma autonomo** partendo da zero.
- Puoi prendere in prestito frammenti o strutture logiche dal programma appena studiato, applicandoli per risolvere un problema diverso o per realizzare una funzione nuova.
- Questo è il momento in cui passi da "lettore di codice" a "creatore di software".
