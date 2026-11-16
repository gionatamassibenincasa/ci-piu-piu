# 📋 Piano Didattico Blocco 3: Progettazione Orientata agli Oggetti e Template

**Corso:** Ci Più Più — C++ per la classe 3ª SIA (Sistemi Informativi Aziendali)  
**Prerequisito:** Blocco 1 e Blocco 2 completati (capitoli 0–25: linguaggio, funzioni, array, `struct`/`enum`, algoritmi di base, ricorsione introduttiva).  
**Approccio:** Micro-Chunking (15–25 min nucleo) + PRIMM + metafore Head First + scenari SIA.  
**Numerazione prevista:** capitoli **26–36** (`order` 26–36), file `chapters/25_…` … `chapters/35_…` (allineare nomi file a `order` in fase di scrittura).  
**Durata orientativa del blocco:** 18–24 ore di attività (lezione + lab + Make/Classroom50), compatibile con la terza area del corso (~90 ore totali).

**Riferimento syllabus:** UFC/ITP competenze su classi semplici, incapsulamento, cenni a ereditarietà/polimorfismo, funzioni e classi template; progetto conclusivo orientato agli oggetti.

---

## 🎯 Obiettivi pedagogici del blocco

Alla fine del Blocco 3 lo studente è in grado di:

1. **Passare da `struct` a `class`**: dati privati, interfaccia pubblica, responsabilità di un “reparto-oggetto”.
2. **Costruire oggetti in modo controllato** (costruttori, invarianti semplici, `const` sui metodi di lettura).
3. **Modellare relazioni “ha-un”** (composizione) prima di specializzazioni complesse.
4. **Usare l’ereditarietà e il polimorfismo in forma essenziale** (una gerarchia poco profonda, metodi virtuali dove servono).
5. **Introdurre la programmazione generica**: funzione template; consumo consapevole di un contenitore template (`std::vector`) come *cliente*, non come autore della STL.
6. **Integrare** oggetti + collezioni in un mini-progetto gestionale consegnabile (Classroom50).

### Cosa *non* è obiettivo di questo blocco (3ª SIA)

- Metaprogrammazione avanzata, SFINAE, concetti C++20.
- Gerarchie profonde, ereditarietà multipla, CRTP.
- Smart pointer come tema centrale (cenno opzionale in nota “mondo reale”).
- Scrivere una STL personale.

---

## 🧭 Principi di progettazione didattica

| Principio | Applicazione nel Blocco 3 |
|-----------|---------------------------|
| **Chunking** | Un concetto dominante per capitolo (es. solo costruttore; solo `virtual`) |
| **PRIMM** | Codice *già funzionante* con oggetti; Predict su stato dell’oggetto; Make su scenario SIA diverso |
| **Head First** | Metafore aziendali stabili (reparto, sportello, contratto, listino, conto) |
| **Productive failure** | Prima “struct + funzioni sparse”, poi il bisogno della `class` |
| **Progressione** | Composizione → ereditarietà leggera → template come *riuso di algoritmi/tipi* |
| **Classroom50** | Ogni capitolo PRIMM con `files[].action: create` sul Make; 1 assignment = 1 capitolo |

### Filo metaforico del blocco

> L’azienda non è un unico ufficio (`main`): è un insieme di **reparti-oggetto** con **regole interne** (dati privati), **sportelli pubblici** (metodi), **contratti di creazione** (costruttori) e, quando serve, **ruoli specializzati** (ereditarietà) e **procedure uguali per tipi diversi** (template).

---

## 🗺️ Mappa dei capitoli (26–36)

### Capitolo 26 — `25_da_struct_a_class.md`  
**Titolo:** *Dal cartellino al reparto: `struct` → `class` e incapsulamento*  
**Durata:** ~20–25 min · **methodology:** PRIMM · **order:** 26

- **Metafora:** cartellino anagrafico (`struct` pubblica) vs **reparto con porta chiusa** (`class`: stato interno privato, sportelli pubblici).
- **Concetti:** `class`, `public` / `private`, motivazione dell’incapsulamento (invarianti: prezzo ≥ 0, giacenza ≥ 0).
- **Ponte dal Blocco 2:** stesso dominio `Articolo` già visto come `struct`.
- **PRIMM:** Predict su accesso a membro privato; Run con getter/setter minimi; Make: classe `Articolo` con interfaccia controllata.
- **Classroom50:** `articolo_classe.cpp` (create).

---

### Capitolo 27 — `26_costruttori_e_invarianti.md`  
**Titolo:** *Assunzione in organico: costruttori e oggetto ben formato*  
**Durata:** ~20 min · **PRIMM** · **order:** 27

- **Metafora:** assunzione / apertura posizione: non esiste impiegato “a metà”.
- **Concetti:** costruttore di default (se utile), costruttore con parametri, inizializzazione, perché non lasciare campi “a caso”.
- **PRIMM:** Predict “cosa succede se costruisco senza validare il prezzo”; Make: `ContoCorrente` o `Articolo` che nasce già coerente.
- **Nota:** distruttore solo cenni (“fine rapporto”); niente risorse heap obbligatorie.

---

