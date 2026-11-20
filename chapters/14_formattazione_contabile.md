---
activity_id: "formattazione-contabile-01"
title: "La stampante fiscale: formattare importi con `<iomanip>`"
methodology: PRIMM
order: 15
version: "2026-11-20"
language: it
components:
  predict_quiz:
    code: |
      #include <iostream>
      #include <iomanip>

      int main() {
          double imponibile = 19.5;
          std::cout << std::fixed << std::setprecision(2) << imponibile;
          return 0;
      }
    items:
      - question: "Perché `std::fixed` è utile quando stampi un importo?"
        options:
          - text: "Chiede di rappresentare il numero in forma decimale fissa, adatta a un prospetto"
            correct: true
          - text: "Trasforma automaticamente l'importo da euro a centesimi"
            correct: false
          - text: "Arrotonda sempre il valore memorizzato nella variabile"
            correct: false
      - question: "Che cosa indica `std::setprecision(2)` insieme a `std::fixed`?"
        options:
          - text: "Mostrare due cifre dopo il punto decimale"
            correct: true
          - text: "Moltiplicare il numero per 2"
            correct: false
          - text: "Mostrare al massimo due cifre complessive"
            correct: false
      - question: "Prima del Run, quale output prevedi per `19.5`?"
        options:
          - text: "19.50"
            correct: true
          - text: "19.5"
            correct: false
          - text: "20.00"
            correct: false
      - question: "Perché nel programma serve `#include <iomanip>`?"
        options:
          - text: "Per rendere disponibili `std::fixed` e `std::setprecision`"
            correct: true
          - text: "Per dichiarare automaticamente tutte le variabili `double`"
            correct: false
          - text: "Per sostituire `#include <iostream>` nelle stampe"
            correct: false
      - question: "Se scrivi `std::setprecision(2)` senza `std::fixed`, quale previsione è più corretta?"
        options:
          - text: "La precisione riguarda le cifre significative, quindi non garantisce sempre due decimali"
            correct: true
          - text: "Il programma non può compilare perché `setprecision` richiede un intero positivo diverso da 2"
            correct: false
          - text: "L'output avrà sempre esattamente due cifre dopo il punto"
            correct: false
  investigate_quiz:
    code: |
      #include <iostream>
      #include <iomanip>

      int main() {
          double imponibile = 19.5;
          double iva = imponibile * 0.22;
          double totale = imponibile + iva;

          std::cout << std::fixed << std::setprecision(2);
          std::cout << "Imponibile: " << imponibile << '\n';
          std::cout << "IVA:        " << iva << '\n';
          std::cout << "Totale:     " << totale << '\n';
          return 0;
      }
    items:
      - question: "Perché anche `iva` e `totale` vengono stampate con due decimali?"
        options:
          - text: "I manipolatori restano attivi per le stampe successive dello stesso `std::cout`"
            correct: true
          - text: "Ogni `double` viene sempre stampato con due decimali in C++"
            correct: false
          - text: "La variabile `imponibile` trasferisce il suo formato alle altre variabili"
            correct: false
      - question: "Qual è l'ordine corretto nella riga di configurazione?"
        options:
          - text: "Prima `std::fixed`, poi `std::setprecision(2)`, quindi il valore da stampare"
            correct: true
          - text: "Prima il valore, poi `std::fixed` e infine `std::setprecision(2)`"
            correct: false
          - text: "Prima `std::setprecision(2)`, poi si chiude `std::cout` con un punto e virgola"
            correct: false
      - question: "Perché il risultato di `19.5 * 0.22` può essere visualizzato come `4.29`?"
        options:
          - text: "Il formato mostra due decimali e arrotonda la rappresentazione visualizzata"
            correct: true
          - text: "Il programma sostituisce sempre il valore con il numero intero più vicino"
            correct: false
          - text: "La moltiplicazione viene eseguita come testo e non come numero"
            correct: false
      - question: "Che cosa succede se togli `#include <iomanip>` ma lasci `std::setprecision(2)`?"
        options:
          - text: "Il compilatore può segnalare che `setprecision` non è dichiarata"
            correct: true
          - text: "Il programma compila, ma `std::cout` ignora soltanto la precisione"
            correct: false
          - text: "Il valore viene automaticamente stampato come intero"
            correct: false
      - question: "Se aggiungi una stampa dopo il prospetto senza cambiare il formato, che cosa accade?"
        options:
          - text: "Anche quella stampa usa il formato corrente di `std::cout`, finché non lo modifichi"
            correct: true
          - text: "Il formato si annulla automaticamente dopo ogni riga"
            correct: false
          - text: "Il formato si applica solo alla variabile `imponibile`"
            correct: false
  modify_quiz:
    code: |
      std::cout << std::fixed << std::setprecision(2);
      std::cout << "Totale: " << totale << '\n';
    items:
      - question: "Quale modifica fa apparire tre cifre dopo il punto decimale?"
        options:
          - text: "Sostituire `std::setprecision(2)` con `std::setprecision(3)`"
            correct: true
          - text: "Sostituire `std::fixed` con `std::setprecision(3)`"
            correct: false
          - text: "Moltiplicare `totale` per 3 prima della stampa"
            correct: false
      - question: "Che effetto ha togliere `std::fixed` lasciando `std::setprecision(2)`?"
        options:
          - text: "La precisione può indicare due cifre significative, non necessariamente due decimali"
            correct: true
          - text: "Il programma stampa sempre due zeri in più"
            correct: false
          - text: "Il valore di `totale` viene cancellato"
            correct: false
      - question: "Quale modifica mantiene il prospetto a due decimali ma stampa prima l'etichetta `Totale`?"
        options:
          - text: "Spostare l'etichetta nella stessa espressione di output, prima di `totale`"
            correct: true
          - text: "Mettere `std::fixed` dopo `totale` e prima dell'etichetta"
            correct: false
          - text: "Cambiare `totale` in una variabile `int`"
            correct: false
      - question: "Se sostituisci `std::setprecision(2)` con `std::setprecision(0)`, quale effetto prevedi?"
        options:
          - text: "La stampa usa zero cifre dopo il punto e può arrotondare il valore visualizzato"
            correct: true
          - text: "La stampa usa automaticamente due cifre perché gli importi sono monetari"
            correct: false
          - text: "Il programma entra in un ciclo infinito"
            correct: false
      - question: "Quale modifica formatta anche la nuova variabile `sconto` con due decimali?"
        options:
          - text: "Stampare `sconto` con lo stesso `std::cout` dopo aver impostato `fixed` e `setprecision(2)`"
            correct: true
          - text: "Dichiarare `sconto` come `char`"
            correct: false
          - text: "Inserire `std::setprecision(2)` solo dopo la stampa di `sconto`"
            correct: false
  make_instructions: "Crea un prospetto di preventivo con imponibile, IVA e totale, tutti visualizzati con due cifre decimali."
  visualization:
    kind: table
    note: "Confrontare lo stesso importo prima e dopo l'impostazione di fixed e setprecision."
