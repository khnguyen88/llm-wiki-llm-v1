---
title: "Snowflake"
summary: "A cloud data warehouse platform available as a Broadcast destination for streaming OpenRouter LLM traces"
type: entity
sources:
  - raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md
tags:
  - snowflake
  - data-warehouse
  - broadcast
  - analytics
  - sql
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Snowflake

A cloud data warehouse platform available as an [[concepts/broadcast|OpenRouter Broadcast]] destination for streaming LLM traces for custom analytics, long-term storage, and business intelligence. ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

## Key Facts

- Serves as a Broadcast destination in OpenRouter, receiving trace data in the `OPENROUTER_TRACES` table ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Requires a Programmatic Access Token with `ACCOUNTADMIN` permissions, created under Settings > Authentication in the Snowflake UI ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Account identifier is composed of the account number and region from the Snowflake URL (e.g., `eac52885.us-east-1` from `https://app.snowflake.com/us-east-1/eac52885`) ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Default configuration: database `SNOWFLAKE_LEARNING_DB`, schema `PUBLIC`, table `OPENROUTER_TRACES`, warehouse `COMPUTE_WH` ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Schema design uses typed columns for identifiers, timestamps, model info, and metrics alongside VARIANT columns for variable-structure data (ATTRIBUTES, INPUT/OUTPUT, METADATA, MODEL_PARAMETERS) ^[raw/document/openrouter/openrouter/064-guides-features-broadcast-snowflake-2026-04-29.md]
- Custom metadata from the `trace` field is stored in the `METADATA` VARIANT column and queried using Snowflake's semi-structured data syntax ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- Materialized views can be created on frequently queried metadata fields for better performance ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]
- The `OPENROUTER_TRACES` table creation SQL is provided in the OpenRouter dashboard during destination configuration ^[raw/document/openrouter/openrouter-064-guides-features-broadcast-snowflake-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/broadcast]]
- [[concepts/data_privacy]]