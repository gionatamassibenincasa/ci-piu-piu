<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-14
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
← Prec. · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/01_ambiente-sviluppo-01.md)

---


## 🧭 Guida allo Studio: come imparare a programmare

> Il calcolatore era (ed è ancora) un nuovo e meraviglioso concetto filosofico
> e matematico. Il calcolatore è ancora più rivoluzionario come idea che come
> congegno pratico che modifica la società -- e tutti sappiamo quanto abbia
> cambiato la nostra vita.
>
> Perché lo dico? Perché il calcolatore cambia l'epistemologia, modifica il
> significato del verbo «comprendere».
> A mio giudizio, si capisce qualcosa solo se si è capaci -- noi, non altri! --
> di scriverne il programma.
> Altrimenti non si ha una vera comprensione, si crede soltanto di capire.
>
> — Gregory Chaitin, *Alla ricerca di Omega*, Adelphi Edizioni

Imparare a programmare non significa memorizzare comandi a memoria: significa sviluppare un **metodo di lavoro mentale**.

Questa guida raccoglie due strumenti metodologici complementari pensati per accompagnarti lungo tutto il corso:

1. **La visione d'insieme:** come studiare e assimilare i contenuti di ogni capitolo (metodo di lettura tecnica).
2. **Il lavoro pratico:** come affrontare ogni singolo programma ed esercizio di codice (metodo PRIMM).

---

### 🎯 Obiettivo

Alla fine della guida sai pianificare lo studio di un capitolo e affrontare un
programma seguendo il ciclo PRIMM.

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

#### Prima del Predict: orientati

- Leggi la teoria che presenta parole, struttura e regole indispensabili.
- Non cercare ancora la risposta del quiz: prepara soltanto gli strumenti per ragionare sul codice.

#### 1. PREDICT (Prevedi)

- Prima di eseguire il programma, esamina attentamente il codice sorgente e **ipotizza cosa farà**.
- Se il codice contiene condizioni, cicli o variabili che cambiano, costruisci sul quaderno una **tabella di traccia** (colonne con i valori assunti dalle variabili passo dopo passo).

#### 2. RUN (Esegui)

- Copia il programma nel tuo ambiente di sviluppo (VS Code o un IDE online).
- **Attenzione:** **non fare copia e incolla!** Digitare il codice parola per parola è indispensabile per memorizzare la sintassi e accorgersi dei dettagli.
- Esegui il programma e confronta l'output ottenuto con la previsione che avevi fatto al passo 1.

#### 3. INVESTIGATE (Investiga)

- Quando il programma usa variabili o memoria, copialo su [Python Tutor (C++ Visualizer)](https://pythontutor.com/cpp.html) ed eseguilo **passo dopo passo**.
- Osserva come evolve lo stato della memoria e confrontalo con la tabella di traccia.

#### 4. MODIFY (Modifica)

- Modifica il codice sorgente procedendo a piccoli passi, per fare tuo il programma:
  - *Esempio 1:* se il programma usa valori prefissati (hardcoded), modificalo per chiedere i dati all'utente tramite istruzioni di input (`std::cin`).
  - *Esempio 2:* se usa numeri interi (`int`), prova a convertirli in numeri a virgola mobile (`double`) o viceversa, osservando come cambia il comportamento della divisione.
- Più modifichi il codice con cognizione di causa, più ne diventi padrone.

#### 5. MAKE (Crea)

- Scrivi un **nuovo programma autonomo** partendo da zero.
- Puoi prendere in prestito frammenti o strutture logiche dal programma appena studiato, applicandoli per risolvere un problema diverso o per realizzare una funzione nuova.
- Questo è il momento in cui passi da "lettore di codice" a "creatore di software".

---

### 📝 Riepilogo tascabile

- Prima leggi il contesto, l'obiettivo e la teoria: poi fai una previsione.
- Digita il codice a mano, senza *copia-e-incolla*, e confronta sempre output e Predict.
- Usa una tabella di traccia e [Python Tutor](https://pythontutor.com/cpp.html#mode=edit) quando cambiano variabili o memoria.
- Modifica poco alla volta; nel Make riusa l'idea in uno scenario nuovo.

---

### ➡️ Da dove si comincia

Prima di scrivere programmi, allestiamo l’**officina**: editor, compilatore e debugger.  
È una sessione di laboratorio, non una lettura di 20 minuti: senza utensili collaudati il resto del corso non parte.
