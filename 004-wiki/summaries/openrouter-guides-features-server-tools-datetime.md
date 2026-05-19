---
title: "Openrouter Guides Features Server Tools Datetime"
summary: "OpenRouter's datetime server tool gives any model access to the current date and time, useful for prompts requiring temporal awareness"
type: summary
sources:
  - raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md
tags:
  - openrouter
  - server-tools
  - datetime
  - temporal-awareness
  - api
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Openrouter Guides Features Server Tools Datetime

## Key Points

- The `openrouter:datetime` server tool gives any model access to the current date and time, enabling temporal awareness for scheduling, time-sensitive questions, and tasks requiring "right now" knowledge ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Server tools are currently in beta; the API and behavior may change ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Invoked by including `{ "type": "openrouter:datetime" }` in the `tools` array of a chat completions request ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Accepts an optional `timezone` parameter using IANA timezone names (e.g., `"America/New_York"`, `"Europe/London"`, `"Asia/Tokyo"`); defaults to `UTC` ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Response includes `datetime` (ISO 8601 with timezone offset) and `timezone` fields ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- No additional cost beyond standard token usage ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Works with the standard OpenRouter chat completions endpoint (`/api/v1/chat/completions`) ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]

## Notes

- The datetime tool is one of four OpenRouter server tools, alongside `openrouter:web_search`, `openrouter:image_generation`, and `openrouter:web_fetch` ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]

## Related

- [[entities/openrouter]]
- [[concepts/server_tools]]
- [[concepts/server_tools_datetime]]
- [[concepts/tool_calling]]