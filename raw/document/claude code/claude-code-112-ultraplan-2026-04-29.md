<!--
url: https://code.claude.com/docs/en/ultraplan
download_date: 2026-04-29
website: claude-code
webpage: ultraplan
-->

# Ultraplan

[Skip to main content](https://code.claude.com/docs/en/ultraplan#content-area)
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
Claude Code on the web
Plan in the cloud with ultraplan
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
    * [Get started](https://code.claude.com/docs/en/web-quickstart)
    * [Reference](https://code.claude.com/docs/en/claude-code-on-the-web)
    * [Routines](https://code.claude.com/docs/en/routines)
    * [Plan in the cloud](https://code.claude.com/docs/en/ultraplan)
    * [Ultrareview](https://code.claude.com/docs/en/ultrareview)
  * Claude Code on desktop
  * [Chrome extension (beta)](https://code.claude.com/docs/en/chrome)
  * [Computer use (preview)](https://code.claude.com/docs/en/computer-use)
  * [Visual Studio Code](https://code.claude.com/docs/en/vs-code)
  * [JetBrains IDEs](https://code.claude.com/docs/en/jetbrains)
  * Code review & CI/CD
  * [Claude Code in Slack](https://code.claude.com/docs/en/slack)


On this page
  * [Launch ultraplan from the CLI](https://code.claude.com/docs/en/ultraplan#launch-ultraplan-from-the-cli)
  * [Review and revise the plan in your browser](https://code.claude.com/docs/en/ultraplan#review-and-revise-the-plan-in-your-browser)
  * [Choose where to execute](https://code.claude.com/docs/en/ultraplan#choose-where-to-execute)
  * [Execute on the web](https://code.claude.com/docs/en/ultraplan#execute-on-the-web)
  * [Send the plan back to your terminal](https://code.claude.com/docs/en/ultraplan#send-the-plan-back-to-your-terminal)
  * [Related resources](https://code.claude.com/docs/en/ultraplan#related-resources)


Claude Code on the web
# Plan in the cloud with ultraplan
Copy page
Start a plan from your CLI, draft it on Claude Code on the web, then execute it remotely or back in your terminal
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Ultraplan is in research preview and requires Claude Code v2.1.91 or later. Behavior and capabilities may change based on feedback.
Ultraplan hands a planning task from your local CLI to a [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) session running in [plan mode](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode). Claude drafts the plan in the cloud while you keep working in your terminal. When the plan is ready, you open it in your browser to comment on specific sections, ask for revisions, and choose where to execute it. This is useful when you want a richer review surface than the terminal offers:
  * **Targeted feedback** : comment on individual sections of the plan instead of replying to the whole thing
  * **Hands-off drafting** : the plan is generated remotely, so your terminal stays free for other work
  * **Flexible execution** : approve the plan to run on the web and open a pull request, or send it back to your terminal

Ultraplan requires a [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) account and a GitHub repository. Because it runs on Anthropic’s cloud infrastructure, it is not available when using Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry. The cloud session runs in your account’s default [cloud environment](https://code.claude.com/docs/en/claude-code-on-the-web#the-cloud-environment). If you don’t have a cloud environment yet, ultraplan creates one automatically when it first launches.
## 
[​](https://code.claude.com/docs/en/ultraplan#launch-ultraplan-from-the-cli)
Launch ultraplan from the CLI
From your local CLI session, you can launch ultraplan in three ways:
  * **Command** : run `/ultraplan` followed by your prompt
  * **Keyword** : include the word `ultraplan` anywhere in a normal prompt
  * **From a local plan** : when Claude finishes a local plan and shows the approval dialog, choose **No, refine with Ultraplan on Claude Code on the web** to send the draft to the cloud for further iteration

For example, to plan a service migration with the command:

```
/ultraplan migrate the auth service from sessions to JWTs

```

The command and keyword paths open a confirmation dialog before launching. The local plan path skips this dialog because that selection already serves as confirmation. If [Remote Control](https://code.claude.com/docs/en/remote-control) is active, it disconnects when ultraplan starts because both features occupy the claude.ai/code interface and only one can be connected at a time. After the cloud session launches, your CLI’s prompt input shows a status indicator while the remote session works:  
| Status  | Meaning  |  
| --- | --- |  
| `◇ ultraplan`  | Claude is researching your codebase and drafting the plan  |  
| `◇ ultraplan needs your input`  | Claude has a clarifying question; open the session link to respond  |  
| `◆ ultraplan ready`  | The plan is ready to review in your browser  |  
Run `/tasks` and select the ultraplan entry to open a detail view with the session link, agent activity, and a **Stop ultraplan** action. Stopping archives the cloud session and clears the indicator; nothing is saved to your terminal.
## 
[​](https://code.claude.com/docs/en/ultraplan#review-and-revise-the-plan-in-your-browser)
Review and revise the plan in your browser
When the status changes to `◆ ultraplan ready`, open the session link to view the plan on claude.ai. The plan appears in a dedicated review view:
  * **Inline comments** : highlight any passage and leave a comment for Claude to address
  * **Emoji reactions** : react to a section to signal approval or concern without writing a full comment
  * **Outline sidebar** : jump between sections of the plan

When you ask Claude to address your comments, it revises the plan and presents an updated draft. You can iterate as many times as needed before choosing where to execute.
## 
[​](https://code.claude.com/docs/en/ultraplan#choose-where-to-execute)
Choose where to execute
When the plan looks right, you choose from the browser whether Claude implements it in the same cloud session or sends it back to your waiting terminal.
### 
[​](https://code.claude.com/docs/en/ultraplan#execute-on-the-web)
Execute on the web
Select **Approve Claude’s plan and start coding** in your browser to have Claude implement it in the same Claude Code on the web session. Your terminal shows a confirmation, the status indicator clears, and the work continues in the cloud. When the implementation finishes, [review the diff](https://code.claude.com/docs/en/claude-code-on-the-web#review-changes) and create a pull request from the web interface.
### 
[​](https://code.claude.com/docs/en/ultraplan#send-the-plan-back-to-your-terminal)
Send the plan back to your terminal
Select **Approve plan and teleport back to terminal** in your browser to implement the plan locally with full access to your environment. This option appears when the session was launched from your CLI and the terminal is still polling. The web session is archived so it doesn’t continue working in parallel. Your terminal shows the plan in a dialog titled **Ultraplan approved** with three options:
  * **Implement here** : inject the plan into your current conversation and continue from where you left off
  * **Start new session** : clear the current conversation and begin fresh with only the plan as context
  * **Cancel** : save the plan to a file without executing it; Claude prints the file path so you can return to it later

If you start a new session, Claude prints a `claude --resume` command at the top so you can return to your previous conversation later.
## 
[​](https://code.claude.com/docs/en/ultraplan#related-resources)
Related resources
  * [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web): the cloud infrastructure ultraplan runs on
  * [Plan mode](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode): how planning works in a local session
  * [Find bugs with ultrareview](https://code.claude.com/docs/en/ultrareview): the code review counterpart to ultraplan for catching issues before merge
  * [Remote Control](https://code.claude.com/docs/en/remote-control): use the claude.ai/code interface with a session running on your own machine


Was this page helpful?
YesNo
[Routines](https://code.claude.com/docs/en/routines)[Ultrareview](https://code.claude.com/docs/en/ultrareview)
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
[Privacy choices](https://code.claude.com/docs/en/ultraplan)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
