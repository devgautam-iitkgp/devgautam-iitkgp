# How to Automate with Claude — Patterns Directory

Researched 2026-11-23, updated 2026-11-24. Mirror of the Claude doc https://claude.ai/artifact/H6idk1MoA39ynYkapdgwUz ("Full directory" tab). Short version for agents: AGENT_INDEX.md.

## 0. Quick pick

This doc is about **how** Claude automates work: the parts, the patterns, the wiring. Pick a route, then read section 1 (the parts) and section 2 (the patterns) before the route's own section.

Route picker:

1. Will other people use it as a product? → yes: **Route 2, Agent SDK or API** (Managed Agents can host it)
2. Does the work live in a code repo? → yes: **Route 1, Claude Code** (`claude -p`, hooks, GitHub Action, cloud tasks)
3. Is it mostly moving data between apps? → yes: **Route 3, Zapier, n8n or Make** (the engine runs steps, Claude does the thinking)
4. Otherwise → **Route 3, the Claude app** (connectors, skills, scheduled tasks)

It has to run with your laptop closed? Every route has a cloud option: cloud scheduled tasks or a GitHub Action for Claude Code, Managed Agents for the SDK, and the hosted versions of Zapier, n8n and Make.

| If you want to… | Start with | Section |
| --- | --- | --- |
| Run a prompt on a schedule with no code | A scheduled task in the Claude app | 5 |
| Have Claude review every PR or fix docs weekly | A GitHub Action or a cloud scheduled task | 3 |
| Glue Claude into Gmail, CRM, Sheets, Slack | Zapier MCP or an n8n AI Agent node | 5 |
| Ship an agent inside your own product | The Agent SDK | 4 |
| Process 10,000 documents cheaply | The Message Batches API (50% off) | 4 |
| Let an agent improve itself over time | A reflection loop plus an eval set | 7 |
| Make an automation reusable or shareable | A skill, hook, MCP server or plugin | 10 |

## 1. The six parts of every automation

Whatever the route, from a one-step Zap to sixteen agents writing a compiler, an automation is the same six parts. Decide each one on purpose and the route becomes a detail.

| Part | The question it answers | How you build it with Claude |
| --- | --- | --- |
| Trigger | What starts a run? | A schedule (cloud scheduled task, `/loop`, cron), an event (GitHub webhook, n8n or Zapier trigger), an API call, a message, or another agent finishing |
| Agent loop | Who runs the tool calls and feeds results back? | Claude Code and the Agent SDK run it for you; on the raw API you write it yourself, with an iteration cap |
| Tools | What can it actually do? | Built-in tools, MCP servers and connectors, your own functions. Tool design matters as much as the prompt |
| State | What survives between steps and between runs? | Files on disk (a progress file, a JSON task list, git commits), `CLAUDE.md`, the memory tool, or a database |
| Verification | How does it know it is done, and right? | Tests, an end-to-end check, a second agent as judge, a `/goal` condition, a Stop hook |
| Checkpoint | Where does a human say yes? | A pull request, an approval step before money or email leaves, a Slack ping, a review queue |

Two more stop being optional once it runs unattended. **Cost:** agents use about 4× the tokens of a chat and multi-agent systems about 15×, per Anthropic's [multi-agent research post](https://www.anthropic.com/engineering/multi-agent-research-system); the Batch API is 50% off and prompt caching cuts repeated input. **Observability:** keep `--output-format stream-json` logs, transcripts and run history, or you can't debug a run you didn't watch.

**The rule Anthropic repeats most:** start with the simplest thing that works. A fixed workflow (steps you define) beats an autonomous agent (steps Claude chooses) whenever you can write the steps down. Reach for an agent only when the path can't be known in advance. ([Building effective agents](https://www.anthropic.com/engineering/building-effective-agents))

## 2. Workflow patterns — the shapes automations take

These six shapes come from Anthropic's [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents). Almost every automation here is one of them, or two stacked.

| Pattern | Shape | Use it when | How with Claude |
| --- | --- | --- | --- |
| Prompt chaining | Fixed steps, a check between each | The task splits cleanly: outline → draft → fact-check → format | A shell script of `claude -p` calls, or chained nodes in n8n or Zapier |
| Routing | Classify first, then hand to a specialist | Inputs differ a lot: support tickets, inbox triage | A cheap model (Haiku) classifies; each branch has its own prompt or model |
| Parallelization | Split into independent parts (sectioning), or run the same task several times (voting) | Parts don't depend on each other, or you want a second opinion | Subagents, `/batch` in Claude Code, the Message Batches API for bulk |
| Orchestrator–workers | A lead plans subtasks at run time and hands them out | You can't know the subtasks up front: research, multi-file changes | Agent SDK with subagents, Claude Code agent teams |
| Evaluator–optimizer | Generate, critique against criteria, revise | There are clear standards: brand voice, character limits, tests | A writer agent plus a judge agent or skill; loop until the judge passes it |
| Autonomous agent | Loop until done, state kept outside the model | Open-ended, long, checkable work | `/goal`, a Ralph loop, or a harness with a progress file and a feature list |

