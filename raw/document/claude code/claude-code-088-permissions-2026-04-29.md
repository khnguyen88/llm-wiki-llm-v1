<!--
url: https://code.claude.com/docs/en/permissions
download_date: 2026-04-29
website: claude-code
webpage: permissions
-->

# Permissions

[Skip to main content](https://code.claude.com/docs/en/permissions#content-area)
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
Settings and permissions
Configure permissions
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Settings and permissions
  * [Settings](https://code.claude.com/docs/en/settings)
  * [Permissions](https://code.claude.com/docs/en/permissions)
  * [Sandboxing](https://code.claude.com/docs/en/sandboxing)


##### Model and responses
  * [Model configuration](https://code.claude.com/docs/en/model-config)
  * [Speed up responses with fast mode](https://code.claude.com/docs/en/fast-mode)
  * [Output styles](https://code.claude.com/docs/en/output-styles)


##### Interface
  * [Terminal configuration](https://code.claude.com/docs/en/terminal-config)
  * [Fullscreen rendering](https://code.claude.com/docs/en/fullscreen)
  * [Voice dictation](https://code.claude.com/docs/en/voice-dictation)
  * [Customize status line](https://code.claude.com/docs/en/statusline)
  * [Customize keyboard shortcuts](https://code.claude.com/docs/en/keybindings)


On this page
  * [Permission system](https://code.claude.com/docs/en/permissions#permission-system)
  * [Manage permissions](https://code.claude.com/docs/en/permissions#manage-permissions)
  * [Permission modes](https://code.claude.com/docs/en/permissions#permission-modes)
  * [Permission rule syntax](https://code.claude.com/docs/en/permissions#permission-rule-syntax)
  * [Match all uses of a tool](https://code.claude.com/docs/en/permissions#match-all-uses-of-a-tool)
  * [Use specifiers for fine-grained control](https://code.claude.com/docs/en/permissions#use-specifiers-for-fine-grained-control)
  * [Wildcard patterns](https://code.claude.com/docs/en/permissions#wildcard-patterns)
  * [Tool-specific permission rules](https://code.claude.com/docs/en/permissions#tool-specific-permission-rules)
  * [Bash](https://code.claude.com/docs/en/permissions#bash)
  * [Compound commands](https://code.claude.com/docs/en/permissions#compound-commands)
  * [Process wrappers](https://code.claude.com/docs/en/permissions#process-wrappers)
  * [Read-only commands](https://code.claude.com/docs/en/permissions#read-only-commands)
  * [Read and Edit](https://code.claude.com/docs/en/permissions#read-and-edit)
  * [WebFetch](https://code.claude.com/docs/en/permissions#webfetch)
  * [MCP](https://code.claude.com/docs/en/permissions#mcp)
  * [Agent (subagents)](https://code.claude.com/docs/en/permissions#agent-subagents)
  * [Extend permissions with hooks](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks)
  * [Working directories](https://code.claude.com/docs/en/permissions#working-directories)
  * [Additional directories grant file access, not configuration](https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration)
  * [How permissions interact with sandboxing](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)
  * [Managed settings](https://code.claude.com/docs/en/permissions#managed-settings)
  * [Managed-only settings](https://code.claude.com/docs/en/permissions#managed-only-settings)
  * [Settings precedence](https://code.claude.com/docs/en/permissions#settings-precedence)
  * [Example configurations](https://code.claude.com/docs/en/permissions#example-configurations)
  * [See also](https://code.claude.com/docs/en/permissions#see-also)


Settings and permissions
# Configure permissions
Copy page
Control what Claude Code can access and do with fine-grained permission rules, modes, and managed policies.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Claude Code supports fine-grained permissions so that you can specify exactly what the agent is allowed to do and what it cannot. Permission settings can be checked into version control and distributed to all developers in your organization, as well as customized by individual developers.
## 
[​](https://code.claude.com/docs/en/permissions#permission-system)
Permission system
Claude Code uses a tiered permission system to balance power and safety:  
| Tool type  | Example  | Approval required  | ”Yes, don’t ask again” behavior  |  
| --- | --- | --- | --- |  
| Read-only  | File reads, Grep  | No  | N/A  |  
| Bash commands  | Shell execution  | Yes  | Permanently per project directory and command  |  
| File modification  | Edit/write files  | Yes  | Until session end  |  
## 
[​](https://code.claude.com/docs/en/permissions#manage-permissions)
Manage permissions
You can view and manage Claude Code’s tool permissions with `/permissions`. This UI lists all permission rules and the settings.json file they are sourced from.
  * **Allow** rules let Claude Code use the specified tool without manual approval.
  * **Ask** rules prompt for confirmation whenever Claude Code tries to use the specified tool.
  * **Deny** rules prevent Claude Code from using the specified tool.

Rules are evaluated in order: **deny - > ask -> allow**. The first matching rule wins, so deny rules always take precedence.
## 
[​](https://code.claude.com/docs/en/permissions#permission-modes)
Permission modes
Claude Code supports several permission modes that control how tools are approved. See [Permission modes](https://code.claude.com/docs/en/permission-modes) for when to use each one. Set the `defaultMode` in your [settings files](https://code.claude.com/docs/en/settings#settings-files):  
| Mode  | Description  |  
| --- | --- |  
| `default`  | Standard behavior: prompts for permission on first use of each tool  |  
| `acceptEdits`  | Automatically accepts file edits and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.) for paths in the working directory or `additionalDirectories`  |  
| `plan`  | Plan Mode: Claude can analyze but not modify files or execute commands  |  
| `auto`  | Auto-approves tool calls with background safety checks that verify actions align with your request. Currently a research preview  |  
| `dontAsk`  | Auto-denies tools unless pre-approved via `/permissions` or `permissions.allow` rules  |  
| `bypassPermissions`  | Skips permission prompts except for writes to protected directories (see warning below)  |  
`bypassPermissions` mode skips permission prompts. Writes to `.git`, `.claude`, `.vscode`, `.idea`, and `.husky` directories still prompt for confirmation to prevent accidental corruption of repository state, editor configuration, and git hooks. Writes to `.claude/commands`, `.claude/agents`, and `.claude/skills` are exempt and do not prompt, because Claude routinely writes there when creating skills, subagents, and commands. Only use this mode in isolated environments like containers or VMs where Claude Code cannot cause damage. Administrators can prevent this mode by setting `permissions.disableBypassPermissionsMode` to `"disable"` in [managed settings](https://code.claude.com/docs/en/permissions#managed-settings).
To prevent `bypassPermissions` or `auto` mode from being used, set `permissions.disableBypassPermissionsMode` or `permissions.disableAutoMode` to `"disable"` in any [settings file](https://code.claude.com/docs/en/settings#settings-files). These are most useful in [managed settings](https://code.claude.com/docs/en/permissions#managed-settings) where they cannot be overridden.
## 
[​](https://code.claude.com/docs/en/permissions#permission-rule-syntax)
Permission rule syntax
Permission rules follow the format `Tool` or `Tool(specifier)`.
### 
[​](https://code.claude.com/docs/en/permissions#match-all-uses-of-a-tool)
Match all uses of a tool
To match all uses of a tool, use just the tool name without parentheses:  
| Rule  | Effect  |  
| --- | --- |  
| `Bash`  | Matches all Bash commands  |  
| `WebFetch`  | Matches all web fetch requests  |  
| `Read`  | Matches all file reads  |  
`Bash(*)` is equivalent to `Bash` and matches all Bash commands.
### 
[​](https://code.claude.com/docs/en/permissions#use-specifiers-for-fine-grained-control)
Use specifiers for fine-grained control
Add a specifier in parentheses to match specific tool uses:  
| Rule  | Effect  |  
| --- | --- |  
| `Bash(npm run build)`  | Matches the exact command `npm run build`  |  
| `Read(./.env)`  | Matches reading the `.env` file in the current directory  |  
| `WebFetch(domain:example.com)`  | Matches fetch requests to example.com  |  
### 
[​](https://code.claude.com/docs/en/permissions#wildcard-patterns)
Wildcard patterns
Bash rules support glob patterns with `*`. Wildcards can appear at any position in the command. This configuration allows npm and git commit commands while blocking git push:

```
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git commit *)",
      "Bash(git * main)",
      "Bash(* --version)",
      "Bash(* --help *)"
    ],
    "deny": [
      "Bash(git push *)"
    ]
  }
}

```

The space before `*` matters: `Bash(ls *)` matches `ls -la` but not `lsof`, while `Bash(ls*)` matches both. The `:*` suffix is an equivalent way to write a trailing wildcard, so `Bash(ls:*)` matches the same commands as `Bash(ls *)`. The permission dialog writes the space-separated form when you select “Yes, don’t ask again” for a command prefix. The `:*` form is only recognized at the end of a pattern. In a pattern like `Bash(git:* push)`, the colon is treated as a literal character and won’t match git commands.
## 
[​](https://code.claude.com/docs/en/permissions#tool-specific-permission-rules)
Tool-specific permission rules
### 
[​](https://code.claude.com/docs/en/permissions#bash)
Bash
Bash permission rules support wildcard matching with `*`. Wildcards can appear at any position in the command, including at the beginning, middle, or end:
  * `Bash(npm run build)` matches the exact Bash command `npm run build`
  * `Bash(npm run test *)` matches Bash commands starting with `npm run test`
  * `Bash(npm *)` matches any command starting with `npm `
  * `Bash(* install)` matches any command ending with ` install`
  * `Bash(git * main)` matches commands like `git checkout main` and `git log --oneline main`

A single `*` matches any sequence of characters including spaces, so one wildcard can span multiple arguments. `Bash(git *)` matches `git log --oneline --all`, and `Bash(git * main)` matches `git push origin main` as well as `git merge main`. When `*` appears at the end with a space before it (like `Bash(ls *)`), it enforces a word boundary, requiring the prefix to be followed by a space or end-of-string. For example, `Bash(ls *)` matches `ls -la` but not `lsof`. In contrast, `Bash(ls*)` without a space matches both `ls -la` and `lsof` because there’s no word boundary constraint.
#### 
[​](https://code.claude.com/docs/en/permissions#compound-commands)
Compound commands
Claude Code is aware of shell operators, so a rule like `Bash(safe-cmd *)` won’t give it permission to run the command `safe-cmd && other-cmd`. The recognized command separators are `&&`, `||`, `;`, `|`, `|&`, `&`, and newlines. A rule must match each subcommand independently.
When you approve a compound command with “Yes, don’t ask again”, Claude Code saves a separate rule for each subcommand that requires approval, rather than a single rule for the full compound string. For example, approving `git status && npm test` saves a rule for `npm test`, so future `npm test` invocations are recognized regardless of what precedes the `&&`. Subcommands like `cd` into a subdirectory generate their own Read rule for that path. Up to 5 rules may be saved for a single compound command.
#### 
[​](https://code.claude.com/docs/en/permissions#process-wrappers)
Process wrappers
Before matching Bash rules, Claude Code strips a fixed set of process wrappers so a rule like `Bash(npm test *)` also matches `timeout 30 npm test`. The recognized wrappers are `timeout`, `time`, `nice`, `nohup`, and `stdbuf`. Bare `xargs` is also stripped, so `Bash(grep *)` matches `xargs grep pattern`. Stripping applies only when `xargs` has no flags: an invocation like `xargs -n1 grep pattern` is matched as an `xargs` command, so rules written for the inner command do not cover it. This wrapper list is built in and is not configurable. Development environment runners such as `direnv exec`, `devbox run`, `mise exec`, `npx`, and `docker exec` are not in the list. Because these tools execute their arguments as a command, a rule like `Bash(devbox run *)` matches whatever comes after `run`, including `devbox run rm -rf .`. To approve work inside an environment runner, write a specific rule that includes both the runner and the inner command, such as `Bash(devbox run npm test)`. Add one rule per inner command you want to allow. Exec wrappers such as `watch`, `setsid`, `ionice`, and `flock` always prompt and cannot be auto-approved by a prefix rule like `Bash(watch *)`. The same applies to `find` with `-exec` or `-delete`: a `Bash(find *)` rule does not cover these forms. To approve a specific invocation, write an exact-match rule for the full command string.
#### 
[​](https://code.claude.com/docs/en/permissions#read-only-commands)
Read-only commands
Claude Code recognizes a built-in set of Bash commands as read-only and runs them without a permission prompt in every mode. These include `ls`, `cat`, `head`, `tail`, `grep`, `find`, `wc`, `diff`, `stat`, `du`, `cd`, and read-only forms of `git`. The set is not configurable; to require a prompt for one of these commands, add an `ask` or `deny` rule for it. Unquoted glob patterns are permitted for commands whose every flag is read-only, so `ls *.ts` and `wc -l src/*.py` run without a prompt. Commands with write-capable or exec-capable flags, such as `find`, `sort`, `sed`, and `git`, still prompt when an unquoted glob is present because the glob could expand to a flag like `-delete`. A `cd` into a path inside your working directory or an [additional directory](https://code.claude.com/docs/en/permissions#working-directories) is also read-only. A compound command like `cd packages/api && ls` runs without a prompt when each part qualifies on its own. Combining `cd` with `git` in one compound command always prompts, regardless of the target directory.
Bash permission patterns that try to constrain command arguments are fragile. For example, `Bash(curl http://github.com/ *)` intends to restrict curl to GitHub URLs, but won’t match variations like:
  * Options before URL: `curl -X GET http://github.com/...`
  * Different protocol: `curl https://github.com/...`
  * Redirects: `curl -L http://bit.ly/xyz` (redirects to github)
  * Variables: `URL=http://github.com && curl $URL`
  * Extra spaces: `curl  http://github.com`

For more reliable URL filtering, consider:
  * **Restrict Bash network tools** : use deny rules to block `curl`, `wget`, and similar commands, then use the WebFetch tool with `WebFetch(domain:github.com)` permission for allowed domains
  * **Use PreToolUse hooks** : implement a hook that validates URLs in Bash commands and blocks disallowed domains
  * Instructing Claude Code about your allowed curl patterns via CLAUDE.md

Note that using WebFetch alone does not prevent network access. If Bash is allowed, Claude can still use `curl`, `wget`, or other tools to reach any URL.
### 
[​](https://code.claude.com/docs/en/permissions#read-and-edit)
Read and Edit
`Edit` rules apply to all built-in tools that edit files. Claude makes a best-effort attempt to apply `Read` rules to all built-in tools that read files like Grep and Glob.
Read and Edit deny rules apply to Claude’s built-in file tools, not to Bash subprocesses. A `Read(./.env)` deny rule blocks the Read tool but does not prevent `cat .env` in Bash. For OS-level enforcement that blocks all processes from accessing a path, [enable the sandbox](https://code.claude.com/docs/en/sandboxing).
Read and Edit rules both follow the [gitignore](https://git-scm.com/docs/gitignore) specification with four distinct pattern types:  
| Pattern  | Meaning  | Example  | Matches  |  
| --- | --- | --- | --- |  
| `//path`  |  **Absolute** path from filesystem root  | `Read(//Users/alice/secrets/**)`  | `/Users/alice/secrets/**`  |  
| `~/path`  | Path from **home** directory  | `Read(~/Documents/*.pdf)`  | `/Users/alice/Documents/*.pdf`  |  
| `/path`  | Path **relative to project root**  | `Edit(/src/**/*.ts)`  | `<project root>/src/**/*.ts`  |  
|  `path` or `./path`  | Path **relative to current directory**  | `Read(*.env)`  | `<cwd>/*.env`  |  
A pattern like `/Users/alice/file` is NOT an absolute path. It’s relative to the project root. Use `//Users/alice/file` for absolute paths.
On Windows, paths are normalized to POSIX form before matching. `C:\Users\alice` becomes `/c/Users/alice`, so use `//c/**/.env` to match `.env` files anywhere on that drive. To match across all drives, use `//**/.env`. Examples:
  * `Edit(/docs/**)`: edits in `<project>/docs/` (NOT `/docs/` and NOT `<project>/.claude/docs/`)
  * `Read(~/.zshrc)`: reads your home directory’s `.zshrc`
  * `Edit(//tmp/scratch.txt)`: edits the absolute path `/tmp/scratch.txt`
  * `Read(src/**)`: reads from `<current-directory>/src/`


In gitignore patterns, `*` matches files in a single directory while `**` matches recursively across directories. To allow all file access, use just the tool name without parentheses: `Read`, `Edit`, or `Write`.
When Claude accesses a symlink, permission rules check two paths: the symlink itself and the file it resolves to. Allow and deny rules treat that pair differently: allow rules fall back to prompting you, while deny rules block outright.
  * **Allow rules** : apply only when both the symlink path and its target match. A symlink inside an allowed directory that points outside it still prompts you.
  * **Deny rules** : apply when either the symlink path or its target matches. A symlink that points to a denied file is itself denied.

For example, with `Read(./project/**)` allowed and `Read(~/.ssh/**)` denied, a symlink at `./project/key` pointing to `~/.ssh/id_rsa` is blocked: the target fails the allow rule and matches the deny rule.
### 
[​](https://code.claude.com/docs/en/permissions#webfetch)
WebFetch
  * `WebFetch(domain:example.com)` matches fetch requests to example.com


### 
[​](https://code.claude.com/docs/en/permissions#mcp)
MCP
  * `mcp__puppeteer` matches any tool provided by the `puppeteer` server (name configured in Claude Code)
  * `mcp__puppeteer__*` wildcard syntax that also matches all tools from the `puppeteer` server
  * `mcp__puppeteer__puppeteer_navigate` matches the `puppeteer_navigate` tool provided by the `puppeteer` server


### 
[​](https://code.claude.com/docs/en/permissions#agent-subagents)
Agent (subagents)
Use `Agent(AgentName)` rules to control which [subagents](https://code.claude.com/docs/en/sub-agents) Claude can use:
  * `Agent(Explore)` matches the Explore subagent
  * `Agent(Plan)` matches the Plan subagent
  * `Agent(my-custom-agent)` matches a custom subagent named `my-custom-agent`

Add these rules to the `deny` array in your settings or use the `--disallowedTools` CLI flag to disable specific agents. To disable the Explore agent:

```
{
  "permissions": {
    "deny": ["Agent(Explore)"]
  }
}

```

## 
[​](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks)
Extend permissions with hooks
[Claude Code hooks](https://code.claude.com/docs/en/hooks-guide) provide a way to register custom shell commands to perform permission evaluation at runtime. When Claude Code makes a tool call, PreToolUse hooks run before the permission prompt. The hook output can deny the tool call, force a prompt, or skip the prompt to let the call proceed. Hook decisions do not bypass permission rules. Deny and ask rules are evaluated regardless of what a PreToolUse hook returns, so a matching deny rule blocks the call and a matching ask rule still prompts even when the hook returned `"allow"` or `"ask"`. This preserves the deny-first precedence described in [Manage permissions](https://code.claude.com/docs/en/permissions#manage-permissions), including deny rules set in managed settings. A blocking hook also takes precedence over allow rules. A hook that exits with code 2 stops the tool call before permission rules are evaluated, so the block applies even when an allow rule would otherwise let the call proceed. To run all Bash commands without prompts except for a few you want blocked, add `"Bash"` to your allow list and register a PreToolUse hook that rejects those specific commands. See [Block edits to protected files](https://code.claude.com/docs/en/hooks-guide#block-edits-to-protected-files) for a hook script you can adapt.
## 
[​](https://code.claude.com/docs/en/permissions#working-directories)
Working directories
By default, Claude has access to files in the directory where it was launched. You can extend this access:
  * **During startup** : use `--add-dir <path>` CLI argument
  * **During session** : use `/add-dir` command
  * **Persistent configuration** : add to `additionalDirectories` in [settings files](https://code.claude.com/docs/en/settings#settings-files)

Files in additional directories follow the same permission rules as the original working directory: they become readable without prompts, and file editing permissions follow the current permission mode.
### 
[​](https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration)
Additional directories grant file access, not configuration
Adding a directory extends where Claude can read and edit files. It does not make that directory a full configuration root: most `.claude/` configuration is not discovered from additional directories, though a few types are loaded as exceptions. The following configuration types are loaded from `--add-dir` directories:  
| Configuration  | Loaded from `--add-dir`  |  
| --- | --- |  
|  [Skills](https://code.claude.com/docs/en/skills) in `.claude/skills/`  | Yes, with live reload  |  
| Plugin settings in `.claude/settings.json`  |  `enabledPlugins` and `extraKnownMarketplaces` only  |  
|  [CLAUDE.md](https://code.claude.com/docs/en/memory) files, `.claude/rules/`, and `CLAUDE.local.md`  | Only when `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` is set. `CLAUDE.local.md` additionally requires the `local` setting source, which is enabled by default  |  
Everything else, including subagents, commands, output styles, hooks, and other settings, is discovered only from the current working directory and its parents, your user directory at `~/.claude/`, and managed settings. To share that configuration across projects, use one of these approaches:
  * **User-level configuration** : place files in `~/.claude/agents/`, `~/.claude/output-styles/`, or `~/.claude/settings.json` to make them available in every project
  * **Plugins** : package and distribute configuration as a [plugin](https://code.claude.com/docs/en/plugins) that teams can install
  * **Launch from the config directory** : run Claude Code from the directory containing the `.claude/` configuration you want


## 
[​](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)
How permissions interact with sandboxing
Permissions and [sandboxing](https://code.claude.com/docs/en/sandboxing) are complementary security layers:
  * **Permissions** control which tools Claude Code can use and which files or domains it can access. They apply to all tools (Bash, Read, Edit, WebFetch, MCP, and others).
  * **Sandboxing** provides OS-level enforcement that restricts the Bash tool’s filesystem and network access. It applies only to Bash commands and their child processes.

Use both for defense-in-depth:
  * Permission deny rules block Claude from even attempting to access restricted resources
  * Sandbox restrictions prevent Bash commands from reaching resources outside defined boundaries, even if a prompt injection bypasses Claude’s decision-making
  * Filesystem restrictions in the sandbox use Read and Edit deny rules, not separate sandbox configuration
  * Network restrictions combine WebFetch permission rules with the sandbox’s `allowedDomains` and `deniedDomains` lists

When sandboxing is enabled with `autoAllowBashIfSandboxed: true`, which is the default, sandboxed Bash commands run without prompting even if your permissions include `ask: Bash(*)`. The sandbox boundary substitutes for the per-command prompt. Explicit deny rules still apply, and `rm` or `rmdir` commands that target `/`, your home directory, or other critical system paths still trigger a prompt. See [sandbox modes](https://code.claude.com/docs/en/sandboxing#sandbox-modes) to change this behavior.
## 
[​](https://code.claude.com/docs/en/permissions#managed-settings)
Managed settings
For organizations that need centralized control over Claude Code configuration, administrators can deploy managed settings that cannot be overridden by user or project settings. These policy settings follow the same format as regular settings files and can be delivered through MDM/OS-level policies, managed settings files, or [server-managed settings](https://code.claude.com/docs/en/server-managed-settings). See [settings files](https://code.claude.com/docs/en/settings#settings-files) for delivery mechanisms and file locations.
### 
[​](https://code.claude.com/docs/en/permissions#managed-only-settings)
Managed-only settings
The following settings are only read from managed settings. Placing them in user or project settings files has no effect.  
| Setting  | Description  |  
| --- | --- |  
| `allowedChannelPlugins`  | Allowlist of channel plugins that may push messages. Replaces the default Anthropic allowlist when set. Requires `channelsEnabled: true`. See [Restrict which channel plugins can run](https://code.claude.com/docs/en/channels#restrict-which-channel-plugins-can-run)  |  
| `allowManagedHooksOnly`  | When `true`, only managed hooks, SDK hooks, and hooks from plugins force-enabled in managed settings `enabledPlugins` are loaded. User, project, and all other plugin hooks are blocked  |  
| `allowManagedMcpServersOnly`  | When `true`, only `allowedMcpServers` from managed settings are respected. `deniedMcpServers` still merges from all sources. See [Managed MCP configuration](https://code.claude.com/docs/en/mcp#managed-mcp-configuration)  |  
| `allowManagedPermissionRulesOnly`  | When `true`, prevents user and project settings from defining `allow`, `ask`, or `deny` permission rules. Only rules in managed settings apply  |  
| `blockedMarketplaces`  | Blocklist of marketplace sources. Blocked sources are checked before downloading, so they never touch the filesystem. See [managed marketplace restrictions](https://code.claude.com/docs/en/plugin-marketplaces#managed-marketplace-restrictions)  |  
| `channelsEnabled`  | Allow [channels](https://code.claude.com/docs/en/channels) for Team and Enterprise users. Unset or `false` blocks channel message delivery regardless of what users pass to `--channels`  |  
| `forceRemoteSettingsRefresh`  | When `true`, blocks CLI startup until remote managed settings are freshly fetched and exits if the fetch fails. See [fail-closed enforcement](https://code.claude.com/docs/en/server-managed-settings#enforce-fail-closed-startup)  |  
| `pluginTrustMessage`  | Custom message appended to the plugin trust warning shown before installation  |  
| `sandbox.filesystem.allowManagedReadPathsOnly`  | When `true`, only `filesystem.allowRead` paths from managed settings are respected. `denyRead` still merges from all sources  |  
| `sandbox.network.allowManagedDomainsOnly`  | When `true`, only `allowedDomains` and `WebFetch(domain:...)` allow rules from managed settings are respected. Non-allowed domains are blocked automatically without prompting the user. Denied domains still merge from all sources  |  
| `strictKnownMarketplaces`  | Controls which plugin marketplace sources users can add and install plugins from. See [managed marketplace restrictions](https://code.claude.com/docs/en/plugin-marketplaces#managed-marketplace-restrictions)  |  
| `wslInheritsWindowsSettings`  | When `true` in the Windows HKLM registry key or `C:\Program Files\ClaudeCode\managed-settings.json`, WSL reads managed settings from the Windows policy chain in addition to `/etc/claude-code`. See [Settings files](https://code.claude.com/docs/en/settings#settings-files)  |  
`disableBypassPermissionsMode` is typically placed in managed settings to enforce organizational policy, but it works from any scope. A user can set it in their own settings to lock themselves out of bypass mode.
Access to [Remote Control](https://code.claude.com/docs/en/remote-control) and [web sessions](https://code.claude.com/docs/en/claude-code-on-the-web) is not controlled by a managed settings key. On Team and Enterprise plans, an admin enables or disables these features in [Claude Code admin settings](https://claude.ai/admin-settings/claude-code).
## 
[​](https://code.claude.com/docs/en/permissions#settings-precedence)
Settings precedence
Permission rules follow the same [settings precedence](https://code.claude.com/docs/en/settings#settings-precedence) as all other Claude Code settings:
  1. **Managed settings** : cannot be overridden by any other level, including command line arguments
  2. **Command line arguments** : temporary session overrides
  3. **Local project settings** (`.claude/settings.local.json`)
  4. **Shared project settings** (`.claude/settings.json`)
  5. **User settings** (`~/.claude/settings.json`)

If a tool is denied at any level, no other level can allow it. For example, a managed settings deny cannot be overridden by `--allowedTools`, and `--disallowedTools` can add restrictions beyond what managed settings define. If a permission is allowed in user settings but denied in project settings, the project setting takes precedence and the permission is blocked.
## 
[​](https://code.claude.com/docs/en/permissions#example-configurations)
Example configurations
This [repository](https://github.com/anthropics/claude-code/tree/main/examples/settings) includes starter settings configurations for common deployment scenarios. Use these as starting points and adjust them to fit your needs.
## 
[​](https://code.claude.com/docs/en/permissions#see-also)
See also
  * [Settings](https://code.claude.com/docs/en/settings): complete configuration reference including the permission settings table
  * [Configure auto mode](https://code.claude.com/docs/en/auto-mode-config): tell the auto mode classifier which infrastructure your organization trusts
  * [Sandboxing](https://code.claude.com/docs/en/sandboxing): OS-level filesystem and network isolation for Bash commands
  * [Authentication](https://code.claude.com/docs/en/authentication): set up user access to Claude Code
  * [Security](https://code.claude.com/docs/en/security): security safeguards and best practices
  * [Hooks](https://code.claude.com/docs/en/hooks-guide): automate workflows and extend permission evaluation


Was this page helpful?
YesNo
[Settings](https://code.claude.com/docs/en/settings)[Sandboxing](https://code.claude.com/docs/en/sandboxing)
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
[Privacy choices](https://code.claude.com/docs/en/permissions)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
