<!--
url: https://code.claude.com/docs/en/plugins
download_date: 2026-04-29
website: claude-code
webpage: plugins
-->

# Plugins

[Skip to main content](https://code.claude.com/docs/en/plugins#content-area)
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
Tools and plugins
Create plugins
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Agents
  * [Create custom subagents](https://code.claude.com/docs/en/sub-agents)
  * [Run agent teams](https://code.claude.com/docs/en/agent-teams)


##### Tools and plugins
  * [Model Context Protocol (MCP)](https://code.claude.com/docs/en/mcp)
  * [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)
  * [Create plugins](https://code.claude.com/docs/en/plugins)
  * [Extend Claude with skills](https://code.claude.com/docs/en/skills)


##### Automation
  * [Automate with hooks](https://code.claude.com/docs/en/hooks-guide)
  * [Push external events to Claude](https://code.claude.com/docs/en/channels)
  * [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
  * [Programmatic usage](https://code.claude.com/docs/en/headless)


##### Troubleshooting
  * [Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)
  * [Troubleshoot performance and stability](https://code.claude.com/docs/en/troubleshooting)
  * [Debug configuration](https://code.claude.com/docs/en/debug-your-config)
  * [Error reference](https://code.claude.com/docs/en/errors)


On this page
  * [When to use plugins vs standalone configuration](https://code.claude.com/docs/en/plugins#when-to-use-plugins-vs-standalone-configuration)
  * [Quickstart](https://code.claude.com/docs/en/plugins#quickstart)
  * [Prerequisites](https://code.claude.com/docs/en/plugins#prerequisites)
  * [Create your first plugin](https://code.claude.com/docs/en/plugins#create-your-first-plugin)
  * [Plugin structure overview](https://code.claude.com/docs/en/plugins#plugin-structure-overview)
  * [Develop more complex plugins](https://code.claude.com/docs/en/plugins#develop-more-complex-plugins)
  * [Add Skills to your plugin](https://code.claude.com/docs/en/plugins#add-skills-to-your-plugin)
  * [Add LSP servers to your plugin](https://code.claude.com/docs/en/plugins#add-lsp-servers-to-your-plugin)
  * [Add background monitors to your plugin](https://code.claude.com/docs/en/plugins#add-background-monitors-to-your-plugin)
  * [Ship default settings with your plugin](https://code.claude.com/docs/en/plugins#ship-default-settings-with-your-plugin)
  * [Organize complex plugins](https://code.claude.com/docs/en/plugins#organize-complex-plugins)
  * [Test your plugins locally](https://code.claude.com/docs/en/plugins#test-your-plugins-locally)
  * [Debug plugin issues](https://code.claude.com/docs/en/plugins#debug-plugin-issues)
  * [Share your plugins](https://code.claude.com/docs/en/plugins#share-your-plugins)
  * [Submit your plugin to the official marketplace](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-official-marketplace)
  * [Convert existing configurations to plugins](https://code.claude.com/docs/en/plugins#convert-existing-configurations-to-plugins)
  * [Migration steps](https://code.claude.com/docs/en/plugins#migration-steps)
  * [What changes when migrating](https://code.claude.com/docs/en/plugins#what-changes-when-migrating)
  * [Next steps](https://code.claude.com/docs/en/plugins#next-steps)
  * [For plugin users](https://code.claude.com/docs/en/plugins#for-plugin-users)
  * [For plugin developers](https://code.claude.com/docs/en/plugins#for-plugin-developers)


Tools and plugins
# Create plugins
Copy page
Create custom plugins to extend Claude Code with skills, agents, hooks, and MCP servers.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Plugins let you extend Claude Code with custom functionality that can be shared across projects and teams. This guide covers creating your own plugins with skills, agents, hooks, and MCP servers. Looking to install existing plugins? See [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins). For complete technical specifications, see [Plugins reference](https://code.claude.com/docs/en/plugins-reference).
## 
[​](https://code.claude.com/docs/en/plugins#when-to-use-plugins-vs-standalone-configuration)
When to use plugins vs standalone configuration
Claude Code supports two ways to add custom skills, agents, and hooks:  
| Approach  | Skill names  | Best for  |  
| --- | --- | --- |  
|  **Standalone** (`.claude/` directory)  | `/hello`  | Personal workflows, project-specific customizations, quick experiments  |  
|  **Plugins** (directories with `.claude-plugin/plugin.json`)  | `/plugin-name:hello`  | Sharing with teammates, distributing to community, versioned releases, reusable across projects  |  
**Use standalone configuration when** :
  * You’re customizing Claude Code for a single project
  * The configuration is personal and doesn’t need to be shared
  * You’re experimenting with skills or hooks before packaging them
  * You want short skill names like `/hello` or `/deploy`

**Use plugins when** :
  * You want to share functionality with your team or community
  * You need the same skills/agents across multiple projects
  * You want version control and easy updates for your extensions
  * You’re distributing through a marketplace
  * You’re okay with namespaced skills like `/my-plugin:hello` (namespacing prevents conflicts between plugins)


Start with standalone configuration in `.claude/` for quick iteration, then [convert to a plugin](https://code.claude.com/docs/en/plugins#convert-existing-configurations-to-plugins) when you’re ready to share.
## 
[​](https://code.claude.com/docs/en/plugins#quickstart)
Quickstart
This quickstart walks you through creating a plugin with a custom skill. You’ll create a manifest (the configuration file that defines your plugin), add a skill, and test it locally using the `--plugin-dir` flag.
### 
[​](https://code.claude.com/docs/en/plugins#prerequisites)
Prerequisites
  * Claude Code [installed and authenticated](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)


If you don’t see the `/plugin` command, update Claude Code to the latest version. See [Troubleshooting](https://code.claude.com/docs/en/troubleshooting) for upgrade instructions.
### 
[​](https://code.claude.com/docs/en/plugins#create-your-first-plugin)
Create your first plugin
1
[](https://code.claude.com/docs/en/plugins)
Create the plugin directory
Every plugin lives in its own directory containing a manifest and your skills, agents, or hooks. Create one now:

```
mkdir my-first-plugin

```

2
[](https://code.claude.com/docs/en/plugins)
Create the plugin manifest
The manifest file at `.claude-plugin/plugin.json` defines your plugin’s identity: its name, description, and version. Claude Code uses this metadata to display your plugin in the plugin manager.Create the `.claude-plugin` directory inside your plugin folder:

```
mkdir my-first-plugin/.claude-plugin

```

Then create `my-first-plugin/.claude-plugin/plugin.json` with this content:
my-first-plugin/.claude-plugin/plugin.json

```
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}

```
  
| Field  | Purpose  |  
| --- | --- |  
| `name`  | Unique identifier and skill namespace. Skills are prefixed with this (e.g., `/my-first-plugin:hello`).  |  
| `description`  | Shown in the plugin manager when browsing or installing plugins.  |  
| `version`  | Optional. If set, users only receive updates when you bump this field. If omitted and your plugin is distributed via git, the commit SHA is used and every commit counts as a new version. See [version management](https://code.claude.com/docs/en/plugins-reference#version-management).  |  
| `author`  | Optional. Helpful for attribution.  |  
For additional fields like `homepage`, `repository`, and `license`, see the [full manifest schema](https://code.claude.com/docs/en/plugins-reference#plugin-manifest-schema).
3
[](https://code.claude.com/docs/en/plugins)
Add a skill
Skills live in the `skills/` directory. Each skill is a folder containing a `SKILL.md` file. The folder name becomes the skill name, prefixed with the plugin’s namespace (`hello/` in a plugin named `my-first-plugin` creates `/my-first-plugin:hello`).Create a skill directory in your plugin folder:

```
mkdir -p my-first-plugin/skills/hello

```

Then create `my-first-plugin/skills/hello/SKILL.md` with this content:
my-first-plugin/skills/hello/SKILL.md

```
---
description: Greet the user with a friendly message
disable-model-invocation: true
---

Greet the user warmly and ask how you can help them today.

```

4
[](https://code.claude.com/docs/en/plugins)
Test your plugin
Run Claude Code with the `--plugin-dir` flag to load your plugin:

```
claude --plugin-dir ./my-first-plugin

```

Once Claude Code starts, try your new skill:

```
/my-first-plugin:hello

```

You’ll see Claude respond with a greeting. Run `/help` to see your skill listed under the plugin namespace.
**Why namespacing?** Plugin skills are always namespaced (like `/my-first-plugin:hello`) to prevent conflicts when multiple plugins have skills with the same name.To change the namespace prefix, update the `name` field in `plugin.json`.
5
[](https://code.claude.com/docs/en/plugins)
Add skill arguments
Make your skill dynamic by accepting user input. The `$ARGUMENTS` placeholder captures any text the user provides after the skill name.Update your `SKILL.md` file:
my-first-plugin/skills/hello/SKILL.md

```
---
description: Greet the user with a personalized message
---

# Hello Skill

Greet the user named "$ARGUMENTS" warmly and ask how you can help them today. Make the greeting personal and encouraging.

```

Run `/reload-plugins` to pick up the changes, then try the skill with your name:

```
/my-first-plugin:hello Alex

```

Claude will greet you by name. For more on passing arguments to skills, see [Skills](https://code.claude.com/docs/en/skills#pass-arguments-to-skills).
You’ve successfully created and tested a plugin with these key components:
  * **Plugin manifest** (`.claude-plugin/plugin.json`): describes your plugin’s metadata
  * **Skills directory** (`skills/`): contains your custom skills
  * **Skill arguments** (`$ARGUMENTS`): captures user input for dynamic behavior


The `--plugin-dir` flag is useful for development and testing. When you’re ready to share your plugin with others, see [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces).
## 
[​](https://code.claude.com/docs/en/plugins#plugin-structure-overview)
Plugin structure overview
You’ve created a plugin with a skill, but plugins can include much more: custom agents, hooks, MCP servers, LSP servers, and background monitors.
**Common mistake** : Don’t put `commands/`, `agents/`, `skills/`, or `hooks/` inside the `.claude-plugin/` directory. Only `plugin.json` goes inside `.claude-plugin/`. All other directories must be at the plugin root level.  
| Directory  | Location  | Purpose  |  
| --- | --- | --- |  
| `.claude-plugin/`  | Plugin root  | Contains `plugin.json` manifest (optional if components use default locations)  |  
| `skills/`  | Plugin root  | Skills as `<name>/SKILL.md` directories  |  
| `commands/`  | Plugin root  | Skills as flat Markdown files. Use `skills/` for new plugins  |  
| `agents/`  | Plugin root  | Custom agent definitions  |  
| `hooks/`  | Plugin root  | Event handlers in `hooks.json`  |  
| `.mcp.json`  | Plugin root  | MCP server configurations  |  
| `.lsp.json`  | Plugin root  | LSP server configurations for code intelligence  |  
| `monitors/`  | Plugin root  | Background monitor configurations in `monitors.json`  |  
| `bin/`  | Plugin root  | Executables added to the Bash tool’s `PATH` while the plugin is enabled  |  
| `settings.json`  | Plugin root  | Default [settings](https://code.claude.com/docs/en/settings) applied when the plugin is enabled  |  
**Next steps** : Ready to add more features? Jump to [Develop more complex plugins](https://code.claude.com/docs/en/plugins#develop-more-complex-plugins) to add agents, hooks, MCP servers, and LSP servers. For complete technical specifications of all plugin components, see [Plugins reference](https://code.claude.com/docs/en/plugins-reference).
## 
[​](https://code.claude.com/docs/en/plugins#develop-more-complex-plugins)
Develop more complex plugins
Once you’re comfortable with basic plugins, you can create more sophisticated extensions.
### 
[​](https://code.claude.com/docs/en/plugins#add-skills-to-your-plugin)
Add Skills to your plugin
Plugins can include [Agent Skills](https://code.claude.com/docs/en/skills) to extend Claude’s capabilities. Skills are model-invoked: Claude automatically uses them based on the task context. Add a `skills/` directory at your plugin root with Skill folders containing `SKILL.md` files:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── code-review/
        └── SKILL.md

```

Each `SKILL.md` contains YAML frontmatter and instructions. Include a `description` so Claude knows when to use the skill:

```
---
description: Reviews code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
---

When reviewing code, check for:
1. Code organization and structure
2. Error handling
3. Security concerns
4. Test coverage

```

After installing the plugin, run `/reload-plugins` to load the Skills. For complete Skill authoring guidance including progressive disclosure and tool restrictions, see [Agent Skills](https://code.claude.com/docs/en/skills).
### 
[​](https://code.claude.com/docs/en/plugins#add-lsp-servers-to-your-plugin)
Add LSP servers to your plugin
For common languages like TypeScript, Python, and Rust, install the pre-built LSP plugins from the official marketplace. Create custom LSP plugins only when you need support for languages not already covered.
LSP (Language Server Protocol) plugins give Claude real-time code intelligence. If you need to support a language that doesn’t have an official LSP plugin, you can create your own by adding an `.lsp.json` file to your plugin:
.lsp.json

```
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}

```

Users installing your plugin must have the language server binary installed on their machine. For complete LSP configuration options, see [LSP servers](https://code.claude.com/docs/en/plugins-reference#lsp-servers).
### 
[​](https://code.claude.com/docs/en/plugins#add-background-monitors-to-your-plugin)
Add background monitors to your plugin
Background monitors let your plugin watch logs, files, or external status in the background and notify Claude as events arrive. Claude Code starts each monitor automatically when the plugin is active, so you don’t need to instruct Claude to start the watch. Add a `monitors/monitors.json` file at the plugin root with an array of monitor entries:
monitors/monitors.json

```
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log"
  }
]

```

Each stdout line from `command` is delivered to Claude as a notification during the session. For the full schema, including the `when` trigger and variable substitution, see [Monitors](https://code.claude.com/docs/en/plugins-reference#monitors).
### 
[​](https://code.claude.com/docs/en/plugins#ship-default-settings-with-your-plugin)
Ship default settings with your plugin
Plugins can include a `settings.json` file at the plugin root to apply default configuration when the plugin is enabled. Currently, only the `agent` and `subagentStatusLine` keys are supported. Setting `agent` activates one of the plugin’s [custom agents](https://code.claude.com/docs/en/sub-agents) as the main thread, applying its system prompt, tool restrictions, and model. This lets a plugin change how Claude Code behaves by default when enabled.
settings.json

```
{
  "agent": "security-reviewer"
}

```

This example activates the `security-reviewer` agent defined in the plugin’s `agents/` directory. Settings from `settings.json` take priority over `settings` declared in `plugin.json`. Unknown keys are silently ignored.
### 
[​](https://code.claude.com/docs/en/plugins#organize-complex-plugins)
Organize complex plugins
For plugins with many components, organize your directory structure by functionality. For complete directory layouts and organization patterns, see [Plugin directory structure](https://code.claude.com/docs/en/plugins-reference#plugin-directory-structure).
### 
[​](https://code.claude.com/docs/en/plugins#test-your-plugins-locally)
Test your plugins locally
Use the `--plugin-dir` flag to test plugins during development. This loads your plugin directly without requiring installation.

```
claude --plugin-dir ./my-plugin

```

When a `--plugin-dir` plugin has the same name as an installed marketplace plugin, the local copy takes precedence for that session. This lets you test changes to a plugin you already have installed without uninstalling it first. Marketplace plugins force-enabled by managed settings are the only exception and cannot be overridden. As you make changes to your plugin, run `/reload-plugins` to pick up the updates without restarting. This reloads plugins, skills, agents, hooks, plugin MCP servers, and plugin LSP servers. Test your plugin components:
  * Try your skills with `/plugin-name:skill-name`
  * Check that agents appear in `/agents`
  * Verify hooks work as expected


You can load multiple plugins at once by specifying the flag multiple times:

```
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two

```

### 
[​](https://code.claude.com/docs/en/plugins#debug-plugin-issues)
Debug plugin issues
If your plugin isn’t working as expected:
  1. **Check the structure** : Ensure your directories are at the plugin root, not inside `.claude-plugin/`
  2. **Test components individually** : Check each skill, agent, and hook separately
  3. **Use validation and debugging tools** : See [Debugging and development tools](https://code.claude.com/docs/en/plugins-reference#debugging-and-development-tools) for CLI commands and troubleshooting techniques


### 
[​](https://code.claude.com/docs/en/plugins#share-your-plugins)
Share your plugins
When your plugin is ready to share:
  1. **Add documentation** : Include a `README.md` with installation and usage instructions
  2. **Choose a versioning strategy** : Decide whether to set an explicit `version` or rely on the git commit SHA. See [version management](https://code.claude.com/docs/en/plugins-reference#version-management)
  3. **Create or use a marketplace** : Distribute through [plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) for installation
  4. **Test with others** : Have team members test the plugin before wider distribution

Once your plugin is in a marketplace, others can install it using the instructions in [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins). To keep a plugin internal to your team, host the marketplace in a [private repository](https://code.claude.com/docs/en/plugin-marketplaces#private-repositories).
### 
[​](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-official-marketplace)
Submit your plugin to the official marketplace
To submit a plugin to the official Anthropic marketplace, use one of the in-app submission forms:
  * **Claude.ai** : [claude.ai/settings/plugins/submit](https://claude.ai/settings/plugins/submit)
  * **Console** : [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit)

Once your plugin is listed, you can have your own CLI prompt Claude Code users to install it. See [Recommend your plugin from your CLI](https://code.claude.com/docs/en/plugin-hints).
For complete technical specifications, debugging techniques, and distribution strategies, see [Plugins reference](https://code.claude.com/docs/en/plugins-reference).
## 
[​](https://code.claude.com/docs/en/plugins#convert-existing-configurations-to-plugins)
Convert existing configurations to plugins
If you already have skills or hooks in your `.claude/` directory, you can convert them into a plugin for easier sharing and distribution.
### 
[​](https://code.claude.com/docs/en/plugins#migration-steps)
Migration steps
1
[](https://code.claude.com/docs/en/plugins)
Create the plugin structure
Create a new plugin directory:

```
mkdir -p my-plugin/.claude-plugin

```

Create the manifest file at `my-plugin/.claude-plugin/plugin.json`:
my-plugin/.claude-plugin/plugin.json

```
{
  "name": "my-plugin",
  "description": "Migrated from standalone configuration",
  "version": "1.0.0"
}

```

2
[](https://code.claude.com/docs/en/plugins)
Copy your existing files
Copy your existing configurations to the plugin directory:

```
# Copy commands
cp -r .claude/commands my-plugin/

# Copy agents (if any)
cp -r .claude/agents my-plugin/

# Copy skills (if any)
cp -r .claude/skills my-plugin/

```

3
[](https://code.claude.com/docs/en/plugins)
Migrate hooks
If you have hooks in your settings, create a hooks directory:

```
mkdir my-plugin/hooks

```

Create `my-plugin/hooks/hooks.json` with your hooks configuration. Copy the `hooks` object from your `.claude/settings.json` or `settings.local.json`, since the format is the same. The command receives hook input as JSON on stdin, so use `jq` to extract the file path:
my-plugin/hooks/hooks.json

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npm run lint:fix" }]
      }
    ]
  }
}

```

4
[](https://code.claude.com/docs/en/plugins)
Test your migrated plugin
Load your plugin to verify everything works:

```
claude --plugin-dir ./my-plugin

```

Test each component: run your commands, check agents appear in `/agents`, and verify hooks trigger correctly.
### 
[​](https://code.claude.com/docs/en/plugins#what-changes-when-migrating)
What changes when migrating  
| Standalone (`.claude/`)  | Plugin  |  
| --- | --- |  
| Only available in one project  | Can be shared via marketplaces  |  
| Files in `.claude/commands/`  | Files in `plugin-name/commands/`  |  
| Hooks in `settings.json`  | Hooks in `hooks/hooks.json`  |  
| Must manually copy to share  | Install with `/plugin install`  |  
After migrating, you can remove the original files from `.claude/` to avoid duplicates. The plugin version will take precedence when loaded.
## 
[​](https://code.claude.com/docs/en/plugins#next-steps)
Next steps
Now that you understand Claude Code’s plugin system, here are suggested paths for different goals:
### 
[​](https://code.claude.com/docs/en/plugins#for-plugin-users)
For plugin users
  * [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins): browse marketplaces and install plugins
  * [Configure team marketplaces](https://code.claude.com/docs/en/discover-plugins#configure-team-marketplaces): set up repository-level plugins for your team


### 
[​](https://code.claude.com/docs/en/plugins#for-plugin-developers)
For plugin developers
  * [Create and distribute a marketplace](https://code.claude.com/docs/en/plugin-marketplaces): package and share your plugins
  * [Plugins reference](https://code.claude.com/docs/en/plugins-reference): complete technical specifications
  * Dive deeper into specific plugin components:
    * [Skills](https://code.claude.com/docs/en/skills): skill development details
    * [Subagents](https://code.claude.com/docs/en/sub-agents): agent configuration and capabilities
    * [Hooks](https://code.claude.com/docs/en/hooks): event handling and automation
    * [MCP](https://code.claude.com/docs/en/mcp): external tool integration


Was this page helpful?
YesNo
[Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)[Extend Claude with skills](https://code.claude.com/docs/en/skills)
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
[Privacy choices](https://code.claude.com/docs/en/plugins)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
