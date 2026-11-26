# YouTube Growth Directory — Build and Grow a Channel

Branch `youtube-growth` of devgautam-iitkgp/devgautam-iitkgp. Everything a creator, or an AI agent helping one, needs to build and grow a YouTube channel: how recommendations work, ideas, packaging, hooks and retention, production and sound, Shorts, faceless and AI-assisted channels, upload settings, analytics, monetisation, community, policies, and agents with the YouTube APIs. For any creator, anywhere; long-form, Shorts and faceless formats. Researched November 2026, with a source link on every fact.

**Install as a Claude Code skill** (Claude loads it by itself when YouTube work comes up):

```bash
git clone -b youtube-growth --depth 1 https://github.com/devgautam-iitkgp/devgautam-iitkgp ~/.claude/skills/youtube-growth
```

One-time per computer: every local Claude Code session (terminal, desktop app, VS Code) then has it. Cloud sessions (claude.ai/code) and Cowork don't load personal skills; there, fetch the index directly: https://raw.githubusercontent.com/devgautam-iitkgp/devgautam-iitkgp/youtube-growth/AGENT_INDEX.md

| File | What it is |
| --- | --- |
| `SKILL.md` | Skill entry point (tells Claude what to read) |
| `AGENT_INDEX.md` | Compact index (~2.5k tokens), section pointers like [§6] |
| `DIRECTORY.md` | Full directory, sections 0–15 |
| `resources.json` | Every linked source with its section |
| `evals/questions.json` | 38 test questions (10 held out) the index must answer, plus a token budget |
| `scripts/eval_index.py`, `scripts/check_links.py`, `scripts/check_structure.py` | Run the evals; check every link; check the skill's structure |

Quality checks: `python3 scripts/eval_index.py AGENT_INDEX.md evals/questions.json`, `python3 scripts/check_links.py resources.json` and `python3 scripts/check_structure.py`.

Also available as a Claude doc: https://claude.ai/artifact/2Lq8sVePp9rNjqE8Eouva6

Sister directories: [Video craft](https://github.com/devgautam-iitkgp/devgautam-iitkgp/tree/video-craft) (AI narration, AI visuals, documentary scripts, sound), [Claude automation patterns](https://github.com/devgautam-iitkgp/devgautam-iitkgp/tree/claude-automation) and [Blender + Claude MCP](https://github.com/devgautam-iitkgp/devgautam-iitkgp/tree/blender-claude-mcp).

This is a summary of public sources, not legal or financial advice.