**Four kinds of loop**, by what makes a run repeat: turn-based (one request, one run), goal-based (repeat until a condition holds, e.g. `/goal`), time-based (on a schedule, e.g. `/loop` or scheduled tasks) and event-based (on a webhook, a PR, a new email).

**Long-running work needs a harness.** Anthropic's [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) splits the job in two. An *initializer* agent runs once and writes a JSON feature list, a progress file and an `init.sh`. Every later *coding* session reads those, does one feature, tests it end to end, commits, and updates the progress file. The model forgets between sessions; the files and git history don't.

**Multi-agent is a cost decision, not a default.** In Anthropic's research system, a lead Opus agent with Sonnet subagents beat a single Opus agent by 90.2% on their internal eval, but used roughly 15× the tokens of a chat. Subagents write findings to storage and pass back short references, not full text. Use it when the task is broad, parallel and valuable enough to pay for. ([How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system))

## 3. Route 1 — Claude Code as an automation engine

Use it when the work lives in files or a repo, or when you want Anthropic's strongest agent harness without writing one. It is not only for code: Anthropic uses the same harness for research, video and note-taking.

### Headless runs: `claude -p`

`-p` runs one prompt with no UI and exits (code 0 on success), so any shell script, cron job or CI step can call Claude.

```bash
# pipe data in, write the answer to a file
cat build-error.txt | claude -p 'concisely explain the root cause' > output.txt

# structured output a script can trust
claude -p "Extract the main function names from auth.py" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}' \
  | jq '.structured_output'

# unattended: a classifier guards actions, nothing waits for a human
claude -p "Update the dependency pins and run the tests" \
  --permission-mode auto --permission-prompts none
```

The flags that matter for automation:

- `--bare` skips the host's hooks, plugins, MCP servers, memory and `CLAUDE.md`, so CI gives the same result on every machine. It needs `ANTHROPIC_API_KEY` and is set to become the default for `-p`.
- `--allowedTools "Bash(git diff *),Read"` pre-approves exactly what it may do (the space before `*` matters).
- `--permission-mode auto | dontAsk | acceptEdits` sets the baseline; `--permission-prompts none` denies anything that would wait for a person.
- `--output-format json` adds `total_cost_usd`; `stream-json` streams every event, subagents and retries included.
- `--continue` and `--resume <session_id>` chain multi-step runs; `--max-budget-usd` caps spend.

