---
title: "Broadcast"
summary: "An OpenRouter feature that sends request and response traces to external observability platforms with per-destination filtering, sampling, and privacy controls"
type: concept
sources:
  - raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md
  - raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md
  - raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md
  - raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md
  - raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md
  - raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md
  - raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md
  - raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md
  - raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md
  - raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md
  - raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md
  - raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md
  - raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md
  - raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md
  - raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md
  - raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md
  - raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md
  - raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md
tags:
  - openrouter
  - observability
  - monitoring
  - analytics
  - tracing
  - privacy
  - sampling
  - clickhouse
  - datadog
  - grafana
  - langfuse
  - langsmith
  - traceql
  - otlp
  - newrelic
  - axiom
  - jaeger
  - honeycomb
  - lightstep
  - posthog
  - ramp
  - s3
  - sentry
  - snowflake
  - cloudflare-r2
  - wandb-weave
  - webhook
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Broadcast

An OpenRouter feature that sends LLM request and response trace data to external observability platforms, configured in the workspace's Observability settings. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

## Key Points

- Data is stored on the user's external platform rather than on OpenRouter ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Setup requires configuring destinations and credentials, unlike [[concepts/input_output_logging|Input & Output Logging]] which uses a single toggle ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- Primary use case is production monitoring and analytics, complementing Input & Output Logging's debugging and prompt optimization focus ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]
- 17 stable destinations are available including Langfuse, Datadog, Grafana Cloud, ClickHouse, Snowflake, S3, and a generic Webhook endpoint ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Each destination can be filtered by API key and configured with an independent sampling rate; sampling is deterministic per `session_id` so complete sessions stay intact ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Privacy Mode per destination strips prompt and completion content while preserving token counts, costs, timing, and metadata ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]
- Destination credentials are encrypted at rest and traces are sent asynchronously, adding no latency to API responses ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

## Details

Broadcast and [[concepts/input_output_logging|Input & Output Logging]] can be used together for comprehensive observability. Both are configured in the workspace's Observability settings. Broadcast is suited for ongoing production monitoring with external tooling, while Input & Output Logging is suited for ad-hoc debugging and prompt evaluation directly on the OpenRouter platform. ^[raw/document/openrouter/openrouter-048-guides-features-input-output-logging-2026-04-29.md]

### Trace Data

Each broadcast trace includes request/response data (with multimodal content stripped), token usage, cost information, timing metrics, model information, and tool usage metadata. Three optional enrichment fields can be included in API requests: `user` (associates traces with end-users, up to 128 characters), `session_id` (groups related requests, also passable via `x-session-id` header, up to 128 characters), and `trace` (arbitrary JSON metadata passed through to all destinations). ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

The `trace` field supports standard keys for hierarchical trace structure: `trace_id` (groups requests into a single trace), `trace_name` (custom name for the root trace), `span_name` (parent span for grouping LLM operations), `generation_name` (name for the specific LLM call), and `parent_span_id` (links to an external tracing span, e.g., OpenTelemetry). ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

### API Key Filtering and Sampling

Each destination can be configured to receive traces only from specific API keys. If no keys are selected, the destination receives traces from all API keys. Each destination also has a configurable sampling rate (0.0–1.0) controlling what percentage of traces are sent; a rate of 1.0 sends all traces while 0.5 sends approximately 50%. Sampling is deterministic per `session_id`, ensuring complete sessions appear together in observability platforms. ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

### Organization Support

Broadcast can be configured at both individual and organization levels. Organization admins can set up shared destinations that apply to all API keys within the organization, ensuring consistent observability across teams. ^[raw/document/openrouter/openrouter-049-guides-features-broadcast-overview-2026-04-29.md]

### Arize AI Destination

