---
activity_id: doxygen-funzioni-01
title: "Il manuale dei reparti: documentare le funzioni con Doxygen"
methodology: convention
order: 20
version: "2026-11-28"
language: it
components: {}
files: []
---

## 📚 Il manuale dei reparti: documentare le funzioni con Doxygen

Hai già imparato a dividere un programma in funzioni. Ora aggiungi una
descrizione che renda ogni funzione comprensibile anche fuori dal file in cui
è stata scritta.

> 💡 **Metafora:** Una funzione è un reparto specializzato. La documentazione
> Doxygen è la scheda appesa all'ingresso: spiega il lavoro del reparto, i dati
> che riceve e il risultato che consegna.

Questa scheda serve a due persone: ai **futuri lettori** del codice e agli
**editor**. VS Code, tramite IntelliSense e le estensioni C++, può mostrare
`@brief`, `@param` e `@return` quando passi sopra una funzione o la richiami.
Una documentazione precisa diventa quindi parte dell'aiuto che l'editor ti
offre mentre scrivi.

### 🎯 Obiettivi

Alla fine sai:

- documentare una funzione con `@brief`, `@param` e `@return`;
- associare ogni `@param` al nome e al significato corretto;
- descrivere il valore prodotto da `return`;
- scrivere una scheda utile sia a un lettore sia all'editor.

### 📋 La scheda di una funzione

| Tag | Domanda a cui risponde | Esempio |
|---|---|---|
| `@brief` | Qual è lo scopo? | `Calcola il totale ivato.` |
| `@param` | Che dato entra? | `@param imponibile Importo netto in euro.` |
| `@return` | Che dato esce? | `@return double Totale lordo.` |

Il nome dopo `@param` deve coincidere con il parametro del codice. Non
documentare un parametro inesistente: confonde il lettore e può produrre
informazioni sbagliate nell'editor.

### ✅ Esempio completo

```cpp
/**
 * @brief Calcola il totale ivato di una transazione.
 * @param imponibile Importo netto della merce in euro.
 * @return double Totale lordo comprensivo di IVA al 22%.
 */
double calcolaTotaleIvato(double imponibile) {
    /// Aliquota ordinaria usata dal listino aziendale.
    const double aliquotaIva = 0.22;
    return imponibile * (1.0 + aliquotaIva);
}
```

Quando richiami `calcolaTotaleIvato(100.0)`, l'editor può mostrarti la firma e
la descrizione senza obbligarti a tornare al punto in cui la funzione è stata
definita. Il commento non cambia l'esecuzione, ma migliora il contesto mentre
programmi.

### 🔍 Funzioni con più parametri

Documenta ogni parametro su una riga separata:

```cpp
/**
 * @brief Calcola il valore netto dopo uno sconto percentuale.
 * @param prezzo Prezzo iniziale in euro.
 * @param percentuale Percentuale di sconto compresa tra 0 e 100.
 * @return double Prezzo dopo lo sconto.
 */
double applicaSconto(double prezzo, double percentuale) {
    return prezzo * (1.0 - percentuale / 100.0);
}
```

La descrizione deve chiarire unità di misura, significato aziendale e vincoli
utili. Non basta riscrivere il tipo: “`double percentuale`” non dice quanto
vale né come viene usato.

### 🧭 Checklist prima di consegnare

- [ ] `@brief` descrive un solo lavoro della funzione.
- [ ] Ogni parametro del codice compare una volta in `@param`.
- [ ] Nessun `@param` cita un nome che non esiste.
- [ ] `@return` indica tipo e significato del risultato.
- [ ] Un eventuale `///` spiega una scelta di business, non la sintassi.
- [ ] Il commento è vicino alla funzione documentata.

### 🧪 Attività di revisione

Completa la documentazione di questa funzione:

```cpp
double calcolaCommissione(double importo, double percentuale) {
    return importo * percentuale / 100.0;
}
```

Scrivi `@brief`, due `@param` e `@return`. Poi controlla nel tuo editor se,
passando sopra il nome della funzione, compare una descrizione leggibile.

<details>
<summary>💡 Controllo finale</summary>

La scheda deve spiegare l'importo in euro, la percentuale applicata e la
commissione restituita. Se il tooltip dell'editor è vuoto, verifica che il
commento sia immediatamente sopra la funzione e che i nomi dei parametri
coincidano.
</details>

### 📝 Riepilogo tascabile

- [ ] `@brief` spiega il lavoro della funzione.
- [ ] `@param` spiega ogni dato in ingresso usando il nome esatto.
- [ ] `@return` spiega il risultato prodotto.
- [ ] Doxygen aiuta sia i lettori futuri sia l'editor durante la scrittura.
- [ ] Una documentazione breve ma precisa è migliore di un commento prolisso.

### ➡️ Prossimo passo

Le tue funzioni ora hanno un contratto leggibile. Nel prossimo capitolo
studierai scope e passaggio dei parametri: la documentazione ti aiuterà a
ricordare quali dati entrano e quale risultato esce.
