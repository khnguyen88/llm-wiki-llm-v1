<!--
url: https://code.claude.com/docs/en/network-config
download_date: 2026-04-29
website: claude-code
webpage: network-config
-->

# Network Config

[Skip to main content](https://code.claude.com/docs/en/network-config#content-area)
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
Deployment
Enterprise network configuration
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
  * [Proxy configuration](https://code.claude.com/docs/en/network-config#proxy-configuration)
  * [Environment variables](https://code.claude.com/docs/en/network-config#environment-variables)
  * [Basic authentication](https://code.claude.com/docs/en/network-config#basic-authentication)
  * [CA certificate store](https://code.claude.com/docs/en/network-config#ca-certificate-store)
  * [Custom CA certificates](https://code.claude.com/docs/en/network-config#custom-ca-certificates)
  * [mTLS authentication](https://code.claude.com/docs/en/network-config#mtls-authentication)
  * [Network access requirements](https://code.claude.com/docs/en/network-config#network-access-requirements)
  * [Additional resources](https://code.claude.com/docs/en/network-config#additional-resources)


Deployment
# Enterprise network configuration
Copy page
Configure Claude Code for enterprise environments with proxy servers, custom Certificate Authorities (CA), and mutual Transport Layer Security (mTLS) authentication.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Claude Code supports various enterprise network and security configurations through environment variables. This includes routing traffic through corporate proxy servers, trusting custom Certificate Authorities (CA), and authenticating with mutual Transport Layer Security (mTLS) certificates for enhanced security.
All environment variables shown on this page can also be configured in [`settings.json`](https://code.claude.com/docs/en/settings).
## 
[​](https://code.claude.com/docs/en/network-config#proxy-configuration)
Proxy configuration
### 
[​](https://code.claude.com/docs/en/network-config#environment-variables)
Environment variables
Claude Code respects standard proxy environment variables:

```
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for specific requests - space-separated format
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# Bypass proxy for specific requests - comma-separated format
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# Bypass proxy for all requests
export NO_PROXY="*"

```

Claude Code does not support SOCKS proxies.
### 
[​](https://code.claude.com/docs/en/network-config#basic-authentication)
Basic authentication
If your proxy requires basic authentication, include credentials in the proxy URL:

```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080

```

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.
For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.
## 
[​](https://code.claude.com/docs/en/network-config#ca-certificate-store)
CA certificate store
By default, Claude Code trusts both its bundled Mozilla CA certificates and your operating system’s certificate store. Enterprise TLS-inspection proxies such as CrowdStrike Falcon and Zscaler work without additional configuration when their root certificate is installed in the OS trust store.
System CA store integration requires the native Claude Code binary distribution. When running on the Node.js runtime, the system CA store is not merged automatically. In that case, set `NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem` to trust an enterprise root CA.
`CLAUDE_CODE_CERT_STORE` accepts a comma-separated list of sources. Recognized values are `bundled` for the Mozilla CA set shipped with Claude Code and `system` for the operating system trust store. The default is `bundled,system`. To trust only the bundled Mozilla CA set:

```
export CLAUDE_CODE_CERT_STORE=bundled

```

To trust only the OS certificate store:

```
export CLAUDE_CODE_CERT_STORE=system

```

`CLAUDE_CODE_CERT_STORE` has no dedicated `settings.json` schema key. Set it via the `env` block in `~/.claude/settings.json` or directly in the process environment.
## 
[​](https://code.claude.com/docs/en/network-config#custom-ca-certificates)
Custom CA certificates
If your enterprise environment uses a custom CA, configure Claude Code to trust it directly:

```
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem

```

## 
[​](https://code.claude.com/docs/en/network-config#mtls-authentication)
mTLS authentication
For enterprise environments requiring client certificate authentication:

```
# Client certificate for authentication
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# Client private key
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# Optional: Passphrase for encrypted private key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"

```

## 
[​](https://code.claude.com/docs/en/network-config#network-access-requirements)
Network access requirements
Claude Code requires access to the following URLs. Allowlist these in your proxy configuration and firewall rules, especially in containerized or restricted network environments.  
| URL  | Required for  |  
| --- | --- |  
| `api.anthropic.com`  | Claude API requests  |  
| `claude.ai`  | claude.ai account authentication  |  
| `platform.claude.com`  | Anthropic Console account authentication  |  
| `downloads.claude.ai`  | Plugin executable downloads; native installer and native auto-updater  |  
| `storage.googleapis.com`  | Native installer and native auto-updater on versions prior to 2.1.116  |  
| `bridge.claudeusercontent.com`  |  [Claude in Chrome](https://code.claude.com/docs/en/chrome) extension WebSocket bridge  |  
If you install Claude Code through npm or manage your own binary distribution, end users may not need access to `downloads.claude.ai` or `storage.googleapis.com`. Claude Code also sends optional operational telemetry by default, which you can disable with environment variables. See [Telemetry services](https://code.claude.com/docs/en/data-usage#telemetry-services) for how to disable it before finalizing your allowlist. When using [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai), or [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry), model traffic and authentication go to your provider instead of `api.anthropic.com`, `claude.ai`, or `platform.claude.com`. The WebFetch tool still calls `api.anthropic.com` for its [domain safety check](https://code.claude.com/docs/en/data-usage#webfetch-domain-safety-check) unless you set `skipWebFetchPreflight: true` in [settings](https://code.claude.com/docs/en/settings). [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) and [Code Review](https://code.claude.com/docs/en/code-review) connect to your repositories from Anthropic-managed infrastructure. If your GitHub Enterprise Cloud organization restricts access by IP address, enable [IP allow list inheritance for installed GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps). The Claude GitHub App registers its IP ranges, so enabling this setting allows access without manual configuration. To [add the ranges to your allow list manually](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#adding-an-allowed-ip-address) instead, or to configure other firewalls, see the [Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses). For self-hosted [GitHub Enterprise Server](https://code.claude.com/docs/en/github-enterprise-server) instances behind a firewall, allowlist the same [Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses) so Anthropic infrastructure can reach your GHES host to clone repositories and post review comments.
## 
[​](https://code.claude.com/docs/en/network-config#additional-resources)
Additional resources
  * [Claude Code settings](https://code.claude.com/docs/en/settings)
  * [Environment variables reference](https://code.claude.com/docs/en/env-vars)
  * [Troubleshooting guide](https://code.claude.com/docs/en/troubleshooting)


Was this page helpful?
YesNo
[Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry)[LLM gateway](https://code.claude.com/docs/en/llm-gateway)
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
[Privacy choices](https://code.claude.com/docs/en/network-config)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
