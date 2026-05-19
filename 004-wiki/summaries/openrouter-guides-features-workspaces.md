---
title: "Openrouter Guides Features Workspaces"
summary: "OpenRouter Workspaces let you organize projects into separate environments with independent API keys, routing defaults, guardrails, and observability under a single account"
type: summary
sources:
  - raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md
tags:
  - openrouter
  - workspaces
  - api-keys
  - guardrails
  - organization
  - multi-tenant
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Workspaces

## Key Points

- Workspaces organize OpenRouter projects into isolated environments, each with its own API keys, routing defaults, guardrails, and observability integrations ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Every account starts with a Default workspace containing all existing API keys, guardrails, BYOK provider keys, routing policies, presets, plugins, and observability integrations; if multiple workspaces are not needed, nothing changes ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Each workspace has independent settings for API keys, guardrails, BYOK provider keys, routing, presets, plugins, observability, and members ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Only organization admins can create and delete workspaces; members can create their own API keys in any workspace they belong to ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Account-level settings (activity, logs, credits, billing, organization membership, management keys, privacy, preferences) apply globally across all workspaces ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Workspace guardrails inherit account-level policies and can only add more restrictive rules within those constraints ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- All organization members automatically have member access to the Default workspace; chatroom and Fusion usage is governed by the Default workspace's settings ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Quotes

- "Workspaces let you organize your OpenRouter projects into separate environments, each with its own API keys, routing defaults, guardrails, and observability." ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- "Only organization admins can create and delete workspaces." ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- "Workspace guardrails inherit account-level policies and can add more restrictive rules within those constraints." ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Notes

- Workspaces can also be created and managed programmatically via the management API ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- When a member is removed from a workspace, their API keys in that workspace must be deleted first; their access to other workspaces is unaffected ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/workspaces]]
- [[concepts/byok]]
- [[concepts/provider_routing]]
- [[concepts/observability]]
- [[concepts/management_api_keys]]
- [[concepts/authentication]]