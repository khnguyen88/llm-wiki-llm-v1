---
title: "ClickHouse"
summary: "A fast, open-source columnar database for real-time analytics, available as a Broadcast destination for OpenRouter LLM traces"
type: entity
sources:
  - raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md
tags:
  - clickhouse
  - database
  - analytics
  - openrouter
  - broadcast
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# ClickHouse

A fast, open-source columnar database for real-time analytics. [[entities/openrouter|OpenRouter]] can stream traces directly to ClickHouse for high-performance analytics and custom dashboards. ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Key Facts

- Self-hosted ClickHouse uses the HTTP endpoint on port 8123 (e.g., `https://clickhouse.example.com:8123`); ClickHouse Cloud uses port 8443 with the format `https://{instance}.{region}.clickhouse.cloud:8443` ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- The `OPENROUTER_TRACES` table must be created before connecting OpenRouter; the exact SQL is available in the OpenRouter dashboard during destination configuration ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Requires `CREATE TABLE` permissions on the target database: `GRANT CREATE TABLE ON your_database.* TO your_database_user` ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- The schema uses typed columns for commonly-queried fields (identifiers like TRACE_ID, USER_ID, SESSION_ID; timestamps as DateTime64 with millisecond precision; model info; token and cost metrics) and JSON string columns for variable-structure data (ATTRIBUTES, INPUT/OUTPUT, METADATA, MODEL_PARAMETERS) ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Nested JSON fields are queried using ClickHouse's `JSONExtract*` functions ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- Custom metadata from the `trace` field is stored in the `METADATA` JSON column; standard keys (`trace_id`, `trace_name`, `span_name`, `generation_name`) have dedicated mappings ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- For high-performance filtering on metadata fields, materialized columns can be created with `ALTER TABLE ... ADD COLUMN` ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]
- When [[concepts/data_privacy|Privacy Mode]] is enabled, prompt and completion content is excluded from traces while all other data continues to be sent ^[raw/document/openrouter/openrouter-052-guides-features-broadcast-clickhouse-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/data_privacy]]
- [[concepts/observability]]
- [[summaries/openrouter-guides-features-broadcast-clickhouse]]