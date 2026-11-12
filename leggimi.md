# Ci Più Più

Appunti sul linguaggio C++ per un corso rivolto a novizi (studenti di 3ª SIA).

## Struttura del repository

```
ci-piu-piu/
├── index.md            # Entrypoint sorgente con metadati e direttive #include
├── README.md           # File LiaScript assemblato (output finale generato)
├── preprocess.py       # Pre-processore che espande gli #include in README.md
├── chapters/           # I "segmenti" (chunk) delle lezioni
│   ├── 00_guida_allo_studio.md
│   ├── ...
│   └── ...
├── docs/               # Riferimenti metodologici e template (per autori e LLM)
│   ├── template_lezione.md   # Template standard di capitolo
│   ├── quiz_liascript.md     # Sintassi corretta dei quiz LiaScript
│   ├── chunking.md           # Lezioni segmentate e un solo obiettivo
│   ├── primm.md              # Le cinque fasi PRIMM in dettaglio
│   └── head_first_style.md   # Tono, metafore e scenari aziendali
├── assets/             # Immagini o risorse esterne (se necessarie)
├── SKILLS.md           # Profilo docente, metodologie e regole di stile
├── leggimi.md          # Guida al repository e flusso di lavoro per i contributori
├── LICENSE             # La licenza del progetto
└── .gitignore
```

## Flusso di lavoro

1. **Scelta o creazione del segmento**: parti sempre da `docs/template_lezione.md`. Copialo in `chapters/XX_nome.md` e sostituisci i placeholder.  
   Rispetta:
   - [SKILLS.md](SKILLS.md)
   - [docs/chunking.md](docs/chunking.md)
   - [docs/primm.md](docs/primm.md)
   - [docs/head_first_style.md](docs/head_first_style.md)
   - [docs/quiz_liascript.md](docs/quiz_liascript.md)
2. **Inclusione nell'indice**: assicurati che il capitolo sia incluso in `index.md` tramite la direttiva `#include <chapters/nome_file.md>`.
3. **Generazione dell'output**:
   ```bash
   python3 preprocess.py index.md > README.md
   ```
4. **Verifica**: controlla il risultato localmente o aprendolo su LiaScript.
5. **Pubblicazione**:
   ```bash
   git add .
   git commit -m "Descrizione delle modifiche"
   git push
   ```
6. Torna al passo 1 per il modulo successivo.
