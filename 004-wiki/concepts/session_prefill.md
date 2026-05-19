---
title: "Session Prefill"
summary: "URL parameters for pre-filling Claude Code web session prompts, repositories, and environments to enable integrations like issue-tracker buttons"
type: concept
sources:
  - raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md
tags:
  - claude-code
  - web
  - sessions
  - url-parameters
  - integration
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Session Prefill

Web sessions at claude.ai/code can be pre-filled by appending query parameters to the URL, enabling programmatic session creation from external tools like issue trackers or project management dashboards. ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]

## Key Points

- `prompt` (alias `q`) pre-fills the input box with task text; URL-encode the value ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- `prompt_url` fetches prompt text from a URL for prompts too long to embed in a query string; the URL must allow cross-origin requests; ignored when `prompt` is also set ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- `repositories` (alias `repo`) accepts a comma-separated list of `owner/repo` slugs to pre-select; example: `acme/webapp,acme/api` ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- `environment` pre-selects a cloud environment by name or ID ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]
- All parameter values must be URL-encoded; example: `https://claude.ai/code?prompt=Fix%20the%20login%20bug&repositories=acme/webapp` ^[raw/document/claude code/claude-code-116-web-quickstart-2026-04-29.md]

## Details

Session prefill enables deep-linking into Claude Code on the web from external systems. A project management tool could construct a URL with the issue description as the prompt and the relevant repository pre-selected, so developers can jump directly into a task without manually configuring the session. The `prompt_url` parameter supports fetching longer prompts from a remote endpoint, useful for templates or detailed specifications that exceed practical URL length limits.

## Related

- [[entities/claude_code_web]]
- [[concepts/sessions]]
- [[concepts/cloud_environment]]
- [[summaries/claude-code-web-quickstart]]