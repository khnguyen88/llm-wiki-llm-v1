<!--
url: https://code.claude.com/docs/en/monitoring-usage
download_date: 2026-04-29
website: claude-code
webpage: monitoring-usage
-->

# Monitoring Usage

[Skip to main content](https://code.claude.com/docs/en/monitoring-usage#content-area)
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
Usage and costs
Monitoring
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
  * [Quick start](https://code.claude.com/docs/en/monitoring-usage#quick-start)
  * [Administrator configuration](https://code.claude.com/docs/en/monitoring-usage#administrator-configuration)
  * [Configuration details](https://code.claude.com/docs/en/monitoring-usage#configuration-details)
  * [Common configuration variables](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)
  * [Metrics cardinality control](https://code.claude.com/docs/en/monitoring-usage#metrics-cardinality-control)
  * [Traces (beta)](https://code.claude.com/docs/en/monitoring-usage#traces-beta)
  * [Span hierarchy](https://code.claude.com/docs/en/monitoring-usage#span-hierarchy)
  * [Span attributes](https://code.claude.com/docs/en/monitoring-usage#span-attributes)
  * [Dynamic headers](https://code.claude.com/docs/en/monitoring-usage#dynamic-headers)
  * [Settings configuration](https://code.claude.com/docs/en/monitoring-usage#settings-configuration)
  * [Script requirements](https://code.claude.com/docs/en/monitoring-usage#script-requirements)
  * [Refresh behavior](https://code.claude.com/docs/en/monitoring-usage#refresh-behavior)
  * [Multi-team organization support](https://code.claude.com/docs/en/monitoring-usage#multi-team-organization-support)
  * [Example configurations](https://code.claude.com/docs/en/monitoring-usage#example-configurations)
  * [Available metrics and events](https://code.claude.com/docs/en/monitoring-usage#available-metrics-and-events)
  * [Standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * [Metrics](https://code.claude.com/docs/en/monitoring-usage#metrics)
  * [Metric details](https://code.claude.com/docs/en/monitoring-usage#metric-details)
  * [Session counter](https://code.claude.com/docs/en/monitoring-usage#session-counter)
  * [Lines of code counter](https://code.claude.com/docs/en/monitoring-usage#lines-of-code-counter)
  * [Pull request counter](https://code.claude.com/docs/en/monitoring-usage#pull-request-counter)
  * [Commit counter](https://code.claude.com/docs/en/monitoring-usage#commit-counter)
  * [Cost counter](https://code.claude.com/docs/en/monitoring-usage#cost-counter)
  * [Token counter](https://code.claude.com/docs/en/monitoring-usage#token-counter)
  * [Code edit tool decision counter](https://code.claude.com/docs/en/monitoring-usage#code-edit-tool-decision-counter)
  * [Active time counter](https://code.claude.com/docs/en/monitoring-usage#active-time-counter)
  * [Events](https://code.claude.com/docs/en/monitoring-usage#events)
  * [Event correlation attributes](https://code.claude.com/docs/en/monitoring-usage#event-correlation-attributes)
  * [User prompt event](https://code.claude.com/docs/en/monitoring-usage#user-prompt-event)
  * [Tool result event](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)
  * [API request event](https://code.claude.com/docs/en/monitoring-usage#api-request-event)
  * [API error event](https://code.claude.com/docs/en/monitoring-usage#api-error-event)
  * [API request body event](https://code.claude.com/docs/en/monitoring-usage#api-request-body-event)
  * [API response body event](https://code.claude.com/docs/en/monitoring-usage#api-response-body-event)
  * [Tool decision event](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)
  * [Permission mode changed event](https://code.claude.com/docs/en/monitoring-usage#permission-mode-changed-event)
  * [Auth event](https://code.claude.com/docs/en/monitoring-usage#auth-event)
  * [MCP server connection event](https://code.claude.com/docs/en/monitoring-usage#mcp-server-connection-event)
  * [Internal error event](https://code.claude.com/docs/en/monitoring-usage#internal-error-event)
  * [Plugin installed event](https://code.claude.com/docs/en/monitoring-usage#plugin-installed-event)
  * [Skill activated event](https://code.claude.com/docs/en/monitoring-usage#skill-activated-event)
  * [At mention event](https://code.claude.com/docs/en/monitoring-usage#at-mention-event)
  * [API retries exhausted event](https://code.claude.com/docs/en/monitoring-usage#api-retries-exhausted-event)
  * [Hook execution start event](https://code.claude.com/docs/en/monitoring-usage#hook-execution-start-event)
  * [Hook execution complete event](https://code.claude.com/docs/en/monitoring-usage#hook-execution-complete-event)
  * [Compaction event](https://code.claude.com/docs/en/monitoring-usage#compaction-event)
  * [Interpret metrics and events data](https://code.claude.com/docs/en/monitoring-usage#interpret-metrics-and-events-data)
  * [Usage monitoring](https://code.claude.com/docs/en/monitoring-usage#usage-monitoring)
  * [Cost monitoring](https://code.claude.com/docs/en/monitoring-usage#cost-monitoring)
  * [Alerting and segmentation](https://code.claude.com/docs/en/monitoring-usage#alerting-and-segmentation)
  * [Detect retry exhaustion](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)
  * [Event analysis](https://code.claude.com/docs/en/monitoring-usage#event-analysis)
  * [Backend considerations](https://code.claude.com/docs/en/monitoring-usage#backend-considerations)
  * [For metrics](https://code.claude.com/docs/en/monitoring-usage#for-metrics)
  * [For events/logs](https://code.claude.com/docs/en/monitoring-usage#for-events%2Flogs)
  * [For traces](https://code.claude.com/docs/en/monitoring-usage#for-traces)
  * [Service information](https://code.claude.com/docs/en/monitoring-usage#service-information)
  * [ROI measurement resources](https://code.claude.com/docs/en/monitoring-usage#roi-measurement-resources)
  * [Security and privacy](https://code.claude.com/docs/en/monitoring-usage#security-and-privacy)
  * [Monitor Claude Code on Amazon Bedrock](https://code.claude.com/docs/en/monitoring-usage#monitor-claude-code-on-amazon-bedrock)


Usage and costs
# Monitoring
Copy page
Learn how to enable and configure OpenTelemetry for Claude Code.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Track Claude Code usage, costs, and tool activity across your organization by exporting telemetry data through OpenTelemetry (OTel). Claude Code exports metrics as time series data via the standard metrics protocol, events via the logs/events protocol, and optionally distributed traces via the [traces protocol](https://code.claude.com/docs/en/monitoring-usage#traces-beta). Configure your metrics, logs, and traces backends to match your monitoring requirements.
## 
[​](https://code.claude.com/docs/en/monitoring-usage#quick-start)
Quick start
Configure OpenTelemetry using environment variables:

```
# 1. Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=1

# 2. Choose exporters (both are optional - configure only what you need)
export OTEL_METRICS_EXPORTER=otlp       # Options: otlp, prometheus, console, none
export OTEL_LOGS_EXPORTER=otlp          # Options: otlp, console, none

# 3. Configure OTLP endpoint (for OTLP exporter)
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# 4. Set authentication (if required)
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"

# 5. For debugging: reduce export intervals
export OTEL_METRIC_EXPORT_INTERVAL=10000  # 10 seconds (default: 60000ms)
export OTEL_LOGS_EXPORT_INTERVAL=5000     # 5 seconds (default: 5000ms)

# 6. Run Claude Code
claude

```

The default export intervals are 60 seconds for metrics and 5 seconds for logs. During setup, you may want to use shorter intervals for debugging purposes. Remember to reset these for production use.
For full configuration options, see the [OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options).
## 
[​](https://code.claude.com/docs/en/monitoring-usage#administrator-configuration)
Administrator configuration
Administrators can configure OpenTelemetry settings for all users through the [managed settings file](https://code.claude.com/docs/en/settings#settings-files). This allows for centralized control of telemetry settings across an organization. See the [settings precedence](https://code.claude.com/docs/en/settings#settings-precedence) for more information about how settings are applied. Example managed settings configuration:

```
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.example.com:4317",
    "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer example-token"
  }
}

```

Managed settings can be distributed via MDM (Mobile Device Management) or other device management solutions. Environment variables defined in the managed settings file have high precedence and cannot be overridden by users.
## 
[​](https://code.claude.com/docs/en/monitoring-usage#configuration-details)
Configuration details
### 
[​](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)
Common configuration variables  
| Environment Variable  | Description  | Example Values  |  
| --- | --- | --- |  
| `CLAUDE_CODE_ENABLE_TELEMETRY`  | Enables telemetry collection (required)  | `1`  |  
| `OTEL_METRICS_EXPORTER`  | Metrics exporter types, comma-separated. Use `none` to disable  |  `console`, `otlp`, `prometheus`, `none`  |  
| `OTEL_LOGS_EXPORTER`  | Logs/events exporter types, comma-separated. Use `none` to disable  |  `console`, `otlp`, `none`  |  
| `OTEL_EXPORTER_OTLP_PROTOCOL`  | Protocol for OTLP exporter, applies to all signals  |  `grpc`, `http/json`, `http/protobuf`  |  
| `OTEL_EXPORTER_OTLP_ENDPOINT`  | OTLP collector endpoint for all signals  | `http://localhost:4317`  |  
| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL`  | Protocol for metrics, overrides general setting  |  `grpc`, `http/json`, `http/protobuf`  |  
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`  | OTLP metrics endpoint, overrides general setting  | `http://localhost:4318/v1/metrics`  |  
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL`  | Protocol for logs, overrides general setting  |  `grpc`, `http/json`, `http/protobuf`  |  
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`  | OTLP logs endpoint, overrides general setting  | `http://localhost:4318/v1/logs`  |  
| `OTEL_EXPORTER_OTLP_HEADERS`  | Authentication headers for OTLP  | `Authorization=Bearer token`  |  
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY`  | Client key for mTLS authentication  | Path to client key file  |  
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_CERTIFICATE`  | Client certificate for mTLS authentication  | Path to client cert file  |  
| `OTEL_METRIC_EXPORT_INTERVAL`  | Export interval in milliseconds (default: 60000)  |  `5000`, `60000`  |  
| `OTEL_LOGS_EXPORT_INTERVAL`  | Logs export interval in milliseconds (default: 5000)  |  `1000`, `10000`  |  
| `OTEL_LOG_USER_PROMPTS`  | Enable logging of user prompt content (default: disabled)  |  `1` to enable  |  
| `OTEL_LOG_TOOL_DETAILS`  | Enable logging of tool parameters and input arguments in tool events and trace span attributes: Bash commands, MCP server and tool names, skill names, and tool input. Also enables custom, plugin, and MCP command names on `user_prompt` events (default: disabled)  |  `1` to enable  |  
| `OTEL_LOG_TOOL_CONTENT`  | Enable logging of tool input and output content in span events (default: disabled). Requires [tracing](https://code.claude.com/docs/en/monitoring-usage#traces-beta). Content is truncated at 60 KB  |  `1` to enable  |  
| `OTEL_LOG_RAW_API_BODIES`  | Emit the full Anthropic Messages API request and response JSON as `api_request_body` / `api_response_body` log events (default: disabled). Bodies include the entire conversation history. Enabling this implies consent to everything `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`, and `OTEL_LOG_TOOL_CONTENT` would reveal  |  `1` for inline bodies truncated at 60 KB, or `file:<dir>` for untruncated bodies on disk with a `body_ref` pointer in the event  |  
| `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE`  | Metrics temporality preference (default: `delta`). Set to `cumulative` if your backend expects cumulative temporality  |  `delta`, `cumulative`  |  
| `CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS`  | Interval for refreshing dynamic headers (default: 1740000ms / 29 minutes)  | `900000`  |  
### 
[​](https://code.claude.com/docs/en/monitoring-usage#metrics-cardinality-control)
Metrics cardinality control
The following environment variables control which attributes are included in metrics to manage cardinality:  
| Environment Variable  | Description  | Default Value  | Example to Disable  |  
| --- | --- | --- | --- |  
| `OTEL_METRICS_INCLUDE_SESSION_ID`  | Include session.id attribute in metrics  | `true`  | `false`  |  
| `OTEL_METRICS_INCLUDE_VERSION`  | Include app.version attribute in metrics  | `false`  | `true`  |  
| `OTEL_METRICS_INCLUDE_ACCOUNT_UUID`  | Include user.account_uuid and user.account_id attributes in metrics  | `true`  | `false`  |  
These variables help control the cardinality of metrics, which affects storage requirements and query performance in your metrics backend. Lower cardinality generally means better performance and lower storage costs but less granular data for analysis.
### 
[​](https://code.claude.com/docs/en/monitoring-usage#traces-beta)
Traces (beta)
Distributed tracing exports spans that link each user prompt to the API requests and tool executions it triggers, so you can view a full request as a single trace in your tracing backend. Tracing is off by default. To enable it, set both `CLAUDE_CODE_ENABLE_TELEMETRY=1` and `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`, then set `OTEL_TRACES_EXPORTER` to choose where spans are sent. Traces reuse the [common OTLP configuration](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables) for endpoint, protocol, and headers.  
| Environment Variable  | Description  | Example Values  |  
| --- | --- | --- |  
| `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA`  | Enable span tracing (required). `ENABLE_ENHANCED_TELEMETRY_BETA` is also accepted  | `1`  |  
| `OTEL_TRACES_EXPORTER`  | Traces exporter types, comma-separated. Use `none` to disable  |  `console`, `otlp`, `none`  |  
| `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL`  | Protocol for traces, overrides `OTEL_EXPORTER_OTLP_PROTOCOL`  |  `grpc`, `http/json`, `http/protobuf`  |  
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`  | OTLP traces endpoint, overrides `OTEL_EXPORTER_OTLP_ENDPOINT`  | `http://localhost:4318/v1/traces`  |  
| `OTEL_TRACES_EXPORT_INTERVAL`  | Span batch export interval in milliseconds (default: 5000)  |  `1000`, `10000`  |  
Spans redact user prompt text, tool input details, and tool content by default. Set `OTEL_LOG_USER_PROMPTS=1`, `OTEL_LOG_TOOL_DETAILS=1`, and `OTEL_LOG_TOOL_CONTENT=1` to include them. When tracing is active, Bash and PowerShell subprocesses automatically inherit a `TRACEPARENT` environment variable containing the W3C trace context of the active tool execution span. This lets any subprocess that reads `TRACEPARENT` parent its own spans under the same trace, enabling end-to-end distributed tracing through scripts and commands that Claude runs. In Agent SDK and non-interactive sessions started with `-p`, Claude Code also reads `TRACEPARENT` and `TRACESTATE` from its own environment when starting each interaction span. This lets an embedding process pass its active W3C trace context into the subprocess so Claude Code’s spans appear as children of the caller’s distributed trace. Interactive sessions ignore inbound `TRACEPARENT` to avoid accidentally inheriting ambient values from CI or container environments.
#### 
[​](https://code.claude.com/docs/en/monitoring-usage#span-hierarchy)
Span hierarchy
Each user prompt starts a `claude_code.interaction` root span. API calls, tool calls, and hook executions are recorded as its children. Tool spans have two child spans of their own: one for the time spent waiting on a permission decision and one for the execution itself. When the Task tool spawns a subagent, the subagent’s API and tool spans nest under the parent’s `claude_code.tool` span.

```
claude_code.interaction
├── claude_code.llm_request
├── claude_code.hook                    (requires detailed beta tracing)
└── claude_code.tool
    ├── claude_code.tool.blocked_on_user
    ├── claude_code.tool.execution
    └── (Task tool) subagent claude_code.llm_request / claude_code.tool spans

```

In Agent SDK and `claude -p` sessions, `claude_code.interaction` itself becomes a child of the caller’s span when `TRACEPARENT` is set in the environment.
#### 
[​](https://code.claude.com/docs/en/monitoring-usage#span-attributes)
Span attributes
Every span carries the [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes) plus a `span.type` attribute matching its name. The tables below list the additional attributes set on each span. The `llm_request`, `tool.execution`, and `hook` spans set OpenTelemetry status `ERROR` when they record a failure; the other spans always end with status `UNSET`. **`claude_code.interaction`**  
| Attribute  | Description  | Gated by  |  
| --- | --- | --- |  
| `user_prompt`  | Prompt text. Value is `<REDACTED>` unless the gate is set  | `OTEL_LOG_USER_PROMPTS`  |  
| `user_prompt_length`  | Prompt length in characters  |   |  
| `interaction.sequence`  | 1-based counter of interactions in this session  |   |  
| `interaction.duration_ms`  | Wall-clock duration of the turn  |   |  
**`claude_code.llm_request`**  
| Attribute  | Description  | Gated by  |  
| --- | --- | --- |  
| `model`  | Model identifier  |   |  
| `gen_ai.system`  | Always `anthropic`. OpenTelemetry GenAI semantic convention  |   |  
| `gen_ai.request.model`  | Same value as `model`. OpenTelemetry GenAI semantic convention  |   |  
| `query_source`  | Subsystem that issued the request, such as `repl_main_thread` or a subagent name  |   |  
| `speed`  |  `fast` or `normal`  |   |  
| `llm_request.context`  |  `interaction`, `tool`, or `standalone` depending on the parent span  |   |  
| `duration_ms`  | Wall-clock duration including retries  |   |  
| `ttft_ms`  | Time to first token in milliseconds  |   |  
| `input_tokens`  | Input token count from the API usage block  |   |  
| `output_tokens`  | Output token count  |   |  
| `cache_read_tokens`  | Tokens read from prompt cache  |   |  
| `cache_creation_tokens`  | Tokens written to prompt cache  |   |  
| `request_id`  | Anthropic API request ID from the `request-id` response header  |   |  
| `gen_ai.response.id`  | Same value as `request_id`. OpenTelemetry GenAI semantic convention  |   |  
| `client_request_id`  | Client-generated `x-client-request-id` of the final attempt  |   |  
| `attempt`  | Total attempts made for this request  |   |  
| `success`  |  `true` or `false`  |   |  
| `status_code`  | HTTP status code when the request failed  |   |  
| `error`  | Error message when the request failed  |   |  
| `response.has_tool_call`  |  `true` when the response contained tool-use blocks  |   |  
| `stop_reason`  | API response `stop_reason`, such as `end_turn`, `tool_use`, `max_tokens`, `stop_sequence`, `pause_turn`, or `refusal`  |   |  
| `gen_ai.response.finish_reasons`  | Same value as `stop_reason`, wrapped in a string array. OpenTelemetry GenAI semantic convention  |   |  
Each retry attempt is also recorded as a `gen_ai.request.attempt` span event with `attempt` and `client_request_id` attributes. **`claude_code.tool`**  
| Attribute  | Description  | Gated by  |  
| --- | --- | --- |  
| `tool_name`  | Tool name  |   |  
| `duration_ms`  | Wall-clock duration including permission wait and execution  |   |  
| `result_tokens`  | Approximate token size of the tool result  |   |  
| `file_path`  | Target file path for Read, Edit, and Write tools  | `OTEL_LOG_TOOL_DETAILS`  |  
| `full_command`  | Command string for the Bash tool  | `OTEL_LOG_TOOL_DETAILS`  |  
| `skill_name`  | Skill name for the Skill tool  | `OTEL_LOG_TOOL_DETAILS`  |  
| `subagent_type`  | Subagent type for the Task tool  | `OTEL_LOG_TOOL_DETAILS`  |  
When `OTEL_LOG_TOOL_CONTENT=1`, this span also records a `tool.output` span event whose attributes contain the tool’s input and output bodies, truncated at 60 KB per attribute. **`claude_code.tool.blocked_on_user`**  
| Attribute  | Description  | Gated by  |  
| --- | --- | --- |  
| `duration_ms`  | Time spent waiting for the permission decision  |   |  
| `decision`  |  `accept` or `reject`  |   |  
| `source`  | Decision source, matching the `tool_decision` event  |   |  
**`claude_code.tool.execution`**  
| Attribute  | Description  | Gated by  |  
| --- | --- | --- |  
| `duration_ms`  | Time spent running the tool body  |   |  
| `success`  |  `true` or `false`  |   |  
| `error`  | Error category string when execution failed, such as `Error:ENOENT` or `ShellError`. Contains the full error message instead when the gate is set  | `OTEL_LOG_TOOL_DETAILS`  |  
**`claude_code.hook`** This span is emitted only when detailed beta tracing is active, which requires `ENABLE_BETA_TRACING_DETAILED=1` and `BETA_TRACING_ENDPOINT` in addition to the trace exporter configuration above. In interactive CLI sessions, this also requires your organization to be allowlisted for the feature. Agent SDK and non-interactive `-p` sessions are not gated. It is not emitted when only `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA` is set.  
| Attribute  | Description  | Gated by  |  
| --- | --- | --- |  
| `hook_event`  | Hook event type, such as `PreToolUse`  |   |  
| `hook_name`  | Full hook name, such as `PreToolUse:Write`  |   |  
| `num_hooks`  | Number of matching hook commands executed  |   |  
| `hook_definitions`  | JSON-serialized hook configuration  | `OTEL_LOG_TOOL_DETAILS`  |  
| `duration_ms`  | Wall-clock duration of all matching hooks  |   |  
| `num_success`  | Count of hooks that completed successfully  |   |  
| `num_blocking`  | Count of hooks that returned a blocking decision  |   |  
| `num_non_blocking_error`  | Count of hooks that failed without blocking  |   |  
| `num_cancelled`  | Count of hooks cancelled before completion  |   |  
Additional content-bearing attributes such as `new_context`, `system_prompt_preview`, `user_system_prompt`, `tool_input`, and `response.model_output` are emitted only when detailed beta tracing is active. They are not part of the stable span schema. `user_system_prompt` additionally requires `OTEL_LOG_USER_PROMPTS=1`. It carries only the system prompt text you provide via the `systemPrompt` SDK option or `--system-prompt` and `--append-system-prompt` flags, truncated at 60 KB, and is emitted once per session rather than per request.
### 
[​](https://code.claude.com/docs/en/monitoring-usage#dynamic-headers)
Dynamic headers
For enterprise environments that require dynamic authentication, you can configure a script to generate headers dynamically:
#### 
[​](https://code.claude.com/docs/en/monitoring-usage#settings-configuration)
Settings configuration
Add to your `.claude/settings.json`:

```
{
  "otelHeadersHelper": "/bin/generate_opentelemetry_headers.sh"
}

```

#### 
[​](https://code.claude.com/docs/en/monitoring-usage#script-requirements)
Script requirements
The script must output valid JSON with string key-value pairs representing HTTP headers:

```
#!/bin/bash
# Example: Multiple headers
echo "{\"Authorization\": \"Bearer $(get-token.sh)\", \"X-API-Key\": \"$(get-api-key.sh)\"}"

```

#### 
[​](https://code.claude.com/docs/en/monitoring-usage#refresh-behavior)
Refresh behavior
The headers helper script runs at startup and periodically thereafter to support token refresh. By default, the script runs every 29 minutes. Customize the interval with the `CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS` environment variable.
### 
[​](https://code.claude.com/docs/en/monitoring-usage#multi-team-organization-support)
Multi-team organization support
Organizations with multiple teams or departments can add custom attributes to distinguish between different groups using the `OTEL_RESOURCE_ATTRIBUTES` environment variable:

```
# Add custom attributes for team identification
export OTEL_RESOURCE_ATTRIBUTES="department=engineering,team.id=platform,cost_center=eng-123"

```

These custom attributes will be included in all metrics and events, allowing you to:
  * Filter metrics by team or department
  * Track costs per cost center
  * Create team-specific dashboards
  * Set up alerts for specific teams


**Important formatting requirements for OTEL_RESOURCE_ATTRIBUTES:** The `OTEL_RESOURCE_ATTRIBUTES` environment variable uses comma-separated key=value pairs with strict formatting requirements:
  * **No spaces allowed** : Values cannot contain spaces. For example, `user.organizationName=My Company` is invalid
  * **Format** : Must be comma-separated key=value pairs: `key1=value1,key2=value2`
  * **Allowed characters** : Only US-ASCII characters excluding control characters, whitespace, double quotes, commas, semicolons, and backslashes
  * **Special characters** : Characters outside the allowed range must be percent-encoded

**Examples:**

```
# ❌ Invalid - contains spaces
export OTEL_RESOURCE_ATTRIBUTES="org.name=John's Organization"

# ✅ Valid - use underscores or camelCase instead
export OTEL_RESOURCE_ATTRIBUTES="org.name=Johns_Organization"
export OTEL_RESOURCE_ATTRIBUTES="org.name=JohnsOrganization"

# ✅ Valid - percent-encode special characters if needed
export OTEL_RESOURCE_ATTRIBUTES="org.name=John%27s%20Organization"

```

Note: wrapping values in quotes doesn’t escape spaces. For example, `org.name="My Company"` results in the literal value `"My Company"` (with quotes included), not `My Company`.
### 
[​](https://code.claude.com/docs/en/monitoring-usage#example-configurations)
Example configurations
Set these environment variables before running `claude`. Each block shows a complete configuration for a different exporter or deployment scenario:

```
# Console debugging (1-second intervals)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console
export OTEL_METRIC_EXPORT_INTERVAL=1000

# OTLP/gRPC
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Prometheus
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=prometheus

# Multiple exporters
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=console,otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/json

# Different endpoints/backends for metrics and logs
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_METRICS_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://metrics.example.com:4318
export OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://logs.example.com:4317

# Metrics only (no events/logs)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Events/logs only (no metrics)
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

```

## 
[​](https://code.claude.com/docs/en/monitoring-usage#available-metrics-and-events)
Available metrics and events
### 
[​](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
Standard attributes
All metrics and events share these standard attributes:  
| Attribute  | Description  | Controlled By  |  
| --- | --- | --- |  
| `session.id`  | Unique session identifier  |  `OTEL_METRICS_INCLUDE_SESSION_ID` (default: true)  |  
| `app.version`  | Current Claude Code version  |  `OTEL_METRICS_INCLUDE_VERSION` (default: false)  |  
| `organization.id`  | Organization UUID (when authenticated)  | Always included when available  |  
| `user.account_uuid`  | Account UUID (when authenticated)  |  `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default: true)  |  
| `user.account_id`  | Account ID in tagged format matching Anthropic admin APIs (when authenticated), such as `user_01BWBeN28...`  |  `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` (default: true)  |  
| `user.id`  | Anonymous device/installation identifier, generated per Claude Code installation  | Always included  |  
| `user.email`  | User email address (when authenticated via OAuth)  | Always included when available  |  
| `terminal.type`  | Terminal type, such as `iTerm.app`, `vscode`, `cursor`, or `tmux`  | Always included when detected  |  
Events additionally include the following attributes. These are never attached to metrics because they would cause unbounded cardinality:
  * `prompt.id`: UUID correlating a user prompt with all subsequent events until the next prompt. See [Event correlation attributes](https://code.claude.com/docs/en/monitoring-usage#event-correlation-attributes).
  * `workspace.host_paths`: host workspace directories selected in the desktop app, as a string array


### 
[​](https://code.claude.com/docs/en/monitoring-usage#metrics)
Metrics
Claude Code exports the following metrics:  
| Metric Name  | Description  | Unit  |  
| --- | --- | --- |  
| `claude_code.session.count`  | Count of CLI sessions started  | count  |  
| `claude_code.lines_of_code.count`  | Count of lines of code modified  | count  |  
| `claude_code.pull_request.count`  | Number of pull requests created  | count  |  
| `claude_code.commit.count`  | Number of git commits created  | count  |  
| `claude_code.cost.usage`  | Cost of the Claude Code session  | USD  |  
| `claude_code.token.usage`  | Number of tokens used  | tokens  |  
| `claude_code.code_edit_tool.decision`  | Count of code editing tool permission decisions  | count  |  
| `claude_code.active_time.total`  | Total active time in seconds  | s  |  
### 
[​](https://code.claude.com/docs/en/monitoring-usage#metric-details)
Metric details
Each metric includes the standard attributes listed above. Metrics with additional context-specific attributes are noted below.
#### 
[​](https://code.claude.com/docs/en/monitoring-usage#session-counter)
Session counter
Incremented at the start of each session. **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `start_type`: How the session was started. One of `"fresh"`, `"resume"`, or `"continue"`


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#lines-of-code-counter)
Lines of code counter
Incremented when code is added or removed. **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `type`: (`"added"`, `"removed"`)


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#pull-request-counter)
Pull request counter
Incremented when creating pull requests via Claude Code. **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#commit-counter)
Commit counter
Incremented when creating git commits via Claude Code. **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#cost-counter)
Cost counter
Incremented after each API request. **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `model`: Model identifier (for example, “claude-sonnet-4-6”)
  * `query_source`: Category of the subsystem that issued the request. One of `"main"`, `"subagent"`, or `"auxiliary"`
  * `speed`: `"fast"` when the request used fast mode. Absent otherwise
  * `effort`: [Effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level) applied to the request: `"low"`, `"medium"`, `"high"`, `"xhigh"`, or `"max"`. Absent when the model does not support effort.


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#token-counter)
Token counter
Incremented after each API request. **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `type`: (`"input"`, `"output"`, `"cacheRead"`, `"cacheCreation"`)
  * `model`: Model identifier (for example, “claude-sonnet-4-6”)
  * `query_source`: Category of the subsystem that issued the request. One of `"main"`, `"subagent"`, or `"auxiliary"`
  * `speed`: `"fast"` when the request used fast mode. Absent otherwise
  * `effort`: [Effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level) applied to the request. See [Cost counter](https://code.claude.com/docs/en/monitoring-usage#cost-counter) for details.


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#code-edit-tool-decision-counter)
Code edit tool decision counter
Incremented when user accepts or rejects Edit, Write, or NotebookEdit tool usage. **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `tool_name`: Tool name (`"Edit"`, `"Write"`, `"NotebookEdit"`)
  * `decision`: User decision (`"accept"`, `"reject"`)
  * `source`: Decision source - `"config"`, `"hook"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`
  * `language`: Programming language of the edited file, such as `"TypeScript"`, `"Python"`, `"JavaScript"`, or `"Markdown"`. Returns `"unknown"` for unrecognized file extensions.


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#active-time-counter)
Active time counter
Tracks actual time spent actively using Claude Code, excluding idle time. This metric is incremented during user interactions (typing, reading responses) and during CLI processing (tool execution, AI response generation). **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `type`: `"user"` for keyboard interactions, `"cli"` for tool execution and AI responses


### 
[​](https://code.claude.com/docs/en/monitoring-usage#events)
Events
Claude Code exports the following events via OpenTelemetry logs/events (when `OTEL_LOGS_EXPORTER` is configured):
#### 
[​](https://code.claude.com/docs/en/monitoring-usage#event-correlation-attributes)
Event correlation attributes
When a user submits a prompt, Claude Code may make multiple API calls and run several tools. The `prompt.id` attribute lets you tie all of those events back to the single prompt that triggered them.  
| Attribute  | Description  |  
| --- | --- |  
| `prompt.id`  | UUID v4 identifier linking all events produced while processing a single user prompt  |  
To trace all activity triggered by a single prompt, filter your events by a specific `prompt.id` value. This returns the user_prompt event, any api_request events, and any tool_result events that occurred while processing that prompt.
`prompt.id` is intentionally excluded from metrics because each prompt generates a unique ID, which would create an ever-growing number of time series. Use it for event-level analysis and audit trails only.
#### 
[​](https://code.claude.com/docs/en/monitoring-usage#user-prompt-event)
User prompt event
Logged when a user submits a prompt. **Event Name** : `claude_code.user_prompt` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"user_prompt"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `prompt_length`: Length of the prompt
  * `prompt`: Prompt content (redacted by default, enable with `OTEL_LOG_USER_PROMPTS=1`)
  * `command_name`: Command name when the prompt invokes one. Built-in and bundled command names such as `compact` or `debug` are emitted as-is; aliases such as `reset` emit as typed rather than the canonical name. Custom, plugin, and MCP command names collapse to `custom` or `mcp` unless `OTEL_LOG_TOOL_DETAILS=1` is set
  * `command_source`: Origin of the command when present: `builtin`, `custom`, or `mcp`. Plugin-provided commands report as `custom`


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)
Tool result event
Logged when a tool completes execution. **Event Name** : `claude_code.tool_result` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"tool_result"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `tool_name`: Name of the tool
  * `tool_use_id`: Unique identifier for this tool invocation. Matches the `tool_use_id` passed to hooks, allowing correlation between OTel events and hook-captured data.
  * `success`: `"true"` or `"false"`
  * `duration_ms`: Execution time in milliseconds
  * `error_type`: Error category string when the tool failed, such as `"Error:ENOENT"` or `"ShellError"`
  * `error` (when `OTEL_LOG_TOOL_DETAILS=1`): Full error message when the tool failed
  * `decision_type`: Either `"accept"` or `"reject"`
  * `decision_source`: Decision source - `"config"`, `"hook"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`
  * `tool_input_size_bytes`: Size of the JSON-serialized tool input in bytes
  * `tool_result_size_bytes`: Size of the tool result in bytes
  * `mcp_server_scope`: MCP server scope identifier (for MCP tools)
  * `tool_parameters` (when `OTEL_LOG_TOOL_DETAILS=1`): JSON string containing tool-specific parameters:
    * For Bash tool: includes `bash_command`, `full_command`, `timeout`, `description`, `dangerouslyDisableSandbox`, and `git_commit_id` (the commit SHA, when a `git commit` command succeeds)
    * For MCP tools: includes `mcp_server_name`, `mcp_tool_name`
    * For Skill tool: includes `skill_name`
    * For Task tool: includes `subagent_type`
  * `tool_input` (when `OTEL_LOG_TOOL_DETAILS=1`): JSON-serialized tool arguments. Individual values over 512 characters are truncated, and the full payload is bounded to ~4 K characters. Applies to all tools including MCP tools.


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#api-request-event)
API request event
Logged for each API request to Claude. **Event Name** : `claude_code.api_request` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"api_request"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `model`: Model used (for example, “claude-sonnet-4-6”)
  * `cost_usd`: Estimated cost in USD
  * `duration_ms`: Request duration in milliseconds
  * `input_tokens`: Number of input tokens
  * `output_tokens`: Number of output tokens
  * `cache_read_tokens`: Number of tokens read from cache
  * `cache_creation_tokens`: Number of tokens used for cache creation
  * `request_id`: Anthropic API request ID from the response’s `request-id` header, such as `"req_011..."`. Present only when the API returns one.
  * `speed`: `"fast"` or `"normal"`, indicating whether fast mode was active
  * `query_source`: Subsystem that issued the request, such as `"repl_main_thread"`, `"compact"`, or a subagent name
  * `effort`: [Effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level) applied to the request: `"low"`, `"medium"`, `"high"`, `"xhigh"`, or `"max"`. Absent when the model does not support effort.


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#api-error-event)
API error event
Logged when an API request to Claude fails. **Event Name** : `claude_code.api_error` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"api_error"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `model`: Model used (for example, “claude-sonnet-4-6”)
  * `error`: Error message
  * `status_code`: HTTP status code as a number. Absent for non-HTTP errors such as connection failures.
  * `duration_ms`: Request duration in milliseconds
  * `attempt`: Total number of attempts made, including the initial request (`1` means no retries occurred)
  * `request_id`: Anthropic API request ID from the response’s `request-id` header, such as `"req_011..."`. Present only when the API returns one.
  * `speed`: `"fast"` or `"normal"`, indicating whether fast mode was active
  * `query_source`: Subsystem that issued the request, such as `"repl_main_thread"`, `"compact"`, or a subagent name
  * `effort`: [Effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level) applied to the request. Absent when the model does not support effort.


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#api-request-body-event)
API request body event
Logged for each API request attempt when `OTEL_LOG_RAW_API_BODIES` is set. One event is emitted per attempt, so retries with adjusted parameters each produce their own event. **Event Name** : `claude_code.api_request_body` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"api_request_body"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `body`: JSON-serialized Messages API request parameters (system prompt, messages, tools, etc.), truncated at 60 KB. Extended-thinking content in prior assistant turns is redacted. Emitted only in inline mode (`OTEL_LOG_RAW_API_BODIES=1`).
  * `body_ref`: Absolute path to a `<dir>/<uuid>.request.json` file containing the untruncated body. Emitted only in file mode (`OTEL_LOG_RAW_API_BODIES=file:<dir>`).
  * `body_length`: Untruncated body length. UTF-8 bytes when `OTEL_LOG_RAW_API_BODIES=file:<dir>`, or UTF-16 code units when `=1`
  * `body_truncated`: `"true"` when inline truncation occurred. Absent in file mode and when no truncation occurred.
  * `model`: Model identifier from the request parameters
  * `query_source`: Subsystem that issued the request (for example, `"compact"`)


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#api-response-body-event)
API response body event
Logged for each successful API response when `OTEL_LOG_RAW_API_BODIES` is set. **Event Name** : `claude_code.api_response_body` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"api_response_body"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `body`: JSON-serialized Messages API response (id, content blocks, usage, stop reason), truncated at 60 KB. Extended-thinking content is redacted. Emitted only in inline mode (`OTEL_LOG_RAW_API_BODIES=1`).
  * `body_ref`: Absolute path to a `<dir>/<request_id>.response.json` file containing the untruncated body. Emitted only in file mode (`OTEL_LOG_RAW_API_BODIES=file:<dir>`).
  * `body_length`: Untruncated body length. UTF-8 bytes when `OTEL_LOG_RAW_API_BODIES=file:<dir>`, or UTF-16 code units when `=1`
  * `body_truncated`: `"true"` when inline truncation occurred. Absent in file mode and when no truncation occurred.
  * `model`: Model identifier
  * `query_source`: Subsystem that issued the request
  * `request_id`: Anthropic API request ID from the response’s `request-id` header, such as `"req_011..."`. Present only when the API returns one.


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)
Tool decision event
Logged when a tool permission decision is made (accept/reject). **Event Name** : `claude_code.tool_decision` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"tool_decision"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `tool_name`: Name of the tool (for example, “Read”, “Edit”, “Write”, “NotebookEdit”)
  * `tool_use_id`: Unique identifier for this tool invocation. Matches the `tool_use_id` passed to hooks, allowing correlation between OTel events and hook-captured data.
  * `decision`: Either `"accept"` or `"reject"`
  * `source`: Decision source - `"config"`, `"hook"`, `"user_permanent"`, `"user_temporary"`, `"user_abort"`, or `"user_reject"`


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#permission-mode-changed-event)
Permission mode changed event
Logged when the permission mode changes, for example from `Shift+Tab` cycling, exiting plan mode, or an auto mode gate check. **Event Name** : `claude_code.permission_mode_changed` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"permission_mode_changed"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `from_mode`: The previous permission mode, for example `"default"`, `"plan"`, `"acceptEdits"`, `"auto"`, or `"bypassPermissions"`
  * `to_mode`: The new permission mode
  * `trigger`: What caused the change. One of `"shift_tab"`, `"exit_plan_mode"`, `"auto_gate_denied"`, or `"auto_opt_in"`. Absent when the transition originates from the SDK or bridge


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#auth-event)
Auth event
Logged when `/login` or `/logout` completes. **Event Name** : `claude_code.auth` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"auth"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `action`: `"login"` or `"logout"`
  * `success`: `"true"` or `"false"`
  * `auth_method`: Authentication method, such as `"oauth"`
  * `error_category`: Categorical error kind when the action failed. The raw error message is never included
  * `status_code`: HTTP status code as a string when the action failed with an HTTP error


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#mcp-server-connection-event)
MCP server connection event
Logged when an MCP server connects, disconnects, or fails to connect. **Event Name** : `claude_code.mcp_server_connection` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"mcp_server_connection"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `status`: `"connected"`, `"failed"`, or `"disconnected"`
  * `transport_type`: Server transport, such as `"stdio"`, `"sse"`, or `"http"`
  * `server_scope`: Scope the server is configured at, such as `"user"`, `"project"`, or `"local"`
  * `duration_ms`: Connection attempt duration in milliseconds
  * `error_code`: Error code when the connection failed
  * `server_name` (when `OTEL_LOG_TOOL_DETAILS=1`): Configured server name
  * `error` (when `OTEL_LOG_TOOL_DETAILS=1`): Full error message when the connection failed


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#internal-error-event)
Internal error event
Logged when Claude Code catches an unexpected internal error. Only the error class name and an errno-style code are recorded. The error message and stack trace are never included. This event is not emitted when running against Bedrock, Vertex, or Foundry, or when `DISABLE_ERROR_REPORTING` is set. **Event Name** : `claude_code.internal_error` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"internal_error"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `error_name`: Error class name, such as `"TypeError"` or `"SyntaxError"`
  * `error_code`: Node.js errno code such as `"ENOENT"` when present on the error


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#plugin-installed-event)
Plugin installed event
Logged when a plugin finishes installing, from both the `claude plugin install` CLI command and the interactive `/plugin` UI. **Event Name** : `claude_code.plugin_installed` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"plugin_installed"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `marketplace.is_official`: `"true"` if the marketplace is an official Anthropic marketplace, `"false"` otherwise
  * `install.trigger`: `"cli"` or `"ui"`
  * `plugin.name`: Name of the installed plugin. For third-party marketplaces this is included only when `OTEL_LOG_TOOL_DETAILS=1`
  * `plugin.version`: Plugin version when declared in the marketplace entry. For third-party marketplaces this is included only when `OTEL_LOG_TOOL_DETAILS=1`
  * `marketplace.name`: Marketplace the plugin was installed from. For third-party marketplaces this is included only when `OTEL_LOG_TOOL_DETAILS=1`


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#skill-activated-event)
Skill activated event
Logged when a skill is invoked. **Event Name** : `claude_code.skill_activated` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"skill_activated"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `skill.name`: Name of the skill. For user-defined and third-party plugin skills the value is the placeholder `"custom_skill"` unless `OTEL_LOG_TOOL_DETAILS=1`
  * `skill.source`: Where the skill was loaded from (for example, `"bundled"`, `"userSettings"`, `"projectSettings"`, `"plugin"`)
  * `plugin.name` (when `OTEL_LOG_TOOL_DETAILS=1` or the plugin is from an official marketplace): Name of the owning plugin when the skill is provided by a plugin
  * `marketplace.name` (when `OTEL_LOG_TOOL_DETAILS=1` or the plugin is from an official marketplace): Marketplace the owning plugin was installed from, when the skill is provided by a plugin


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#at-mention-event)
At mention event
Logged when Claude Code resolves an `@`-mention in a prompt. Not every mention emits an event: early-exit paths such as permission denials, oversized files, PDF reference attachments, and directory listing failures return without logging. **Event Name** : `claude_code.at_mention` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"at_mention"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `mention_type`: Type of mention (`"file"`, `"directory"`, `"agent"`, `"mcp_resource"`)
  * `success`: Whether the mention resolved successfully (`"true"` or `"false"`)


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#api-retries-exhausted-event)
API retries exhausted event
Logged once when an API request fails after more than one attempt. Emitted alongside the final `api_error` event. **Event Name** : `claude_code.api_retries_exhausted` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"api_retries_exhausted"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `model`: Model used
  * `error`: Final error message
  * `status_code`: HTTP status code as a number. Absent for non-HTTP errors.
  * `total_attempts`: Total number of attempts made
  * `total_retry_duration_ms`: Total wall-clock time across all attempts
  * `speed`: `"fast"` or `"normal"`


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#hook-execution-start-event)
Hook execution start event
Logged when one or more hooks begin executing for a hook event. **Event Name** : `claude_code.hook_execution_start` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"hook_execution_start"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `hook_event`: Hook event type, such as `"PreToolUse"` or `"PostToolUse"`
  * `hook_name`: Full hook name including matcher, such as `"PreToolUse:Write"`
  * `num_hooks`: Number of matching hook commands
  * `managed_only`: `"true"` when only managed-policy hooks are permitted
  * `hook_source`: `"policySettings"` or `"merged"`
  * `hook_definitions`: JSON-serialized hook configuration. Included only when both detailed beta tracing and `OTEL_LOG_TOOL_DETAILS=1` are enabled


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#hook-execution-complete-event)
Hook execution complete event
Logged when all hooks for a hook event have finished. **Event Name** : `claude_code.hook_execution_complete` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"hook_execution_complete"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `hook_event`: Hook event type
  * `hook_name`: Full hook name including matcher
  * `num_hooks`: Number of matching hook commands
  * `num_success`: Count that completed successfully
  * `num_blocking`: Count that returned a blocking decision
  * `num_non_blocking_error`: Count that failed without blocking
  * `num_cancelled`: Count cancelled before completion
  * `total_duration_ms`: Wall-clock duration of all matching hooks
  * `managed_only`: `"true"` when only managed-policy hooks are permitted
  * `hook_source`: `"policySettings"` or `"merged"`
  * `hook_definitions`: JSON-serialized hook configuration. Included only when both detailed beta tracing and `OTEL_LOG_TOOL_DETAILS=1` are enabled


#### 
[​](https://code.claude.com/docs/en/monitoring-usage#compaction-event)
Compaction event
Logged when conversation compaction completes. **Event Name** : `claude_code.compaction` **Attributes** :
  * All [standard attributes](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
  * `event.name`: `"compaction"`
  * `event.timestamp`: ISO 8601 timestamp
  * `event.sequence`: monotonically increasing counter for ordering events within a session
  * `trigger`: `"auto"` or `"manual"`
  * `success`: `"true"` or `"false"`
  * `duration_ms`: Compaction duration
  * `pre_tokens`: Approximate token count before compaction
  * `post_tokens`: Approximate token count after compaction
  * `error`: Error message when compaction failed


## 
[​](https://code.claude.com/docs/en/monitoring-usage#interpret-metrics-and-events-data)
Interpret metrics and events data
The exported metrics and events support a range of analyses:
### 
[​](https://code.claude.com/docs/en/monitoring-usage#usage-monitoring)
Usage monitoring  
| Metric  | Analysis Opportunity  |  
| --- | --- |  
| `claude_code.token.usage`  | Break down by `type` (input/output), user, team, or model  |  
| `claude_code.session.count`  | Track adoption and engagement over time  |  
| `claude_code.lines_of_code.count`  | Measure productivity by tracking code additions/removals  |  
|  `claude_code.commit.count` & `claude_code.pull_request.count`  | Understand impact on development workflows  |  
### 
[​](https://code.claude.com/docs/en/monitoring-usage#cost-monitoring)
Cost monitoring
The `claude_code.cost.usage` metric helps with:
  * Tracking usage trends across teams or individuals
  * Identifying high-usage sessions for optimization


Cost metrics are approximations. For official billing data, refer to your API provider (Claude Console, AWS Bedrock, or Google Cloud Vertex).
### 
[​](https://code.claude.com/docs/en/monitoring-usage#alerting-and-segmentation)
Alerting and segmentation
Common alerts to consider:
  * Cost spikes
  * Unusual token consumption
  * High session volume from specific users

All metrics can be segmented by `user.account_uuid`, `user.account_id`, `organization.id`, `session.id`, `model`, and `app.version`.
### 
[​](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)
Detect retry exhaustion
Claude Code retries failed API requests internally and emits a single `claude_code.api_error` event only after it gives up, so the event itself is the terminal signal for that request. Intermediate retry attempts are not logged as separate events. The `attempt` attribute on the event records how many attempts were made in total. A value greater than `CLAUDE_CODE_MAX_RETRIES` (default `10`) indicates the request exhausted all retries on a transient error. A lower value indicates a non-retryable error such as a `400` response. To distinguish a session that recovered from one that stalled, group events by `session.id` and check whether a later `api_request` event exists after the error.
### 
[​](https://code.claude.com/docs/en/monitoring-usage#event-analysis)
Event analysis
The event data provides detailed insights into Claude Code interactions: **Tool Usage Patterns** : analyze tool result events to identify:
  * Most frequently used tools
  * Tool success rates
  * Average tool execution times
  * Error patterns by tool type

**Performance Monitoring** : track API request durations and tool execution times to identify performance bottlenecks.
## 
[​](https://code.claude.com/docs/en/monitoring-usage#backend-considerations)
Backend considerations
Your choice of metrics, logs, and traces backends determines the types of analyses you can perform:
### 
[​](https://code.claude.com/docs/en/monitoring-usage#for-metrics)
For metrics
  * **Time series databases (for example, Prometheus)** : Rate calculations, aggregated metrics
  * **Columnar stores (for example, ClickHouse)** : Complex queries, unique user analysis
  * **Full-featured observability platforms (for example, Honeycomb, Datadog)** : Advanced querying, visualization, alerting


### 
[​](https://code.claude.com/docs/en/monitoring-usage#for-events/logs)
For events/logs
  * **Log aggregation systems (for example, Elasticsearch, Loki)** : Full-text search, log analysis
  * **Columnar stores (for example, ClickHouse)** : Structured event analysis
  * **Full-featured observability platforms (for example, Honeycomb, Datadog)** : Correlation between metrics and events


### 
[​](https://code.claude.com/docs/en/monitoring-usage#for-traces)
For traces
Choose a backend that supports distributed trace storage and span correlation:
  * **Distributed tracing systems (for example, Jaeger, Zipkin, Grafana Tempo)** : Span visualization, request waterfalls, latency analysis
  * **Full-featured observability platforms (for example, Honeycomb, Datadog)** : Trace search and correlation with metrics and logs

For organizations requiring Daily/Weekly/Monthly Active User (DAU/WAU/MAU) metrics, consider backends that support efficient unique value queries.
## 
[​](https://code.claude.com/docs/en/monitoring-usage#service-information)
Service information
All metrics and events are exported with the following resource attributes:
  * `service.name`: `claude-code`
  * `service.version`: Current Claude Code version
  * `os.type`: Operating system type (for example, `linux`, `darwin`, `windows`)
  * `os.version`: Operating system version string
  * `host.arch`: Host architecture (for example, `amd64`, `arm64`)
  * `wsl.version`: WSL version number (only present when running on Windows Subsystem for Linux)
  * Meter Name: `com.anthropic.claude_code`


## 
[​](https://code.claude.com/docs/en/monitoring-usage#roi-measurement-resources)
ROI measurement resources
For a comprehensive guide on measuring return on investment for Claude Code, including telemetry setup, cost analysis, productivity metrics, and automated reporting, see the [Claude Code ROI Measurement Guide](https://github.com/anthropics/claude-code-monitoring-guide). This repository provides ready-to-use Docker Compose configurations, Prometheus and OpenTelemetry setups, and templates for generating productivity reports integrated with tools like Linear.
## 
[​](https://code.claude.com/docs/en/monitoring-usage#security-and-privacy)
Security and privacy
  * OpenTelemetry export to your backend is opt-in and requires explicit configuration. For Anthropic’s separate operational telemetry and how to disable it, see [Data usage](https://code.claude.com/docs/en/data-usage#telemetry-services)
  * Raw file contents and code snippets are not included in metrics or events. Trace spans are a separate data path: see the `OTEL_LOG_TOOL_CONTENT` bullet below
  * When authenticated via OAuth, `user.email` is included in telemetry attributes. If this is a concern for your organization, work with your telemetry backend to filter or redact this field
  * User prompt content is not collected by default. Only prompt length is recorded. To include prompt content, set `OTEL_LOG_USER_PROMPTS=1`
  * Tool input arguments and parameters are not logged by default. To include them, set `OTEL_LOG_TOOL_DETAILS=1`. When enabled, `tool_result` events include a `tool_parameters` attribute with Bash commands, MCP server and tool names, and skill names, plus a `tool_input` attribute with file paths, URLs, search patterns, and other arguments. `user_prompt` events include the verbatim `command_name` for custom, plugin, and MCP commands. Trace spans include the same `tool_input` attribute and input-derived attributes such as `file_path`. Individual values over 512 characters are truncated and the total is bounded to ~4 K characters, but the arguments may still contain sensitive values. Configure your telemetry backend to filter or redact these attributes as needed
  * Tool input and output content is not logged in trace spans by default. To include it, set `OTEL_LOG_TOOL_CONTENT=1`. When enabled, span events include full tool input and output content truncated at 60 KB per span. This can include raw file contents from Read tool results and Bash command output. Configure your telemetry backend to filter or redact these attributes as needed
  * Raw Anthropic Messages API request and response bodies are not logged by default. To include them, set `OTEL_LOG_RAW_API_BODIES`. With `=1`, each API call emits `api_request_body` and `api_response_body` log events whose `body` attribute is the JSON-serialized payload, truncated at 60 KB. With `=file:<dir>`, untruncated bodies are written to `.request.json` and `.response.json` files under that directory and the events carry a `body_ref` path instead of the inline body. Ship the directory with a log collector or sidecar rather than through the telemetry stream. In both modes, bodies contain the full conversation history (system prompt, every prior user and assistant turn, tool results), so enabling this implies consent to everything the other `OTEL_LOG_*` content flags would reveal. Claude’s extended-thinking content is always redacted from these bodies regardless of other settings


## 
[​](https://code.claude.com/docs/en/monitoring-usage#monitor-claude-code-on-amazon-bedrock)
Monitor Claude Code on Amazon Bedrock
For detailed Claude Code usage monitoring guidance for Amazon Bedrock, see [Claude Code Monitoring Implementation (Bedrock)](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/MONITORING.md).
Was this page helpful?
YesNo
[Development containers](https://code.claude.com/docs/en/devcontainer)[Costs](https://code.claude.com/docs/en/costs)
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
[Privacy choices](https://code.claude.com/docs/en/monitoring-usage)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
