<!--
url: https://code.claude.com/docs/en/auto-mode-config
download_date: 2026-04-29
website: claude-code
webpage: auto-mode-config
-->

# Auto Mode Config

[Skip to main content](https://code.claude.com/docs/en/auto-mode-config#content-area)
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
Configure auto mode
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
  * [Where the classifier reads configuration](https://code.claude.com/docs/en/auto-mode-config#where-the-classifier-reads-configuration)
  * [Define trusted infrastructure](https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure)
  * [Override the block and allow rules](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules)
  * [Inspect the defaults and your effective config](https://code.claude.com/docs/en/auto-mode-config#inspect-the-defaults-and-your-effective-config)
  * [Review denials](https://code.claude.com/docs/en/auto-mode-config#review-denials)
  * [See also](https://code.claude.com/docs/en/auto-mode-config#see-also)


Setup and access
# Configure auto mode
Copy page
Tell the auto mode classifier which repos, buckets, and domains your organization trusts. Set environment context, override the default block and allow rules, and inspect your effective config with the auto-mode CLI subcommands.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
[Auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) lets Claude Code run without permission prompts by routing each tool call through a classifier that blocks anything irreversible, destructive, or aimed outside your environment. Use the `autoMode` settings block to tell that classifier which repos, buckets, and domains your organization trusts, so it stops blocking routine internal operations. Out of the box, the classifier trusts only the working directory and the current repo’s configured remotes. Actions like pushing to your company’s source-control org or writing to a team cloud bucket are blocked until you add them to `autoMode.environment`. For how to enable auto mode and what it blocks by default, see [Permission modes](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode). This page is the configuration reference. This page covers how to:
  * [Choose where to set rules](https://code.claude.com/docs/en/auto-mode-config#where-the-classifier-reads-configuration) across CLAUDE.md, user settings, and managed settings
  * [Define trusted infrastructure](https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure) with `autoMode.environment`
  * [Override the block and allow rules](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules) when the defaults don’t fit your pipeline
  * [Inspect your effective config](https://code.claude.com/docs/en/auto-mode-config#inspect-the-defaults-and-your-effective-config) with the `claude auto-mode` subcommands
  * [Review denials](https://code.claude.com/docs/en/auto-mode-config#review-denials) so you know what to add next


## 
[​](https://code.claude.com/docs/en/auto-mode-config#where-the-classifier-reads-configuration)
Where the classifier reads configuration
The classifier reads the same [CLAUDE.md](https://code.claude.com/docs/en/memory) content Claude itself loads, so an instruction like “never force push” in your project’s CLAUDE.md steers both Claude and the classifier at the same time. Start there for project conventions and behavioral rules. For rules that apply across projects, such as trusted infrastructure or organization-wide deny rules, use the `autoMode` settings block. The classifier reads `autoMode` from the following scopes:  
| Scope  | File  | Use for  |  
| --- | --- | --- |  
| One developer  | `~/.claude/settings.json`  | Personal trusted infrastructure  |  
| One project, one developer  | `.claude/settings.local.json`  | Per-project trusted buckets or services, gitignored  |  
| Organization-wide  | [Managed settings](https://code.claude.com/docs/en/server-managed-settings)  | Trusted infrastructure distributed to all developers  |  
|  `--settings` flag or Agent SDK  | Inline JSON  | Per-invocation overrides for automation  |  
The classifier does not read `autoMode` from shared project settings in `.claude/settings.json`, so a checked-in repo cannot inject its own allow rules. Entries from each scope are combined. A developer can extend `environment`, `allow`, and `soft_deny` with personal entries but cannot remove entries that managed settings provide. Because allow rules act as exceptions to block rules inside the classifier, a developer-added `allow` entry can override an organization `soft_deny` entry: the combination is additive, not a hard policy boundary.
The classifier is a second gate that runs after the [permissions system](https://code.claude.com/docs/en/permissions). For actions that must never run regardless of user intent or classifier configuration, use `permissions.deny` in managed settings, which blocks the action before the classifier is consulted and cannot be overridden.
## 
[​](https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure)
Define trusted infrastructure
For most organizations, `autoMode.environment` is the only field you need to set. It tells the classifier which repos, buckets, and domains are trusted: the classifier uses it to decide what “external” means, so any destination not listed is a potential exfiltration target. The default environment list trusts the working repo and its configured remotes. To add your own entries alongside that default, include the literal string `"$defaults"` in the array. The default entries are spliced in at that position, so your custom entries can go before or after them.

```
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Source control: github.example.com/acme-corp and all repos under it",
      "Trusted cloud buckets: s3://acme-build-artifacts, gs://acme-ml-datasets",
      "Trusted internal domains: *.corp.example.com, api.internal.example.com",
      "Key internal services: Jenkins at ci.example.com, Artifactory at artifacts.example.com"
    ]
  }
}

```

Entries are prose, not regex or tool patterns. The classifier reads them as natural-language rules. Write them the way you would describe your infrastructure to a new engineer. A thorough environment section covers:
  * **Organization** : your company name and what Claude Code is primarily used for, like software development, infrastructure automation, or data engineering
  * **Source control** : every GitHub, GitLab, or Bitbucket org your developers push to
  * **Cloud providers and trusted buckets** : bucket names or prefixes that Claude should be able to read from and write to
  * **Trusted internal domains** : hostnames for APIs, dashboards, and services inside your network, like `*.internal.example.com`
  * **Key internal services** : CI, artifact registries, internal package indexes, incident tooling
  * **Additional context** : regulated-industry constraints, multi-tenant infrastructure, or compliance requirements that affect what the classifier should treat as risky

A useful starting template: fill in the bracketed fields and remove any lines that don’t apply.

```
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Organization: {COMPANY_NAME}. Primary use: {PRIMARY_USE_CASE, e.g. software development, infrastructure automation}",
      "Source control: {SOURCE_CONTROL, e.g. GitHub org github.example.com/acme-corp}",
      "Cloud provider(s): {CLOUD_PROVIDERS, e.g. AWS, GCP, Azure}",
      "Trusted cloud buckets: {TRUSTED_BUCKETS, e.g. s3://acme-builds, gs://acme-datasets}",
      "Trusted internal domains: {TRUSTED_DOMAINS, e.g. *.internal.example.com, api.example.com}",
      "Key internal services: {SERVICES, e.g. Jenkins at ci.example.com, Artifactory at artifacts.example.com}",
      "Additional context: {EXTRA, e.g. regulated industry, multi-tenant infrastructure, compliance requirements}"
    ]
  }
}

```

The more specific context you give, the better the classifier can distinguish routine internal operations from exfiltration attempts. You don’t need to fill everything in at once. A reasonable rollout: start with the defaults and add your source control org and key internal services, which resolves the most common false positives like pushing to your own repos. Add trusted domains and cloud buckets next. Fill the rest as blocks come up.
## 
[​](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules)
Override the block and allow rules
Two additional fields let you replace the classifier’s built-in rule lists: `autoMode.soft_deny` controls what gets blocked, and `autoMode.allow` controls which exceptions apply. Each is an array of prose descriptions, read as natural-language rules. There is no `autoMode.deny` field; to hard-block an action regardless of intent, use [`permissions.deny`](https://code.claude.com/docs/en/permissions), which runs before the classifier. Inside the classifier, precedence works in three tiers:
  * `soft_deny` rules block first
  * `allow` rules then override matching blocks as exceptions
  * Explicit user intent overrides both: if the user’s message directly and specifically describes the exact action Claude is about to take, the classifier allows it even when a `soft_deny` rule matches

General requests don’t count as explicit intent. Asking Claude to “clean up the repo” does not authorize force-pushing, but asking Claude to “force-push this branch” does. To loosen, add to `allow` when the classifier repeatedly flags a routine pattern the default exceptions don’t cover. To tighten, add to `soft_deny` for risks specific to your environment that the defaults miss. To keep the built-in rules while adding your own, include the literal string `"$defaults"` in the array. The default rules are spliced in at that position, so your custom rules can go before or after them, and you continue to inherit updates as the built-in list changes across releases.

```
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Source control: github.example.com/acme-corp and all repos under it"
    ],
    "allow": [
      "$defaults",
      "Deploying to the staging namespace is allowed: staging is isolated from production and resets nightly",
      "Writing to s3://acme-scratch/ is allowed: ephemeral bucket with a 7-day lifecycle policy"
    ],
    "soft_deny": [
      "$defaults",
      "Never run database migrations outside the migrations CLI, even against dev databases",
      "Never modify files under infra/terraform/prod/: production infrastructure changes go through the review workflow"
    ]
  }
}

```

Setting any of `environment`, `allow`, or `soft_deny` without `"$defaults"` replaces the entire default list for that section. If you set `soft_deny` with a single entry and omit `"$defaults"`, every built-in block rule is discarded: force push, data exfiltration, `curl | bash`, production deploys, and all other default block rules become allowed. Only omit `"$defaults"` when you intend to take full ownership of the list. In that case, run `claude auto-mode defaults` to print the built-in rules, copy them into your settings file, then review each rule against your own pipeline and risk tolerance.
Each section is evaluated independently, so setting `environment` alone leaves the default `allow` and `soft_deny` lists intact.
## 
[​](https://code.claude.com/docs/en/auto-mode-config#inspect-the-defaults-and-your-effective-config)
Inspect the defaults and your effective config
Three CLI subcommands help you inspect and validate your configuration. Print the built-in `environment`, `allow`, and `soft_deny` rules as JSON:

```
claude auto-mode defaults

```

Print what the classifier actually uses as JSON, with your settings applied where set and defaults otherwise:

```
claude auto-mode config

```

Get AI feedback on your custom `allow` and `soft_deny` rules:

```
claude auto-mode critique

```

Run `claude auto-mode config` after saving your settings to confirm the effective rules are what you expect, with `"$defaults"` expanded in place. If you’ve written custom rules, `claude auto-mode critique` reviews them and flags entries that are ambiguous, redundant, or likely to cause false positives. If you need to remove or rewrite a built-in rule rather than add alongside it, save the output of `claude auto-mode defaults` to a file, edit the lists, and paste the result into your settings file in place of `"$defaults"`.
## 
[​](https://code.claude.com/docs/en/auto-mode-config#review-denials)
Review denials
When auto mode denies a tool call, the denial is recorded in `/permissions` under the Recently denied tab. Press `r` on a denied action to mark it for retry: when you exit the dialog, Claude Code sends a message telling the model it may retry that tool call and resumes the conversation. Repeated denials for the same destination usually mean the classifier is missing context. Add that destination to `autoMode.environment`, then run `claude auto-mode config` to confirm it took effect. To react to denials programmatically, use the [`PermissionDenied` hook](https://code.claude.com/docs/en/hooks#permissiondenied).
## 
[​](https://code.claude.com/docs/en/auto-mode-config#see-also)
See also
  * [Permission modes](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode): what auto mode is, what it blocks by default, and how to enable it
  * [Managed settings](https://code.claude.com/docs/en/server-managed-settings): deploy `autoMode` configuration across your organization
  * [Permissions](https://code.claude.com/docs/en/permissions): allow, ask, and deny rules that apply before the classifier runs
  * [Settings](https://code.claude.com/docs/en/settings): the full settings reference, including the `autoMode` key


Was this page helpful?
YesNo
[Server-managed settings](https://code.claude.com/docs/en/server-managed-settings)[Overview](https://code.claude.com/docs/en/third-party-integrations)
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
[Privacy choices](https://code.claude.com/docs/en/auto-mode-config)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
