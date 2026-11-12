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
│   ├── template_lezione.md
│   ├── quiz_liascript.md
│   ├── chunking.md
│   ├── primm.md
│   └── head_first_style.md
├── .agents/skills/     # Skill ufficiali per agenti AI
│   ├── README.md
│   ├── liascript-syntax/   # Sintassi ufficiale LiaScript
│   └── liascript-skill/    # LiaSkill — generazione corsi interattivi
├── assets/             # Immagini o risorse esterne (se necessarie)
├── SKILLS.md           # Profilo docente + gerarchia skill + regole di stile
├── leggimi.md          # Guida al repository e flusso di lavoro
├── LICENSE
└── .gitignore
```

## Flusso di lavoro

1. **Scelta o creazione del segmento**: parti sempre da `docs/template_lezione.md`. Copialo in `chapters/XX_nome.md` e sostituisci i placeholder.  
   Rispetta, in ordine:
   - [SKILLS.md](SKILLS.md) (pedagogia + C++ + gerarchia skill)
   - [docs/](docs/) (template, quiz, chunking, PRIMM, Head First)
   - `.agents/skills/liascript-syntax/` (sintassi ufficiale LiaScript)
   - `.agents/skills/liascript-skill/` (pattern di corso interattivo)
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