### Capitolo 28 — `27_metodi_e_responsabilita.md`  
**Titolo:** *Cosa sa fare il reparto: metodi, `this`, responsabilità*  
**Durata:** ~20 min · **PRIMM** · **order:** 28

- **Metafora:** mansioni del reparto (caricare merce, applicare sconto, emettere scheda).
- **Concetti:** metodi di istanza, differenza funzione libera vs metodo, idea di `this` (senza ossessione sintattica).
- **PRIMM:** Make su `MagazzinoArticolo` con `scarica`, `carica`, `scheda`.

---

### Capitolo 29 — `28_const_correttezza_oggetti.md`  
**Titolo:** *Consultare senza modificare: metodi `const`*  
**Durata:** ~15–20 min · **PRIMM** · **order:** 29

- **Metafora:** accesso in **sola lettura** alla pratica (audit).
- **Concetti:** `const` sul metodo, oggetti `const`, perché i getter sono `const`.
- **Collegamento:** formattazione contabile del Blocco 2 per stampare saldi in sola lettura.

---

### Capitolo 30 — `29_composizione_ha_un.md`  
**Titolo:** *L’azienda è fatta di pezzi: composizione (“ha un”)*  
**Durata:** ~20–25 min · **PRIMM** · **order:** 30

- **Metafora:** `Fattura` *ha un* `Cliente` e *ha una* lista di righe (per ora array o pochi oggetti).
- **Concetti:** oggetti membro, costruzione a catena, preferire composizione a ereditarietà forzata.
- **Make:** `Ordine` con cliente + importo / stato (`enum class`).

---

### Capitolo 31 — `30_ereditarieta_essenziale.md`  
**Titolo:** *Specializzazioni in organigramma: ereditarietà essenziale*  
**Durata:** ~20–25 min · **PRIMM** · **order:** 31

- **Metafora:** `Dipendente` generico → `DipendenteFullTime` / `Collaboratore` (o `Movimento` → `Entrata`/`Uscita` se più vicino alla contabilità).
- **Concetti:** classe base, derivata, `public` inheritance, riuso senza copiare attributi comuni.
- **Vincolo chunk:** **una sola** gerarchia a 2 livelli; niente diamanti.
- **Make:** gerarchia minima + stampa polimorfica ancora *senza* `virtual` (o solo override statico se si anticipa il 32).

---

### Capitolo 32 — `31_polimorfismo_virtual.md`  
**Titolo:** *Stesso sportello, comportamenti diversi: `virtual`*  
**Durata:** ~20–25 min · **PRIMM** · **order:** 32

- **Metafora:** sportello unico “calcola compenso” / “calcola totale”; dietro, procedure diverse.
- **Concetti:** puntatore/riferimento alla base, `virtual`, binding dinamico in forma elementare.
- **PRIMM:** Predict sull’output con/senza `virtual`; Investigate con tabella “tipo statico vs dinamico” semplificata.
- **Make:** array (o `vector` se già introdotto al 34–35) di puntatori a base — se `vector` non c’è ancora, array di puntatori a base a dimensione fissa.

---

### Capitolo 33 — `32_overloading_operatori_essenziale.md`  
**Titolo:** *Linguaggio del dominio: overloading essenziale*  
**Durata:** ~15–20 min · **PRIMM** · **order:** 33

- **Metafora:** scrivere `totale = netto + iva` con tipi `Denaro` / `Importo`.
- **Concetti:** overloading di `+` o `+=` **oppure** `<<` per output (sceglierne **uno** come focus del chunk).
- **Vincolo:** non trasformare il capitolo in elenco di tutti gli operatori.

---

### Capitolo 34 — `33_funzioni_template.md`  
**Titolo:** *Stessa procedura, tipi diversi: funzioni template*  
**Durata:** ~20 min · **PRIMM** · **order:** 34

- **Metafora:** modulo “massimo tra due valori” valido per quantità e per prezzi.
- **Concetti:** `template <typename T>`, istanziazione da parte del compilatore, limiti (tipi confrontabili).
- **Ponte:** algoritmi del Blocco 2 (max su array) generici su `T`.
- **Make:** `massimo` / `scambia` template usati su `int` e `double`.

---

### Capitolo 35 — `34_vector_come_cliente.md`  
**Titolo:** *Il magazzino elastico: usare `std::vector` (cliente del template)*  
**Durata:** ~20–25 min · **PRIMM** · **order:** 35

- **Metafora:** scaffale che **cresce** senza dichiarare la capacità a compile-time.
- **Concetti:** `push_back`, `size`, `[]` / `at`, range-`for`; array grezzo vs vector (richiamo nota Blocco 2).
- **Postura:** lo studente è **utente** di una classe template della libreria, non l’autore.
- **Make:** elenco dinamico di movimenti o articoli.

---

### Capitolo 36 — `35_progetto_oop_gestionale.md`  
**Titolo:** *Mini-progetto: gestionale a oggetti in memoria*  
**Durata:** 2–3 sessioni (lab esteso) · **methodology:** `lab` o PRIMM leggero · **order:** 36

