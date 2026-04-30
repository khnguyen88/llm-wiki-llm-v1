<!--
url: https://code.claude.com/docs/en/whats-new/2026-w14
download_date: 2026-04-29
website: claude-code
webpage: whats-new-2026-w14
-->

# Whats New 2026 W14

[Skip to main content](https://code.claude.com/docs/en/whats-new/2026-w14#content-area)
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
Week 14 · March 30 – April 3, 2026
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### What's New
  * [What's new](https://code.claude.com/docs/en/whats-new)
  * [Week 17 · Apr 20–24](https://code.claude.com/docs/en/whats-new/2026-w17)
  * [Week 16 · Apr 13–17](https://code.claude.com/docs/en/whats-new/2026-w16)
  * [Week 15 · Apr 6–10](https://code.claude.com/docs/en/whats-new/2026-w15)
  * [Week 14 · Mar 30 – Apr 3](https://code.claude.com/docs/en/whats-new/2026-w14)
  * [Week 13 · Mar 23–27](https://code.claude.com/docs/en/whats-new/2026-w13)


What's New
# Week 14 · March 30 – April 3, 2026
Copy page
Computer use in the CLI, interactive in-product lessons, flicker-free rendering, per-tool MCP result-size overrides, and plugin executables on PATH.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Releases [v2.1.86 → v2.1.91](https://code.claude.com/docs/en/changelog#2-1-86)5 features · March 30 – April 3
Computer use in the CLIresearch preview
Last week computer use landed in the Desktop app. This week it’s in the CLI: Claude can open native apps, click through UI, test its own changes, and fix what breaks, all from your terminal. Web apps already had verification loops; native iOS, macOS, and other GUI-only apps didn’t. Now they do. Best for closing the loop on apps and tools where there’s no API to call. Still early; expect rough edges.
Run `/mcp`, find `computer-use`, and toggle it on. Then ask Claude to verify a change end to end:
Claude Code

```
> Open the iOS simulator, tap through onboarding, and screenshot each step

```

[Computer use guide](https://code.claude.com/docs/en/computer-use)
/powerupv2.1.90
Interactive lessons that teach Claude Code features through animated demos, right inside your terminal. Claude Code releases frequently, and features that would have changed how you work last month can slip by. Run `/powerup` once and you’ll know what’s there.
Run it:
Claude Code

```
> /powerup

```

[Commands reference](https://code.claude.com/docs/en/commands)
Flicker-free renderingv2.1.89
Opt into a new alt-screen renderer with virtualized scrollback. The prompt input stays pinned to the bottom, mouse selection works across long conversations, and the flicker on redraw is gone. Unset `CLAUDE_CODE_NO_FLICKER` to roll back.
Set the env var and restart Claude Code:

```
export CLAUDE_CODE_NO_FLICKER=1
claude

```

[Fullscreen rendering](https://code.claude.com/docs/en/fullscreen)
MCP result-size overridev2.1.91
MCP server authors can now raise the truncation cap on a specific tool by setting `anthropic/maxResultSizeChars` in the tool’s `tools/list` entry, up to a hard ceiling of 500K characters. The cap used to be global, so tools that occasionally returned inherently large payloads like database schemas or full file trees hit the default limit and got persisted to disk with a file reference. Per-tool overrides keep those results inline when the tool really needs them.
Annotate the tool in your server’s `tools/list` response:

```
{
  "name": "get_schema",
  "description": "Returns the full database schema",
  "_meta": {
    "anthropic/maxResultSizeChars": 500000
  }
}

```

[MCP reference](https://code.claude.com/docs/en/mcp#raise-the-limit-for-a-specific-tool)
Plugin executables on PATHv2.1.91
Place an executable in a `bin/` directory at your plugin root and Claude Code adds that directory to the Bash tool’s `PATH` while the plugin is enabled. Claude can then invoke the binary as a bare command from any Bash tool call, with no absolute path or wrapper script needed. Handy for packaging CLI helpers next to the commands, agents, and hooks that call them.
Add a `bin/` directory at the plugin root:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── bin/
    └── my-tool

```

[Plugins reference](https://code.claude.com/docs/en/plugins-reference#file-locations-reference)
Other wins
Auto mode follow-ups: new `PermissionDenied` hook fires on classifier denials (return `retry: true` to let Claude try a different approach), and `/permissions` → Recent lets you retry manually with `r`
New `defer` value for `permissionDecision` in `PreToolUse` hooks: `-p` sessions pause at a tool call and exit with a `deferred_tool_use` payload so an SDK app or custom UI can surface it, then resume with `—resume`
`/buddy`: hatch a small creature that watches you code (April 1st)
`disableSkillShellExecution` setting blocks inline shell from skills, slash commands, and plugin commands
Edit tool now works on files viewed via `cat` or `sed -n` without a separate Read
Hook output over 50K saved to disk with a path + preview instead of injected into context
Thinking summaries off by default in interactive sessions (`showThinkingSummaries: true` to restore)
Voice mode: push-to-talk modifier combos, Windows WebSocket, macOS Apple Silicon mic permission
`claude-cli://` deep links accept multi-line prompts (encoded `%0A`)
[Full changelog for v2.1.86–v2.1.91 →](https://code.claude.com/docs/en/changelog#2-1-86)
Was this page helpful?
YesNo
[Week 15 · Apr 6–10](https://code.claude.com/docs/en/whats-new/2026-w15)[Week 13 · Mar 23–27](https://code.claude.com/docs/en/whats-new/2026-w13)
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
[Privacy choices](https://code.claude.com/docs/en/whats-new/2026-w14)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
