<!--
url: https://code.claude.com/docs/en/platforms
download_date: 2026-04-29
website: claude-code
webpage: platforms
-->

# Platforms

[Skip to main content](https://code.claude.com/docs/en/platforms#content-area)
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
Platforms and integrations
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
  * [Where to run Claude Code](https://code.claude.com/docs/en/platforms#where-to-run-claude-code)
  * [Connect your tools](https://code.claude.com/docs/en/platforms#connect-your-tools)
  * [Work when you are away from your terminal](https://code.claude.com/docs/en/platforms#work-when-you-are-away-from-your-terminal)
  * [Related resources](https://code.claude.com/docs/en/platforms#related-resources)
  * [Platforms](https://code.claude.com/docs/en/platforms#platforms)
  * [Integrations](https://code.claude.com/docs/en/platforms#integrations)
  * [Remote access](https://code.claude.com/docs/en/platforms#remote-access)


Platforms and integrations
# Platforms and integrations
Copy page
Choose where to run Claude Code and what to connect it to. Compare the CLI, Desktop, VS Code, JetBrains, web, mobile, and integrations like Chrome, Slack, and CI/CD.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Claude Code runs the same underlying engine everywhere, but each surface is tuned for a different way of working. This page helps you pick the right platform for your workflow and connect the tools you already use.
## 
[​](https://code.claude.com/docs/en/platforms#where-to-run-claude-code)
Where to run Claude Code
Choose a platform based on how you like to work and where your project lives.  
| Platform  | Best for  | What you get  |  
| --- | --- | --- |  
| [CLI](https://code.claude.com/docs/en/quickstart)  | Terminal workflows, scripting, remote servers  | Full feature set, [Agent SDK](https://code.claude.com/docs/en/headless), [computer use](https://code.claude.com/docs/en/computer-use) on macOS (Pro and Max), third-party providers  |  
| [Desktop](https://code.claude.com/docs/en/desktop)  | Visual review, parallel sessions, managed setup  | Diff viewer, app preview, [computer use](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer) and [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch) on Pro and Max  |  
| [VS Code](https://code.claude.com/docs/en/vs-code)  | Working inside VS Code without switching to a terminal  | Inline diffs, integrated terminal, file context  |  
| [JetBrains](https://code.claude.com/docs/en/jetbrains)  | Working inside IntelliJ, PyCharm, WebStorm, or other JetBrains IDEs  | Diff viewer, selection sharing, terminal session  |  
| [Web](https://code.claude.com/docs/en/claude-code-on-the-web)  | Long-running tasks that don’t need much steering, or work that should continue when you’re offline  | Anthropic-managed cloud, continues after you disconnect  |  
| Mobile  | Starting and monitoring tasks while away from your computer  | Cloud sessions from the Claude app for iOS and Android, [Remote Control](https://code.claude.com/docs/en/remote-control) for local sessions, [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch) to Desktop on Pro and Max  |  
The CLI is the most complete surface for terminal-native work: scripting, third-party providers, and the Agent SDK are CLI-only. Desktop and the IDE extensions trade some CLI-only features for visual review and tighter editor integration. The web runs in Anthropic’s cloud, so tasks keep going after you disconnect. Mobile is a thin client into those same cloud sessions or into a local session via Remote Control, and can send tasks to Desktop with Dispatch. You can mix surfaces on the same project. Configuration, project memory, and MCP servers are shared across the local surfaces.
## 
[​](https://code.claude.com/docs/en/platforms#connect-your-tools)
Connect your tools
Integrations let Claude work with services outside your codebase.  
| Integration  | What it does  | Use it for  |  
| --- | --- | --- |  
| [Chrome](https://code.claude.com/docs/en/chrome)  | Controls your browser with your logged-in sessions  | Testing web apps, filling forms, automating sites without an API  |  
| [GitHub Actions](https://code.claude.com/docs/en/github-actions)  | Runs Claude in your CI pipeline  | Automated PR reviews, issue triage, scheduled maintenance  |  
| [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd)  | Same as GitHub Actions for GitLab  | CI-driven automation on GitLab  |  
| [Code Review](https://code.claude.com/docs/en/code-review)  | Reviews every PR automatically  | Catching bugs before human review  |  
| [Slack](https://code.claude.com/docs/en/slack)  | Responds to `@Claude` mentions in your channels  | Turning bug reports into pull requests from team chat  |  
For integrations not listed here, [MCP servers](https://code.claude.com/docs/en/mcp) and [connectors](https://code.claude.com/docs/en/desktop#connect-external-tools) let you connect almost anything: Linear, Notion, Google Drive, or your own internal APIs.
## 
[​](https://code.claude.com/docs/en/platforms#work-when-you-are-away-from-your-terminal)
Work when you are away from your terminal
Claude Code offers several ways to work when you’re not at your terminal. They differ in what triggers the work, where Claude runs, and how much you need to set up.  
|   | Trigger  | Claude runs on  | Setup  | Best for  |  
| --- | --- | --- | --- | --- |  
| [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch)  | Message a task from the Claude mobile app  | Your machine (Desktop)  | [Pair the mobile app with Desktop](https://support.claude.com/en/articles/13947068)  | Delegating work while you’re away, minimal setup  |  
| [Remote Control](https://code.claude.com/docs/en/remote-control)  | Drive a running session from [claude.ai/code](https://claude.ai/code) or the Claude mobile app  | Your machine (CLI or VS Code)  | Run `claude remote-control`  | Steering in-progress work from another device  |  
| [Channels](https://code.claude.com/docs/en/channels)  | Push events from a chat app like Telegram or Discord, or your own server  | Your machine (CLI)  |  [Install a channel plugin](https://code.claude.com/docs/en/channels#quickstart) or [build your own](https://code.claude.com/docs/en/channels-reference)  | Reacting to external events like CI failures or chat messages  |  
| [Slack](https://code.claude.com/docs/en/slack)  | Mention `@Claude` in a team channel  | Anthropic cloud  |  [Install the Slack app](https://code.claude.com/docs/en/slack#setting-up-claude-code-in-slack) with [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) enabled  | PRs and reviews from team chat  |  
| [Scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks)  | Set a schedule  |  [CLI](https://code.claude.com/docs/en/scheduled-tasks), [Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks), or [cloud](https://code.claude.com/docs/en/routines)  | Pick a frequency  | Recurring automation like daily reviews  |  
If you’re not sure where to start, [install the CLI](https://code.claude.com/docs/en/quickstart) and run it in a project directory. If you’d rather not use a terminal, [Desktop](https://code.claude.com/docs/en/desktop-quickstart) gives you the same engine with a graphical interface.
## 
[​](https://code.claude.com/docs/en/platforms#related-resources)
Related resources
### 
[​](https://code.claude.com/docs/en/platforms#platforms)
Platforms
  * [CLI quickstart](https://code.claude.com/docs/en/quickstart): install and run your first command in the terminal
  * [Desktop](https://code.claude.com/docs/en/desktop): visual diff review, parallel sessions, computer use, and Dispatch
  * [VS Code](https://code.claude.com/docs/en/vs-code): the Claude Code extension inside your editor
  * [JetBrains](https://code.claude.com/docs/en/jetbrains): the extension for IntelliJ, PyCharm, and other JetBrains IDEs
  * [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web): cloud sessions that keep running when you disconnect
  * Mobile: the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) for starting and monitoring tasks while away from your computer


### 
[​](https://code.claude.com/docs/en/platforms#integrations)
Integrations
  * [Chrome](https://code.claude.com/docs/en/chrome): automate browser tasks with your logged-in sessions
  * [Computer use](https://code.claude.com/docs/en/computer-use): let Claude open apps and control your screen on macOS
  * [GitHub Actions](https://code.claude.com/docs/en/github-actions): run Claude in your CI pipeline
  * [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd): the same for GitLab
  * [Code Review](https://code.claude.com/docs/en/code-review): automatic review on every pull request
  * [Slack](https://code.claude.com/docs/en/slack): send tasks from team chat, get PRs back


### 
[​](https://code.claude.com/docs/en/platforms#remote-access)
Remote access
  * [Dispatch](https://code.claude.com/docs/en/desktop#sessions-from-dispatch): message a task from your phone and it can spawn a Desktop session
  * [Remote Control](https://code.claude.com/docs/en/remote-control): drive a running session from your phone or browser
  * [Channels](https://code.claude.com/docs/en/channels): push events from chat apps or your own servers into a session
  * [Scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks): run prompts on a recurring schedule


Was this page helpful?
YesNo
[Best practices](https://code.claude.com/docs/en/best-practices)[Remote Control](https://code.claude.com/docs/en/remote-control)
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
[Privacy choices](https://code.claude.com/docs/en/platforms)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
