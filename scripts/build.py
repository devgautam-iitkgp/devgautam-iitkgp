"""Build AGENT_INDEX.md, DIRECTORY.md and README.md from resources.json."""
import json, sys, pathlib

src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
d = json.loads(src.read_text())
cats, res, checked = d["categories"], d["resources"], d["checked"]

def esc(s):
    return s.replace("|", "\\|")

# ---- Agent index: one line per resource, compact ----
lines = [
    "# Blender + Claude MCP: agent index",
    "",
    f"Checked {checked}. Read this first. One line per resource: `name | url | stars | short note`. "
    "`*` = page opened on check date; others from search or listing sites. "
    "Star counts drift; re-check before quoting. Full tables: DIRECTORY.md.",
    "",
    "## Decide",
    "- Official Blender Lab connector: analysis, cleanup, batch scripts, node explanations. Blender 5.1+. Claude Desktop or Claude Code only.",
    "- Community mcp-for-blender: build scenes, asset libraries, AI 3D generation. Blender 3.0+.",
    "- Add a skill pack: arjun988 (community server) for game assets; ra100 (official server) for bpy depth.",
    "- Rules: one add-on at a time (port 9876). Never claude.ai web. Work on .blend copies (arbitrary Python).",
    "",
    "## Start here (stop reading if this answers you)",
    "1. Official setup: https://academy.claude.com/tutorials/using-the-blender-connector-in-claude",
    "2. Official add-on: https://www.blender.org/lab/mcp-server/",
    "3. Community server: https://github.com/ahujasid/mcp-for-blender  (`claude mcp add blender uvx mcp-for-blender`)",
    "   Official server in Claude Code: `claude mcp add blender -- uvx --from \"git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp\" blender-mcp`",
    "4. Biggest skill pack: https://github.com/arjun988/blender-skills  (needs community server)",
    "5. Skills for official server: https://github.com/ra100/blender-claude-plugin",
    "6. Best tested comparison: https://www.meltflexai.com/blog/connect-claude-to-blender",
    "7. Honest limits: https://www.mindstudio.ai/blog/claude-blender-mcp-real-world-performance",
    "8. Best video (official + Claude Code): https://www.youtube.com/watch?v=b5F-yNG4lds",
    "9. Research baseline: https://arxiv.org/abs/2504.01786 (BlenderGym)",
    "10. Fixes: see Top fixes at the end of this file",
    "",
]
INDEX_SKIP = {"news"}
for key, title in cats.items():
    items = [r for r in res if r["cat"] == key]
    if not items or key in INDEX_SKIP:
        continue
    lines.append(f"## {title}")
    for r in items:
        star = "*" if r.get("v") == "v" else ""
        stars = f" | {r['stars']}★" if r.get("stars") else ""
        note = r["note"]
        if len(note) > 140:
            cut = note[:140].rsplit(" ", 1)[0]
            note = cut.rstrip(".,;:") + "…"
        lines.append(f"- {r['name']}{star} | {r['url']}{stars} | {note}")
    lines.append("")
lines.append("## Top fixes")
lines += [f"- {f}" for f in d["fixes"]]
lines.append("")
(out / "AGENT_INDEX.generated.md").write_text("\n".join(lines))  # AGENT_INDEX.md is hand-condensed from this

