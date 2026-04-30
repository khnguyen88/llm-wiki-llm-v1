<!--
url: https://code.claude.com/docs/en/github-enterprise-server
download_date: 2026-04-29
website: claude-code
webpage: github-enterprise-server
-->

# Github Enterprise Server

[Skip to main content](https://code.claude.com/docs/en/github-enterprise-server#content-area)
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
Code review & CI/CD
Claude Code with GitHub Enterprise Server
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
    * [Code Review](https://code.claude.com/docs/en/code-review)
    * [GitHub Actions](https://code.claude.com/docs/en/github-actions)
    * [GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server)
    * [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd)
  * [Claude Code in Slack](https://code.claude.com/docs/en/slack)


On this page
  * [What works with GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server#what-works-with-github-enterprise-server)
  * [Admin setup](https://code.claude.com/docs/en/github-enterprise-server#admin-setup)
  * [GitHub App permissions](https://code.claude.com/docs/en/github-enterprise-server#github-app-permissions)
  * [Manual setup](https://code.claude.com/docs/en/github-enterprise-server#manual-setup)
  * [Network requirements](https://code.claude.com/docs/en/github-enterprise-server#network-requirements)
  * [Developer workflow](https://code.claude.com/docs/en/github-enterprise-server#developer-workflow)
  * [Teleport sessions to your terminal](https://code.claude.com/docs/en/github-enterprise-server#teleport-sessions-to-your-terminal)
  * [Plugin marketplaces on GHES](https://code.claude.com/docs/en/github-enterprise-server#plugin-marketplaces-on-ghes)
  * [Add a GHES marketplace](https://code.claude.com/docs/en/github-enterprise-server#add-a-ghes-marketplace)
  * [Allowlist GHES marketplaces in managed settings](https://code.claude.com/docs/en/github-enterprise-server#allowlist-ghes-marketplaces-in-managed-settings)
  * [Limitations](https://code.claude.com/docs/en/github-enterprise-server#limitations)
  * [Troubleshooting](https://code.claude.com/docs/en/github-enterprise-server#troubleshooting)
  * [Web session fails to clone repository](https://code.claude.com/docs/en/github-enterprise-server#web-session-fails-to-clone-repository)
  * [Marketplace add fails with a policy error](https://code.claude.com/docs/en/github-enterprise-server#marketplace-add-fails-with-a-policy-error)
  * [GHES instance not reachable](https://code.claude.com/docs/en/github-enterprise-server#ghes-instance-not-reachable)
  * [Related resources](https://code.claude.com/docs/en/github-enterprise-server#related-resources)


Code review & CI/CD
# Claude Code with GitHub Enterprise Server
Copy page
Connect Claude Code to your self-hosted GitHub Enterprise Server instance for web sessions, code review, and plugin marketplaces.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
GitHub Enterprise Server support is available for Team and Enterprise plans.
GitHub Enterprise Server (GHES) support lets your organization use Claude Code with repositories hosted on your self-managed GitHub instance instead of github.com. Once an admin connects your GHES instance, developers can run web sessions, get automated code reviews, and install plugins from internal marketplaces without any per-repository configuration. For repositories on github.com, see [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) and [Code Review](https://code.claude.com/docs/en/code-review). To run Claude in your own CI infrastructure, see [GitHub Actions](https://code.claude.com/docs/en/github-actions).
## 
[​](https://code.claude.com/docs/en/github-enterprise-server#what-works-with-github-enterprise-server)
What works with GitHub Enterprise Server
The table below shows which Claude Code features support GHES and any differences from github.com behavior.  
| Feature  | GHES support  | Notes  |  
| --- | --- | --- |  
| Claude Code on the web  | ✅ Supported  | Admin connects the GHES instance once; developers use `claude --remote` or [claude.ai/code](https://claude.ai/code) as usual  |  
| Code Review  | ✅ Supported  | Same automated PR reviews as github.com  |  
| Teleport sessions  | ✅ Supported  | Move sessions between web and terminal with `--teleport`  |  
| Plugin marketplaces  | ✅ Supported  | Use full git URLs instead of `owner/repo` shorthand  |  
| Contribution metrics  | ✅ Supported  | Delivered via webhooks to the [analytics dashboard](https://code.claude.com/docs/en/analytics)  |  
| GitHub Actions  | ✅ Supported  | Requires manual workflow setup; `/install-github-app` is github.com only  |  
| GitHub MCP server  | ❌ Not supported  | The GitHub MCP server does not work with GHES instances  |  
## 
[​](https://code.claude.com/docs/en/github-enterprise-server#admin-setup)
Admin setup
An admin connects your GHES instance to Claude Code once. After that, developers in your organization can use GHES repositories without any additional configuration. You need admin access to your Claude organization and permission to create GitHub Apps on your GHES instance. The guided setup generates a GitHub App manifest and redirects you to your GHES instance to create the app in one click. If your environment blocks the redirect flow, an [alternative manual setup](https://code.claude.com/docs/en/github-enterprise-server#manual-setup) is available.
1
[](https://code.claude.com/docs/en/github-enterprise-server)
Open Claude Code admin settings
Go to [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code) and find the GitHub Enterprise Server section.
2
[](https://code.claude.com/docs/en/github-enterprise-server)
Start the guided setup
Click **Connect**. Enter a display name for the connection and your GHES hostname, for example `github.example.com`. If your GHES instance uses a self-signed or private certificate authority, paste the CA certificate in the optional field.
3
[](https://code.claude.com/docs/en/github-enterprise-server)
Create the GitHub App
Click **Continue to GitHub Enterprise**. Your browser redirects to your GHES instance with a pre-filled app manifest. Review the configuration and click **Create GitHub App**. GHES redirects you back to Claude with the app credentials stored automatically.
4
[](https://code.claude.com/docs/en/github-enterprise-server)
Install the app on your repositories
From the GitHub App page on your GHES instance, install the app on the repositories or organizations you want Claude to access. You can start with a subset and add more later.
5
[](https://code.claude.com/docs/en/github-enterprise-server)
Enable features
Return to [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code) and enable [Code Review](https://code.claude.com/docs/en/code-review#set-up-code-review) and [contribution metrics](https://code.claude.com/docs/en/analytics#enable-contribution-metrics) for your GHES repositories using the same configuration as github.com.
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#github-app-permissions)
GitHub App permissions
The manifest configures the GitHub App with the permissions and webhook events Claude needs across web sessions, Code Review, and contribution metrics:  
| Permission  | Access  | Used for  |  
| --- | --- | --- |  
| Contents  | Read and write  | Cloning repositories and pushing branches  |  
| Pull requests  | Read and write  | Creating PRs and posting review comments  |  
| Issues  | Read and write  | Responding to issue mentions  |  
| Checks  | Read and write  | Posting Code Review check runs  |  
| Actions  | Read  | Reading CI status for auto-fix  |  
| Repository hooks  | Read and write  | Receiving webhooks for contribution metrics  |  
| Metadata  | Read  | Required by GitHub for all apps  |  
The app subscribes to `pull_request`, `issue_comment`, `pull_request_review_comment`, `pull_request_review`, and `check_run` events.
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#manual-setup)
Manual setup
If the guided redirect flow is blocked by your network configuration, click **Add manually** instead of Connect. Create a GitHub App on your GHES instance with the [permissions and events above](https://code.claude.com/docs/en/github-enterprise-server#github-app-permissions), then enter the app credentials in the form: hostname, OAuth client ID and secret, GitHub App ID, client ID, client secret, webhook secret, and private key.
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#network-requirements)
Network requirements
Your GHES instance must be reachable from Anthropic infrastructure so Claude can clone repositories and post review comments. If your GHES instance is behind a firewall, allowlist the [Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses).
## 
[​](https://code.claude.com/docs/en/github-enterprise-server#developer-workflow)
Developer workflow
Once your admin has connected the GHES instance, no developer-side configuration is needed. Claude Code detects your GHES hostname automatically from the git remote in your working directory. Clone a repository from your GHES instance as you normally would:

```
git clone git@github.example.com:platform/api-service.git
cd api-service

```

Then start a web session. Claude detects the GHES host from your git remote and routes the session through your organization’s configured instance:

```
claude --remote "Add retry logic to the payment webhook handler"

```

The session runs on Anthropic infrastructure, clones your repository from GHES, and pushes changes back to a branch. Monitor progress with `/tasks` or at [claude.ai/code](https://claude.ai/code). See [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) for the full remote session workflow including diff review, auto-fix, and routines.
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#teleport-sessions-to-your-terminal)
Teleport sessions to your terminal
Pull a web session into your local terminal with `claude --teleport`. Teleport verifies you’re in a checkout of the same GHES repository before fetching the branch and loading the session history. See [teleport requirements](https://code.claude.com/docs/en/claude-code-on-the-web#teleport-requirements) for details.
## 
[​](https://code.claude.com/docs/en/github-enterprise-server#plugin-marketplaces-on-ghes)
Plugin marketplaces on GHES
Host plugin marketplaces on your GHES instance to distribute internal tooling across your organization. The marketplace structure is identical to github.com-hosted marketplaces; the only difference is how you reference them.
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#add-a-ghes-marketplace)
Add a GHES marketplace
The `owner/repo` shorthand always resolves to github.com. For GHES-hosted marketplaces, use the full git URL:

```
/plugin marketplace add git@github.example.com:platform/claude-plugins.git

```

HTTPS URLs work as well:

```
/plugin marketplace add https://github.example.com/platform/claude-plugins.git

```

See [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) for the full guide to building marketplaces.
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#allowlist-ghes-marketplaces-in-managed-settings)
Allowlist GHES marketplaces in managed settings
If your organization uses [managed settings](https://code.claude.com/docs/en/settings) to restrict which marketplaces developers can add, use the `hostPattern` source type to allow all marketplaces from your GHES instance without enumerating each repository:

```
{
  "strictKnownMarketplaces": [
    {
      "source": "hostPattern",
      "hostPattern": "^github\\.example\\.com$"
    }
  ]
}

```

You can also pre-register marketplaces for developers so they appear without manual setup. This example makes an internal tools marketplace available organization-wide:

```
{
  "extraKnownMarketplaces": {
    "internal-tools": {
      "source": {
        "source": "git",
        "url": "git@github.example.com:platform/claude-plugins.git"
      }
    }
  }
}

```

See the [strictKnownMarketplaces](https://code.claude.com/docs/en/settings#strictknownmarketplaces) and [extraKnownMarketplaces](https://code.claude.com/docs/en/settings#extraknownmarketplaces) settings reference for the complete schema.
## 
[​](https://code.claude.com/docs/en/github-enterprise-server#limitations)
Limitations
A few features behave differently on GHES than on github.com. The [feature table](https://code.claude.com/docs/en/github-enterprise-server#what-works-with-github-enterprise-server) summarizes support; this section covers the workarounds.
  * **`/install-github-app`command** : follow the [admin setup](https://code.claude.com/docs/en/github-enterprise-server#admin-setup) flow on claude.ai instead. If you also want GitHub Actions workflows on GHES, adapt the [example workflow](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml) manually.
  * **GitHub MCP server** : use the `gh` CLI configured for your GHES host instead. Run `gh auth login --hostname github.example.com` to authenticate, then Claude can use `gh` commands in sessions.


## 
[​](https://code.claude.com/docs/en/github-enterprise-server#troubleshooting)
Troubleshooting
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#web-session-fails-to-clone-repository)
Web session fails to clone repository
If `claude --remote` fails with a clone error, verify that your admin has completed setup for your GHES instance and that the GitHub App is installed on the repository you’re working in. Check with your admin that the instance hostname registered in Claude settings matches the hostname in your git remote.
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#marketplace-add-fails-with-a-policy-error)
Marketplace add fails with a policy error
If `/plugin marketplace add` is blocked for your GHES URL, your organization has restricted marketplace sources. Ask your admin to add a `hostPattern` entry for your GHES hostname in [managed settings](https://code.claude.com/docs/en/github-enterprise-server#allowlist-ghes-marketplaces-in-managed-settings).
### 
[​](https://code.claude.com/docs/en/github-enterprise-server#ghes-instance-not-reachable)
GHES instance not reachable
If reviews or web sessions time out, your GHES instance may not be reachable from Anthropic infrastructure. Confirm your firewall allows inbound connections from the [Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses).
## 
[​](https://code.claude.com/docs/en/github-enterprise-server#related-resources)
Related resources
These pages cover the features referenced throughout this guide in more depth:
  * [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web): run Claude Code sessions on cloud infrastructure
  * [Code Review](https://code.claude.com/docs/en/code-review): automated PR reviews
  * [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces): build and distribute plugin catalogs
  * [Analytics](https://code.claude.com/docs/en/analytics): track usage and contribution metrics
  * [Managed settings](https://code.claude.com/docs/en/settings): organization-wide policy configuration
  * [Network configuration](https://code.claude.com/docs/en/network-config): firewall and IP allowlist requirements


Was this page helpful?
YesNo
[GitHub Actions](https://code.claude.com/docs/en/github-actions)[GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd)
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
[Privacy choices](https://code.claude.com/docs/en/github-enterprise-server)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
