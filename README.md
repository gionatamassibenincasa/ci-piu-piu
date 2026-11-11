<!--
author:   Gionata Massi
email:    gionata.massi@savoiabenicasa.it
version:  2026-11-11
language: it
narrator: IT Italian Male
comment:  Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
          Alcune frasi sono tratte da: Bjarne Stroustrup - Programming Principles and Practice Using C++
import:   https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:   https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
-->

# 🚀 C++ - AS 2026-27 - 3ze SIA

> "Programmare è capire."
> — *Kristen Nygaard*

Benvenuto nel corso! Questo non è un semplice libro di testo: è un **laboratorio interattivo**. 
Se non vedi le animazioni o i blocchi di codice eseguibili, assicurati di visualizzare questa pagina su LiaScript:

🔗 [Apri il corso su LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/refs/heads/main/README.md)

---

## 🧠 Come useremo questo materiale (Metodo PRIMM)
Ogni lezione è un "chunk" (un boccone digeribile) strutturato in 5 fasi per allenare il tuo cervello da programmatore:
1. **P**redict (Prevedi): Cosa pensi che farà questo codice?
2. **R**un (Esegui): Prova il codice e verifica la tua ipotesi.
3. **I**nvestigate (Investiga): Analizza *perché* ha funzionato in quel modo.
4. **M**odify (Modifica): Cambia piccole parti del codice per vedere cosa si rompe (e come aggiustarlo!).
5. **M**ake (Crea): Usa ciò che hai imparato per costruire qualcosa di tuo.

---

## ⚙️ Il Motore Sotto il Cofano

> "La programmazione è l'arte di esprimere soluzioni ai problemi in modo che un computer possa eseguirle. Spesso un problema viene compreso appieno solo attraverso il processo di programmazione di una soluzione."
> — *Bjarne Stroustrup*

Sviluppare un programma non è "scrivere codice a caso sperando che funzioni". È un processo ingegneristico composto da 4 fasi:
1. **Analisi**: Qual è il problema? Cosa vuole l'utente?
2. **Progettazione**: Qual è la struttura? Come comunicano le parti?
3. **Programmazione**: Scrivere il codice rispettando i vincoli (tempo, spazio, affidabilità).
4. **Test**: Provare sistematicamente che tutto funzioni in ogni circostanza.

### 🇨🇭 Perché proprio il C++?
- **Espressivo**: Ti permette di tradurre le tue idee in codice in modo diretto.
- **Onnipresente**: È uno standard disponibile su quasi tutti i computer e dispositivi.
- **Formativo**: I concetti che impari qui (memoria, tipi, controllo) sono le fondamenta per *qualsiasi* altro linguaggio futuro.

---

### 🏭 La Fabbrica del Codice: La Compilazione

Il C++ è un linguaggio **compilato**. Il computer non capisce il C++ direttamente; capisce solo istruzioni macchina (zeri e uni). Dobbiamo quindi tradurre il nostro codice. Immagina una catena di montaggio in 4 passaggi:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

rectangle "Codice Sorgente\n(human readable)" as Source {
  [main.cpp]
}

rectangle "Pre-elaboratore\n(Preprocessor)" as Pre {
  note right: Espande gli #include\nRimuove i commenti
}

rectangle "Compilatore\n(Compiler)" as Comp {
  note right: Traduce in Assembly\n(controlla la sintassi!)
}

rectangle "Assemblatore\n(Assembler)" as Asm {
  note right: Traduce in Codice\nMacchina (file .o)
}

rectangle "Linker\n(Linker)" as Link {
  note right: Unisce i file .o\ne le librerie esterne
}

rectangle "Eseguibile\n(machine code)" as Exe {
  [a.out / main.exe]
}

Source --> Pre : 1. cpp
Pre --> Comp : 2. codice pulito
Comp --> Asm : 3. codice assembly (.s)
Asm --> Link : 4. file oggetto (.o)
Link --> Exe : 5. eseguibile finale
@enduml
```
*💡 Brain Friendly Tip: Il compilatore è un controllore pedante, non un indovino. Se dimentichi un punto e virgola, lui si ferma e ti fa la multa (errore di compilazione), non cerca di "indovinare" cosa volevi dire!*

---

### 🔬 PRIMM: Il Programma Più Piccolo Possibile

Il nostro obiettivo ora non è fare qualcosa di utile, ma **sperimentare la catena di montaggio**. Vogliamo vedere con i nostri occhi gli artefatti intermedi.

#### 1. PREDICT (Prevedi)
? Guarda questo codice. Secondo te, cosa succederà se proviamo a compilarlo ed eseguirlo?
- [ ] Darà un errore perché manca `#include <iostream>`
- [x] Si compilerà silenziosamente e non stamperà nulla a video
- [ ] Stamperà "Hello World" automaticamente

