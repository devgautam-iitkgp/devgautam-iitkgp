# Agent index: Blender + Claude MCP

Install as a skill (auto-loads on Blender questions): git clone -b blender-claude-mcp --depth 1 https://github.com/devgautam-iitkgp/devgautam-iitkgp ~/.claude/skills/blender-claude-mcp

For AI sessions: read only this file (about 3k tokens; the Start here block alone is about 250). Open DIRECTORY.md only for full notes; resources.json is the machine-readable source of truth.

Checked 2026-11-23; links re-checked 2026-11-24. One line per resource: name | url | stars | short note. * = page opened on check date; others from search or listing sites. Star counts drift; re-check before quoting.

## Decide
- Official Blender Lab connector: analysis, cleanup, batch scripts, node explanations. Blender 5.1+. Claude Desktop or Claude Code only.
- Community mcp-for-blender: build scenes, asset libraries, AI 3D generation. Blender 3.0+.
- Add a skill pack: arjun988 (community server) for game assets; ra100 (official server) for bpy depth.
- Rules: one add-on at a time (port 9876). Never claude.ai web. Work on .blend copies (arbitrary Python).

## Start here (stop reading if this answers you)
1. Official setup: https://academy.claude.com/tutorials/using-the-blender-connector-in-claude
2. Official add-on: https://www.blender.org/lab/mcp-server/
3. Community server: https://github.com/ahujasid/mcp-for-blender  (claude mcp add blender uvx mcp-for-blender; or one command: uvx mcp-for-blender setup)
   Official server in Claude Code: claude mcp add blender -- uvx --from "git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp" blender-mcp
4. Biggest skill pack: https://github.com/arjun988/blender-skills  (needs community server)
5. Skills for official server: https://github.com/ra100/blender-claude-plugin
6. Best tested comparison: https://www.meltflexai.com/blog/connect-claude-to-blender
7. Honest limits: https://www.mindstudio.ai/blog/claude-blender-mcp-real-world-performance
8. Best video (official + Claude Code): https://www.youtube.com/watch?v=b5F-yNG4lds
9. Research baseline: https://arxiv.org/abs/2504.01786 (BlenderGym)
10. Automating Blender (headless, self-checks, schedules): see Automate below
11. Fixes: see Top fixes at the end

