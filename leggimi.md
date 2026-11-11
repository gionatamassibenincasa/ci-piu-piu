# Ci Più Più

Appunti sul linguaggio C++ per un corso rivolto a novizi.

## Struttura del repository

```
ci-piu-piu/
├── README.md           # Il file LiaScript (output)
├── preprocess.py       # Il pre-processore che genera l'output
├── chapters/           # I "segmenti" delle lezioni
│   ├── 00_intro.md
│   ├── 01_ciao_mondo.md
│   ├── 02_variabili.md
│   └── ...
├── assets/             # Immagini o risorse esterne se necessarie
├── LICENSE             # La licenza
└── .gitignore
```

## Flusso di lavoro

1. Scelta del "segmento" da sviluppare (es. "chapters/01_ciao_mondo.md").
2. Scrittura del codice Markdown.
3. Salvataggio
4. `python3 preprocess.py index.md > README.md`
5. `git add`, `git commit` e `git push`.
6. Torna al passo 1 se non hai finito.


