<!--
url: https://code.claude.com/docs/en/computer-use
download_date: 2026-04-29
website: claude-code
webpage: computer-use
-->

# Computer Use

[Skip to main content](https://code.claude.com/docs/en/computer-use#content-area)
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
Platforms and integrations
Let Claude use your computer from the CLI
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
  * [What you can do with computer use](https://code.claude.com/docs/en/computer-use#what-you-can-do-with-computer-use)
  * [When computer use applies](https://code.claude.com/docs/en/computer-use#when-computer-use-applies)
  * [Enable computer use](https://code.claude.com/docs/en/computer-use#enable-computer-use)
  * [Approve apps per session](https://code.claude.com/docs/en/computer-use#approve-apps-per-session)
  * [How Claude works on your screen](https://code.claude.com/docs/en/computer-use#how-claude-works-on-your-screen)
  * [One session at a time](https://code.claude.com/docs/en/computer-use#one-session-at-a-time)
  * [Apps are hidden while Claude works](https://code.claude.com/docs/en/computer-use#apps-are-hidden-while-claude-works)
  * [Screenshots are downscaled automatically](https://code.claude.com/docs/en/computer-use#screenshots-are-downscaled-automatically)
  * [Stop at any time](https://code.claude.com/docs/en/computer-use#stop-at-any-time)
  * [Safety and the trust boundary](https://code.claude.com/docs/en/computer-use#safety-and-the-trust-boundary)
  * [Example workflows](https://code.claude.com/docs/en/computer-use#example-workflows)
  * [Validate a native build](https://code.claude.com/docs/en/computer-use#validate-a-native-build)
  * [Reproduce a layout bug](https://code.claude.com/docs/en/computer-use#reproduce-a-layout-bug)
  * [Test a simulator flow](https://code.claude.com/docs/en/computer-use#test-a-simulator-flow)
  * [Differences from the Desktop app](https://code.claude.com/docs/en/computer-use#differences-from-the-desktop-app)
  * [Troubleshooting](https://code.claude.com/docs/en/computer-use#troubleshooting)
  * [”Computer use is in use by another Claude session”](https://code.claude.com/docs/en/computer-use#%E2%80%9Dcomputer-use-is-in-use-by-another-claude-session%E2%80%9D)
  * [macOS permissions prompt keeps reappearing](https://code.claude.com/docs/en/computer-use#macos-permissions-prompt-keeps-reappearing)
  * [computer-use doesn’t appear in /mcp](https://code.claude.com/docs/en/computer-use#computer-use-doesn%E2%80%99t-appear-in-%2Fmcp)
  * [See also](https://code.claude.com/docs/en/computer-use#see-also)


Platforms and integrations
# Let Claude use your computer from the CLI
Copy page
Enable computer use in the Claude Code CLI so Claude can open apps, click, type, and see your screen on macOS. Test native apps, debug visual issues, and automate GUI-only tools without leaving your terminal.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Computer use is a research preview on macOS that requires a Pro or Max plan. It is not available on Team or Enterprise plans. It requires Claude Code v2.1.85 or later and an interactive session, so it is not available in non-interactive mode with the `-p` flag.
Computer use lets Claude open apps, control your screen, and work on your machine the way you would. From the CLI, Claude can compile a Swift app, launch it, click through every button, and screenshot the result, all in the same conversation where it wrote the code. This page covers how computer use works in the CLI. For the Desktop app on macOS or Windows, see [computer use in Desktop](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer).
## 
[​](https://code.claude.com/docs/en/computer-use#what-you-can-do-with-computer-use)
What you can do with computer use
Computer use handles tasks that require a GUI: anything you’d normally have to leave the terminal and do by hand.
  * **Build and validate native apps** : ask Claude to build a macOS menu bar app. Claude writes the Swift, compiles it, launches it, and clicks through every control to verify it works before you ever open it.
  * **End-to-end UI testing** : point Claude at a local Electron app and say “test the onboarding flow.” Claude opens the app, clicks through signup, and screenshots each step. No Playwright config, no test harness.
  * **Debug visual and layout issues** : tell Claude “the modal is clipping on small windows.” Claude resizes the window, reproduces the bug, screenshots it, patches the CSS, and verifies the fix. Claude sees what you see.
  * **Drive GUI-only tools** : interact with design tools, hardware control panels, the iOS Simulator, or proprietary apps that have no CLI or API.


## 
[​](https://code.claude.com/docs/en/computer-use#when-computer-use-applies)
When computer use applies
Claude has several ways to interact with an app or service. Computer use is the broadest and slowest, so Claude tries the most precise tool first:
  * If you have an [MCP server](https://code.claude.com/docs/en/mcp) for the service, Claude uses that.
  * If the task is a shell command, Claude uses Bash.
  * If the task is browser work and you have [Claude in Chrome](https://code.claude.com/docs/en/chrome) set up, Claude uses that.
  * If none of those apply, Claude uses computer use.

Screen control is reserved for things nothing else can reach: native apps, simulators, and tools without an API.
## 
[​](https://code.claude.com/docs/en/computer-use#enable-computer-use)
Enable computer use
Computer use is available as a built-in MCP server called `computer-use`. It’s off by default until you enable it.
1
[](https://code.claude.com/docs/en/computer-use)
Open the MCP menu
In an interactive Claude Code session, run:

```
/mcp

```

Find `computer-use` in the server list. It shows as disabled.
2
[](https://code.claude.com/docs/en/computer-use)
Enable the server
Select `computer-use` and choose **Enable**. The setting persists per project, so you only do this once for each project where you want computer use.
3
[](https://code.claude.com/docs/en/computer-use)
Grant macOS permissions
The first time Claude tries to use your computer, you’ll see a prompt to grant two macOS permissions:
  * **Accessibility** : lets Claude click, type, and scroll
  * **Screen Recording** : lets Claude see what’s on your screen

The prompt includes links to open the relevant System Settings pane. Grant both, then select **Try again** in the prompt. macOS may require you to restart Claude Code after granting Screen Recording.
After setup, ask Claude to do something that needs the GUI:

```
Build the app target, launch it, and click through each tab to make
sure nothing crashes. Screenshot any error states you find.

```

## 
[​](https://code.claude.com/docs/en/computer-use#approve-apps-per-session)
Approve apps per session
Enabling the `computer-use` server doesn’t grant Claude access to every app on your machine. The first time Claude needs a specific app in a session, a prompt appears in your terminal showing:
  * Which apps Claude wants to control
  * Any extra permissions requested, such as clipboard access
  * How many other apps will be hidden while Claude works

Choose **Allow for this session** or **Deny**. Approvals last for the current session. You can approve multiple apps at once when Claude requests them together. Apps with broad reach show an extra warning in the prompt so you know what approving them grants:  
| Warning  | Applies to  |  
| --- | --- |  
| Equivalent to shell access  | Terminal, iTerm, VS Code, Warp, and other terminals and IDEs  |  
| Can read or write any file  | Finder  |  
| Can change system settings  | System Settings  |  
These apps aren’t blocked. The warning lets you decide whether the task warrants that level of access. Claude’s level of control also varies by app category: browsers and trading platforms are view-only, terminals and IDEs are click-only, and everything else gets full control. See [app permissions in Desktop](https://code.claude.com/docs/en/desktop#app-permissions) for the complete tier breakdown.
## 
[​](https://code.claude.com/docs/en/computer-use#how-claude-works-on-your-screen)
How Claude works on your screen
Understanding the flow helps you anticipate what Claude will do and how to intervene.
### 
[​](https://code.claude.com/docs/en/computer-use#one-session-at-a-time)
One session at a time
Computer use holds a machine-wide lock while active. If another Claude Code session is already using your computer, new attempts fail with a message telling you which session holds the lock. Finish or exit that session first.
### 
[​](https://code.claude.com/docs/en/computer-use#apps-are-hidden-while-claude-works)
Apps are hidden while Claude works
When Claude starts controlling your screen, other visible apps are hidden so Claude interacts with only the approved apps. Your terminal window stays visible and is excluded from screenshots, so you can watch the session and Claude never sees its own output. When Claude finishes the turn, hidden apps are restored automatically.
### 
[​](https://code.claude.com/docs/en/computer-use#screenshots-are-downscaled-automatically)
Screenshots are downscaled automatically
Claude Code downscales every screenshot before sending it to the model. You don’t need to lower your display resolution or resize windows on Retina or other high-resolution displays. A 16-inch MacBook Pro at native Retina resolution captures at 3456×2234 and downscales to roughly 1372×887, preserving aspect ratio. There is no setting to change the target size. If on-screen text or controls are too small for Claude to read after downscaling, increase their size in the app rather than changing your display resolution.
### 
[​](https://code.claude.com/docs/en/computer-use#stop-at-any-time)
Stop at any time
When Claude acquires the lock, a macOS notification appears: “Claude is using your computer · press Esc to stop.” Press `Esc` anywhere to abort the current action immediately, or press `Ctrl+C` in the terminal. Either way, Claude releases the lock, unhides your apps, and returns control to you. A second notification appears when Claude is done.
## 
[​](https://code.claude.com/docs/en/computer-use#safety-and-the-trust-boundary)
Safety and the trust boundary
Unlike the [sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing), computer use runs on your actual desktop with access to the apps you approve. Claude checks each action and flags potential prompt injection from on-screen content, but the trust boundary is different. See the [computer use safety guide](https://support.claude.com/en/articles/14128542) for best practices.
The built-in guardrails reduce risk without requiring configuration:
  * **Per-app approval** : Claude can only control apps you’ve approved in the current session.
  * **Sentinel warnings** : apps that grant shell, filesystem, or system settings access are flagged before you approve.
  * **Terminal excluded from screenshots** : Claude never sees your terminal window, so on-screen prompts in your session can’t feed back into the model.
  * **Global escape** : the `Esc` key aborts computer use from anywhere, and the key press is consumed so prompt injection can’t use it to dismiss dialogs.
  * **Lock file** : only one session can control your machine at a time.


## 
[​](https://code.claude.com/docs/en/computer-use#example-workflows)
Example workflows
These examples show common ways to combine computer use with coding tasks.
### 
[​](https://code.claude.com/docs/en/computer-use#validate-a-native-build)
Validate a native build
After making changes to a macOS or iOS app, have Claude compile and verify in one pass:

```
Build the MenuBarStats target, launch it, open the preferences window,
and verify the interval slider updates the label. Screenshot the
preferences window when you're done.

```

Claude runs `xcodebuild`, launches the app, interacts with the UI, and reports what it finds.
### 
[​](https://code.claude.com/docs/en/computer-use#reproduce-a-layout-bug)
Reproduce a layout bug
When a visual bug only appears at certain window sizes, let Claude find it:

```
The settings modal clips its footer on narrow windows. Resize the app
window down until you can reproduce it, screenshot the clipped state,
then check the CSS for the modal container.

```

Claude resizes the window, captures the broken state, and reads the relevant stylesheets.
### 
[​](https://code.claude.com/docs/en/computer-use#test-a-simulator-flow)
Test a simulator flow
Drive the iOS Simulator without writing XCTest:

```
Open the iOS Simulator, launch the app, tap through the onboarding
screens, and tell me if any screen takes more than a second to load.

```

Claude controls the simulator the same way you would with a mouse.
## 
[​](https://code.claude.com/docs/en/computer-use#differences-from-the-desktop-app)
Differences from the Desktop app
The CLI and Desktop surfaces share the same computer use engine, with a few differences:  
| Feature  | Desktop  | CLI  |  
| --- | --- | --- |  
| Platforms  | macOS and Windows  | macOS only  |  
| Enable  | Toggle in **Settings > General** (under **Desktop app**)  | Enable `computer-use` in `/mcp`  |  
| Denied apps list  | Configurable in Settings  | Not yet available  |  
| Auto-unhide toggle  | Optional  | Always on  |  
| Dispatch integration  | Dispatch-spawned sessions can use computer use  | Not applicable  |  
## 
[​](https://code.claude.com/docs/en/computer-use#troubleshooting)
Troubleshooting
### 
[​](https://code.claude.com/docs/en/computer-use#%E2%80%9Dcomputer-use-is-in-use-by-another-claude-session%E2%80%9D)
”Computer use is in use by another Claude session”
Another Claude Code session holds the lock. Finish the task in that session or exit it. If the other session crashed, the lock is released automatically when Claude detects the process is no longer running.
### 
[​](https://code.claude.com/docs/en/computer-use#macos-permissions-prompt-keeps-reappearing)
macOS permissions prompt keeps reappearing
macOS sometimes requires a restart of the requesting process after you grant Screen Recording. Quit Claude Code completely and start a new session. If the prompt persists, open **System Settings > Privacy & Security > Screen Recording** and confirm your terminal app is listed and enabled.
### 
[​](https://code.claude.com/docs/en/computer-use#computer-use-doesn%E2%80%99t-appear-in-/mcp)
`computer-use` doesn’t appear in `/mcp`
The server only appears on eligible setups. Check that:
  * You’re on macOS. Computer use in the CLI is not available on Linux or Windows. On Windows, use [computer use in Desktop](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer) instead.
  * You’re running Claude Code v2.1.85 or later. Run `claude --version` to check.
  * You’re on a Pro or Max plan. Run `/status` to confirm your subscription.
  * You’re authenticated through claude.ai. Computer use is not available with third-party providers like Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry. If you access Claude exclusively through a third-party provider, you need a separate claude.ai account to use this feature.
  * You’re in an interactive session. Computer use is not available in non-interactive mode with the `-p` flag.


## 
[​](https://code.claude.com/docs/en/computer-use#see-also)
See also
  * [Computer use in Desktop](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer): the same capability with a graphical settings page
  * [Claude in Chrome](https://code.claude.com/docs/en/chrome): browser automation for web-based tasks
  * [MCP](https://code.claude.com/docs/en/mcp): connect Claude to structured tools and APIs
  * [Sandboxing](https://code.claude.com/docs/en/sandboxing): how Claude’s Bash tool isolates filesystem and network access
  * [Computer use safety guide](https://support.claude.com/en/articles/14128542): best practices for safe computer use


Was this page helpful?
YesNo
[Chrome extension (beta)](https://code.claude.com/docs/en/chrome)[Visual Studio Code](https://code.claude.com/docs/en/vs-code)
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
[Privacy choices](https://code.claude.com/docs/en/computer-use)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
