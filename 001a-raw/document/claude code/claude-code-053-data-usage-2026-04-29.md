<!--
url: https://code.claude.com/docs/en/data-usage
download_date: 2026-04-29
website: claude-code
webpage: data-usage
-->

# Data Usage

[Skip to main content](https://code.claude.com/docs/en/data-usage#content-area)
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
Data usage
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
  * [Data policies](https://code.claude.com/docs/en/data-usage#data-policies)
  * [Data training policy](https://code.claude.com/docs/en/data-usage#data-training-policy)
  * [Development Partner Program](https://code.claude.com/docs/en/data-usage#development-partner-program)
  * [Feedback using the /feedback command](https://code.claude.com/docs/en/data-usage#feedback-using-the-%2Ffeedback-command)
  * [Session quality surveys](https://code.claude.com/docs/en/data-usage#session-quality-surveys)
  * [Data retention](https://code.claude.com/docs/en/data-usage#data-retention)
  * [Data access](https://code.claude.com/docs/en/data-usage#data-access)
  * [Local Claude Code: Data flow and dependencies](https://code.claude.com/docs/en/data-usage#local-claude-code-data-flow-and-dependencies)
  * [Cloud execution: Data flow and dependencies](https://code.claude.com/docs/en/data-usage#cloud-execution-data-flow-and-dependencies)
  * [Telemetry services](https://code.claude.com/docs/en/data-usage#telemetry-services)
  * [Default behaviors by API provider](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)
  * [WebFetch domain safety check](https://code.claude.com/docs/en/data-usage#webfetch-domain-safety-check)


Security and data
# Data usage
Copy page
Learn about Anthropic’s data usage policies for Claude
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
## 
[​](https://code.claude.com/docs/en/data-usage#data-policies)
Data policies
### 
[​](https://code.claude.com/docs/en/data-usage#data-training-policy)
Data training policy
**Consumer users (Free, Pro, and Max plans)** : We give you the choice to allow your data to be used to improve future Claude models. We will train new models using data from Free, Pro, and Max accounts when this setting is on (including when you use Claude Code from these accounts). **Commercial users** : (Team and Enterprise plans, API, 3rd-party platforms, and Claude Gov) maintain existing policies: Anthropic does not train generative models using code or prompts sent to Claude Code under commercial terms, unless the customer has chosen to provide their data to us for model improvement (for example, the [Developer Partner Program](https://support.claude.com/en/articles/11174108-about-the-development-partner-program)).
### 
[​](https://code.claude.com/docs/en/data-usage#development-partner-program)
Development Partner Program
If you explicitly opt in to methods to provide us with materials to train on, such as via the [Development Partner Program](https://support.claude.com/en/articles/11174108-about-the-development-partner-program), we may use those materials provided to train our models. An organization admin can expressly opt-in to the Development Partner Program for their organization. Note that this program is available only for Anthropic first-party API, and not for Bedrock or Vertex users.
### 
[​](https://code.claude.com/docs/en/data-usage#feedback-using-the-/feedback-command)
Feedback using the `/feedback` command
If you choose to send us feedback about Claude Code using the `/feedback` command, we may use your feedback to improve our products and services. Transcripts shared via `/feedback` are retained for 5 years.
### 
[​](https://code.claude.com/docs/en/data-usage#session-quality-surveys)
Session quality surveys
When you see the “How is Claude doing this session?” prompt in Claude Code, responding to this survey, including selecting “Dismiss”, records only your rating. We do not collect or store any conversation transcripts, inputs, outputs, or other session data as part of the rating prompt itself. Unlike thumbs up/down feedback or `/feedback` reports, this session quality survey is a simple product satisfaction metric. After the rating prompt, you may see a separate follow-up asking “Can Anthropic look at your session transcript to help us improve Claude Code?”. This is an optional second step distinct from the rating:
  * **Yes** : uploads your conversation transcript, any subagent transcripts, and the raw session log file from disk to Anthropic. Known API key and token patterns are redacted before upload. Source code, file contents, and other conversation content are uploaded as-is. Shared transcripts are retained for up to 6 months.
  * **No** : declines without sending anything
  * **Don’t ask again** : declines and stops this follow-up from appearing in future sessions

Nothing is uploaded unless you explicitly select **Yes**. Organizations with [zero data retention](https://code.claude.com/docs/en/zero-data-retention), or where product feedback is disabled by organization policy, never see this follow-up. Your responses to this survey, including session transcripts submitted after the rating prompt, do not impact your data training preferences and cannot be used to train our AI models. To disable these surveys, set `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1`. The survey is also disabled when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set. To control frequency instead of disabling, set [`feedbackSurveyRate`](https://code.claude.com/docs/en/settings#available-settings) in your settings file to a probability between `0` and `1`.
### 
[​](https://code.claude.com/docs/en/data-usage#data-retention)
Data retention
Anthropic retains Claude Code data based on your account type and preferences. **Consumer users (Free, Pro, and Max plans)** :
  * Users who allow data use for model improvement: 5-year retention period to support model development and safety improvements
  * Users who don’t allow data use for model improvement: 30-day retention period
  * Privacy settings can be changed at any time at [claude.ai/settings/data-privacy-controls](https://claude.ai/settings/data-privacy-controls).

**Commercial users (Team, Enterprise, and API)** :
  * Standard: 30-day retention period
  * [Zero data retention](https://code.claude.com/docs/en/zero-data-retention): available for Claude Code on Claude for Enterprise. ZDR is enabled on a per-organization basis; each new organization must have ZDR enabled separately by your account team
  * Local caching: Claude Code clients store session transcripts locally in plaintext under `~/.claude/projects/` for 30 days by default to enable session resumption. Adjust the period with `cleanupPeriodDays`. See [application data](https://code.claude.com/docs/en/claude-directory#application-data) for what’s stored and how to clear it.

You can delete individual Claude Code on the web sessions at any time. Deleting a session permanently removes the session’s event data. For instructions on how to delete sessions, see [Delete sessions](https://code.claude.com/docs/en/claude-code-on-the-web#delete-sessions). Learn more about data retention practices in our [Privacy Center](https://privacy.anthropic.com/). For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) (for Team, Enterprise, and API users) or [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (for Free, Pro, and Max users) and [Privacy Policy](https://www.anthropic.com/legal/privacy).
## 
[​](https://code.claude.com/docs/en/data-usage#data-access)
Data access
For all first party users, you can learn more about what data is logged for [local Claude Code](https://code.claude.com/docs/en/data-usage#local-claude-code-data-flow-and-dependencies) and [remote Claude Code](https://code.claude.com/docs/en/data-usage#cloud-execution-data-flow-and-dependencies). [Remote Control](https://code.claude.com/docs/en/remote-control) sessions follow the local data flow since all execution happens on your machine. Note for remote Claude Code, Claude accesses the repository where you initiate your Claude Code session. Claude does not access repositories that you have connected but have not started a session in.
## 
[​](https://code.claude.com/docs/en/data-usage#local-claude-code-data-flow-and-dependencies)
Local Claude Code: Data flow and dependencies
The diagram below shows how Claude Code connects to external services during installation and normal operation. Solid lines indicate required connections, while dashed lines represent optional or user-initiated data flows. ![Diagram showing Claude Code's external connections: install/update connects to the distribution server, and user requests connect to Anthropic services including Console auth, public-api, and optionally Statsig, Sentry, and bug reporting](https://mintcdn.com/claude-code/YcBW2H7CArGcduPb/images/claude-code-data-flow.svg?fit=max&auto=format&n=YcBW2H7CArGcduPb&q=85&s=b600a89f84fc86f9ff7be00a466c0635) Claude Code runs locally. To interact with the LLM, Claude Code sends data over the network. This data includes all user prompts and model outputs, encrypted in transit via TLS 1.2+. Claude Code is compatible with most popular VPNs and LLM proxies. Encryption at rest depends on your model provider:  
| Provider  | Encryption at rest  |  
| --- | --- |  
| Anthropic API  | Infrastructure-level disk encryption (AES-256). Enable [Zero Data Retention](https://code.claude.com/docs/en/zero-data-retention) for no server-side persistence.  |  
| Amazon Bedrock  | AES-256 with AWS-managed keys. Customer-managed keys available via AWS KMS.  |  
| Google Cloud Vertex AI  | Google-managed encryption keys. CMEK available.  |  
| Microsoft Foundry  | Requests route to Anthropic infrastructure with AES-256 disk encryption.  |  
Claude Code is built on Anthropic’s APIs. For details on API security controls, including API logging procedures, see the compliance artifacts in the [Anthropic Trust Center](https://trust.anthropic.com).
### 
[​](https://code.claude.com/docs/en/data-usage#cloud-execution-data-flow-and-dependencies)
Cloud execution: Data flow and dependencies
When using [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web), sessions run in Anthropic-managed virtual machines instead of locally. In cloud environments:
  * **Code and data storage:** Your repository is cloned to an isolated VM. Code and session data are subject to the retention and usage policies for your account type (see Data retention section above)
  * **Credentials:** GitHub authentication is handled through a secure proxy; your GitHub credentials never enter the sandbox
  * **Network traffic:** All outbound traffic goes through a security proxy for audit logging and abuse prevention
  * **Session data:** Prompts, code changes, and outputs follow the same data policies as local Claude Code usage

For security details about cloud execution, see [Security](https://code.claude.com/docs/en/security#cloud-execution-security).
## 
[​](https://code.claude.com/docs/en/data-usage#telemetry-services)
Telemetry services
Claude Code connects from users’ machines to the Statsig service to log operational metrics such as latency, reliability, and usage patterns. This logging does not include any code or file paths. Data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Statsig security documentation](https://www.statsig.com/trust/security). To opt out of Statsig telemetry, set the `DISABLE_TELEMETRY` environment variable. Claude Code connects from users’ machines to Sentry for operational error logging. The data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Sentry security documentation](https://sentry.io/security/). To opt out of error logging, set the `DISABLE_ERROR_REPORTING` environment variable. When users run the `/feedback` command, a copy of their full conversation history including code is sent to Anthropic. The data is encrypted in transit via TLS. Optionally, a GitHub issue is created in the public repository. To opt out, set the `DISABLE_FEEDBACK_COMMAND` environment variable to `1`.
## 
[​](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)
Default behaviors by API provider
By default, error reporting, telemetry, and bug reporting are disabled when using Bedrock, Vertex, or Foundry. Session quality surveys and the WebFetch domain safety check are exceptions and run regardless of provider. You can opt out of all non-essential traffic, including surveys, at once by setting `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. This variable does not affect the WebFetch check, which has its own opt-out. Here are the full default behaviors:  
| Service  | Claude API  | Vertex API  | Bedrock API  | Foundry API  |  
| --- | --- | --- | --- | --- |  
| **Statsig (Metrics)**  | Default on.  
`DISABLE_TELEMETRY=1` to disable.  | Default off.  
`CLAUDE_CODE_USE_VERTEX` must be 1.  | Default off.  
`CLAUDE_CODE_USE_BEDROCK` must be 1.  | Default off.  
`CLAUDE_CODE_USE_FOUNDRY` must be 1.  |  
| **Sentry (Errors)**  | Default on.  
`DISABLE_ERROR_REPORTING=1` to disable.  | Default off.  
`CLAUDE_CODE_USE_VERTEX` must be 1.  | Default off.  
`CLAUDE_CODE_USE_BEDROCK` must be 1.  | Default off.  
`CLAUDE_CODE_USE_FOUNDRY` must be 1.  |  
| **Claude API (`/feedback` reports)**  | Default on.  
`DISABLE_FEEDBACK_COMMAND=1` to disable.  | Default off.  
`CLAUDE_CODE_USE_VERTEX` must be 1.  | Default off.  
`CLAUDE_CODE_USE_BEDROCK` must be 1.  | Default off.  
`CLAUDE_CODE_USE_FOUNDRY` must be 1.  |  
| **Session quality surveys**  | Default on.  
`CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` to disable.  | Default on.  
`CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` to disable.  | Default on.  
`CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` to disable.  | Default on.  
`CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1` to disable.  |  
| **WebFetch domain safety check**  | Default on.  
`skipWebFetchPreflight: true` in [settings](https://code.claude.com/docs/en/settings) to disable.  | Default on.  
`skipWebFetchPreflight: true` in [settings](https://code.claude.com/docs/en/settings) to disable.  | Default on.  
`skipWebFetchPreflight: true` in [settings](https://code.claude.com/docs/en/settings) to disable.  | Default on.  
`skipWebFetchPreflight: true` in [settings](https://code.claude.com/docs/en/settings) to disable.  |  
All environment variables can be checked into `settings.json` (see [settings reference](https://code.claude.com/docs/en/settings)).
### 
[​](https://code.claude.com/docs/en/data-usage#webfetch-domain-safety-check)
WebFetch domain safety check
Before fetching a URL, the WebFetch tool sends the requested hostname to `api.anthropic.com` to check it against a safety blocklist maintained by Anthropic. Only the hostname is sent, not the full URL, path, or page contents. Results are cached per hostname for five minutes. This check runs regardless of which model provider you use and is not affected by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. If your network blocks `api.anthropic.com`, WebFetch requests fail until you either allowlist the domain or set `skipWebFetchPreflight: true` in [settings](https://code.claude.com/docs/en/settings). Disabling the check means WebFetch attempts to retrieve any URL without consulting the blocklist, so combine it with [`WebFetch` permission rules](https://code.claude.com/docs/en/permissions#webfetch) if you need to restrict which domains Claude can reach.
Was this page helpful?
YesNo
[Security](https://code.claude.com/docs/en/security)[Zero data retention](https://code.claude.com/docs/en/zero-data-retention)
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
[Privacy choices](https://code.claude.com/docs/en/data-usage)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
