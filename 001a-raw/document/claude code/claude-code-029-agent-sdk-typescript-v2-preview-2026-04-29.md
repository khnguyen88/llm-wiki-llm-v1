<!--
url: https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview
download_date: 2026-04-29
website: claude-code
webpage: agent-sdk-typescript-v2-preview
-->

# Agent Sdk Typescript V2 Preview

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#content-area)
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
SDK references
TypeScript SDK V2 interface (preview)
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
  * [Installation](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#installation)
  * [Quick start](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#quick-start)
  * [One-shot prompt](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#one-shot-prompt)
  * [Basic session](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#basic-session)
  * [Multi-turn conversation](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#multi-turn-conversation)
  * [Session resume](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#session-resume)
  * [Cleanup](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#cleanup)
  * [API reference](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#api-reference)
  * [unstable_v2_createSession()](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#unstable_v2_createsession)
  * [unstable_v2_resumeSession()](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#unstable_v2_resumesession)
  * [unstable_v2_prompt()](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#unstable_v2_prompt)
  * [SDKSession interface](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#sdksession-interface)
  * [Feature availability](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#feature-availability)
  * [Feedback](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#feedback)
  * [See also](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#see-also)


SDK references
# TypeScript SDK V2 interface (preview)
Copy page
Preview of the simplified V2 TypeScript Agent SDK, with session-based send/stream patterns for multi-turn conversations.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
The V2 interface is an **unstable preview**. APIs may change based on feedback before becoming stable. Some features like session forking are only available in the [V1 SDK](https://code.claude.com/docs/en/agent-sdk/typescript).
The V2 Claude Agent TypeScript SDK removes the need for async generators and yield coordination. This makes multi-turn conversations simpler, instead of managing generator state across turns, each turn is a separate `send()`/`stream()` cycle. The API surface reduces to three concepts:
  * `createSession()` / `resumeSession()`: Start or continue a conversation
  * `session.send()`: Send a message
  * `session.stream()`: Get the response


## 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#installation)
Installation
The V2 interface is included in the existing SDK package:

```
npm install @anthropic-ai/claude-agent-sdk

```

The SDK bundles a native Claude Code binary for your platform as an optional dependency, so you don’t need to install Claude Code separately.
## 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#quick-start)
Quick start
### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#one-shot-prompt)
One-shot prompt
For simple single-turn queries where you don’t need to maintain a session, use `unstable_v2_prompt()`. This example sends a math question and logs the answer:

```
import { unstable_v2_prompt } from "@anthropic-ai/claude-agent-sdk";

const result = await unstable_v2_prompt("What is 2 + 2?", {
  model: "claude-opus-4-7"
});
if (result.subtype === "success") {
  console.log(result.result);
}

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#basic-session)
Basic session
For interactions beyond a single prompt, create a session. V2 separates sending and streaming into distinct steps:
  * `send()` dispatches your message
  * `stream()` streams back the response

This explicit separation makes it easier to add logic between turns (like processing responses before sending follow-ups). The example below creates a session, sends “Hello!” to Claude, and prints the text response. It uses [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management) (TypeScript 5.2+) to automatically close the session when the block exits. You can also call `session.close()` manually.

```
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

await session.send("Hello!");
for await (const msg of session.stream()) {
  // Filter for assistant messages to get human-readable output
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#multi-turn-conversation)
Multi-turn conversation
Sessions persist context across multiple exchanges. To continue a conversation, call `send()` again on the same session. Claude remembers the previous turns. This example asks a math question, then asks a follow-up that references the previous answer:

```
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

// Turn 1
await session.send("What is 5 + 3?");
for await (const msg of session.stream()) {
  // Filter for assistant messages to get human-readable output
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}

// Turn 2
await session.send("Multiply that by 2");
for await (const msg of session.stream()) {
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#session-resume)
Session resume
If you have a session ID from a previous interaction, you can resume it later. This is useful for long-running workflows or when you need to persist conversations across application restarts. This example creates a session, stores its ID, closes it, then resumes the conversation:

```
import {
  unstable_v2_createSession,
  unstable_v2_resumeSession,
  type SDKMessage
} from "@anthropic-ai/claude-agent-sdk";

// Helper to extract text from assistant messages
function getAssistantText(msg: SDKMessage): string | null {
  if (msg.type !== "assistant") return null;
  return msg.message.content
    .filter((block) => block.type === "text")
    .map((block) => block.text)
    .join("");
}

// Create initial session and have a conversation
const session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

await session.send("Remember this number: 42");

// Get the session ID from any received message
let sessionId: string | undefined;
for await (const msg of session.stream()) {
  sessionId = msg.session_id;
  const text = getAssistantText(msg);
  if (text) console.log("Initial response:", text);
}

console.log("Session ID:", sessionId);
session.close();

// Later: resume the session using the stored ID
await using resumedSession = unstable_v2_resumeSession(sessionId!, {
  model: "claude-opus-4-7"
});

await resumedSession.send("What number did I ask you to remember?");
for await (const msg of resumedSession.stream()) {
  const text = getAssistantText(msg);
  if (text) console.log("Resumed response:", text);
}

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#cleanup)
Cleanup
Sessions can be closed manually or automatically using [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management), a TypeScript 5.2+ feature for automatic resource cleanup. If you’re using an older TypeScript version or encounter compatibility issues, use manual cleanup instead. **Automatic cleanup (TypeScript 5.2+):**

```
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});
// Session closes automatically when the block exits

```

**Manual cleanup:**

```
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

const session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});
// ... use the session ...
session.close();

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#api-reference)
API reference
### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#unstable_v2_createsession)
`unstable_v2_createSession()`
Creates a new session for multi-turn conversations.

```
function unstable_v2_createSession(options: {
  model: string;
  // Additional options supported
}): SDKSession;

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#unstable_v2_resumesession)
`unstable_v2_resumeSession()`
Resumes an existing session by ID.

```
function unstable_v2_resumeSession(
  sessionId: string,
  options: {
    model: string;
    // Additional options supported
  }
): SDKSession;

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#unstable_v2_prompt)
`unstable_v2_prompt()`
One-shot convenience function for single-turn queries.

```
function unstable_v2_prompt(
  prompt: string,
  options: {
    model: string;
    // Additional options supported
  }
): Promise<SDKResultMessage>;

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#sdksession-interface)
SDKSession interface

```
interface SDKSession {
  readonly sessionId: string;
  send(message: string | SDKUserMessage): Promise<void>;
  stream(): AsyncGenerator<SDKMessage, void>;
  close(): void;
}

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#feature-availability)
Feature availability
Not all V1 features are available in V2 yet. The following require using the [V1 SDK](https://code.claude.com/docs/en/agent-sdk/typescript):
  * Session forking (`forkSession` option)
  * Some advanced streaming input patterns


## 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#feedback)
Feedback
Share your feedback on the V2 interface before it becomes stable. Report issues and suggestions through [GitHub Issues](https://github.com/anthropics/claude-code/issues).
## 
[​](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview#see-also)
See also
  * [TypeScript SDK reference (V1)](https://code.claude.com/docs/en/agent-sdk/typescript) - Full V1 SDK documentation
  * [SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) - General SDK concepts
  * [V2 examples on GitHub](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world-v2) - Working code examples


Was this page helpful?
YesNo
[TypeScript SDK](https://code.claude.com/docs/en/agent-sdk/typescript)[Python SDK](https://code.claude.com/docs/en/agent-sdk/python)
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
[Privacy choices](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
