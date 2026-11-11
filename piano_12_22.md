# 📋 Piano Didattico Blocco 2: Modularità, Strutture Dati e Algoritmi
**Corso:** Ci Più Più — C++ per la classe 3ª SIA (Sistemi Informativi Aziendali)  
**Approccio:** Micro-Chunking a granularità fine (lezioni da 20-25 min) con casi studio economico-gestionali, metodo PRIMM rigoroso, metafore cognitive "Head First" e approccio **unplugged** per gli algoritmi.

---

## 🎯 Obiettivi Pedagogici del Blocco
- Superare il paradigma del programma monolitico nel `main`: comprendere la programmazione come scomposizione in **moduli cooperativi e specializzati (sviluppo top-down)**.
- Introdurre le **collezioni di dati omogenee (Array)** tramite la tecnica del *Productive Failure* (creare il bisogno cognitivo prima della sintassi).
- Padroneggiare la gestione della memoria in modo visivo:
  - Stack frame delle funzioni (chiamata, passaggio parametri e ritorno).
  - Meccanismo di copia (valore) vs accesso diretto (riferimento `&`).
  - L'indirizzo di memoria come informazione manipolabile (puntatori `*` e `nullptr`).
- Raggruppare entità aziendali eterogenee tramite **enumerazioni (`enum class`)** e **strutture (`struct`)**.
- Comprendere l'**efficienza computazionale** attraverso metafore concrete e confronti numerici diretti (senza notazione matematica formale).
- Culmine pratico: realizzare un **database gestionale in memoria** combinando array di strutture, funzioni e algoritmi di ricerca/ordinamento.

---

## 🗺️ Mappa Dettagliata dei Capitoli (12 - 23)

### 🏢 Capitolo 12: `chapters/12_funzioni_scomposizione_top_down.md`
**Titolo:** *I Reparti dell'Azienda: Sviluppo Top-Down e la Funzione come Scatola Nera*  
**Durata stimata:** 20 minuti

- **La Metafora Guida:** L'**Ufficio Amministrativo Specializzato** (il dirigente non controlla come lavora l'impiegato; gli consegna i dati di input sulla scrivania (**parametri formali**) e attende il documento finale timbrato (**valore di ritorno**)).
- **Concetti teorici:**
  - Il principio della scomposizione top-down (*Divide et Impera* architetturale).
  - La funzione come **scatola nera**: separazione tra interfaccia pubblica e implementazione interna.
  - Distinzione fondamentale: **Parametro Formale** (il segnaposto nella firma) vs **Argomento Reale** (il valore effettivo passato alla chiamata).
  - Prototipo (dichiarazione preventiva) vs Definizione (codice effettivo).
  - L'istruzione `return`: restituzione del valore e terminazione immediata della funzione.
  - Funzioni `void` (procedure che compiono azioni senza restituire un dato).
- **Esempio Applicativo SIA (Caso Studio):**
  - *Il Modulo Paghe Aziendale:* Scomposizione del calcolo busta paga in funzioni indipendenti:
    - `double calcolaLordo(double oreLavorate, double tariffaOraria);`
    - `double calcolaRitenuteFiscali(double importoLordo);`
    - `void stampaCedolino(std::string dipendente, double lordo, double netto);`
- **Laboratorio & PRIMM:**
  - *Predict:* Cosa accade se una funzione ha istruzioni dopo la riga del `return`? (Codice irraggiungibile).
  - *Investigate (PythonTutor):* Visualizzare lo **Stack Frame**: come la chiamata mette "in pausa" il `main`, alloca un nuovo frame isolato per la funzione e lo distrugge al `return`.
  - *Modify:* Creare una funzione `applicaBonus(double stipendio, double bonus)` e comporla con il calcolo del netto.
  - *Make:* Progettare una funzione `calcolaRataMutuo` con documentazione Doxygen completa.

---

