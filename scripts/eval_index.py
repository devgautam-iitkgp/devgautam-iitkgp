#!/usr/bin/env python3
"""Code grader for an AGENT_INDEX.md: each question passes only if every
required pattern group matches somewhere in the index (case-insensitive).
Usage: python3 eval_index.py AGENT_INDEX.md evals/questions.json"""
import json, re, sys
index = open(sys.argv[1], encoding="utf-8").read()
spec = json.load(open(sys.argv[2], encoding="utf-8"))
qs = spec["questions"]
budget = spec.get("max_tokens")
passed = 0
for q in qs:
    miss = [g for g in q["must_match"] if not re.search(g, index, re.I)]
    ok = not miss
    passed += ok
    print(("PASS " if ok else "FAIL ") + q["id"] + "  " + q["q"] + ("" if ok else "   missing: " + " | ".join(miss)))
tokens = len(index) // 4
over = budget and tokens > budget
print(f"\nscore {passed}/{len(qs)}  index ~{tokens} tokens" + (f"  OVER BUDGET ({budget})" if over else (f" (budget {budget})" if budget else "")))
sys.exit(0 if passed == len(qs) and not over else 1)
