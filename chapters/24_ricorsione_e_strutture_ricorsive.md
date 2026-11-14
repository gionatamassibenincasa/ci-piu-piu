---
activity_id: ricorsione-01
title: Ricorsione e strutture ricorsive
methodology: PRIMM
order: 24
version: '2026-11-15'
language: it
components:
  predict_quiz:
    question: Cosa deve avere ogni funzione ricorsiva corretta?
    code: "int f(int n) {\n  if (n <= 0) return 1; // caso base\n  return n * f(n\
      \ - 1);\n}"
    options:
    - text: Solo chiamate ricorsive, senza mai fermarsi
      correct: false
    - text: Almeno un caso base che interrompe la ricorsione
      correct: true
    - text: Obbligo di usare array globali
      correct: false
---



## 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Descrivere i concetti di caso base e passo ricorsivo.
- Implementare funzioni ricorsive semplici in C++.
- Utilizzare strutture dati ricorsive (es. liste collegate) per rappresentare alberi o componenti annidati.
- Analizzare il flusso di chiamate (call stack) e il suo *unwinding*.

---

### 💡 La Metafora Guida
> **Metafora:** *La Matrioska e il riflesso di uno specchio* – ogni cavità contiene una più piccola, fino a giungere al nucleo (caso base). Analogamente, una funzione ricorsiva chiama se stessa su una versione più piccola del problema fino a raggiungere il caso base.

---

### ⚙️ Concetto in breve
| Elemento | Descrizione |
|----------|-------------|
| Caso Base | Condizione di arresto che restituisce un valore noto senza ulteriori chiamate. |
| Passo Ricorsivo | Invocazione della stessa funzione con argomenti più piccoli o più semplici. |
| Call Stack | Pila di attivazioni della funzione; ogni chiamata aggiunge un frame. |
| Unwinding | Fase di ritorno dove i risultati vengono combinati mentre i frame si rimuovono. |
| Struttura Ricorsiva | Tipo di dato che contiene un puntatore a se stesso (es. lista collegata, nodo albero). |

---

### ⚠️ Tranelli tipici
- **Mancanza di caso base:** porta a ricorsione infinita e stack overflow.
- **Passo ricorsivo non riduttivo:** non avvicina il problema al caso base, causandolo anch'esso.
- **Gestione della memoria:** dimenticare di liberare nodi in strutture ricorsive provoca leak.

---

### 🔬 Laboratorio PRIMM: *Lista collegata ricorsiva*

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]
> Quale condizione garantisce la terminazione di una funzione ricorsiva che stampa i valori di una lista collegata?
- [(X)] Quando il puntatore al nodo corrente è `nullptr`.
- [( )] Quando la lista contiene più di un elemento.
- [( )] Quando il valore del nodo è zero.

<details><summary>💡 Spiegazione</summary>
Il caso base per una lista collegata è raggiungere il puntatore nullo, segnale di fine lista.
</details>

#### 2. RUN (Esegui)
Esegui il codice che stampa ricorsivamente i valori di una lista collegata.
```cpp
#include <iostream>

struct Nodo {
    int valore;
    Nodo* prossimo;
};

void stampa(Nodo* n) {
    if (!n) return; // caso base
    std::cout << n->valore << ' ';
    stampa(n->prossimo); // passo ricorsivo
}

int main(){
    Nodo n3{3, nullptr};
    Nodo n2{2, &n3};
    Nodo n1{1, &n2};
    stampa(&n1);
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)
| Riga / Costrutto | Cosa fa | A cosa serve |
|------------------|---------|--------------|
| `if (!n) return;` | caso base | interrompe la ricorsione alla fine della lista |
| `stampa(n->prossimo);` | passo ricorsivo | chiama la stessa funzione sul nodo successivo |
| `struct Nodo` | definisce la struttura ricorsiva | ogni nodo contiene il prossimo nodo |

🔗 [Python Tutor C++](https://pythontutor.com/cpp.html)

#### 4. MODIFY (Modifica)
1. Aggiungi una funzione ricorsiva `int somma(Nodo* n)` che restituisce la somma dei valori.
2. Implementa la cancellazione ricorsiva di tutta la lista.
3. Trasforma la lista in una struttura ad albero binario e stampa in‑order.

#### 5. MAKE (Crea)
**Scenario aziendale:** Un magazzino registra le quantità di prodotti in una lista collegata; deve calcolare il totale e rimuovere prodotti esauriti.
**Requisiti:**
- Funzione `int totale(Nodo*)` che restituisce la somma.
- Funzione `void rimuoviZero(Nodo*&)` che elimina i nodi con valore 0.
- Documentazione Doxygen per ogni funzione.
- Nessuna variabile globale.

---

### 📝 Riepilogo tascabile
- Caso base + passo ricorsivo = ricorsione corretta.
- Call stack visualizza le attivazioni; l’unwinding restituisce i risultati.
- Strutture ricorsive (liste, alberi) richiedono attenzione alla gestione della memoria.

---

➡️ Prossimo chunk: *Fine del blocco* (eventuale conclusione).