Source: [Run Claude Code programmatically](https://code.claude.com/docs/en/headless). Billing note: since June 15, 2026, Agent SDK and `claude -p` use on a subscription draws from a separate monthly credit.

### Hooks: fixed rules around a flexible agent

Hooks run your code at set points: session (`SessionStart`, `SessionEnd`), turn (`UserPromptSubmit`, `Stop`), tool calls (`PreToolUse`, `PostToolUse`, `PermissionRequest`), subagents (`SubagentStart`, `SubagentStop`), compaction and more. A hook can be a `command`, an `http` POST, an `mcp_tool` call, a one-shot `prompt` to Claude, or (experimental) an `agent`.

- **Block:** a `PreToolUse` hook that exits with code 2 stops the call and shows its stderr to Claude as the reason. Nothing in the hook's JSON can override that block.
- **Enforce:** a `PostToolUse` hook runs the formatter or the tests after every edit.
- **Don't stop early:** a `Stop` hook checks the definition of done and sends Claude back if it isn't met.
- **Report:** an `http` hook posts to Slack or any webhook when a run ends.

Source: [Hooks reference](https://code.claude.com/docs/en/hooks).

### Subagents, teams and fan-out

- **Subagents** each get their own context window and tool list; the main agent gets back only their summary. Use them for parallel research and to keep a long job's context clean.
- **Agent teams** (experimental, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) are several sessions that coordinate and message each other.
- **`/batch`** splits one large change across 5–30 subagents in separate git worktrees, each opening its own PR.
- **Dynamic workflows** let Claude write and run a multi-agent workflow on the fly, using patterns such as classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament and loop-until-done. Saved ones live in `~/.claude/workflows`. They burn tokens fast, so keep them for work that is worth it.

### Loops: keep going until done

- **`/goal <condition>`** (v2.1.139+) keeps Claude working until a small model judges the condition met. It replaces most uses of the Ralph loop.
- **The Ralph loop** is the original trick: `while :; do cat PROMPT.md | claude ; done`. State lives in files; every pass starts fresh. The official ralph-wiggum plugin packages it.
- **`/loop`** repeats a prompt on an interval inside an open session.

### Scheduling: three layers

| Layer | Runs on | Machine must be on? | Triggers | Best for |
| --- | --- | --- | --- | --- |
| `/loop` | Your open session | Yes | Interval | Watching something while you work |
| Desktop scheduled tasks | Your computer | Yes | Schedule | Jobs that need local files or apps |
| Cloud scheduled tasks (formerly routines) | Anthropic's cloud | No | Schedule, API call, GitHub event | Unattended, recurring, cross-repo work |

A cloud scheduled task bundles a prompt, one or more repos and connectors. Create it at [claude.ai/code/routines](https://claude.ai/code/routines), in the desktop app, or with `/schedule` (the CLI makes schedule triggers only; add API or GitHub triggers on the web). Each API trigger gets its own endpoint and token: POST a message, get a session URL back. Runs have no permission prompts, so the repos, branch-push settings, environment and connectors you pick are the fence. Examples from the docs: a weekly docs-drift scan that opens update PRs, a custom code review on `pull_request.opened`, and a feedback widget that POSTs a report so Claude drafts the fix. Source: [Automate work with routines](https://code.claude.com/docs/en/routines).

### CI: GitHub Actions

Run `/install-github-app` inside Claude Code, store `ANTHROPIC_API_KEY` as a repo secret, and `@claude` in any issue or PR comment starts a run. The same action runs on a cron for nightly jobs; GitLab CI/CD is supported too. Check the action's README for current inputs (`prompt`, `claude_args`, `trigger_phrase`).

```yaml
name: claude
on:
  issue_comment: { types: [created] }
  pull_request_review_comment: { types: [created] }
jobs:
  claude:
    if: contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    permissions: { contents: write, pull-requests: write, issues: write, id-token: write, actions: read }
    steps:
      - uses: actions/checkout@v6
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## 4. Route 2 — Agent SDK and the API

Use it when the automation is a product or a service: your own UI, your own users, your own servers, or full control over each step.

### Pick the layer

| Layer | You get | You write | Pick it when |
| --- | --- | --- | --- |
| Agent SDK (Python `claude-agent-sdk`, TypeScript `@anthropic-ai/claude-agent-sdk`) | Claude Code's harness: agent loop, file and shell tools, subagents, hooks, MCP, context management | The app around it | You want a capable agent fast, on your own infrastructure |
| Claude Managed Agents | A hosted harness and sandbox, with sessions, outcomes, multi-agent and scheduled deployments | Config and prompts | You don't want to run agent infrastructure ($0.08 per session-hour plus tokens; beta header `managed-agents-2026-04-01`) |
| Messages API (Client SDK) | One model call at a time, with tool use | The loop, tools, state and retries | Simple workflows, maximum control, or bulk jobs |

A minimal SDK agent in Python:

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for msg in query(
        prompt="Research this week's changes to the EU AI Act; write brief.md with sources",
        options=ClaudeAgentOptions(allowed_tools=["WebSearch", "WebFetch", "Write"]),
    ):
        print(msg)

asyncio.run(main())
```

Start from [claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos) (an email agent, and a research agent that splits a question into subtopics, runs parallel researchers and writes a report) or the [Claude Cookbook](https://platform.claude.com/cookbook) Agent SDK series, which grows from a one-liner research agent to multi-agent systems. Products you build for others should use API keys; third parties may not offer claude.ai login.

### API levers that change cost and reach

| Lever | What it does | Use it for |
| --- | --- | --- |
| Message Batches API | Asynchronous jobs at 50% off, results within 24 hours; stacks with prompt caching | Bulk classification, extraction, summaries, eval runs |
| Prompt caching | Reuses a long shared prefix (system prompt, documents, tool list) at a fraction of the input price | Any loop that resends the same context |
| Tool search (`defer_loading`) | Claude loads tool definitions only when it needs them | Agents with roughly 10 or more tools |
| Programmatic tool calling | Claude writes code that calls your tools; only the final result enters its context | Many chained calls over big data (Anthropic reported about 37% fewer tokens on complex research tasks) |
| Tool use examples | Example calls shown beside the schema | Tools with tricky parameters (72% → 90% accuracy in Anthropic's tests) |
| Context editing + memory tool (`memory_20250818`) | Clears stale tool results; keeps notes in files outside the window | Long-running agents (39% better together in Anthropic's eval, 29% from context editing alone) |
| Code execution with MCP | Presents MCP servers as code the agent imports, instead of loading every tool definition | Big tool libraries or big intermediate data (Anthropic's example: 150,000 → 2,000 tokens) |
| Computer use (`computer_toolset_20260801`) | Screenshot, mouse and keyboard; 17 member tools. Your app runs each call and returns one result per call | Desktop apps with no API. Inside a web page, the browser use tool fits better |

Sources: [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use), [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool).

### Design tools like a UI for the model

From [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents):

- Fewer, higher-level tools beat thin API wrappers: one `schedule_event`, not `list_users` + `list_events` + `create_event`.
- Namespace related tools (`asana_search`, `jira_search`) so Claude picks the right one.
- Return only what helps, in readable form, with a concise or detailed option; paginate and truncate with clear hints.
- Describe each tool as you would to a new colleague, then run an eval and let Claude rewrite the tools from the transcripts.

### Build your own MCP server when…

…your system has no connector and more than one agent or app will use it. One server then serves Claude Code, the Claude app, the SDK and other clients alike. Keep it small, typed and scoped to the least permission. Check Zapier MCP first: it may already cover the app.

## 5. Route 3 — No-code and in-app automation

Use it when you'd rather configure than code, or the job is mostly about your business apps. The key idea: **let a workflow engine run the fixed steps, and call Claude only where judgment is needed.** That is cheaper, easier to debug, and doesn't depend on a model taking the same path every time.

### Inside the Claude app

- **Connectors** reach Gmail, Google Drive, Slack, GitHub, Notion and many more; any remote MCP server can be added as a custom connector (on Team and Enterprise, an admin enables it first).
- **Skills** package a procedure once (brand voice, a report format, a checklist) and Claude loads it when it's relevant.
- **Scheduled tasks** run a saved prompt on a schedule in a fresh session, for example: "Every weekday at 8:30, summarise unread client email and today's calendar." Tasks that need your computer run only while it's on.
- **Claude in Chrome** acts in your real Chrome with your sign-ins: forms, dashboards, sites with no API. It carries the most prompt-injection risk of any route (section 8).

### Zapier: three directions

- **Claude drives Zapier.** Connect Zapier MCP as a connector and Claude can search, create, update and send across 9,000+ apps and 40,000+ actions. Each successful tool call uses two Zapier tasks.
- **Claude builds Zaps.** With Next Gen Zaps (early access), you describe the workflow and Claude builds and deploys it to Zapier, where it runs on real events without a model call at every step.
- **Zapier calls Claude.** Add a Claude step to an existing Zap using your own Anthropic account.

Sources: [Zapier MCP docs](https://docs.zapier.com/mcp/home), [Zapier: automate Claude](https://zapier.com/blog/automate-claude/).

### n8n: the most complete MCP setup

- **Claude as the brain.** The Anthropic Chat Model sub-node plugs into an AI Agent node (or a Basic LLM Chain). Add a Structured Output Parser when you need JSON.
- **n8n as Claude's tool.** The MCP Server Trigger node turns any workflow into an MCP endpoint that Claude Desktop or Claude Code can call.
- **n8n's agent using other tools.** The MCP Client Tool node lets n8n's own agent call external MCP servers.
- **Claude as the builder.** The community [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) server teaches Claude n8n's nodes so it can draft workflows for you.

There is no one-click n8n connector in Claude's directory; you wire it up yourself.

### Make

The Anthropic Claude module drops a Claude call into any scenario, the same pattern as a Claude step in a Zap.

### Rule of thumb

Draft the flow with Claude, run it on the engine, and keep Claude's steps to classifying, extracting, writing and judging. When an AI step gives the same answer every time, swap it for a plain step.

## 6. How-to by goal

Each recipe names the trigger, the steps, the check and the route. Swap the details; keep the shape.

### Content

**Ad and social variations at scale** (from Anthropic's growth marketing team)

- **Trigger:** a weekly performance export (CSV), or a custom slash command.
- **Steps:** find the underperforming ads → two specialised subagents write new headlines and descriptions → each draft is checked against Agent Skills for brand voice, product accuracy and platform best practice, and against hard character limits → export an upload-ready CSV.
- **Check:** a person treats the output as a starting point and edits it.
- **Route:** Claude Code with a custom command plus skills.
- **Reported result:** 30 minutes per ad down to 30 seconds, built by a marketer who had never opened a terminal. ([Anthropic](https://claude.com/blog/how-anthropic-uses-claude-marketing))

**One source, many formats.** A new post or video transcript lands in a folder → extract the key points → write LinkedIn, X and newsletter versions in parallel → an evaluator checks each against the voice skill and length rules → drafts go to a review queue (Notion, Docs or Slack). Route: a Zapier or n8n trigger with Claude steps, or a cloud scheduled task.

**What makes content automation work:** the voice lives in a skill with real examples written by your best writers, limits are checkable by code, and a person stays the editor.

### Research

**Recurring research brief**

- **Trigger:** a weekly schedule, or an API call carrying a question.
- **Steps:** a lead agent plans subtopics → parallel subagents search and read, each writing findings with sources to files → the lead synthesises → a citation pass checks that every claim has a source.
- **Check:** before you trust it, run about 20 test questions through an LLM judge with a rubric (accuracy, citations, completeness, source quality), as Anthropic did for its research system.
- **Route:** the Agent SDK (start from the research-agent demo) or Claude Code with subagents, run as a cloud scheduled task.
- **Watch:** multi-agent research is token-heavy; cap the budget per run.

**Watchlist digest.** One agent, not many: each morning it checks a fixed list of sources (a competitor's changelog, a regulator's page, a repo), compares against yesterday's saved snapshot, and reports only what changed. Cheaper and more reliable than open-ended research.

### Learning

**Learning path for a new tool or topic.** An Agent SDK research agent with a learning-a-tool skill reads the docs, the GitHub repo and the web, then writes a staged learning path. DeepLearning.AI's Agent Skills course with Anthropic builds exactly this.

**Daily review loop** (a design, not a published case). Keep notes plus a `progress.json` of what you've learned and when. A daily scheduled task picks items due for review (spaced repetition), writes five questions, grades your answers next time and updates the file. It is the long-running harness from section 2 pointed at you: state in a file, one small step per run.

### Operations and business

- **Docs drift:** a weekly cloud scheduled task scans merged PRs, finds docs that mention changed APIs, and opens update PRs.
- **Review on every PR:** a GitHub trigger on `pull_request.opened`, with your own checklist as a skill.
- **Personal weekly briefings:** an Anthropic field marketer connected Claude Code to BigQuery through MCP and turned one weekly sales report into a personalised Monday briefing for each account executive. ([Anthropic](https://claude.com/resources/articles/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep))
- **Inbox and lead triage:** each new email or form fill is classified by a cheap model → Claude drafts a reply or a CRM update → a person approves before anything is sent. Zapier or n8n.
- **Bulk documents:** invoices, contracts or survey answers through the Batch API with a JSON schema, at half price.

## 7. Self-improving agents

An agent improves itself when something it learned in one run changes how the next run behaves. In practice it writes to one of four places, listed here from safest to riskiest:

| What it updates | How | Tools and examples |
| --- | --- | --- |
| Its notes (memory) | Saves facts and decisions to files it reads next time | The memory tool, Claude Code's auto memory, a progress file |
| Its instructions | Turns corrections into rules in `CLAUDE.md` | claude-reflect, the review-claudemd skill, a session-mining workflow |
| Its procedures | Writes a new skill when it repeats a multi-step job | skill-creator, claude-skill-self-improvement |
| Its tools | Rewrites tool descriptions or code from eval transcripts | Anthropic's tool-writing guide (section 4) |

### The reflection loop

1. **Capture.** A `Stop` or `SessionEnd` hook, or an end-of-task prompt, asks what went wrong, what the user corrected, and what took too long.
2. **Propose.** Claude drafts the change as a diff to `CLAUDE.md`, a skill or a tool description, and does not apply it.
3. **Review.** A person approves it (a PR is ideal), or a second agent tests it against the eval set.
4. **Measure.** Run the eval set before and after; keep the change only if the scores hold or rise.
5. **Prune.** Every so often, have Claude merge duplicate rules and delete stale ones. Instruction files rot.

### Repos to copy from

- [claude-reflect](https://github.com/BayramAnnakov/claude-reflect) captures your corrections during sessions and proposes `CLAUDE.md` updates.
- [claude-skill-self-improvement](https://github.com/bokan/claude-skill-self-improvement) is a skill that has Claude improve its skills from experience.
- [claude-code-tips](https://github.com/ykdojo/claude-code-tips) includes a review-claudemd skill that mines past conversations for rules worth adding.
- [anthropics/skills](https://github.com/anthropics/skills) includes skill-creator, which writes and tests new skills.

### Evals turn "improvement" into a number

From [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): give each task clear success criteria; grade the outcome and the transcript; use code graders where you can and model graders where you must; track pass@k (succeeds at least once in k tries) for capability and pass^k (succeeds every time) for reliability; start with capability evals and turn them into regression evals once they pass. Twenty well-chosen cases beat none.

### Guardrails for self-modification

- Notes: edit freely. Instructions, skills and tools: propose only. Its own permissions, hooks and secrets: never.
- Keep everything in git so any "lesson" can be rolled back.
- Watch for drift: a new rule that makes it more agreeable or skip a check is a regression, not an improvement.

## 8. Guardrails — so it can run while you sleep

An unattended agent fails in three ways: it does something you didn't want, someone else's text steers it, or it quietly loops and spends. Each has a known fix.

### Permissions: decide what it may do without asking

| Mode | Behaviour | Use it for |
| --- | --- | --- |
| Manual | Asks before edits and commands | Trying out a new automation |
| `acceptEdits` | Writes files freely; most commands still need approval | Editing jobs in a trusted repo |
| `auto` | A classifier reviews each action; risky ones are blocked or escalated | Long and unattended runs |
| `dontAsk` | Denies anything that would prompt | Locked-down CI |
| `--dangerously-skip-permissions` | No checks at all | Only inside a throwaway container or VM |

Why auto mode exists: Anthropic found people approve the vast majority of permission prompts (93% in one post, 97% in a later one), which looks like reflex rather than review. Auto mode puts a model-based classifier in front of each action, and on entering it Claude Code drops allow rules that grant arbitrary code execution (blanket shell access, wildcard interpreters, package-manager run commands). It went generally available on July 10, 2026; The Register reports it became the default from August 14, falling back to manual approval after three blocks in a row or 20 in a session. Sources: [Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode), [The Register](https://www.theregister.com/a/5285326).

### Sandboxing: fence the blast radius

Claude Code can sandbox its shell with filesystem and network limits you set, and run without prompts inside them; Anthropic says this cut permission prompts by 84% internally. For anything unattended add an outer fence as well: a container or VM, a scoped API key, a branch it can push to but not merge. Auto mode lowers risk but doesn't remove it, and Anthropic still recommends isolated environments. ([Beyond permission prompts](https://www.anthropic.com/engineering/claude-code-sandboxing))

### Prompt injection: treat everything it reads as untrusted

Any web page, email, PDF or issue comment can hide instructions. Browser agents are the most exposed because they can click, fill forms and download. Anthropic brought browser attack success down to about 1% with Claude Opus 4.5 and its safeguards, and still calls the problem far from solved. ([Mitigating prompt injection in browser use](https://www.anthropic.com/research/prompt-injection-defenses))

- Don't give one agent all three of: untrusted input, access to private data or secrets, and a way to send data out. Split readers from actors.
- Require a human yes for irreversible or outbound actions: sending email, paying, deleting, publishing.
- Scope connectors and API tokens to the least access the job needs.
- Pass untrusted content in as data (a file, a quoted block), never as instructions.

### Hard rules with hooks

For things that must never happen, use a `PreToolUse` hook that exits with code 2 (section 3). It blocks the call whatever the model or the classifier decides: no `rm -rf`, no push to `main`, no network call outside an allowlist.

### Failure handling

- **Stop conditions:** an iteration cap, `--max-budget-usd`, a wall-clock timeout.
- **Idempotent steps:** running a step twice must not send twice or charge twice; write a done-marker per item.
- **Retries with backoff,** then a clear failure message to a human channel.
- **Logs you can replay:** `stream-json` output and transcripts for every run.
- **Careful rollouts:** Anthropic's research system uses rainbow deployments so a change doesn't break agents mid-task.
- **Test with hostile users.** Project Vend's shop agent did fine with friendly colleagues and was talked into bad deals by determined outsiders. Better tools and human approval of purchases helped more than a smarter model.

## 9. Standout cases and how they were built

| Case | What happened | How it was built | The lesson |
| --- | --- | --- | --- |
| C compiler by an agent team (Anthropic, Feb 2026) | 16 Claude Opus 4.6 agents, nearly 2,000 Claude Code sessions over about two weeks and about $20,000 in API cost produced a 100,000-line Rust C compiler that builds Linux 6.9 on x86, ARM and RISC-V | Each agent in its own container, in a simple Ralph-style loop on a shared git repo; README and progress files for orientation; fast test modes sampling 1–10% of cases; GCC as an oracle so agents could debug in parallel | Tests and the harness steer, not the prompt. Run it in containers. ([post](https://www.anthropic.com/engineering/building-c-compiler), [repo](https://github.com/anthropics/claudes-c-compiler)) |
| Multi-agent research system (Anthropic) | Powers Claude's Research feature | A lead Opus agent plans; Sonnet subagents search in parallel; results stored outside and passed back by reference; LLM-judge evals; rainbow deploys | +90.2% over one agent for about 15× the tokens: pay for breadth only when it is worth it ([post](https://www.anthropic.com/engineering/multi-agent-research-system)) |
| Long-running app builder (Anthropic) | One agent builds a web app across many context windows | An initializer writes a feature list (JSON), a progress file and `init.sh`; each coding session does one feature, tests it end to end and commits | Memory is files and git, not the context window ([post](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)) |
| Growth marketing (Anthropic) | Ad creation down from 30 minutes to 30 seconds | A custom command, two subagents, Agent Skills for voice and rules, CSV in and out | A non-coder can build it; skills carry the expertise ([post](https://claude.com/blog/how-anthropic-uses-claude-marketing)) |
| Field marketing briefings (Anthropic) | A personalised weekly briefing for every account executive | Claude Code plus BigQuery through MCP, built during an hour of a marketing hackathon | Data access through MCP turns one report into many ([post](https://claude.com/resources/articles/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep)) |
| Project Vend (Anthropic and Andon Labs) | An AI shopkeeper lost money in phase one (Sonnet 3.7) and turned a profit in phase two | Phase two: Sonnet 4.0, then 4.5; better inventory and supplier tools; human approval of purchases; a CEO agent and a merchandise agent alongside the shopkeeper | Scaffolding beats raw intelligence; agents can be manipulated, so approvals matter ([phase two](https://www.anthropic.com/news/project-vend-2)) |

## 10. Packaging — how automations get installed and shared

Every automation above ends up as one of six things. Pick the lightest one that does the job:

| You have… | Package it as | Where it lives | How it runs |
| --- | --- | --- | --- |
| A fact every session needs ("we use pnpm", "renders go in /out") | `CLAUDE.md` | Project root, or `~/.claude/CLAUDE.md` for all projects | Loaded into every session |
| A procedure you keep pasting | Skill | `~/.claude/skills/<name>/SKILL.md` (all projects) or `.claude/skills/<name>/SKILL.md` (this repo) | Claude loads it when the description matches, or you type `/name` |
| A worker that needs its own context and tools | Subagent | `.claude/agents/<name>.md` (or `~/.claude/agents/`) | Claude delegates to it, or you @-mention it |
| A rule that must always hold | Hook | `.claude/settings.json` (or `~/.claude/settings.json`) | Runs at its event, whatever the model decides |
| A new capability (an API, a database, an app) | MCP server | `claude mcp add …`, stored in `~/.claude.json` or `.mcp.json` | Its tools appear to Claude |
| A bundle to share with others | Plugin | A directory with `.claude-plugin/plugin.json`, listed in a marketplace | `/plugin marketplace add`, then `/plugin install` |

**Where these load.** Personal skills (`~/.claude/skills/`), user subagents and locally installed plugins load in every Claude Code session on that computer (terminal, desktop app, VS Code), with no per-session setup. They do not load in cloud sessions (claude.ai/code) or Cowork. For those, commit the skill to the repo's `.claude/skills/` or point the session at a raw URL.

### MCP servers

```bash
claude mcp add <name> -- <command> [args...]          # local process (stdio)
claude mcp add --transport http <name> <url>           # remote server
claude mcp add --transport http shared --scope project https://example.com/mcp
```

Scopes: `local` (default; this project, only you), `project` (written to `.mcp.json` in the repo, shared through git) and `user` (all your projects). Source: [MCP docs](https://code.claude.com/docs/en/mcp).

### Skills

```markdown
---
name: weekly-report
description: Build the weekly sales report from the CRM export. Use when asked for the weekly report or a sales summary.
---

1. Read the newest CSV in ./exports.
2. Total by rep and region; flag anything down more than 20% week on week.
3. Write report.md with a 5-line summary at the top.
```

- The description is the trigger: Claude reads every skill's description and loads the one that matches, so put the words a request would use up front.
- Scripts, templates and reference files sit beside `SKILL.md` and are read only when needed (progressive disclosure).
- Custom commands were merged into skills: `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both make `/deploy`.
- Claude Code watches skill folders, so a new or edited skill works in the current session.
- When a section of `CLAUDE.md` grows from a fact into a procedure, move it into a skill.

Source: [Skills docs](https://code.claude.com/docs/en/skills).

### Subagents

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. Give specific, actionable feedback on quality, security and best practices.
```

Save it as `.claude/agents/code-reviewer.md` (this project) or `~/.claude/agents/` (all projects). `name` and `description` are required; the body becomes the subagent's system prompt. Claude delegates when the description fits; `@agent-code-reviewer` forces it, and `claude --agent code-reviewer` runs a whole session as it. Source: [Subagents docs](https://code.claude.com/docs/en/sub-agents).

### Hooks: where they live

`~/.claude/settings.json` (all your projects), `.claude/settings.json` (this project, committed), `.claude/settings.local.json` (this project, not committed), a plugin's `hooks/hooks.json`, or the frontmatter of a skill or subagent (active only while it runs). Match MCP tools by name: `mcp__<server>__<tool>`, e.g. matcher `mcp__github__.*`. Source: [Hooks guide](https://code.claude.com/docs/en/hooks-guide). The Blender directory ships a ready, tested example: `hooks/block_unsafe_blender_python.py`.

### Plugins and marketplaces

A plugin is one directory: `.claude-plugin/plugin.json` plus any of `skills/`, `agents/`, `hooks/hooks.json` and `.mcp.json`. A marketplace is a repo with `.claude-plugin/marketplace.json` listing plugins.

```text
/plugin marketplace add owner/repo
/plugin install name@marketplace
/plugin install github@claude-plugins-official          # Anthropic's official marketplace
claude plugin install name@marketplace --scope project  # from a script
```

Install scopes: user (every project on this computer), project (everyone in the repo, through `.claude/settings.json`) or local (you, this repo only). An enabled plugin costs context in every session: the name and description of each skill and agent it adds sit in context on every turn, even when unused, so disable plugins you don't use.

Sources: [Plugins overview](https://code.claude.com/docs/en/plugins/overview), [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

### Worked example: this directory is a skill

```bash
git clone -b claude-automation --depth 1 https://github.com/devgautam-iitkgp/devgautam-iitkgp ~/.claude/skills/claude-automation-patterns
git -C ~/.claude/skills/claude-automation-patterns pull    # update later
```

The branch has a `SKILL.md` at its root, so Claude Code loads it whenever automation comes up, with no link to paste. It is a one-time setup per computer. The Blender directory installs the same way (branch `blender-claude-mcp`).

## 11. Sources and where to keep learning

### Anthropic engineering posts (read these first)

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — the workflow patterns
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use) and [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [Beyond permission prompts](https://www.anthropic.com/engineering/claude-code-sandboxing) and [Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)

### Docs

- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless) · [Hooks](https://code.claude.com/docs/en/hooks) · [Skills](https://code.claude.com/docs/en/skills) · [MCP](https://code.claude.com/docs/en/mcp) · [Plugins](https://code.claude.com/docs/en/plugins/overview) · [Cloud scheduled tasks](https://code.claude.com/docs/en/routines) · [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) · [Claude Cookbook](https://platform.claude.com/cookbook) · [Zapier MCP](https://docs.zapier.com/mcp/home)

### Repos

- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — the community hub for skills, hooks, commands and orchestrators
- [claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos) · [claude-cookbooks](https://github.com/anthropics/claude-cookbooks) · [claude-code-action](https://github.com/anthropics/claude-code-action) · [skills](https://github.com/anthropics/skills)
- [claudes-c-compiler](https://github.com/anthropics/claudes-c-compiler) · [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) · [zapier-mcp](https://github.com/zapier/zapier-mcp)
- Self-improvement: [claude-reflect](https://github.com/BayramAnnakov/claude-reflect) · [claude-skill-self-improvement](https://github.com/bokan/claude-skill-self-improvement) · [claude-code-tips](https://github.com/ykdojo/claude-code-tips)

### Coverage

Researched on November 23, 2026 from Anthropic's docs and posts, vendor docs (Zapier, n8n), GitHub and news coverage. Links re-checked on November 24, 2026 with `scripts/check_links.py`. The index is tested with `evals/questions.json` and `scripts/eval_index.py`: it scored 16/20 before section 10 was added and 20/20 after. The grader also fails if the index grows past its token budget. Reddit was blocked from the research environment, so no Reddit threads are listed; r/ClaudeAI and r/ClaudeCode are worth checking yourself. Figures are as reported by their sources. Names change fast (routines became cloud scheduled tasks), so check the linked doc before you rely on a flag.
