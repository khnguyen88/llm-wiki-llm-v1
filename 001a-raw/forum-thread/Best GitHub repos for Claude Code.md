---
title: "Best GitHub repos for Claude Code"
source: "https://www.reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/"
author:
    - "[[I_AM_HYLIAN]]"
published: 2026-04-22
created: 2026-04-23
description: "tried 40+ skills, plugins, and helpers. most got uninstalled within a week. these stayed. Big ones: awesome-claude-skills (ComposioHQ, 55."
tags:
    - "clippings"
---

tried 40+ skills, plugins, and helpers. most got uninstalled within a week. these stayed.

Big ones:

[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (ComposioHQ, 55.5k stars). canonical Claude Skills list. PDF/Word/Excel/PPT, CSV analysis, brand voice, Composio-backed SaaS integrations. where i find most of the skills i install.

Repomix (yamadashy, 23.7k stars). packs a repo into one file Claude can read. replaces the copy-paste-15-files workflow.

agent-orchestrator (ComposioHQ, 6.4k stars). parallel Claude Code sessions across git worktrees. one agent per feature branch, CI auto-handled.

ccusage (ryoppippi, 13.2k stars). CLI that prints token spend per session. most "Claude is expensive" posts are people who never looked at their own numbers.

Five bookmarked: awesome-claude-code (40k, broader than the skills list), SuperClaude_Framework (22.4k), context-mode (8.8k, MCP token bloat), claude-code-system-prompts (9.3k, reverse-engineered system prompts), awesome-claude-plugins (ComposioHQ, 1.4k).

what's in your top 3.

Edit: List of everyone mine and favorite:
https://github.com/jqueryscript/awesome-claude-code
https://github.com/ryoppippi/ccusage
https://github.com/ComposioHQ/agent-orchestrator
https://github.com/pcvelz/superpowers
https://github.com/gsd-build/get-shit-done
https://github.com/yamadashy/repomix
https://github.com/SuperClaude-Org/SuperClaude_Framework
https://github.com/mksglu/context-mode
https://github.com/Piebald-AI/claude-code-system-prompts
https://github.com/ComposioHQ/awesome-claude-plugins
https://github.com/Mathews-Tom/armory

---

## Comments

> **yolk3d** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm54kq/) · 29 points
>
> There’s tonnes of these threads and blogs. Superpowers for everyday development.
>
> > **I_AM_HYLIAN** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm5g0f/) · 4 points
> >
> > oops sorry i forgot superpowers!

> **SgtPeanut_Butt3r** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmi9lr/) · 11 points
>
> GSD
>
> > **Slothilism** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohpzdp4/) · 2 points
> >
> > Don’t know why GSD isn’t more popular! Superpowers got me started with skills a few months back, but the randomness of the skill invoking and lack of proper “planning” made me look for more. GSD literally breaks it down into digestible phases to where there should be no misunderstanding between you and the machine. Don’t get me wrong it’s still buggy or loops when it shouldn’t, but it’s gotten me quite far on personal projects.

> **LawfulnessSlow9361** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm6ew3/) · 22 points
>
> OpenWolf (github.com/cytostack/openwolf). 6 hooks that give Claude a file index, learning memory, and token ledger. Claude stops re-reading files it already opened, remembers your corrections across sessions, and you can see exactly where tokens go. One init, then invisible. Stayed because it's the only thing that actually reduced how fast I hit limits.
>
> > **Danieboy** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmcdmm/) · 3 points
> >
> > First I'm hearing of this, strange
> >
> > > **LawfulnessSlow9361** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohnpzp5/) · 1 point
> > >
> > > Check out the docs at: openwolf.com
> > >
> > > It's free, opensource.
>
> > **hibzy7** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohpldvq/) · 1 point
> >
> > Just checked this. This overlaps with graphify. So just either will do. But yeah looks good

> **NightSp4rk** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm989m/) · 7 points
>
> Superpowers is missing in there :)
>
> > **ALEX_BUROV** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohn30d9/) · 3 points
> >
> > Best plugin

> **tensorfish** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm3bou/) · 3 points
>
> ccusage and repomix stayed. Third slot ended up being my own boring repo template for CLAUDE.md, file map, and test aliases, because most public setup packs become plugin tax fast. Tiny global defaults plus repo-local rules beat a giant universal setup.

