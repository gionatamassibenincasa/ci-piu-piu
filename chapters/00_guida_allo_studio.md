## 🧭 Guida allo Studio: Come Imparare a Programmare

> Il calcolatore era (ed è ancora) un nuovo e meraviglioso concetto filosofico
> e matematico. […] si capisce qualcosa solo se si è capaci — noi, non altri! —
> di scriverne il programma. Altrimenti non si ha una vera comprensione,
> si crede soltanto di capire.
>
> — *Gregory Chaitin, Alla ricerca di Omega*

Imparare a programmare non è memorizzare comandi: è costruire un **metodo di lavoro mentale**.  
Questa guida ti dà tre bussole per tutto il corso.

---

### 🎯 Cosa trovi in questo corso

| Blocco | Contenuti principali | Capitoli (indicativi) |
|--------|----------------------|------------------------|
| **1 — Il linguaggio** | Ambiente, compilazione, I/O, variabili, espressioni, selezione, cicli | 1–13 |
| **2 — Modularità e dati** | Funzioni, array, struct, algoritmi di base, progetto gestionale | 14–24 |
| **3 — OOP e template** | Classi, incapsulamento, cenni a ereditarietà e template | (in costruzione) |

Ogni capitolo è pensato come **chunk** da 15–25 minuti (a volte una sessione di laboratorio più lunga, come l’installazione dell’ambiente).

---

### 📖 Come leggere un capitolo tecnico (5 passi)

Adattamento per la classe del saggio di Sebastian Raschka [*How to Read Technical Books*](https://sebastianraschka.com/blog/2025/reading-books.html).

1. **Prima lettura (panoramica, ~15–20 min)**  
   Leggi dall’inizio alla fine **senza scrivere codice**. Cerca il quadro generale. Annota solo i punti confusi.

2. **Seconda lettura (con le mani sulla tastiera)**  
   Rileggi e **digita** gli esempi. Niente copia-incolla nella fase di studio: digitare costringe a notare ogni simbolo.

3. **Esegui e osserva**  
   Compila, lancia, confronta l’output con ciò che ti aspettavi. Se qualcosa non torna, **non andare avanti**: ferma e investiga.

4. **Modifica con uno scopo**  
   Cambia *una cosa alla volta* (un numero, una condizione, un messaggio) e prevedi l’effetto prima di rieseguire.

5. **Crea**  
   Affronta il Make del capitolo da zero. È il momento in cui passi da lettore a autore.

---

### 🔬 Il metodo PRIMM (per ogni laboratorio di codice)

| Fase | Cosa fai tu | Perché serve |
|------|-------------|--------------|
| **P**redict | Prima di eseguire, *indovina* cosa succederà | Attiva il modello mentale |
| **R**un | Esegui (terminale, VS Code o blocco `@LIA.cpp`) | Confronto con la realtà |
| **I**nvestigate | Spiega *perché* è successo così (tabella, Python Tutor, messaggio del compilatore) | Collega sintassi e significato |
| **M**odify | Cambia il codice in modo guidato | Consolida senza partire da zero |
| **M**ake | Scrivi un programma nuovo sul tema | Trasferimento autonomo |

Nei capitoli trovi queste fasi già strutturate. Usale anche quando studi da solo.

---

### 🧩 Come sono fatti i capitoli

- **Un solo obiettivo** osservabile per chunk  
- **Metafora** concreta (officina, locker, tornello, cassa…)  
- **Scenario SIA** (magazzino, POS, conto corrente, caveau…)  
- **Quiz** interattivi LiaScript  
- **Riepilogo tascabile** e ponte al capitolo successivo  

Regole di scrittura del codice (le rispetterai nei Make):
- Documentazione **Doxygen** proporzionata (vedi capitolo 4)
- Commenti `///` sul **perché**, non sul cosa ovvio
- Niente programmi monolitici inutilmente lunghi

---

### 🛠️ Strumenti che userai

- **VS Code + MinGW-w64 (MSYS2)** — officina locale (capitolo 1)
- **Terminale** — compilazione e primi controlli
- **Python Tutor (C++)** — ispezione di memoria e stack nelle fasi Investigate
- **LiaScript** — questa pagina interattiva (quiz, codice eseguibile)

---

### ⚠️ Errori e mentalità

Gli errori di compilazione non sono “fallimenti”: sono **messaggi precisi** della fabbrica.  
Imparare a leggerli è una competenza del corso, al pari della sintassi.

Se resti bloccato:
1. Rileggi l’obiettivo del chunk  
2. Rifai la fase Investigate sull’ultimo esempio che funzionava  
3. Chiedi in classe portando il messaggio di errore completo  

---

### ➡️ Prossimo passo

Allestisci l’officina: installazione di VS Code, estensione C/C++, MSYS2 e MinGW-w64.  
Poi apriremo il cofano e vedremo come il sorgente diventa un eseguibile.

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Allineata a chunking, PRIMM, Head First
  [x] Mappa a tre blocchi e numerazione aggiornata (1–13 / 14–24)
  [x] Riferimento esplicito a Doxygen (cap. 4) e a Python Tutor
  [x] Tono conversazionale, senza sovraccarico
-->
