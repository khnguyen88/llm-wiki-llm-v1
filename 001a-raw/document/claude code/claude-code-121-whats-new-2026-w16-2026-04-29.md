<!--
url: https://code.claude.com/docs/en/whats-new/2026-w16
download_date: 2026-04-29
website: claude-code
webpage: whats-new-2026-w16
-->

# Whats New 2026 W16

[Skip to main content](https://code.claude.com/docs/en/whats-new/2026-w16#content-area)
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)
English
Search...
⌘KAsk AI
  * [Claude Developer Platform](https://platform.claude.com/)
  * [Claude Code on the Web](https://claude.ai/code)
  * [Claude Code on the Web](https://claude.ai/code)


Search...
Navigation
What's New
Week 16 · April 13–17, 2026
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### What's New
  * [What's new](https://code.claude.com/docs/en/whats-new)
  * [Week 17 · Apr 20–24](https://code.claude.com/docs/en/whats-new/2026-w17)
  * [Week 16 · Apr 13–17](https://code.claude.com/docs/en/whats-new/2026-w16)
  * [Week 15 · Apr 6–10](https://code.claude.com/docs/en/whats-new/2026-w15)
  * [Week 14 · Mar 30 – Apr 3](https://code.claude.com/docs/en/whats-new/2026-w14)
  * [Week 13 · Mar 23–27](https://code.claude.com/docs/en/whats-new/2026-w13)


What's New
# Week 16 · April 13–17, 2026
Copy page
Claude Opus 4.7 with the new xhigh effort level, Routines on Claude Code on the web, /ultrareview cloud code review, a /usage breakdown that shows what’s driving your limits, and native binaries replacing the bundled JavaScript.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Releases [v2.1.105 → v2.1.113](https://code.claude.com/docs/en/changelog#2-1-105)5 features · April 13–17
Claude Opus 4.7new model
Anthropic’s strongest coding model yet is now the default on Max and Team Premium, and available everywhere else from `/model`. It adds a new `xhigh` effort level that sits between `high` and `max`: best results for most coding and agentic tasks, applied as the default the first time you switch to 4.7. `/effort` now opens an interactive arrow-key slider when you call it without arguments, so you can dial intelligence against speed without remembering the level names.
Switch model and effort in one go:
Claude Code

```
> /model opus
> /effort xhigh

```

[Model config: effort levels](https://code.claude.com/docs/en/model-config#adjust-effort-level)
Routinesweb
Templated cloud agents that fire on a schedule, a GitHub event, or an API call. Define a routine once on Claude Code on the web with a prompt, the repos it can touch, and the connectors it needs, then let PR-opened, release-published, or your own webhook trigger it without your machine running. The trigger picker now covers GitHub events with optional filters and gives every routine a tokened `/fire` endpoint for external systems.
![Creating a routine on Claude Code on the web with schedule, GitHub event, and API triggers](https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/routines.png?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=2ba818ea9280c549511cb48b9b4d1dc5)
Create one from the web UI, or scaffold from your terminal:
Claude Code

```
> /schedule daily PR review at 9am

```

[Routines guide](https://code.claude.com/docs/en/routines)
/usage breakdownCLI
More visibility into where your Claude Code usage goes. `/usage` now shows what’s driving your limits: parallel sessions, subagents, cache misses, and long context, each with a percentage of your last 24 hours and a tip to optimize it. Press `d` or `w` to switch between day and week views.
![The /usage command showing a breakdown of what's contributing to limits usage](https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/usage.png?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=792a4b43cbef4e2931974831f076bca6)
Run it any time:
Claude Code

```
> /usage

```

[Commands reference](https://code.claude.com/docs/en/commands)
/ultrareviewv2.1.111
Comprehensive code review in the cloud. Ultrareview fans your branch out across parallel reviewers on Claude Code on the web, runs an adversarial critique pass over each finding, and returns a verified findings report while your terminal stays free. Call it with no arguments to review your current branch, or pass a PR number to fetch and review that PR. The launch dialog now shows a diffstat so you know what’s going up before you confirm.
Review the branch you’re on:
Claude Code

```
> /ultrareview

```

Or point it at a PR:
Claude Code

```
> /ultrareview 1234

```

[Ultrareview guide](https://code.claude.com/docs/en/ultrareview)
Native binariesv2.1.113
The `claude` CLI now spawns a native per-platform binary instead of bundled JavaScript, so the installed `claude` command no longer invokes Node. The npm package pulls the right binary in through an optional dependency such as `@anthropic-ai/claude-code-darwin-arm64`, so your install command doesn’t change. The standalone installer already shipped this binary; npm now matches it.
Upgrade and check what you’re running:

```
claude update
claude --version

```

[Setup guide](https://code.claude.com/docs/en/setup)
Other wins
[Auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) is now available for Max subscribers on Opus 4.7, and the `—enable-auto-mode` flag is no longer required
[Session recap](https://code.claude.com/docs/en/interactive-mode#session-recap) shows a one-line summary of what happened while you were away; run `/recap` on demand or turn it off from `/config`
New `/tui` command and `tui` setting switch between classic and flicker-free rendering mid-conversation; focus view moved from `Ctrl+O` to its own `/focus` command
Push notification tool: with [Remote Control](https://code.claude.com/docs/en/remote-control) connected and “Push when Claude decides” enabled, Claude can ping your phone when it needs you
Plugins can ship background watchers via a top-level `monitors` manifest key that auto-arms at session start or on skill invoke
”Auto (match terminal)” option in `/theme` follows your terminal’s dark/light mode
`/fewer-permission-prompts` scans your transcripts for common read-only Bash and MCP calls and proposes an allowlist for `.claude/settings.json`
Claude can now discover and run built-in commands like `/init`, `/review`, and `/security-review` via the Skill tool
`PreCompact` hooks can block compaction by exiting with code 2 or returning `“decision”:“block”`
`ENABLE_PROMPT_CACHING_1H` opts API key, Bedrock, Vertex, and Foundry users into 1-hour prompt cache TTL
`sandbox.network.deniedDomains` setting carves specific domains out of a broader `allowedDomains` wildcard
`/undo` is now an alias for `/rewind`, and `/proactive` is an alias for `/loop`
Hardened Bash permissions: deny rules now match through `env`/`sudo`/`watch` wrappers, and `Bash(find:*)` allow rules no longer auto-approve `-exec` or `-delete`
[Full changelog for v2.1.105–v2.1.113 →](https://code.claude.com/docs/en/changelog#2-1-105)
Was this page helpful?
YesNo
[Week 17 · Apr 20–24](https://code.claude.com/docs/en/whats-new/2026-w17)[Week 15 · Apr 6–10](https://code.claude.com/docs/en/whats-new/2026-w15)
⌘I
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
Company
[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)
Help and security
[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)
Learn
[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)
Terms and policies
[Privacy choices](https://code.claude.com/docs/en/whats-new/2026-w16)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