### 📎 Capitolo 13: `chapters/13_scope_e_passaggio_parametri.md`
**Titolo:** *La Fotocopia vs L'Originale: Scope e Passaggio per Riferimento (`&`)*  
**Durata stimata:** 20 minuti

- **La Metafora Guida:**
  - *Passaggio per Valore:* Ti consegno una **fotocopia** del listino prezzi: se ci scrivi sopra, la fattura originale nel cassetto non cambia.
  - *Passaggio per Riferimento (`&`):* Ti consegno la **chiave dello sportello originale del Locker**: qualsiasi cifra modifichi, stai alterando la merce reale!
- **Concetti teorici:**
  - **Passaggio per Valore (default):** clonazione del dato in memoria (sicuro per tipi primitivi, ma non modifica l'originale).
  - **Passaggio per Riferimento (`tipo& nome`):** creazione di un alias per lavorare direttamente sulla cella di memoria originale.
  - Riferimenti costanti (`const tipo&`): il meglio dei due mondi per dati pesanti (zero copie, massima velocità, garanzia di sola lettura).
  - Scope locale vs Variabili globali: perché le variabili globali sono una cattiva pratica che causa "effetti collaterali" imprevedibili.
- **Esempio Applicativo SIA (Caso Studio):**
  - *Aggiornamento Listino e Scambio:*
    - Funzione `void applicaScontoPromozionale(double& prezzo, double percentuale);` che modifica sul posto il prezzo a catalogo.
    - Funzione classica di scambio: `void scambiaPrezzi(double& p1, double& p2);`.
- **Laboratorio & PRIMM:**
  - *Predict:* Data una funzione senza `&` che raddoppia una variabile, quanto vale la variabile nel `main` dopo la chiamata?
  - *Investigate (PythonTutor):* **Momento clou:** visualizzare su Python Tutor due etichette distinte che puntano alla *stessa identica cella di memoria* nello stack frame chiamante.
  - *Modify:* Convertire una funzione da passaggio per valore a passaggio per riferimento e osservare l'effetto persistente.
  - *Make:* Funzione `void aggiornaGiacenza(int& scorte, int pezziVenduti, bool& sottoscorta)` che aggiorna le scorte e attiva il flag di allarme.

---

### 🗄️ Capitolo 14: `chapters/14_array_sequenze_dati.md`
**Titolo:** *La Batteria di Locker: Gli Array e le Sequenze di Dati*  
**Durata stimata:** 25 minuti

- **Tecnica Didattica (Productive Failure):** *"L'azienda deve registrare le vendite di 30 giorni e trovare la media e il giorno di picco: prova a farlo dichiarando 30 variabili distinte `g1`, `g2`, ..., `g30`!"*. Emerge la necessità insostituibile dell'array.
- **La Metafora Guida:** Una **fila orizzontale di sportelli Locker identici** posti uno accanto all'altro sullo stesso ripiano del magazzino (celle contigue di memoria dello stesso tipo), numerati partendo rigorosamente dallo sportello `[0]`.
- **Concetti teorici:**
  - Definizione e allocazione: `tipo nome[DIMENSIONE];`.
  - Accesso agli elementi tramite indice numerico intero: `vendite[i]`.
  - Inizializzazione con lista a graffe `{}` e deduzione automatica della dimensione.
  - La trappola dell'indice fuori dai limiti (*Out of Bounds* / Buffer Overflow): perché in C++ non c'è controllo automatico dell'indice e come prevenirlo.
  - **Box Obbligatorio "⚠️ Nota dal Mondo Reale (Array Grezzi vs std::vector)":**
    - Chiarire esplicitamente agli studenti che impariamo gli array grezzi (`tipo arr[N]`) per comprendere come funziona la memoria fisica contigua e i puntatori sotto il cofano, ma che nello sviluppo software aziendale moderno si usa quasi sempre `std::vector` (oggetto del Blocco 3) per sicurezza, gestione dinamica della dimensione ed eliminazione dei rischi di overflow.
  - **Algoritmi Fondamentali con ciclo `for`:**
    - Caricamento e visualizzazione tabellare dell'array.
    - Calcolo della somma totale (accumulatore) e della media aritmetica.
    - Algoritmo del "Re della Collina" per trovare il valore **Massimo** e **Minimo** e la relativa posizione (indice).
- **Esempio Applicativo SIA (Caso Studio):**
  - *Monitoraggio Vendite Mensili:* Array di 30 giorni di incassi: totale fatturato del mese, media giornaliera, giorno record di incasso e giorno peggiore.
- **Laboratorio & PRIMM:**
  - *Predict:* Cosa stampa `vendite[30]` se l'array è dichiarato con dimensione 30? (Errore di indice: l'ultimo è `[29]`).
  - *Investigate (PythonTutor):* Visualizzare l'array come un unico grande blocco rettangolare suddiviso in celle contigue nello stack.
  - *Modify:* Aggiungere il conteggio dei giorni in cui l'incasso ha superato una soglia prefissata (es. > 1.000€).
  - *Make:* Programma `controllo_qualita.cpp` che registra le misure di 20 pezzi industriali, calcola lo scarto rispetto allo standard e individua i pezzi difettosi.

