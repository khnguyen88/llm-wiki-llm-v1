---
title: "Grafana Cloud"
summary: "A fully-managed observability platform by Grafana Labs that includes Grafana Tempo for distributed tracing and receives OpenRouter Broadcast traces via OTLP"
type: entity
sources:
  - raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md
tags:
  - grafana
  - observability
  - tracing
  - otlp
  - tempo
  - broadcast
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Grafana Cloud

A fully-managed observability platform by Grafana Labs that includes Grafana Tempo for distributed tracing and serves as a Broadcast destination for OpenRouter. ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Key Facts

- Receives OpenRouter traces via the standard OTLP HTTP/JSON endpoint ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Configuration requires three credentials: OTLP base URL (`https://otlp-gateway-prod-{region}.grafana.net`), numeric Instance ID, and API key with `traces:write` scope (prefixed `glc_...`) ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- The OTLP endpoint URL is found at Connections > Add new connection > OpenTelemetry (OTLP) in the Grafana Cloud portal, distinct from the main Grafana dashboard URL ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Instance ID is found at `https://grafana.com/orgs/{org}/stacks` by selecting the stack and reading the numeric value from the URL or stack details ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- API tokens are created under Access Policies with `traces:write` scope ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Traces can be viewed via Explore with TraceQL or via Drilldown > Traces in the left sidebar ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- The Tempo data source is typically named `grafanacloud-{stack}-traces` ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]
- Traces may take 1-2 minutes to appear after being sent ^[001a-raw/document/openrouter/openrouter-055-guides-features-broadcast-grafana-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/entities/open_telemetry]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/concepts/traceql]]