registro:
  argomenti: "Formattazione di importi con <iomanip>, std::fixed e std::setprecision; prospetto contabile con imponibile, IVA e totale."
  note: "Laboratorio PRIMM su output monetario in uno scenario di contabilità aziendale."
assessment:
  duration_min: 15
  total_points: 6
  versions: ["A", "B"]
  predict:
    points: 2
    prompt: "Prevedi l'output di un importo stampato con std::fixed e std::setprecision(2) e spiega il ruolo dei due manipolatori."
    context: "fixed imposta la notazione decimale fissa; setprecision(2) visualizza due cifre dopo il punto."
  investigate:
    points: 2
    questions:
      - "Perché il formato resta attivo nelle stampe successive dello stesso std::cout?"
      - "Che errore può comparire se manca #include <iomanip>?"
    typical_errors:
      - "Confondere la precisione con il numero di cifre dopo il punto quando manca fixed."
      - "Pensare che il formato cambi il valore memorizzato."
    context: "I manipolatori configurano lo stream e agiscono sulla rappresentazione visualizzata."
  modify:
    points: 1
    prompt: "Modifica un prospetto per mostrare tre cifre decimali senza cambiare i calcoli."
    typical_errors:
      - "Moltiplicare il valore invece di cambiare setprecision."
    context: "Il numero passato a setprecision determina le cifre visualizzate in modalità fixed."
  make:
    points: 1
    prompt: "Completa un preventivo con imponibile, IVA e totale, tutti con due decimali."
    must_include: ["<iomanip>", "std::fixed", "std::setprecision(2)"]
    typical_errors:
      - "Dimenticare di impostare il formato prima delle stampe."
    context: "Il prospetto deve essere leggibile e coerente come un documento contabile."
files:
  - path: "student_work/make/prospetto_preventivo.cpp"
    action: create
    phase: make
    template_content: |
      #include <iostream>
      #include <iomanip>

      int main() {
          double imponibile = 125.5;
          double iva = imponibile * 0.22;
          double totale = imponibile + iva;

          // TODO: configura il formato del prospetto
          // TODO: stampa imponibile, IVA e totale
          return 0;
      }
    validation_rules:
      min_lines: 14
      must_contain: ["setprecision", "fixed"]
---

## 🖨️ La stampante fiscale: `std::fixed` e `std::setprecision`

Quando stampi un importo, `std::cout` mostra il valore in una forma tecnica. In un preventivo o in una fattura, invece, vuoi una forma regolare: due cifre dopo il punto decimale per ogni riga.

> 💡 **Metafora:**  
> Immagina una stampante fiscale. `std::fixed` seleziona la modalità “importo decimale”; `std::setprecision(2)` imposta due caselle per i centesimi. La stampante non cambia il valore del calcolo: cambia il modo in cui lo presenta.

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- formattare un prospetto di importi con `std::fixed` e `std::setprecision(2)`.

---

### ⚙️ Prima del laboratorio: i due manipolatori

