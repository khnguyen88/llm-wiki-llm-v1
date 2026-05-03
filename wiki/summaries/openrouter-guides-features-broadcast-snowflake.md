---
title: "Openrouter Guides Features Broadcast Snowflake"
summary: "OpenRouter Broadcast integration with Snowflake for streaming LLM traces to a cloud data warehouse for analytics, cost tracking, and business intelligence"
type: summary
sources:
  - raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md
tags:
  - openrouter
  - snowflake
  - broadcast
  - observability
  - analytics
  - sql
  - data-warehouse
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Broadcast Snowflake

## Key Points

- Snowflake is a Broadcast destination that streams OpenRouter traces directly to a Snowflake database for custom analytics, long-term storage, and business intelligence ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Setup requires five steps: creating the `OPENROUTER_TRACES` table, generating a Programmatic Access Token with `ACCOUNTADMIN` permissions, enabling Broadcast, configuring Snowflake connection details, and testing ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- The Snowflake account identifier is composed of the account number and region from the Snowflake URL (e.g., `eac52885.us-east-1`) ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Configuration defaults: database `SNOWFLAKE_LEARNING_DB`, schema `PUBLIC`, table `OPENROUTER_TRACES`, warehouse `COMPUTE_WH` ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- The schema uses typed columns for commonly-queried fields (identifiers, timestamps, model info, metrics) and VARIANT columns for variable-structure data (ATTRIBUTES, INPUT/OUTPUT, METADATA, MODEL_PARAMETERS) ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Custom metadata from the `trace` field is stored in the `METADATA` VARIANT column and queried using Snowflake's semi-structured data syntax (e.g., `METADATA:department::STRING`) ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Privacy Mode excludes prompt and completion content from traces while preserving all other data (token usage, costs, timing, model information, custom metadata) ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

## Quotes

- "Snowflake is a cloud data warehouse platform. OpenRouter can stream traces directly to your Snowflake database for custom analytics, long-term storage, and business intelligence." ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md:3]
- "This design balances query performance with schema flexibility and storage efficiency." ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md:119]
- "You can create materialized views on frequently queried metadata fields for better performance" ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md:144]

## Notes

- The source provides six example SQL queries: cost analysis by model, user activity analysis, error analysis, provider performance comparison, usage by API key, and VARIANT column access patterns
- The `trace` field supports four metadata keys in Snowflake: `trace_id` (also a typed column), `trace_name`, `span_name`, `generation_name`
- The `user` field maps to the `USER_ID` typed column and `session_id` maps to the `SESSION_ID` typed column

## Related

- [[entities/snowflake]]
- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/data_privacy]]
- [[concepts/observability]]