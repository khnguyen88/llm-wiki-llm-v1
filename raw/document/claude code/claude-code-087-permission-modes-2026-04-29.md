<!--
url: https://code.claude.com/docs/en/permission-modes
download_date: 2026-04-29
website: claude-code
webpage: permission-modes
-->

# Permission Modes

[Skip to main content](https://code.claude.com/docs/en/permission-modes#content-area)
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
Use Claude Code
Choose a permission mode
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Getting started
  * [Overview](https://code.claude.com/docs/en/overview)
  * [Quickstart](https://code.claude.com/docs/en/quickstart)
  * [Changelog](https://code.claude.com/docs/en/changelog)


##### Core concepts
  * [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
  * [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
  * [Explore the .claude directory](https://code.claude.com/docs/en/claude-directory)
  * [Explore the context window](https://code.claude.com/docs/en/context-window)


##### Use Claude Code
  * [Store instructions and memories](https://code.claude.com/docs/en/memory)
  * [Permission modes](https://code.claude.com/docs/en/permission-modes)
  * [Common workflows](https://code.claude.com/docs/en/common-workflows)
  * [Best practices](https://code.claude.com/docs/en/best-practices)


##### Platforms and integrations
  * [Overview](https://code.claude.com/docs/en/platforms)
  * [Remote Control](https://code.claude.com/docs/en/remote-control)
  * Claude Code on the web
  * Claude Code on desktop
  * [Chrome extension (beta)](https://code.claude.com/docs/en/chrome)
  * [Computer use (preview)](https://code.claude.com/docs/en/computer-use)
  * [Visual Studio Code](https://code.claude.com/docs/en/vs-code)
  * [JetBrains IDEs](https://code.claude.com/docs/en/jetbrains)
  * Code review & CI/CD
  * [Claude Code in Slack](https://code.claude.com/docs/en/slack)


On this page
  * [Available modes](https://code.claude.com/docs/en/permission-modes#available-modes)
  * [Switch permission modes](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
  * [Auto-approve file edits with acceptEdits mode](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)
  * [Analyze before you edit with plan mode](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)
  * [Eliminate prompts with auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)
  * [What the classifier blocks by default](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)
  * [Boundaries you state in conversation](https://code.claude.com/docs/en/permission-modes#boundaries-you-state-in-conversation)
  * [When auto mode falls back](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)
  * [Allow only pre-approved tools with dontAsk mode](https://code.claude.com/docs/en/permission-modes#allow-only-pre-approved-tools-with-dontask-mode)
  * [Skip all checks with bypassPermissions mode](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)
  * [Protected paths](https://code.claude.com/docs/en/permission-modes#protected-paths)
  * [See also](https://code.claude.com/docs/en/permission-modes#see-also)


Use Claude Code
# Choose a permission mode
Copy page
Control whether Claude asks before editing files or running commands. Cycle modes with Shift+Tab in the CLI or use the mode selector in VS Code, Desktop, and claude.ai.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
When Claude wants to edit a file, run a shell command, or make a network request, it pauses and asks you to approve the action. Permission modes control how often that pause happens. The mode you pick shapes the flow of a session: default mode has you review each action as it comes, while looser modes let Claude work in longer uninterrupted stretches and report back when done. Pick more oversight for sensitive work, or fewer interruptions when you trust the direction.
## 
[​](https://code.claude.com/docs/en/permission-modes#available-modes)
Available modes
Each mode makes a different tradeoff between convenience and oversight. The table below shows what Claude can do without a permission prompt in each mode.  
| Mode  | What runs without asking  | Best for  |  
| --- | --- | --- |  
| `default`  | Reads only  | Getting started, sensitive work  |  
| [`acceptEdits`](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)  | Reads, file edits, and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.)  | Iterating on code you’re reviewing  |  
| [`plan`](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)  | Reads only  | Exploring a codebase before changing it  |  
| [`auto`](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)  | Everything, with background safety checks  | Long tasks, reducing prompt fatigue  |  
| [`dontAsk`](https://code.claude.com/docs/en/permission-modes#allow-only-pre-approved-tools-with-dontask-mode)  | Only pre-approved tools  | Locked-down CI and scripts  |  
| [`bypassPermissions`](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)  | Everything except protected paths  | Isolated containers and VMs only  |  
Regardless of mode, writes to [protected paths](https://code.claude.com/docs/en/permission-modes#protected-paths) are never auto-approved, guarding repository state and Claude’s own configuration against accidental corruption. Modes set the baseline. Layer [permission rules](https://code.claude.com/docs/en/permissions#manage-permissions) on top to pre-approve or block specific tools in any mode except `bypassPermissions`, which skips the permission layer entirely.
## 
[​](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
Switch permission modes
You can switch modes mid-session, at startup, or as a persistent default. The mode is set through these controls, not by asking Claude in chat. Select your interface below to see how to change it.
  * CLI
  * VS Code
  * JetBrains
  * Desktop
  * Web and mobile


**During a session** : press `Shift+Tab` to cycle `default` → `acceptEdits` → `plan`. The current mode appears in the status bar. Not every mode is in the default cycle:
  * `auto`: appears when your account meets the [auto mode requirements](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode); cycling to auto shows an opt-in prompt until you accept it, or select **No, don’t ask again** to remove auto from the cycle
  * `bypassPermissions`: appears after you start with `--permission-mode bypassPermissions`, `--dangerously-skip-permissions`, or `--allow-dangerously-skip-permissions`; the `--allow-` variant adds the mode to the cycle without activating it
  * `dontAsk`: never appears in the cycle; set it with `--permission-mode dontAsk`

Enabled optional modes slot in after `plan`, with `bypassPermissions` first and `auto` last. If you have both enabled, you will cycle through `bypassPermissions` on the way to `auto`.**At startup** : pass the mode as a flag.

```
claude --permission-mode plan

```

**As a default** : set `defaultMode` in [settings](https://code.claude.com/docs/en/settings#settings-files).

```
{
  "permissions": {
    "defaultMode": "acceptEdits"
  }
}

```

The same `--permission-mode` flag works with `-p` for [non-interactive runs](https://code.claude.com/docs/en/headless).
**During a session** : click the mode indicator at the bottom of the prompt box.**As a default** : set `claudeCode.initialPermissionMode` in VS Code settings, or use the Claude Code extension settings panel.The mode indicator shows these labels, mapped to the mode each one applies:  
| UI label  | Mode  |  
| --- | --- |  
| Ask before edits  | `default`  |  
| Edit automatically  | `acceptEdits`  |  
| Plan mode  | `plan`  |  
| Auto mode  | `auto`  |  
| Bypass permissions  | `bypassPermissions`  |  
Auto mode appears in the mode indicator after you enable **Allow dangerously skip permissions** in the extension settings, but it stays unavailable until your account meets every requirement listed in the [auto mode section](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode). The `claudeCode.initialPermissionMode` setting does not accept `auto`; to start in auto mode by default, set `defaultMode` in your Claude Code [`settings.json`](https://code.claude.com/docs/en/settings#settings-files) instead.Bypass permissions also requires the **Allow dangerously skip permissions** toggle before it appears in the mode indicator.See the [VS Code guide](https://code.claude.com/docs/en/vs-code) for extension-specific details.
The JetBrains plugin runs Claude Code in the IDE terminal, so switching modes works the same as in the CLI: press `Shift+Tab` to cycle, or pass `--permission-mode` when launching.
Use the mode selector next to the send button. Auto and Bypass permissions appear only after you enable them in Desktop settings. See the [Desktop guide](https://code.claude.com/docs/en/desktop#choose-a-permission-mode).
Use the mode dropdown next to the prompt box on [claude.ai/code](https://claude.ai/code) or in the mobile app. Permission prompts appear in claude.ai for approval. Which modes appear depends on where the session runs:
  * **Cloud sessions** on [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web): Auto accept edits and Plan mode. Ask permissions, Auto, and Bypass permissions are not available.
  * **[Remote Control](https://code.claude.com/docs/en/remote-control) sessions** on your local machine: Ask permissions, Auto accept edits, and Plan mode. Auto and Bypass permissions are not available.

For Remote Control, you can also set the starting mode when launching the host:

```
claude remote-control --permission-mode acceptEdits

```

## 
[​](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)
Auto-approve file edits with acceptEdits mode
`acceptEdits` mode lets Claude create and edit files in your working directory without prompting. The status bar shows `⏵⏵ accept edits on` while this mode is active. In addition to file edits, `acceptEdits` mode auto-approves common filesystem Bash commands: `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, and `sed`. These commands are also auto-approved when prefixed with safe environment variables such as `LANG=C` or `NO_COLOR=1`, or process wrappers such as `timeout`, `nice`, or `nohup`. Like file edits, auto-approval applies only to paths inside your working directory or `additionalDirectories`. Paths outside that scope, writes to [protected paths](https://code.claude.com/docs/en/permission-modes#protected-paths), and all other Bash commands still prompt. Use `acceptEdits` when you want to review changes in your editor or via `git diff` after the fact rather than approving each edit inline. Press `Shift+Tab` once from default mode to enter it, or start with it directly:

```
claude --permission-mode acceptEdits

```

## 
[​](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)
Analyze before you edit with plan mode
Plan mode tells Claude to research and propose changes without making them. Claude reads files, runs shell commands to explore, and writes a plan, but does not edit your source. Permission prompts still apply the same as default mode. Enter plan mode by pressing `Shift+Tab` or prefixing a single prompt with `/plan`. You can also start in plan mode from the CLI:

```
claude --permission-mode plan

```

Press `Shift+Tab` again to leave plan mode without approving a plan. When the plan is ready, Claude presents it and asks how to proceed. From that prompt you can:
  * Approve and start in auto mode
  * Approve and accept edits
  * Approve and review each edit manually
  * Keep planning with feedback
  * Refine with [Ultraplan](https://code.claude.com/docs/en/ultraplan) for browser-based review

Each approve option also offers to clear the planning context first.
## 
[​](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)
Eliminate prompts with auto mode
Auto mode requires Claude Code v2.1.83 or later.
Auto mode lets Claude execute without permission prompts. A separate classifier model reviews actions before they run, blocking anything that escalates beyond your request, targets unrecognized infrastructure, or appears driven by hostile content Claude read.
Auto mode is a research preview. It reduces prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations.
Auto mode is available only when your account meets all of these requirements:
  * **Plan** : Max, Team, Enterprise, or API. Not available on Pro.
  * **Admin** : on Team and Enterprise, an admin must enable it in [Claude Code admin settings](https://claude.ai/admin-settings/claude-code) before users can turn it on. Admins can also lock it off by setting `permissions.disableAutoMode` to `"disable"` in [managed settings](https://code.claude.com/docs/en/permissions#managed-settings).
  * **Model** : Claude Sonnet 4.6, Opus 4.6, or Opus 4.7 on Team, Enterprise, and API plans; Claude Opus 4.7 only on Max plans. Other models, including Haiku and claude-3 models, are not supported.
  * **Provider** : Anthropic API only. Not available on Bedrock, Vertex, or Foundry.

If Claude Code reports auto mode as unavailable, one of these requirements is unmet; this is not a transient outage. A separate message that names a model and says auto mode “cannot determine the safety” of an action is a transient classifier outage; see the [error reference](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action).
### 
[​](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)
What the classifier blocks by default
The classifier trusts your working directory and your repo’s configured remotes. Everything else is treated as external until you [configure trusted infrastructure](https://code.claude.com/docs/en/auto-mode-config). **Blocked by default** :
  * Downloading and executing code, like `curl | bash`
  * Sending sensitive data to external endpoints
  * Production deploys and migrations
  * Mass deletion on cloud storage
  * Granting IAM or repo permissions
  * Modifying shared infrastructure
  * Irreversibly destroying files that existed before the session
  * Force push, or pushing directly to `main`

**Allowed by default** :
  * Local file operations in your working directory
  * Installing dependencies declared in your lock files or manifests
  * Reading `.env` and sending credentials to their matching API
  * Read-only HTTP requests
  * Pushing to the branch you started on or one Claude created

Sandbox network access requests are routed through the classifier rather than allowed by default. Run `claude auto-mode defaults` to see the full rule lists. If routine actions get blocked, an administrator can add trusted repos, buckets, and services via the `autoMode.environment` setting: see [Configure auto mode](https://code.claude.com/docs/en/auto-mode-config).
### 
[​](https://code.claude.com/docs/en/permission-modes#boundaries-you-state-in-conversation)
Boundaries you state in conversation
The classifier treats boundaries you state in the conversation as a block signal. If you tell Claude “don’t push” or “wait until I review before deploying”, the classifier blocks matching actions even when the default rules would allow them. A boundary stays in force until you lift it in a later message. Claude’s own judgment that a condition was met does not lift it. Boundaries are not stored as rules. The classifier re-reads them from the transcript on each check, so a boundary can be lost if [context compaction](https://code.claude.com/docs/en/costs#reduce-token-usage) removes the message that stated it. For a hard guarantee, add a [deny rule](https://code.claude.com/docs/en/permissions#permission-rule-syntax) instead.
### 
[​](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)
When auto mode falls back
Each denied action shows a notification and appears in `/permissions` under the Recently denied tab, where you can press `r` to retry it with a manual approval. If the classifier blocks an action 3 times in a row or 20 times total, auto mode pauses and Claude Code resumes prompting. Approving the prompted action resumes auto mode. These thresholds are not configurable. Any allowed action resets the consecutive counter, while the total counter persists for the session and resets only when its own limit triggers a fallback. In [non-interactive mode](https://code.claude.com/docs/en/headless) with the `-p` flag, repeated blocks abort the session since there is no user to prompt. Repeated blocks usually mean the classifier is missing context about your infrastructure. Use `/feedback` to report false positives, or have an administrator [configure trusted infrastructure](https://code.claude.com/docs/en/auto-mode-config).
How the classifier evaluates actions
Each action goes through a fixed decision order. The first matching step wins:
  1. Actions matching your [allow or deny rules](https://code.claude.com/docs/en/permissions#manage-permissions) resolve immediately
  2. Read-only actions and file edits in your working directory are auto-approved, except writes to [protected paths](https://code.claude.com/docs/en/permission-modes#protected-paths)
  3. Everything else goes to the classifier
  4. If the classifier blocks, Claude receives the reason and tries an alternative

On entering auto mode, broad allow rules that grant arbitrary code execution are dropped:
  * Blanket `Bash(*)` or `PowerShell(*)`
  * Wildcarded interpreters like `Bash(python*)`
  * Package-manager run commands
  * `Agent` allow rules

Narrow rules like `Bash(npm test)` carry over. Dropped rules are restored when you leave auto mode.The classifier sees user messages, tool calls, and your CLAUDE.md content. Tool results are stripped, so hostile content in a file or web page cannot manipulate it directly. A separate server-side probe scans incoming tool results and flags suspicious content before Claude reads it. For more on how these layers work together, see the [auto mode announcement](https://claude.com/blog/auto-mode) and the [engineering deep dive](https://www.anthropic.com/engineering/claude-code-auto-mode).
How auto mode handles subagents
The classifier checks [subagent](https://code.claude.com/docs/en/sub-agents) work at three points:
  1. Before a subagent starts, the delegated task description is evaluated, so a dangerous-looking task is blocked at spawn time.
  2. While the subagent runs, each of its actions goes through the classifier with the same rules as the parent session, and any `permissionMode` in the subagent’s frontmatter is ignored.
  3. When the subagent finishes, the classifier reviews its full action history; if that return check flags a concern, a security warning is prepended to the subagent’s results.


Cost and latency
The classifier runs on a server-configured model that is independent of your `/model` selection, so switching models does not change classifier availability. Classifier calls count toward your token usage. Each check sends a portion of the transcript plus the pending action, adding a round-trip before execution. Reads and working-directory edits outside protected paths skip the classifier, so the overhead comes mainly from shell commands and network operations.
## 
[​](https://code.claude.com/docs/en/permission-modes#allow-only-pre-approved-tools-with-dontask-mode)
Allow only pre-approved tools with dontAsk mode
`dontAsk` mode auto-denies every tool call that would otherwise prompt. Only actions matching your `permissions.allow` rules and [read-only Bash commands](https://code.claude.com/docs/en/permissions#read-only-commands) can execute; explicit `ask` rules are denied rather than prompting. This makes the mode fully non-interactive for CI pipelines or restricted environments where you pre-define exactly what Claude may do. Set it at startup with the flag:

```
claude --permission-mode dontAsk

```

## 
[​](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)
Skip all checks with bypassPermissions mode
`bypassPermissions` mode disables permission prompts and safety checks so tool calls execute immediately. Writes to [protected paths](https://code.claude.com/docs/en/permission-modes#protected-paths) are the only actions that still prompt. Only use this mode in isolated environments like containers, VMs, or dev containers without internet access, where Claude Code cannot damage your host system. You cannot enter `bypassPermissions` from a session that was started without one of the enabling flags; restart with one to enable it:

```
claude --permission-mode bypassPermissions

```

The `--dangerously-skip-permissions` flag is equivalent.
`bypassPermissions` offers no protection against prompt injection or unintended actions. For background safety checks without prompts, use [auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) instead. Administrators can block this mode by setting `permissions.disableBypassPermissionsMode` to `"disable"` in [managed settings](https://code.claude.com/docs/en/permissions#managed-settings).
## 
[​](https://code.claude.com/docs/en/permission-modes#protected-paths)
Protected paths
Writes to a small set of paths are never auto-approved, in every mode. This prevents accidental corruption of repository state and Claude’s own configuration. In `default`, `acceptEdits`, `plan`, and `bypassPermissions` these writes prompt; in `auto` they route to the classifier; in `dontAsk` they are denied. Protected directories:
  * `.git`
  * `.vscode`
  * `.idea`
  * `.husky`
  * `.claude`, except for `.claude/commands`, `.claude/agents`, `.claude/skills`, and `.claude/worktrees` where Claude routinely creates content

Protected files:
  * `.gitconfig`, `.gitmodules`
  * `.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`, `.profile`
  * `.ripgreprc`
  * `.mcp.json`, `.claude.json`


## 
[​](https://code.claude.com/docs/en/permission-modes#see-also)
See also
  * [Permissions](https://code.claude.com/docs/en/permissions): allow, ask, and deny rules; managed policies
  * [Configure auto mode](https://code.claude.com/docs/en/auto-mode-config): tell the classifier which infrastructure your organization trusts
  * [Hooks](https://code.claude.com/docs/en/hooks): custom permission logic via `PreToolUse` and `PermissionRequest` hooks
  * [Ultraplan](https://code.claude.com/docs/en/ultraplan): run plan mode in a Claude Code on the web session with browser-based review
  * [Security](https://code.claude.com/docs/en/security): safeguards and best practices
  * [Sandboxing](https://code.claude.com/docs/en/sandboxing): filesystem and network isolation for Bash commands
  * [Non-interactive mode](https://code.claude.com/docs/en/headless): run Claude Code with the `-p` flag


Was this page helpful?
YesNo
[Store instructions and memories](https://code.claude.com/docs/en/memory)[Common workflows](https://code.claude.com/docs/en/common-workflows)
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
[Privacy choices](https://code.claude.com/docs/en/permission-modes)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
