<!--
url: https://code.claude.com/docs/en/agent-sdk/permissions
download_date: 2026-04-29
website: claude-code
webpage: agent-sdk-permissions
-->

# Agent Sdk Permissions

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/permissions#content-area)
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
Control and observability
Configure permissions
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
  * [How permissions are evaluated](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)
  * [Allow and deny rules](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)
  * [Permission modes](https://code.claude.com/docs/en/agent-sdk/permissions#permission-modes)
  * [Available modes](https://code.claude.com/docs/en/agent-sdk/permissions#available-modes)
  * [Set permission mode](https://code.claude.com/docs/en/agent-sdk/permissions#set-permission-mode)
  * [Mode details](https://code.claude.com/docs/en/agent-sdk/permissions#mode-details)
  * [Accept edits mode (acceptEdits)](https://code.claude.com/docs/en/agent-sdk/permissions#accept-edits-mode-acceptedits)
  * [Don’t ask mode (dontAsk)](https://code.claude.com/docs/en/agent-sdk/permissions#don%E2%80%99t-ask-mode-dontask)
  * [Bypass permissions mode (bypassPermissions)](https://code.claude.com/docs/en/agent-sdk/permissions#bypass-permissions-mode-bypasspermissions)
  * [Plan mode (plan)](https://code.claude.com/docs/en/agent-sdk/permissions#plan-mode-plan)
  * [Related resources](https://code.claude.com/docs/en/agent-sdk/permissions#related-resources)


Control and observability
# Configure permissions
Copy page
Control how your agent uses tools with permission modes, hooks, and declarative allow/deny rules.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
The Claude Agent SDK provides permission controls to manage how Claude uses tools. Use permission modes and rules to define what’s allowed automatically, and the [`canUseTool` callback](https://code.claude.com/docs/en/agent-sdk/user-input) to handle everything else at runtime.
This page covers permission modes and rules. To build interactive approval flows where users approve or deny tool requests at runtime, see [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input).
## 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)
How permissions are evaluated
When Claude requests a tool, the SDK checks permissions in this order:
1
[](https://code.claude.com/docs/en/agent-sdk/permissions)
Hooks
Run [hooks](https://code.claude.com/docs/en/agent-sdk/hooks) first, which can allow, deny, or continue to the next step
2
[](https://code.claude.com/docs/en/agent-sdk/permissions)
Deny rules
Check `deny` rules (from `disallowed_tools` and [settings.json](https://code.claude.com/docs/en/settings#permission-settings)). If a deny rule matches, the tool is blocked, even in `bypassPermissions` mode.
3
[](https://code.claude.com/docs/en/agent-sdk/permissions)
Permission mode
Apply the active [permission mode](https://code.claude.com/docs/en/agent-sdk/permissions#permission-modes). `bypassPermissions` approves everything that reaches this step. `acceptEdits` approves file operations. Other modes fall through.
4
[](https://code.claude.com/docs/en/agent-sdk/permissions)
Allow rules
Check `allow` rules (from `allowed_tools` and settings.json). If a rule matches, the tool is approved.
5
[](https://code.claude.com/docs/en/agent-sdk/permissions)
canUseTool callback
If not resolved by any of the above, call your [`canUseTool` callback](https://code.claude.com/docs/en/agent-sdk/user-input) for a decision. In `dontAsk` mode, this step is skipped and the tool is denied.
![Permission evaluation flow diagram](https://mintcdn.com/claude-code/gvy2DIUELtNA8qD3/images/agent-sdk/permissions-flow.svg?fit=max&auto=format&n=gvy2DIUELtNA8qD3&q=85&s=0ccd63043a9ffc2a34d863602e043f72) This page focuses on **allow and deny rules** and **permission modes**. For the other steps:
  * **Hooks:** run custom code to allow, deny, or modify tool requests. See [Control execution with hooks](https://code.claude.com/docs/en/agent-sdk/hooks).
  * **canUseTool callback:** prompt users for approval at runtime. See [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input).


## 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)
Allow and deny rules
`allowed_tools` and `disallowed_tools` (TypeScript: `allowedTools` / `disallowedTools`) add entries to the allow and deny rule lists in the evaluation flow above. They control whether a tool call is approved, not whether the tool is available to Claude.  
| Option  | Effect  |  
| --- | --- |  
| `allowed_tools=["Read", "Grep"]`  |  `Read` and `Grep` are auto-approved. Tools not listed here still exist and fall through to the permission mode and `canUseTool`.  |  
| `disallowed_tools=["Bash"]`  |  `Bash` is always denied. Deny rules are checked first and hold in every permission mode, including `bypassPermissions`.  |  
For a locked-down agent, pair `allowedTools` with `permissionMode: "dontAsk"`. Listed tools are approved; anything else is denied outright instead of prompting:

```
const options = {
  allowedTools: ["Read", "Glob", "Grep"],
  permissionMode: "dontAsk"
};

```

**`allowed_tools`does not constrain`bypassPermissions`.** `allowed_tools` only pre-approves the tools you list. Unlisted tools are not matched by any allow rule and fall through to the permission mode, where `bypassPermissions` approves them. Setting `allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"` still approves every tool, including `Bash`, `Write`, and `Edit`. If you need `bypassPermissions` but want specific tools blocked, use `disallowed_tools`.
You can also configure allow, deny, and ask rules declaratively in `.claude/settings.json`. These rules are read when the `project` setting source is enabled, which it is for default `query()` options. If you set `setting_sources` (TypeScript: `settingSources`) explicitly, include `"project"` for them to apply. See [Permission settings](https://code.claude.com/docs/en/settings#permission-settings) for the rule syntax.
## 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#permission-modes)
Permission modes
Permission modes provide global control over how Claude uses tools. You can set the permission mode when calling `query()` or change it dynamically during streaming sessions.
### 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#available-modes)
Available modes
The SDK supports these permission modes:  
| Mode  | Description  | Tool behavior  |  
| --- | --- | --- |  
| `default`  | Standard permission behavior  | No auto-approvals; unmatched tools trigger your `canUseTool` callback  |  
| `dontAsk`  | Deny instead of prompting  | Anything not pre-approved by `allowed_tools` or rules is denied; `canUseTool` is never called  |  
| `acceptEdits`  | Auto-accept file edits  | File edits and [filesystem operations](https://code.claude.com/docs/en/agent-sdk/permissions#accept-edits-mode-acceptedits) (`mkdir`, `rm`, `mv`, etc.) are automatically approved  |  
| `bypassPermissions`  | Bypass all permission checks  | All tools run without permission prompts (use with caution)  |  
| `plan`  | Planning mode  | No tool execution; Claude plans without making changes  |  
|  `auto` (TypeScript only)  | Model-classified approvals  | A model classifier approves or denies each tool call. See [Auto mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) for availability  |  
**Subagent inheritance:** When the parent uses `bypassPermissions`, `acceptEdits`, or `auto`, all subagents inherit that mode and it cannot be overridden per subagent. Subagents may have different system prompts and less constrained behavior than your main agent, so inheriting `bypassPermissions` grants them full, autonomous system access without any approval prompts.
### 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#set-permission-mode)
Set permission mode
You can set the permission mode once when starting a query, or change it dynamically while the session is active.
  * At query time
  * During streaming


Pass `permission_mode` (Python) or `permissionMode` (TypeScript) when creating a query. This mode applies for the entire session unless changed dynamically.
Python
TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    async for message in query(
        prompt="Help me refactor this code",
        options=ClaudeAgentOptions(
            permission_mode="default",  # Set the mode here
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)


asyncio.run(main())

```

Call `set_permission_mode()` (Python) or `setPermissionMode()` (TypeScript) to change the mode mid-session. The new mode takes effect immediately for all subsequent tool requests. This lets you start restrictive and loosen permissions as trust builds, for example switching to `acceptEdits` after reviewing Claude’s initial approach.
Python
TypeScript

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    q = query(
        prompt="Help me refactor this code",
        options=ClaudeAgentOptions(
            permission_mode="default",  # Start in default mode
        ),
    )

    # Change mode dynamically mid-session
    await q.set_permission_mode("acceptEdits")

    # Process messages with the new permission mode
    async for message in q:
        if hasattr(message, "result"):
            print(message.result)


asyncio.run(main())

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#mode-details)
Mode details
#### 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#accept-edits-mode-acceptedits)
Accept edits mode (`acceptEdits`)
Auto-approves file operations so Claude can edit code without prompting. Other tools (like Bash commands that aren’t filesystem operations) still require normal permissions. **Auto-approved operations:**
  * File edits (Edit, Write tools)
  * Filesystem commands: `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`

Both apply only to paths inside the working directory or `additionalDirectories`. Paths outside that scope and writes to protected paths still prompt. **Use when:** you trust Claude’s edits and want faster iteration, such as during prototyping or when working in an isolated directory.
#### 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#don%E2%80%99t-ask-mode-dontask)
Don’t ask mode (`dontAsk`)
Converts any permission prompt into a denial. Tools pre-approved by `allowed_tools`, `settings.json` allow rules, or a hook run as normal. Everything else is denied without calling `canUseTool`. **Use when:** you want a fixed, explicit tool surface for a headless agent and prefer a hard deny over silent reliance on `canUseTool` being absent.
#### 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#bypass-permissions-mode-bypasspermissions)
Bypass permissions mode (`bypassPermissions`)
Auto-approves all tool uses without prompts. Hooks still execute and can block operations if needed.
Use with extreme caution. Claude has full system access in this mode. Only use in controlled environments where you trust all possible operations.`allowed_tools` does not constrain this mode. Every tool is approved, not just the ones you listed. Deny rules (`disallowed_tools`), explicit `ask` rules, and hooks are evaluated before the mode check and can still block a tool.
#### 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#plan-mode-plan)
Plan mode (`plan`)
Prevents tool execution entirely. Claude can analyze code and create plans but cannot make changes. Claude may use `AskUserQuestion` to clarify requirements before finalizing the plan. See [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input#handle-clarifying-questions) for handling these prompts. **Use when:** you want Claude to propose changes without executing them, such as during code review or when you need to approve changes before they’re made.
## 
[​](https://code.claude.com/docs/en/agent-sdk/permissions#related-resources)
Related resources
For the other steps in the permission evaluation flow:
  * [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input): interactive approval prompts and clarifying questions
  * [Hooks guide](https://code.claude.com/docs/en/agent-sdk/hooks): run custom code at key points in the agent lifecycle
  * [Permission rules](https://code.claude.com/docs/en/settings#permission-settings): declarative allow/deny rules in `settings.json`


Was this page helpful?
YesNo
[Plugins in the SDK](https://code.claude.com/docs/en/agent-sdk/plugins)[Intercept and control agent behavior with hooks](https://code.claude.com/docs/en/agent-sdk/hooks)
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
[Privacy choices](https://code.claude.com/docs/en/agent-sdk/permissions)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
