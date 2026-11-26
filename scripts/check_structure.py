#!/usr/bin/env python3
"""Structural checks for a directory skill folder.
- SKILL.md has frontmatter with name + description (description <= 1024 chars, body < 500 lines)
- every [§N] pointer in AGENT_INDEX.md matches a '## N.' heading in DIRECTORY.md
- every DIRECTORY.md section is pointed to from the index at least once
- evals/questions.json parses and has a token budget
Usage: python3 check_structure.py [folder]   (default: current folder)"""
import json, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
p = lambda f: os.path.join(root, f)
problems = []

skill = open(p("SKILL.md"), encoding="utf-8").read()
fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not fm:
    problems.append("SKILL.md: no frontmatter")
else:
    name = re.search(r"^name:\s*(\S+)", fm.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", fm.group(1), re.M)
    if not name: problems.append("SKILL.md: missing name")
    elif not re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1)): problems.append("SKILL.md: name not lowercase-hyphen")
    if not desc: problems.append("SKILL.md: missing description")
    elif len(desc.group(1)) > 1024: problems.append(f"SKILL.md: description {len(desc.group(1))} chars > 1024")
if skill.count("\n") >= 500: problems.append("SKILL.md: 500+ lines")

index = open(p("AGENT_INDEX.md"), encoding="utf-8").read()
directory = open(p("DIRECTORY.md"), encoding="utf-8").read()
sections = {int(n) for n in re.findall(r"^## (\d+)\.", directory, re.M)}
pointers = {int(n) for n in re.findall(r"§(\d+)", index)}
for n in sorted(pointers - sections): problems.append(f"AGENT_INDEX.md points to §{n}, which DIRECTORY.md lacks")
for n in sorted(sections - pointers - {0}): problems.append(f"DIRECTORY.md section {n} is never pointed to from the index")

spec = json.load(open(p("evals/questions.json"), encoding="utf-8"))
if not spec.get("max_tokens"): problems.append("evals: no max_tokens budget")
held = sum(1 for q in spec["questions"] if q.get("heldout"))

for x in problems: print("FAIL", x)
print(f"{'OK' if not problems else 'PROBLEMS'}: {len(sections)} sections, {len(pointers)} pointers, {len(spec['questions'])} eval questions ({held} held out)")
sys.exit(1 if problems else 0)
