#!/usr/bin/env python3
"""Code grader for an AGENT_INDEX.md: each question passes only if every
required pattern group matches somewhere in the index (case-insensitive).
Usage: python3 eval_index.py AGENT_INDEX.md evals/questions.json"""
import json, re, sys
index = open(sys.argv[1], encoding="utf-8").read()
qs = json.load(open(sys.argv[2], encoding="utf-8"))["questions"]
passed = 0
for q in qs:
    miss = [g for g in q["must_match"] if not re.search(g, index, re.I)]
    ok = not miss
    passed += ok
    print(("PASS " if ok else "FAIL ") + q["id"] + "  " + q["q"] + ("" if ok else "   missing: " + " | ".join(miss)))
print(f"\nscore {passed}/{len(qs)}  index ~{len(index)//4} tokens")
