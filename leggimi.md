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
│   ├── 01_il_motore_sotto_il_cofano.md
│   ├── 02_ciao_mondo.md
│   ├── 03_variabili_costanti_tipi.md
│   ├── 04_espressioni_e_operatore_ternario.md
│   ├── 05_bivi_semplici_if_else.md
│   ├── 06_bivi_complessi_e_regole_if.md
│   ├── 07_selezione_multipla_switch.md
│   ├── 08_ciclo_while.md
│   ├── 09_ciclo_for.md
│   ├── 10_ciclo_do_while.md
│   ├── 11_controllo_cicli_e_formattazione.md
│   └── ...
├── assets/             # Immagini o risorse esterne (se necessarie)
├── SKILLS.md           # Profilo docente, metodologie didattiche (PRIMM) e regole di stile
├── leggimi.md          # Guida al repository e flusso di lavoro per i contributori
├── LICENSE             # La licenza del progetto
└── .gitignore
```

## Flusso di lavoro

1. **Scelta o creazione del segmento**: crea o modifica un file in `chapters/` (es. `chapters/02_ciao_mondo.md`), seguendo le metodologie didattiche (PRIMM, metafore "Head First", commenti Doxygen) definite in [SKILLS.md](SKILLS.md).
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
