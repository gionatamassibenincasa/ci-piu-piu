# Lingua italiana e traduzione automatica del browser

## Cosa fa già il corso

- Meta LiaScript `language: it` (header di ogni lezione in `dist/lessons/`).
- Il player LiaScript imposta in genere `lang="it"` sul documento.
- `translateWithGoogle: false` in `course.yaml` disattiva il traduttore **integrato in LiaScript** (menu sperimentale Google nel player), non quello del browser.

## Perché Chrome propone comunque “Traduci in italiano”

Chrome non si basa solo su `lang`. Usa un **rilevatore statistico** sul testo visibile.

Nelle lezioni ci sono molte parole **inglesi “tecniche”** (nomi C++, fasi PRIMM *Predict/Run/…*, API, URL). Il rilevatore può classificare la pagina come inglese anche se la prosa è italiana e `lang="it"` è corretto.

`class="notranslate"` / `translate="no"` sul `<html>` li controlla il **shell** di `liascript.github.io`, non il nostro Markdown sorgente: non possiamo forzarli dal solo header del corso.

## Cosa può fare lo studente (workaround)

1. Quando compare il banner: **Mai tradurre questo sito** (o “Never translate”).
2. In Chrome → Impostazioni → Lingue: non aggiungere la traduzione automatica dall’inglese, oppure escludere il sito.
3. Preferire la lettura senza traduzione automatica attiva a livello profilo.

## Cosa non promettiamo

Nessuna patch al solo repository del corso **garantisce** l’assenza del banner Chrome su ogni dispositivo. È un comportamento del browser + shell LiaScript.

Se in futuro LiaScript espone un meta ufficiale tipo `notranslate` a livello documento, andrà aggiunto in `format_liascript_header` / `course.yaml`.
