<!--
url: https://code.claude.com/docs/en/agent-sdk/cost-tracking
download_date: 2026-04-29
website: claude-code
webpage: agent-sdk-cost-tracking
-->

# Agent Sdk Cost Tracking

[Skip to main content](https://code.claude.com/docs/en/agent-sdk/cost-tracking#content-area)
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
Track cost and usage
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
  * [Understand token usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking#understand-token-usage)
  * [Get the total cost of a query](https://code.claude.com/docs/en/agent-sdk/cost-tracking#get-the-total-cost-of-a-query)
  * [Track per-step and per-model usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-per-step-and-per-model-usage)
  * [Track per-step usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-per-step-usage)
  * [Break down usage per model](https://code.claude.com/docs/en/agent-sdk/cost-tracking#break-down-usage-per-model)
  * [Accumulate costs across multiple calls](https://code.claude.com/docs/en/agent-sdk/cost-tracking#accumulate-costs-across-multiple-calls)
  * [Handle errors, caching, and token discrepancies](https://code.claude.com/docs/en/agent-sdk/cost-tracking#handle-errors-caching-and-token-discrepancies)
  * [Resolve output token discrepancies](https://code.claude.com/docs/en/agent-sdk/cost-tracking#resolve-output-token-discrepancies)
  * [Track costs on failed conversations](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-costs-on-failed-conversations)
  * [Track cache tokens](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-cache-tokens)
  * [Extend the prompt cache TTL to one hour](https://code.claude.com/docs/en/agent-sdk/cost-tracking#extend-the-prompt-cache-ttl-to-one-hour)
  * [Related documentation](https://code.claude.com/docs/en/agent-sdk/cost-tracking#related-documentation)


Control and observability
# Track cost and usage
Copy page
Learn how to track token usage, estimate costs, and configure prompt caching with the Claude Agent SDK.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
The Claude Agent SDK provides detailed token usage information for each interaction with Claude. This guide explains how to properly track usage and understand cost reporting, especially when dealing with parallel tool uses and multi-step conversations. For complete API documentation, see the [TypeScript SDK reference](https://code.claude.com/docs/en/agent-sdk/typescript) and [Python SDK reference](https://code.claude.com/docs/en/agent-sdk/python).
The `total_cost_usd` and `costUSD` fields are client-side estimates, not authoritative billing data. The SDK computes them locally from a price table bundled at build time, so they can drift from what you are actually billed when:
  * pricing changes
  * the installed SDK version does not recognize a model
  * billing rules apply that the client cannot model

Use these fields for development insight and approximate budgeting. For authoritative billing, use the [Usage and Cost API](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api) or the Usage page in the [Claude Console](https://platform.claude.com/usage). Do not bill end users or trigger financial decisions from these fields.
## 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#understand-token-usage)
Understand token usage
The TypeScript and Python SDKs expose the same usage data with different field names:
  * **TypeScript** provides per-step token breakdowns on each assistant message (`message.message.id`, `message.message.usage`), per-model cost via `modelUsage` on the result message, and a cumulative total on the result message.
  * **Python** provides per-step token breakdowns on each assistant message (`message.usage`, `message.message_id`), per-model cost via `model_usage` on the result message, and the accumulated total on the result message (`total_cost_usd` and `usage` dict).

Both SDKs use the same underlying cost model and expose the same granularity. The difference is in field naming and where per-step usage is nested. Cost tracking depends on understanding how the SDK scopes usage data:
  * **`query()`call:** one invocation of the SDK’s `query()` function. A single call can involve multiple steps (Claude responds, uses tools, gets results, responds again). Each call produces one [`result`](https://code.claude.com/docs/en/agent-sdk/typescript#sdk-result-message) message at the end.
  * **Step:** a single request/response cycle within a `query()` call. Each step produces assistant messages with token usage.
  * **Session:** a series of `query()` calls linked by a session ID (using the `resume` option). Each `query()` call within a session reports its own cost independently.

The following diagram shows the message stream from a single `query()` call, with token usage reported at each step and the cumulative estimate at the end: ![Diagram showing a query producing two steps of messages. Step 1 has four assistant messages sharing the same ID and usage \(count once\), Step 2 has one assistant message with a new ID, and the final result message shows the estimated total_cost_usd.](https://mintcdn.com/claude-code/Dujg43sxTkuhSELI/images/agent-sdk/message-usage-flow.svg?fit=max&auto=format&n=Dujg43sxTkuhSELI&q=85&s=c542f51ff58547ef9c0e57b16d03f33c)
1
[](https://code.claude.com/docs/en/agent-sdk/cost-tracking)
Each step produces assistant messages
When Claude responds, it sends one or more assistant messages. In TypeScript, each assistant message contains a nested `BetaMessage` (accessed via `message.message`) with an `id` and a [`usage`](https://platform.claude.com/docs/en/api/messages) object with token counts (`input_tokens`, `output_tokens`). In Python, the `AssistantMessage` dataclass exposes the same data directly via `message.usage` and `message.message_id`. When Claude uses multiple tools in one turn, all messages in that turn share the same ID, so deduplicate by ID to avoid double-counting.
2
[](https://code.claude.com/docs/en/agent-sdk/cost-tracking)
The result message provides the cumulative estimate
When the `query()` call completes, the SDK emits a result message with `total_cost_usd` and cumulative `usage`. This is available in both TypeScript ([`SDKResultMessage`](https://code.claude.com/docs/en/agent-sdk/typescript#sdk-result-message)) and Python ([`ResultMessage`](https://code.claude.com/docs/en/agent-sdk/python#result-message)). If you make multiple `query()` calls (for example, in a multi-turn session), each result only reflects the cost of that individual call. If you only need the estimated total, you can ignore the per-step usage and read this single value.
## 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#get-the-total-cost-of-a-query)
Get the total cost of a query
The result message ([TypeScript](https://code.claude.com/docs/en/agent-sdk/typescript#sdk-result-message), [Python](https://code.claude.com/docs/en/agent-sdk/python#result-message)) marks the end of the agent loop for a `query()` call. It includes `total_cost_usd`, the cumulative estimated cost across all steps in that call. This works for both success and error results. If you use sessions to make multiple `query()` calls, each result only reflects the cost of that individual call. The following examples iterate over the message stream from a `query()` call and print the total cost when the `result` message arrives:
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({ prompt: "Summarize this project" })) {
  if (message.type === "result") {
    console.log(`Total cost: $${message.total_cost_usd}`);
  }
}

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-per-step-and-per-model-usage)
Track per-step and per-model usage
The examples in this section use TypeScript field names. In Python, the equivalent fields are [`AssistantMessage.usage`](https://code.claude.com/docs/en/agent-sdk/python#assistant-message) and `AssistantMessage.message_id` for per-step usage, and [`ResultMessage.model_usage`](https://code.claude.com/docs/en/agent-sdk/python#result-message) for per-model breakdowns.
### 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-per-step-usage)
Track per-step usage
Each assistant message contains a nested `BetaMessage` (accessed via `message.message`) with an `id` and `usage` object with token counts. When Claude uses tools in parallel, multiple messages share the same `id` with identical usage data. Track which IDs you’ve already counted and skip duplicates to avoid inflated totals.
Parallel tool calls produce multiple assistant messages whose nested `BetaMessage` shares the same `id` and identical usage. Always deduplicate by ID to get accurate per-step token counts.
The following example accumulates input and output tokens across all steps, counting each unique message ID only once:

```
import { query } from "@anthropic-ai/claude-agent-sdk";

const seenIds = new Set<string>();
let totalInputTokens = 0;
let totalOutputTokens = 0;

for await (const message of query({ prompt: "Summarize this project" })) {
  if (message.type === "assistant") {
    const msgId = message.message.id;

    // Parallel tool calls share the same ID, only count once
    if (!seenIds.has(msgId)) {
      seenIds.add(msgId);
      totalInputTokens += message.message.usage.input_tokens;
      totalOutputTokens += message.message.usage.output_tokens;
    }
  }
}

console.log(`Steps: ${seenIds.size}`);
console.log(`Input tokens: ${totalInputTokens}`);
console.log(`Output tokens: ${totalOutputTokens}`);

```

### 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#break-down-usage-per-model)
Break down usage per model
The result message includes [`modelUsage`](https://code.claude.com/docs/en/agent-sdk/typescript#model-usage), a map of model name to per-model token counts and cost. This is useful when you run multiple models (for example, Haiku for subagents and Opus for the main agent) and want to see where tokens are going. The following example runs a query and prints the cost and token breakdown for each model used:

```
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({ prompt: "Summarize this project" })) {
  if (message.type !== "result") continue;

  for (const [modelName, usage] of Object.entries(message.modelUsage)) {
    console.log(`${modelName}: $${usage.costUSD.toFixed(4)}`);
    console.log(`  Input tokens: ${usage.inputTokens}`);
    console.log(`  Output tokens: ${usage.outputTokens}`);
    console.log(`  Cache read: ${usage.cacheReadInputTokens}`);
    console.log(`  Cache creation: ${usage.cacheCreationInputTokens}`);
  }
}

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#accumulate-costs-across-multiple-calls)
Accumulate costs across multiple calls
Each `query()` call returns its own `total_cost_usd`. The SDK does not provide a session-level total, so if your application makes multiple `query()` calls (for example, in a multi-turn session or across different users), accumulate the totals yourself. The following examples run two `query()` calls sequentially, add each call’s `total_cost_usd` to a running total, and print both the per-call and combined cost:
TypeScript
Python

```
import { query } from "@anthropic-ai/claude-agent-sdk";

// Track cumulative cost across multiple query() calls
let totalSpend = 0;

const prompts = [
  "Read the files in src/ and summarize the architecture",
  "List all exported functions in src/auth.ts"
];

for (const prompt of prompts) {
  for await (const message of query({ prompt })) {
    if (message.type === "result") {
      totalSpend += message.total_cost_usd;
      console.log(`This call: $${message.total_cost_usd}`);
    }
  }
}

console.log(`Total spend: $${totalSpend.toFixed(4)}`);

```

## 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#handle-errors-caching-and-token-discrepancies)
Handle errors, caching, and token discrepancies
For accurate cost tracking, account for failed conversations, cache token pricing, and occasional reporting inconsistencies.
### 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#resolve-output-token-discrepancies)
Resolve output token discrepancies
In rare cases, you might observe different `output_tokens` values for messages with the same ID. When this occurs:
  1. **Use the highest value:** the final message in a group typically contains the accurate total.
  2. **Prefer the result message:** the `total_cost_usd` in the result message reflects the SDK’s accumulated estimate across all steps, so it is more reliable than summing per-step values yourself. It is still an estimate and may differ from your actual bill.
  3. **Report inconsistencies:** file issues at the [Claude Code GitHub repository](https://github.com/anthropics/claude-code/issues).


### 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-costs-on-failed-conversations)
Track costs on failed conversations
Both success and error result messages include `usage` and `total_cost_usd`. If a conversation fails mid-way, you still consumed tokens up to the point of failure. Always read cost data from the result message regardless of its `subtype`.
### 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-cache-tokens)
Track cache tokens
The Agent SDK automatically uses [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) to reduce costs on repeated content. You do not need to configure caching yourself. The usage object includes two additional fields for cache tracking:
  * `cache_creation_input_tokens`: tokens used to create new cache entries (charged at a higher rate than standard input tokens).
  * `cache_read_input_tokens`: tokens read from existing cache entries (charged at a reduced rate).

Track these separately from `input_tokens` to understand caching savings. In TypeScript, these fields are typed on the [`Usage`](https://code.claude.com/docs/en/agent-sdk/typescript#usage) object. In Python, they appear as keys in the [`ResultMessage.usage`](https://code.claude.com/docs/en/agent-sdk/python#result-message) dict (for example, `message.usage.get("cache_read_input_tokens", 0)`).
### 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#extend-the-prompt-cache-ttl-to-one-hour)
Extend the prompt cache TTL to one hour
Cache entries written by the SDK use a 5-minute TTL by default when you authenticate with an API key or run on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry. If your workload runs many short sessions against the same system prompt and context with gaps longer than 5 minutes between them, the cache expires between sessions and each new session pays full input price. To request a 1-hour TTL on cache writes, set the [`ENABLE_PROMPT_CACHING_1H`](https://code.claude.com/docs/en/env-vars) environment variable. You can export it in your shell or container environment, or pass it through `options.env`. The following example enables 1-hour TTL for an agent running on Bedrock:
Python
TypeScript

```
options = ClaudeAgentOptions(
    env={
        "CLAUDE_CODE_USE_BEDROCK": "1",
        "ENABLE_PROMPT_CACHING_1H": "1",
    },
)

```

Cache writes with a 1-hour TTL are billed at a higher rate than 5-minute writes, so enabling this trades higher write cost for more cache reads. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details. Claude subscription users already receive 1-hour TTL automatically and do not need to set this variable.
## 
[​](https://code.claude.com/docs/en/agent-sdk/cost-tracking#related-documentation)
Related documentation
  * [TypeScript SDK Reference](https://code.claude.com/docs/en/agent-sdk/typescript) - Complete API documentation
  * [SDK Overview](https://code.claude.com/docs/en/agent-sdk/overview) - Getting started with the SDK
  * [SDK Permissions](https://code.claude.com/docs/en/agent-sdk/permissions) - Managing tool permissions


Was this page helpful?
YesNo
[Rewind file changes with checkpointing](https://code.claude.com/docs/en/agent-sdk/file-checkpointing)[Observability with OpenTelemetry](https://code.claude.com/docs/en/agent-sdk/observability)
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
[Privacy choices](https://code.claude.com/docs/en/agent-sdk/cost-tracking)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
