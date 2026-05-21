---
title: "Plugins"
summary: "Extension mechanisms that add capabilities to a system — Claude Code plugins are packages of skills, agents, hooks, and MCP servers; OpenRouter plugins inject or mutate requests/responses"
type: concept
sources:
  - raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md
  - raw/document/claude code/claude-code-039-channels-2026-04-29.md
  - raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md
  - raw/document/claude code/claude-code-115-vs-code-2026-04-29.md
  - raw/document/claude code/claude-code-117-whats-new-2026-04-29.md
  - raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md
  - raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md
  - raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md
  - raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md
  - raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md
tags:
  - agent-sdk
  - plugins
  - extensibility
  - skills
  - hooks
  - mcp
  - channels
  - openrouter
  - response-healing
  - context-compression
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Plugins

Plugins are packages of Claude Code extensions that can be shared across projects and loaded into Agent SDK sessions to add custom slash commands, agents, skills, hooks, and MCP servers. ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

## Key Points

- Plugins contain four types of extensions: skills (model-invoked capabilities), agents (specialized subagents), hooks (event handlers), and MCP servers (external tool integrations) ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugins are loaded via the `plugins` option in `query()` with `type: "local"` and a filesystem path; the SDK only accepts local paths, not remote or marketplace references ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Plugin skills are automatically namespaced as `plugin-name:skill-name` when invoked as slash commands to prevent naming conflicts between plugins ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- A plugin directory must contain a `.claude-plugin/plugin.json` manifest file at its root ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- The `commands/` directory is a legacy format; new plugins should use `skills/` instead ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]
- Channel plugins are MCP servers that push external events into a running session; they are installed via `/plugin install` (e.g., `telegram@claude-plugins-official`), activated with `/reload-plugins`, and enabled per session with `claude --channels plugin:<name>@<marketplace>` ^[001a-raw/document/claude code/claude-code-039-channels-2026-04-29.md]
- Channel plugins published to a marketplace still require `--dangerously-load-development-channels` during the research preview unless they are on the Anthropic allowlist; to get added, submit the plugin to the official marketplace for security review ^[001a-raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]
- On Team and Enterprise plans, admins can use `allowedChannelPlugins` to replace the default Anthropic allowlist entirely with an organization-specific list of approved channel plugins ^[001a-raw/document/claude code/claude-code-040-channels-reference-2026-04-29.md]

## Details

Plugin paths can be relative (resolved from the current working directory) or absolute. The path must point to the plugin root directory containing `.claude-plugin/plugin.json`. Multiple plugins from different locations can be loaded in a single session. ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

Successful plugin loading is verified through the system init message (`message.type === "system" && message.subtype === "init"`), which exposes `message.plugins` (loaded plugin list) and `message.slash_commands` (available commands including namespaced plugin skills). ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

The plugin directory structure includes `.claude-plugin/plugin.json` (required), and optional `skills/`, `commands/` (legacy), `agents/`, `hooks/`, and `.mcp.json` directories/files. Each skill must have its own subdirectory under `skills/` with a `SKILL.md` file (e.g., `skills/my-skill/SKILL.md`). ^[001a-raw/document/claude code/claude-code-015-agent-sdk-plugins-2026-04-29.md]