- **Metafora:** piccolo sistema informativo aziendale in RAM.
- **Requisiti minimi (rubrica):**
  - almeno **2 classi** con dati privati e interfaccia pubblica;
  - almeno una relazione di **composizione**;
  - uso di **`std::vector`** (o array di oggetti se si vuole tenere il progetto prima del 35 — preferibile dopo 35);
  - output formattato (`iomanip`);
  - documentazione Doxygen sui tipi pubblici.
- **Ereditarietà/polimorfismo:** obbligatori in forma minima **oppure** opzione “plus” in rubrica (adattare alla classe).
- **Consegna:** un solo assignment Classroom50 di progetto (eccezione consapevole alla regola 1 capitolo = 1 assignment: qui il capitolo *è* il progetto).

---

## 📊 Sequenza e dipendenze

```text
26 class/incapsulamento
    → 27 costruttori
        → 28 metodi
            → 29 const
                → 30 composizione
                    → 31 ereditarietà
                        → 32 virtual
                            → 33 operatori (opzionale nello stesso sprint di 31–32)
34 template di funzione ──┐
35 vector come cliente   ┘→ 36 progetto
```

**Possibile compressione** (se il monte ore è stretto):

| Taglio | Effetto |
|--------|---------|
| Unire 28+29 | Un chunk “metodi e const” |
| Saltare 33 | Overloading solo cenno nel progetto |
| Alleggerire 31–32 | Solo composizione + vector nel progetto (OOP “incapsulamento-first”) |

**Sconsigliato:** saltare 26–27 (sono il cuore del passaggio da Blocco 2).

---

## 🏢 Dominio SIA ricorrente (coerenza tra capitoli)

| Concetto OOP | Esempio aziendale ricorrente |
|--------------|------------------------------|
| Classe | `Articolo`, `ContoCorrente`, `Movimento`, `Cliente` |
| Invariante | saldo coerente, giacenza ≥ 0, IBAN non vuoto |
| Composizione | `Ordine` ha `Cliente` e righe |
| Ereditarietà | `Movimento` → `Entrata`/`Uscita` **oppure** tipologie dipendente |
| Template | max/scambio generici; `vector<Movimento>` |
| Progetto | mini-prima nota / magazzino / listino clienti |

Un unico dominio (es. **magazzino + movimenti**) riduce il carico cognitivo tra un capitolo e l’altro.

---

## ⏱️ Stima ore

| Attività | Ore orientative |
|----------|-----------------|
| Capitoli 26–35 (nucleo + lab PRIMM) | 12–16 |
| Progetto 36 | 4–6 |
| Recupero / Classroom50 / verifiche | 2–3 |
| **Totale blocco** | **~18–24** |

---

## ✅ Criteri di accettazione (Definition of Done per ogni capitolo 26–35)

- [ ] Frontmatter valido (`activity_id`, `order`, `methodology`, `files` create se c’è Make)
- [ ] Un solo obiettivo dominante (chunking)
- [ ] Metafora mappata esplicitamente
- [ ] Predict da `components.predict_quiz` + `[[ predict_block() ]]`
- [ ] Run con `@LIA.cpp`
- [ ] Investigate (stato dell’oggetto / tabella / Python Tutor quando c’è memoria)
- [ ] Modify a gradi senza costrutti del capitolo *successivo*
- [ ] Make su scenario SIA + scaffold
- [ ] Riepilogo tascabile + ponte al chunk successivo
- [ ] `cipiupiu validate` ok; template Classroom50 generabile con `scaffold-assignment`

---

## 🛠️ Impatto sul tooling e sul repo

| Elemento | Azione |
|----------|--------|
| `index.md` | Aggiungere `#include` dei nuovi capitoli in coda |
| `order` | Continuare da 26 (dopo `ricorsione-01` = 25) |
| `piano_chunk_14_24.md` | Resta il piano del Blocco 2; questo file è il piano del Blocco 3 |
| Syllabus UFC | Allineato a itp3-6 (classi, template, progetto OOP) |
| Classroom50 | Assignment regolari 26–35; progetto unico al 36 |

---

## 📅 Ordine di implementazione consigliato (scrittura OER)

1. **26–27** (class + costruttore) — sbloccano tutto il resto  
2. **28–30** (metodi, const, composizione) — OOP “quotidiano”  
3. **35** (`vector` cliente) — prima di un progetto serio con collezioni  
4. **34** (funzione template) — può stare subito prima o dopo 35  
5. **31–32** (ereditarietà / virtual) — dopo che composizione è solida  
6. **33** se c’è tempo  
7. **36** progetto con rubrica e assignment dedicato  

---

## 🔗 Collegamento ai blocchi precedenti

| Dal Blocco 2 | Nel Blocco 3 diventa |
|--------------|----------------------|
| `struct` + funzioni | `class` + metodi |
| Parametro `T&` | Metodi che modificano lo stato |
| Array di `struct` | `vector` di oggetti / composizione |
| Doxygen su funzioni | Doxygen su tipi e interfacce pubbliche |
| Make “archivio in RAM” | Progetto OOP gestionale |

---

*Documento operativo per autori e LLM: da aggiornare solo con decisioni di scope (compressione capitoli, dominio unico, obbligatorietà di 31–32).*