## Automate (patterns; general ones: https://raw.githubusercontent.com/devgautam-iitkgp/devgautam-iitkgp/claude-automation/AGENT_INDEX.md)
- live vs headless: MCP drives an open Blender (port 9876). Batch/unattended: skip MCP, Claude writes bpy and runs `blender -b copy.blend --python-exit-code 1 -P job.py -- args` (non-zero exit on Python error; args after -- in sys.argv)
- render: `-o //renders/frame_#### -f 1` (// = next to .blend) or `-a` for animation
- self-check: render preview PNG or community viewport screenshot -> Claude reads image, judges vs concrete criteria -> loop (evaluator-optimizer; BlenderGym: models verify worse than they generate)
- unattended: `claude -p "<job>" --allowedTools "Bash(blender -b *),Read,Write"` via cron/Desktop scheduled task; cloud tasks/GitHub Actions only if runner installs Blender
- guardrails: .blend copies; outputs in git; PreToolUse hook on Blender code tool (matcher like mcp__blender__.*) blocking os/subprocess/shutil
- reuse: save a working prompt+script as ~/.claude/skills/<name>/SKILL.md
- CLI manual: https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html

## Official
- Blender Lab MCP Server page | https://www.blender.org/lab/mcp-server/ | docs + add-on install link (drag in twice). Blender 5.1+, Allow Online Access
- Blender Lab repo* | https://projects.blender.org/lab/blender_mcp | GPL-3.0+, ~26 tools, v1.0.3 (11 Sep 2026), Blender core devs
- Claude Blender connector | https://claude.com/connectors/blender | Desktop > Customize > Connectors > Blender. Any plan. Not claude.ai web
- Anthropic tutorial* | https://academy.claude.com/tutorials/using-the-blender-connector-in-claude | says 4.2+, manifest needs 5.1+
- Claude for Creative Work | https://www.anthropic.com/news/claude-for-creative-work | 28 Apr 2026 launch
- Official via Claude Code (Qiita) | https://qiita.com/zukka/items/6492cf4db31e374850e2 | plain `uvx blender-mcp` = COMMUNITY server (name clash)

## Free servers and bridges
- MCP for Blender (ahujasid)* | https://github.com/ahujasid/mcp-for-blender | 35.4k | MIT, 3.0+, Poly Haven/Sketchfab/Rodin/Hunyuan3D/Tripo; Python on by default; viewport screenshots; package renamed from blender-mcp (old name still works); Discord discord.gg/SNqPn4TcKQ
- blenderwright (was blend-ai)* | https://github.com/jabberwock/blend-ai | 187 | 276 tools, 5.2 LTS only, uvx blenderwright
- blender-open-mcp* | https://github.com/dhakalnirajan/blender-open-mcp | 114 | local LLMs: Ollama, LM Studio, llama.cpp, OpenAI-compatible
- dcc-mcp-blender* | https://github.com/dcc-mcp/dcc-mcp-blender | 53 | typed tools, 4.5+, pip install dcc-mcp-blender
- Meshwire* | https://github.com/RFingAdam/mcp-blender | 34 | AGPL, 225 tools, 4.2-5.2, uvx meshwire
- blender-mcp-server (djeada)* | https://github.com/djeada/blender-mcp-server | 24 | own add-on, incompatible protocol
- blender-agent* | https://github.com/ptrthomas/blender-agent | 11 | no MCP, HTTP + skills, 5.0+
- Blender MCP Plus | https://glama.ai/mcp/servers/dq930e7q6b | official add-on + Poly Haven, one port
- sandraschi/blender-mcp | https://glama.ai/mcp/servers/sandraschi/blender-mcp | 80+ tools, .mcpb install, VRChat checks
- hardened fork (soozs1) | https://glama.ai/mcp/servers/soozs1/Blender-MCP | no telemetry, token auth, loopback only
- CommonSenseMachines | https://github.com/CommonSenseMachines/blender-mcp | text-to-3D, auto-rig; repo UNREACHABLE 2026-11-24
- Scenario for Blender | https://www.claudemarketplace.net/mcp/blender-plugin | AI textures/HDRI + MCP, paid account
- blender-ai-mcp* | https://github.com/PatrykIti/blender-ai-mcp | 67 | ARCHIVED, skip

## Paid servers
- Blender MCP Pro (abyo)* | https://blender-mcp-pro.abyo.net | $5/mo or $15, 110-120+ tools, 3.6+
- BlenderMCP Pro (Anvil) | https://superhivemarket.com/products/blendermcp-pro | different product, v2.5.2
- StraySpark* | https://www.strayspark.studio/products/blender-mcp-server | $55.99 or $174.99, safe defaults, 5.1+

## Skill packs
- arjun988/blender-skills* | https://github.com/arjun988/blender-skills | 4.5k | 94 skills, game assets, entry=blender-director, community server; /plugin marketplace add arjun988/blender-skills
- kevinbadi/blender-skills* | https://github.com/kevinbadi/blender-skills | 288 | 16 skills, product shots, camera moves, Meshy
- EL4CTEO/blender-skills* | https://github.com/el4cteo/blender-skills | 164 | 22 skills, 5.2 LTS+; /plugin marketplace add EL4CTEO/blender-skills (snippets claim 2.7k/28: unconfirmed)
- ra100/blender-claude-plugin* | https://github.com/ra100/blender-claude-plugin | 11 | 8 bpy skills, OFFICIAL server; claude plugin marketplace add ra100/blender-claude-plugin
- jithinolickal/blender* | https://github.com/jithinolickal/blender | 9 | 1 parametric-design skill, community server
- mromidev* | https://github.com/mromidev/claude-blender-skills | 2 | 3 film skills, own bridge
- scenario-labs/skills | https://github.com/scenario-labs/skills | blender-expert router, hard-surface, rigging, sculpt
- Dev-GOM blender-toolkit | https://github.com/Dev-GOM/claude-code-marketplace | WebSocket, Mixamo retarget
- vladmdgolam blender-mcp | https://github.com/vladmdgolam/agent-skills | MCP tools vs Python guidance
- TMHSDigital | https://github.com/TMHSDigital/Blender-Developer-Tools | add-on dev skills, 5.1
- SamuelAsherRivello | https://skillsmp.com/ar/creators/samuelasherrivello/ai-skills-blender | ~28 asset skills
- animated-asset-skill | https://github.com/rehan-remade/animated-asset-skill | prompt to rigged voxel creature
- Patch-gg/trompe | https://github.com/Patch-gg/trompe | blockout + image-model texturing
- singles | https://skills.sh/terminalskills/skills/blender-scripting | also alivirgo, openaec (BIM), code-buddy, flue, digitalsamba, blender-game-skills
- lead: Rehan Sheikh 29 skills | https://x.com/rehan_shei | repo not found

## Videos
- official test, Claude Code at 3:14 | https://www.youtube.com/watch?v=b5F-yNG4lds
- official Mac setup + FAQ | https://www.youtube.com/watch?v=0PdIuWlxhHA
- official with Claude/Codex/Gemini | https://www.youtube.com/watch?v=YQBO5de575Y
- official, no config | https://www.youtube.com/watch?v=WaGIc9KJRwE
- community, Nov 2026, safety settings | https://m.youtube.com/watch?v=rohl0_7cZc8
- community classic, 26 min | https://www.youtube.com/watch?v=lCyQ717DuzQ
- with vs without skills (Spanish) | https://www.youtube.com/watch?v=VWEa-zeL2fY
- character animation test | https://www.youtube.com/watch?v=qhi9A_j-1Gc
- car rigging | https://www.youtube.com/watch?v=e_s84dETgKA
- Claude Code workflow | https://www.youtube.com/watch?v=4cReMIc1qgQ
- 3D animator workflow | https://www.youtube.com/watch?v=f2yPoquP77g
- 4 free pieces (short) | https://www.youtube.com/shorts/aH3_Vgn5Qjc
- more ids: 0kMhtqYBe4Y 2Ardi_JpgIM l7AHwQSyeK8 GFtIO3U6qcI Ci9Xc-VPc04 kdYfEudqpis cGxweONcSUY PBSvqfx4gwQ DqgKuLYUv00 I29rn92gkC4 FDRb03XPiRo
- Udemy course (paid) | https://www.udemy.com/course/automation-with-claude-ai-for-creative-work/

## Reads
- MeltFlex tested comparison* | https://www.meltflexai.com/blog/connect-claude-to-blender | best single read
- MindStudio limits* | https://www.mindstudio.ai/blog/claude-blender-mcp-real-world-performance
- StraySpark comparison* | https://www.strayspark.studio/blog/official-blender-mcp-server-comparison-2026 | vendor-biased
- Voyager official vs community | https://voyager.so/blog/blender-mcp
- Qiita official + Claude Code (JP) | https://qiita.com/zukka/items/6492cf4db31e374850e2
- Classmethod Desktop + Code | https://dev.classmethod.jp/en/articles/claude-blender-connector-desktop-and-code/
- mcp.so Claude Code setup | https://mcp.so/blog/blender-mcp-claude-code-setup
- privacy comparison | https://blendervisualinvestigation.com/knowledge-base/docs/addons/blender-mcp/
- arjun988 review | https://thakicloud.com/tech-blog/en/agentops/blender-skills-agent/
- b2renger tutorial | https://github.com/b2renger/blender-mcp_experiments
- runoob (CN) troubleshooting | https://www.runoob.com/ai-agent/ai-3d-blender.html
- Zenn (JP) internals | https://zenn.dev/yuichi_ai/articles/2d689e5f848068
- Meshy + MCP | https://www.meshy.ai/tutorials/blender-mcp-guide
- Sprixen game-dev MCP ranking | https://sprixen.com/blog/best-mcp-servers-for-game-development-2026
- best-of-mcp-servers | https://github.com/tolkonepiu/best-of-mcp-servers
- Snyk 3D skills | https://snyk.io/articles/top-claude-skills-3d-modeling-game-dev-shader-programming

## Research
- BlenderGym | https://arxiv.org/abs/2504.01786 | VLMs weak at novice-level edits; balance generate vs verify
- SceneCraft | https://arxiv.org/abs/2403.01248 | scene graph + constraints + self-critique + library
- BlenderAlchemy | https://arxiv.org/abs/2404.17672 | VLM-guided material/lighting edits
- LL3M | https://arxiv.org/abs/2508.08228 | multi-agent Blender script writing
- VIGA / BlenderBench | https://arxiv.org/abs/2601.11109
- 3DHarnessBench | https://arxiv.org/abs/2609.06535
- BlenderWorld | https://arxiv.org/abs/2610.23986
- BlenderFORGE | https://arxiv.org/abs/2611.10768
- SimWorlds | https://arxiv.org/abs/2607.01766
- Planner-Actor-Critic | https://arxiv.org/abs/2601.05016

## Community
- devtalk MCP architecture + security | https://devtalk.blender.org/t/3d-agent-blender-ai-assistant-built-a-multi-agent-system-on-top-of-blenders-mcp-and-python-api-and-sharing-architecture-learnings-for-the-lab-discussion/44260
- devtalk early MCP thread | https://devtalk.blender.org/t/i-would-love-to-help-write-the-mcp-for-blender-can-i-get-involved-in-that/43367
- BlenderArtists launch debate | https://blenderartists.org/t/from-blender-mcp-to-3d-agent-anthropic-partners-with-blender-claude-ai-connector-now-official/1639106
- Polycount pipeline thread | https://polycount.com/discussion/238781/blendermcp-pro-ai-pipeline-tool-for-blender-asset-validation-batch-export-game-engine-prep
- GitHub Discussions | https://github.com/ahujasid/mcp-for-blender/discussions
- X reusable prompt | https://x.com/rewind02/status/2116918597658305001
- X A-Z animation guide | https://x.com/kirillk_web3/status/2114393429874479530
- X original launch | https://x.com/sidahuj/status/1899460492999184534
- X Python 3.11 fix | https://x.com/LucioFulci74/status/2043242029279486372
- Reddit: BLOCKED for Claude tools; threads listed at https://trendshift.io/repositories/74897

## Security
- CVE-2026-66004 path traversal | https://nvd.nist.gov/vuln/detail/cve-2026-66004
- CVE-2026-10688/10661/10662 | https://nvd.nist.gov/vuln/detail/CVE-2026-10688 | old blender-mcp; update
- StraySpark safety checklist | https://www.strayspark.studio/blog/is-blender-mcp-safe-security-guide-2026

## Top fixes
- Official: Blender 5.1+ and Preferences > System > Allow Online Access
- Drag the official install link in twice
- Start server in add-on prefs; enable Auto Start
- Only one Blender MCP add-on (port 9876)
- Fully quit Claude Desktop, then reopen
- claude.ai web cannot connect
- uvx blender-mcp = community; official needs uvx --from git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp blender-mcp
- "Server disconnected": pin Python 3.11
- uv via official installer; uv cache clean blender-mcp && uvx --refresh blender-mcp
- Work on copies: arbitrary Python
