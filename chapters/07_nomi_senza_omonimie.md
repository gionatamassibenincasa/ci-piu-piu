---
activity_id: namespace-01
title: "Nomi senza omonimie: usare i namespace"
methodology: PRIMM
order: 7
version: "2026-11-28"
language: it
components:
  predict_quiz:
    code: |
      #include <iostream>

      int main() {
          std::cout << "Cassa pronta\n";
          return 0;
      }
    items:
      - question: "Che cosa indica `std::` davanti a `cout`?"
        options:
          - text: "Il namespace `std`, che raccoglie il nome `cout` della libreria standard"
            correct: true
          - text: "Un comando che stampa automaticamente due volte"
            correct: false
          - text: "Il tipo numerico usato da `cout`"
            correct: false
      - question: "Perché due aziende possono avere entrambe una funzione chiamata `stampa()` senza creare per forza un conflitto?"
        options:
          - text: "Possono collocarla in namespace diversi e usare il nome completo"
            correct: true
          - text: "Perché C++ ignora sempre i nomi ripetuti"
            correct: false
          - text: "Perché una funzione con lo stesso nome viene cancellata"
            correct: false
      - question: "Quale nome identifica senza ambiguità la funzione `stampa` del namespace `magazzino`?"
        options:
          - text: "`magazzino::stampa`"
            correct: true
          - text: "`stampa::magazzino`"
            correct: false
          - text: "`namespace.magazzino.stampa`"
            correct: false
      - question: "Che cosa aggiunge l'operatore `::`?"
        options:
          - text: "Separa il namespace dal nome che contiene"
            correct: true
          - text: "Esegue due volte la funzione"
            correct: false
          - text: "Trasforma il nome in una variabile"
            correct: false
      - question: "Quale scelta rende più esplicito da dove arriva `cout`?"
        options:
          - text: "Scrivere `std::cout`"
            correct: true
          - text: "Scrivere solo `output`"
            correct: false
          - text: "Scrivere `cout::std`"
            correct: false
  investigate_quiz:
    code: |
      #include <iostream>

      namespace cassa {
          void stampa() {
              std::cout << "Totale POS\n";
          }
      }

      namespace magazzino {
          void stampa() {
              std::cout << "Scorte aggiornate\n";
          }
      }

      int main() {
          cassa::stampa();
          magazzino::stampa();
          return 0;
      }
    items:
      - question: "Quale messaggio compare per primo?"
        options:
          - text: "`Totale POS`, perché viene chiamata prima `cassa::stampa()`"
            correct: true
          - text: "`Scorte aggiornate`, perché `magazzino` viene dichiarato per ultimo"
            correct: false
          - text: "Nessun messaggio, perché i namespace impediscono le chiamate"
            correct: false
      - question: "Perché le due funzioni `stampa()` non sono lo stesso nome completo?"
        options:
          - text: "Il namespace fa parte del nome completo: `cassa::stampa` e `magazzino::stampa` sono diversi"
            correct: true
          - text: "Perché una è scritta prima dell'altra"
            correct: false
          - text: "Perché una stampa testo e l'altra no"
            correct: false
      - question: "Che cosa succede se scrivi solo `stampa();` in `main`?"
        options:
          - text: "Il compilatore non sa quale delle due funzioni scegliere"
            correct: true
          - text: "Chiama sempre la funzione del primo namespace"
            correct: false
          - text: "Chiama entrambe le funzioni in ordine alfabetico"
            correct: false
      - question: "Quale parte del codice appartiene al namespace `cassa`?"
        options:
          - text: "La funzione racchiusa tra `namespace cassa {` e la parentesi graffa corrispondente"
            correct: true
          - text: "Solo l'istruzione `std::cout`"
            correct: false
          - text: "Tutto il file, anche ciò che viene dopo"
            correct: false
      - question: "Perché `std::cout` resta esplicito anche dentro `cassa`?"
        options:
          - text: "Per distinguere il nome della libreria standard da eventuali nomi locali"
            correct: true
          - text: "Perché `std` indica sempre una variabile"
            correct: false
          - text: "Perché un namespace può contenere solo numeri"
            correct: false
  modify_quiz:
    code: |
      namespace cassa {
          void stampa() {
              std::cout << "Totale POS\n";
          }
      }

      namespace magazzino {
          void stampa() {
              std::cout << "Scorte aggiornate\n";
          }
      }
    items:
      - question: "Quale modifica aggiunge un terzo reparto senza cambiare i due esistenti?"
        options:
          - text: "Creare `namespace clienti` con una propria funzione `stampa()`"
            correct: true
          - text: "Rinominare tutte le funzioni in `stampa1`"
            correct: false
          - text: "Cancellare i namespace già presenti"
            correct: false
      - question: "Come chiami il nuovo reparto `clienti` da `main`?"
        options:
          - text: "`clienti::stampa();`"
            correct: true
          - text: "`stampa::clienti();`"
            correct: false
          - text: "`clienti.stampa();`"
            correct: false
      - question: "Quale modifica mantiene chiari i nomi se aggiungi una funzione `totale` alla cassa?"
        options:
          - text: "Chiamarla con `cassa::totale()` dal punto di utilizzo"
            correct: true
          - text: "Usare sempre solo `totale()`"
            correct: false
          - text: "Metterla nel namespace `std`"
            correct: false
      - question: "Perché non devi aggiungere funzioni personali dentro `namespace std`?"
        options:
          - text: "`std` è riservato alla libreria standard; i tuoi nomi devono stare in namespace tuoi"
            correct: true
          - text: "Perché `std` può contenere solo stringhe"
            correct: false
          - text: "Perché il compilatore non riconosce le parentesi graffe"
            correct: false
      - question: "Quale scelta riduce il rischio di usare la funzione del reparto sbagliato?"
        options:
          - text: "Scrivere il namespace in modo esplicito nelle chiamate importanti"
            correct: true
          - text: "Dare a tutte le funzioni lo stesso corpo"
            correct: false
          - text: "Eliminare i nomi dei reparti"
            correct: false
  make_instructions: >
    Crea un programma per un gestionale con i namespace `pos`, `magazzino` e
    `clienti`. Ogni namespace deve contenere una funzione `stampa()` diversa;
    `main` deve chiamarle tutte con il nome qualificato `namespace::funzione`.
  visualization:
    kind: plantuml
    note: "Rappresentare tre reparti distinti che espongono ciascuno una funzione stampa."