[[entities/arize_ai|Arize AI]] is one of the 17 stable Broadcast destinations. It uses the [[entities/openinference|OpenInference]] semantic convention for tracing, mapping custom metadata from the `trace` field as span attributes in the OTLP payload. Configuration requires an API Key, Space Key, Model ID, and an optional Base URL (default `https://otlp.arize.com`). The Test Connection button validates credentials before saving. ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

For Arize specifically, the five standard `trace` keys map to dedicated fields: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID. Arbitrary metadata keys map to the `metadata.*` namespace. The `user` and `session_id` request fields map to user identification and session tracking span attributes respectively. ^[raw/document/openrouter/openrouter-050-guides-features-broadcast-arize-2026-04-29.md]

### Braintrust Destination

[[entities/braintrust|Braintrust]] is an end-to-end platform for evaluating, monitoring, and improving LLM applications, available as a Broadcast destination. Configuration requires a Braintrust API key (from Account Settings), a Project ID (from project settings), and an optional Base URL (default `https://api.braintrust.dev`). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]

Braintrust maps four metadata keys from the `trace` field: `trace_id` → Span ID / Root Span ID (groups logs into a single trace), `trace_name` → Name (display name in log view), `span_name` → Name (intermediate span name), `generation_name` → Name (LLM span name). The `user` field maps to `user_id` and `session_id` maps to `session_id` in Braintrust metadata. Custom metadata keys are included in the span's metadata object, and tags are passed through for UI filtering. ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]

Braintrust receives detailed per-call metrics: token counts (prompt, completion, total), cached token usage, reasoning token counts for supported models, cost information (input, output, total), and duration/timing metrics. When [[concepts/data_privacy|Privacy Mode]] is enabled for the Braintrust destination, prompt and completion content is excluded from traces while all other data continues to be sent normally. ^[raw/document/openrouter/openrouter-051-guides-features-broadcast-braintrust-2026-04-29.md]

### ClickHouse Destination

[[entities/clickhouse|ClickHouse]] is a fast, open-source columnar database for real-time analytics, available as a Broadcast destination. Setup requires creating the `OPENROUTER_TRACES` table (SQL provided in the dashboard), granting `CREATE TABLE` permissions, enabling Broadcast in Settings > Observability, and configuring the ClickHouse connection (host, database, table, username, password). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

The ClickHouse schema uses typed columns for commonly-queried fields (identifiers like TRACE_ID, USER_ID, SESSION_ID; timestamps as DateTime64 with millisecond precision; model info; token and cost metrics) and JSON string columns for variable-structure data (ATTRIBUTES, INPUT/OUTPUT, METADATA, MODEL_PARAMETERS). Nested JSON fields are queried using `JSONExtract*` functions. For high-performance metadata filtering, materialized columns can be added with `ALTER TABLE ... ADD COLUMN`. ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

Custom metadata from the `trace` field maps as follows: `trace_id` → TRACE_ID column and METADATA JSON, `trace_name` → METADATA JSON, `span_name` → METADATA JSON, `generation_name` → METADATA JSON. The `user` field maps to `USER_ID` and `session_id` maps to `SESSION_ID`. ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the ClickHouse destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is sent normally. ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

### Comet Opik Destination

[[entities/comet_opik|Comet Opik]] is an open-source platform for evaluating, testing, and monitoring LLM applications, available as a Broadcast destination. Configuration requires a Comet API key (prefix `opik_...`), workspace name, and project name, entered in Settings > Observability after enabling Broadcast. The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

Opik maps four metadata keys from the `trace` field: `trace_id` → trace metadata (`openrouter_trace_id`), `trace_name` → Trace Name, `span_name` → Span Name, `generation_name` → Span Name. Custom metadata keys from the `trace` field are included in both trace and span metadata objects. Cost information (input, output, total) is automatically added to span metadata, and model parameters and finish reasons are included when available. Opik uses UUIDv7 format for trace and span IDs internally; original OpenRouter IDs are stored as `openrouter_trace_id` and `openrouter_observation_id` in metadata. The `user` field maps to user identification in trace metadata. ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Opik destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-053-guides-features-broadcast-opik-2026-04-29.md]