| Elemento | Che cosa imposta | Perché serve in contabilità |
| :--- | :--- | :--- |
| `#include <iomanip>` | Rende disponibili i manipolatori di formattazione | Il compilatore conosce `std::fixed` e `std::setprecision` |
| `std::fixed` | Notazione decimale fissa | Evita una visualizzazione tecnica o variabile |
| `std::setprecision(2)` | Due cifre dopo il punto con `fixed` | Mantiene coerenti importi e totali |

```cpp
std::cout << std::fixed << std::setprecision(2);
std::cout << 19.5;  // 19.50
```

La configurazione resta attiva per le stampe successive dello stesso `std::cout`.

---

### 🔬 Laboratorio PRIMM: il prospetto di una vendita

Il negozio registra un imponibile di `19.5` euro e applica l'IVA al 22%. Prima di eseguire il programma, osserva come verranno stampate le tre righe.

#### 1. PREDICT (Prevedi)

[[ predict_block() ]]

Completa prima il quiz: concentrati sulla differenza tra **valore calcolato** e **valore visualizzato**.

#### 2. RUN (Esegui)

Ricopia ed esegui il programma. Confronta il risultato con la tua previsione.

```cpp
/**
 * @file prospetto_vendita.cpp
 * @brief Presenta un prospetto di vendita in un formato leggibile.
 */
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Imponibile: " << imponibile << '\n';
    std::cout << "IVA 22%:    " << iva << '\n';
    std::cout << "Totale:     " << totale << '\n';
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

[[ investigate_block() ]]

Perché l'impostazione compare una sola volta ma vale per tre stampe? Segui l'ordine delle istruzioni:

| Passo | Istruzione | Che cosa osservi |
| :---: | :--- | :--- |
| 1 | `imponibile = 19.5` | Il programma conserva il valore numerico |
| 2 | `iva = imponibile * 0.22` | Calcola l'IVA |
| 3 | `totale = imponibile + iva` | Calcola il totale |
| 4 | `fixed` + `setprecision(2)` | Configura la visualizzazione di `std::cout` |
| 5 | Le tre stampe | Ogni importo appare con due cifre decimali |

Con `fixed` e `setprecision(2)`, `19.5` viene mostrato come `19.50`. Il formato non arrotonda o riscrive la variabile in memoria: riguarda la stampa.

#### 4. MODIFY (Modifica)

[[ modify_block() ]]

Apporta una modifica alla volta e riesegui.

**Modifica A — Cambia la precisione**  
Sostituisci `std::setprecision(2)` con `std::setprecision(3)`. Controlla tutte le righe del prospetto.

**Modifica B — Togli `fixed`**  
Lascia `std::setprecision(2)` ma rimuovi `std::fixed`. Confronta il risultato e spiega perché non hai più la garanzia di due cifre dopo il punto.

**Modifica C — Aggiungi una riga**  
Dichiara `double sconto = 1.5;` e stampa `Sconto: 1.50` usando la stessa configurazione già attiva.

<details>
<summary>💡 Scaffold per le modifiche</summary>

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 19.5;
    double iva = imponibile * 0.22;
    double totale = imponibile + iva;
    double sconto = 1.5;

    std::cout << std::fixed << std::setprecision(2);
    // TODO: stampa il prospetto e la nuova riga Sconto
    return 0;
}
```

</details>

#### 5. MAKE (Crea)

**Scenario aziendale:** l'ufficio commerciale prepara un preventivo per un cliente.

**Requisiti**:

1. Dichiara `imponibile = 125.5` e `aliquota = 0.22`.
2. Calcola `iva` e `totale` con variabili `double`.
3. Configura `std::cout` con `std::fixed` e `std::setprecision(2)`.
4. Stampa le tre etichette `Imponibile`, `IVA 22%` e `Totale`, ciascuna su una riga.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double imponibile = 125.5;
    double aliquota = 0.22;
    double iva = imponibile * aliquota;
    double totale = imponibile + iva;

    /// Il formato uniforme rende il preventivo leggibile e confrontabile.
    // TODO: configura la stampa a due decimali
    // TODO: stampa imponibile, IVA e totale
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- `#include <iomanip>` rende disponibili i manipolatori di formattazione.
- `std::fixed` imposta la notazione decimale fissa.
- Con `std::fixed`, `std::setprecision(2)` mostra due cifre dopo il punto.
- La configurazione resta attiva per le stampe successive dello stesso `std::cout`.
- Il formato cambia la rappresentazione visualizzata, non il valore memorizzato.

---

### ➡️ Prossimo chunk

Ora che sai presentare bene un risultato, puoi imparare a organizzare il calcolo in **funzioni** riutilizzabili.

<!--#
  Checklist autore / LLM (golden sample = chapters/03_ciao_mondo.md)
  [ ] Un solo obiettivo (chunking)
  [ ] Metafora esplicita con corrispondenze concrete
  [ ] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [ ] investigate_quiz.items ~5, perché / tracing / errori
  [ ] modify_quiz.items ~5, effetto della modifica
  [ ] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [ ] Run con @LIA.cpp; codice completo e terminante
  [ ] Make con scenario SIA, requisiti chiusi e scaffold
  [ ] Commenti /// solo sul perché
  [ ] Nessun costrutto successivo introdotto per necessità
  [ ] validate OK
#-->
