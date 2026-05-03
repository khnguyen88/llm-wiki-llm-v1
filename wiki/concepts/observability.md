---
title: "Observability"
summary: "The ability to monitor agent runs by exporting traces, metrics, and log events via OpenTelemetry to external backends for inspection and analysis"
type: concept
sources:
  - raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md
  - raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md
  - raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md
  - raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md
  - raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md
  - raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md
tags:
  - observability
  - opentelemetry
  - tracing
  - metrics
  - agent-sdk
  - monitoring
  - openrouter
  - input-output-logging
  - broadcast
  - grafana
  - traceql
  - wandb-weave
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Observability

The ability to monitor running agents by exporting structured telemetry — traces, metrics, and log events — via OpenTelemetry to external backends. In the Agent SDK, observability provides visibility into which tools were called, how long model requests took, how many tokens were spent, and where failures occurred. ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

## Key Points

- The CLI subprocess (not the SDK) produces all telemetry; the SDK passes configuration to the child process via environment variables ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Environment variables can be set in the process environment (recommended for production) or per-call via `ClaudeAgentOptions.env` (Python) / `options.env` (TypeScript) ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Three independent signals: metrics (tokens, cost, sessions, lines of code, tool decisions), log events (prompt, API request, API error, tool result records), traces (interaction, model request, tool call, and hook spans) ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Telemetry is off by default; requires `CLAUDE_CODE_ENABLE_TELEMETRY=1` and at least one exporter ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Trace spans carry a `session.id` attribute by default; filter on it in the backend to see multiple `query()` calls against the same session as one timeline ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]
- Sensitive data is excluded by default; four opt-in variables control what content is added to exports ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

## Details

The Agent SDK's observability architecture relies on the fact that `query()` spawns the Claude Code CLI as a child process communicating over a local pipe. The CLI has OpenTelemetry instrumentation built in, recording spans around each model request and tool execution, emitting metric counters for tokens and cost, and emitting structured log events for prompts and tool results. Configuration flows as environment variables: the child process inherits the application's environment by default, or per-call variables can be set via `ClaudeAgentOptions.env`. ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

Traces provide the most detailed view of an agent run. Four span types form a hierarchy: `claude_code.interaction` wraps a full agent turn; `claude_code.llm_request` wraps each API call; `claude_code.tool` wraps each tool invocation (with child spans `claude_code.tool.blocked_on_user` for permission waits and `claude_code.tool.execution` for execution); and `claude_code.hook` wraps hook execution. When the agent spawns a subagent via the Task tool, the subagent's spans nest under the parent's `claude_code.tool` span, preserving the full delegation chain as one trace. ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

The SDK automatically propagates W3C trace context into the CLI subprocess. When `query()` is called while an OpenTelemetry span is active in the parent application, `TRACEPARENT` and `TRACESTATE` are injected into the child process environment, making the agent's `claude_code.interaction` span a child of the application's span. The CLI also forwards `TRACEPARENT` to every Bash and PowerShell command it runs, so commands emitting their own spans nest correctly. Auto-injection is skipped when `TRACEPARENT` is set explicitly in `options.env`. ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

For short-lived processes, the CLI's default batching intervals (60s for metrics, 5s for traces and logs) can cause data loss if the process exits before flushing. Reducing export intervals via `OTEL_METRIC_EXPORT_INTERVAL`, `OTEL_LOGS_EXPORT_INTERVAL`, and `OTEL_TRACES_EXPORT_INTERVAL` ensures data reaches the collector while the task is still running. Content your agent reads and writes is not recorded by default; four opt-in environment variables (`OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_RAW_API_BODIES`) progressively add more content to exports, with `OTEL_LOG_RAW_API_BODIES` implying consent to everything the other three would reveal. ^[raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md]

### Observability in OpenRouter Workspaces

In OpenRouter [[concepts/workspaces|Workspaces]], observability integrations can be configured independently per workspace, allowing different teams or projects to send traces to different backends. Alternatively, traces from all workspaces can be sent to the same observability platform for centralized monitoring. ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

### OpenRouter Input & Output Logging and Broadcast

OpenRouter provides two observability features configured in workspace Observability settings: [[concepts/input_output_logging|Input & Output Logging]] privately stores full request/response content on OpenRouter for debugging and prompt optimization, while [[concepts/broadcast|Broadcast]] sends data to external observability platforms for production monitoring and analytics. Both can be used together for comprehensive observability. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

Broadcast supports 17 stable destinations (including Langfuse, Datadog, Grafana Cloud, and an OpenTelemetry Collector), per-destination API key filtering and sampling rates, and Privacy Mode that strips prompt/completion content while preserving metrics. The `trace` field accepts arbitrary JSON metadata with standard keys (`trace_id`, `trace_name`, `span_name`, `generation_name`, `parent_span_id`) for hierarchical trace structure, enabling integration with existing tracing systems via `parent_span_id`. ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md] Datadog LLM Observability is one such destination, mapping `trace` keys to Datadog trace/span fields and auto-adding `service` and `user_id` tags. ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

Grafana Cloud is another Broadcast destination, receiving traces via the OTLP HTTP/JSON endpoint into Grafana Tempo. Traces use OpenTelemetry GenAI semantic conventions (`gen_ai.*` attributes) and can be queried with [[concepts/traceql|TraceQL]] in Grafana's Explore view. Custom metadata from the `trace` field appears under the `trace.metadata.*` namespace in span attributes. ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Related

- [[entities/open_telemetry]]
- [[entities/agent_sdk]]
- [[entities/openrouter]]
- [[concepts/workspaces]]
- [[concepts/cost_tracking]]
- [[concepts/hooks]]
- [[concepts/agent_loop]]
- [[concepts/input_output_logging]]
- [[concepts/broadcast]]
- [[entities/grafana_cloud]]
- [[concepts/traceql]]
- [[entities/wandb_weave]]