### Datadog Destination

[[entities/datadog|Datadog]] LLM Observability is a Broadcast destination for investigating root causes, monitoring operational performance, and evaluating LLM application quality, privacy, and safety. Configuration requires a Datadog API key (from Organization Settings > API Keys), an ML App name, and an optional URL override (default `https://api.us5.datadoghq.com`). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

Datadog maps four metadata keys from the `trace` field: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name. Two tags are automatically added: `service:{ml_app}` (from the configured ML App name) and `user_id:{user}` (from the request `user` field). Any additional keys in the `trace` object are passed to the span's `meta` object and viewable in Datadog's trace details. ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Datadog destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-054-guides-features-broadcast-datadog-2026-04-29.md]

### Grafana Cloud Destination

[[entities/grafana_cloud|Grafana Cloud]] is a fully-managed observability platform that includes Grafana Tempo for distributed tracing, available as a Broadcast destination. It receives traces via the standard OTLP HTTP/JSON endpoint. Configuration requires three values: an OTLP base URL (e.g., `https://otlp-gateway-prod-us-west-0.grafana.net`), a numeric Instance ID, and an API key with `traces:write` scope (prefixed `glc_...`). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

OpenRouter traces include resource attributes (`service.name: openrouter`, `service.version: 1.0.0`, `openrouter.trace.id`) and span attributes following OpenTelemetry GenAI semantic conventions (`gen_ai.operation.name`, `gen_ai.system`, `gen_ai.request.model`, `gen_ai.response.model`, token usage counts, `gen_ai.response.finish_reason`). Custom metadata from the `trace` field maps to `trace.metadata.*` span attributes; the `user` field maps to `user.id` and `session_id` maps to `session.id`. ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

Grafana Cloud maps five standard `trace` keys: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID. Traces can be viewed via Explore with [[concepts/traceql|TraceQL]] (using `{ resource.service.name = "openrouter" }` as a base query) or via Drilldown > Traces with attribute-based filtering. ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Grafana Cloud destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

### Langfuse Destination

[[entities/langfuse|Langfuse]] is an open-source LLM engineering platform for tracing, evaluating, and debugging, available as a Broadcast destination. Configuration requires a Secret Key and Public Key (created in Langfuse project Settings > API Keys) and an optional Base URL (default `https://us.cloud.langfuse.com`, changeable for other regions or self-hosted instances). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]

Langfuse maps five standard `trace` keys to its hierarchy: `trace_id` → Trace ID (groups requests into a single trace), `trace_name` → Trace Name, `span_name` → Span Name (intermediate spans), `generation_name` → Generation Name (LLM generation observation), `parent_span_id` → Parent Observation ID (links to existing spans). The `user` field maps to Langfuse's User ID for user-level analytics, and `session_id` maps to Session ID for grouping conversations. Additional keys in the `trace` object are passed as trace metadata for filtering and analysis. ^[raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Langfuse destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-056-guides-features-broadcast-langfuse-2026-04-29.md]

### LangSmith Destination

[[entities/langsmith|LangSmith]] is LangChain's platform for debugging, testing, evaluating, and monitoring LLM applications, available as a Broadcast destination. Configuration requires a LangSmith API key (prefix `lsv2_pt_...`, created in Settings > API Keys), a project name, and an optional endpoint (default `https://api.smith.langchain.com`, changeable for self-hosted instances). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

LangSmith receives trace data via the [[entities/open_telemetry|OpenTelemetry]] protocol at the `/otel/v1/traces` endpoint. Traces include GenAI semantic conventions (model name, token counts, costs, request parameters), LangSmith-specific attributes (trace name, span kind, user ID, custom metadata), and error events with exception types and messages. ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

