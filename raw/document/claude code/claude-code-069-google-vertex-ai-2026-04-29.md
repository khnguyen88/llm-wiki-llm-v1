<!--
url: https://code.claude.com/docs/en/google-vertex-ai
download_date: 2026-04-29
website: claude-code
webpage: google-vertex-ai
-->

# Google Vertex Ai

[Skip to main content](https://code.claude.com/docs/en/google-vertex-ai#content-area)
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
Claude Code on Google Vertex AI
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
  * [Prerequisites](https://code.claude.com/docs/en/google-vertex-ai#prerequisites)
  * [Sign in with Vertex AI](https://code.claude.com/docs/en/google-vertex-ai#sign-in-with-vertex-ai)
  * [Region configuration](https://code.claude.com/docs/en/google-vertex-ai#region-configuration)
  * [Set up manually](https://code.claude.com/docs/en/google-vertex-ai#set-up-manually)
  * [1. Enable Vertex AI API](https://code.claude.com/docs/en/google-vertex-ai#1-enable-vertex-ai-api)
  * [2. Request model access](https://code.claude.com/docs/en/google-vertex-ai#2-request-model-access)
  * [3. Configure GCP credentials](https://code.claude.com/docs/en/google-vertex-ai#3-configure-gcp-credentials)
  * [4. Configure Claude Code](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)
  * [5. Pin model versions](https://code.claude.com/docs/en/google-vertex-ai#5-pin-model-versions)
  * [Startup model checks](https://code.claude.com/docs/en/google-vertex-ai#startup-model-checks)
  * [IAM configuration](https://code.claude.com/docs/en/google-vertex-ai#iam-configuration)
  * [1M token context window](https://code.claude.com/docs/en/google-vertex-ai#1m-token-context-window)
  * [Troubleshooting](https://code.claude.com/docs/en/google-vertex-ai#troubleshooting)
  * [Additional resources](https://code.claude.com/docs/en/google-vertex-ai#additional-resources)


Deployment
# Claude Code on Google Vertex AI
Copy page
Learn about configuring Claude Code through Google Vertex AI, including setup, IAM configuration, and troubleshooting.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
## 
[​](https://code.claude.com/docs/en/google-vertex-ai#prerequisites)
Prerequisites
Before configuring Claude Code with Vertex AI, ensure you have:
  * A Google Cloud Platform (GCP) account with billing enabled
  * A GCP project with Vertex AI API enabled
  * Access to desired Claude models (for example, Claude Sonnet 4.6)
  * Google Cloud SDK (`gcloud`) installed and configured
  * Quota allocated in desired GCP region

To sign in with your own Vertex AI credentials, follow [Sign in with Vertex AI](https://code.claude.com/docs/en/google-vertex-ai#sign-in-with-vertex-ai) below. To deploy Claude Code across a team, use the [manual setup](https://code.claude.com/docs/en/google-vertex-ai#set-up-manually) steps and [pin your model versions](https://code.claude.com/docs/en/google-vertex-ai#5-pin-model-versions) before rolling out.
## 
[​](https://code.claude.com/docs/en/google-vertex-ai#sign-in-with-vertex-ai)
Sign in with Vertex AI
If you have Google Cloud credentials and want to start using Claude Code through Vertex AI, the login wizard walks you through it. You complete the GCP-side prerequisites once per project; the wizard handles the Claude Code side.
The Vertex AI setup wizard requires Claude Code v2.1.98 or later. Run `claude --version` to check.
1
[](https://code.claude.com/docs/en/google-vertex-ai)
Enable Claude models in your GCP project
[Enable the Vertex AI API](https://code.claude.com/docs/en/google-vertex-ai#1-enable-vertex-ai-api) for your project, then request access to the Claude models you want in the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden). See [IAM configuration](https://code.claude.com/docs/en/google-vertex-ai#iam-configuration) for the permissions your account needs.
2
[](https://code.claude.com/docs/en/google-vertex-ai)
Start Claude Code and choose Vertex AI
Run `claude`. At the login prompt, select **3rd-party platform** , then **Google Vertex AI**.
3
[](https://code.claude.com/docs/en/google-vertex-ai)
Follow the wizard prompts
Choose how you authenticate to Google Cloud: Application Default Credentials from `gcloud`, a service account key file, or credentials already in your environment. The wizard detects your project and region, verifies which Claude models your project can invoke, and lets you pin them. It saves the result to the `env` block of your [user settings file](https://code.claude.com/docs/en/settings), so you don’t need to export environment variables yourself.
After you’ve signed in, run `/setup-vertex` any time to reopen the wizard and change your credentials, project, region, or model pins.
## 
[​](https://code.claude.com/docs/en/google-vertex-ai#region-configuration)
Region configuration
Claude Code supports Vertex AI [global](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai), multi-region, and regional endpoints. Set `CLOUD_ML_REGION` to `global`, a multi-region location such as `eu` or `us`, or a specific region such as `us-east5`. Claude Code selects the correct Vertex AI hostname for each form, including the `aiplatform.eu.rep.googleapis.com` and `aiplatform.us.rep.googleapis.com` hosts for multi-region locations.
Vertex AI may not support the Claude Code default models on every endpoint type. Model availability varies across [specific regions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#genai-partner-models), multi-region locations, and [global endpoints](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#supported_models). You may need to switch to a supported location or specify a supported model.
## 
[​](https://code.claude.com/docs/en/google-vertex-ai#set-up-manually)
Set up manually
To configure Vertex AI through environment variables instead of the wizard, for example in CI or a scripted enterprise rollout, follow the steps below.
### 
[​](https://code.claude.com/docs/en/google-vertex-ai#1-enable-vertex-ai-api)
1. Enable Vertex AI API
Enable the Vertex AI API in your GCP project:

```
# Set your project ID
gcloud config set project YOUR-PROJECT-ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com

```

### 
[​](https://code.claude.com/docs/en/google-vertex-ai#2-request-model-access)
2. Request model access
Request access to Claude models in Vertex AI:
  1. Navigate to the [Vertex AI Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
  2. Search for “Claude” models
  3. Request access to desired Claude models (for example, Claude Sonnet 4.6)
  4. Wait for approval (may take 24-48 hours)


### 
[​](https://code.claude.com/docs/en/google-vertex-ai#3-configure-gcp-credentials)
3. Configure GCP credentials
Claude Code uses standard Google Cloud authentication. For more information, see [Google Cloud authentication documentation](https://cloud.google.com/docs/authentication). Claude Code v2.1.121 or later supports [X.509 certificate-based Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates) through the same Application Default Credentials chain. Set `GOOGLE_APPLICATION_CREDENTIALS` to the path of your credential configuration file.
When authenticating, Claude Code will automatically use the project ID from the `ANTHROPIC_VERTEX_PROJECT_ID` environment variable. To override this, set one of these environment variables: `GCLOUD_PROJECT`, `GOOGLE_CLOUD_PROJECT`, or `GOOGLE_APPLICATION_CREDENTIALS`.
### 
[​](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)
4. Configure Claude Code
Set the following environment variables:

```
# Enable Vertex AI integration
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=global
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID

# Optional: Override the Vertex endpoint URL for custom endpoints or gateways
# export ANTHROPIC_VERTEX_BASE_URL=https://aiplatform.googleapis.com

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1

# Optional: Request 1-hour prompt cache TTL instead of the 5-minute default
export ENABLE_PROMPT_CACHING_1H=1

# When CLOUD_ML_REGION=global, override region for models that don't support global endpoints
export VERTEX_REGION_CLAUDE_HAIKU_4_5=us-east5
export VERTEX_REGION_CLAUDE_4_6_SONNET=europe-west1

```

Most model versions have a corresponding `VERTEX_REGION_CLAUDE_*` variable. See the [Environment variables reference](https://code.claude.com/docs/en/env-vars) for the full list. Check [Vertex Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) to determine which models support global endpoints versus regional only. [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) is enabled automatically. To disable it, set `DISABLE_PROMPT_CACHING=1`. To request a 1-hour cache TTL instead of the 5-minute default, set `ENABLE_PROMPT_CACHING_1H=1`; cache writes with a 1-hour TTL are billed at a higher rate. For heightened rate limits, contact Google Cloud support. When using Vertex AI, the `/login` and `/logout` commands are disabled since authentication is handled through Google Cloud credentials. [MCP tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) is disabled by default on Vertex AI because the endpoint does not accept the required beta header. All MCP tool definitions load upfront instead. To opt in, set `ENABLE_TOOL_SEARCH=true`.
### 
[​](https://code.claude.com/docs/en/google-vertex-ai#5-pin-model-versions)
5. Pin model versions
Pin specific model versions when deploying to multiple users. Without pinning, model aliases such as `sonnet` and `opus` resolve to the latest version, which may not yet be enabled in your Vertex AI project when Anthropic releases an update. Claude Code [falls back](https://code.claude.com/docs/en/google-vertex-ai#startup-model-checks) to the previous version at startup when the latest is unavailable, but pinning lets you control when your users move to a new model.
Set these environment variables to specific Vertex AI model IDs. Without `ANTHROPIC_DEFAULT_OPUS_MODEL`, the `opus` alias on Vertex resolves to Opus 4.6. Set it to the Opus 4.7 ID to use the latest model:

```
export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-7'
export ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-4-6'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5@20251001'

```

For current and legacy model IDs, see [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview). See [Model configuration](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments) for the full list of environment variables. Claude Code uses these default models when no pinning variables are set:  
| Model type  | Default value  |  
| --- | --- |  
| Primary model  | `claude-sonnet-4-5@20250929`  |  
| Small/fast model  | `claude-haiku-4-5@20251001`  |  
To customize models further:

```
export ANTHROPIC_MODEL='claude-opus-4-7'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5@20251001'

```

## 
[​](https://code.claude.com/docs/en/google-vertex-ai#startup-model-checks)
Startup model checks
When Claude Code starts with Vertex AI configured, it verifies that the models it intends to use are accessible in your project. This check requires Claude Code v2.1.98 or later. If you have pinned a model version that is older than the current Claude Code default, and your project can invoke the newer version, Claude Code prompts you to update the pin. Accepting writes the new model ID to your [user settings file](https://code.claude.com/docs/en/settings) and restarts Claude Code. Declining is remembered until the next default version change. If you have not pinned a model and the current default is unavailable in your project, Claude Code falls back to the previous version for the current session and shows a notice. The fallback is not persisted. Enable the newer model in [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) or [pin a version](https://code.claude.com/docs/en/google-vertex-ai#5-pin-model-versions) to make the choice permanent.
## 
[​](https://code.claude.com/docs/en/google-vertex-ai#iam-configuration)
IAM configuration
Assign the required IAM permissions: The `roles/aiplatform.user` role includes the required permissions:
  * `aiplatform.endpoints.predict` - Required for model invocation and token counting

For more restrictive permissions, create a custom role with only the permissions above. For details, see [Vertex IAM documentation](https://cloud.google.com/vertex-ai/docs/general/access-control).
Create a dedicated GCP project for Claude Code to simplify cost tracking and access control.
## 
[​](https://code.claude.com/docs/en/google-vertex-ai#1m-token-context-window)
1M token context window
Claude Opus 4.7, Opus 4.6, and Sonnet 4.6 support the [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows#1m-token-context-window) on Vertex AI. Claude Code automatically enables the extended context window when you select a 1M model variant. The [setup wizard](https://code.claude.com/docs/en/google-vertex-ai#sign-in-with-vertex-ai) offers a 1M context option when it pins models. To enable it for a manually pinned model instead, append `[1m]` to the model ID. See [Pin models for third-party deployments](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments) for details.
## 
[​](https://code.claude.com/docs/en/google-vertex-ai#troubleshooting)
Troubleshooting
If you encounter quota issues:
  * Check current quotas or request quota increase through [Cloud Console](https://cloud.google.com/docs/quotas/view-manage)

If you encounter “model not found” 404 errors:
  * Confirm model is Enabled in [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden)
  * Verify the model is available in the location you specified. Some models are offered only on `global` or multi-region locations such as `eu` and `us`, not in specific regions
  * If using `CLOUD_ML_REGION=global`, check that your models support global endpoints in [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) under “Supported features”. For models that don’t support global endpoints, either:
    * Specify a supported model via `ANTHROPIC_MODEL` or `ANTHROPIC_DEFAULT_HAIKU_MODEL`, or
    * Set a region or multi-region location using `VERTEX_REGION_<MODEL_NAME>` environment variables

If you encounter 429 errors:
  * For regional endpoints, ensure the primary model and small/fast model are supported in your selected region
  * Consider switching to `CLOUD_ML_REGION=global` for better availability


## 
[​](https://code.claude.com/docs/en/google-vertex-ai#additional-resources)
Additional resources
  * [Vertex AI documentation](https://cloud.google.com/vertex-ai/docs)
  * [Vertex AI pricing](https://cloud.google.com/vertex-ai/pricing)
  * [Vertex AI quotas and limits](https://cloud.google.com/vertex-ai/docs/quotas)


Was this page helpful?
YesNo
[Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock)[Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry)
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
[Privacy choices](https://code.claude.com/docs/en/google-vertex-ai)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