---

## 🏢 Nomi senza omonimie: usare i namespace

In un'azienda, il reparto POS e il reparto magazzino possono avere entrambi
una procedura chiamata “stampa”. Il nome breve è uguale, ma il contesto è
diverso. In C++ quel contesto si chiama **namespace**.

> 💡 **Metafora:** Un namespace è come l'insegna di un reparto. `stampa` è il
> nome della procedura sul cartellino; `cassa::stampa` significa “la stampa
> del reparto cassa”, mentre `magazzino::stampa` indica l'altra.

### 🎯 Obiettivo

Alla fine della lezione sai:

- leggere `std::cout` come nome qualificato;
- creare un namespace con funzioni dai nomi riutilizzabili;
- chiamare una funzione con l'operatore `::`;
- spiegare perché il contesto evita omonimie.

### ⚙️ Il nome completo

```cpp
namespace cassa {
    void stampa() {
        std::cout << "Totale POS\n";
    }
}

cassa::stampa();
```

Il simbolo `::` si legge “appartiene a”. Il nome completo è più lungo, ma
comunica subito il reparto responsabile.

### 🔬 Laboratorio PRIMM: due reparti, una procedura

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

#### 2. RUN (Esegui)

```cpp
#include <iostream>

namespace cassa {
    void stampa() {
        std::cout << "Totale POS\n";
    }
}

namespace magazzino {
    void stampa() {
        std::cout << "Scorte aggiornate\n";
    }
}

int main() {
    cassa::stampa();
    magazzino::stampa();
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Indaga)

[[ investigate_block() ]]

| Passo | Istruzione | Perché è importante |
|---:|---|---|
| 1 | `namespace cassa` | Apre il contesto del reparto POS |
| 2 | `cassa::stampa()` | Seleziona la procedura della cassa |
| 3 | `namespace magazzino` | Apre un contesto distinto |
| 4 | `magazzino::stampa()` | Seleziona la procedura del magazzino |

Il compilatore non confonde le due funzioni perché il nome completo contiene
anche il namespace. Puoi osservare il flusso passo-passo in
[Python Tutor C++](https://pythontutor.com/cpp.html).

#### 4. MODIFY (Modifica)

[[ modify_block() ]]

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

namespace cassa {
    void stampa() { std::cout << "Totale POS\n"; }
}

int main() {
    cassa::stampa();
    return 0;
}
```
</details>

1. Aggiungi `namespace clienti` con una propria `stampa()`.
2. Aggiungi `totale()` dentro `cassa` e chiamala con `cassa::totale()`.
3. Prova a chiamare solo `stampa()` e osserva l'errore di nome non visibile o
   ambiguo; poi correggi usando il nome qualificato.

#### 5. MAKE (Crea)

Realizza `reparti.cpp` per un gestionale:

1. crea i namespace `pos`, `magazzino` e `clienti`;
2. definisci in ognuno una funzione `stampa()` con un messaggio diverso;
3. chiama le tre funzioni da `main` usando sempre `namespace::stampa()`;
4. aggiungi un commento `///` per spiegare una scelta aziendale.

<details>
<summary>💡 Scaffold</summary>

```cpp
#include <iostream>

namespace pos {
    void stampa() {
        // TODO: messaggio del reparto POS
    }
}

int main() {
    // TODO: aggiungi gli altri reparti e chiamali con ::
    return 0;
}
```
</details>

### 📝 Riepilogo tascabile

- [ ] Un namespace raggruppa nomi appartenenti allo stesso contesto.
- [ ] `::` collega il contesto al nome: `reparto::funzione`.
- [ ] Due funzioni con lo stesso nome breve possono convivere in namespace diversi.
- [ ] `std::cout` esplicita che `cout` appartiene alla libreria standard.

### ➡️ Prossimo passo

Ora che i nomi sono ordinati, impari a lasciare etichette utili anche sul
programma: la documentazione Doxygen.