> **Putrid_Ground_1065** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm2gtd/) · 2 points
>
> How do you keep your CLAUDE.md from bloating? Mine keeps growing and Claude ignores 80% of it past a point
>
> > **I_AM_HYLIAN** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm32z3/) · 6 points
> >
> > 40 line root, rest in skill files claude pulls on demand. past 200 lines it stops reading the bottom anyway.
> >
> > > **Any_Owl2116** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm7uks/) · 1 point
> > >
> > > Please expound
> > >
> > > > **fs2d** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmpa5n/) · 3 points
> > > >
> > > > OP is correct - this is SL implementation theory. 40-60 line system prompt, and skills are loaded on demand that dynamically inject into the prompt. Keeps the active context window fresh for longer (ie: it takes longer for the core system rules to end up so far away in the context that Claude stops reading them).
> > > >
> > > > The other part of this equation is to keep skills limited to 1-2 actions per skill, keep them concise and explicit, and to manage your context properly. Same idea - keeping the context slim to forego pushing core directives further back in the context history is the best way to ensure adherence across the board.
> > > >
> > > > > **makinggrace** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohpzh5q/) · 2 points
> > > > >
> > > > > What is "SL implementation theory"? These concepts are what I have stumbled my way into but knowledge would be helpful
> > > > >
> > > > > > **fs2d** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohrbjpd/) · 1 point
> > > > > >
> > > > > > Sorry, internal talk at work - Single Loop architecture / Single Loop implementation. The idea is that in a SL setup, there is only one agent that calls tools in a loop - so all payload responses, etc get dumped into the context continually rather than chunked into variables and sent in pieces like they are in a planner/synthesizer loop.
> > > > > >
> > > > > > SL implementation (in our environment) refers to our process where we streamline the system prompt down into explicit "shape" directives only (sub 60 lines or so) and the assign "doctrine" / "domain" / etc directives to skills that only get injected into the context when needed.
> > > > > >
> > > > > > This helps to allow the SL agent to retain the core system directives longer and assists with staving off context drift.
> > > >
> > > > > **ImperatorPC** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohquijd/) · 1 point
> > > > >
> > > > > If you wouldn't mind providing some examples id really appreciate it. Are you putting additional context rules in the skill or telling Claude via the main prompt where another file is that had more information it can get if it needs it?
> > > > >
> > > > > > **fs2d** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohrl2b2/) · 1 point
> > > > > >
> > > > > > Sure - I posted this in reply to the other person but it applies here too:
> > > > > >
> > > > > > > Single Loop architecture / Single Loop implementation. The idea is that in a SL setup, there is only one agent that calls tools in a loop - so all payload responses, etc get dumped into the context continually rather than chunked into variables and sent in pieces. SL implementation (in our environment) refers to our process where we streamline the system prompt down into explicit "shape" directives only (sub 60 lines or so) and the assign "doctrine" / "domain" / etc directives to skills that only get injected into the context when needed.
> > > > > > >
> > > > > > > This helps to allow the SL agent to retain the core system directives longer and assists with staving off context drift.
> > > > > >
> > > > > > > **smdaegan** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohrmrtl/) · 1 point
> > > > > > >
> > > > > > > I read this but I still don't understand how I'd even implement it. 

> **SMB-Punt** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmgjht/) · 2 points
>
> "agent-orchestrator" ? Claude Code already handle git worktrees ?

> **tom_mathews** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmmnku/) · 2 points
>
> repomix is the one i kept too, the copy-paste workflow was actually killing me before that. ccusage is underrated, half the "claude is broken" threads are people not realizing their /init alone burns 40k tokens. been quietly maintaining my own collection at [https://github.com/Mathews-Tom/armory](https://github.com/Mathews-Tom/armory), skills/agents/hooks i actually use day to day, not the kitchen sink kind, ymmv.
>
> > **notDonaldGlover2** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohqyb2r/) · 1 point
> >
> > > repomix
> >
> > how does it deal with massive monorepos?

> **No_Tooth_4909** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohqzkmo/) · 2 points
>
> built a tool that plants a forest in terminal while you code 🤷

> **thecontentengineer** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm3brk/) · 3 points
>
> gstack missing! not for everyone but biggest everyone talks about
>
> > **I_AM_HYLIAN** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm3r47/) · 5 points
> >
> > not for me tbh too much brainstorming lol

