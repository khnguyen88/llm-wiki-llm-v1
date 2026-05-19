<!--
url: https://code.claude.com/docs/en/admin-setup
download_date: 2026-04-29
website: claude-code
webpage: admin-setup
-->

# Admin Setup

[Skip to main content](https://code.claude.com/docs/en/admin-setup#content-area)
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
Setup and access
Set up Claude Code for your organization
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Setup and access
  * [Administration overview](https://code.claude.com/docs/en/admin-setup)
  * [Advanced setup](https://code.claude.com/docs/en/setup)
  * [Authentication](https://code.claude.com/docs/en/authentication)
  * [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings)
  * [Auto mode](https://code.claude.com/docs/en/auto-mode-config)


##### Deployment
  * [Overview](https://code.claude.com/docs/en/third-party-integrations)
  * [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock)
  * [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai)
  * [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry)
  * [Network configuration](https://code.claude.com/docs/en/network-config)
  * [LLM gateway](https://code.claude.com/docs/en/llm-gateway)
  * [Development containers](https://code.claude.com/docs/en/devcontainer)


##### Usage and costs
  * [Monitoring](https://code.claude.com/docs/en/monitoring-usage)
  * [Costs](https://code.claude.com/docs/en/costs)
  * [Track team usage with analytics](https://code.claude.com/docs/en/analytics)


##### Plugin distribution
  * [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
  * [Plugin dependency versions](https://code.claude.com/docs/en/plugin-dependencies)


##### Security and data
  * [Security](https://code.claude.com/docs/en/security)
  * [Data usage](https://code.claude.com/docs/en/data-usage)
  * [Zero data retention](https://code.claude.com/docs/en/zero-data-retention)


##### Adoption
  * [Communications kit](https://code.claude.com/docs/en/communications-kit)
  * [Champion kit](https://code.claude.com/docs/en/champion-kit)


On this page
  * [Choose your API provider](https://code.claude.com/docs/en/admin-setup#choose-your-api-provider)
  * [Decide how settings reach devices](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)
  * [Decide what to enforce](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)
  * [Set up usage visibility](https://code.claude.com/docs/en/admin-setup#set-up-usage-visibility)
  * [Review data handling](https://code.claude.com/docs/en/admin-setup#review-data-handling)
  * [Verify and onboard](https://code.claude.com/docs/en/admin-setup#verify-and-onboard)
  * [Next steps](https://code.claude.com/docs/en/admin-setup#next-steps)


Setup and access
# Set up Claude Code for your organization
Copy page
A decision map for administrators deploying Claude Code, covering API providers, managed settings, policy enforcement, usage monitoring, and data handling.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Claude Code enforces organization policy through managed settings that take precedence over local developer configuration. You deliver those settings from the Claude admin console, your mobile device management (MDM) system, or a file on disk. The settings control which tools, commands, servers, and network destinations Claude can reach. This page walks through the deployment decisions in order. Each row links to the section below and to the reference page for that area.
SSO, SCIM provisioning, and seat assignment are configured at the Claude account level. See the [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide) and [seat assignment](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan) for those steps.  
| Decision  | What you’re choosing  | Reference  |  
| --- | --- | --- |  
| [Choose your API provider](https://code.claude.com/docs/en/admin-setup#choose-your-api-provider)  | Where Claude Code authenticates and how it’s billed  |  [Authentication](https://code.claude.com/docs/en/authentication), [Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Vertex AI](https://code.claude.com/docs/en/google-vertex-ai), [Foundry](https://code.claude.com/docs/en/microsoft-foundry)  |  
| [Decide how settings reach devices](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)  | How managed policy reaches developer machines  |  [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings), [Settings files](https://code.claude.com/docs/en/settings#settings-files)  |  
| [Decide what to enforce](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)  | Which tools, commands, and integrations are allowed  |  [Permissions](https://code.claude.com/docs/en/permissions), [Sandboxing](https://code.claude.com/docs/en/sandboxing)  |  
| [Set up usage visibility](https://code.claude.com/docs/en/admin-setup#set-up-usage-visibility)  | How you track spend and adoption  |  [Analytics](https://code.claude.com/docs/en/analytics), [Monitoring](https://code.claude.com/docs/en/monitoring-usage), [Costs](https://code.claude.com/docs/en/costs)  |  
| [Review data handling](https://code.claude.com/docs/en/admin-setup#review-data-handling)  | Data retention and compliance posture  |  [Data usage](https://code.claude.com/docs/en/data-usage), [Security](https://code.claude.com/docs/en/security)  |  
## 
[​](https://code.claude.com/docs/en/admin-setup#choose-your-api-provider)
Choose your API provider
Claude Code connects to Claude through one of several API providers. Your choice affects billing, authentication, and which compliance posture you inherit.  
| Provider  | Choose this when  |  
| --- | --- |  
| Claude for Teams / Enterprise  | You want Claude Code and claude.ai under one per-seat subscription with no infrastructure to run. This is the default recommendation.  |  
| Claude Console  | You’re API-first or want pay-as-you-go billing  |  
| Amazon Bedrock  | You want to inherit existing AWS compliance controls and billing  |  
| Google Vertex AI  | You want to inherit existing GCP compliance controls and billing  |  
| Microsoft Foundry  | You want to inherit existing Azure compliance controls and billing  |  
For the full provider comparison covering authentication, regions, and feature parity, see the [enterprise deployment overview](https://code.claude.com/docs/en/third-party-integrations). Each provider’s auth setup is in [Authentication](https://code.claude.com/docs/en/authentication). Proxy and firewall requirements in [Network configuration](https://code.claude.com/docs/en/network-config) apply regardless of provider. If you want a single endpoint in front of multiple providers or centralized request logging, see [LLM gateway](https://code.claude.com/docs/en/llm-gateway).
## 
[​](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)
Decide how settings reach devices
Managed settings define policy that takes precedence over local developer configuration. Claude Code looks for them in four places and uses the first one it finds on a given device.  
| Mechanism  | Delivery  | Priority  | Platforms  |  
| --- | --- | --- | --- |  
| Server-managed  | Claude.ai admin console  | Highest  | All  |  
| plist / registry policy  | macOS: `com.anthropic.claudecode` plist  
Windows: `HKLM\SOFTWARE\Policies\ClaudeCode`  | High  | macOS, Windows  |  
| File-based managed  | macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`  
Linux and WSL: `/etc/claude-code/managed-settings.json`  
Windows: `C:\Program Files\ClaudeCode\managed-settings.json`  | Medium  | All  |  
| Windows user registry  | `HKCU\SOFTWARE\Policies\ClaudeCode`  | Lowest  | Windows only  |  
Server-managed settings reach devices at authentication time and refresh hourly during active sessions, with no endpoint infrastructure. They require a Claude for Teams or Enterprise plan, so deployments on other providers need one of the file-based or OS-level mechanisms instead. If your organization mixes providers, configure [server-managed settings](https://code.claude.com/docs/en/server-managed-settings) for Claude.ai users plus a [file-based or plist/registry fallback](https://code.claude.com/docs/en/settings#settings-files) so other users still receive managed policy. The plist and HKLM registry locations work with any provider and resist tampering because they require admin privileges to write. The Windows user registry at HKCU is writable without elevation, so treat it as a convenience default rather than an enforcement channel. By default WSL reads only the Linux file path at `/etc/claude-code`. To extend your Windows registry and `C:\Program Files\ClaudeCode` policy to WSL on the same machine, set [`wslInheritsWindowsSettings: true`](https://code.claude.com/docs/en/settings#available-settings) in either of those admin-only Windows sources. Whichever mechanism you choose, managed values take precedence over user and project settings. Array settings such as `permissions.allow` and `permissions.deny` merge entries from all sources, so developers can extend managed lists but not remove from them. See [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings) and [Settings files and precedence](https://code.claude.com/docs/en/settings#settings-files).
## 
[​](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)
Decide what to enforce
Managed settings can lock down tools, sandbox execution, restrict MCP servers and plugin sources, and control which hooks run. Each row is a control surface with the setting keys that drive it.  
| Control  | What it does  | Key settings  |  
| --- | --- | --- |  
| [Permission rules](https://code.claude.com/docs/en/permissions)  | Allow, ask, or deny specific tools and commands  |  `permissions.allow`, `permissions.deny`  |  
| [Permission lockdown](https://code.claude.com/docs/en/permissions#managed-only-settings)  | Only managed permission rules apply; disable `--dangerously-skip-permissions`  |  `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode`  |  
| [Sandboxing](https://code.claude.com/docs/en/sandboxing)  | OS-level filesystem and network isolation with domain allowlists  |  `sandbox.enabled`, `sandbox.network.allowedDomains`  |  
| [Managed policy CLAUDE.md](https://code.claude.com/docs/en/memory#deploy-organization-wide-claude-md)  | Org-wide instructions loaded in every session, cannot be excluded  | File at the managed policy path  |  
| [MCP server control](https://code.claude.com/docs/en/mcp#managed-mcp-configuration)  | Restrict which MCP servers users can add or connect to  |  `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`  |  
| [Plugin marketplace control](https://code.claude.com/docs/en/plugin-marketplaces#managed-marketplace-restrictions)  | Restrict which marketplace sources users can add and install from  |  `strictKnownMarketplaces`, `blockedMarketplaces`  |  
| [Hook restrictions](https://code.claude.com/docs/en/settings#hook-configuration)  | Only managed hooks load; restrict HTTP hook URLs  |  `allowManagedHooksOnly`, `allowedHttpHookUrls`  |  
| [Version floor](https://code.claude.com/docs/en/settings)  | Prevent auto-update from installing below an org-wide minimum  | `minimumVersion`  |  
Permission rules and sandboxing cover different layers. Denying WebFetch blocks Claude’s fetch tool, but if Bash is allowed, `curl` and `wget` can still reach any URL. Sandboxing closes that gap with a network domain allowlist enforced at the OS level. For the threat model these controls defend against, see [Security](https://code.claude.com/docs/en/security).
## 
[​](https://code.claude.com/docs/en/admin-setup#set-up-usage-visibility)
Set up usage visibility
Choose monitoring based on what you need to report on.  
| Capability  | What you get  | Availability  | Where to start  |  
| --- | --- | --- | --- |  
| Usage monitoring  | OpenTelemetry export of sessions, tools, and tokens  | All providers  | [Monitoring usage](https://code.claude.com/docs/en/monitoring-usage)  |  
| Analytics dashboard  | Per-user metrics, contribution tracking, leaderboard  | Anthropic only  | [Analytics](https://code.claude.com/docs/en/analytics)  |  
| Cost tracking  | Spend limits, rate limits, and usage attribution  | Anthropic only  | [Costs](https://code.claude.com/docs/en/costs)  |  
Cloud providers expose spend through AWS Cost Explorer, GCP Billing, or Azure Cost Management. Claude for Teams and Enterprise plans include a usage dashboard at [claude.ai/analytics/claude-code](https://claude.ai/analytics/claude-code).
## 
[​](https://code.claude.com/docs/en/admin-setup#review-data-handling)
Review data handling
On Team, Enterprise, Claude API, and cloud provider plans, Anthropic does not train models on your code or prompts. Your API provider determines retention and compliance posture.  
| Topic  | What to know  | Where to start  |  
| --- | --- | --- |  
| Data usage policy  | What Anthropic collects, how long it’s retained, what’s never used for training  | [Data usage](https://code.claude.com/docs/en/data-usage)  |  
| Zero Data Retention (ZDR)  | Nothing stored after the request completes. Available on Claude for Enterprise  | [Zero data retention](https://code.claude.com/docs/en/zero-data-retention)  |  
| Security architecture  | Network model, encryption, authentication, audit trail  | [Security](https://code.claude.com/docs/en/security)  |  
If you need request-level audit logging or to route traffic by data sensitivity, place an [LLM gateway](https://code.claude.com/docs/en/llm-gateway) between developers and your provider. For regulatory requirements and certifications, see [Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance).
## 
[​](https://code.claude.com/docs/en/admin-setup#verify-and-onboard)
Verify and onboard
After configuring managed settings, have a developer run `/status` inside Claude Code. The output includes a line beginning with `Enterprise managed settings` followed by the source in parentheses, one of `(remote)`, `(plist)`, `(HKLM)`, `(HKCU)`, or `(file)`. See [Verify active settings](https://code.claude.com/docs/en/settings#verify-active-settings). Share these resources to help developers get started:
  * [Quickstart](https://code.claude.com/docs/en/quickstart): first-session walkthrough from install to working with a project
  * [Common workflows](https://code.claude.com/docs/en/common-workflows): patterns for everyday tasks like code review, refactoring, and debugging
  * [Claude 101](https://anthropic.skilljar.com/claude-101) and [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action): self-paced Anthropic Academy courses

For login issues, point developers to [authentication troubleshooting](https://code.claude.com/docs/en/troubleshoot-install#login-and-authentication). The most common fixes are:
  * Run `/logout` then `/login` to switch accounts
  * Run `claude update` if the enterprise auth option is missing
  * Restart the terminal after updating

If a developer sees “You haven’t been added to your organization yet,” their seat doesn’t include Claude Code access and needs to be updated in the admin console.
## 
[​](https://code.claude.com/docs/en/admin-setup#next-steps)
Next steps
With provider and delivery mechanism chosen, move on to detailed configuration:
  * [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings): deliver managed policy from the Claude admin console
  * [Settings reference](https://code.claude.com/docs/en/settings): every setting key, file location, and precedence rule
  * [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai), [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry): provider-specific deployment
  * [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide): SSO, SCIM, seat management, and rollout playbook


Was this page helpful?
YesNo
[Advanced setup](https://code.claude.com/docs/en/setup)
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
[Privacy choices](https://code.claude.com/docs/en/admin-setup)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
