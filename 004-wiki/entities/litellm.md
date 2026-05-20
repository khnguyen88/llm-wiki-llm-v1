---
title: "LiteLLM"
summary: "Open-source tool used to track Claude Code spend by API key on Bedrock, Vertex, and Foundry deployments where native cost metrics are unavailable"
type: entity
sources:
  - raw/document/claude code/claude-code-052-costs-2026-04-29.md
tags:
  - litellm
  - cost-tracking
  - deployment
  - open-source
  - bedrock
  - vertex
  - foundry
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.8
provenance: extracted
---

# LiteLLM

An open-source tool that helps organizations track spend by API key on cloud-hosted Claude Code deployments. On Bedrock, Vertex, and Foundry, Claude Code does not send metrics from the cloud, so cost tracking requires an external solution. Several large enterprises have reported using LiteLLM for this purpose. ^[001a-raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Key Facts

- LiteLLM is used to track spend by key on Bedrock, Vertex, and Foundry deployments where native cost metrics are unavailable ^[001a-raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- The project is unaffiliated with Anthropic and has not been audited for security ^[001a-raw/document/claude code/claude-code-052-costs-2026-04-29.md]
- LiteLLM can be configured as an LLM gateway for Claude Code ^[001a-raw/document/claude code/claude-code-052-costs-2026-04-29.md]

## Related

- [[004-wiki/entities/amazon_bedrock]]
- [[004-wiki/entities/google_vertex_ai]]
- [[004-wiki/entities/microsoft_foundry]]
- [[004-wiki/concepts/cost_tracking]]
- [[004-wiki/concepts/deployment_patterns]]
- [[004-wiki/summaries/claude-code-costs]]