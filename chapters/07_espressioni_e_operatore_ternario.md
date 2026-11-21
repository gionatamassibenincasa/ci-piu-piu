---
activity_id: espressioni-ternario-01
title: 'La Calcolatrice Fiscale: espressioni e operatore ternario'
methodology: PRIMM
order: 7
version: '2026-11-22'
language: it
components:
  predict_quiz:
    code: |
      double importoProdotti = 85.00;
      double sconto = (importoProdotti >= 50.0) ? 0.10 : 0.02;
      double netto = importoProdotti - importoProdotti * sconto;
      double spedizione = (netto >= 60.0) ? 0.0 : 6.50;
    items:
      - question: 'Perché `importoProdotti >= 50.0` è utile dentro il ternario?'
        options:
          - text: 'Produce una condizione `true` o `false` che permette di scegliere un valore'
            correct: true
          - text: 'Converte automaticamente l’importo in euro interi'
            correct: false
          - text: 'Ripete il calcolo finché l’importo raggiunge 50 euro'
            correct: false
      - question: 'Quale valore assume `sconto` con `importoProdotti = 85.00`?'
        options:
          - text: '`0.10`, perché 85 soddisfa la condizione e viene scelto il valore dopo `?`'
            correct: true
          - text: '`0.02`, perché il ternario sceglie sempre il valore dopo `:`'
            correct: false
          - text: '`10.00`, perché il numero 10 rappresenta direttamente gli euro di sconto'
            correct: false
      - question: 'Perché `importoProdotti / 2 * 10.0` con `int importoProdotti = 5` non dà 25.0?'
        options:
          - text: 'La divisione tra due `int` viene eseguita prima e perde la parte decimale: 5 / 2 vale 2'
            correct: true
          - text: 'Il simbolo `*` viene ignorato quando compare dopo `/`'
            correct: false
          - text: 'Un `int` non può essere usato in nessuna espressione con `double`'
            correct: false
      - question: 'Quale valore completo restituisce `netto >= 60.0 ? 0.0 : 6.50` quando `netto` vale 76.50?'
        options:
          - text: '`0.0`, perché la condizione è vera e si sceglie il primo valore'
            correct: true
          - text: '`6.50`, perché le spese standard vengono calcolate per prime'
            correct: false
          - text: '`true`, perché un confronto restituisce sempre un booleano stampabile'
            correct: false
      - question: 'Quale forma assegna correttamente al netto il prezzo lordo meno lo sconto?'
        options:
          - text: '`netto = lordo - lordo * percentualeSconto;`'
            correct: true
          - text: '`netto = lordo - percentualeSconto;`'
            correct: false
          - text: '`netto = lordo * percentualeSconto - lordo;`'
            correct: false
  investigate_quiz:
    code: |
      const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;
      const double COSTO_SPEDIZIONE_STANDARD = 6.50;
      double importoProdotti = 85.00;
      double percentualeSconto =
          (importoProdotti >= 50.0) ? 0.10 : 0.02;
      double valoreSconto = importoProdotti * percentualeSconto;
      double nettoProdotti = importoProdotti - valoreSconto;
      double speseSpedizione =
          (nettoProdotti >= SOGLIA_SPEDIZIONE_GRATIS)
              ? 0.0 : COSTO_SPEDIZIONE_STANDARD;
      double totaleDaPagare = nettoProdotti + speseSpedizione;
    items:
      - question: 'Quale ordine descrive correttamente il calcolo del totale?'
        options:
          - text: 'Prima si sceglie la percentuale, poi si calcola lo sconto, poi il netto e infine la spedizione'
            correct: true
          - text: 'Prima si calcola il totale, poi si decide quale percentuale usare'
            correct: false
          - text: 'I due ternari vengono eseguiti dopo la stampa, perché assegnano solo etichette'
            correct: false
      - question: 'Perché `valoreSconto` vale `8.5` in questo esempio?'
        options:
          - text: 'Perché l’espressione moltiplica 85.0 per 0.10, cioè il 10% scritto in forma decimale'
            correct: true
          - text: 'Perché 0.10 viene interpretato come 10 euro fissi'
            correct: false
          - text: 'Perché il programma divide 85 per 10 prima di moltiplicare'
            correct: false
      - question: 'Quale ramo del secondo ternario viene scelto?'
        options:
          - text: 'Il ramo `0.0`, perché `nettoProdotti` vale 76.5 ed è almeno 60.0'
            correct: true
          - text: 'Il ramo `6.50`, perché il prezzo lordo è diverso dalla soglia'
            correct: false
          - text: 'Nessun ramo, perché un `double` non può essere confrontato con una costante'
            correct: false
      - question: 'Perché il totale viene calcolato con `nettoProdotti + speseSpedizione` e non con l’importo lordo?'
        options:
          - text: 'Perché lo sconto è già stato sottratto e il cliente deve pagare il netto più l’eventuale spedizione'
            correct: true
          - text: 'Perché il lordo contiene sempre un errore di divisione intera'
            correct: false
          - text: 'Perché il ternario può sommare soltanto variabili chiamate `netto`'
            correct: false
      - question: 'Se il codice usa `nettoProdotti` prima della sua dichiarazione, perché il compilatore segnala un errore?'
        options:
          - text: 'Una variabile deve essere dichiarata e inizializzata prima di poter essere usata'
            correct: true
          - text: 'Il compilatore esegue le righe in ordine alfabetico'
            correct: false
          - text: 'I nomi con la parola `netto` sono riservati e non ammessi'
            correct: false
  modify_quiz:
    code: |
      double importoProdotti = 85.00;
      double speseSpedizione =
          (importoProdotti >= 60.0) ? 0.0 : 6.50;
      std::cout << speseSpedizione << "\n";
    items:
      - question: 'Quale modifica fa pagare la spedizione gratis solo da 100 euro in su?'
        options:
          - text: 'Cambiare `importoProdotti >= 60.0` in `importoProdotti >= 100.0`'
            correct: true
          - text: 'Cambiare `0.0` in `100.0`'
            correct: false
          - text: 'Cambiare il simbolo `?` in `:`'
            correct: false
      - question: 'Con `importoProdotti = 45.00`, quale modifica produce 3.00 euro di supplemento express?'
        options:
          - text: 'Aggiungere `double supplemento = consegnaRapida ? 3.00 : 0.0;` e sommarlo alla spedizione'
            correct: true
          - text: 'Sostituire la condizione con `consegnaRapida + 3.00`'
            correct: false
          - text: 'Moltiplicare `speseSpedizione` per `consegnaRapida`'
            correct: false
      - question: 'Se sostituisci `0.0` con `0`, quale effetto corretto osservi?'
        options:
          - text: 'La scelta continua a funzionare e il risultato numerico è zero; `0.0` rende però esplicito il tipo decimale'
            correct: true
          - text: 'Il ternario non compila perché il valore vero deve avere sempre due decimali'
            correct: false
          - text: 'La condizione diventa automaticamente falsa'
            correct: false
      - question: 'Quale modifica stampa `"pari"` quando `articoli` vale 14?'
        options:
          - text: '`std::cout << ((articoli % 2 == 0) ? "pari" : "dispari");`'
            correct: true
          - text: '`std::cout << ((articoli / 2 == 0) ? "pari" : "dispari");`'
            correct: false
          - text: '`std::cout << (articoli % 2 ? "pari" : "dispari");`'
            correct: false
      - question: 'Perché in Modify conviene cambiare una sola soglia o un solo valore alla volta?'
        options:
          - text: 'Per collegare ogni differenza nell’output alla modifica che l’ha provocata'
            correct: true
          - text: 'Perché C++ permette una sola assegnazione per programma'
            correct: false
          - text: 'Perché il ternario non può comparire due volte nello stesso file'
            correct: false
  make_instructions: >
    Scrivi un programma per calcolare la commissione POS di un pagamento:
    usa un ternario per scegliere l'aliquota in base al circuito internazionale,
    un secondo ternario per applicare la commissione minima e stampa l'incasso
    netto con un output leggibile.
  visualization:
    kind: pythontutor
    note: Osservare l’ordine con cui cambiano percentuale, sconto, netto, spedizione e totale.
