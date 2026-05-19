<!--
url: https://code.claude.com/docs/en/zero-data-retention
download_date: 2026-04-29
website: claude-code
webpage: zero-data-retention
-->

# Zero Data Retention

[Skip to main content](https://code.claude.com/docs/en/zero-data-retention#content-area)
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
Security and data
Zero data retention
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
  * [ZDR scope](https://code.claude.com/docs/en/zero-data-retention#zdr-scope)
  * [What ZDR covers](https://code.claude.com/docs/en/zero-data-retention#what-zdr-covers)
  * [What ZDR does not cover](https://code.claude.com/docs/en/zero-data-retention#what-zdr-does-not-cover)
  * [Features disabled under ZDR](https://code.claude.com/docs/en/zero-data-retention#features-disabled-under-zdr)
  * [Data retention for policy violations](https://code.claude.com/docs/en/zero-data-retention#data-retention-for-policy-violations)
  * [Request ZDR](https://code.claude.com/docs/en/zero-data-retention#request-zdr)


Security and data
# Zero data retention
Copy page
Learn about Zero Data Retention (ZDR) for Claude Code on Claude for Enterprise, including scope, disabled features, and how to request enablement.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Zero Data Retention (ZDR) is available for Claude Code when used through Claude for Enterprise. When ZDR is enabled, prompts and model responses generated during Claude Code sessions are processed in real time and not stored by Anthropic after the response is returned, except where needed to comply with law or combat misuse. ZDR on Claude for Enterprise gives enterprise customers the ability to use Claude Code with zero data retention and access administrative capabilities:
  * Cost controls per user
  * [Analytics](https://code.claude.com/docs/en/analytics) dashboard
  * [Server-managed settings](https://code.claude.com/docs/en/server-managed-settings)
  * Audit logs

ZDR for Claude Code on Claude for Enterprise applies only to Anthropic’s direct platform. For Claude deployments on AWS Bedrock, Google Vertex AI, or Microsoft Foundry, refer to those platforms’ data retention policies.
## 
[​](https://code.claude.com/docs/en/zero-data-retention#zdr-scope)
ZDR scope
ZDR covers Claude Code inference on Claude for Enterprise.
ZDR is enabled on a per-organization basis. Each new organization requires ZDR to be enabled separately by your Anthropic account team. ZDR does not automatically apply to new organizations created under the same account. Contact your account team to enable ZDR for any new organizations.
### 
[​](https://code.claude.com/docs/en/zero-data-retention#what-zdr-covers)
What ZDR covers
ZDR covers model inference calls made through Claude Code on Claude for Enterprise. When you use Claude Code in your terminal, the prompts you send and the responses Claude generates are not retained by Anthropic. This applies regardless of which Claude model is used.
### 
[​](https://code.claude.com/docs/en/zero-data-retention#what-zdr-does-not-cover)
What ZDR does not cover
ZDR does not extend to the following, even for organizations with ZDR enabled. These features follow [standard data retention policies](https://code.claude.com/docs/en/data-usage#data-retention):  
| Feature  | Details  |  
| --- | --- |  
| Chat on claude.ai  | Chat conversations through the Claude for Enterprise web interface are not covered by ZDR.  |  
| Cowork  | Cowork sessions are not covered by ZDR.  |  
| Claude Code Analytics  | Does not store prompts or model responses, but collects productivity metadata such as account emails and usage statistics. Contribution metrics are not available for ZDR organizations; the [analytics dashboard](https://code.claude.com/docs/en/analytics) shows usage metrics only.  |  
| User and seat management  | Administrative data such as account emails and seat assignments is retained under standard policies.  |  
| Third-party integrations  | Data processed by third-party tools, MCP servers, or other external integrations is not covered by ZDR. Review those services’ data handling practices independently.  |  
## 
[​](https://code.claude.com/docs/en/zero-data-retention#features-disabled-under-zdr)
Features disabled under ZDR
When ZDR is enabled for a Claude Code organization on Claude for Enterprise, certain features that require storing prompts or completions are automatically disabled at the backend level:  
| Feature  | Reason  |  
| --- | --- |  
| [Claude Code on the Web](https://code.claude.com/docs/en/claude-code-on-the-web)  | Requires server-side storage of conversation history.  |  
|  [Remote sessions](https://code.claude.com/docs/en/desktop#remote-sessions) from the Desktop app  | Requires persistent session data that includes prompts and completions.  |  
| Feedback submission (`/feedback`)  | Submitting feedback sends conversation data to Anthropic.  |  
These features are blocked in the backend regardless of client-side display. If you see a disabled feature in the Claude Code terminal during startup, attempting to use it returns an error indicating the organization’s policies do not allow that action. Future features may also be disabled if they require storing prompts or completions.
## 
[​](https://code.claude.com/docs/en/zero-data-retention#data-retention-for-policy-violations)
Data retention for policy violations
Even with ZDR enabled, Anthropic may retain data where required by law or to address Usage Policy violations. If a session is flagged for a policy violation, Anthropic may retain the associated inputs and outputs for up to 2 years, consistent with Anthropic’s standard ZDR policy.
## 
[​](https://code.claude.com/docs/en/zero-data-retention#request-zdr)
Request ZDR
To request ZDR for Claude Code on Claude for Enterprise, [contact sales](https://www.anthropic.com/contact-sales?utm_source=claude_code&utm_medium=docs&utm_content=zero_data_retention_request) or your Anthropic account team. Your account team will submit the request internally, and Anthropic will review and enable ZDR on your organization after confirming eligibility. All enablement actions are audit-logged. If you are currently using ZDR for Claude Code via pay-as-you-go API keys, you can transition to Claude for Enterprise to gain access to administrative features while maintaining ZDR for Claude Code. Contact your account team to coordinate the migration.
Was this page helpful?
YesNo
[Data usage](https://code.claude.com/docs/en/data-usage)[Communications kit](https://code.claude.com/docs/en/communications-kit)
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
[Privacy choices](https://code.claude.com/docs/en/zero-data-retention)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
