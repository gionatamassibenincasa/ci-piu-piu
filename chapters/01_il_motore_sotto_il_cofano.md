## ⚙️ Capitolo: Il Motore Sotto il Cofano

> "La programmazione è l'arte di esprimere soluzioni ai problemi in modo che un computer possa eseguirle."
> — *Bjarne Stroustrup*

Hai appena allestito l’officina (VS Code + g++).  
Ora apriamo il cofano e guardiamo **cosa succede davvero** quando premi il pulsante di compilazione.

Il computer non capisce il C++. Capisce solo istruzioni macchina (sequenze di 0 e 1).  
Tra il file che scrivi tu (`.cpp`) e il programma che gira (`.exe`) c’è una **catena di montaggio** con quattro stazioni.

> 💡 **Metafora:**  
> Pensa a una **fabbrica di auto**.  
> - Il progetto su carta = il tuo file `.cpp`  
> - I reparti della fabbrica = pre-elaboratore, compilatore, assemblatore, linker  
> - L’auto finita che esce dal cancello = il file eseguibile  
> Ogni reparto fa un lavoro preciso. Se un pezzo è sbagliato, la catena si ferma e ti arriva una “multa” (errore di compilazione).

---

### 🎯 Obiettivo di questo chunk
Alla fine di questa lezione sei in grado di:
- Descrivere le quattro fasi della compilazione C++ e il ruolo di ciascuna
- Usare `g++ -save-temps` per generare e ispezionare i file intermedi (`.ii`, `.s`, `.o`)
- Collegare una riga di C++ semplice al corrispondente frammento Assembly

---

### 🏭 La fabbrica del codice — le quattro stazioni

```text @plantUML
@startuml
skinparam monochrome true
skinparam shadowing false

rectangle "1. Codice sorgente\n(.cpp)" as Source
rectangle "2. Pre-elaboratore\n(.ii)" as Pre
rectangle "3. Compilatore\n(.s Assembly)" as Comp
rectangle "4. Assemblatore\n(.o oggetto)" as Asm
rectangle "5. Linker\n(.exe eseguibile)" as Link

Source --> Pre : espande #include\nrimuove commenti
Pre --> Comp : controlla sintassi\ntraduce in Assembly
Comp --> Asm : traduce in\ncodice macchina
Asm --> Link : unisce librerie\nproduce l'eseguibile
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
/**
 * @file ridotto.cpp
 * @brief Programma minimo per ispezionare la catena di compilazione.
 */
int main() {
    return 0;   /// dice al sistema operativo: "tutto ok"
}
```

#### 1. PREDICT (Prevedi)
Prima di compilare, rispondi:

Se compiliamo questo programma con `g++ -save-temps`, quale file conterrà il codice **dopo** che il pre-elaboratore ha rimosso i commenti?

[( )] `ridotto.o`
[(X)] `ridotto.ii`
[( )] `ridotto.s`
[( )] `ridotto.exe`

#### 2. RUN (Esegui)
Nella cartella del progetto digita:

```bat
g++ -save-temps -O0 ridotto.cpp -o ridotto.exe
```

Il flag `-save-temps` dice a g++: “non cancellare i file intermedi”.  
`-O0` disattiva le ottimizzazioni, così l’Assembly resta più leggibile.

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

| File | Cosa ci trovi | Cosa osservare |
|------|----------------|----------------|
| `ridotto.ii` | Codice “pulito” dopo il pre-elaboratore | I commenti sono spariti; possono comparire righe di sistema |
| `ridotto.s` | Assembly | Cerca una riga con `movl` o `mov` e il numero `0` |
| `ridotto.o` | Codice macchina (binario) | Non è leggibile come testo |
| `ridotto.exe` | Eseguibile finale | È il prodotto finito della fabbrica |

Nel file `.s` noterai istruzioni del tipo:
```asm
movl $0, %eax
```
Che, in pratica, prepara il valore di ritorno `0` (successo).

#### 4. MODIFY (Modifica)
1. Cambia il programma in:
   ```cpp
   int main() {
       return 42;
   }
   ```
2. Ricompila con lo stesso comando:
   ```bat
   g++ -save-temps -O0 ridotto.cpp -o ridotto.exe
   ```
3. Riapri `ridotto.s` e cerca di nuovo l’istruzione `movl` / `mov`.

Cosa è cambiato?

[( )] È scomparsa l’istruzione di movimento
[(X)] Il valore letterale è passato da `$0` a `$42`
[( )] Il file `.s` è diventato molto più grande
[( )] Non viene più generato il file `.s`

<details>
<summary>💡 Perché è importante?</summary>
Hai visto con i tuoi occhi la traduzione: una riga C++ ad alto livello (<code>return 42;</code>) diventa una precisa istruzione Assembly. Il compilatore non fa magia: fa <strong>traduzione</strong>.
</details>

Esegui di nuovo il programma e controlla il codice di uscita:

```bat
ridotto.exe
echo %ERRORLEVEL%
```

Dovresti vedere `42`.

#### 5. MAKE (Crea)
Crea un nuovo file `codice_uscita.cpp` che:
1. Contiene solo la funzione `main`
2. Restituisce un numero a tua scelta tra 1 e 99 (diverso da 0 e da 42)
3. Viene compilato con `-save-temps`
4. Ti permette di verificare, aprendo il `.s`, che il numero scelto compaia nell’Assembly
5. Mostra lo stesso numero con `echo %ERRORLEVEL%` dopo l’esecuzione

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

---

<!-- 
  NOTE PER L'AUTORE / LLM
  [x] Un solo obiettivo principale: capire la catena di compilazione
  [x] Metafora fabbrica / catena di montaggio
  [x] Quiz con sintassi LiaScript corretta
  [x] PRIMM completo su programma minimo SENZA iostream
  [x] Nessuna sovrapposizione con Ciao Mondo (niente cout nel Make)
  [x] -save-temps e ispezione .ii / .s
  [x] Collegamento esplicito return N → movl $N
  [x] Riepilogo tascabile e ponte al capitolo successivo
-->
