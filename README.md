# How to Automate with Claude — Patterns Directory

Branch `claude-automation` of devgautam-iitkgp/devgautam-iitkgp. A directory of **how** Claude automates work (routes, building blocks, patterns, packaging, guardrails, self-improving agents), with real cases as examples. Researched 2026-11-23, updated 2026-11-24.

**Install as a Claude Code skill** (Claude loads it by itself when automation comes up):

```bash
git clone -b claude-automation --depth 1 https://github.com/devgautam-iitkgp/devgautam-iitkgp ~/.claude/skills/claude-automation-patterns
```

One-time per computer: every local Claude Code session (terminal, desktop app, VS Code) then has it. Cloud sessions (claude.ai/code) and Cowork don't load personal skills; there, fetch the index directly: https://raw.githubusercontent.com/devgautam-iitkgp/devgautam-iitkgp/claude-automation/AGENT_INDEX.md

| File | What it is |
| --- | --- |
| `SKILL.md` | Skill entry point (tells Claude what to read) |
| `AGENT_INDEX.md` | Compact index (~2.4k tokens), section pointers like [§3] |
| `DIRECTORY.md` | Full directory, sections 0–11 |
| `resources.json` | Every linked source with its section |
| `evals/questions.json` | 33 test questions (10 held out) the index must answer, plus a token budget |
| `scripts/eval_index.py`, `scripts/check_links.py` | Run the evals; check every link |

Quality checks: `python3 scripts/eval_index.py AGENT_INDEX.md evals/questions.json` and `python3 scripts/check_links.py resources.json`.

Also available as a Claude doc: https://claude.ai/artifact/H6idk1MoA39ynYkapdgwUz