LangSmith maps five standard `trace` keys: `trace_id` → Trace ID, `trace_name` → Run Name, `span_name` → Run Name, `generation_name` → Run Name, `parent_span_id` → Parent Run ID. Observation types map to LangSmith run types: GENERATION → `llm`, SPAN → `chain`, EVENT → `tool`. The `user` field maps to LangSmith User ID and `session_id` maps to Session ID for conversation tracking. Custom metadata keys are passed as span attributes; string arrays become comma-separated tags. ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the LangSmith destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-057-guides-features-broadcast-langsmith-2026-04-29.md]

### New Relic Destination

[[entities/new_relic|New Relic]] is a full-stack observability platform for monitoring applications, infrastructure, and digital experiences, available as a Broadcast destination. New Relic receives traces via the [[entities/open_telemetry|OTLP]] protocol. Configuration requires a New Relic Ingest License Key (from API Keys in account settings) and a region selection (`us` or `eu`), entered in Settings > Observability after enabling Broadcast. The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

New Relic maps five standard `trace` metadata keys: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID. Custom metadata keys from the `trace` field are included as span attributes under the `trace.metadata.*` namespace. The `user` field maps to `user.id` and `session_id` maps to `session.id`. GenAI semantic conventions (`gen_ai.*` attributes) are used for model, token, and cost data. ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

In New Relic's distributed tracing view, traces can be filtered by custom attributes using NRQL queries, custom metadata can be viewed in the span attributes panel, and alerts and dashboards can be created based on metadata fields. ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the New Relic destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-058-guides-features-broadcast-newrelic-2026-04-29.md]

### OpenTelemetry Collector Destination

OpenRouter Broadcast supports an [[entities/open_telemetry|OpenTelemetry]] Collector destination that sends traces to any backend supporting OTLP over HTTP, including [[entities/axiom|Axiom]], Jaeger, Grafana Tempo, Honeycomb, Lightstep, and self-hosted collectors. Traces are sent using OTLP/HTTP protocol with JSON encoding on the `/v1/traces` path. ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

Configuration requires enabling Broadcast in Settings > Observability, then adding an OpenTelemetry Collector destination with an endpoint URL (e.g., `https://api.axiom.co/v1/traces` for Axiom or `https://your-collector.example.com:4318/v1/traces` for self-hosted) and optional authentication headers as a JSON object. The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

Custom metadata from the `trace` field maps to five standard OTLP keys: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID. Arbitrary metadata keys are included as span attributes under the `trace.metadata.*` namespace. The `user` field maps to `user.id` and `session_id` maps to `session.id`. Standard GenAI semantic conventions (`gen_ai.*`) are used for model, token usage, and cost attributes. ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the OpenTelemetry Collector destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) continues to be sent normally. ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

### PostHog Destination

[[entities/posthog|PostHog]] is an open-source product analytics platform with LLM analytics capabilities, available as a Broadcast destination. Configuration requires a PostHog project API key (prefix `phc_...`) and an optional endpoint override — the default is `https://us.i.posthog.com`, with `https://eu.i.posthog.com` for the EU region. The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]

PostHog maps three standard `trace` keys to event properties: `trace_id`, `trace_name`, and `generation_name`. The `user` field maps to PostHog's `$ai_user` property for user-level LLM analytics, and `session_id` maps to `$ai_session_id` for session grouping. Custom metadata keys from the `trace` field are included as properties on the LLM analytics event. PostHog's LLM analytics dashboard automatically tracks token usage, costs, and model performance. ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the PostHog destination, the `$ai_input` and `$ai_output_choices` properties are excluded from events while all other analytics data (token usage, costs, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-060-guides-features-broadcast-posthog-2026-04-29.md]

### Ramp Destination