# ---- Full directory: one table per category ----
full = [
    "# Blender + Claude MCP: full directory",
    "",
    f"Checked {checked}. Verified = page opened that day. Stars from the live GitHub page when verified. AI agents: use AGENT_INDEX.md (or the doc's Agent index tab) instead; it is shorter.",
    "",
    "## Quick pick",
    "",
    "- **Official Blender Lab connector**: scene analysis, cleanup, batch scripts, explaining node setups. Free, Blender 5.1+, installs from Claude Desktop.",
    "- **Community MCP for Blender**: building scenes from prompts, Poly Haven/Sketchfab assets, AI 3D generation, Blender 3.0+.",
    "- **Fully local models**: blender-open-mcp. **No MCP at all**: Claude Code + `blender --background --python script.py`.",
    "- **Add a skill pack**: arjun988/blender-skills (community server, game assets) or ra100/blender-claude-plugin (official server).",
    "- Every option: one Blender MCP add-on at a time (port 9876); Claude Desktop or Claude Code only, never claude.ai web; work on copies, since all of them can run arbitrary Python.",
    "",
]
full += [
    "## Automate Blender with Claude (patterns)",
    "",
    "General automation patterns (headless runs, hooks, loops, scheduling, evals, guardrails) live in the sister directory: https://raw.githubusercontent.com/devgautam-iitkgp/devgautam-iitkgp/claude-automation/AGENT_INDEX.md. Applied to Blender:",
    "",
    "- **Live or headless.** MCP drives an open Blender through the add-on (port 9876): good for interactive scene work. For batch jobs and anything unattended, skip MCP: Claude writes a bpy script and runs `blender -b copy.blend --python-exit-code 1 -P job.py -- <your args>`. `--python-exit-code 1` makes a Python error exit non-zero, so a script or loop can catch it; arguments after `--` reach the script through `sys.argv`.",
    "- **Render from the command line.** `-o //renders/frame_#### -f 1` renders one frame (`//` = relative to the .blend); `-a` renders the whole animation.",
    "- **Let Claude check its own work.** Render a small preview PNG (or use the community server's viewport screenshot tool), have Claude read the image and judge it against the brief, and loop until it passes: the evaluator-optimizer pattern. BlenderGym found models weaker at verifying than generating, so give the judge concrete criteria (object count, camera framing, material names).",
    "- **Run it unattended.** `claude -p \"<job>\" --allowedTools \"Bash(blender -b *),Read,Write\"` from cron or a Desktop scheduled task when Blender is on your machine. Cloud scheduled tasks and GitHub Actions work only if the runner installs Blender first.",
    "- **Guardrails.** Work on copies of .blend files; keep outputs in git or versioned folders; use the ready PreToolUse hook in this repo, `hooks/block_unsafe_blender_python.py` (matcher `mcp__blender__.*`): it exits 2, blocking the call, when Blender code imports os, subprocess, shutil or socket, calls exec or eval, or opens a file for writing. The settings snippet is in its header; `sh hooks/test_hook.sh` runs its tests. It is a tripwire, not a sandbox.",
    "- **Make it reusable.** Once a prompt plus script works, save it as a skill (`~/.claude/skills/<name>/SKILL.md`) so `/name` reruns it.",
    "",
]
for key, title in cats.items():
    items = [r for r in res if r["cat"] == key]
    if not items:
        continue
    full.append(f"## {title}")
    full.append("")
    has_stars = any("stars" in r for r in items)
    if has_stars:
        full.append("| Name | Stars | Notes | Verified |")
        full.append("| --- | --- | --- | --- |")
    else:
        full.append("| Name | Notes | Verified |")
        full.append("| --- | --- | --- |")
    for r in items:
        name = f"[{esc(r['name'])}]({r['url']})"
        ver = "yes" if r.get("v") == "v" else "no"
        if has_stars:
            full.append(f"| {name} | {r.get('stars','-')} | {esc(r['note'])} | {ver} |")
        else:
            full.append(f"| {name} | {esc(r['note'])} | {ver} |")
    full.append("")
full.append("## Troubleshooting")
full.append("")
full += [f"{i}. {f}" for i, f in enumerate(d["fixes"], 1)]
full.append("")
full.append("## Coverage and limits")
full.append("")
full.append("Swept: web search, GitHub pages, skills.sh, claudepluginhub, claudemarketplaces, skillsdirectory, skillsllm, glama, mcp.so, mcpservers.org, arXiv, NVD, Blender devtalk, BlenderArtists, Polycount, Qiita, Zenn, CSDN, YouTube and X (site-limited search). "
            "Not reachable: Reddit (blocked for Claude tools), Discord (login), GitHub API (not enabled in the building session). "
            f"A GitHub search for \"blender mcp\" returned 1,132 repos in Oct 2026; only notable ones are listed.")
full.append("")
(out / "DIRECTORY.md").write_text("\n".join(full))

# ---- README ----
n = len(res)
readme = f"""# Blender + Claude MCP resource directory

A checked list of {n} resources for driving Blender with Claude (and other MCP clients): the official connector, community servers, skill packs, videos, articles, research papers, community threads and security notes.

- **AI agents:** read [AGENT_INDEX.md](AGENT_INDEX.md) first (compact, one line per resource). Machine-readable: [resources.json](resources.json).
- **People:** browse [DIRECTORY.md](DIRECTORY.md).
- **Install as a Claude Code skill** (loads by itself when Blender comes up): `git clone -b blender-claude-mcp --depth 1 https://github.com/devgautam-iitkgp/devgautam-iitkgp ~/.claude/skills/blender-claude-mcp` (update later with `git -C ~/.claude/skills/blender-claude-mcp pull`). One-time per computer: every local session loads it. Cloud sessions (claude.ai/code) and Cowork do not load personal skills; there, fetch the raw AGENT_INDEX.md link instead.
- **Quality checks:** `python3 scripts/eval_index.py AGENT_INDEX.md evals/questions.json` (does the index answer real questions?) and `python3 scripts/check_links.py resources.json` (are links alive?).

Last checked: {checked}. Entries marked verified were opened on that date; others come from search results or listing sites.

To update: edit `resources.json`, run `python scripts/build.py resources.json .` (rebuilds DIRECTORY.md and README.md), then mirror any changes into the hand-condensed AGENT_INDEX.md.
"""
(out / "README.md").write_text(readme)
print(n, "resources;", len((out / "AGENT_INDEX.md").read_text()), "chars index")
