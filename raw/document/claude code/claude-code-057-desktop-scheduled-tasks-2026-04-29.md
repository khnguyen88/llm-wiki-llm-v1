<!--
url: https://code.claude.com/docs/en/desktop-scheduled-tasks
download_date: 2026-04-29
website: claude-code
webpage: desktop-scheduled-tasks
-->

# Desktop Scheduled Tasks

[Skip to main content](https://code.claude.com/docs/en/desktop-scheduled-tasks#content-area)
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
Claude Code on desktop
Schedule recurring tasks in Claude Code Desktop
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
    * [Get started](https://code.claude.com/docs/en/desktop-quickstart)
    * [Reference](https://code.claude.com/docs/en/desktop)
    * [Scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)
  * [Chrome extension (beta)](https://code.claude.com/docs/en/chrome)
  * [Computer use (preview)](https://code.claude.com/docs/en/computer-use)
  * [Visual Studio Code](https://code.claude.com/docs/en/vs-code)
  * [JetBrains IDEs](https://code.claude.com/docs/en/jetbrains)
  * Code review & CI/CD
  * [Claude Code in Slack](https://code.claude.com/docs/en/slack)


On this page
  * [Compare scheduling options](https://code.claude.com/docs/en/desktop-scheduled-tasks#compare-scheduling-options)
  * [Create a scheduled task](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)
  * [Schedule options](https://code.claude.com/docs/en/desktop-scheduled-tasks#schedule-options)
  * [How scheduled tasks run](https://code.claude.com/docs/en/desktop-scheduled-tasks#how-scheduled-tasks-run)
  * [Missed runs](https://code.claude.com/docs/en/desktop-scheduled-tasks#missed-runs)
  * [Permissions for scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks#permissions-for-scheduled-tasks)
  * [Manage scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)
  * [Related resources](https://code.claude.com/docs/en/desktop-scheduled-tasks#related-resources)


Claude Code on desktop
# Schedule recurring tasks in Claude Code Desktop
Copy page
Set up scheduled tasks in Claude Code Desktop to run Claude automatically on a recurring basis for daily code reviews, dependency audits, or morning briefings.
Copy page
> ## Documentation Index
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
> Use this file to discover all available pages before exploring further.
Scheduled tasks start a new session automatically at a time and frequency you choose. Use them for recurring work like daily code reviews, dependency update checks, or morning briefings that pull from your calendar and inbox. The Desktop app’s **Routines** page lets you create both local scheduled tasks and remote [routines](https://code.claude.com/docs/en/routines). A local task runs on your machine with direct access to your files and tools, but only fires while the app is open and your computer is awake. A remote routine runs on Anthropic-managed cloud infrastructure even when your computer is off, and can also fire on API calls or GitHub events. This page covers local scheduled tasks; for remote routines and their trigger options, see [Routines](https://code.claude.com/docs/en/routines).
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#compare-scheduling-options)
Compare scheduling options
Claude Code offers three ways to schedule recurring or one-off work:  
|   | [Cloud](https://code.claude.com/docs/en/routines)  | [Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks)  | [`/loop`](https://code.claude.com/docs/en/scheduled-tasks)  |  
| --- | --- | --- | --- |  
| Runs on  | Anthropic cloud  | Your machine  | Your machine  |  
| Requires machine on  | No  | Yes  | Yes  |  
| Requires open session  | No  | No  | Yes  |  
| Persistent across restarts  | Yes  | Yes  | Restored on `--resume` if unexpired  |  
| Access to local files  | No (fresh clone)  | Yes  | Yes  |  
| MCP servers  | Connectors configured per task  |  [Config files](https://code.claude.com/docs/en/mcp) and connectors  | Inherits from session  |  
| Permission prompts  | No (runs autonomously)  | Configurable per task  | Inherits from session  |  
| Customizable schedule  | Via `/schedule` in the CLI  | Yes  | Yes  |  
| Minimum interval  | 1 hour  | 1 minute  | 1 minute  |  
Use **cloud tasks** for work that should run reliably without your machine. Use **Desktop tasks** when you need access to local files and tools. Use **`/loop`**for quick polling during a session.
By default, scheduled tasks run against whatever state your working directory is in, including uncommitted changes. Enable the worktree toggle when creating the task to give each run its own isolated Git worktree, the same way [parallel sessions](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions) work.
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)
Create a scheduled task
Click **Routines** in the sidebar, then click **New routine** and choose **Local**. Configure these fields:  
| Field  | Description  |  
| --- | --- |  
| Name  | Identifier for the task. Converted to lowercase kebab-case and used as the folder name on disk. Must be unique across your tasks.  |  
| Description  | Short summary shown in the task list.  |  
| Instructions  | What Claude should do when the task runs. Write this the same way you’d write any message in the prompt box. The instructions input includes pickers for the permission mode and model, and below it you select the working folder and whether to run in an isolated worktree.  |  
| Schedule  | How often the task runs. See [schedule options](https://code.claude.com/docs/en/desktop-scheduled-tasks#schedule-options) below.  |  
A folder is required before you can save the task. If you haven’t trusted that folder yet, Desktop prompts you to trust it before saving. You can also create a task by describing what you want in any session. For example, “set up a daily code review that runs every morning at 9am” creates a recurring task, and “remind me at 3pm tomorrow to check the deploy” creates a one-time task that disables itself after it fires.
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#schedule-options)
Schedule options
Pick a preset from the Schedule control:
  * **Manual** : no schedule, only runs when you click **Run now**. Useful for saving a prompt you trigger on demand
  * **Hourly** : runs every hour
  * **Daily** : shows a time picker, defaults to 9:00 AM local time
  * **Weekdays** : same as Daily but skips Saturday and Sunday
  * **Weekly** : shows a time picker and a day picker

For intervals the picker doesn’t offer, such as every 15 minutes, the first of each month, or a single run at a specific future time, ask Claude in any Desktop session to set the schedule. Use plain language; for example, “schedule a task to run all the tests every 6 hours.”
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#how-scheduled-tasks-run)
How scheduled tasks run
Scheduled tasks run on your machine. Desktop checks the schedule every minute while the app is open and starts a fresh session when a task is due, independent of any manual sessions you have open. Each task gets a small delay of a few minutes after the scheduled time to stagger API traffic. The delay is deterministic: the same task always starts at the same offset. When a task fires, you get a desktop notification and a new session appears under a **Scheduled** section in the sidebar. Open it to see what Claude did, review changes, or respond to permission prompts. The session works like any other: Claude can edit files, run commands, create commits, and open pull requests. Tasks only run while the desktop app is running and your computer is awake. If your computer sleeps through a scheduled time, the run is skipped. To prevent idle-sleep, enable **Keep computer awake** in Settings under **Desktop app → General**. Closing the laptop lid still puts it to sleep. For tasks that need to run even when your computer is off, or that should trigger on an API call or GitHub event, create a remote [routine](https://code.claude.com/docs/en/routines) instead.
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#missed-runs)
Missed runs
When the app starts or your computer wakes, Desktop checks whether each task missed any runs in the last seven days. If it did, Desktop starts exactly one catch-up run for the most recently missed time and discards anything older. A daily task that missed six days runs once on wake. Desktop shows a notification when a catch-up run starts. Keep this in mind when writing prompts. A task scheduled for 9am might run at 11pm if your computer was asleep all day. If timing matters, add guardrails to the prompt itself, for example: “Only review today’s commits. If it’s after 5pm, skip the review and just post a summary of what was missed.”
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#permissions-for-scheduled-tasks)
Permissions for scheduled tasks
Each task has its own permission mode, which you set when creating or editing the task. Allow rules from `~/.claude/settings.json` also apply to scheduled task sessions. If a task runs in Ask mode and needs to run a tool it doesn’t have permission for, the run stalls until you approve it. The session stays open in the sidebar so you can answer later. To avoid stalls, click **Run now** after creating a task, watch for permission prompts, and select “always allow” for each one. Future runs of that task auto-approve the same tools without prompting. You can review and revoke these approvals from the task’s detail page.
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)
Manage scheduled tasks
Click a task in the **Routines** list to open its detail page. From here you can:
  * **Run now** : start the task immediately without waiting for the next scheduled time
  * **Status** : toggle between Active and Paused to pause or resume scheduled runs without deleting the task
  * **Edit** : change the instructions, schedule, folder, or other settings
  * **Review history** : see every past run, including skipped runs. Hover a skipped entry to see why: your computer was asleep, the previous run was still in progress, or other scheduled tasks were already running. Click **Show more** to load older entries.
  * **Review allowed permissions** : see and revoke saved tool approvals for this task from the **Always allowed** panel
  * **Delete** : remove the task and archive all sessions it created

You can also list, create, edit, and pause tasks by asking Claude in any Desktop session. For example, “pause my dependency-audit task” or “show me my scheduled tasks.” To delete a task, use the **Delete** button on its detail page. To edit a task’s prompt on disk, open `~/.claude/scheduled-tasks/<task-name>/SKILL.md` (or under [`CLAUDE_CONFIG_DIR`](https://code.claude.com/docs/en/env-vars) if set). The file uses YAML frontmatter for `name` and `description`, with the prompt as the body. Changes take effect on the next run. Schedule, folder, model, and enabled state are not in this file: change them through the Edit form or ask Claude.
## 
[​](https://code.claude.com/docs/en/desktop-scheduled-tasks#related-resources)
Related resources
  * [Routines](https://code.claude.com/docs/en/routines): run tasks on Anthropic-managed infrastructure on a schedule, via API call, or in response to GitHub events, even when your computer is off
  * [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks): session-scoped scheduling with `/loop` in the CLI
  * [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions): run Claude on a schedule in CI instead of on your machine
  * [Use Claude Code Desktop](https://code.claude.com/docs/en/desktop): the full Desktop app guide


Was this page helpful?
YesNo
[Reference](https://code.claude.com/docs/en/desktop)[Chrome extension (beta)](https://code.claude.com/docs/en/chrome)
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
[Privacy choices](https://code.claude.com/docs/en/desktop-scheduled-tasks)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.