[[entities/ramp|Ramp]] is a finance automation platform that helps businesses manage expenses, track spending, and optimize costs. It is available as a Broadcast destination for monitoring and controlling LLM spending through OpenRouter. Configuration requires a Ramp API key (generated in Ramp's Settings > Integrations by searching for "OpenRouter"), an optional Base URL (default `https://api.ramp.com/developer/v1/ai-usage/openrouter`), and optional custom HTTP headers as a JSON object. The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]

Ramp receives traces via the [[entities/open_telemetry|OpenTelemetry Protocol (OTLP)]]. Each trace includes token usage (prompt, completion, total), cost information, timing (start, end, latency), model information (slug and provider name), and request/response content. Five standard `trace` keys map to OTLP span attributes: `trace_id` → Trace ID, `trace_name` → Span Name, `span_name` → Span Name, `generation_name` → Span Name, `parent_span_id` → Parent Span ID. The `user` field maps to `user.id`, `session_id` maps to `session.id`, and custom metadata keys map to the `trace.metadata.*` namespace. Standard GenAI semantic conventions (`gen_ai.*`) are used for model, token usage, and cost attributes. ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Ramp destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-061-guides-features-broadcast-ramp-2026-04-29.md]

### S3 / S3-Compatible Destination

[[entities/amazon_s3|Amazon S3]] is a scalable object storage service supported as a Broadcast destination. OpenRouter can send traces to any S3-compatible storage, including AWS S3, [[entities/cloudflare_r2|Cloudflare R2]], MinIO, and other compatible services. ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

Setup requires creating an S3 bucket with write credentials, enabling Broadcast in Settings > Observability, and configuring the S3 destination. For AWS S3, this means creating an IAM user with `s3:PutObject` permissions on the bucket. For Cloudflare R2, this means creating an R2 bucket and generating an API token with write permissions, plus specifying the custom endpoint URL (e.g., `https://your-account-id.r2.cloudflarestorage.com`). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

Configuration fields include: Bucket Name, Region (optional, auto-detected for AWS S3), Custom Endpoint (optional, for S3-compatible services), Access Key ID, Secret Access Key, Session Token (optional, for temporary credentials), and Path Template (default `openrouter-traces/{date}`). Each trace is saved as a separate JSON file with the format `{traceId}-{timestamp}.json`. ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

Path templates support variables `{prefix}`, `{date}`, `{year}`, `{month}`, `{day}`, and `{apiKeyName}` for organizing traces. Examples: `traces/{year}/{month}/{day}` for hierarchical date structure, `{apiKeyName}/{date}` for organization by API key name, or `production/llm-traces/{date}` for environment separation. ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

Custom metadata from the `trace` field maps to four supported keys in S3 trace files: `trace_id` → trace-level `id`, `trace_name` → trace-level `name`, `span_name` → observation-level `name`, `generation_name` → observation-level `name`. The `user` field maps to `userId` and `session_id` maps to `sessionId` in the trace JSON. Trace files include full input/output messages, token counts, costs, and timing data alongside custom metadata. S3 trace files can be queried using JSON-aware engines like Amazon Athena or Presto. ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the S3 destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-062-guides-features-broadcast-s3-2026-04-29.md]

### Sentry Destination

[[entities/sentry|Sentry]] is an application monitoring platform that helps developers identify and fix issues in real-time, available as a Broadcast destination with AI monitoring capabilities for tracking LLM performance and errors. Sentry receives traces via the [[entities/open_telemetry|OpenTelemetry Protocol (OTLP)]], requiring both an OTLP Traces Endpoint URL and a DSN for authentication and trace routing. ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

Setup requires: (1) obtaining the OTLP Traces Endpoint URL and DSN from Sentry's project SDK setup (Settings > Projects > [Project] > SDK Setup > Client Keys > OpenTelemetry tab), (2) enabling Broadcast in OpenRouter Settings > Observability, (3) configuring Sentry with the endpoint URL (format: `https://o{org_id}.ingest.us.sentry.io/api/{project_id}/integration/otlp/v1/traces`) and DSN (format: `https://{key}@o{org_id}.ingest.us.sentry.io/{project_id}`), and (4) testing and saving the connection. The configuration only saves if the test passes. ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

