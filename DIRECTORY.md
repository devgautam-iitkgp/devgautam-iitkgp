# Blender + Claude MCP: full directory

Checked 2026-11-23. Verified = page opened that day. Stars from the live GitHub page when verified. AI agents: use AGENT_INDEX.md (or the doc's Agent index tab) instead; it is shorter.

## Quick pick

- **Official Blender Lab connector**: scene analysis, cleanup, batch scripts, explaining node setups. Free, Blender 5.1+, installs from Claude Desktop.
- **Community MCP for Blender**: building scenes from prompts, Poly Haven/Sketchfab assets, AI 3D generation, Blender 3.0+.
- **Fully local models**: blender-open-mcp. **No MCP at all**: Claude Code + `blender --background --python script.py`.
- **Add a skill pack**: arjun988/blender-skills (community server, game assets) or ra100/blender-claude-plugin (official server).
- Every option: one Blender MCP add-on at a time (port 9876); Claude Desktop or Claude Code only, never claude.ai web; work on copies, since all of them can run arbitrary Python.

## Official (Blender Lab + Claude connector)

| Name | Notes | Verified |
| --- | --- | --- |
| [Blender Lab MCP Server page](https://www.blender.org/lab/mcp-server/) | Official docs + add-on install link (drag into Blender twice: 1st adds the lab repo, 2nd installs). Needs Blender 5.1+ and Allow Online Access. | no |
| [Blender Lab repo](https://projects.blender.org/lab/blender_mcp) | GPL-3.0+. Add-on + MCP server, ~26 tools (scene summaries, screenshots, bundled manual/API docs, Python exec, background jobs). Latest v1.0.3 (11 Sep 2026). Maintained by Blender core devs. | yes |
| [Claude Blender connector](https://claude.com/connectors/blender) | Claude Desktop > Customize > Connectors > Blender > Add. Any plan incl. Free. Not usable from claude.ai web. | no |
| [Anthropic tutorial (Claude Academy)](https://academy.claude.com/tutorials/using-the-blender-connector-in-claude) | Official steps + 4 example uses. Says Blender 4.2+, but the add-on manifest requires 5.1+. | yes |
| [Claude for Creative Work announcement](https://www.anthropic.com/news/claude-for-creative-work) | 28 Apr 2026 launch of 9 creative connectors incl. Blender. | no |
| [Official server via Claude Code](https://qiita.com/zukka/items/6492cf4db31e374850e2) | uvx --from "git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp" blender-mcp  (plain `uvx blender-mcp` runs the COMMUNITY server: same command name). | no |

## Free MCP servers and bridges

| Name | Stars | Notes | Verified |
| --- | --- | --- | --- |
| [MCP for Blender (ahujasid, formerly blender-mcp)](https://github.com/ahujasid/mcp-for-blender) | 35.4k | MIT. The community default. Blender 3.0+. Poly Haven, Sketchfab, Poly Pizza, Rodin, Hunyuan3D, Tripo, screenshots. Arbitrary Python on by default (safe mode opt-in). Install: claude mcp add blender uvx mcp-for-blender. Discord: discord.gg/SNqPn4TcKQ | yes |
| [blenderwright (formerly blend-ai)](https://github.com/jabberwock/blend-ai) | 187 | MIT. 276 tools across 32 modules. Blender 5.2 LTS only. uvx blenderwright | yes |
| [blender-open-mcp](https://github.com/dhakalnirajan/blender-open-mcp) | 114 | MIT. Local/any LLM backend: Ollama, LM Studio, llama.cpp, OpenAI-compatible (vLLM, OpenRouter, Groq...). pip install -e from clone. | yes |
| [dcc-mcp-blender](https://github.com/dcc-mcp/dcc-mcp-blender) | 53 | MIT. Add-on embeds an MCP server with typed tools (mesh, UV, rig, materials, render). Blender 4.5+. pip install dcc-mcp-blender | yes |
| [Meshwire (RFingAdam)](https://github.com/RFingAdam/mcp-blender) | 34 | AGPL-3.0. 225 tools incl. sculpt, animation, AI 3D gen, MSFS content. Blender 4.2-5.2, CI on 4.5/5.2 LTS. uvx meshwire | yes |
| [blender-mcp-server (djeada)](https://github.com/djeada/blender-mcp-server) | 24 | MIT. 22-27 tools (README inconsistent). Own add-on; protocol not compatible with others. | yes |
| [blender-agent (ptrthomas)](https://github.com/ptrthomas/blender-agent) | 11 | No MCP: Python over HTTP (curl localhost:5656) + bundled Agent Skills. Blender 5.0+. | yes |
| [Blender MCP Plus](https://glama.ai/mcp/servers/dq930e7q6b) | - | Extends the OFFICIAL add-on with a Poly Haven library; one add-on, one port. Tested on 5.2.2. | no |
| [sandraschi/blender-mcp](https://glama.ai/mcp/servers/sandraschi/blender-mcp) | - | 80+ tools, .mcpb drag-in install for Claude Desktop, VRM/VRChat validation. | no |
| [Security-hardened fork (soozs1)](https://glama.ai/mcp/servers/soozs1/Blender-MCP) | - | Fork of ahujasid with telemetry removed, token auth, loopback-only binding. | no |
| [CommonSenseMachines/blender-mcp](https://github.com/CommonSenseMachines/blender-mcp) | - | CSM.ai text-to-3D, asset search, text-to-animation with auto-rig. Repo page could not be opened on check date. | no |
| [Scenario for Blender](https://www.claudemarketplace.net/mcp/blender-plugin) | - | Blender 5.0+ extension: AI images/video/3D/PBR/HDRI + local MCP server. Needs Scenario account. | no |
| [blender-ai-mcp (ARCHIVED)](https://github.com/PatrykIti/blender-ai-mcp) | 67 | Apache-2.0. README says archived/unmaintained. Listed only because older guides recommend it. | yes |

## Paid servers

| Name | Notes | Verified |
| --- | --- | --- |
| [Blender MCP Pro (abyo)](https://blender-mcp-pro.abyo.net) | $5/mo or $15 one-time, 7-day trial. 110-120+ tools. Blender 3.6 LTS+. Python exec, no sandbox described; online licence check (72h cache). | yes |
| [BlenderMCP Pro (Anvil, Superhive)](https://superhivemarket.com/products/blendermcp-pro) | Different product from the above. v2.5.2, agent workflows, spatial checks. | no |
| [StraySpark Blender MCP Server](https://www.strayspark.studio/products/blender-mcp-server) | $55.99 Personal / $174.99 Professional (Nov 2026; was $79.99-$249.99). Code exec off by default, path jails, audit log. Blender 5.1+ (5.2 LTS primary). | yes |

## Skill packs and plugins

| Name | Stars | Notes | Verified |
| --- | --- | --- | --- |
| [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | 4.5k | MIT, v1.3.0, 94 skills + 175 refs. Game-asset pipeline: blockout to Unity/Unreal/Godot, art-style + genre direction. Entry skill: blender-director. Needs COMMUNITY server (BlenderMCP add-on). Install: git clone, copy .claude/skills into project; or /plugin marketplace add arjun988/blender-skills | yes |
| [kevinbadi/blender-skills](https://github.com/kevinbadi/blender-skills) | 288 | 16 skills: product shots, turntables, camera moves, Poly Haven scenes, image-to-3D (Meshy key), Three.js export. Needs community server. Blender 5.x. | yes |
| [EL4CTEO/blender-skills](https://github.com/el4cteo/blender-skills) | 164 | MIT. 22 skills (search snippets claim 28 and 2.7k stars; live page showed 22/164). Pro workflows, Blender 5.2 LTS+. /plugin marketplace add EL4CTEO/blender-skills then /plugin install blender-agent-skills@blender-agent-skills | yes |
| [ra100/blender-claude-plugin](https://github.com/ra100/blender-claude-plugin) | 11 | MIT. 8 skills (geometry/shader/compositing nodes, Python, rigging, modifiers, physics, rendering). Uses the OFFICIAL server; falls back to bpy scripts. claude plugin marketplace add ra100/blender-claude-plugin | yes |
| [jithinolickal/blender](https://github.com/jithinolickal/blender) | 9 | Apache-2.0. 1 skill: parametric design, materials, lighting, renders + MCP troubleshooting. Community server. claude plugin marketplace add jithinolickal/blender | yes |
| [mromidev/claude-blender-skills](https://github.com/mromidev/claude-blender-skills) | 2 | MIT. 3 film/animation skills (forest, car film) with real scripts; uses its own bridge.py, not MCP. | yes |
| [scenario-labs/skills (Blender experts)](https://github.com/scenario-labs/skills) | - | scenario-blender-expert router + hard-surface, rigging, sculpting skills; headless or via MCP; tests pass on 5.2.1. | no |
| [Dev-GOM blender-toolkit](https://github.com/Dev-GOM/claude-code-marketplace) | - | Experimental plugin: WebSocket control (not MCP), Mixamo retargeting. /plugin install blender-toolkit@dev-gom-plugins | no |
| [vladmdgolam blender-mcp skill](https://github.com/vladmdgolam/agent-skills) | - | When to use MCP tools vs Python; headless export. npx skills add vladmdgolam/agent-skills --skill blender-mcp | no |
| [Hermes Agent blender-mcp skill](https://tessl.io/registry/skills/github/NousResearch/hermes-agent/blender-mcp/review) | - | bpy recipes + pitfalls references; standard SKILL.md. | no |
| [TMHSDigital/Blender-Developer-Tools](https://github.com/TMHSDigital/Blender-Developer-Tools) | - | 8 skills, rules, snippets for add-on dev; Blender 5.1 (4.5 LTS fallback). | no |
| [SamuelAsherRivello/ai-skills-blender](https://skillsmp.com/ar/creators/samuelasherrivello/ai-skills-blender) | - | ~28 skills for editable assets via Blender MCP (image-to-model, relief). | no |
| [rehan-remade/animated-asset-skill](https://github.com/rehan-remade/animated-asset-skill) | - | One sentence to rigged animated voxel creature: fal + Hunyuan-3D + headless Blender to glTF. | no |
| [Patch-gg/trompe](https://github.com/Patch-gg/trompe) | - | Blockout in Blender, then texture with image models by projecting 128 views. | no |
| [Other single skills](https://skills.sh/terminalskills/skills/blender-scripting) | - | TerminalSkills blender-scripting (headless), alivirgo Major-AI-Skills blender, openaec-foundation (BIM/Bonsai), phuetz code-buddy, sfkislev/flue, digitalsamba video toolkit, majidmanzarpour/blender-game-skills. | no |
| [Lead: Rehan Sheikh 29-skill pack (patch)](https://x.com/rehan_shei) | - | Announced on X (modeling, rigging, hair, sims, lighting, export); repo not yet found. | no |

## Videos

| Name | Notes | Verified |
| --- | --- | --- |
| [I Tested Claude's Official Blender Connector](https://www.youtube.com/watch?v=b5F-yNG4lds) | Aidan Stanik, 28 Apr 2026, 12 min. Official; Claude Code part at 3:14. | no |
| [How To Connect Claude To Blender (Blender MCP Setup)](https://www.youtube.com/watch?v=0PdIuWlxhHA) | Think Tutorial, 5 min, official on Mac; FAQ in comments. | no |
| [How to Setup Blender MCP with Claude, Codex & Gemini CLI](https://www.youtube.com/watch?v=YQBO5de575Y) | Official server with 3 clients. | no |
| [How to Connect Blender to Claude AI (Official Method)](https://www.youtube.com/watch?v=WaGIc9KJRwE) | Official, no config files. | no |
| [Claude + Blender (Free MCP Setup): Build 3D Scenes](https://m.youtube.com/watch?v=rohl0_7cZc8) | Nov 2026. Community server, 3 builds with code on 5.3, safety settings. | no |
| [Create 3D with Claude AI with Blender MCP (26 min)](https://www.youtube.com/watch?v=lCyQ717DuzQ) | DesignCode, Mar 2025. Classic community-server walkthrough. | no |
| [Claude en Blender: con y sin 22 skills](https://www.youtube.com/watch?v=VWEa-zeL2fY) | Spanish. Same prompt with vs without skills. | no |
| [Can Claude Animate Characters in Blender?](https://www.youtube.com/watch?v=qhi9A_j-1Gc) | Animation test. | no |
| [I Used Claude AI to Rig a Car in Blender](https://www.youtube.com/watch?v=e_s84dETgKA) | Rigging over MCP. | no |
| [3D Modeling with Claude Code: A Practical Blender Workflow](https://www.youtube.com/watch?v=4cReMIc1qgQ) | Claude Code as agent controller. | no |
| [Turn Claude Code into a 3D Animator](https://www.youtube.com/watch?v=f2yPoquP77g) | Animated videos from prompts. | no |
| [Claude Code builds your 3D scene: the 4 free pieces](https://www.youtube.com/shorts/aH3_Vgn5Qjc) | Short: Blender + MCP for Blender + arjun988 skills setup. | no |
| [More videos](https://www.youtube.com/watch?v=0kMhtqYBe4Y) | Also: 2Ardi_JpgIM (2-min setup), l7AHwQSyeK8, GFtIO3U6qcI (Spanish official), Ci9Xc-VPc04, kdYfEudqpis (Roblox), cGxweONcSUY (Korean CAD), PBSvqfx4gwQ (Windows), demos DqgKuLYUv00 / I29rn92gkC4 / FDRb03XPiRo. | no |
| [Udemy: Automation with Claude AI for Creative Work](https://www.udemy.com/course/automation-with-claude-ai-for-creative-work/) | Paid course: Blender MCP setup, product animation, skill-based image-to-3D pipeline. | no |

## Articles and guides

| Name | Notes | Verified |
| --- | --- | --- |
| [How to Connect Claude to Blender (Tested) — MeltFlex](https://www.meltflexai.com/blog/connect-claude-to-blender) | Best single read: both servers on real briefs, time + cost (~$0.7/brief), fix list. | yes |
| [What It Can and Can't Do — MindStudio](https://www.mindstudio.ai/blog/claude-blender-mcp-real-world-performance) | Good: blockouts, batch scripts, hard-surface. Weak: organic, topology, rigging, complex nodes. | yes |
| [Blender MCP Servers Compared — StraySpark](https://www.strayspark.studio/blog/official-blender-mcp-server-comparison-2026) | Tools, prices, exec defaults, official release history. Vendor-biased. | yes |
| [Official vs community + setup — Voyager](https://voyager.so/blog/blender-mcp) | Oct 2026 stats; devtalk security debate summary. | no |
| [Claude Code + official MCP desk build (Japanese) — Qiita](https://qiita.com/zukka/items/6492cf4db31e374850e2) | Blender 5.1.2. Explains the official/community name clash and pitfalls. | no |
| [Official connector on Desktop + Code — Classmethod](https://dev.classmethod.jp/en/articles/claude-blender-connector-desktop-and-code/) | Add-on v1.0.0 hands-on, `claude mcp list` check. | no |
| [Blender MCP with Claude Code — mcp.so](https://mcp.so/blog/blender-mcp-claude-code-setup) | --scope user, /mcp check, common errors. | no |
| [Blender MCP knowledge base — Blender Visual Investigation](https://blendervisualinvestigation.com/knowledge-base/docs/addons/blender-mcp/) | Servers compared by privacy posture. | no |
| [Blender Skills 94-pack review — ThakiCloud](https://thakicloud.com/tech-blog/en/agentops/blender-skills-agent/) | Independent check of arjun988 claims. | no |
| [blender-mcp_experiments — b2renger](https://github.com/b2renger/blender-mcp_experiments) | Full tutorial: architecture, uv, troubleshooting table, Ollama. | no |
| [Chinese tutorials (CSDN, runoob)](https://www.runoob.com/ai-agent/ai-3d-blender.html) | Also deepseek.csdn.net MCP for Blender guide; runoob has a good troubleshooting list. | no |
| [Japanese (Zenn)](https://zenn.dev/yuichi_ai/articles/2d689e5f848068) | Internals of the community server; also zenn.dev/yurinchi (Godot + Blender MCP game). | no |
| [Meshy + Blender MCP guide](https://www.meshy.ai/tutorials/blender-mcp-guide) | Vendor: official server + Meshy asset generation. | no |
| [Best MCP servers for game dev 2026 — Sprixen](https://sprixen.com/blog/best-mcp-servers-for-game-development-2026) | Ranking with API-read stars (1 Nov 2026). | no |
| [best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers) | Weekly-ranked MCP list (Art & Culture section). | no |
| [Top Claude skills for 3D and game dev — Snyk](https://snyk.io/articles/top-claude-skills-3d-modeling-game-dev-shader-programming) | Skills vs MCP explained; install paths; review skills before installing. | no |

## Research papers and benchmarks

| Name | Notes | Verified |
| --- | --- | --- |
| [BlenderGym (CVPR 2025)](https://arxiv.org/abs/2504.01786) | Benchmark: even top VLMs struggle on edits easy for novice Blender users; split compute between generation and verification. | no |
| [SceneCraft (ICML 2024)](https://arxiv.org/abs/2403.01248) | Text to Blender code via scene graph + constraint solver + VLM self-critique + learned function library. | no |
| [BlenderAlchemy](https://arxiv.org/abs/2404.17672) | VLM-guided editing of materials/lighting programs. | no |
| [LL3M: Large Language 3D Modelers](https://arxiv.org/abs/2508.08228) | Multi-agent plan/retrieve/write/debug/refine of Blender scripts for assets. | no |
| [VIGA + BlenderBench](https://arxiv.org/abs/2601.11109) | Vision-as-inverse-graphics agent; new BlenderBench benchmark. | no |
| [3DHarnessBench](https://arxiv.org/abs/2609.06535) | Agentic 3D-to-code benchmark; cites both Blender MCP servers. | no |
| [BlenderWorld](https://arxiv.org/abs/2610.23986) | Benchmark for visual agents creating 3D from real-world references. | no |
| [BlenderFORGE](https://arxiv.org/abs/2611.10768) | Optimizing reactive 3D-editing ability of MLLMs. | no |
| [SimWorlds](https://arxiv.org/abs/2607.01766) | Multi-agent text-to-4D editable Blender projects. | no |
| [Planner-Actor-Critic 3D modeling](https://arxiv.org/abs/2601.05016) | Built on blender-mcp; notes MCP tool limits and script failures. | no |

## Forums, X and community

| Name | Notes | Verified |
| --- | --- | --- |
| [Blender devtalk: 3D-Agent + MCP architecture thread](https://devtalk.blender.org/t/3d-agent-blender-ai-assistant-built-a-multi-agent-system-on-top-of-blenders-mcp-and-python-api-and-sharing-architecture-learnings-for-the-lab-discussion/44260) | Developer-forum discussion with Blender devs; security debate. | no |
| [Blender devtalk: helping write the MCP](https://devtalk.blender.org/t/i-would-love-to-help-write-the-mcp-for-blender-can-i-get-involved-in-that/43367) | Nov 2025 thread before the official server. | no |
| [BlenderArtists: connector launch thread](https://blenderartists.org/t/from-blender-mcp-to-3d-agent-anthropic-partners-with-blender-claude-ai-connector-now-official/1639106) | Heated for/against AI debate. | no |
| [Polycount: BlenderMCP Pro pipeline thread](https://polycount.com/discussion/238781/blendermcp-pro-ai-pipeline-tool-for-blender-asset-validation-batch-export-game-engine-prep) | Pipeline-focused discussion. | no |
| [GitHub Discussions (community server)](https://github.com/ahujasid/blender-mcp/discussions) | Q&A and showcase. | no |
| [X: reusable modeling prompt (@rewind02)](https://x.com/rewind02/status/2116918597658305001) | Inspect, silhouette, geometry, materials, previews, self-correct. | no |
| [X: Claude + Blender A-Z animation guide (@kirillk_web3)](https://x.com/kirillk_web3/status/2114393429874479530) | Sandbox route vs official connector route. | no |
| [X: original launch (@sidahuj)](https://x.com/sidahuj/status/1899460492999184534) | 11 Mar 2025 dragon demo. | no |
| [X: Python 3.11 fix (@LucioFulci74)](https://x.com/LucioFulci74/status/2043242029279486372) | "Server disconnected" fixed by pinning --python 3.11. | no |
| [Reddit (not reachable by Claude tools)](https://trendshift.io/repositories/74897) | Reddit is blocked for Claude's fetch + search. Trendshift lists arjun988 posts on r/TechnicalArtist, r/kiroIDE, r/coolgithubprojects, r/claudeskills. | no |

## Security

| Name | Notes | Verified |
| --- | --- | --- |
| [CVE-2026-66004 (path traversal)](https://nvd.nist.gov/vuln/detail/cve-2026-66004) | ahujasid download_polyhaven_asset; 24 Jul 2026. | no |
| [CVE-2026-10688 / 10661 / 10662](https://nvd.nist.gov/vuln/detail/CVE-2026-10688) | Code injection, injection, SSRF in old blender-mcp (<= 7636d13). Update to mcp-for-blender. | no |
| [Is Blender MCP safe? — StraySpark](https://www.strayspark.studio/blog/is-blender-mcp-safe-security-guide-2026) | 10-point checklist for any server (vendor). | no |

## Launch news and background

| Name | Notes | Verified |
| --- | --- | --- |
| [Blender Foundation: funding changed to one-time donation](https://gamedev.net/news/3088-upcoming-blender-development-fund-and-ai-policies/) | 1 May 2026, after community backlash; no gen-AI features in Blender itself. | no |
| [CG Channel: patronage downgraded](https://www.cgchannel.com/?p=175793) | 4 May 2026 explainer. | no |
| [MacRumors: creative connectors launch](https://macrumors.com/2026/04/28/claude-creative-tool-connectors) | 28 Apr 2026. | no |

## Troubleshooting

1. Official add-on: Blender 5.1+ and Edit > Preferences > System > Allow Online Access
2. Drag the official install link in twice (1st adds repo)
3. Start the server in add-on prefs; enable Auto Start
4. Only one Blender MCP add-on enabled (most use port 9876)
5. Fully quit Claude Desktop (not just close window), then reopen
6. claude.ai web cannot connect; use Claude Desktop or Claude Code
7. `uvx blender-mcp` = community server; official needs uvx --from git+https://projects.blender.org/lab/blender_mcp.git#subdirectory=mcp blender-mcp
8. "Server disconnected": pin Python 3.11 (uvx --python 3.11 ...)
9. Install uv with its official installer, not pip; clear cache: uv cache clean blender-mcp && uvx --refresh blender-mcp
10. Work on copies: every server can run arbitrary Python

## Coverage and limits

Swept: web search, GitHub pages, skills.sh, claudepluginhub, claudemarketplaces, skillsdirectory, skillsllm, glama, mcp.so, mcpservers.org, arXiv, NVD, Blender devtalk, BlenderArtists, Polycount, Qiita, Zenn, CSDN, YouTube and X (site-limited search). Not reachable: Reddit (blocked for Claude tools), Discord (login), GitHub API (not enabled in the building session). A GitHub search for "blender mcp" returned 1,132 repos in Oct 2026; only notable ones are listed.