> **InfinriDev** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm4f6u/) · 1 point
>
> [https://github.com/infinri/Phaselock](https://github.com/infinri/Phaselock)

> **qwertyalp1020** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm6onb/) · 1 point
>
> I use [https://github.com/KhazP/vibe-coding-prompt-template](https://github.com/KhazP/vibe-coding-prompt-template) before starting a repo

> **Kevin_Xiang** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmmajb/) · 1 point
>
> I've been curating a similar list internally. The repos that actually stick are the ones with eval harnesses or sandboxing built in, not just wrappers. Would love to see a category for 'agent safety / rollback' if you expand this.

> **Worried-Squirrel2023** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmmgmi/) · 1 point
>
> curated lists are useful but the bigger win is picking 3-4 repos and following their issue trackers directly. you learn more from watching people hit real bugs than from star-count rankings.

> **baradas** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmrezi/) · 1 point
>
> Give this a spin  
> [https://github.com/mercurialsolo/claudectl](https://github.com/mercurialsolo/claudectl)
>
> Auto-pilot for claude code sessions - fully local brain | MIT
>
> [<image>](https://i.redd.it/hxxqwsr8yqwg1.gif)

> **ALEX_BUROV** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohn3927/) · 1 point
>
> Claude squad or agent dock better than agent-orchestrator. Superpowers > skills + agents

> **Fun_Potential_3520** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohn5qsq/) · 1 point
>
> [https://github.com/EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)

> **andan02** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohp4chp/) · 1 point
>
> See where your repo ranks. Get a badge to show others. [https://console.kubestellar.io/acmm](https://console.kubestellar.io/acmm)

> **nyldn** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohpltq5/) · 2 points
>
> Keep using Claude Code but shift the real work to Codex:
>
> [https://github.com/nyldn/claude-octopus](https://github.com/nyldn/claude-octopus)

> **jajanet** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohpx6be/) · 1 point
>
> ccusage is overrated. It's just another standard token dashboard
>
> Would be better if you could actually manage old windows and sessions

> **UTedeX** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohq38g7/) · 1 point
>
> !RemindMe 5 days
>
> > **RemindMeBot** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohq3cb3/) · 1 point
> >
> > I will be messaging you in 5 days on [**2026-04-27 23:34:52 UTC**](http://www.wolframalpha.com/input/?i=2026-04-27%2023:34:52%20UTC%20To%20Local%20Time) to remind you of [**this link**](https://www.reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohq38g7/?context=3)
> >
> > [**CLICK THIS LINK**](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2FClaudeCode%2Fcomments%2F1ssimaz%2Fbest_github_repos_for_claude_code%2Fohq38g7%2F%5D%0A%0ARemindMe%21%202026-04-27%2023%3A34%3A52%20UTC) to send a PM to also be reminded and to reduce spam.
> >
> > <sup>Parent commenter can </sup> [<sup>delete this message to hide from others.</sup>](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Delete%20Comment&message=Delete%21%201ssimaz)
> >
> > ---
> >
> > | [<sup>Info</sup>](https://www.reddit.com/r/RemindMeBot/comments/e1bko7/remindmebot_info_v21/) | [<sup>Custom</sup>](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5BLink%20or%20message%20inside%20square%20brackets%5D%0A%0ARemindMe%21%20Time%20period%20here) | [<sup>Your Reminders</sup>](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=List%20Of%20Reminders&message=MyReminders%21) | [<sup>Feedback</sup>](https://www.reddit.com/message/compose/?to=Watchful1&subject=RemindMeBot%20Feedback) |
> > | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |

> **petertanham** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohrfl6j/) · 2 points
>
> You can see a full list of these (and sort by popularity) at [https://sharedcontext.ai/library](https://sharedcontext.ai/library%C2%A0) 

> **ninjaway16** · [2026-04-23](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohrhxjc/) · 1 point
>
> I built spine architecture to handle my daily software development, saves about 80% of tokens. Give it a try. [https://github.com/Nodewarrior/spine](https://github.com/Nodewarrior/spine)

> **btherl** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohm9sw9/) · 0 points
>
> Why would you need repomix with Claude Code? It can access local files with tools.

> **Input-X** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohny1mk/) · 0 points
>
> Worth a look, in beta rn. Fyi use with opus, 4.6. 4.7 is unhinged.
>
> [https://github.com/AIOSAI/AIPass](https://github.com/AIOSAI/AIPass)

> **themoregames** · [2026-04-22](https://reddit.com/r/ClaudeCode/comments/1ssimaz/best_github_repos_for_claude_code/ohmgcyc/) · \-4 points
>
> What
