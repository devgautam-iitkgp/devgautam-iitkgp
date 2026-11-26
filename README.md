# Video Craft Directory — AI Narration, AI Visuals, Documentary Scripts, Sound

Branch `video-craft` of devgautam-iitkgp/devgautam-iitkgp. A deep companion to the YouTube growth directory for four production problems:

1. AI narration and text-to-speech: choosing the engine and voice, controlling delivery and emphasis, picking and fixing takes.
2. Flow, Veo and Nano Banana: quirks (rotated stills, references across projects, the sparkle watermark), keeping one style, and making AI art not look AI.
3. Documentary and story scriptwriting.
4. Sound design, music and mixing for long videos.

Researched November 2026, with a source link on every fact.

**Install as a Claude Code skill** (Claude loads it by itself when this kind of work comes up):

```bash
git clone -b video-craft --depth 1 https://github.com/devgautam-iitkgp/devgautam-iitkgp ~/.claude/skills/video-craft
```

One-time per computer: every local Claude Code session (terminal, desktop app, VS Code) then has it. Cloud sessions (claude.ai/code) and Cowork don't load personal skills; there, fetch the index directly: https://raw.githubusercontent.com/devgautam-iitkgp/devgautam-iitkgp/video-craft/AGENT_INDEX.md

| File | What it is |
| --- | --- |
| `SKILL.md` | Skill entry point (tells Claude what to read) |
| `AGENT_INDEX.md` | Compact index (~2.9k tokens), section pointers like [§3] |
| `DIRECTORY.md` | Full directory, sections 0–13 |
| `resources.json` | Every linked source with its section |
| `evals/questions.json` | 42 test questions (10 held out) the index must answer, plus a token budget |
| `scripts/eval_index.py`, `scripts/check_links.py`, `scripts/check_structure.py` | Run the evals; check every link; check the skill's structure |

Quality checks:

```bash
python3 scripts/eval_index.py AGENT_INDEX.md evals/questions.json
python3 scripts/check_links.py resources.json
python3 scripts/check_structure.py
```

Also available as a Claude doc: https://claude.ai/artifact/6GmncC4PDJ8FPVnDmzRp2i

Sister directories: [YouTube growth](https://github.com/devgautam-iitkgp/devgautam-iitkgp/tree/youtube-growth), [Claude automation patterns](https://github.com/devgautam-iitkgp/devgautam-iitkgp/tree/claude-automation) and [Blender + Claude MCP](https://github.com/devgautam-iitkgp/devgautam-iitkgp/tree/blender-claude-mcp).