registro:
  argomenti: >
    Espressioni aritmetiche e confronti; divisione intera; operatore ternario
    `?:` per scegliere un valore; laboratorio PRIMM su sconto e spedizione
    di un ordine e-commerce.
  note: >
    Verifica formativa su Predict, Investigate, Modify e Make; consegna digitale
    collegata su Classroom50.
assessment:
  duration_min: 15
  total_points: 6
  versions: ['A', 'B']
  predict:
    points: 2
    context: >
      Riconoscere la divisione intera, il significato dei rami del ternario
      e l’ordine delle operazioni in un’espressione.
  investigate:
    points: 2
    questions:
      - Perché viene scelto il 10% di sconto?
      - Quale ordine seguono sconto, netto, spedizione e totale?
      - Perché la spedizione vale zero?
    typical_errors:
      - Confonde 0.10 con 10 euro fissi.
      - Applica la spedizione alla somma lorda prima dello sconto.
    context: >
      Tracciare valori e rami del ternario, motivando l’ordine dei calcoli.
  modify:
    points: 1
    prompt: >
      Modifica il listato per rendere gratuita la spedizione da 100 euro
      e stampa il risultato con l’importo prodotti pari a 85 euro.
    code: |
      #include <iostream>

      int main() {
          double importoProdotti = 85.00;
          double spedizione =
              (importoProdotti >= 60.0) ? 0.0 : 6.50;
          // modifica qui la soglia
          std::cout << spedizione << "\n";
          return 0;
      }
    typical_errors:
      - Cambia il valore del ramo invece della soglia nella condizione.
      - Modifica contemporaneamente la soglia e il costo standard.
    context: >
      La soglia appartiene alla condizione; i due valori dopo `?` e `:`
      restano i risultati possibili.
  make:
    points: 1
    prompt: >
      Realizza un programma POS con importo 45.00 euro e flag
      `circuitoInternazionale`. Scegli 1.8% oppure 0.7%, applica una
      commissione minima di 0.15 euro e calcola l’incasso netto.
    must_include:
      - Un ternario per l’aliquota.
      - Un ternario per la commissione minima.
      - Output di commissione finale e incasso netto.
    typical_errors:
      - Usa 1.8 invece di 0.018.
      - Applica la soglia minima prima di calcolare la commissione.
    context: >
      Il programma deve scegliere aliquota e commissione minima come espressioni
      che restituiscono un valore.
    code: ''
  variants:
    B:
      modify:
        prompt: >
          Modifica il listato per rendere gratuita la spedizione da 50 euro
          e usa importo prodotti pari a 45 euro.
        code: |
          #include <iostream>

          int main() {
              double importoProdotti = 45.00;
              double spedizione =
                  (importoProdotti >= 60.0) ? 0.0 : 6.50;
              // modifica qui la soglia
              std::cout << spedizione << "\n";
              return 0;
          }
