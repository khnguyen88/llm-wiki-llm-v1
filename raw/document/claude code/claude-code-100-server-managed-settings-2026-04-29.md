<!--
url: https://code.claude.com/docs/en/server-managed-settings
download_date: 2026-04-29
website: claude-code
webpage: server-managed-settings
-->

# Server Managed Settings

[Skip to main content](https://code.claude.com/docs/en/server-managed-settings#content-area)
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
Configure server-managed settings
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
  * [Requirements](https://code.claude.com/docs/en/server-managed-settings#requirements)
  * [Choose between server-managed and endpoint-managed settings](https://code.claude.com/docs/en/server-managed-settings#choose-between-server-managed-and-endpoint-managed-settings)
  * [Configure server-managed settings](https://code.claude.com/docs/en/server-managed-settings#configure-server-managed-settings)
  * [Verify settings delivery](https://code.claude.com/docs/en/server-managed-settings#verify-settings-delivery)
  * [Access control](https://code.claude.com/docs/en/server-managed-settings#access-control)
  * [Managed-only settings](https://code.claude.com/docs/en/server-managed-settings#managed-only-settings)
  * [Current limitations](https://code.claude.com/docs/en/server-managed-settings#current-limitations)
  * [Settings delivery](https://code.claude.com/docs/en/server-managed-settings#settings-delivery)
  * [Settings precedence](https://code.claude.com/docs/en/server-managed-settings#settings-precedence)
  * [Fetch and caching behavior](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
  * [Enforce fail-closed startup](https://code.claude.com/docs/en/server-managed-settings#enforce-fail-closed-startup)
  * [Security approval dialogs](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)
  * [Platform availability](https://code.claude.com/docs/en/server-managed-settings#platform-availability)
  * [Audit logging](https://code.claude.com/docs/en/server-managed-settings#audit-logging)
  * [Security considerations](https://code.claude.com/docs/en/server-managed-settings#security-considerations)
  * [See also](https://code.claude.com/docs/en/server-managed-settings#see-also)


Setup and access
# Configure server-managed settings
Copy page
Centrally configure Claude Code for your organization through server-delivered settings, without requiring device management infrastructure.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Server-managed settings allow administrators to centrally configure Claude Code through a web-based interface on Claude.ai. Claude Code clients automatically receive these settings when users authenticate with their organization credentials. This approach is designed for organizations that do not have device management infrastructure in place, or need to manage settings for users on unmanaged devices.
Server-managed settings are available for [Claude for Teams](https://claude.com/pricing?utm_source=claude_code&utm_medium=docs&utm_content=server_settings_teams#team-&-enterprise) and [Claude for Enterprise](https://anthropic.com/contact-sales?utm_source=claude_code&utm_medium=docs&utm_content=server_settings_enterprise) customers.
## 
[​](https://code.claude.com/docs/en/server-managed-settings#requirements)
Requirements
To use server-managed settings, you need:
  * Claude for Teams or Claude for Enterprise plan
  * Claude Code version 2.1.38 or later for Claude for Teams, or version 2.1.30 or later for Claude for Enterprise
  * Network access to `api.anthropic.com`


## 
[​](https://code.claude.com/docs/en/server-managed-settings#choose-between-server-managed-and-endpoint-managed-settings)
Choose between server-managed and endpoint-managed settings
Claude Code supports two approaches for centralized configuration. Server-managed settings deliver configuration from Anthropic’s servers. [Endpoint-managed settings](https://code.claude.com/docs/en/settings#settings-files) are deployed directly to devices through native OS policies (macOS managed preferences, Windows registry) or managed settings files.  
| Approach  | Best for  | Security model  |  
| --- | --- | --- |  
| **Server-managed settings**  | Organizations without MDM, or users on unmanaged devices  | Settings delivered from Anthropic’s servers at authentication time  |  
| **[Endpoint-managed settings](https://code.claude.com/docs/en/settings#settings-files)**  | Organizations with MDM or endpoint management  | Settings deployed to devices via MDM configuration profiles, registry policies, or managed settings files  |  
If your devices are enrolled in an MDM or endpoint management solution, endpoint-managed settings provide stronger security guarantees because the settings file can be protected from user modification at the OS level.
## 
[​](https://code.claude.com/docs/en/server-managed-settings#configure-server-managed-settings)
Configure server-managed settings
1
[](https://code.claude.com/docs/en/server-managed-settings)
Open the admin console
In [Claude.ai](https://claude.ai), navigate to **Admin Settings > Claude Code > Managed settings**.
2
[](https://code.claude.com/docs/en/server-managed-settings)
Define your settings
Add your configuration as JSON. All [settings available in `settings.json`](https://code.claude.com/docs/en/settings#available-settings) are supported, including [hooks](https://code.claude.com/docs/en/hooks), [environment variables](https://code.claude.com/docs/en/env-vars), and [managed-only settings](https://code.claude.com/docs/en/permissions#managed-only-settings) like `allowManagedPermissionRulesOnly`.This example enforces a permission deny list, prevents users from bypassing permissions, and restricts permission rules to those defined in managed settings:

```
{
  "permissions": {
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ],
    "disableBypassPermissionsMode": "disable"
  },
  "allowManagedPermissionRulesOnly": true
}

```

Hooks use the same format as in `settings.json`.This example runs an audit script after every file edit across the organization:

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "/usr/local/bin/audit-edit.sh" }
        ]
      }
    ]
  }
}

```

To configure the [auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) classifier so it knows which repos, buckets, and domains your organization trusts:

```
{
  "autoMode": {
    "environment": [
      "Source control: github.example.com/acme-corp and all repos under it",
      "Trusted cloud buckets: s3://acme-build-artifacts, gs://acme-ml-datasets",
      "Trusted internal domains: *.corp.example.com"
    ]
  }
}

```

Because hooks execute shell commands, users see a [security approval dialog](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs) before they’re applied. See [Configure auto mode](https://code.claude.com/docs/en/auto-mode-config) for how the `autoMode` entries affect what the classifier blocks and important warnings about the `allow` and `soft_deny` fields.
3
[](https://code.claude.com/docs/en/server-managed-settings)
Save and deploy
Save your changes. Claude Code clients receive the updated settings on their next startup or hourly polling cycle.
### 
[​](https://code.claude.com/docs/en/server-managed-settings#verify-settings-delivery)
Verify settings delivery
To confirm that settings are being applied, ask a user to restart Claude Code. If the configuration includes settings that trigger the [security approval dialog](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs), the user sees a prompt describing the managed settings on startup. You can also verify that managed permission rules are active by having a user run `/permissions` to view their effective permission rules.
### 
[​](https://code.claude.com/docs/en/server-managed-settings#access-control)
Access control
The following roles can manage server-managed settings:
  * **Primary Owner**
  * **Owner**

Restrict access to trusted personnel, as settings changes apply to all users in the organization.
### 
[​](https://code.claude.com/docs/en/server-managed-settings#managed-only-settings)
Managed-only settings
Most [settings keys](https://code.claude.com/docs/en/settings#available-settings) work in any scope. A handful of keys are only read from managed settings and have no effect when placed in user or project settings files. See [managed-only settings](https://code.claude.com/docs/en/permissions#managed-only-settings) for the full list. Any setting not on that list can still be placed in managed settings and takes the highest precedence.
### 
[​](https://code.claude.com/docs/en/server-managed-settings#current-limitations)
Current limitations
Server-managed settings have the following limitations:
  * Settings apply uniformly to all users in the organization. Per-group configurations are not yet supported.
  * [MCP server configurations](https://code.claude.com/docs/en/mcp#managed-mcp-configuration) cannot be distributed through server-managed settings.


## 
[​](https://code.claude.com/docs/en/server-managed-settings#settings-delivery)
Settings delivery
### 
[​](https://code.claude.com/docs/en/server-managed-settings#settings-precedence)
Settings precedence
Server-managed settings and [endpoint-managed settings](https://code.claude.com/docs/en/settings#settings-files) both occupy the highest tier in the Claude Code [settings hierarchy](https://code.claude.com/docs/en/settings#settings-precedence). No other settings level can override them, including command line arguments. Within the managed tier, the first source that delivers a non-empty configuration wins. Server-managed settings are checked first, then endpoint-managed settings. Sources do not merge: if server-managed settings deliver any keys at all, endpoint-managed settings are ignored entirely. If server-managed settings deliver nothing, endpoint-managed settings apply. If you clear your server-managed configuration in the admin console with the intent of falling back to an endpoint-managed plist or registry policy, be aware that [cached settings](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior) persist on client machines until the next successful fetch. Run `/status` to see which managed source is active.
### 
[​](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
Fetch and caching behavior
Claude Code fetches settings from Anthropic’s servers at startup and polls for updates hourly during active sessions. **First launch without cached settings:**
  * Claude Code fetches settings asynchronously
  * If the fetch fails, Claude Code continues without managed settings
  * There is a brief window before settings load where restrictions are not yet enforced

**Subsequent launches with cached settings:**
  * Cached settings apply immediately at startup
  * Claude Code fetches fresh settings in the background
  * Cached settings persist through network failures

Claude Code applies settings updates automatically without a restart, except for advanced settings like OpenTelemetry configuration, which require a full restart to take effect.
### 
[​](https://code.claude.com/docs/en/server-managed-settings#enforce-fail-closed-startup)
Enforce fail-closed startup
By default, if the remote settings fetch fails at startup, the CLI continues without managed settings. For environments where this brief unenforced window is unacceptable, set `forceRemoteSettingsRefresh: true` in your managed settings. When this setting is active, the CLI blocks at startup until remote settings are freshly fetched. If the fetch fails, the CLI exits rather than proceeding without the policy. This setting self-perpetuates: once delivered from the server, it is also cached locally so that subsequent startups enforce the same behavior even before the first successful fetch of a new session. To enable this, add the key to your managed settings configuration:

```
{
  "forceRemoteSettingsRefresh": true
}

```

Before enabling this setting, ensure your network policies allow connectivity to `api.anthropic.com`. If that endpoint is unreachable, the CLI exits at startup and users cannot start Claude Code.
### 
[​](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)
Security approval dialogs
Certain settings that could pose security risks require explicit user approval before being applied:
  * **Shell command settings** : settings that execute shell commands
  * **Custom environment variables** : variables not in the known safe allowlist
  * **Hook configurations** : any hook definition

When these settings are present, users see a security dialog explaining what is being configured. Users must approve to proceed. If a user rejects the settings, Claude Code exits.
In non-interactive mode with the `-p` flag, Claude Code skips security dialogs and applies settings without user approval.
## 
[​](https://code.claude.com/docs/en/server-managed-settings#platform-availability)
Platform availability
Server-managed settings require a direct connection to `api.anthropic.com` and are not available when using third-party model providers:
  * Amazon Bedrock
  * Google Vertex AI
  * Microsoft Foundry
  * Custom API endpoints via `ANTHROPIC_BASE_URL` or [LLM gateways](https://code.claude.com/docs/en/llm-gateway)


## 
[​](https://code.claude.com/docs/en/server-managed-settings#audit-logging)
Audit logging
Audit log events for settings changes are available through the compliance API or audit log export. Contact your Anthropic account team for access. Audit events include the type of action performed, the account and device that performed the action, and references to the previous and new values.
## 
[​](https://code.claude.com/docs/en/server-managed-settings#security-considerations)
Security considerations
Server-managed settings provide centralized policy enforcement, but they operate as a client-side control. On unmanaged devices, users with admin or sudo access can modify the Claude Code binary, filesystem, or network configuration.  
| Scenario  | Behavior  |  
| --- | --- |  
| User edits the cached settings file  | Tampered file applies at startup, but correct settings restore on the next server fetch  |  
| User deletes the cached settings file  | First-launch behavior occurs: settings fetch asynchronously with a brief unenforced window  |  
| API is unavailable  | Cached settings apply if available, otherwise managed settings are not enforced until the next successful fetch. With `forceRemoteSettingsRefresh: true`, the CLI exits instead of continuing  |  
| User authenticates with a different organization  | Settings are not delivered for accounts outside the managed organization  |  
| User configures a [third-party model provider](https://code.claude.com/docs/en/server-managed-settings#platform-availability)  | Server-managed settings are bypassed. This includes setting `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_MANTLE`, `CLAUDE_CODE_USE_VERTEX`, `CLAUDE_CODE_USE_FOUNDRY`, or a non-default `ANTHROPIC_BASE_URL`  |  
To detect runtime configuration changes, use [`ConfigChange` hooks](https://code.claude.com/docs/en/hooks#configchange) to log modifications or block unauthorized changes before they take effect. For stronger enforcement guarantees, use [endpoint-managed settings](https://code.claude.com/docs/en/settings#settings-files) on devices enrolled in an MDM solution.
## 
[​](https://code.claude.com/docs/en/server-managed-settings#see-also)
See also
Related pages for managing Claude Code configuration:
  * [Settings](https://code.claude.com/docs/en/settings): complete configuration reference including all available settings
  * [Endpoint-managed settings](https://code.claude.com/docs/en/settings#settings-files): managed settings deployed to devices by IT
  * [Authentication](https://code.claude.com/docs/en/authentication): set up user access to Claude Code
  * [Security](https://code.claude.com/docs/en/security): security safeguards and best practices


Was this page helpful?
YesNo
[Authentication](https://code.claude.com/docs/en/authentication)[Auto mode](https://code.claude.com/docs/en/auto-mode-config)
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
[Privacy choices](https://code.claude.com/docs/en/server-managed-settings)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
