# Skills di progetto — Ci Più Più

Questa cartella contiene le **skill** che gli agenti AI (Claude Code, Copilot, Cursor, Gemini CLI, Grok, ecc.) caricano automaticamente per produrre contenuto corretto.

## Skill installate

| Cartella | Origine | Ruolo |
|----------|---------|--------|
| `liascript-syntax/` | [LiaScript/skills](https://github.com/LiaScript/skills) | Riferimento completo di sintassi LiaScript (quiz, effetti, code block, TTS, …). **Obbligatoria** per generare Markdown valido. |
| `liascript-skill/` | [LiaScript/LiaSkill](https://github.com/LiaScript/LiaSkill) | Skill generale per creare corsi interattivi LiaScript da descrizioni in linguaggio naturale. |

## Skill pedagogica di dominio

Oltre a queste skill tecniche, il progetto ha:

- **`SKILLS.md`** (radice del repository) — profilo operativo del docente di Informatica 3ª SIA, metodologie (PRIMM, chunking, Head First), regole C++ e vincoli didattici.
- **`docs/`** — guide operative di progetto:
  - `docs/template_lezione.md`
  - `docs/quiz_liascript.md`
  - `docs/chunking.md`
  - `docs/primm.md`
  - `docs/head_first_style.md`

## Come usarle

### Claude Code / Cursor / Copilot / Gemini CLI
Le cartelle sotto `.agents/skills/` vengono scoperte automaticamente dalla maggior parte degli agenti compatibili con [Agent Skills](https://agentskills.io).

### Installazione / aggiornamento manuale
```bash
# Aggiornare liascript-syntax
npx skills add LiaScript/skills --skill liascript-syntax

# Oppure clonare e copiare
git clone --depth 1 https://github.com/LiaScript/skills.git /tmp/ls-skills
cp -r /tmp/ls-skills/skills/liascript-syntax .agents/skills/
```

### LiaSkill
```bash
git clone --depth 1 https://github.com/LiaScript/LiaSkill.git /tmp/LiaSkill
cp -r /tmp/LiaSkill/liascript-skill .agents/skills/
```

## Ordine di priorità quando si genera contenuto

1. **SKILLS.md** (pedagogia + C++ + stile Head First + PRIMM)
2. **docs/** (template di lezione, sintassi quiz di progetto, chunking, …)
3. **liascript-syntax** (sintassi ufficiale LiaScript)
4. **liascript-skill** (pattern generali di corso interattivo)

Non inventare sintassi quiz o costrutti LiaScript: usa solo quanto documentato in `liascript-syntax` e in `docs/quiz_liascript.md`.