files:
  - path: README.md
    action: create
    description: Istruzioni per svolgere la consegna PRIMM
    template_content: |
      # Espressioni e operatore ternario

      Lavora nell'ordine Predict → Run → Investigate → Modify → Make.
      Cambia una sola cosa alla volta e ricompila dopo ogni modifica.
  - path: student_work/modify/cassa_fiscale.cpp
    action: create
    phase: modify
    description: Modifica guidata della soglia di spedizione
    template_content: |
      #include <iostream>

      int main() {
          double importoProdotti = 85.00;
          double speseSpedizione =
              (importoProdotti >= 60.0) ? 0.0 : 6.50;
          // TODO: modifica la soglia richiesta
          std::cout << speseSpedizione << "\n";
          return 0;
      }
    validation_rules:
      min_lines: 8
      must_contain:
        - '?'
  - path: student_work/make/commissioni_pos.cpp
    action: create
    phase: make
    description: Calcolo della commissione POS con due ternari
    template_content: |
      #include <iostream>

      int main() {
          double importoPagamento = 45.00;
          bool circuitoInternazionale = true;
          /// Le due aliquote rappresentano il costo dei circuiti di pagamento.
          // TODO: scegli l'aliquota con un ternario
          // TODO: calcola la commissione e applica il minimo
          // TODO: stampa commissione finale e incasso netto
          return 0;
      }
    validation_rules:
      min_lines: 10
      must_contain:
        - '?'
---

## 🧮 La Calcolatrice Fiscale: espressioni e operatore ternario

> "La semplicità è la sofisticazione suprema."
>
> — *Leonardo da Vinci*

Quando prepari uno scontrino, non fai un solo calcolo: parti dall'importo,
applichi uno sconto e poi decidi se la spedizione è gratuita. In C++ puoi
scrivere questi passaggi come **espressioni** e usare il ternario per una
scelta semplice che restituisce direttamente un valore.

