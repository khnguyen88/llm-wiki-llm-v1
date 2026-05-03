---
title: "Axiom"
summary: "A cloud-native observability platform for log and trace management that supports OTLP ingestion, available as an OpenRouter Broadcast destination"
type: entity
sources:
  - raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md
tags:
  - axiom
  - observability
  - tracing
  - otlp
  - broadcast
  - openrouter
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Axiom

A cloud-native log and trace management platform that accepts traces via the OpenTelemetry Protocol (OTLP), listed as a compatible backend for OpenRouter's Broadcast feature. ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

## Key Facts

- Listed as a compatible OTLP backend for OpenRouter's OpenTelemetry Collector Broadcast destination ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- Requires an Axiom account and dataset, with an API token created via Settings > API Tokens ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- OTLP traces endpoint: `https://api.axiom.co/v1/traces` ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]
- Authentication headers required: `Authorization: Bearer xaat-xxx` (API token) and `X-Axiom-Dataset: your-dataset` (dataset name) ^[raw/document/openrouter/openrouter-059-guides-features-broadcast-otel-collector-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[entities/open_telemetry]]
- [[summaries/openrouter-guides-features-broadcast-otel-collector]]