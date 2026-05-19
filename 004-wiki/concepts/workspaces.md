---
title: "Workspaces"
summary: "Isolated environments within a single OpenRouter account that scope API keys, guardrails, BYOK keys, routing, presets, plugins, observability, and membership"
type: concept
sources:
  - raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md
tags:
  - openrouter
  - workspaces
  - multi-tenant
  - organization
  - isolation
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Workspaces

Workspaces organize OpenRouter projects into separate environments under a single account, each with independent API keys, routing defaults, guardrails, and observability. They enable isolation of teams, projects, or deployment stages (e.g., staging vs. production). ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Key Points

- Every account has a Default workspace containing all existing keys, guardrails, BYOK provider keys, routing policies, presets, plugins, and observability integrations; no action is needed if multiple workspaces are not required ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Each workspace has independent settings for API keys, guardrails, BYOK provider keys, routing, presets, plugins, observability integrations, and members ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Only organization admins can create and delete workspaces; members can create their own API keys in any workspace they belong to ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- Workspace guardrails inherit account-level policies and can add more restrictive rules, but cannot be less restrictive than the account-level ceiling ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]
- All organization members automatically have member access to the Default workspace; chatroom and Fusion usage is governed by the Default workspace ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Details

### Workspace-Scoped Resources

Each workspace maintains independent configuration for eight categories:

| Resource | Scope Behavior |
|---|---|
| API Keys | Every key lives in exactly one workspace; members create their own keys, admins create system keys owned by the workspace |
| Guardrails | Per-workspace rules that inherit account-level policies; workspaces can only add more restrictive constraints |
| BYOK | Provider keys can be per-workspace or shared across multiple workspaces |
| Routing | Provider routing configured per workspace (cost, latency, throughput, or tool-calling quality) |
| Presets | Shortcuts for system prompts, model/provider configurations, and request parameters — scoped per workspace |
| Plugins | Default plugin behavior for API requests configured per workspace |
| Observability | Different integrations per workspace, or traces from all workspaces to the same platform |
| Members | Access control per workspace; members can belong to multiple workspaces |

^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

### Account-Level Settings

Some settings apply globally across all workspaces: activity and logs (filterable by workspace), credits and billing, organization membership and roles, management keys (for administrative actions across all workspaces), privacy policies and provider/model restrictions, and account preferences. ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

### Organization Roles

Organization admins have admin permissions across all workspaces and can view and manage everything (API keys, guardrails, BYOK, routing, presets, plugins, observability, members, settings). Only admins can create/delete workspaces and control member access. Organization members have member permissions in each workspace they belong to, with their API keys governed by that workspace's settings. ^[raw/document/openrouter/openrouter-029-guides-features-workspaces-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/byok]]
- [[concepts/provider_routing]]
- [[concepts/observability]]
- [[concepts/management_api_keys]]
- [[concepts/authentication]]
- [[concepts/data_privacy]]