```cpp
// file: ridotto.cpp
int main() {}
```
<details>
<summary>🔍 Clicca per la spiegazione</summary>
Ogni programma C++ deve avere <b>esattamente una</b> funzione globale chiamata <code>main</code>. È il punto di ingresso. Le parentesi <code>{}</code> racchiudono il corpo della funzione. Essendo vuoto, non fa nulla e termina immediatamente, restituendo implicitamente 0 al sistema operativo (successo).
</details>

#### 2. RUN (Esegui)
Copia e incolla questi comandi nel tuo terminale (o nell'ambiente di sviluppo). Stiamo chiedendo al compilatore (`g++`) di **salvare le tappe intermedie** (`-save-temps`) invece di cancellarle.

```bash
# 1. Compila salvando i file temporanei
g++ -save-temps -fverbose-asm -O0 ridotto.cpp -o ridotto

# 2. Lista i file generati
ls
```
**Output atteso:**
```text
ridotto  ridotto.cpp  ridotto.ii  ridotto.o  ridotto.s
```

#### 3. INVESTIGATE (Investiga)
Osserviamo cosa ha prodotto la "fabbrica".

? Quale di questi file contiene il codice dopo che il **Pre-elaboratore** ha rimosso i commenti e espanso le direttive?
- [ ] `ridotto.o`
- [x] `ridotto.ii`
- [ ] `ridotto.s`

Se esegui `cat ridotto.ii`, vedrai il tuo codice originale, ma con l'aggiunta di alcune righe di sistema (le "dichiarazioni d'obbligo" del compilatore).
Se esegui `cat ridotto.s`, vedrai il linguaggio **Assembly**, il ponte tra il C++ leggibile e il codice macchina. Noterai istruzioni come `pushq %rbp` e `movl $0, %eax` (che significa proprio "prepara il valore di ritorno 0").

#### 4. MODIFY (Modifica)
Modifichiamo il nostro programma minimo per vedere come cambia la catena di montaggio.

1. Apri `ridotto.cpp`.
2. Cambia il codice in:
   ```cpp
   int main() {
       return 42;
   }
   ```
3. Ricompila con lo stesso comando: `g++ -save-temps -O0 ridotto.cpp -o ridotto`
4. Esegui `cat ridotto.s` e cerca la riga che contiene `movl`.

? Cosa è cambiato nell'istruzione Assembly rispetto a prima?
- [ ] È scomparsa l'istruzione `movl`
- [x] Il valore è cambiato da `$0` a `$42`
- [ ] Il file `.s` è diventato molto più grande

<details>
<summary>💡 Perché è importante?</summary>
Hai appena visto con i tuoi occhi come un'istruzione C++ ad alto livello (<code>return 42;</code>) si traduce in una specifica istruzione macchina (<code>movl $42, %eax</code>). Il compilatore non fa magia, fa traduzione!
</details>

#### 5. MAKE (Crea)
Ora tocca a te. Crea un nuovo file chiamato `saluto.cpp`.
1. Scrivi il programma minimo `int main() {}`.
2. Aggiungi una riga per stampare "Ciao, Mondo!" usando `#include <iostream>` e `std::cout`. *(Suggerimento: guarda l'esempio qui sotto se sei bloccato)*.
3. Compilalo ed eseguilo.

```cpp
// Esempio di riferimento (non copiare subito, prova prima tu!)

int main() {
    // Stampa "Ciao, Mondo!" e va a capo con \n
    std::cout << "Ciao, Mondo!\n";
    return 0; // 0 = successo per il sistema operativo
}
```
@LIA.cpp

---
### 📝 Riepilogo "Tascabile"
- Un programma C++ parte **sempre** dalla funzione `int main()`.
- Il valore `return 0;` dice al sistema operativo: "Tutto ok, nessuna errore".
- La compilazione ha 4 fasi: **Pre-processing** → **Compiling** → **Assembling** → **Linking**.
- Il codice è scritto per **due lettori**: il computer (che lo esegue) e l'essere umano (che lo deve leggere e mantenere). Usa i commenti `//` per parlare con l'umano!

> **Sfida per la prossima volta:** Cosa succede se dimentichiamo il punto e virgola `;` dopo `std::cout << "Ciao"`? Provaci e porta l'errore in classe!

