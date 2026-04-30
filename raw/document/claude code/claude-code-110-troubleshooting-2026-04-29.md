<!--
url: https://code.claude.com/docs/en/troubleshooting
download_date: 2026-04-29
website: claude-code
webpage: troubleshooting
-->

# Troubleshooting

[Skip to main content](https://code.claude.com/docs/en/troubleshooting#content-area)
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
Troubleshooting
Troubleshooting
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Agents
  * [Create custom subagents](https://code.claude.com/docs/en/sub-agents)
  * [Run agent teams](https://code.claude.com/docs/en/agent-teams)


##### Tools and plugins
  * [Model Context Protocol (MCP)](https://code.claude.com/docs/en/mcp)
  * [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)
  * [Create plugins](https://code.claude.com/docs/en/plugins)
  * [Extend Claude with skills](https://code.claude.com/docs/en/skills)


##### Automation
  * [Automate with hooks](https://code.claude.com/docs/en/hooks-guide)
  * [Push external events to Claude](https://code.claude.com/docs/en/channels)
  * [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
  * [Programmatic usage](https://code.claude.com/docs/en/headless)


##### Troubleshooting
  * [Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)
  * [Troubleshoot performance and stability](https://code.claude.com/docs/en/troubleshooting)
  * [Debug configuration](https://code.claude.com/docs/en/debug-your-config)
  * [Error reference](https://code.claude.com/docs/en/errors)


On this page
  * [Performance and stability](https://code.claude.com/docs/en/troubleshooting#performance-and-stability)
  * [High CPU or memory usage](https://code.claude.com/docs/en/troubleshooting#high-cpu-or-memory-usage)
  * [Auto-compaction stops with a thrashing error](https://code.claude.com/docs/en/troubleshooting#auto-compaction-stops-with-a-thrashing-error)
  * [Command hangs or freezes](https://code.claude.com/docs/en/troubleshooting#command-hangs-or-freezes)
  * [Search and discovery issues](https://code.claude.com/docs/en/troubleshooting#search-and-discovery-issues)
  * [Slow or incomplete search results on WSL](https://code.claude.com/docs/en/troubleshooting#slow-or-incomplete-search-results-on-wsl)
  * [Get more help](https://code.claude.com/docs/en/troubleshooting#get-more-help)


Troubleshooting
# Troubleshooting
Copy page
Fix high CPU or memory usage, hangs, auto-compact thrashing, and search problems in Claude Code, and find the right page for other issues.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
This page covers performance, stability, and search problems once Claude Code is running. For other issues, start with the page that matches where you’re stuck:  
| Symptom  | Go to  |  
| --- | --- |  
|  `command not found`, install fails, PATH issues, `EACCES`, TLS errors  | [Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)  |  
| Login loops, OAuth errors, `403 Forbidden`, “organization disabled”, Bedrock/Vertex/Foundry credentials  | [Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install#login-and-authentication)  |  
| Settings not applying, hooks not firing, MCP servers not loading  | [Debug your configuration](https://code.claude.com/docs/en/debug-your-config)  |  
|  `API Error: 5xx`, `529 Overloaded`, `429`, request validation errors  | [Error reference](https://code.claude.com/docs/en/errors)  |  
|  `model not found` or `you may not have access to it`  | [Error reference](https://code.claude.com/docs/en/errors#theres-an-issue-with-the-selected-model)  |  
| VS Code extension not connecting or detecting Claude  | [VS Code integration](https://code.claude.com/docs/en/vs-code#fix-common-issues)  |  
| JetBrains plugin or IDE not detected  | [JetBrains integration](https://code.claude.com/docs/en/jetbrains#troubleshooting)  |  
| High CPU or memory, slow responses, hangs, search not finding files  |  [Performance and stability](https://code.claude.com/docs/en/troubleshooting#performance-and-stability) below  |  
If you’re not sure which applies, run `/doctor` inside Claude Code for an automated check of your installation, settings, MCP servers, and context usage. If `claude` won’t start at all, run `claude doctor` from your shell instead.
## 
[​](https://code.claude.com/docs/en/troubleshooting#performance-and-stability)
Performance and stability
These sections cover issues related to resource usage, responsiveness, and search behavior.
### 
[​](https://code.claude.com/docs/en/troubleshooting#high-cpu-or-memory-usage)
High CPU or memory usage
Claude Code is designed to work with most development environments, but may consume significant resources when processing large codebases. If you’re experiencing performance issues:
  1. Use `/compact` regularly to reduce context size
  2. Close and restart Claude Code between major tasks
  3. Consider adding large build directories to your `.gitignore` file

If memory usage stays high after these steps, run `/heapdump` to write a JavaScript heap snapshot and a memory breakdown to `~/Desktop`. On Linux without a Desktop folder, the files are written to your home directory. The breakdown shows resident set size, JS heap, array buffers, and unaccounted native memory, which helps identify whether the growth is in JavaScript objects or in native code. To inspect retainers, open the `.heapsnapshot` file in Chrome DevTools under Memory → Load. Attach both files when reporting a memory issue on [GitHub](https://github.com/anthropics/claude-code/issues).
### 
[​](https://code.claude.com/docs/en/troubleshooting#auto-compaction-stops-with-a-thrashing-error)
Auto-compaction stops with a thrashing error
If you see `Autocompact is thrashing: the context refilled to the limit...`, automatic compaction succeeded but a file or tool output immediately refilled the context window several times in a row. Claude Code stops retrying to avoid wasting API calls on a loop that isn’t making progress. To recover:
  1. Ask Claude to read the oversized file in smaller chunks, such as a specific line range or function, instead of the whole file
  2. Run `/compact` with a focus that drops the large output, for example `/compact keep only the plan and the diff`
  3. Move the large-file work to a [subagent](https://code.claude.com/docs/en/sub-agents) so it runs in a separate context window
  4. Run `/clear` if the earlier conversation is no longer needed


### 
[​](https://code.claude.com/docs/en/troubleshooting#command-hangs-or-freezes)
Command hangs or freezes
If Claude Code seems unresponsive:
  1. Press Ctrl+C to attempt to cancel the current operation
  2. If unresponsive, you may need to close the terminal and restart

Restarting doesn’t lose your conversation. Run `claude --resume` in the same directory to pick the session back up.
### 
[​](https://code.claude.com/docs/en/troubleshooting#search-and-discovery-issues)
Search and discovery issues
If the Search tool, `@file` mentions, custom agents, or custom skills aren’t finding files, the bundled `ripgrep` binary may not run on your system. Install your platform’s `ripgrep` package and tell Claude Code to use it instead:
  * macOS
  * Ubuntu/Debian
  * Alpine
  * Arch
  * Windows



```
brew install ripgrep

```


```
sudo apt install ripgrep

```


```
apk add ripgrep

```


```
pacman -S ripgrep

```


```
winget install BurntSushi.ripgrep.MSVC

```

Then set `USE_BUILTIN_RIPGREP=0` in your [environment](https://code.claude.com/docs/en/env-vars).
### 
[​](https://code.claude.com/docs/en/troubleshooting#slow-or-incomplete-search-results-on-wsl)
Slow or incomplete search results on WSL
Disk read performance penalties when [working across file systems on WSL](https://learn.microsoft.com/en-us/windows/wsl/filesystems) may result in fewer-than-expected matches when using Claude Code on WSL. Search still functions, but returns fewer results than on a native filesystem.
`/doctor` will show Search as OK in this case.
**Solutions:**
  1. **Submit more specific searches** : reduce the number of files searched by specifying directories or file types: “Search for JWT validation logic in the auth-service package” or “Find use of md5 hash in JS files”.
  2. **Move project to Linux filesystem** : if possible, ensure your project is located on the Linux filesystem (`/home/`) rather than the Windows filesystem (`/mnt/c/`).
  3. **Use native Windows instead** : consider running Claude Code natively on Windows instead of through WSL, for better file system performance.


## 
[​](https://code.claude.com/docs/en/troubleshooting#get-more-help)
Get more help
If you’re experiencing issues not covered here:
  1. Run `/doctor` to check installation health, settings validity, MCP configuration, and context usage in one pass
  2. Use the `/feedback` command within Claude Code to report problems directly to Anthropic
  3. Check the [GitHub repository](https://github.com/anthropics/claude-code) for known issues
  4. Ask Claude directly about its capabilities and features. Claude has built-in access to its documentation.


Was this page helpful?
YesNo
[Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)[Debug configuration](https://code.claude.com/docs/en/debug-your-config)
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
[Privacy choices](https://code.claude.com/docs/en/troubleshooting)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
