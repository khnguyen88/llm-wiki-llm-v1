---
title: "Observability"
summary: "The ability to monitor agent runs by exporting traces, metrics, and log events via OpenTelemetry to external backends for inspection and analysis"
type: concept
sources:
  - raw/document/claude code/claude-code-012-agent-sdk-observability-2026-04-29.md
tags:
  - observability
  - opentelemetry
  - tracing
  - metrics
  - agent-sdk
  - monitoring
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
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

## Related

- [[entities/open_telemetry]]
- [[entities/agent_sdk]]
- [[concepts/cost_tracking]]
- [[concepts/hooks]]
- [[concepts/agent_loop]]