Sentry maps five standard `trace` metadata keys: `trace_id` → Trace ID (groups multiple requests into a single trace), `trace_name` → Transaction Name (custom name for the root span), `span_name` → Span Description (name for intermediate spans), `generation_name` → Span Description (name for the LLM generation span), `parent_span_id` → Parent Span ID (links to an existing span in the trace hierarchy). Custom metadata keys from the `trace` field are included as span attributes under the `trace.metadata.*` namespace. The `user` field maps to `user.id` and `session_id` maps to `session.id` in span attributes. ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

Sentry automatically correlates LLM traces with existing application error and performance data when `parent_span_id` is provided, enabling cross-referencing between LLM calls and application errors. Traces can be viewed in Sentry's Performance or Traces view. ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Sentry destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-063-guides-features-broadcast-sentry-2026-04-29.md]

### Snowflake Destination

[[entities/snowflake|Snowflake]] is a cloud data warehouse platform available as a Broadcast destination for streaming LLM traces for custom analytics, long-term storage, and business intelligence. Setup requires: (1) creating the `OPENROUTER_TRACES` table (SQL provided in the OpenRouter dashboard), (2) generating a Programmatic Access Token with `ACCOUNTADMIN` permissions in Snowflake's Settings > Authentication, (3) enabling Broadcast in OpenRouter Settings > Observability, (4) configuring the Snowflake connection (account identifier, token, database, schema, table, warehouse), and (5) testing and saving. The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

The account identifier is composed of the account number and region from the Snowflake URL (e.g., `eac52885.us-east-1` from `https://app.snowflake.com/us-east-1/eac52885`). Default configuration values: database `SNOWFLAKE_LEARNING_DB`, schema `PUBLIC`, table `OPENROUTER_TRACES`, warehouse `COMPUTE_WH`. ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

The Snowflake schema uses typed columns for commonly-queried fields (identifiers like TRACE_ID, USER_ID, SESSION_ID; timestamps; model info; token and cost metrics) and VARIANT columns for variable-structure data (ATTRIBUTES, INPUT/OUTPUT, METADATA, MODEL_PARAMETERS). This design balances query performance with schema flexibility and storage efficiency. VARIANT columns are queried using Snowflake's semi-structured data syntax (e.g., `METADATA:department::STRING`, `INPUT:messages[0]:role::STRING`). ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

Custom metadata from the `trace` field maps as follows: `trace_id` → TRACE_ID column and METADATA VARIANT, `trace_name` → METADATA VARIANT, `span_name` → METADATA VARIANT, `generation_name` → METADATA VARIANT. The `user` field maps to the USER_ID typed column and `session_id` maps to the SESSION_ID typed column. Materialized views can be created on frequently queried metadata fields for better performance. ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Snowflake destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

### W&B Weave Destination

[[entities/wandb_weave|W&B Weave]] is an observability platform by Weights & Biases for tracking and evaluating LLM applications, available as a Broadcast destination. Configuration requires a W&B API key (from W&B User Settings), an Entity (W&B username or team name), a Project name, and an optional Base URL (default `https://trace.wandb.ai`). The configuration only saves if the Test Connection check passes. ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

W&B Weave supports three custom metadata keys from the `trace` field: `trace_id` maps to the `openrouter_trace_id` attribute, `trace_name` maps to `op_name`, and `generation_name` maps to `op_name`. The `user` field maps to `user_id` and `session_id` maps to `session_id` in attributes. Custom metadata keys from the `trace` field are merged into the call's attributes. Model parameters (`temperature`, `max_tokens`, `top_p`) are included in inputs for easy filtering. ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

Weave organizes trace data into three categories: **Attributes** (metadata about the call — user IDs, organization IDs, trace identifiers, custom metadata), **Inputs** (actual request data including messages and model parameters), and **Summary** (token usage, costs, and timing metrics). ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the W&B Weave destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-065-guides-features-broadcast-weave-2026-04-29.md]

