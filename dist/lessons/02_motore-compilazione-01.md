<!--
author:               Gionata Massi
email:                gionata.massi@savoiabenicasa.it
version:              2026-11-12
language:             it
narrator:             IT Italian Male
comment:              Appunti delle lezioni di Informatica - Classi terze ITE SIA - Anno Scolastico 26/27
import:               https://raw.githubusercontent.com/LiaScript/CodeRunner/master/README.md
import:               https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
import:               https://raw.githubusercontent.com/gionata/PythonTutor/main/README.md
-->
[← Prec.](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/01_ambiente-sviluppo-01.md) · [Indice](https://liascript.github.io/course/?https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/index.md) · [Corso](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/README.md) · [Succ. →](https://raw.githubusercontent.com/gionatamassibenincasa/ci-piu-piu/main/dist/lessons/03_ciao-mondo-01.md)

---


## ⚙️ Il Motore Sotto il Cofano: dalla sorgente all'eseguibile

> "La programmazione è l'arte di esprimere soluzioni ai problemi in modo che un computer possa eseguirle."
>
> — Bjarne Stroustrup

Hai appena allestito l’officina (VS Code + g++).  
Ora apriamo il cofano e guardiamo **cosa succede davvero** quando premi il pulsante di compilazione.

Il computer non capisce il C++. Capisce solo istruzioni macchina (sequenze di 0 e 1).  
Tra il file che scrivi tu (`.cpp`) e il programma che gira (`.exe`) c’è una **catena di montaggio** con quattro stazioni.

> 💡 **Metafora:**  
> Pensa a una **fabbrica di auto**.  
> - Il progetto su carta = il tuo file `.cpp`  
> - I reparti della fabbrica = pre-elaboratore, compilatore, assemblatore, linker  
> - L’auto finita che esce dal cancello = il file eseguibile  
> Ogni reparto fa un lavoro preciso. Se un pezzo è sbagliato, la catena si ferma e ti arriva una “notifica” (errore di compilazione).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Seguire il percorso di un programma C++ dal sorgente all'eseguibile e ispezionarne i file intermedi con `g++ -save-temps`

---

### ⚙️ Prima del laboratorio: dal sorgente all'eseguibile

Il percorso essenziale è questo:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center
skinparam ArrowColor #000000
skinparam rectangle {
  BackgroundColor #DDDDDD
  BorderColor #000000
}
top to bottom direction

rectangle "ridotto.cpp\n(codice sorgente)" as SRC
rectangle "Compilatore" as COMP
rectangle "ridotto.o\n(codice oggetto)" as OBJ
rectangle "Linker" as LINK
rectangle "ridotto.exe\n(codice eseguibile)" as EXE

rectangle "codice di libreria" as LIB
rectangle "codice di avvio\n(start-up)" as START

SRC --> COMP
COMP --> OBJ
OBJ --> LINK
LIB --> LINK
START --> LINK
LINK --> EXE

SRC -[hidden]right-> LIB
COMP -[hidden]right-> START
@enduml
```

Il file `.cpp` che scrivi non viene eseguito direttamente: il compilatore e il
linker lo trasformano in un `.exe` pronto per Windows.

---

### 🧭 Prima del laboratorio: le quattro stazioni

Dentro la fase di traduzione ci sono quattro stazioni. Con `g++` le vediamo così:

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam defaultTextAlignment center

rectangle ".cpp\nsorgente" as S
rectangle "Pre-elaboratore\n(.ii)" as P
rectangle "Compilatore\n(.s Assembly)" as C
rectangle "Assemblatore\n(.o oggetto)" as A
rectangle "Linker\n(+ librerie)\n.exe" as L

S -right-> P
P -right-> C
C -right-> A
A -right-> L
@enduml
```

| Stazione | Cosa fa | File tipico |
|----------|---------|-------------|
| **Pre-elaboratore** | Espande le direttive `#include`, rimuove i commenti, gestisce le macro | `.ii` |
| **Compilatore** | Controlla la sintassi e traduce il C++ in **Assembly** (linguaggio a basso livello ma ancora leggibile) | `.s` |
| **Assemblatore** | Traduce l’Assembly in codice macchina (oggetti non ancora eseguibili da soli) | `.o` |
| **Linker** | Unisce i file oggetto con le librerie (es. la parte di sistema che serve per `main`) e produce l’eseguibile finale | `.exe` |

> 💡 **Brain-friendly tip:** Il compilatore è un controllore pedante, non un indovino. Se dimentichi un punto e virgola, si ferma e ti segnala l’errore. Non cerca di “capire cosa volevi dire”.

---

### 🔬 Laboratorio PRIMM: Guarda sotto il cofano

Useremo il programma **più piccolo possibile** (senza ancora stampare nulla).  
Così concentriamo l’attenzione sulla catena di montaggio, non sull’output a video.

```cpp
int main() {
    return 0;
}
```

#### 1. PREDICT (Prevedi)


Dopo g++ -save-temps, quale file contiene il codice senza commenti?

```cpp
int main() { return 0; }
```

[( )] ridotto.o
[(X)] ridotto.ii
[( )] ridotto.exe
[( )] ridotto.s


#### 2. RUN (Esegui)
Prima esegui il programma minimo nel blocco, poi ripeti l'esperimento dal
terminale per lasciare visibili i file intermedi.

```cpp
int main() {
    return 0;
}
```
@LIA.cpp

Nella cartella del progetto digita:

```bat
g++ -save-temps -O0 -fverbose-asm ridotto.cpp -o ridotto.exe
```

Il flag `-save-temps` dice a g++: “non cancellare i file intermedi”.  
`-O0` disattiva le ottimizzazioni, così l’Assembly resta più leggibile.
`-fverbose-asm` annota ogni riga rilevante per mostrare la corrispondenza tra il codice assembly prodotto e quello C++ _sorgente_.


**Controllo:** nella cartella devono comparire almeno:
- `ridotto.ii`
- `ridotto.s`
- `ridotto.o`
- `ridotto.exe`

Prova anche:

```bat
ridotto.exe
echo %ERRORLEVEL%
```

(Su Windows `ERRORLEVEL` mostra il valore restituito da `main`. Dovresti vedere `0`.)

#### 3. INVESTIGATE (Investiga)
Apri i file intermedi con un editor di testo (o con `type ridotto.ii` / `type ridotto.s` nel Prompt).

| File | Cosa ci trovi | Perché è importante |
|------|---------------|---------------------|
| `ridotto.ii` | Codice "pulito" dopo il pre-elaboratore | Vedi cosa resta quando spariscono i commenti |
| `ridotto.s` | Assembly (ancora leggibile) | Colleghi una riga C++ a un'istruzione macchina |
| `ridotto.o` | Codice oggetto (binario) | Non è ancora un programma completo da solo |
| `ridotto.exe` | Eseguibile finale | È il prodotto della fabbrica, pronto da lanciare |

Nel file `.s` noterai istruzioni del tipo:
```asm
movl $0, %eax
```
Che, in pratica, prepara il valore di ritorno `0` (successo).

#### 4. MODIFY (Modifica)
<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
int main() {
    return 0;
}
```

</details>

1. Cambia il programma in:
   ```cpp
   int main() {
       return 42;
   }
   ```
2. Ricompila con lo stesso comando:
   ```bat
   g++ -save-temps -O0 -fverbose-asm ridotto.cpp -o ridotto.exe
   ```
3. Riapri `ridotto.s` e cerca di nuovo l’istruzione `movl` / `mov`.

Cosa è cambiato?

[( )] È scomparsa l’istruzione di movimento
[(X)] Il valore letterale è passato da `$0` a `$42`
[( )] Il file `.s` è diventato molto più grande
[( )] Non viene più generato il file `.s`

<details>
<summary>💡 Spiegazione</summary>
Hai visto con i tuoi occhi la traduzione: una riga C++ ad alto livello (<code>return 42;</code>) diventa una precisa istruzione Assembly. Il compilatore non fa magia: fa <strong>traduzione</strong>.
</details>

Esegui di nuovo il programma e controlla il codice di uscita:

```bat
ridotto.exe
echo %ERRORLEVEL%
```

Dovresti vedere `42`.

#### 5. MAKE (Crea)
**Scenario aziendale:** un programma automatico importa gli ordini notturni.
Non deve ancora stampare nulla, ma deve restituire un codice di esito che un
altro programma possa leggere.

Crea `codice_uscita.cpp` che:
1. Contiene solo `main` e restituisce un codice tra 1 e 99 (diverso da 0 e 42).
2. Usa un commento `///` per spiegare cosa rappresenta il codice scelto.
3. Viene compilato con `-save-temps -fverbose-asm`.
4. Ti permette di verificare nel `.s` il numero scelto.
5. Mostra lo stesso numero con `echo %ERRORLEVEL%` dopo l'esecuzione.

<details>
<summary>💡 Scaffold di partenza</summary>

```cpp
int main() {
    /// TODO: spiega l'esito dell'importazione.
    return 7;
}
```

</details>

**Non** usare ancora `#include <iostream>` né `std::cout`: restiamo concentrati sulla catena di compilazione.  
La stampa a video arriverà nel prossimo capitolo.

---

### 📝 Riepilogo tascabile
- C++ è un linguaggio **compilato**: il sorgente viene tradotto in eseguibile attraverso più stazioni.
- Le quattro fasi: **Pre-elaboratore → Compilatore → Assemblatore → Linker**.
- `g++ -save-temps` lascia i file intermedi (`.ii`, `.s`, `.o`) così puoi ispezionarli.
- `return N;` in `main` diventa, in Assembly, un’istruzione che mette `N` nel registro di ritorno.
- Gli errori di compilazione sono segnalazioni precise della fabbrica: imparare a leggerli è una competenza chiave.

---

### ➡️ Prossimo chunk
Finora il nostro programma non ha ancora *parlato* con noi.  
Nel prossimo capitolo gli daremo il megafono (`std::cout`) e scriveremo il primo vero dialogo: **Ciao, Mondo!**.

