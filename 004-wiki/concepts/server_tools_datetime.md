---
title: "Server Tools Datetime"
summary: "An OpenRouter server tool that gives any model access to the current date and time with optional timezone configuration"
type: concept
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
confidence: 1.0
provenance: extracted
---

# Server Tools Datetime

The `openrouter:datetime` server tool gives any model on OpenRouter access to the current date and time. It is useful for prompts that require temporal awareness — scheduling, time-sensitive questions, or any task where the model needs to know the current moment. ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]

## Key Points

- Invoked by including `{ "type": "openrouter:datetime" }` in the `tools` array of a chat completions request; the model decides when to call it based on the prompt ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Accepts an optional `timezone` parameter (IANA timezone name) that defaults to `UTC` ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Response returns a JSON object with `datetime` (ISO 8601 with timezone offset) and `timezone` fields ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- No additional cost beyond standard token usage ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]
- Currently in beta; API and behavior may change ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]

## Details

The datetime tool is one of four OpenRouter server tools (alongside `openrouter:web_search`, `openrouter:image_generation`, and `openrouter:web_fetch`). Like other server tools, it requires no client-side implementation — the model decides when to call it, and OpenRouter executes it server-side, returning the result to the model. ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]

### Configuration

The tool is specified in the request's `tools` array with type `openrouter:datetime`. An optional `timezone` parameter accepts IANA timezone names (e.g., `"America/New_York"`, `"Europe/London"`, `"Asia/Tokyo"`). When no timezone is provided, the default is `UTC`. ^[raw/document/openrouter/openrouter-036-guides-features-server-tools-datetime-2026-04-29.md]

Example configuration with timezone:

```json
{
  "type": "openrouter:datetime",
  "parameters": {
    "timezone": "America/New_York"
  }
}
```

### Response Format

When the model calls the datetime tool, it receives a JSON response containing the current `datetime` in ISO 8601 format with timezone offset and the `timezone` name:

```json
{
  "datetime": "2025-07-15T14:30:00.000-04:00",
  "timezone": "America/New_York"
}
```

## Related

- [[entities/openrouter]]
- [[concepts/server_tools]]
- [[concepts/tool_calling]]
- [[concepts/web_search]]
- [[concepts/web_fetch]]
- [[summaries/openrouter-guides-features-server-tools-datetime]]