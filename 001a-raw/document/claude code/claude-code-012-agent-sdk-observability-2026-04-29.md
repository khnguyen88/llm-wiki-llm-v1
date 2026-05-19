<!--
url: https://code.claude.com/docs/en/agent-sdk/observability
download_date: 2026-04-29
website: claude-code
webpage: agent-sdk-observability
-->

# Agent Sdk Observability

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/observability#content-area)
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
Control and observability
Observability with OpenTelemetry
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Agent SDK
  * [Overview](https://code.claude.com/docs/en/agent-sdk/overview)
  * [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart)


##### Core concepts
  * [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop)
  * [Use Claude Code features](https://code.claude.com/docs/en/agent-sdk/claude-code-features)
  * [Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions)


##### Input and output
  * [Streaming Input](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)
  * [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input)
  * [Stream responses in real-time](https://code.claude.com/docs/en/agent-sdk/streaming-output)
  * [Get structured output from agents](https://code.claude.com/docs/en/agent-sdk/structured-outputs)


##### Extend with tools
  * [Give Claude custom tools](https://code.claude.com/docs/en/agent-sdk/custom-tools)
  * [Connect to external tools with MCP](https://code.claude.com/docs/en/agent-sdk/mcp)
  * [Scale to many tools with tool search](https://code.claude.com/docs/en/agent-sdk/tool-search)
  * [Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents)


##### Customize behavior
  * [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)
  * [Slash Commands in the SDK](https://code.claude.com/docs/en/agent-sdk/slash-commands)
  * [Agent Skills in the SDK](https://code.claude.com/docs/en/agent-sdk/skills)
  * [Plugins in the SDK](https://code.claude.com/docs/en/agent-sdk/plugins)


##### Control and observability
  * [Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
  * [Intercept and control agent behavior with hooks](https://code.claude.com/docs/en/agent-sdk/hooks)
  * [Rewind file changes with checkpointing](https://code.claude.com/docs/en/agent-sdk/file-checkpointing)
  * [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking)
  * [Observability with OpenTelemetry](https://code.claude.com/docs/en/agent-sdk/observability)
  * [Todo Lists](https://code.claude.com/docs/en/agent-sdk/todo-tracking)


##### Deployment
  * [Hosting the Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting)
  * [Securely deploying AI agents](https://code.claude.com/docs/en/agent-sdk/secure-deployment)


##### SDK references
  * [TypeScript SDK](https://code.claude.com/docs/en/agent-sdk/typescript)
  * [TypeScript V2 (preview)](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview)
  * [Python SDK](https://code.claude.com/docs/en/agent-sdk/python)
  * [Migration Guide](https://code.claude.com/docs/en/agent-sdk/migration-guide)


On this page
  * [How telemetry flows from the SDK](https://code.claude.com/docs/en/agent-sdk/observability#how-telemetry-flows-from-the-sdk)
  * [Enable telemetry export](https://code.claude.com/docs/en/agent-sdk/observability#enable-telemetry-export)
  * [Flush telemetry from short-lived calls](https://code.claude.com/docs/en/agent-sdk/observability#flush-telemetry-from-short-lived-calls)
  * [Read agent traces](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces)
  * [Link traces to your application](https://code.claude.com/docs/en/agent-sdk/observability#link-traces-to-your-application)
  * [Tag telemetry from your agent](https://code.claude.com/docs/en/agent-sdk/observability#tag-telemetry-from-your-agent)
  * [Control sensitive data in exports](https://code.claude.com/docs/en/agent-sdk/observability#control-sensitive-data-in-exports)
  * [Related documentation](https://code.claude.com/docs/en/agent-sdk/observability#related-documentation)


Control and observability
# Observability with OpenTelemetry
Copy page
Export traces, metrics, and events from the Agent SDK to your observability backend using OpenTelemetry.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
When you run agents in production, you need visibility into what they did:
  * which tools they called
  * how long each model request took
  * how many tokens were spent
  * where failures occurred

The Agent SDK can export this data as OpenTelemetry traces, metrics, and log events to any backend that accepts the OpenTelemetry Protocol (OTLP), such as Honeycomb, Datadog, Grafana, Langfuse, or a self-hosted collector. This guide explains how the SDK emits telemetry, how to configure the export, and how to tag and filter the data once it reaches your backend. To read token usage and cost directly from the SDK response stream instead of exporting to a backend, see [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking).
## 
[​](https://code.claude.com/docs/en/agent-sdk/observability#how-telemetry-flows-from-the-sdk)
How telemetry flows from the SDK
The Agent SDK runs the Claude Code CLI as a child process and communicates with it over a local pipe. The CLI has OpenTelemetry instrumentation built in: it records spans around each model request and tool execution, emits metrics for token and cost counters, and emits structured log events for prompts and tool results. The SDK does not produce telemetry of its own. Instead, it passes configuration through to the CLI process, and the CLI exports directly to your collector. Configuration is passed as environment variables. By default, the child process inherits your application’s environment, so you can configure telemetry in either of two places:
  * **Process environment:** set the variables in your shell, container, or orchestrator before your application starts. Every `query()` call picks them up automatically with no code change. This is the recommended approach for production deployments.
  * **Per-call options:** set the variables in `ClaudeAgentOptions.env` (Python) or `options.env` (TypeScript). Use this when different agents in the same process need different telemetry settings. In Python, `env` is merged on top of the inherited environment. In TypeScript, `env` replaces the inherited environment entirely, so include `...process.env` in the object you pass.

The CLI exports three independent OpenTelemetry signals. Each has its own enable switch and its own exporter, so you can turn on only the ones you need.  
| Signal  | What it contains  | Enable with  |  
| --- | --- | --- |  
| Metrics  | Counters for tokens, cost, sessions, lines of code, and tool decisions  | `OTEL_METRICS_EXPORTER`  |  
| Log events  | Structured records for each prompt, API request, API error, and tool result  | `OTEL_LOGS_EXPORTER`  |  
| Traces  | Spans for each interaction, model request, tool call, and hook (beta)  |  `OTEL_TRACES_EXPORTER` plus `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`  |  
For the complete list of metric names, event names, and attributes, see the Claude Code [Monitoring](https://code.claude.com/docs/en/monitoring-usage) reference. The Agent SDK emits the same data because it runs the same CLI. Span names are listed in [Read agent traces](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces) below.
## 
[​](https://code.claude.com/docs/en/agent-sdk/observability#enable-telemetry-export)
Enable telemetry export
Telemetry is off until you set `CLAUDE_CODE_ENABLE_TELEMETRY=1` and choose at least one exporter. The most common configuration sends all three signals over OTLP HTTP to a collector. The following example sets the variables in a dictionary and passes them through `options.env`. The agent runs a single task, and the CLI exports spans, metrics, and events to the collector at `collector.example.com` while the loop consumes the response stream:
Python
TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

OTEL_ENV = {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    # Required for traces, which are in beta. Metrics and log events do not need this.
    "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA": "1",
    # Choose an exporter per signal. Use otlp for the SDK; see the Note below.
    "OTEL_TRACES_EXPORTER": "otlp",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    # Standard OTLP transport configuration.
    "OTEL_EXPORTER_OTLP_PROTOCOL": "http/protobuf",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.example.com:4318",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer your-token",
}


async def main():
    options = ClaudeAgentOptions(env=OTEL_ENV)
    async for message in query(
        prompt="List the files in this directory", options=options
    ):
        print(message)


asyncio.run(main())

```

Because the child process inherits your application’s environment by default, you can achieve the same result by exporting these variables in a Dockerfile, Kubernetes manifest, or shell profile and omitting `options.env` entirely.
The `console` exporter writes telemetry to standard output, which the SDK uses as its message channel. Do not set `console` as an exporter value when running through the SDK. To inspect telemetry locally, point `OTEL_EXPORTER_OTLP_ENDPOINT` at a local collector or an all-in-one Jaeger container instead.
### 
[​](https://code.claude.com/docs/en/agent-sdk/observability#flush-telemetry-from-short-lived-calls)
Flush telemetry from short-lived calls
The CLI batches telemetry and exports on an interval. On a clean process exit it attempts to flush pending data, but the flush is bounded by a short timeout, so spans can still be dropped if the collector is slow to respond. If your process is killed before the CLI shuts down, anything still in the batch buffer is lost. Lowering the export intervals reduces both windows. By default, metrics export every 60 seconds and traces and logs export every 5 seconds. The following example shortens all three intervals so that data reaches the collector while a short task is still running:
Python
TypeScript

```
OTEL_ENV = {
    # ... exporter configuration from the previous example ...
    "OTEL_METRIC_EXPORT_INTERVAL": "1000",
    "OTEL_LOGS_EXPORT_INTERVAL": "1000",
    "OTEL_TRACES_EXPORT_INTERVAL": "1000",
}

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces)
Read agent traces
Traces give you the most detailed view of an agent run. With `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` set, each step of the agent loop becomes a span you can inspect in your tracing backend:
  * **`claude_code.interaction`:** wraps a single turn of the agent loop, from receiving a prompt to producing a response.
  * **`claude_code.llm_request`:** wraps each call to the Claude API, with model name, latency, and token counts as attributes.
  * **`claude_code.tool`:** wraps each tool invocation, with child spans for the permission wait (`claude_code.tool.blocked_on_user`) and the execution itself (`claude_code.tool.execution`).
  * **`claude_code.hook`:** wraps each [hook](https://code.claude.com/docs/en/agent-sdk/hooks) execution. Requires detailed beta tracing (`ENABLE_BETA_TRACING_DETAILED=1` and `BETA_TRACING_ENDPOINT`) in addition to the variables above.

The `llm_request`, `tool`, and `hook` spans are children of the enclosing `claude_code.interaction` span. When the agent spawns a subagent through the Task tool, the subagent’s `llm_request` and `tool` spans nest under the parent agent’s `claude_code.tool` span, so the full delegation chain appears as one trace. Spans carry a `session.id` attribute by default. When you make several `query()` calls against the same [session](https://code.claude.com/docs/en/agent-sdk/sessions), filter on `session.id` in your backend to see them as one timeline. The attribute is omitted if `OTEL_METRICS_INCLUDE_SESSION_ID` is set to a falsy value.
Tracing is in beta. Span names and attributes may change between releases. See [Traces (beta)](https://code.claude.com/docs/en/monitoring-usage#traces-beta) in the Monitoring reference for the trace exporter configuration variables.
## 
[​](https://code.claude.com/docs/en/agent-sdk/observability#link-traces-to-your-application)
Link traces to your application
The SDK automatically propagates W3C trace context into the CLI subprocess. When you call `query()` while an OpenTelemetry span is active in your application, the SDK injects `TRACEPARENT` and `TRACESTATE` into the child process environment, and the CLI reads them so its `claude_code.interaction` span becomes a child of your span. The agent run then appears inside your application’s trace instead of as a disconnected root. The CLI also forwards `TRACEPARENT` to every Bash and PowerShell command it runs. If a command launched through the Bash tool emits its own OpenTelemetry spans, those spans nest under the `claude_code.tool.execution` span that wraps the command. Auto-injection is skipped when you set `TRACEPARENT` explicitly in `options.env`, so you can pin a specific parent context if needed. Interactive CLI sessions ignore inbound `TRACEPARENT` entirely; only Agent SDK and `claude -p` runs honor it. See [Traces (beta)](https://code.claude.com/docs/en/monitoring-usage#traces-beta) in the Monitoring reference for the full span and attribute reference.
## 
[​](https://code.claude.com/docs/en/agent-sdk/observability#tag-telemetry-from-your-agent)
Tag telemetry from your agent
By default, the CLI reports `service.name` as `claude-code`. If you run several agents, or run the SDK alongside other services that export to the same collector, override the service name and add resource attributes so you can filter by agent in your backend. The following example renames the service and attaches deployment metadata. These values are applied as OpenTelemetry resource attributes on every span, metric, and event the agent emits:
Python
TypeScript

```
options = ClaudeAgentOptions(
    env={
        # ... exporter configuration ...
        "OTEL_SERVICE_NAME": "support-triage-agent",
        "OTEL_RESOURCE_ATTRIBUTES": "service.version=1.4.0,deployment.environment=production",
    },
)

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/observability#control-sensitive-data-in-exports)
Control sensitive data in exports
Telemetry is structural by default. Durations, model names, and tool names are recorded on every span; token counts are recorded when the underlying API request returns usage data, so spans for failed or aborted requests may omit them. The content your agent reads and writes is not recorded by default. These opt-in variables add content to the exported data:  
| Variable  | Adds  |  
| --- | --- |  
| `OTEL_LOG_USER_PROMPTS=1`  | Prompt text on `claude_code.user_prompt` events and on the `claude_code.interaction` span  |  
| `OTEL_LOG_TOOL_DETAILS=1`  | Tool input arguments (file paths, shell commands, search patterns) on `claude_code.tool_result` events  |  
| `OTEL_LOG_TOOL_CONTENT=1`  | Full tool input and output bodies as span events on `claude_code.tool`, truncated at 60 KB. Requires [tracing](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces) to be enabled  |  
| `OTEL_LOG_RAW_API_BODIES`  | Full Anthropic Messages API request and response JSON as `claude_code.api_request_body` and `claude_code.api_response_body` log events. Set to `1` for inline bodies truncated at 60 KB, or `file:<dir>` for untruncated bodies on disk with a `body_ref` path in the event. Bodies include the entire conversation history and have extended-thinking content redacted. Enabling this implies consent to everything the three variables above would reveal  |  
Leave these unset unless your observability pipeline is approved to store the data your agent handles. See [Security and privacy](https://code.claude.com/docs/en/monitoring-usage#security-and-privacy) in the Monitoring reference for the full list of attributes and redaction behavior.
## 
[​](https://code.claude.com/docs/en/agent-sdk/observability#related-documentation)
Related documentation
These guides cover adjacent topics for monitoring and deploying agents:
  * [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking): read token and cost data from the message stream without an external backend.
  * [Hosting the Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting): deploy agents in containers where you can set OpenTelemetry variables at the environment level.
  * [Monitoring](https://code.claude.com/docs/en/monitoring-usage): the complete reference for every environment variable, metric, and event the CLI emits.


Was this page helpful?
YesNo
[Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking)[Todo Lists](https://code.claude.com/docs/en/agent-sdk/todo-tracking)
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
[Privacy choices](https://code.claude.com/docs/en/agent-sdk/observability)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
