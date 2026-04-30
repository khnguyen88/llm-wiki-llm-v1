<!--
url: https://code.claude.com/docs/en/web-quickstart
download_date: 2026-04-29
website: claude-code
webpage: web-quickstart
-->

# Web Quickstart

[Skip to main content](https://code.claude.com/docs/en/web-quickstart#content-area)
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
Get started with Claude Code on the web
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
  * [How sessions run](https://code.claude.com/docs/en/web-quickstart#how-sessions-run)
  * [Compare ways to run Claude Code](https://code.claude.com/docs/en/web-quickstart#compare-ways-to-run-claude-code)
  * [Connect GitHub and create an environment](https://code.claude.com/docs/en/web-quickstart#connect-github-and-create-an-environment)
  * [Connect from your terminal](https://code.claude.com/docs/en/web-quickstart#connect-from-your-terminal)
  * [Start a task](https://code.claude.com/docs/en/web-quickstart#start-a-task)
  * [Pre-fill sessions](https://code.claude.com/docs/en/web-quickstart#pre-fill-sessions)
  * [Review and iterate](https://code.claude.com/docs/en/web-quickstart#review-and-iterate)
  * [Troubleshoot setup](https://code.claude.com/docs/en/web-quickstart#troubleshoot-setup)
  * [No repositories appear after connecting GitHub](https://code.claude.com/docs/en/web-quickstart#no-repositories-appear-after-connecting-github)
  * [The page only shows a GitHub login button](https://code.claude.com/docs/en/web-quickstart#the-page-only-shows-a-github-login-button)
  * [”Not available for the selected organization”](https://code.claude.com/docs/en/web-quickstart#%E2%80%9Dnot-available-for-the-selected-organization%E2%80%9D)
  * [/web-setup returns “Unknown command”](https://code.claude.com/docs/en/web-quickstart#%2Fweb-setup-returns-%E2%80%9Cunknown-command%E2%80%9D)
  * [”Could not create a cloud environment” or “No cloud environment available” when using --remote or ultraplan](https://code.claude.com/docs/en/web-quickstart#%E2%80%9Dcould-not-create-a-cloud-environment%E2%80%9D-or-%E2%80%9Cno-cloud-environment-available%E2%80%9D-when-using-remote-or-ultraplan)
  * [Setup script failed](https://code.claude.com/docs/en/web-quickstart#setup-script-failed)
  * [Session keeps running after closing the tab](https://code.claude.com/docs/en/web-quickstart#session-keeps-running-after-closing-the-tab)
  * [Next steps](https://code.claude.com/docs/en/web-quickstart#next-steps)


Claude Code on the web
# Get started with Claude Code on the web
Copy page
Run Claude Code in the cloud from your browser or phone. Connect a GitHub repository, submit a task, and review the PR without local setup.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Claude Code on the web is in research preview for Pro, Max, and Team users, and for Enterprise users with premium seats or Chat + Claude Code seats.
Claude Code on the web runs on Anthropic-managed cloud infrastructure instead of your machine. Submit tasks from [claude.ai/code](https://claude.ai/code) in your browser or the Claude mobile app. You’ll need a GitHub repository to [get started](https://code.claude.com/docs/en/web-quickstart#connect-github-and-create-an-environment). Claude clones it into an isolated virtual machine, makes changes, and pushes a branch for you to review. Sessions persist across devices, so a task you start on your laptop is ready to review from your phone later. Claude Code on the web works well for:
  * **Parallel tasks** : run several independent tasks at once, each in its own session and branch, without managing multiple worktrees
  * **Repos you don’t have locally** : Claude clones the repo fresh every session, so you don’t need it checked out
  * **Tasks that don’t need frequent steering** : submit a well-defined task, do something else, and review the result when Claude is done
  * **Code questions and exploration** : understand a codebase or trace how a feature is implemented without a local checkout

For work that needs your local config, tools, or environment, running Claude Code locally or using [Remote Control](https://code.claude.com/docs/en/remote-control) is a better fit.
## 
[​](https://code.claude.com/docs/en/web-quickstart#how-sessions-run)
How sessions run
When you submit a task:
  1. **Clone and prepare** : your repository is cloned to an Anthropic-managed VM, and your [setup script](https://code.claude.com/docs/en/claude-code-on-the-web#setup-scripts) runs if configured.
  2. **Configure network** : internet access is set based on your environment’s [access level](https://code.claude.com/docs/en/claude-code-on-the-web#access-levels).
  3. **Work** : Claude analyzes code, makes changes, runs tests, and checks its work. You can watch and steer throughout, or step away and come back when it’s done.
  4. **Push the branch** : when Claude reaches a stopping point, it pushes its branch to GitHub. You review the diff, leave inline comments, create a PR, or send another message to keep going.

The session doesn’t close when the branch is pushed. PR creation and further edits all happen within the same conversation.
## 
[​](https://code.claude.com/docs/en/web-quickstart#compare-ways-to-run-claude-code)
Compare ways to run Claude Code
Claude Code behaves the same everywhere. What changes is where code executes and whether your local config is available. The Desktop app offers both local and cloud sessions, so its answers below depend on which you choose:  
|   | On the web  | Remote Control  | Terminal CLI  | Desktop app  |  
| --- | --- | --- | --- | --- |  
| **Code runs on**  | Anthropic cloud VM  | Your machine  | Your machine  | Your machine or cloud VM  |  
| **You chat from**  | claude.ai or mobile app  | claude.ai or mobile app  | Your terminal  | The Desktop UI  |  
| **Uses your local config**  | No, repo only  | Yes  | Yes  | Yes for local, no for cloud  |  
| **Requires GitHub**  | Yes, or [bundle a local repo](https://code.claude.com/docs/en/claude-code-on-the-web#send-local-repositories-without-github) via `--remote`  | No  | No  | Only for cloud sessions  |  
| **Keeps running if you disconnect**  | Yes  | While terminal stays open  | No  | Depends on session type  |  
| **[Permission modes](https://code.claude.com/docs/en/permission-modes)**  | Auto accept edits, Plan  | Ask, Auto accept edits, Plan  | All modes  | Depends on session type  |  
| **Network access**  | Configurable per environment  | Your machine’s network  | Your machine’s network  | Depends on session type  |  
See the [terminal quickstart](https://code.claude.com/docs/en/quickstart), [Desktop app](https://code.claude.com/docs/en/desktop), or [Remote Control](https://code.claude.com/docs/en/remote-control) docs to set those up.
## 
[​](https://code.claude.com/docs/en/web-quickstart#connect-github-and-create-an-environment)
Connect GitHub and create an environment
Setup is a one-time process. If you already use the GitHub CLI, you can [do this from your terminal](https://code.claude.com/docs/en/web-quickstart#connect-from-your-terminal) instead of the browser.
1
[](https://code.claude.com/docs/en/web-quickstart)
Visit claude.ai/code
Go to [claude.ai/code](https://claude.ai/code) and sign in with your Anthropic account.
2
[](https://code.claude.com/docs/en/web-quickstart)
Install the Claude GitHub App
After signing in, claude.ai/code prompts you to connect GitHub. Follow the prompt to install the Claude GitHub App and grant it access to your repositories. Cloud sessions work with existing GitHub repositories, so to start a new project, [create an empty repository on GitHub](https://github.com/new) first.
3
[](https://code.claude.com/docs/en/web-quickstart)
Create your environment
After connecting GitHub, you’ll be prompted to create a cloud environment. The environment controls what network access Claude has during sessions and what runs when a new session is created. See [Installed tools](https://code.claude.com/docs/en/claude-code-on-the-web#installed-tools) for what’s available without any configuration.The form has these fields:
  * **Name** : a display label. Useful when you have multiple environments for different projects or access levels.
  * **Network access** : controls what the session can reach on the internet. The default, `Trusted`, allows connections to [common package registries](https://code.claude.com/docs/en/claude-code-on-the-web#default-allowed-domains) like npm, PyPI, and RubyGems while blocking general internet access.
  * **Environment variables** : optional variables available in every session, in `.env` format. Don’t wrap values in quotes, since quotes are stored as part of the value. These are visible to anyone who can edit this environment.
  * **Setup script** : an optional Bash script that runs before Claude Code launches. Use it to install system tools the cloud VM doesn’t include, like `apt install -y gh`. The result is [cached](https://code.claude.com/docs/en/claude-code-on-the-web#environment-caching), so the script doesn’t re-run on every session. See [Setup scripts](https://code.claude.com/docs/en/claude-code-on-the-web#setup-scripts) for examples and debugging tips.

For a first project, leave the defaults and click **Create environment**. You can [edit it later or create additional environments](https://code.claude.com/docs/en/claude-code-on-the-web#configure-your-environment) for different projects.
### 
[​](https://code.claude.com/docs/en/web-quickstart#connect-from-your-terminal)
Connect from your terminal
If you already use the GitHub CLI (`gh`), you can set up Claude Code on the web without opening a browser. This requires the [Claude Code CLI](https://code.claude.com/docs/en/quickstart). `/web-setup` reads your local `gh` token, links it to your Claude account, and creates a default cloud environment if you don’t have one.
Organizations with [Zero Data Retention](https://code.claude.com/docs/en/zero-data-retention) enabled cannot use `/web-setup` or other cloud session features. If the GitHub CLI isn’t installed or authenticated, `/web-setup` opens the browser onboarding flow instead.
1
[](https://code.claude.com/docs/en/web-quickstart)
Authenticate with the GitHub CLI
In your shell, authenticate the GitHub CLI if you haven’t already:

```
gh auth login

```

2
[](https://code.claude.com/docs/en/web-quickstart)
Sign in to Claude
In the Claude Code CLI, run `/login` to sign in with your claude.ai account. Skip this step if you’re already signed in.
3
[](https://code.claude.com/docs/en/web-quickstart)
Run /web-setup
In the Claude Code CLI, run:

```
/web-setup

```

This syncs your `gh` token to your Claude account. If you don’t have a cloud environment yet, `/web-setup` creates one with Trusted network access and no setup script. You can [edit the environment or add variables](https://code.claude.com/docs/en/claude-code-on-the-web#configure-your-environment) afterward. Once `/web-setup` completes, you can start cloud sessions from your terminal with [`--remote`](https://code.claude.com/docs/en/claude-code-on-the-web#from-terminal-to-web) or set up recurring tasks with [`/schedule`](https://code.claude.com/docs/en/routines).
## 
[​](https://code.claude.com/docs/en/web-quickstart#start-a-task)
Start a task
With GitHub connected and an environment created, you’re ready to submit tasks.
1
[](https://code.claude.com/docs/en/web-quickstart)
Select a repository and branch
From [claude.ai/code](https://claude.ai/code) or the Code tab in the Claude mobile app, click the repository selector below the input box and choose a repository for Claude to work in. Each repository shows a branch selector. Change it to start Claude from a feature branch instead of the default. You can add multiple repositories to work across them in one session.
2
[](https://code.claude.com/docs/en/web-quickstart)
Choose a permission mode
The mode dropdown next to the input defaults to **Auto accept edits** , where Claude makes changes and pushes a branch without stopping for approval. Switch to **Plan mode** if you want Claude to propose an approach and wait for your go-ahead before editing files. Cloud sessions don’t offer Ask permissions, Auto mode, or Bypass permissions. See [Permission modes](https://code.claude.com/docs/en/permission-modes) for the full list.
3
[](https://code.claude.com/docs/en/web-quickstart)
Describe the task and submit
Type a description of what you want and press Enter. Be specific:
  * Name the file or function: “Add a README with setup instructions” or “Fix the failing auth test in `tests/test_auth.py`” is better than “fix tests”
  * Paste error output if you have it
  * Describe the expected behavior, not just the symptom

Claude clones the repositories, runs your setup script if configured, and starts working. Each task gets its own session and its own branch, so you don’t need to wait for one to finish before starting another.
## 
[​](https://code.claude.com/docs/en/web-quickstart#pre-fill-sessions)
Pre-fill sessions
You can prefill the prompt, repositories, and environment for a new session by adding query parameters to the [claude.ai/code](https://claude.ai/code) URL. Use this to build integrations such as a button in your issue tracker that opens Claude Code with the issue description as the prompt.  
| Parameter  | Description  |  
| --- | --- |  
| `prompt`  | Prompt text to prefill in the input box. The alias `q` is also accepted.  |  
| `prompt_url`  | URL to fetch the prompt text from, for prompts too long to embed in a query string. The URL must allow cross-origin requests. Ignored when `prompt` is also set.  |  
| `repositories`  | Comma-separated list of `owner/repo` slugs to preselect. The alias `repo` is also accepted.  |  
| `environment`  | Name or ID of the [environment](https://code.claude.com/docs/en/web-quickstart#connect-github-and-create-an-environment) to preselect.  |  
URL-encode each value. The example below opens the form with a prompt and a repository already selected:

```
https://claude.ai/code?prompt=Fix%20the%20login%20bug&repositories=acme/webapp

```

## 
[​](https://code.claude.com/docs/en/web-quickstart#review-and-iterate)
Review and iterate
When Claude finishes, review the changes, leave feedback on specific lines, and keep going until the diff looks right.
1
[](https://code.claude.com/docs/en/web-quickstart)
Open the diff view
A diff indicator shows lines added and removed across the session, for example `+42 -18`. Select it to open the diff view, with a file list on the left and changes on the right.
2
[](https://code.claude.com/docs/en/web-quickstart)
Leave inline comments
Select any line in the diff, type your feedback, and press Enter. Comments queue up until you send your next message, then they’re bundled with it. Claude sees “at `src/auth.ts:47`, don’t catch the error here” alongside your main instruction, so you don’t have to describe where the problem is.
3
[](https://code.claude.com/docs/en/web-quickstart)
Create a pull request
When the diff looks right, select **Create PR** at the top of the diff view. You can open it as a full PR, a draft, or jump to GitHub’s compose page with a generated title and description.
4
[](https://code.claude.com/docs/en/web-quickstart)
Keep iterating after the PR
The session stays live after the PR is created. Paste CI failure output or reviewer comments into the chat and ask Claude to address them. To have Claude monitor the PR automatically, see [Auto-fix pull requests](https://code.claude.com/docs/en/claude-code-on-the-web#auto-fix-pull-requests).
## 
[​](https://code.claude.com/docs/en/web-quickstart#troubleshoot-setup)
Troubleshoot setup
### 
[​](https://code.claude.com/docs/en/web-quickstart#no-repositories-appear-after-connecting-github)
No repositories appear after connecting GitHub
The Claude GitHub App needs explicit access to each repository you want to use. On github.com, open **Settings → Applications → Claude → Configure** and verify your repo is listed under **Repository access**. Private repositories need the same authorization as public ones.
### 
[​](https://code.claude.com/docs/en/web-quickstart#the-page-only-shows-a-github-login-button)
The page only shows a GitHub login button
Cloud sessions require a connected GitHub account. Connect via the browser flow above, or run `/web-setup` from your terminal if you use the GitHub CLI. If you’d rather not connect GitHub at all, see [Remote Control](https://code.claude.com/docs/en/remote-control) to run Claude Code on your own machine and monitor it from the web.
### 
[​](https://code.claude.com/docs/en/web-quickstart#%E2%80%9Dnot-available-for-the-selected-organization%E2%80%9D)
”Not available for the selected organization”
Enterprise organizations may need an admin to enable Claude Code on the web. Contact your Anthropic account team.
### 
[​](https://code.claude.com/docs/en/web-quickstart#/web-setup-returns-%E2%80%9Cunknown-command%E2%80%9D)
`/web-setup` returns “Unknown command”
`/web-setup` runs inside the Claude Code CLI, not your shell. Launch `claude` first, then type `/web-setup` at the prompt. If you typed it inside Claude Code and still see the error, your CLI is older than v2.1.80 or you’re authenticated with an API key or third-party provider instead of a claude.ai subscription. Run `claude update`, then `/login` to sign in with your claude.ai account.
### 
[​](https://code.claude.com/docs/en/web-quickstart#%E2%80%9Dcould-not-create-a-cloud-environment%E2%80%9D-or-%E2%80%9Cno-cloud-environment-available%E2%80%9D-when-using-remote-or-ultraplan)
”Could not create a cloud environment” or “No cloud environment available” when using `--remote` or ultraplan
Remote-session features create a default cloud environment automatically if you don’t have one. If you see “Could not create a cloud environment”, automatic creation failed. If you see “No cloud environment available”, your CLI predates automatic creation. In either case, run `/web-setup` in the Claude Code CLI to create one manually, or visit [claude.ai/code](https://claude.ai/code) and follow the **Create your environment** step above.
### 
[​](https://code.claude.com/docs/en/web-quickstart#setup-script-failed)
Setup script failed
The setup script exited with a non-zero status, which blocks the session from starting. Common causes:
  * A package install failed because the registry isn’t in your [network access level](https://code.claude.com/docs/en/claude-code-on-the-web#access-levels). `Trusted` covers most package managers; `None` blocks them all.
  * The script references a file or path that doesn’t exist in a fresh clone.
  * A command that works locally needs a different invocation on Ubuntu.

To debug, add `set -x` at the top of the script to see which command failed. For non-critical commands, append `|| true` so they don’t block session start.
### 
[​](https://code.claude.com/docs/en/web-quickstart#session-keeps-running-after-closing-the-tab)
Session keeps running after closing the tab
This is by design. Closing the tab or navigating away doesn’t stop the session. It continues running in the background until Claude finishes the current task, then idles. From the sidebar, you can [archive a session](https://code.claude.com/docs/en/claude-code-on-the-web#archive-sessions) to hide it from your list, or [delete it](https://code.claude.com/docs/en/claude-code-on-the-web#delete-sessions) to remove it permanently.
## 
[​](https://code.claude.com/docs/en/web-quickstart#next-steps)
Next steps
Now that you can submit and review tasks, these pages cover what comes next: starting cloud sessions from your terminal, scheduling recurring work, and giving Claude standing instructions.
  * [Use Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web): the full reference, including teleporting sessions to your terminal, setup scripts, environment variables, and network config
  * [Routines](https://code.claude.com/docs/en/routines): automate work on a schedule, via API call, or in response to GitHub events
  * [CLAUDE.md](https://code.claude.com/docs/en/memory): give Claude persistent instructions and context that load at the start of every session
  * Install the Claude mobile app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) or [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) to monitor sessions from your phone. From the Claude Code CLI, `/mobile` shows a QR code.


Was this page helpful?
YesNo
[Remote Control](https://code.claude.com/docs/en/remote-control)[Reference](https://code.claude.com/docs/en/claude-code-on-the-web)
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
[Privacy choices](https://code.claude.com/docs/en/web-quickstart)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
