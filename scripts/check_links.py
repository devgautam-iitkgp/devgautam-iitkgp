#!/usr/bin/env python3
"""Check every url in resources.json. GitHub repos via `git ls-remote` (the
web UI often 403s bots); everything else via HTTP GET. Prints only problems.
Usage: python3 check_links.py resources.json"""
import json, re, subprocess, sys, concurrent.futures as cf, urllib.request
data = json.load(open(sys.argv[1], encoding="utf-8"))
items = data.get("resources", data) if isinstance(data, dict) else data
urls = sorted({i["url"] for i in items if isinstance(i, dict) and i.get("url")})
def check(u):
    m = re.match(r"https://github\.com/([^/]+/[^/#?]+)/?$", u)
    if m:
        r = subprocess.run(["git", "ls-remote", "--heads", f"https://github.com/{m.group(1)}"],
                           capture_output=True, text=True, timeout=30, env={"GIT_TERMINAL_PROMPT": "0", "PATH": "/usr/bin:/bin"})
        return u, "git-ok" if r.returncode == 0 else "git-FAIL"
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 link-check"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return u, str(resp.status)
    except urllib.error.HTTPError as e:
        return u, str(e.code)
    except Exception as e:
        return u, "ERR " + type(e).__name__
with cf.ThreadPoolExecutor(12) as ex:
    res = list(ex.map(check, urls))
bad = [(u, s) for u, s in res if s not in ("200", "git-ok")]
for u, s in bad: print(s, u)
print(f"\n{len(urls)-len(bad)}/{len(urls)} ok")
