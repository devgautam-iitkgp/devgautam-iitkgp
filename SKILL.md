---
name: blender-claude-mcp
description: Checked directory of Blender + Claude resources (official Blender Lab connector, community MCP servers, skill packs, videos, research, security, troubleshooting) and patterns for automating Blender headless. Use when setting up or debugging Blender with Claude, choosing an MCP server or skill pack, or scripting, rendering or batch-processing Blender with Claude.
---

# Blender + Claude directory

1. Read `AGENT_INDEX.md` in this folder first (about 3.4k tokens). Its "Start here" block answers most setup questions; "Automate" covers headless runs; "Top fixes" covers common errors.
2. Open `DIRECTORY.md` only for full notes on one entry, and `resources.json` for machine-readable data.
3. Star counts and versions drift. Before quoting one as current, re-check the linked page.
4. For general automation patterns (hooks, loops, scheduling, evals), the sister skill is `claude-automation-patterns`, or fetch https://raw.githubusercontent.com/devgautam-iitkgp/devgautam-iitkgp/claude-automation/AGENT_INDEX.md

Update this skill: `git -C ~/.claude/skills/blender-claude-mcp pull`
