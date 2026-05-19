<!--
url: https://code.claude.com/docs/en/jetbrains
download_date: 2026-04-29
website: claude-code
webpage: jetbrains
-->

# Jetbrains

[Skip to main content](https://code.claude.com/docs/en/jetbrains#content-area)
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
Platforms and integrations
JetBrains IDEs
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Getting started
  * [Overview](https://code.claude.com/docs/en/overview)
  * [Quickstart](https://code.claude.com/docs/en/quickstart)
  * [Changelog](https://code.claude.com/docs/en/changelog)


##### Core concepts
  * [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
  * [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
  * [Explore the .claude directory](https://code.claude.com/docs/en/claude-directory)
  * [Explore the context window](https://code.claude.com/docs/en/context-window)


##### Use Claude Code
  * [Store instructions and memories](https://code.claude.com/docs/en/memory)
  * [Permission modes](https://code.claude.com/docs/en/permission-modes)
  * [Common workflows](https://code.claude.com/docs/en/common-workflows)
  * [Best practices](https://code.claude.com/docs/en/best-practices)


##### Platforms and integrations
  * [Overview](https://code.claude.com/docs/en/platforms)
  * [Remote Control](https://code.claude.com/docs/en/remote-control)
  * Claude Code on the web
  * Claude Code on desktop
  * [Chrome extension (beta)](https://code.claude.com/docs/en/chrome)
  * [Computer use (preview)](https://code.claude.com/docs/en/computer-use)
  * [Visual Studio Code](https://code.claude.com/docs/en/vs-code)
  * [JetBrains IDEs](https://code.claude.com/docs/en/jetbrains)
  * Code review & CI/CD
  * [Claude Code in Slack](https://code.claude.com/docs/en/slack)


On this page
  * [Supported IDEs](https://code.claude.com/docs/en/jetbrains#supported-ides)
  * [Features](https://code.claude.com/docs/en/jetbrains#features)
  * [Installation](https://code.claude.com/docs/en/jetbrains#installation)
  * [Marketplace installation](https://code.claude.com/docs/en/jetbrains#marketplace-installation)
  * [Usage](https://code.claude.com/docs/en/jetbrains#usage)
  * [From your IDE](https://code.claude.com/docs/en/jetbrains#from-your-ide)
  * [From external terminals](https://code.claude.com/docs/en/jetbrains#from-external-terminals)
  * [Configuration](https://code.claude.com/docs/en/jetbrains#configuration)
  * [Claude Code settings](https://code.claude.com/docs/en/jetbrains#claude-code-settings)
  * [Plugin settings](https://code.claude.com/docs/en/jetbrains#plugin-settings)
  * [General settings](https://code.claude.com/docs/en/jetbrains#general-settings)
  * [ESC key configuration](https://code.claude.com/docs/en/jetbrains#esc-key-configuration)
  * [Special configurations](https://code.claude.com/docs/en/jetbrains#special-configurations)
  * [Remote development](https://code.claude.com/docs/en/jetbrains#remote-development)
  * [WSL configuration](https://code.claude.com/docs/en/jetbrains#wsl-configuration)
  * [Allow WSL2 traffic through Windows Firewall](https://code.claude.com/docs/en/jetbrains#allow-wsl2-traffic-through-windows-firewall)
  * [Switch WSL2 to mirrored networking](https://code.claude.com/docs/en/jetbrains#switch-wsl2-to-mirrored-networking)
  * [Troubleshooting](https://code.claude.com/docs/en/jetbrains#troubleshooting)
  * [Plugin not working](https://code.claude.com/docs/en/jetbrains#plugin-not-working)
  * [IDE not detected](https://code.claude.com/docs/en/jetbrains#ide-not-detected)
  * [Command not found](https://code.claude.com/docs/en/jetbrains#command-not-found)
  * [Security considerations](https://code.claude.com/docs/en/jetbrains#security-considerations)


Platforms and integrations
# JetBrains IDEs
Copy page
Use Claude Code with JetBrains IDEs including IntelliJ, PyCharm, WebStorm, and more
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Claude Code integrates with JetBrains IDEs through a dedicated plugin, providing features like interactive diff viewing, selection context sharing, and more.
## 
[​](https://code.claude.com/docs/en/jetbrains#supported-ides)
Supported IDEs
The Claude Code plugin works with most JetBrains IDEs, including:
  * IntelliJ IDEA
  * PyCharm
  * Android Studio
  * WebStorm
  * PhpStorm
  * GoLand


## 
[​](https://code.claude.com/docs/en/jetbrains#features)
Features
  * **Quick launch** : use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open Claude Code directly from your editor, or click the Claude Code button in the UI
  * **Diff viewing** : code changes can be displayed directly in the IDE diff viewer instead of the terminal
  * **Selection context** : the current selection or tab in the IDE is automatically shared with Claude Code
  * **File reference shortcuts** : use `Cmd+Option+K` (Mac) or `Alt+Ctrl+K` (Linux/Windows) to insert file references such as `@src/auth.ts#L1-99`
  * **Diagnostic sharing** : diagnostic errors from the IDE, such as lint and syntax errors, are automatically shared with Claude as you work


## 
[​](https://code.claude.com/docs/en/jetbrains#installation)
Installation
### 
[​](https://code.claude.com/docs/en/jetbrains#marketplace-installation)
Marketplace installation
Find and install the [Claude Code plugin](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-) from the JetBrains marketplace and restart your IDE. If you haven’t installed Claude Code yet, see the [quickstart guide](https://code.claude.com/docs/en/quickstart) for installation instructions.
After installing the plugin, you may need to restart your IDE completely for it to take effect.
## 
[​](https://code.claude.com/docs/en/jetbrains#usage)
Usage
### 
[​](https://code.claude.com/docs/en/jetbrains#from-your-ide)
From your IDE
Run `claude` from your IDE’s integrated terminal, and all integration features will be active.
### 
[​](https://code.claude.com/docs/en/jetbrains#from-external-terminals)
From external terminals
Use the `/ide` command in any external terminal to connect Claude Code to your JetBrains IDE and activate all features:

```
claude

```


```
/ide

```

If you want Claude to have access to the same files as your IDE, start Claude Code from the same directory as your IDE project root.
## 
[​](https://code.claude.com/docs/en/jetbrains#configuration)
Configuration
### 
[​](https://code.claude.com/docs/en/jetbrains#claude-code-settings)
Claude Code settings
Configure IDE integration through Claude Code’s settings:
  1. Run `claude`
  2. Enter the `/config` command
  3. Set the diff tool to `auto` to show diffs in the IDE, or `terminal` to keep them in the terminal


### 
[​](https://code.claude.com/docs/en/jetbrains#plugin-settings)
Plugin settings
Configure the Claude Code plugin by going to **Settings → Tools → Claude Code [Beta]** :
#### 
[​](https://code.claude.com/docs/en/jetbrains#general-settings)
General settings
  * **Claude command** : specify a custom command to run Claude, for example `claude`, `/usr/local/bin/claude`, or `npx @anthropic-ai/claude-code`
  * **Suppress notification for Claude command not found** : skip notifications about not finding the Claude command
  * **Enable using Option+Enter for multi-line prompts** : on macOS only. When enabled, Option+Enter inserts new lines in Claude Code prompts. Disable if the Option key is being captured unexpectedly. Requires a terminal restart.
  * **Enable automatic updates** : automatically check for and install plugin updates, applied on restart


For WSL users: Set `wsl -d Ubuntu -- bash -lic "claude"` as your Claude command (replace `Ubuntu` with your WSL distribution name)
#### 
[​](https://code.claude.com/docs/en/jetbrains#esc-key-configuration)
ESC key configuration
If the ESC key doesn’t interrupt Claude Code operations in JetBrains terminals:
  1. Go to **Settings → Tools → Terminal**
  2. Either:
     * Uncheck “Move focus to the editor with Escape”, or
     * Click “Configure terminal keybindings” and delete the “Switch focus to Editor” shortcut
  3. Apply the changes

This allows the ESC key to properly interrupt Claude Code operations.
## 
[​](https://code.claude.com/docs/en/jetbrains#special-configurations)
Special configurations
### 
[​](https://code.claude.com/docs/en/jetbrains#remote-development)
Remote development
When using JetBrains Remote Development, you must install the plugin in the remote host via **Settings → Plugin (Host)**.
The plugin must be installed on the remote host, not on your local client machine.
### 
[​](https://code.claude.com/docs/en/jetbrains#wsl-configuration)
WSL configuration
If you’re using Claude Code on WSL2 with a JetBrains IDE and see “No available IDEs detected”, the cause is usually WSL2’s NAT networking or Windows Firewall blocking the connection between WSL2 and the IDE running on the Windows host. WSL1 uses the host’s network directly and isn’t affected.
#### 
[​](https://code.claude.com/docs/en/jetbrains#allow-wsl2-traffic-through-windows-firewall)
Allow WSL2 traffic through Windows Firewall
This is the recommended fix because it keeps your existing WSL2 networking mode.
1
[](https://code.claude.com/docs/en/jetbrains)
Find your WSL2 IP address
From inside your WSL shell, run:

```
hostname -I

```

Note the subnet, for example `172.21.123.45` is in `172.21.0.0/16`.
2
[](https://code.claude.com/docs/en/jetbrains)
Create a firewall rule
Open PowerShell as Administrator and run the following, adjusting the IP range to match your subnet:

```
New-NetFirewallRule -DisplayName "Allow WSL2 Internal Traffic" -Direction Inbound -Protocol TCP -Action Allow -RemoteAddress 172.21.0.0/16 -LocalAddress 172.21.0.0/16

```

3
[](https://code.claude.com/docs/en/jetbrains)
Restart your IDE and Claude Code
Close and reopen both so the new rule takes effect.
#### 
[​](https://code.claude.com/docs/en/jetbrains#switch-wsl2-to-mirrored-networking)
Switch WSL2 to mirrored networking
Mirrored networking requires Windows 11 22H2 or later. If you’re on Windows 10, use the firewall rule above instead. Add this to `.wslconfig` in your Windows user directory:

```
[wsl2]
networkingMode=mirrored

```

Then restart WSL with `wsl --shutdown` from PowerShell.
## 
[​](https://code.claude.com/docs/en/jetbrains#troubleshooting)
Troubleshooting
### 
[​](https://code.claude.com/docs/en/jetbrains#plugin-not-working)
Plugin not working
If the plugin is installed but Claude Code features don’t appear in your IDE:
  * Ensure you’re running Claude Code from the project root directory
  * Check that the JetBrains plugin is enabled in the IDE settings
  * Completely restart the IDE (you may need to do this multiple times)
  * For Remote Development, ensure the plugin is installed in the remote host


### 
[​](https://code.claude.com/docs/en/jetbrains#ide-not-detected)
IDE not detected
If running `claude` shows “No available IDEs detected”:
  * Verify the plugin is installed and enabled
  * Restart the IDE completely
  * Check that you’re running Claude Code from the integrated terminal
  * For WSL users, see [WSL configuration](https://code.claude.com/docs/en/jetbrains#wsl-configuration) above


### 
[​](https://code.claude.com/docs/en/jetbrains#command-not-found)
Command not found
If clicking the Claude icon shows “command not found”:
  1. Verify Claude Code is installed by running `claude --version` in a terminal
  2. Configure the Claude command path in plugin settings
  3. For WSL users, use the WSL command format mentioned in the configuration section


## 
[​](https://code.claude.com/docs/en/jetbrains#security-considerations)
Security considerations
When Claude Code runs in a JetBrains IDE with auto-edit permissions enabled, it may be able to modify IDE configuration files that can be automatically executed by your IDE. This may increase the risk of running Claude Code in auto-edit mode and allow bypassing Claude Code’s permission prompts for bash execution. When running in JetBrains IDEs, consider:
  * Using manual approval mode for edits
  * Taking extra care to ensure Claude is only used with trusted prompts
  * Being aware of which files Claude Code has access to modify

For Claude Code installation or login problems outside the IDE, see [Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install).
Was this page helpful?
YesNo
[Visual Studio Code](https://code.claude.com/docs/en/vs-code)[Code Review](https://code.claude.com/docs/en/code-review)
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
[Privacy choices](https://code.claude.com/docs/en/jetbrains)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
