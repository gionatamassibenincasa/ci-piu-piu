# Stile Head First (Brain-Friendly) — Regole operative

I libri della serie *Head First* (O’Reilly) si basano su principi di scienze cognitive.  
In Ci Più Più li adattiamo a lezioni segmentate di C++ per studenti di 3ª SIA.

## Principi chiave da rispettare

### 1. Metafore obbligatorie e concrete
Ogni concetto astratto **deve** avere un’analogia esplicita, preferibilmente dal mondo economico-aziendale o dalla vita quotidiana degli studenti.

Esempi consolidati nel progetto:
| Concetto C++          | Metafora consigliata                          |
|-----------------------|-----------------------------------------------|
| Variabile             | Scatola etichettata nel magazzino della memoria |
| `if` / `if-else`      | Tornello / lettore badge aziendale            |
| Ciclo `while`/`for`   | Catena di montaggio o ciclo di elaborazione ordini |
| Funzione              | Ufficio/reparto specializzato (scatola nera)  |
| Array                 | Scaffale di magazzino con posizioni numerate  |
| `struct` / `class`    | Scheda anagrafica cliente / stampino per biscotti |
| Puntatore             | Indirizzo / mappa del tesoro / riferimento a un cassetto |

La metafora va messa in un box `> 💡 **Metafora:**` e deve spiegare *cosa corrisponde a cosa*.

### 2. Tono conversazionale e personalizzato
- Usa **“tu”** e **“il tuo programma”**.
- Scrivi come se stessi parlando allo studente, non come un manuale.
- Frasi corte. Domande retoriche. “Immagina che…”, “Cosa succederebbe se…”.
- Evita il tono da “manuale di riferimento” o da paper accademico.

### 3. Visuale > testo denso
- Preferisci tabelle, diagrammi plantUML, elenchi puntati.
- Una tabella di traccia vale più di tre paragrafi.
- Usa emoji in modo misurato come ancore visive (🔬 💡 📝 ➡️ ⚠️).

### 4. “Superficiale ma preciso”
- Non entrare nei dettagli oscuri dello standard C++.
- Usa però la **terminologia corretta**:
  - Sbagliato: “il programma si rompe”
  - Giusto: “il compilatore segnala un errore di sintassi”
- Spiega solo ciò che serve allo studente in quel momento.

### 5. Storie e scenari aziendali
Ogni laboratorio PRIMM e ogni esercizio Make devono essere ambientati in un contesto realistico di Economia Aziendale:
- gestione magazzino / scorte
- terminali POS / pagamenti
- anagrafica clienti / ordini
- calcolo IVA / sconti / fatture
- controllo accessi / badge
- reportistica semplice

Lo studente deve sentire che sta costruendo strumenti utili, non esercizi astratti.

### 6. Gestione dell’attenzione e della memoria
- Un solo concetto principale per chunk (vedi `docs/chunking.md`).
- Riepilogo tascabile alla fine (3-6 punti memorabili).
- Ripeti i punti chiave in forme diverse (metafora → codice → tabella → riepilogo).

### 7. Errori come leva didattica
Quando mostri codice errato:
1. Mostra il codice sbagliato.
2. Mostra (o fai prevedere) il messaggio del compilatore.
3. Spiega come leggerlo.
4. Mostra la correzione.

Non nascondere gli errori; usali.

## Cosa evitare (anti-pattern Head First)
- Paragrafi lunghi senza interruzioni visive.
- Definizioni formali senza metafora precedente.
- Esempi puramente numerici o “Hello World” ripetuti dopo il secondo capitolo.
- Tono impersonale (“Si dichiara una variabile…”).
- Introduzione di più di un costrutto nuovo nello stesso chunk.
- Soluzioni complete a vista senza scaffold precedente.

## Checklist stile prima di pubblicare un capitolo
- [ ] Metafora presente e collegata chiaramente al concetto
- [ ] Tono “tu” e conversazionale
- [ ] Almeno una tabella o un diagramma
- [ ] Scenario aziendale nel laboratorio o nel Make
- [ ] Nessun gergo non definito
- [ ] Riepilogo tascabile presente
- [ ] Errori di compilazione (se mostrati) sono spiegati