---

### 📊 Capitolo 15: `chapters/15_array_bidimensionali_matrici.md`
**Titolo:** *Il Setaccio e la Griglia: Ricerca Lineare e Matrici Contabili*  
**Durata stimata:** 25 minuti

- **La Metafora Guida:** Il **Foglio di Calcolo Excel** aziendale: ogni dato ha una doppia coordinata, riga (es. Reparto) e colonna (es. Mese dell'anno).
- **Concetti teorici:**
  - **L'Algoritmo di Ricerca Lineare (Scansione Sequenziale):**
    - Scorrere l'array con un ciclo `for` e una sentinella booleana `bool trovato = false;`.
    - Restituire l'indice della prima occorrenza o `-1` se il dato è assente.
  - **Array Bidimensionali (Matrici):**
    - Dichiarazione: `tipo tabella[RIGHE][COLONNE];`.
    - Inizializzazione a blocchi nidificati `{{...}, {...}}`.
    - Scansione a doppio ciclo `for` annidato (il ciclo esterno governa le righe, il ciclo interno le colonne).
    - Somme parziali per riga (es. totale annuale per singolo reparto) e per colonna (es. totale mensile di tutta l'azienda).
- **Esempio Applicativo SIA (Caso Studio):**
  - *Il Prospetto di Bilancio Reparti:* Matrice 4×12 che memorizza i ricavi dei 4 reparti dell'azienda (Hardware, Software, Servizi, Consulenza) nei 12 mesi dell'esercizio. Stampa della griglia contabile formattata con `<iomanip>`.
- **Laboratorio & PRIMM:**
  - *Predict:* In quale ordine vengono stampati gli elementi di una matrice 2×3 invertendo i due cicli `for`?
  - *Investigate (PythonTutor):* Osservare come la matrice viene linearizzata in memoria come sequenza continua di righe.
  - *Modify:* Calcolare la media annuale del reparto che ha ottenuto il fatturato più elevato.
  - *Make:* Gestione della griglia presenze dipendenti (giorni × ore di straordinario).

---

### 🗝️ Capitolo 16: `chapters/16_puntatori_e_memoria.md`
**Titolo:** *Il Biglietto di Ritiro: Indirizzi di Memoria, Operatori & e * e Puntatori*  
**Durata stimata:** 20 minuti

- **La Metafora Guida:** Riconnessione perfetta con il **Locker di e-commerce** (introdotto nel Cap. 03):
  - L'operatore **`&`** (indirizzo): *"Qual è il numero di metallo stampato sullo sportello della variabile `prezzo`?"*.
  - Il **Puntatore (`double* ptr`)**: uno sportello speciale che, anziché merce, contiene un **biglietto con il numero di un altro sportello**.
  - L'operatore **`*`** (dereferenziazione): *"Segui il biglietto, vai allo sportello indicato e preleva/modifica la merce"*.
  - Il valore `nullptr`: il biglietto è in bianco (non punta a nessuno sportello).
- **Concetti teorici:**
  - Perché i puntatori? Comprendere come il computer organizza la memoria fisica e come passare dati complessi a costo zero.
  - Dichiarazione: `int* p;` e inizializzazione obbligatoria a `nullptr` o a un indirizzo valido (`&variabile`).
  - Distinzione cruciale tra il *valore del puntatore* (l'indirizzo esadecimale `0x7ffee...`) e il *valore puntato* (`*ptr`).
  - Controllo di sicurezza prima dell'accesso: `if (ptr != nullptr) { ... }`.
  - Passaggio di array alle funzioni: perché un array "decade" naturalmente in un puntatore al suo primo elemento.
- **Esempio Applicativo SIA (Caso Studio):**
  - *Gestione Fido Bancario tramite Riferimento e Puntatore:* Funzione di aggiornamento del credito con verifica preventiva di puntatore valido.
- **Laboratorio & PRIMM:**
  - *Predict:* Dati `int a = 10; int* p = &a; *p = 20;`, quanto vale `a`?
  - *Investigate (PythonTutor):* Osservare le frecce grafiche che collegano la variabile puntatore alla variabile bersaglio.
  - *Modify:* Creare una funzione `void trovaEstremo(const double arr[], int n, double* ptrMax)` che restituisce tramite puntatore il valore massimo.
  - *Make:* Sistema di cambio valuta che manipola importi esteri tramite puntatori a dati.

---

### 🏷️ Capitolo 17: `chapters/17_enum_e_struct.md`
**Titolo:** *L'Anagrafica Aziendale: Enumerazioni (`enum class`) e Strutture (`struct`)*  
**Durata stimata:** 25 minuti

- **La Metafora Guida:**
  - `enum class`: Il **timbro ufficiale dello stato pratica** dell'ufficio protocollo (non puoi inventare stati a caso: o è *In Lavorazione*, o è *Spedito*, o è *Archiviato*).
  - `struct`: La **cartella anagrafica / scatola regalo multi-scomparto**: un unico contenitore che raggruppa oggetti di natura diversa (un testo, due numeri, una data e uno stato).
- **Concetti teorici:**
  - **`enum class` (Scoped Enumerations):** definire tipi personalizzati a valori discreti nominali per eliminare i "numeri magici" dal codice aziendale.
  - **`struct Nome { ... };`:** creare nuovi tipi di dato compositi aggregando variabili eterogenee (i "campi" o "attributi").
  - L'operatore punto `.` per accedere ai singoli campi di una variabile struct.
  - L'operatore freccia `->` per accedere ai campi partendo da un puntatore a struct (`ptr->prezzo` equivalente a `(*ptr).prezzo`).
  - **Regola di Efficienza:** passare sempre le struct alle funzioni per **riferimento costante (`const Struct& s`)** per evitare fotocopie inutili di memoria.
- **Esempio Applicativo SIA (Caso Studio):**
  - *L'Entità Ordine Cliente:*
    ```cpp
    enum class StatoOrdine { InAttesa, Confermato, Spedito, Annullato };
    struct Ordine {
        int idOrdine;
        std::string cliente;
        double importoTotale;
        StatoOrdine stato;
    };
    ```
- **Laboratorio & PRIMM:**
  - *Predict:* Se assegno `Ordine o2 = o1;`, cosa accade alla memoria? (Copia campo per campo).
  - *Investigate (PythonTutor):* Visualizzare la `struct` come una scatola suddivisa internamente in scomparti etichettati, ciascuno con il proprio tipo.
  - *Modify:* Scrivere la funzione `void stampaSchedaOrdine(const Ordine& ord)` con formattazione `<iomanip>`.
  - *Make:* Definire la `struct Dipendente` (matricola, cognome, stipendio base, reparto) e calcolare lo stipendio netto tramite apposita funzione.

---

### 🔍 Capitolo 18: `chapters/18_ricerca_dicotomica.md` *(Opzionale)*
**Titolo:** *Il Dizionario Magico: La Ricerca Dicotomica (Binaria)*  
**Durata stimata:** 20 minuti

- **La Metafora Guida (Unplugged):**
  - *Ricerca Lineare:* Immagina di cercare il numero di telefono di "Mario Rossi" in un elenco telefonico di 1.000 pagine, leggendo una pagina alla volta dal principio. Potresti impiegare fino a 1.000 tentativi!
  - *Ricerca Dicotomica:* Apri il dizionario a metà. Vedi che la lettera "M" è dopo? Butti via la prima metà. Apri di nuovo a metà della parte restante. Vedi che "Rossi" è prima di "Russo"? Butti via la seconda metà. In pochi passi hai trovato la pagina esatta!
- **Concetti teorici (senza notazione matematica):**
  - **Prerequisito assoluto:** l'array deve essere **ordinato**!
  - L'algoritmo degli indici `inizio`, `fine`, `medio`: ad ogni passo dimezzi lo spazio di ricerca.
  - **Tabella comparativa concreta:**
    | Numero di dati | Ricerca Lineare (passi max) | Ricerca Dicotomica (passi max) |
    | :--- | :--- | :--- |
    | 100 | 100 | 7 |
    | 1.000 | 1.000 | 10 |
    | 1.000.000 | 1.000.000 | 20 |
    | 1.000.000.000 | 1.000.000.000 | 30 |
  - **Domanda chiave:** "Se raddoppio i dati, quanti passi in più servono?" → Lineare: il doppio. Dicotomica: appena 1 in più!
- **Esempio Applicativo SIA (Caso Studio):**
  - *Ricerca istantanea del prezzo di un articolo al passaggio della cassa ottica:* il catalogo codici a barre è ordinato, quindi la ricerca è immediata anche su milioni di prodotti.
- **Laboratorio & PRIMM:**
  - *Predict:* Se l'array ha 1.024 elementi ordinati, quanti passi al massimo servono per trovare un valore (o stabilire che non c'è)? (Risposta: 10, perché 2¹⁰ = 1024).
  - *Investigate (PythonTutor):* Visualizzare lo scorrimento degli indici `inizio` e `fine` che convergono verso il dato cercato.
  - *Modify:* Modificare la funzione per restituire `-1` se il valore non è presente, invece di andare in loop.
  - *Make:* Implementare la funzione completa `int ricercaBinaria(const double arr[], int n, double target)`.

---

### 🃏 Capitolo 19: `chapters/19_ordinamento_selection_sort.md` *(Opzionale)*
**Titolo:** *Riordinare le Carte: L'Algoritmo Selection Sort*  
**Durata stimata:** 20 minuti

- **La Metafora Guida (Unplugged):**
  - Immagina di avere un mazzo di carte da gioco sparso sul tavolo e vuoi ordinarle dal valore più basso al più alto.
  - **Strategia Selection Sort:** Guardi tutte le carte, trovi quella con il valore più basso, e la metti in prima posizione. Poi guardi le carte restanti, trovi la seconda più bassa, e la metti in seconda posizione. Ripeti fino a finire.
  - È un metodo semplice e intuitivo, ma **lento** se le carte sono tante: per 100 carte devi fare circa 5.000 confronti!
- **Concetti teorici (senza notazione matematica):**
  - L'algoritmo in 3 passi:
    1. Cerca il minimo nella parte non ordinata dell'array.
    2. Scambialo con il primo elemento della parte non ordinata.
    3. Ripeti per la parte restante.
  - **Tabella comparativa concreta:**
    | Numero di dati | Confronti necessari |
    | :--- | :--- |
    | 10 | 45 |
    | 100 | 4.950 |
    | 1.000 | 499.500 |
    | 10.000 | 49.995.000 |
  - **Domanda chiave:** "Se raddoppio i dati, quanti confronti in più servono?" → Circa 4 volte tanto! (Crescita quadratica).
- **Esempio Applicativo SIA (Caso Studio):**
  - *Ordinamento del listino prezzi per importo crescente:* utile per visualizzare i prodotti dal più economico al più costoso.
- **Laboratorio & PRIMM:**
  - *Predict:* Se l'array è già ordinato, quanti confronti fa comunque il Selection Sort? (Risposta: sempre gli stessi, non "si accorge" che è già ordinato).
  - *Investigate (PythonTutor):* Visualizzare lo scorrimento degli indici e gli scambi di posizione.
  - *Modify:* Modificare l'algoritmo per ordinare in ordine **decrescente** (trovare il massimo invece del minimo).
  - *Make:* Implementare la funzione completa `void selectionSort(double arr[], int n)`.

---

### 🧩 Capitolo 20: `chapters/20_ordinamento_divide_et_impera.md` *(Opzionale)*
**Titolo:** *Divide et Impera: Merge Sort e Quick Sort*  
**Durata stimata:** 25 minuti

- **La Metafora Guida (Unplugged):**
  - *Merge Sort:* Immagina di dover ordinare un mazzo di 100 carte. Invece di affrontarle tutte insieme, le dividi a metà (50 e 50), poi dividi ancora (25, 25, 25, 25), fino ad arrivare a mazzetti di 1 carta (già ordinati!). Poi **fondi** (merge) i mazzetti a due a due, mantenendo l'ordine, fino a ricostruire il mazzo completo ordinato.
  - *Quick Sort:* Scegli una carta "pivot" (es. il 7). Metti tutte le carte minori di 7 a sinistra, tutte le maggiori a destra. Poi applica la stessa strategia ricorsivamente ai due gruppi.
- **Concetti teorici (senza notazione matematica):**
  - **Merge Sort:**
    - Strategia: Dividi a metà, ordina ricorsivamente le due metà, fondi (merge) i due array ordinati.
    - **Tabella comparativa:**
      | Numero di dati | Confronti necessari |
      | :--- | :--- |
      | 10 | ~30 |
      | 100 | ~700 |
      | 1.000 | ~10.000 |
      | 1.000.000 | ~20.000.000 |
    - **Confronto con Selection Sort:** Per 1.000 dati, Selection Sort fa 500.000 confronti, Merge Sort ne fa 10.000. **50 volte più veloce!**
  - **Quick Sort:**
    - Strategia: Scegli un pivot, partiziona l'array in due sottogruppi (minori e maggiori del pivot), ordina ricorsivamente i sottogruppi.
    - Nel caso medio è velocissimo, ma nel caso peggiore (pivot sfortunato) può rallentare.
  - **Diagramma PlantUML:** Visualizzazione del processo di divisione e fusione del Merge Sort.
- **Esempio Applicativo SIA (Caso Studio):**
  - *Ordinamento di grandi archivi aziendali:* quando il catalogo prodotti supera i 10.000 articoli, gli algoritmi "naive" come Selection Sort diventano troppo lenti. Serve un approccio industriale.
- **Laboratorio & PRIMM:**
  - *Predict:* Se raddoppio i dati da 1.000 a 2.000, quanti confronti in più fa il Merge Sort? (Risposta: circa il doppio, non 4 volte tanto come Selection Sort).
  - *Investigate (PythonTutor):* Visualizzare la ricorsione e la fusione dei sotto-array.
  - *Modify:* Implementare la funzione `void merge(double arr[], int inizio, int meta, int fine)` che fonde due sotto-array ordinati.
  - *Make:* Implementare la funzione completa `void mergeSort(double arr[], int inizio, int fine)`.

---

### 🏆 Capitolo 21: `chapters/21_database_in_memoria_progetto.md`
**Titolo:** *Il Database Gestionale: Vettori di Strutture e Progetto Finale del Blocco 2*  
**Durata stimata:** 25 minuti

- **Il Traguardo Didattico:** L'unione organica di tutte le competenze acquisite nel Blocco 1 e nel Blocco 2: **l'Array di Struct (`Prodotto catalogo[50];`)** coordinato da funzioni modulari. È il modello in memoria di una vera tabella di un database aziendale!
- **Concetti teorici:**
  - Array di strutture: ogni riga dell'array è un record completo.
  - Architettura del software gestionale a moduli:
    - Funzione di caricamento e popolamento dati.
    - Funzione di visualizzazione con tabella contabile `<iomanip>`.
    - Funzione di ordinamento dell'archivio per campo chiave (es. per codice o per prezzo).
    - Funzione di ricerca rapida con ricerca dicotomica sul vettore ordinato.
  - *Cenno teorico di fine blocco:* I limiti della dimensione fissa dell'array e introduzione concettuale alle strutture dati dinamiche (liste collegate o `std::vector`), aprendo la porta al Blocco 3.
- **Progetto MAKE di Fine Blocco (Simulazione Esame / Progetto Sommativo):**
  - **"L'ERP del Punto Vendita (Mini-Gestionale di Cassa e Magazzino)"**:
    - Gestione di un archivio di 20 articoli di magazzino (`struct Prodotto`).
    - Menu principale (`switch`) con opzioni:
      1. *Stampa Inventario Completo* (tabella allineata con `<iomanip>`).
      2. *Ordinamento Prodotti per Prezzo* (Selection Sort).
      3. *Ricerca Articolo per Codice* (Ricerca Binaria istantanea).
      4. *Vendita Articolo e Aggiornamento Giacenza* (con passaggio per riferimento `&`).
      5. *Calcolo Valore Totale Patrimoniale del Magazzino*.
      0. *Chiusura e Report Fiscale*.
- **Requisiti di qualità:** Rigore formale, documentazione Doxygen completa su tutte le funzioni, zero variabili globali, gestione robusta dell'input.

---

### 🪆 Capitolo 22: `chapters/22_ricorsione_e_strutture_ricorsive.md`
**Titolo:** *Lo Specchio e la Catena: La Ricorsione e le Strutture Ricorsive*  
**Durata stimata:** 25 minuti

- **La Metafora Guida:**
  - *La Matrioska e lo Specchio Riflesso:* Una scatola che contiene al suo interno un'altra scatola simile più piccola, fino a raggiungere quella centrale indivisibile (caso base).
  - *La Distinta Base di Fabbrica (Bill of Materials):* Il responsabile della produzione chiede il costo di un assemblato; ogni semilavorato delega il calcolo ai suoi componenti elementari, e i costi risalgono la catena fino al prodotto finito.
- **Concetti teorici:**
  - **La Funzione Ricorsiva:** una funzione che risolve un problema invocando se stessa su un sottoinsieme ridotto del problema.
  - **I due pilastri obbligatori per evitare lo Stack Overflow:**
    - **Caso Base:** la condizione di arresto immediato (restituisce un valore noto senza fare ulteriori chiamate).
    - **Passo Ricorsivo:** l'invocazione di se stessa con dati che si avvicinano progressivamente al caso base.
  - **Il Record di Attivazione (Call Stack)** e la fase di "srotolamento" (unwinding) del risultato.
  - **La Ricorsione Strutturale (Structural Recursion):**
    - Quando la funzione rispecchia esattamente la forma ricorsiva del dato.
    - **Strutture dati autoreferenziali** (il puntatore alla stessa `struct`):
      ```cpp
      struct NodoComponente {
          std::string descrizione;
          double costo;
          NodoComponente* prossimo; /// Puntatore ricorsivo al componente successivo
      };
      ```
    - **Attraversamento ricorsivo naturale:**
      - Caso base: `testa == nullptr` (catena vuota o terminata, costo 0.0 o conteggio 0).
      - Passo ricorsivo: `testa->costo + calcolaCostoTotale(testa->prossimo)`.
    - **La magia dell'inversione di controllo:** stampare la catena in ordine inverso invertendo la chiamata ricorsiva con la stampa.
- **Esempio Applicativo SIA (Caso Studio):**
  - *La Distinta Base Industriale (BOM):* Calcolo ricorsivo del costo complessivo di una catena di fornitura/produzione e conteggio automatico dei passaggi intermedi.
- **Laboratorio & PRIMM:**
  - *Predict:* Se metto `std::cout << testa->descrizione;` **dopo** la chiamata ricorsiva anziché **prima**, in che ordine vengono stampati i componenti?
  - *Investigate (PythonTutor):* Visualizzare l'impilamento dei frame ricorsivi nello stack (`nodo1`, `nodo2`, `nodo3`) e il calcolo cumulativo che si srotola all'indietro.
  - *Modify:* Scrivere una funzione ricorsiva `int contaComponenti(const NodoComponente* testa)` che calcola quanti elementi compongono la distinta.
  - *Make:* Funzione ricorsiva `bool cercaMateriale(const NodoComponente* testa, std::string nome)` che restituisce `true` se il materiale è presente lungo la catena di nodi.

---

## 📊 Matrice di Copertura Concettuale del Blocco 2

| Concetto Chiave | Capitolo | Caso d'Uso Aziendale / SIA | Opzionale? |
| :--- | :--- | :--- | :--- |
| Scomposizione Top-Down e Scatola Nera | **Cap. 12** | Modulo stipendi: calcolo lordo, detrazioni e netto | No |
| Stack Frame e Record di Attivazione | **Cap. 12** | Visualizzazione Python Tutor del flusso di chiamata | No |
| Passaggio per Valore vs Riferimento (`&`) | **Cap. 13** | Aggiornamento giacenza magazzino e scambio prezzi | No |
| Riferimenti costanti (`const &`) | **Cap. 13** & **Cap. 17** | Lettura sicura ed efficiente di record e stringhe | No |
| Array monodimensionali e Productive Failure | **Cap. 14** | Serie storica vendite dei 30 giorni del mese | No |
| Algoritmi: Accumulatore, Media, Max/Min | **Cap. 14** | Ricerca del giorno con massimo e minimo incasso | No |
| Ricerca Lineare sequenziale | **Cap. 15** | Controllo presenza articolo a listino | No |
| Matrici Bidimensionali (2D) | **Cap. 15** | Griglia bilancio: 4 reparti per 12 mesi dell'anno | No |
| Puntatori: indirizzi `&`, dereferenziazione `*` | **Cap. 16** | Controllo e modifica crediti con puntatori e `nullptr` | No |
| Enumerazioni fortemente tipizzate (`enum class`) | **Cap. 17** | Stati pratica/ordine (InAttesa, Spedito, Annullato) | No |
| Strutture di Dati (`struct`) | **Cap. 17** | Cartella record cliente e ordine multiparametro | No |
| Ricerca Binaria (Dicotomica) | **Cap. 18** | Ricerca istantanea codice su archivio ordinato | **Sì** |
| Ordinamento Naive (Selection Sort) | **Cap. 19** | Ordinamento del listino prezzi per importo crescente | **Sì** |
| Merge Sort e Quick Sort (Divide et Impera) | **Cap. 20** | Algoritmi industriali per grandi archivi | **Sì** |
| Array di Struct (Database in memoria) | **Cap. 21** | Mini-ERP Gestionale: inventario, ricerca e vendite | No |
| Ricorsione e Strutture Ricorsive | **Cap. 22** | Distinta Base aziendale (BOM) e catena di nodi collegati | **Sì** |

