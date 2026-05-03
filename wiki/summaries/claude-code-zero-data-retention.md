---
title: "Claude Code Zero Data Retention"
summary: "ZDR for Claude Code on Claude for Enterprise ensures prompts and model responses are not stored after delivery, with specific scope exclusions and disabled features"
type: summary
sources:
  - raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md
tags:
  - claude-code
  - enterprise
  - data-retention
  - privacy
  - compliance
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Claude Code Zero Data Retention

## Key Points

- Zero Data Retention (ZDR) is available for Claude Code through Claude for Enterprise; prompts and model responses are processed in real time and not stored by Anthropic after the response is returned, except where required by law or to combat misuse ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- ZDR is enabled on a per-organization basis; each new organization requires ZDR to be enabled separately by the Anthropic account team and it does not automatically apply to new organizations under the same account ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- ZDR covers model inference calls made through Claude Code on Claude for Enterprise regardless of which Claude model is used ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- ZDR does not cover chat on claude.ai, Cowork sessions, analytics productivity metadata, user/seat management data, or third-party integrations ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- Features disabled under ZDR include Claude Code on the Web, remote sessions from the Desktop app, and feedback submission (`/feedback`) ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- Even with ZDR enabled, Anthropic may retain data for up to 2 years if a session is flagged for a policy violation ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- ZDR for Claude Code applies only to Anthropic's direct platform; deployments on AWS Bedrock, Google Vertex AI, or Microsoft Foundry follow those platforms' data retention policies ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]

## Notes

- Organizations currently using ZDR for Claude Code via pay-as-you-go API keys can transition to Claude for Enterprise to gain administrative features while maintaining ZDR ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- All ZDR enablement actions are audit-logged ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]
- Disabled features are blocked at the backend level regardless of client-side display ^[raw/document/claude code/claude-code-124-zero-data-retention-2026-04-29.md]

## Related

- [[concepts/zero_data_retention]]
- [[entities/claude_code]]
- [[entities/claude_code_web]]
- [[concepts/analytics]]
- [[entities/amazon_bedrock]]
- [[entities/google_vertex_ai]]
- [[entities/microsoft_foundry]]