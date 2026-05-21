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

- [[004-wiki/entities/openrouter|OpenRouter]] can stream traces directly to a [[004-wiki/entities/clickhouse|ClickHouse]] database for high-performance analytics and custom dashboards ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Setup requires creating an `OPENROUTER_TRACES` table (SQL provided in the OpenRouter dashboard), granting `CREATE TABLE` permissions, enabling Broadcast in Settings > Observability, and configuring the ClickHouse connection (host, database, table, username, password) ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- The schema uses typed columns (identifiers, timestamps, model info, metrics) for efficient filtering and aggregation, with JSON string columns (ATTRIBUTES, INPUT/OUTPUT, METADATA, MODEL_PARAMETERS) for variable-structure data ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- ClickHouse `JSONExtract*` functions are used to query nested fields in JSON columns, including custom metadata from the `trace` field ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Custom metadata from the `trace` field is stored in the `METADATA` column as a JSON string, with standard keys (`trace_id`, `trace_name`, `span_name`, `generation_name`) mapping to typed columns or JSON fields ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- The `user` and `session_id` request fields map to the `USER_ID` and `SESSION_ID` typed columns respectively ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- When [[004-wiki/concepts/data-privacy|Privacy Mode]] is enabled for a ClickHouse destination, prompt and completion content is excluded from traces while all other data (token usage, costs, timing, model information, custom metadata) is sent normally ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Quotes

> "For high-performance filtering on metadata fields, consider creating materialized columns with `ALTER TABLE ... ADD COLUMN`" ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

> "For ClickHouse Cloud, your host URL is typically `https://{instance}.{region}.clickhouse.cloud:8443`" ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Notes

- The configuration only saves if the Test Connection check passes ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Example queries in the source cover cost analysis by model, user activity analysis, error analysis, provider performance comparison, usage by API key, and JSON column querying ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- ClickHouse Cloud connection details are available under the Connect section of the ClickHouse Cloud console ^[001a-raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Related

- [[004-wiki/entities/openrouter]]
- [[004-wiki/entities/clickhouse]]
- [[004-wiki/concepts/broadcast]]
- [[004-wiki/concepts/data-privacy]]
- [[004-wiki/concepts/observability]]
- [[004-wiki/concepts/cost-tracking]]