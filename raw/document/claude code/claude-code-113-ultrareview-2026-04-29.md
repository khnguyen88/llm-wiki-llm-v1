<!--
url: https://code.claude.com/docs/en/ultrareview
download_date: 2026-04-29
website: claude-code
webpage: ultrareview
-->

# Ultrareview

[Skip to main content](https://code.claude.com/docs/en/ultrareview#content-area)
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
Find bugs with ultrareview
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
  * [Run ultrareview from the CLI](https://code.claude.com/docs/en/ultrareview#run-ultrareview-from-the-cli)
  * [Pricing and free runs](https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs)
  * [Track a running review](https://code.claude.com/docs/en/ultrareview#track-a-running-review)
  * [Run ultrareview non-interactively](https://code.claude.com/docs/en/ultrareview#run-ultrareview-non-interactively)
  * [How ultrareview compares to /review](https://code.claude.com/docs/en/ultrareview#how-ultrareview-compares-to-%2Freview)
  * [Related resources](https://code.claude.com/docs/en/ultrareview#related-resources)


Claude Code on the web
# Find bugs with ultrareview
Copy page
Run a deep, multi-agent code review in the cloud with /ultrareview to find and verify bugs before you merge.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Ultrareview is a research preview feature available in Claude Code v2.1.86 and later. The feature, pricing, and availability may change based on feedback.
Ultrareview is a deep code review that runs on Claude Code on the web infrastructure. When you run `/ultrareview`, Claude Code launches a fleet of reviewer agents in a remote sandbox to find bugs in your branch or pull request. Compared to a local `/review`, ultrareview offers:
  * **Higher signal** : every reported finding is independently reproduced and verified, so the results focus on real bugs rather than style suggestions
  * **Broader coverage** : many reviewer agents explore the change in parallel, which surfaces issues that a single-pass review can miss
  * **No local resource use** : the review runs entirely in a remote sandbox, so your terminal stays free for other work while it runs

Ultrareview requires authentication with a Claude.ai account because it runs on Claude Code on the web infrastructure. If you are signed in with an API key only, run `/login` and authenticate with Claude.ai first. Ultrareview is not available when using Claude Code with Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry, and it is not available to organizations that have enabled Zero Data Retention.
## 
[​](https://code.claude.com/docs/en/ultrareview#run-ultrareview-from-the-cli)
Run ultrareview from the CLI
Start a review from any git repository in the Claude Code CLI.

```
/ultrareview

```

Without arguments, ultrareview reviews the diff between your current branch and the default branch, including any uncommitted and staged changes in your working tree. Claude Code bundles the repository state and uploads it to a remote sandbox for the review. To review a GitHub pull request instead, pass the PR number.

```
/ultrareview 1234

```

In PR mode, the remote sandbox clones the pull request directly from GitHub rather than bundling your local working tree. PR mode requires a `github.com` remote on the repository.
If your repository is too large to bundle, Claude Code prompts you to use PR mode instead. Push your branch and open a draft PR, then run `/ultrareview <PR-number>`.
Before launching, Claude Code shows a confirmation dialog with the review scope (including the file and line count when reviewing a branch), your remaining free runs, and the estimated cost. After you confirm, the review continues in the background and you can keep using your session. The command runs only when you invoke it with `/ultrareview`; Claude does not start an ultrareview on its own.
## 
[​](https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs)
Pricing and free runs
Ultrareview is a premium feature that bills against extra usage rather than your plan’s included usage.  
| Plan  | Included free runs  | After free runs  |  
| --- | --- | --- |  
| Pro  | 3 free runs through May 5, 2026  | billed as [extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)  |  
| Max  | 3 free runs through May 5, 2026  | billed as [extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)  |  
| Team and Enterprise  | none  | billed as [extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)  |  
Pro and Max subscribers receive three free ultrareview runs to try the feature. These three runs are a one-time allotment per account, do not refresh, and expire on May 5, 2026. After you use all three, or after the free run period ends, each review is billed to extra usage and typically costs $5 to $20 depending on the size of the change. A run counts once the remote session starts, so a review that you stop early or that fails to complete still uses a free run. For a paid review, extra usage is billed only for the portion that ran. Because ultrareview always bills as extra usage outside the free runs, your account or organization must have extra usage enabled before you can launch a paid review. If extra usage is not enabled, Claude Code blocks the launch and links you to the billing settings where you can turn it on. You can also run `/extra-usage` to check or change your current setting.
## 
[​](https://code.claude.com/docs/en/ultrareview#track-a-running-review)
Track a running review
A review typically takes 5 to 10 minutes. The review runs as a background task, so you can keep working in your session, start other commands, or close the terminal entirely. Use `/tasks` to see running and completed reviews, open the detail view for a review, or stop a review that is in progress. Stopping a review archives the cloud session, and partial findings are not returned. When the review finishes, the verified findings appear as a notification in your session. Each finding includes the file location and an explanation of the issue so you can ask Claude to fix it directly.
## 
[​](https://code.claude.com/docs/en/ultrareview#run-ultrareview-non-interactively)
Run ultrareview non-interactively
Use the `claude ultrareview` subcommand to start an ultrareview from CI or a script without an interactive session. The subcommand launches the same review as `/ultrareview`, blocks until the remote review finishes, prints the findings to stdout, and exits with code 0 on success or 1 on failure.

```
claude ultrareview
claude ultrareview 1234
claude ultrareview origin/main

```

Without arguments, the subcommand reviews the diff between your current branch and the default branch. Pass a PR number to review a pull request, or pass a base branch to review the diff against that branch instead. Invoking the subcommand counts as consent for the billing and terms prompt that the interactive command shows. Progress messages and the live session URL go to stderr so stdout stays parseable. Use these flags to control the output and timeout:  
| Flag  | Description  |  
| --- | --- |  
| `--json`  | Print the raw `bugs.json` payload instead of the formatted findings  |  
| `--timeout <minutes>`  | Maximum minutes to wait for the review to finish. Defaults to 30  |  
Running `claude ultrareview` requires the same authentication and extra usage configuration as `/ultrareview`. The subcommand exits with code 0 when the review completes with or without findings, code 1 when the review fails to launch, the remote session errors, or the timeout elapses, and code 130 when interrupted with Ctrl-C. The remote review keeps running if you interrupt the subcommand; follow the session URL printed to stderr to watch it in the browser. For automatic reviews on GitHub pull requests, [Code Review](https://code.claude.com/docs/en/code-review) integrates with your repository directly and posts findings as inline PR comments without a CLI step.
## 
[​](https://code.claude.com/docs/en/ultrareview#how-ultrareview-compares-to-/review)
How ultrareview compares to /review
Both commands review code, but they target different stages of your workflow.  
|   | `/review`  | `/ultrareview`  |  
| --- | --- | --- |  
| Runs  | locally in your session  | remotely in a cloud sandbox  |  
| Depth  | single-pass review  | multi-agent fleet with independent verification  |  
| Duration  | seconds to a few minutes  | roughly 5 to 10 minutes  |  
| Cost  | counts toward normal usage  | free runs, then roughly $5 to $20 per review as extra usage  |  
| Best for  | quick feedback while iterating  | pre-merge confidence on substantial changes  |  
Use `/review` for fast feedback as you work. Use `/ultrareview` before merging a substantial change when you want a deeper pass that catches issues a single review might miss.
## 
[​](https://code.claude.com/docs/en/ultrareview#related-resources)
Related resources
  * [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web): learn how remote sessions and cloud sandboxes work
  * [Plan complex changes with ultraplan](https://code.claude.com/docs/en/ultraplan): the planning counterpart to ultrareview for upfront design work
  * [Manage costs effectively](https://code.claude.com/docs/en/costs): track usage and set spending limits


Was this page helpful?
YesNo
[Plan in the cloud](https://code.claude.com/docs/en/ultraplan)[Get started](https://code.claude.com/docs/en/desktop-quickstart)
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
[Privacy choices](https://code.claude.com/docs/en/ultrareview)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