> 💡 **Metafora:**  
> Un'espressione è una riga della calcolatrice della cassa: combina numeri,
> variabili e operatori e restituisce un risultato. Il ternario è il sensore
> della cassa: legge una condizione e apre uno dei due cassetti, quello del
> valore vero oppure quello del valore falso.

---

### 🎯 Obiettivo di questo chunk

Alla fine di questa lezione sei in grado di:

- scrivere un'espressione che calcola un importo e usa l'operatore ternario per scegliere un valore.

---

### ⚙️ Prima del laboratorio: costruire un'espressione

Un'espressione combina valori, variabili e operatori e produce **un solo
risultato**.

| Operatore | Significato | Attenzione |
| :--- | :--- | :--- |
| `+`, `-`, `*` | somma, differenza, prodotto | il risultato dipende dai tipi |
| `/` | divisione | tra soli `int` perde la parte decimale |
| `%` | resto della divisione | utile per controllare pari/dispari |
| `>=`, `==` | confronto | producono `true` oppure `false` |

```cpp
int pezzi = 5;
double a = pezzi / 2;   // 2.0: la divisione è già stata fatta tra int
double b = pezzi / 2.0; // 2.5: almeno un operando è double
```

### 🧭 Prima del laboratorio: scegliere un valore

La forma del ternario è:

```text
condizione ? valore_se_vero : valore_se_falso
```

Il programma valuta prima la condizione e poi sceglie **un solo** ramo:

```cpp
double spedizione = (totale >= 60.0) ? 0.0 : 6.50;
```

Il ternario è adatto a una scelta breve che produce un valore da assegnare,
stampare o usare in un altro calcolo. Le decisioni con più istruzioni
arriveranno con `if` / `else`.

---

### 🔬 Laboratorio PRIMM: Scontrino e-commerce

Calcolerai lo sconto e le spese di spedizione di un ordine online.

#### 1. PREDICT (Prevedi)

Prima di eseguire, osserva l'esempio e scegli la spiegazione più convincente:

[[ predict_block() ]]

#### 2. RUN (Esegui)

Digita il programma, eseguilo e confronta l'output con le tue previsioni.

```cpp
/**
 * @file scontrino_ecommerce.cpp
 * @brief Calcola sconto, spedizione e totale di un ordine online.
 * @return int Codice di uscita del programma.
 */
#include <iostream>

int main() {
    const double SOGLIA_SPEDIZIONE_GRATIS = 60.0;
    const double COSTO_SPEDIZIONE_STANDARD = 6.50;
    double importoProdotti = 85.00;

    /// La soglia collega il vantaggio fedeltà al valore dell'ordine.
    double percentualeSconto =
        (importoProdotti >= 50.0) ? 0.10 : 0.02;
    double valoreSconto = importoProdotti * percentualeSconto;
    double nettoProdotti = importoProdotti - valoreSconto;

    /// La consegna gratuita riduce il costo per ordini abbastanza grandi.
    double speseSpedizione =
        (nettoProdotti >= SOGLIA_SPEDIZIONE_GRATIS)
            ? 0.0 : COSTO_SPEDIZIONE_STANDARD;
    double totaleDaPagare = nettoProdotti + speseSpedizione;

    std::cout << "=== SCONTRINO E-COMMERCE ===\n";
    std::cout << "Prodotti (lordo): " << importoProdotti << " euro\n";
    std::cout << "Sconto: " << valoreSconto << " euro\n";
    std::cout << "Prodotti (netto): " << nettoProdotti << " euro\n";
    std::cout << "Spedizione: " << speseSpedizione << " euro\n";
    std::cout << "TOTALE: " << totaleDaPagare << " euro\n";
    return 0;
}
```
@LIA.cpp

#### 3. INVESTIGATE (Investiga)

Dopo il Run, ricostruisci l'ordine dei valori:

[[ investigate_block() ]]

| Passo | Espressione o variabile | Valore | Perché |
| :---: | :--- | ---: | :--- |
| 1 | `importoProdotti >= 50.0` | `true` | 85 è almeno 50 |
| 2 | `percentualeSconto` | `0.10` | viene scelto il ramo dopo `?` |
| 3 | `valoreSconto` | `8.5` | `85.0 * 0.10` |
| 4 | `nettoProdotti` | `76.5` | `85.0 - 8.5` |
| 5 | `nettoProdotti >= 60.0` | `true` | 76.5 supera la soglia |
| 6 | `speseSpedizione` | `0.0` | viene scelto il ramo dopo `?` |
| 7 | `totaleDaPagare` | `76.5` | netto più spedizione |

