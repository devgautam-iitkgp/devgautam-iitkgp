# AGENT INDEX — How to automate with Claude (patterns, not use cases)
v2026-11-23 · full text: DIRECTORY.md (same folder) · machine list: resources.json
Read this first (~2.5k tokens). Open DIRECTORY.md section N only when you need detail.

## DECIDE (route)
1 product for other people? → R2 Agent SDK/API (Managed Agents = hosted) [§4]
2 work lives in a repo/files? → R1 Claude Code: claude -p, hooks, GH Action, cloud scheduled task [§3]
3 mostly moving data between apps? → R3 Zapier/n8n/Make + Claude step [§5]
4 else → R3 Claude app: connectors + skills + scheduled tasks [§5]
laptop closed? → cloud scheduled task | GitHub Action | Managed Agents | hosted Zapier/n8n

## SIX PARTS (decide each) [§1]
trigger | agent loop | tools | state (files/git/CLAUDE.md/memory) | verification (tests, judge, /goal, Stop hook) | human checkpoint (PR/approval)
+ cost (agent ~4x chat tokens, multi-agent ~15x; Batch -50%; caching) + logs (stream-json)
RULE: simplest thing that works; fixed workflow > autonomous agent when steps are knowable.

## PATTERNS [§2]
chaining = fixed steps+gates → claude -p script / n8n chain
routing = classify (Haiku) → specialist
parallel = sectioning|voting → subagents, /batch, Batch API
orchestrator-workers = lead plans at runtime → SDK subagents, agent teams
evaluator-optimizer = generate→judge→revise → writer + judge agent/skill
autonomous = loop until done, state outside model → /goal, Ralph loop, harness
loops: turn | goal | time | event
long-running harness: initializer writes features.json+progress file+init.sh; each session: 1 feature → e2e test → commit → update progress
multi-agent: +90.2% vs single (Anthropic research) at ~15x tokens; subagents write to storage, return refs

## R1 CLAUDE CODE [§3]
claude -p "..." (exit 0 ok) · pipe stdin (≤10MB) · --output-format json(total_cost_usd)|stream-json
--json-schema '{...}' → .structured_output · --bare (CI-reproducible, needs ANTHROPIC_API_KEY)
--allowedTools "Bash(git diff *),Read" · --permission-mode auto|dontAsk|acceptEdits · --permission-prompts none
--continue / --resume <id> · --max-budget-usd · --append-system-prompt
hooks: SessionStart/End, UserPromptSubmit, Stop, PreToolUse, PostToolUse, PermissionRequest, SubagentStart/Stop… types command|http|mcp_tool|prompt|agent(exp)
  PreToolUse exit 2 = hard block (stderr→Claude) · PostToolUse = format/test · Stop = enforce done · http = notify
subagents (own context) · agent teams CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 · /batch 5–30 worktree subagents, 1 PR each
dynamic workflows (~/.claude/workflows): classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done — token-heavy
/goal <cond> (v2.1.139+) > Ralph `while :; do cat PROMPT.md | claude ; done` · /loop = interval in open session
schedule: /loop (session) | Desktop task (machine on) | Cloud scheduled task (ex-routines; cloud; schedule/API/GitHub triggers; no prompts → repos+env+connectors are the fence) claude.ai/code/routines, /schedule
GH Action: /install-github-app; anthropics/claude-code-action@v1 with anthropic_api_key; @claude in comments; inputs prompt, claude_args
billing: from 2026-06-15 SDK & claude -p on subscriptions use a separate monthly credit

## R2 SDK / API [§4]
Agent SDK (py claude-agent-sdk / ts @anthropic-ai/claude-agent-sdk) = Claude Code harness in your app
  from claude_agent_sdk import query, ClaudeAgentOptions; query(prompt=..., options=ClaudeAgentOptions(allowed_tools=[...]))
  starters: github.com/anthropics/claude-agent-sdk-demos (email, multi-agent research) · platform.claude.com/cookbook
Managed Agents = hosted harness+sandbox, $0.08/session-hr + tokens, beta managed-agents-2026-04-01
Messages API = you write loop/tools/state
levers: Batch -50% ≤24h | prompt caching | tool search defer_loading (10+ tools) | programmatic tool calling (~37% fewer tokens) | tool use examples (72→90%) | context editing+memory_20250818 (+39%) | code execution w/ MCP (150k→2k tokens) | computer_toolset_20260801 (17 tools; one tool_result per tool_use) | browser use tool for web
tool design: few high-level tools, namespaced, concise returns, eval then let Claude rewrite tools
own MCP server only if no connector exists and >1 client will use it (check Zapier MCP first)

