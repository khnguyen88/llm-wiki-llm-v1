---
title: "Openrouter Guides Features Broadcast Clickhouse"
summary: "Guide for configuring OpenRouter Broadcast to stream LLM traces to a ClickHouse database, including table setup, permissions, schema design, and example queries"
type: summary
sources:
  - raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md
tags:
  - openrouter
  - clickhouse
  - broadcast
  - observability
  - analytics
  - sql
  - traces
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Clickhouse

## Key Points

- [[entities/openrouter|OpenRouter]] can stream traces directly to a [[entities/clickhouse|ClickHouse]] database for high-performance analytics and custom dashboards ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Setup requires creating an `OPENROUTER_TRACES` table (SQL provided in the OpenRouter dashboard), granting `CREATE TABLE` permissions, enabling Broadcast in Settings > Observability, and configuring the ClickHouse connection (host, database, table, username, password) ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- The schema uses typed columns (identifiers, timestamps, model info, metrics) for efficient filtering and aggregation, with JSON string columns (ATTRIBUTES, INPUT/OUTPUT, METADATA, MODEL_PARAMETERS) for variable-structure data ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- ClickHouse `JSONExtract*` functions are used to query nested fields in JSON columns, including custom metadata from the `trace` field ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Custom metadata from the `trace` field is stored in the `METADATA` column as a JSON string, with standard keys (`trace_id`, `trace_name`, `span_name`, `generation_name`) mapping to typed columns or JSON fields ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- The `user` and `session_id` request fields map to the `USER_ID` and `SESSION_ID` typed columns respectively ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- When [[concepts/data_privacy|Privacy Mode]] is enabled for a ClickHouse destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is sent normally ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Quotes

> "For high-performance filtering on metadata fields, consider creating materialized columns with `ALTER TABLE ... ADD COLUMN`" ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

> "For ClickHouse Cloud, your host URL is typically `https://{instance}.{region}.clickhouse.cloud:8443`" ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Notes

- The configuration only saves if the Test Connection check passes ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Example queries in the source cover cost analysis by model, user activity analysis, error analysis, provider performance comparison, usage by API key, and JSON column querying ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- ClickHouse Cloud connection details are available under the Connect section of the ClickHouse Cloud console ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[entities/clickhouse]]
- [[concepts/broadcast]]
- [[concepts/data_privacy]]
- [[concepts/observability]]
- [[concepts/cost_tracking]]