Apri il programma in [Python Tutor C++](https://pythontutor.com/cpp.html):
osserva come ogni assegnazione crea o aggiorna una variabile prima della
stampa finale.

#### 4. MODIFY (Modifica)

Prima di cambiare il codice, prevedi l'effetto delle modifiche:

[[ modify_block() ]]

Parti da questo scaffold:

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double importoProdotti = 85.00;
    double speseSpedizione =
        (importoProdotti >= 60.0) ? 0.0 : 6.50;
    std::cout << speseSpedizione << "\n";
    return 0;
}
```

</details>

**Modifica A — nuova soglia**  
Porta la soglia della spedizione gratuita a `100.0`. Cambia una sola parte,
ricompila e spiega perché ora compare il costo standard.

**Modifica B — consegna express**  
Aggiungi `bool consegnaRapida = true;`. Usa un ternario per calcolare un
supplemento di `3.00` se è vero e `0.0` altrimenti; somma il supplemento alla
spedizione.

**Modifica C — pari o dispari**  
Con `int articoli = 14;`, usa `%` e un ternario per stampare `"pari"` oppure
`"dispari"`.

#### 5. MAKE (Crea)

**Scenario aziendale — Commissione transazione POS**

Scrivi `commissioni_pos.cpp` per un esercente. I requisiti sono chiusi:

1. Dichiara `double importoPagamento = 45.00;`.
2. Dichiara `bool circuitoInternazionale = true;`.
3. Usa un ternario: circuito internazionale → aliquota `0.018`, altrimenti
   aliquota `0.007`.
4. Calcola la commissione; con un secondo ternario, se è minore di `0.15`,
   usa `0.15` come commissione finale.
5. Stampa commissione finale e incasso netto
   (`importoPagamento - commissioneFinale`) in un output leggibile.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
#include <iostream>

int main() {
    double importoPagamento = 45.00;
    bool circuitoInternazionale = true;
    /// L'aliquota varia perché i circuiti applicano costi diversi.
    double aliquota = 0.0; // TODO: ternario sulle due aliquote
    double commissione = 0.0; // TODO: importo per aliquota
    double commissioneFinale = 0.0; // TODO: ternario sulla soglia minima
    double incassoNetto = 0.0; // TODO: importo meno commissione finale
    std::cout << "Commissione: " << commissioneFinale << " euro\n";
    std::cout << "Incasso netto: " << incassoNetto << " euro\n";
    return 0;
}
```

</details>

---

### 📝 Riepilogo tascabile

- Un'espressione produce un valore usando variabili, letterali e operatori.
- Tra soli `int`, `/` esegue una divisione intera: la parte decimale si perde.
- Un confronto come `totale >= 60.0` produce `true` o `false`.
- Il ternario ha la forma `condizione ? se_vero : se_falso` e restituisce un valore.
- Cambia una sola cosa alla volta: così colleghi l'output alla causa.

---

### ➡️ Prossimo chunk

Quando una scelta deve eseguire più istruzioni, una riga non basta più.
Nel prossimo chunk userai `if` / `else` per costruire un vero bivio nel
programma.

<!--#
  Checklist autore / LLM (golden sample = chapters/03_ciao_mondo.md)
  [x] Un solo obiettivo osservabile
  [x] Metafora esplicita con mapping tra concetto e scenario
  [x] predict_quiz.items ~5, concettuali, con distrattori da misconception
  [x] investigate_quiz.items ~5, con perché / tracing / errore
  [x] modify_quiz.items ~5, sull'effetto delle modifiche
  [x] Macro [[ predict_block() ]], [[ investigate_block() ]], [[ modify_block() ]]
  [x] Run con programma completo e @LIA.cpp
  [x] Commenti /// solo sul perché
  [x] Investigate con tabella e link a Python Tutor
  [x] Make con scenario SIA, requisiti chiusi e scaffold in <details>
  [x] registro e assessment coerenti con il capitolo
  [x] activity_id e order conservati
  [ ] validate OK
#-->
