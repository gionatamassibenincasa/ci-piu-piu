# Sintassi Quiz LiaScript — Riferimento rapido

Usare **solo** queste forme. La vecchia notazione `? domanda` + `- [ ]` / `- [x]` **non** genera quiz interattivi in LiaScript.

## 1. Single-choice (una sola risposta corretta)

```markdown
Quale operatore si usa per l'output a video?

[( )] `std::cin`
[(X)] `std::cout`
[( )] `std::endl`
[( )] `printf`
```

- `(X)` o `(x)` = risposta corretta  
- `( )` = risposta sbagliata  
- Solo **una** riga può contenere la X.

## 2. Multiple-choice (una o più risposte corrette)

```markdown
Quali di questi sono tipi fondamentali in C++?

[[X]] `int`
[[X]] `double`
[[ ]] `string`   (in realtà è `std::string`, non un tipo built-in puro)
[[ ]] `array`
```

- `[[X]]` = corretta  
- `[[ ]]` = sbagliata  

## 3. Text input (risposta libera)

```markdown
Come si chiama la funzione da cui parte ogni programma C++?

[[main]]
```

La soluzione è case-sensitive. Si possono aggiungere alternative con `|` se necessario (verificare documentazione corrente).

## 4. Selection / Dropdown (inline)

```markdown
Per dichiarare una variabile intera si scrive [[ (int) | float | char | bool ]] nome;
```

L'opzione corretta è avvolta da parentesi tonde `(...)`.

## 5. Matrix (tabella di scelte)

```markdown
[[ Tipo         | Usato per numeri interi | Usato per decimali | Usato per testo ]]
[[ `int`        | (X)                     | ( )                | ( )              ]]
[[ `double`     | ( )                     | (X)                | ( )              ]]
[[ `std::string`| ( )                     | ( )                | (X)              ]]
```

## Buone pratiche

- Metti **sempre** una riga vuota prima e dopo il blocco quiz.
- La domanda va **sopra** le opzioni, non dentro.
- Preferisci single-choice per le fasi PREDICT (riduce carico cognitivo).
- Usa multiple-choice quando vuoi far emergere concetti correlati.
- Aggiungi un hint o una spiegazione dopo il quiz con `<details>` se utile:

```markdown
<details>
<summary>💡 Spiegazione</summary>
Testo della spiegazione...
</details>
```

## Cosa evitare

| Forma sbagliata (non funziona come quiz) | Forma corretta                  |
|------------------------------------------|---------------------------------|
| `? Domanda`<br>`- [ ] a`<br>`- [x] b`    | `[( )] a`<br>`[(X)] b`          |
| Checkbox Markdown generici               | Sintassi a doppie parentesi     |
| Quiz senza riga vuota intorno            | Sempre riga vuota prima/dopo    |

Riferimento ufficiale: [LiaScript Documentation – Quizzes](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#quizzes)
