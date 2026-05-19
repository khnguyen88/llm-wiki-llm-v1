<!--
url: https://code.claude.com/docs/en/whats-new/2026-w17
download_date: 2026-04-29
website: claude-code
webpage: whats-new-2026-w17
-->

# Whats New 2026 W17

[Skip to main content](https://code.claude.com/docs/en/whats-new/2026-w17#content-area)
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
Week 17 · April 20–24, 2026
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### What's New
  * [What's new](https://code.claude.com/docs/en/whats-new)
  * [Week 17 · Apr 20–24](https://code.claude.com/docs/en/whats-new/2026-w17)
  * [Week 16 · Apr 13–17](https://code.claude.com/docs/en/whats-new/2026-w16)
  * [Week 15 · Apr 6–10](https://code.claude.com/docs/en/whats-new/2026-w15)
  * [Week 14 · Mar 30 – Apr 3](https://code.claude.com/docs/en/whats-new/2026-w14)
  * [Week 13 · Mar 23–27](https://code.claude.com/docs/en/whats-new/2026-w13)


What's New
# Week 17 · April 20–24, 2026
Copy page
/ultrareview opens as a research preview, automatic session recaps when you return to a terminal, custom color themes you can build and ship in plugins, and a redesigned Claude Code on the web.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Releases [v2.1.114 → v2.1.119](https://code.claude.com/docs/en/changelog#2-1-114)4 features · April 20–24
/ultrareviewresearch preview
Now in public research preview. Ultrareview runs a fleet of bug-hunting agents in the cloud against your branch or a PR, and findings land back in the CLI or Desktop automatically. Run it before merging critical changes such as auth or data migrations.
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
Session recapCLI
Switch focus away from a session and come back to a one-line recap of what happened while you were gone. Helpful for staying in flow while running several Claude sessions at once.
Generate a recap on demand, or turn the automatic one off from `/config`:
Claude Code

```
> /recap

```

[Interactive mode: session recap](https://code.claude.com/docs/en/interactive-mode#session-recap)
Custom themesv2.1.118
Build and switch between named color themes from `/theme`, or hand-edit JSON files in `~/.claude/themes/`. Each theme picks a base preset and overrides only the tokens you care about. Plugins can ship themes too.
Open the theme picker and create a new one:
Claude Code

```
> /theme

```

[Terminal config: create a custom theme](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme)
Claude Code on the webweb
A new look for [claude.ai/code](https://claude.ai/code) that matches the redesigned desktop app: sessions sidebar, drag-and-drop layout, and a refreshed routines view. Key parts were rebuilt for quicker responses and a more reliable experience.
![Claude Code on the web redesign overview: new UI, speed and reliability, work across web, mobile, and CLI](https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/web-redesign.jpeg?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=a2aca1b49e295b7337f5779038db8e2c)
[Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)
Other wins
[Vim visual mode](https://code.claude.com/docs/en/interactive-mode#vim-editor-mode): press `v` for character selection or `V` for line selection in the prompt input, with operators and visual feedback
Hooks can now call MCP tools directly via [`type: “mcp_tool”`](https://code.claude.com/docs/en/hooks#mcp-tool-hook-fields), so a hook can hit an already-connected server without spawning a process
`/cost` and `/stats` are merged into [`/usage`](https://code.claude.com/docs/en/commands); the old names still work as typing shortcuts that open the relevant tab
`/config` changes (theme, editor mode, verbose, and similar) now persist to `~/.claude/settings.json` and follow the same project/local/policy precedence as other [settings](https://code.claude.com/docs/en/settings)
[Forked subagents](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation) can be enabled on external builds with `CLAUDE_CODE_FORK_SUBAGENT=1`: a fork inherits your full conversation context instead of starting fresh
Default [effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level) for Pro and Max subscribers on Opus 4.6 and Sonnet 4.6 is now `high` (was `medium`)
Native macOS and Linux builds replace the `Glob` and `Grep` tools with embedded `bfs` and `ugrep` available through Bash, for faster searches without a separate tool round-trip
`—from-pr` now accepts GitLab merge request, Bitbucket pull request, and GitHub Enterprise PR URLs in addition to github.com
Auto mode: include `“$defaults”` in [`autoMode.allow`, `soft_deny`, or `environment`](https://code.claude.com/docs/en/auto-mode-config) to add custom rules alongside the built-in list instead of replacing it
New [`claude plugin tag`](https://code.claude.com/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution) command creates release git tags for plugins with version validation
Opus 4.7 sessions now compute against the model’s native 1M context window, fixing inflated `/context` percentages and premature autocompaction
`/resume` on large sessions is up to 67% faster and now offers to summarize stale, large sessions before re-reading them
[Full changelog for v2.1.114–v2.1.119 →](https://code.claude.com/docs/en/changelog#2-1-114)
Was this page helpful?
YesNo
[What's new](https://code.claude.com/docs/en/whats-new)[Week 16 · Apr 13–17](https://code.claude.com/docs/en/whats-new/2026-w16)
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
[Privacy choices](https://code.claude.com/docs/en/whats-new/2026-w17)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