- In the VS Code extension, `/plugins` opens a graphical dialog with Plugins (installed/available with search and toggle switches) and Marketplaces (add/remove sources) tabs; plugins installed from the extension use the same CLI commands under the hood and configurations are shared ^[001a-raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- VS Code plugin installation offers three scopes: "Install for you" (user scope, all projects), "Install for this project" (project scope, shared with collaborators), "Install locally" (local scope, only you, only this repository) ^[001a-raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Plugin marketplaces in VS Code accept GitHub repos, URLs, or local paths; clicking the refresh icon updates the plugin list and the trash icon removes a marketplace; changes prompt a Claude Code restart ^[001a-raw/document/claude code/claude-code-115-vs-code-2026-04-29.md]
- Plugin executables are available on the Bash tool's PATH, allowing plugin-provided commands to be invoked directly from shell commands ^[001a-raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]
- Plugin executables on PATH (v2.1.91): placing an executable in a `bin/` directory at the plugin root causes Claude Code to add that directory to the Bash tool's PATH while the plugin is enabled, enabling bare command invocation without absolute paths or wrapper scripts ^[001a-raw/document/claude code/claude-code-119-whats-new-2026-w14-2026-04-29.md]
- Plugins can ship background watchers via a top-level `monitors` manifest key that auto-arms at session start or on skill invoke ^[001a-raw/document/claude code/claude-code-121-whats-new-2026-w16-2026-04-29.md]
- Plugins can contribute custom themes that appear in the `/theme` list alongside built-in presets and user-created themes ^[001a-raw/document/claude code/claude-code-117-whats-new-2026-04-29.md]
- The `claude plugin tag` command creates release git tags for plugins with version validation ^[001a-raw/document/claude code/claude-code-122-whats-new-2026-w17-2026-04-29.md]

## OpenRouter Plugins

OpenRouter plugins are a distinct mechanism from Claude Code plugins. They extend model capabilities by injecting or mutating requests and responses. Unlike [[004-wiki/concepts/server-tools|server tools]] (which the model calls 0-N times), OpenRouter plugins always run exactly once when enabled. ^[001a-raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

### Available OpenRouter Plugins

| Plugin | ID | Description |
|--------|------|-------------|
| Web Search (deprecated) | `web` | Augments LLM responses with real-time web search results; replaced by `openrouter:web_search` server tool |
| PDF Inputs | — | Parses and extracts content from uploaded PDF files |
| Response Healing | `response-healing` | Automatically fixes malformed JSON responses from LLMs |
| Context Compression | `context-compression` | Compresses prompts exceeding a model's context window using middle-out truncation |

^[001a-raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

### Enabling and Configuring OpenRouter Plugins

Plugins are enabled per-request by adding a `plugins` array to the chat completions request body. Each plugin is identified by its `id` and can include optional configuration parameters. Multiple plugins can be combined in a single request. ^[001a-raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

Organization admins and individual users can configure default plugin settings via the Plugins settings page (`/settings/plugins`). The "Prevent overrides" option enforces org-wide policies by preventing individual requests from disabling or modifying a plugin's configuration. ^[001a-raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

Plugin precedence: request-level settings override account defaults, unless "Prevent overrides" is enabled. A default plugin can be disabled per-request by passing `{ "id": "web", "enabled": false }`. ^[001a-raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

The `:online` model variant suffix is a deprecated shortcut for the `web` plugin, exactly equivalent to `{ "model": "...", "plugins": [{ "id": "web" }] }`. ^[001a-raw/document/openrouter/openrouter-038-guides-features-plugins-overview-2026-04-29.md]

### Web Plugin Configuration (Deprecated)

The `web` plugin accepts configuration parameters: `id` (`"web"`), `engine` (`"native"`, `"exa"`, `"firecrawl"`, `"parallel"`, or undefined for default behavior), `max_results` (defaults to 5), `search_prompt` (custom prompt text for attaching results), `include_domains` (domain whitelist with wildcard and path support), and `exclude_domains` (domain blacklist). The default search prompt instructs the model to cite sources using markdown links named by domain. ^[001a-raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

Domain filtering in the plugin uses `include_domains` and `exclude_domains` (distinct from the server tool's `allowed_domains`/`excluded_domains`). Engine compatibility varies: Exa supports both simultaneously; Parallel supports both but they are mutually exclusive; Firecrawl returns a 400 error if domain filters are set; native provider support varies. Wildcards (`*.substack.com`) and path filtering (`openai.com/blog`) are supported. ^[001a-raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

The `:online` suffix can be combined with `:free` as `"model:free:online"`. Web search results are standardized in the API response `message.annotations` array using the `url_citation` type, following the OpenAI Chat Completion Message schema. ^[001a-raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

### xAI X Search Filters

When xAI models use web search, OpenRouter automatically adds an `x_search` tool alongside `web_search`. The top-level `x_search_filter` parameter controls X/Twitter results with: `allowed_x_handles` and `excluded_x_handles` (mutually exclusive, max 10 each), `from_date` and `to_date` (ISO 8601), and `enable_image_understanding` and `enable_video_understanding` (booleans). If validation fails, the filter is silently dropped. ^[001a-raw/document/openrouter/openrouter-039-guides-features-plugins-web-search-2026-04-29.md]

## Related

- [[004-wiki/entities/agent-sdk]]
- [[004-wiki/entities/vs-code-extension]]
- [[004-wiki/concepts/skills]]
- [[004-wiki/concepts/hooks]]
- [[004-wiki/concepts/mcp]]
- [[004-wiki/concepts/subagents]]
- [[004-wiki/concepts/setting-sources]]
- [[004-wiki/concepts/channels]]
- [[004-wiki/entities/openrouter]]
- [[004-wiki/concepts/server-tools]]
- [[004-wiki/concepts/response-healing]]
- [[004-wiki/concepts/context-compression]]
- [[004-wiki/concepts/model-variants]]
- [[004-wiki/summaries/openrouter-guides-features-plugins-overview]]
- [[004-wiki/summaries/openrouter-guides-features-plugins-web-search]]