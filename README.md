# Blender + Claude MCP resource directory

A checked list of 96 resources for driving Blender with Claude (and other MCP clients): the official connector, community servers, skill packs, videos, articles, research papers, community threads and security notes.

- **AI agents:** read [AGENT_INDEX.md](AGENT_INDEX.md) first (compact, one line per resource). Machine-readable: [resources.json](resources.json).
- **People:** browse [DIRECTORY.md](DIRECTORY.md).
- **Install as a Claude Code skill** (loads by itself when Blender comes up): `git clone -b blender-claude-mcp --depth 1 https://github.com/devgautam-iitkgp/devgautam-iitkgp ~/.claude/skills/blender-claude-mcp` (update later with `git -C ~/.claude/skills/blender-claude-mcp pull`). One-time per computer: every local session loads it. Cloud sessions (claude.ai/code) and Cowork do not load personal skills; there, fetch the raw AGENT_INDEX.md link instead.
- **Quality checks:** `python3 scripts/eval_index.py AGENT_INDEX.md evals/questions.json` (does the index answer real questions?) and `python3 scripts/check_links.py resources.json` (are links alive?).

Last checked: 2026-11-24. Entries marked verified were opened on that date; others come from search results or listing sites.

To update: edit `resources.json`, run `python scripts/build.py resources.json .` (rebuilds DIRECTORY.md and README.md), then mirror any changes into the hand-condensed AGENT_INDEX.md.