### Webhook Destination

The Webhook destination sends traces to any HTTP endpoint that can receive JSON payloads. Traces are delivered in [[entities/open_telemetry|OpenTelemetry Protocol (OTLP)]] JSON format, making them compatible with any OTLP-aware system. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

Setup requires enabling Broadcast in Settings > Observability, then configuring the Webhook destination with a URL (e.g., `https://api.example.com/traces`), an optional HTTP method (`POST` default or `PUT`), and optional custom headers as a JSON object for authentication (e.g., `Authorization: Bearer your-token`). The Test Connection sends an empty OTLP payload with an `X-Test-Connection: true` header; the test passes if the endpoint returns a 2xx or 400 status code. The configuration only saves if the test passes. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

The OTLP JSON payload contains a `resourceSpans` array with span data including trace and span IDs, timestamps and duration, model and provider information, token usage and cost, and request/response content (with multimodal content stripped). Five standard `trace` keys map to OTLP fields: `trace_id` → `traceId`, `trace_name` → Span `name`, `span_name` → Span `name`, `generation_name` → Span `name`, `parent_span_id` → `parentSpanId`. Arbitrary metadata keys appear as span attributes under the `trace.metadata.*` namespace. The `user` field maps to `user.id` and `session_id` maps to `session.id`. All standard GenAI semantic conventions (`gen_ai.*`) are included for model, token, and cost data. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

Use cases for the Webhook destination include custom analytics pipelines, internal monitoring tools, event-driven architectures, compliance logging, and development/testing. For production use, the endpoint should be highly available with retry logic for failed deliveries. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

When [[concepts/data_privacy|Privacy Mode]] is enabled for the Webhook destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is still sent normally. ^[raw/document/openrouter/openrouter-066-guides-features-broadcast-webhook-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/input_output_logging]]
- [[concepts/observability]]
- [[concepts/data_privacy]]
- [[entities/open_telemetry]]
- [[entities/arize_ai]]
- [[entities/openinference]]
- [[summaries/openrouter-guides-features-broadcast-arize]]
- [[entities/braintrust]]
- [[summaries/openrouter-guides-features-broadcast-braintrust]]
- [[entities/clickhouse]]
- [[summaries/openrouter-guides-features-broadcast-clickhouse]]
- [[entities/comet_opik]]
- [[summaries/openrouter-guides-features-broadcast-opik]]
- [[entities/datadog]]
- [[summaries/openrouter-guides-features-broadcast-datadog]]
- [[entities/grafana_cloud]]
- [[concepts/traceql]]
- [[summaries/openrouter-guides-features-broadcast-grafana]]
- [[entities/langfuse]]
- [[summaries/openrouter-guides-features-broadcast-langfuse]]
- [[entities/langsmith]]
- [[summaries/openrouter-guides-features-broadcast-langsmith]]
- [[entities/new_relic]]
- [[summaries/openrouter-guides-features-broadcast-newrelic]]
- [[entities/axiom]]
- [[summaries/openrouter-guides-features-broadcast-otel-collector]]
- [[entities/posthog]]
- [[summaries/openrouter-guides-features-broadcast-posthog]]
- [[entities/ramp]]
- [[summaries/openrouter-guides-features-broadcast-ramp]]
- [[entities/amazon_s3]]
- [[entities/cloudflare_r2]]
- [[summaries/openrouter-guides-features-broadcast-s3]]
- [[entities/sentry]]
- [[summaries/openrouter-guides-features-broadcast-sentry]]
- [[entities/snowflake]]
- [[summaries/openrouter-guides-features-broadcast-snowflake]]
- [[entities/wandb_weave]]
- [[summaries/openrouter-guides-features-broadcast-weave]]
- [[concepts/webhook]]
- [[summaries/openrouter-guides-features-broadcast-webhook]]