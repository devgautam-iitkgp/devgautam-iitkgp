#!/usr/bin/env python3
"""PreToolUse hook: block Blender MCP code that reaches outside Blender.
Reads the hook JSON on stdin, scans every string in tool_input for risky
imports/calls, and exits 2 (block, reason on stderr) if it finds one.
Wire it up in ~/.claude/settings.json or .claude/settings.json:
  {"hooks": {"PreToolUse": [{"matcher": "mcp__blender__.*",
    "hooks": [{"type": "command",
      "command": "python3 ~/.claude/skills/blender-claude-mcp/hooks/block_unsafe_blender_python.py"}]}]}}
Edit RISKY to fit your work. It is a tripwire, not a sandbox: also work on .blend copies."""
import json, re, sys

RISKY = [
    r"\bimport\s+[\w\s,.]*?\b(os|subprocess|shutil|socket|ctypes|urllib|requests)\b",  # also 'import bpy, os'
    r"\b(os|subprocess|shutil|socket)\.\w+\s*\(",  # os.remove(...), subprocess.run(...)
    r"\bfrom\s+(os|subprocess|shutil|socket|ctypes|urllib|requests)\b",
    r"__import__\s*\(", r"\beval\s*\(", r"\bexec\s*\(",
    r"\bopen\s*\([^)]*['\"][wa]",              # writing files
    r"bpy\.ops\.wm\.(quit_blender|save_as_mainfile)\b",
]

def strings(x):
    if isinstance(x, str): yield x
    elif isinstance(x, dict):
        for v in x.values(): yield from strings(v)
    elif isinstance(x, list):
        for v in x: yield from strings(v)

event = json.load(sys.stdin)
for s in strings(event.get("tool_input", {})):
    for pat in RISKY:
        m = re.search(pat, s)
        if m:
            print(f"Blocked by block_unsafe_blender_python.py: '{m.group(0)}' is not allowed in Blender code. "
                  "Do it with bpy only, or ask the user to approve running it by hand.", file=sys.stderr)
            sys.exit(2)
sys.exit(0)