## R3 NO-CODE / APP [§5]
principle: engine runs fixed steps; Claude only for classify/extract/write/judge; replace deterministic AI steps with plain steps
Claude app: connectors (custom = remote MCP URL) · skills · scheduled tasks · Claude in Chrome (highest injection risk)
Zapier: Claude→Zapier MCP (9,000+ apps, 40k+ actions, 2 tasks per call) | Claude builds Zaps (Next Gen Zaps, early access) | Zap calls Claude step
n8n: Anthropic Chat Model → AI Agent node | MCP Server Trigger (workflow = tool for Claude) | MCP Client Tool | czlonkowski/n8n-mcp (Claude drafts workflows) · no 1-click connector
Make: Anthropic Claude module

## RECIPES [§6]
content: CSV → find losers → 2 subagents (headlines/descriptions) → check vs skills (voice, accuracy, limits) → CSV; human edits (Anthropic: 30min→30s)
content: 1 source → parallel formats → voice/length judge → review queue
research: lead plans → parallel subagents write sourced findings to files → synthesize → citation pass; eval ~20 Qs w/ LLM judge; cap budget
research: watchlist digest = 1 agent diffing snapshots (cheaper than open research)
learning: SDK agent + learning-a-tool skill → learning path · daily scheduled quiz w/ progress.json (design)
ops: docs-drift weekly task → PRs · review on pull_request.opened · BigQuery MCP → per-rep briefings · triage → draft → human approve · Batch API for bulk docs

## SELF-IMPROVING [§7]
update targets (safe→risky): notes/memory → CLAUDE.md rules → skills → tools
loop: capture (Stop/SessionEnd hook) → propose diff (don't apply) → review (PR/agent) → measure on eval set → prune
repos: BayramAnnakov/claude-reflect · bokan/claude-skill-self-improvement · ykdojo/claude-code-tips (review-claudemd) · anthropics/skills (skill-creator)
evals: grade outcome+transcript; code graders > model graders; pass@k capability, pass^k reliability; capability→regression
never let it edit its own permissions/hooks/secrets; git everything; rules that skip checks = regression

## GUARDRAILS [§8]
modes: manual | acceptEdits | auto (classifier; GA 2026-07-10; default from 2026-08-14 per The Register; falls back after 3 blocks in a row/20 per session) | dontAsk (CI) | skip-permissions only in throwaway VM
sandbox: fs+network limits, -84% prompts; plus container/VM, scoped keys, push-not-merge branch
injection: never one agent with untrusted input + private data + exfil channel; human yes for send/pay/delete/publish; least-privilege tokens; untrusted content as data
hard rules: PreToolUse exit 2 (no rm -rf, no push main, network allowlist)
failure: iteration cap, budget, timeout, idempotent steps, retries→human alert, replayable logs, careful rollouts, test with hostile users (Project Vend)

## CASES [§9]
C compiler: 16 Opus 4.6 agents, ~2,000 sessions, ~$20k, 100k-line Rust, builds Linux 6.9 x86/ARM/RISC-V; containers + Ralph-style loop + shared git + progress files + 1–10% fast tests + GCC oracle
research system: lead Opus + Sonnet subagents, +90.2%, ~15x tokens · long-running harness: initializer + 1 feature/session
growth marketing 30min→30s · field marketer BigQuery MCP briefings · Project Vend: phase 2 profitable via tools + human purchase approval + CEO agent

## TOP SOURCES [§10]
anthropic.com/engineering/: building-effective-agents · effective-harnesses-for-long-running-agents · multi-agent-research-system · effective-context-engineering-for-ai-agents · writing-tools-for-agents · advanced-tool-use · code-execution-with-mcp · demystifying-evals-for-ai-agents · building-agents-with-the-claude-agent-sdk · claude-code-sandboxing · claude-code-auto-mode · building-c-compiler
docs: code.claude.com/docs/en/{headless,hooks,routines,agent-sdk/overview} · platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool · docs.zapier.com/mcp/home
hub: github.com/hesreallyhim/awesome-claude-code
not covered: Reddit (blocked during research). Verify flags against docs; names change fast.
