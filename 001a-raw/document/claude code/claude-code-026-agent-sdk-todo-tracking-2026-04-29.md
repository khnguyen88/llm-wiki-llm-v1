<!--
url: https://code.claude.com/docs/en/agent-sdk/todo-tracking
download_date: 2026-04-29
website: claude-code
webpage: agent-sdk-todo-tracking
-->

# Agent Sdk Todo Tracking

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/todo-tracking#content-area)
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)
English
Search...
Ctrl KAsk AI
  * [Claude Developer Platform](https://platform.claude.com/)
  * [Claude Code on the Web](https://claude.ai/code)
  * [Claude Code on the Web](https://claude.ai/code)


Search...
Navigation
Control and observability
Todo Lists
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
  * [Todo Lifecycle](https://code.claude.com/docs/en/agent-sdk/todo-tracking#todo-lifecycle)
  * [When Todos Are Used](https://code.claude.com/docs/en/agent-sdk/todo-tracking#when-todos-are-used)
  * [Examples](https://code.claude.com/docs/en/agent-sdk/todo-tracking#examples)
  * [Monitoring Todo Changes](https://code.claude.com/docs/en/agent-sdk/todo-tracking#monitoring-todo-changes)
  * [Real-time Progress Display](https://code.claude.com/docs/en/agent-sdk/todo-tracking#real-time-progress-display)
  * [Related Documentation](https://code.claude.com/docs/en/agent-sdk/todo-tracking#related-documentation)


Control and observability
# Todo Lists
Copy page
Track and display todos using the Claude Agent SDK for organized task management
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Todo tracking provides a structured way to manage tasks and display progress to users. The Claude Agent SDK includes built-in todo functionality that helps organize complex workflows and keep users informed about task progression.
### 
[​](https://code.claude.com/docs/en/agent-sdk/todo-tracking#todo-lifecycle)
Todo Lifecycle
Todos follow a predictable lifecycle:
  1. **Created** as `pending` when tasks are identified
  2. **Activated** to `in_progress` when work begins
  3. **Completed** when the task finishes successfully
  4. **Removed** when all tasks in a group are completed


### 
[​](https://code.claude.com/docs/en/agent-sdk/todo-tracking#when-todos-are-used)
When Todos Are Used
The SDK automatically creates todos for:
  * **Complex multi-step tasks** requiring 3 or more distinct actions
  * **User-provided task lists** when multiple items are mentioned
  * **Non-trivial operations** that benefit from progress tracking
  * **Explicit requests** when users ask for todo organization


## 
[​](https://code.claude.com/docs/en/agent-sdk/todo-tracking#examples)
Examples
### 
[​](https://code.claude.com/docs/en/agent-sdk/todo-tracking#monitoring-todo-changes)
Monitoring Todo Changes
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Optimize my React app performance and track progress with todos",
  options: { maxTurns: 15 }
})) {
  // Todo updates are reflected in the message stream
  if (message.type === "assistant") {
    for (const block of message.message.content) {
      if (block.type === "tool_use" && block.name === "TodoWrite") {
        const todos = block.input.todos;

        console.log("Todo Status Update:");
        todos.forEach((todo, index) => {
          const status =
            todo.status === "completed" ? "✅" : todo.status === "in_progress" ? "🔧" : "❌";
          console.log(`${index + 1}. ${status} ${todo.content}`);
        });
      }
    }
  }
}

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/todo-tracking#real-time-progress-display)
Real-time Progress Display
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

class TodoTracker {
  private todos: any[] = [];

  displayProgress() {
    if (this.todos.length === 0) return;

    const completed = this.todos.filter((t) => t.status === "completed").length;
    const inProgress = this.todos.filter((t) => t.status === "in_progress").length;
    const total = this.todos.length;

    console.log(`\nProgress: ${completed}/${total} completed`);
    console.log(`Currently working on: ${inProgress} task(s)\n`);

    this.todos.forEach((todo, index) => {
      const icon =
        todo.status === "completed" ? "✅" : todo.status === "in_progress" ? "🔧" : "❌";
      const text = todo.status === "in_progress" ? todo.activeForm : todo.content;
      console.log(`${index + 1}. ${icon} ${text}`);
    });
  }

  async trackQuery(prompt: string) {
    for await (const message of query({
      prompt,
      options: { maxTurns: 20 }
    })) {
      if (message.type === "assistant") {
        for (const block of message.message.content) {
          if (block.type === "tool_use" && block.name === "TodoWrite") {
            this.todos = block.input.todos;
            this.displayProgress();
          }
        }
      }
    }
  }
}

// Usage
const tracker = new TodoTracker();
await tracker.trackQuery("Build a complete authentication system with todos");

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/todo-tracking#related-documentation)
Related Documentation
  * [TypeScript SDK Reference](https://code.claude.com/docs/en/agent-sdk/typescript)
  * [Python SDK Reference](https://code.claude.com/docs/en/agent-sdk/python)
  * [Streaming vs Single Mode](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)
  * [Custom Tools](https://code.claude.com/docs/en/agent-sdk/custom-tools)


Was this page helpful?
YesNo
[Observability with OpenTelemetry](https://code.claude.com/docs/en/agent-sdk/observability)[Hosting the Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting)
Ctrl+I
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
Company
[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)
Help and security
[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)
Learn
[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)
Terms and policies
[Privacy choices](https://code.claude.com/docs/en/agent-sdk/todo-tracking)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
