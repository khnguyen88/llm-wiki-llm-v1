<!--
url: https://code.claude.com/docs/en/checkpointing
download_date: 2026-04-29
website: claude-code
webpage: checkpointing
-->

# Checkpointing

[Skip to main content](https://code.claude.com/docs/en/checkpointing#content-area)
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
Reference
Checkpointing
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/sub-agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
##### Reference
  * [CLI reference](https://code.claude.com/docs/en/cli-reference)
  * [Commands](https://code.claude.com/docs/en/commands)
  * [Environment variables](https://code.claude.com/docs/en/env-vars)
  * [Tools reference](https://code.claude.com/docs/en/tools-reference)
  * [Interactive mode](https://code.claude.com/docs/en/interactive-mode)
  * [Checkpointing](https://code.claude.com/docs/en/checkpointing)
  * [Hooks reference](https://code.claude.com/docs/en/hooks)
  * [Plugins reference](https://code.claude.com/docs/en/plugins-reference)
  * [Channels reference](https://code.claude.com/docs/en/channels-reference)


##### Glossary
  * [Glossary](https://code.claude.com/docs/en/glossary)


On this page
  * [How checkpoints work](https://code.claude.com/docs/en/checkpointing#how-checkpoints-work)
  * [Automatic tracking](https://code.claude.com/docs/en/checkpointing#automatic-tracking)
  * [Rewind and summarize](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)
  * [Restore vs. summarize](https://code.claude.com/docs/en/checkpointing#restore-vs-summarize)
  * [Common use cases](https://code.claude.com/docs/en/checkpointing#common-use-cases)
  * [Limitations](https://code.claude.com/docs/en/checkpointing#limitations)
  * [Bash command changes not tracked](https://code.claude.com/docs/en/checkpointing#bash-command-changes-not-tracked)
  * [External changes not tracked](https://code.claude.com/docs/en/checkpointing#external-changes-not-tracked)
  * [Not a replacement for version control](https://code.claude.com/docs/en/checkpointing#not-a-replacement-for-version-control)
  * [See also](https://code.claude.com/docs/en/checkpointing#see-also)


Reference
# Checkpointing
Copy page
Track, rewind, and summarize Claude’s edits and conversation to manage session state.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Claude Code automatically tracks Claude’s file edits as you work, allowing you to quickly undo changes and rewind to previous states if anything gets off track.
## 
[​](https://code.claude.com/docs/en/checkpointing#how-checkpoints-work)
How checkpoints work
As you work with Claude, checkpointing automatically captures the state of your code before each edit. This safety net lets you pursue ambitious, wide-scale tasks knowing you can always return to a prior code state.
### 
[​](https://code.claude.com/docs/en/checkpointing#automatic-tracking)
Automatic tracking
Claude Code tracks all changes made by its file editing tools:
  * Every user prompt creates a new checkpoint
  * Checkpoints persist across sessions, so you can access them in resumed conversations
  * Automatically cleaned up along with sessions after 30 days (configurable)


### 
[​](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)
Rewind and summarize
Press `Esc` twice (`Esc` + `Esc`) or use the `/rewind` command to open the rewind menu. A scrollable list shows each of your prompts from the session. Select the point you want to act on, then choose an action:
  * **Restore code and conversation** : revert both code and conversation to that point
  * **Restore conversation** : rewind to that message while keeping current code
  * **Restore code** : revert file changes while keeping the conversation
  * **Summarize from here** : compress the conversation from this point forward into a summary, freeing context window space
  * **Never mind** : return to the message list without making changes

After restoring the conversation or summarizing, the original prompt from the selected message is restored into the input field so you can re-send or edit it.
#### 
[​](https://code.claude.com/docs/en/checkpointing#restore-vs-summarize)
Restore vs. summarize
The three restore options revert state: they undo code changes, conversation history, or both. “Summarize from here” works differently:
  * Messages before the selected message stay intact
  * The selected message and all subsequent messages get replaced with a compact AI-generated summary
  * No files on disk are changed
  * The original messages are preserved in the session transcript, so Claude can reference the details if needed

This is similar to `/compact`, but targeted: instead of summarizing the entire conversation, you keep early context in full detail and only compress the parts that are using up space. You can type optional instructions to guide what the summary focuses on.
Summarize keeps you in the same session and compresses context. If you want to branch off and try a different approach while preserving the original session intact, use [fork](https://code.claude.com/docs/en/how-claude-code-works#resume-or-fork-sessions) instead (`claude --continue --fork-session`).
## 
[​](https://code.claude.com/docs/en/checkpointing#common-use-cases)
Common use cases
Checkpoints are particularly useful when:
  * **Exploring alternatives** : try different implementation approaches without losing your starting point
  * **Recovering from mistakes** : quickly undo changes that introduced bugs or broke functionality
  * **Iterating on features** : experiment with variations knowing you can revert to working states
  * **Freeing context space** : summarize a verbose debugging session from the midpoint forward, keeping your initial instructions intact


## 
[​](https://code.claude.com/docs/en/checkpointing#limitations)
Limitations
### 
[​](https://code.claude.com/docs/en/checkpointing#bash-command-changes-not-tracked)
Bash command changes not tracked
Checkpointing does not track files modified by bash commands. For example, if Claude Code runs:

```
rm file.txt
mv old.txt new.txt
cp source.txt dest.txt

```

These file modifications cannot be undone through rewind. Only direct file edits made through Claude’s file editing tools are tracked.
### 
[​](https://code.claude.com/docs/en/checkpointing#external-changes-not-tracked)
External changes not tracked
Checkpointing only tracks files that have been edited within the current session. Manual changes you make to files outside of Claude Code and edits from other concurrent sessions are normally not captured, unless they happen to modify the same files as the current session.
### 
[​](https://code.claude.com/docs/en/checkpointing#not-a-replacement-for-version-control)
Not a replacement for version control
Checkpoints are designed for quick, session-level recovery. For permanent version history and collaboration:
  * Continue using version control (ex. Git) for commits, branches, and long-term history
  * Checkpoints complement but don’t replace proper version control
  * Think of checkpoints as “local undo” and Git as “permanent history”


## 
[​](https://code.claude.com/docs/en/checkpointing#see-also)
See also
  * [Interactive mode](https://code.claude.com/docs/en/interactive-mode) - Keyboard shortcuts and session controls
  * [Commands](https://code.claude.com/docs/en/commands) - Accessing checkpoints using `/rewind`
  * [CLI reference](https://code.claude.com/docs/en/cli-reference) - Command-line options


Was this page helpful?
YesNo
[Interactive mode](https://code.claude.com/docs/en/interactive-mode)[Hooks reference](https://code.claude.com/docs/en/hooks)
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
[Privacy choices](https://code.claude.com/docs/en/checkpointing)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
