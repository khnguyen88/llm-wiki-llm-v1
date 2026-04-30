<!--
url: https://code.claude.com/docs/en/agent-sdk/plugins
download_date: 2026-04-29
website: claude-code
webpage: agent-sdk-plugins
-->

# Agent Sdk Plugins

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/plugins#content-area)
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)
English
Search...
⌘KAsk AI
  * [Claude Developer Platform](https://platform.claude.com/)
  * [Claude Code on the Web](https://claude.ai/code)
  * [Claude Code on the Web](https://claude.ai/code)


Search...
Navigation
Customize behavior
Plugins in the SDK
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Agent SDK
  * [Overview](https://code.claude.com/docs/en/agent-sdk/overview)
  * [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart)


##### Core concepts
  * [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop)
  * [Use Claude Code features](https://code.claude.com/docs/en/agent-sdk/claude-code-features)
  * [Work with sessions](https://code.claude.com/docs/en/agent-sdk/sessions)


##### Input and output
  * [Streaming Input](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)
  * [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input)
  * [Stream responses in real-time](https://code.claude.com/docs/en/agent-sdk/streaming-output)
  * [Get structured output from agents](https://code.claude.com/docs/en/agent-sdk/structured-outputs)


##### Extend with tools
  * [Give Claude custom tools](https://code.claude.com/docs/en/agent-sdk/custom-tools)
  * [Connect to external tools with MCP](https://code.claude.com/docs/en/agent-sdk/mcp)
  * [Scale to many tools with tool search](https://code.claude.com/docs/en/agent-sdk/tool-search)
  * [Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents)


##### Customize behavior
  * [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)
  * [Slash Commands in the SDK](https://code.claude.com/docs/en/agent-sdk/slash-commands)
  * [Agent Skills in the SDK](https://code.claude.com/docs/en/agent-sdk/skills)
  * [Plugins in the SDK](https://code.claude.com/docs/en/agent-sdk/plugins)


##### Control and observability
  * [Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
  * [Intercept and control agent behavior with hooks](https://code.claude.com/docs/en/agent-sdk/hooks)
  * [Rewind file changes with checkpointing](https://code.claude.com/docs/en/agent-sdk/file-checkpointing)
  * [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking)
  * [Observability with OpenTelemetry](https://code.claude.com/docs/en/agent-sdk/observability)
  * [Todo Lists](https://code.claude.com/docs/en/agent-sdk/todo-tracking)


##### Deployment
  * [Hosting the Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting)
  * [Securely deploying AI agents](https://code.claude.com/docs/en/agent-sdk/secure-deployment)


##### SDK references
  * [TypeScript SDK](https://code.claude.com/docs/en/agent-sdk/typescript)
  * [TypeScript V2 (preview)](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview)
  * [Python SDK](https://code.claude.com/docs/en/agent-sdk/python)
  * [Migration Guide](https://code.claude.com/docs/en/agent-sdk/migration-guide)


On this page
  * [What are plugins?](https://code.claude.com/docs/en/agent-sdk/plugins#what-are-plugins)
  * [Loading plugins](https://code.claude.com/docs/en/agent-sdk/plugins#loading-plugins)
  * [Path specifications](https://code.claude.com/docs/en/agent-sdk/plugins#path-specifications)
  * [Verifying plugin installation](https://code.claude.com/docs/en/agent-sdk/plugins#verifying-plugin-installation)
  * [Using plugin skills](https://code.claude.com/docs/en/agent-sdk/plugins#using-plugin-skills)
  * [Complete example](https://code.claude.com/docs/en/agent-sdk/plugins#complete-example)
  * [Plugin structure reference](https://code.claude.com/docs/en/agent-sdk/plugins#plugin-structure-reference)
  * [Common use cases](https://code.claude.com/docs/en/agent-sdk/plugins#common-use-cases)
  * [Development and testing](https://code.claude.com/docs/en/agent-sdk/plugins#development-and-testing)
  * [Project-specific extensions](https://code.claude.com/docs/en/agent-sdk/plugins#project-specific-extensions)
  * [Multiple plugin sources](https://code.claude.com/docs/en/agent-sdk/plugins#multiple-plugin-sources)
  * [Troubleshooting](https://code.claude.com/docs/en/agent-sdk/plugins#troubleshooting)
  * [Plugin not loading](https://code.claude.com/docs/en/agent-sdk/plugins#plugin-not-loading)
  * [Skills not appearing](https://code.claude.com/docs/en/agent-sdk/plugins#skills-not-appearing)
  * [Path resolution issues](https://code.claude.com/docs/en/agent-sdk/plugins#path-resolution-issues)
  * [See also](https://code.claude.com/docs/en/agent-sdk/plugins#see-also)


Customize behavior
# Plugins in the SDK
Copy page
Load custom plugins to extend Claude Code with commands, agents, skills, and hooks through the Agent SDK
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Plugins allow you to extend Claude Code with custom functionality that can be shared across projects. Through the Agent SDK, you can programmatically load plugins from local directories to add custom slash commands, agents, skills, hooks, and MCP servers to your agent sessions.
## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#what-are-plugins)
What are plugins?
Plugins are packages of Claude Code extensions that can include:
  * **Skills** : Model-invoked capabilities that Claude uses autonomously (can also be invoked with `/skill-name`)
  * **Agents** : Specialized subagents for specific tasks
  * **Hooks** : Event handlers that respond to tool use and other events
  * **MCP servers** : External tool integrations via Model Context Protocol


The `commands/` directory is a legacy format. Use `skills/` for new plugins. Claude Code continues to support both formats for backward compatibility.
For complete information on plugin structure and how to create plugins, see [Plugins](https://code.claude.com/docs/en/plugins).
## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#loading-plugins)
Loading plugins
Load plugins by providing their local file system paths in your options configuration. The `type` field must be `"local"`, the only value the SDK accepts. To use a plugin distributed through a [marketplace](https://code.claude.com/docs/en/plugin-marketplaces) or remote repository, download it first and provide the local directory path. The SDK supports loading multiple plugins from different locations.
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello",
  options: {
    plugins: [
      { type: "local", path: "./my-plugin" },
      { type: "local", path: "/absolute/path/to/another-plugin" }
    ]
  }
})) {
  // Plugin commands, agents, and other features are now available
}

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#path-specifications)
Path specifications
Plugin paths can be:
  * **Relative paths** : Resolved relative to your current working directory (for example, `"./plugins/my-plugin"`)
  * **Absolute paths** : Full file system paths (for example, `"/home/user/plugins/my-plugin"`)


The path should point to the plugin’s root directory (the directory containing `.claude-plugin/plugin.json`).
## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#verifying-plugin-installation)
Verifying plugin installation
When plugins load successfully, they appear in the system initialization message. You can verify that your plugins are available:
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello",
  options: {
    plugins: [{ type: "local", path: "./my-plugin" }]
  }
})) {
  if (message.type === "system" && message.subtype === "init") {
    // Check loaded plugins
    console.log("Plugins:", message.plugins);
    // Example: [{ name: "my-plugin", path: "./my-plugin" }]

    // Check available commands from plugins
    console.log("Commands:", message.slash_commands);
    // Example: ["/help", "/compact", "my-plugin:custom-command"]
  }
}

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#using-plugin-skills)
Using plugin skills
Skills from plugins are automatically namespaced with the plugin name to avoid conflicts. When invoked as slash commands, the format is `plugin-name:skill-name`.
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

// Load a plugin with a custom /greet skill
for await (const message of query({
  prompt: "/my-plugin:greet", // Use plugin skill with namespace
  options: {
    plugins: [{ type: "local", path: "./my-plugin" }]
  }
})) {
  // Claude executes the custom greeting skill from the plugin
  if (message.type === "assistant") {
    console.log(message.message.content);
  }
}

```

If you installed a plugin via the CLI (for example, `/plugin install my-plugin@marketplace`), you can still use it in the SDK by providing its installation path. Check `~/.claude/plugins/` for CLI-installed plugins.
## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#complete-example)
Complete example
Here’s a full example demonstrating plugin loading and usage:
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";
import * as path from "path";

async function runWithPlugin() {
  const pluginPath = path.join(__dirname, "plugins", "my-plugin");

  console.log("Loading plugin from:", pluginPath);

  for await (const message of query({
    prompt: "What custom commands do you have available?",
    options: {
      plugins: [{ type: "local", path: pluginPath }],
      maxTurns: 3
    }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      console.log("Loaded plugins:", message.plugins);
      console.log("Available commands:", message.slash_commands);
    }

    if (message.type === "assistant") {
      console.log("Assistant:", message.message.content);
    }
  }
}

runWithPlugin().catch(console.error);

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#plugin-structure-reference)
Plugin structure reference
A plugin directory must contain a `.claude-plugin/plugin.json` manifest file. It can optionally include:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin manifest
├── skills/                   # Agent Skills (invoked autonomously or via /skill-name)
│   └── my-skill/
│       └── SKILL.md
├── commands/                 # Legacy: use skills/ instead
│   └── custom-cmd.md
├── agents/                   # Custom agents
│   └── specialist.md
├── hooks/                    # Event handlers
│   └── hooks.json
└── .mcp.json                # MCP server definitions

```

For detailed information on creating plugins, see:
  * [Plugins](https://code.claude.com/docs/en/plugins) - Complete plugin development guide
  * [Plugins reference](https://code.claude.com/docs/en/plugins-reference) - Technical specifications and schemas


## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#common-use-cases)
Common use cases
### 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#development-and-testing)
Development and testing
Load plugins during development without installing them globally:

```
plugins: [{ type: "local", path: "./dev-plugins/my-plugin" }];

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#project-specific-extensions)
Project-specific extensions
Include plugins in your project repository for team-wide consistency:

```
plugins: [{ type: "local", path: "./project-plugins/team-workflows" }];

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#multiple-plugin-sources)
Multiple plugin sources
Combine plugins from different locations:

```
plugins: [
  { type: "local", path: "./local-plugin" },
  { type: "local", path: "~/.claude/custom-plugins/shared-plugin" }
];

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#troubleshooting)
Troubleshooting
### 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#plugin-not-loading)
Plugin not loading
If your plugin doesn’t appear in the init message:
  1. **Check the path** : Ensure the path points to the plugin root directory (containing `.claude-plugin/`)
  2. **Validate plugin.json** : Ensure your manifest file has valid JSON syntax
  3. **Check file permissions** : Ensure the plugin directory is readable


### 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#skills-not-appearing)
Skills not appearing
If plugin skills don’t work:
  1. **Use the namespace** : Plugin skills require the `plugin-name:skill-name` format when invoked as slash commands
  2. **Check init message** : Verify the skill appears in `slash_commands` with the correct namespace
  3. **Validate skill files** : Ensure each skill has a `SKILL.md` file in its own subdirectory under `skills/` (for example, `skills/my-skill/SKILL.md`)


### 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#path-resolution-issues)
Path resolution issues
If relative paths don’t work:
  1. **Check working directory** : Relative paths are resolved from your current working directory
  2. **Use absolute paths** : For reliability, consider using absolute paths
  3. **Normalize paths** : Use path utilities to construct paths correctly


## 
[​](https://code.claude.com/docs/en/agent-sdk/plugins#see-also)
See also
  * [Plugins](https://code.claude.com/docs/en/plugins) - Complete plugin development guide
  * [Plugins reference](https://code.claude.com/docs/en/plugins-reference) - Technical specifications
  * [Slash Commands](https://code.claude.com/docs/en/agent-sdk/slash-commands) - Using slash commands in the SDK
  * [Subagents](https://code.claude.com/docs/en/agent-sdk/subagents) - Working with specialized agents
  * [Skills](https://code.claude.com/docs/en/agent-sdk/skills) - Using Agent Skills


Was this page helpful?
YesNo
[Agent Skills in the SDK](https://code.claude.com/docs/en/agent-sdk/skills)[Configure permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
⌘I
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
Company
[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)
Help and security
[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)
Learn
[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)
Terms and policies
[Privacy choices](https://code.claude.com/docs/en/agent-sdk/plugins)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
