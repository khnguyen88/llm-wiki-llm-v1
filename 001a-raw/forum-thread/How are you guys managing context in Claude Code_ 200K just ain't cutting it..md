---
title: "How are you guys managing context in Claude Code? 200K just ain't cutting it."
source: "https://www.reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/"
author:
  - "[[Dangerous-Formal5641]]"
published: 2026-03-12
created: 2026-04-23
description: "its a codex app screen shot So, Claude Code is great and all, but I've noticed that once it hits the limit and does a \"compact,\" the respon"
tags:
  - "clippings"
---
[its a codex app screen shot](https://preview.redd.it/9bxum9ceokog1.png?width=984&format=png&auto=webp&s=eea148125a1e5417348c4aabb5145c5123998586)

So, Claude Code is great and all, but I've noticed that once it hits the limit and does a "compact," the responses start subtly drifting off the rails. At first, I was gaslighting myself into thinking my prompts were just getting sloppy. But after reviewing my workflow, I realized from experience that whenever I'm working off a strict "plan," the compacting process straight-up nukes crucial context.

(I wish I could back this up with hard numbers, but idk how to even measure that. Bottom line: after it compacts, constraints like the outlines defined in the original plan just vanish into the ether.)

I'm based in Korea, and I recently snagged a 90% off promo for ChatGPT Pro, so I gave it a shot. Turns out their Codex has a massive 1M context window. Even if I crank it up to the GPT 5.4 + Fast model, I’m literally swimming in tokens. (Apparently, if you use the Codex app right now, they double your token allowance).

I've been on it for 5 days, and I shed a tear (okay, maybe not literally 🤖) realizing I can finally code without constantly stressing over context limits.

That said, Claude definitely still has that undeniable special sauce, and I really want to stick with it.

So... how are you guys managing your context? It's legit driving me nuts.

---

## Comments

> **ClaudeAI-mod-bot** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa247tw/)
> 
> **TL;DR of the discussion generated automatically after 50 comments.**
> 
> Yep, the consensus is that the context compaction issue is very real and you're not just gaslighting yourself. The community is overwhelmingly in agreement that Claude Code gets amnesia after it compacts.
> 
> **The community's top advice is to stop treating the context window as your primary memory and start using files instead.** The general sentiment is that while a 1M context window sounds nice, all models suffer from performance degradation at that scale anyway. The key is disciplined context management, not just a bigger window.
> 
> Here are the main strategies the thread is recommending:
> 
> - **The `CLAUDE.md` Method:** This is the most upvoted solution. Create a `CLAUDE.md` file in your project's root. Claude reads this automatically every session. Put your core architecture, constraints, and high-level plan in there. It's your persistent memory that survives compaction. You can also create other files like `PLAN.md` or `TODO.md` and instruct Claude (in `CLAUDE.md`) to read them at the start of each session.
> - **Use Subagents Heavily:** This is the second most popular strategy. Send agents off to do research or implement smaller pieces of code. They do the token-heavy work and report back a concise summary, keeping your main context clean and focused.
> - **Work in Smaller Chunks:** Don't let a single session grow large enough to require compaction in the first place. Break your work into smaller, logical features. Finish one, then start a fresh conversation for the next one.
> - **Create "Handoff Docs":** Before your context fills up, have Claude create a summary document of the session's progress, key decisions, and next steps. Start a new session and have it read that handoff doc to get up to speed instantly.

> **RestaurantHefty322** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa08m9m/) · 73 points
> 
> The compaction issue is real and there are a few things that genuinely help.
> 
> First, use a [CLAUDE.md](http://claude.md/) file in your project root. Claude Code reads this at the start of every conversation, so you can put your architectural decisions, constraints, coding standards, and the current plan there. When context gets compacted, the [CLAUDE.md](http://claude.md/) still gets loaded fresh. Think of it as persistent memory that survives compaction.
> 
> Second, break your work into smaller, focused sessions. Instead of one massive session where you build an entire feature, do one session per logical unit - "implement the auth middleware," then start a new conversation for "wire up the auth routes." Each session stays well within the context window and you do not lose coherence.
> 
> Third, use the /compact command proactively before Claude auto-compacts. When you trigger it yourself, you can add instructions like "/compact - preserve the current implementation plan and all file paths discussed." This gives you more control over what survives.
> 
> Fourth, offload your plan to actual files. Create a [PLAN.md](http://plan.md/) or [TODO.md](http://todo.md/) in your repo that Claude updates as it works. That way the plan lives in the filesystem, not in context. When context resets, Claude just reads the file.
> 
> The 200K limit is workable once you stop treating context as your primary memory and start treating files as memory instead. The models that have 1M context are nice, but you end up with similar drift problems at that scale too - the model just forgets things further back in the window. Structured external memory (files, docs, CLAUDE.md) scales better than raw context length.
> 
> > **tarix76** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0g3i6/) · 36 points
> > 
> > Fifth, use subagents heavily to return a smaller context so that you do not taint your main context with useless tokens.
> > 
> > > **quantum1eeps** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0otjt/) · 7 points
> > > 
> > > This is as important as the other points. This is the way to include more context in your session is by sending agents off to do work and bringing their summaries back to the session context
> > > 
> > > **Ok\_Diver9921** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0ir7a/) · 10 points
> > > 
> > > Good call on subagents. That is probably the single biggest context saver - let the subagent do the heavy exploration and just return the 3-4 lines you actually need back to the main conversation.
> > > 
> > > **laxrulz777** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa14ssy/) · 3 points
> > > 
> > > How do you forcibly kickoff a sub agent?
> > > 
> > > > **Ill-Pilot-6049** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1ax7e/) · 9 points
> > > > 
> > > > In your prompt, include something like "deploy subagents to do x...y....z". You can explicitly call a number, or you can let claude decide (typically does 3 subagents)
> > 
> > > **dubious\_capybara** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0s3kq/) · 1 point
> > > 
> > > Source? I don't see anywhere that sub agents are max only
> > > 
> > > > **tarix76** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0u9so/) · 1 point
> > > > 
> > > > Source was a comment in this thread which appears to be wrong.
> > 
> > > **hereditydrift** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1ydl3/) · 1 point
> > > 
> > > Subagents and linking CC to gemini 3.1 for brainstorming/1st review has been helpful. Opus is primarily my QC for projects.
> > > 
> > > > **thecneu** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa5dbd9/) · 1 point
> > > > 
> > > > How do you do that.
> > > > 
> > > > > **hereditydrift** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa5g4ca/) · 1 point
> > > > > 
> > > > > Gemini is just through the Gemini CLI and Claude uses a skill to access the 3.1 model or other models. If I need CC to make graphics for websites or other uses, then I have claude use Claude for Chrome and prompt Gemini directly. The other stuff (Opus as QC and last reviewer) is just prompts when planning.
> > > > > 
> > > > > What you need to set up Gemini for Claude Code:
> > > > > 
> > > > > 1. Install the Gemini CLI - Google's command-line tool ([https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)). Install with npm install or however Google distributes it.
> > > > > 2. Authenticate - Log in with your Google account so the CLI can make requests.
> > > > > 3. Create the skill file - Put the markdown file at ~/.claude/commands/gemini.md.
> 
> > **communomancer** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1ewq0/) · 2 points
> > 
> > > The compaction issue is real and there are a few things that genuinely help.
> > 
> > If OP wanted to ask Claude for the answer he is already paying for an account.
> > 
> > > **UnifiedFlow** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1nk26/) · 2 points
> > > 
> > > You're right to be frustrated and you are not crazy.
> 
> > **Fuckinglivemealone** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa2cvbl/) · 2 points
> > 
> > What I wonder is why is there no tool to ease/automate all these steps for the user. Based on what's posted on this sub we all try similar measures that end up involving us more than needed on the development process. I understand that there are different use cases but this seems like something almost everyone would benefit of?
> > 
> > > **RestaurantHefty322** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa2f0sp/) · 1 point
> > > 
> > > There are a few tools trying - Claude's auto-memory feature does some of this automatically, and there are community projects like claude-memory and context-pilot that attempt to manage it. But honestly the problem is that what's "worth remembering" is so project-specific that generic tooling struggles. Your CLAUDE.md for a web app looks nothing like one for an ML pipeline. For now the manual setup takes maybe 10 minutes and then just works across sessions, which is hard to beat with automation that might get it wrong.
> > > 
> > > > **Fuckinglivemealone** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa2qikw/) · 2 points
> > > > 
> > > > > Claude's auto-memory
> > > > 
> > > > Ah that must've been quite recent, I didn't know of it until now, thank you!
> > > > 
> > > > To be honest, I get your point that there every project is a different world, but still I feel we do quite a lot of babysitting and provide a lot of guidance on things that could easily be already done/inferred by Claude itself, keeping its memory consistent using documents, injecting smart context, resetting sessions, documenting the progress, creating and using skills, spawning subagents...
> > > > 
> > > > I think an orchestrator that dealt with all those things automatically based on the project's contents and goals and user preferences would do wonders and save us quite a lot of time.
> > > > 
> > > > I'm afraid to admit I spend way more than 10 minutes of manual work setting up everything for CC/Codex to work as autonomously as possible using strict methodologies and even then, they lose their way eventually during development or the results are not really that good, specially for GUI development or for deep testing of workflows. It probably is a skill issue though. Kinda wish the recent Anthropic CC course touched more of this stuff and less basic prompting.
> 
> > **Monkeyslunch** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0rcrl/) · 1 point
> > 
> > This is the way
> > 
> > **mightybob4611** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1nocl/) · 1 point
> > 
> > Do you have to tell it to read the todo.md and plan.md etc? Or it just reads all .md files on each session? How does that work?
> > 
> > > **RestaurantHefty322** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1pzvp/) · 2 points
> > > 
> > > CLAUDE.md gets auto-loaded every session - that one you get for free. For todo.md and plan.md, you reference them explicitly in CLAUDE.md like "always read todo.md at session start before doing anything." Once it reads that instruction it pulls the files automatically. You can also just tell it mid-session to check a file and it'll do it.
> > > 
> > > The key is CLAUDE.md is your bootstrap - everything else chains from there.
> > > 
> > > > **mightybob4611** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa26tgc/) · 1 point
> > > > 
> > > > Appreciate it, thanks!
> 
> > **InanimateCarbonRodAu** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0qr3o/) · 0 points
> > 
> > What kind of memento bullshit is this… this is how we end up killing John G a bunch of times

> **Ebi\_Tendon** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa088jy/) · 28 points
> 
> Performance starts to drop after 100k, and it drops dramatically after 150k. After 250k, Codex’s performance drops to around 50%. Just because you have a 1M context window doesn’t mean you should use all of it.
> 
> > **Dangerous-Formal5641** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0anp9/) · 2 points
> > 
> > Honestly, it’s like **picking your poison** at this point. ChatGPT’s 'lost in the middle' issue (if that’s the right term) vs. Claude getting **straight-up amnesia** after a compact... it's a really tough call.
> > 
> > > **cannontd** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa42jxo/) · 1 point
> > > 
> > > It’s just the way LLMs are. I was testing openwebui with a 1m backed LLM and thought to test it I would upload an 800k file with secrets scattered across it and it found 5/7 with some at the end and some at the beginning - the 30-50% part is a real blind spot. And when people who don’t want to manage context ask how to fix it and you say it’s a feature of the LLM things get wild. We’re too used to determinism.
> > > 
> > > **Ebi\_Tendon** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0b6k6/) · \-1 points
> > > 
> > > You have many ways to make CC survive compaction, like using hooks to feed skill data back and making a skill read breadcrumbs to recover important information. But after 200k in Codex, you can’t guarantee that it’s still working properly.
> 
> > **StopGamer** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa09g43/) · \-3 points
> > 
> > Also codex by itself is worse for non coding, you can use Sonnet 1m with same effect

> **Agravak** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa08t81/) · 6 points
> 
> Have you tried instructing Claude to launch multiple agents, breaking down the workflow you want to do into smaller parts? this is my approach so far. Although 12 agents seem to eat up 85% of the mother agent's context window, and I believe this also depends on the type of reporting asked from each of the sub-agents
> 
> > **buff\_samurai** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0a2vm/) · 0 points
> > 
> > He is on pro, agents are useful only on max.
> > 
> > With agents you need tokens to optimize tokens 🤷🏼‍♂️
> > 
> > > **Agravak** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0ekwr/) · 3 points
> > > 
> > > Ah makes sense, to be honest I only found Pro useful for starting with Claude, and Max has been well worth the money, I try to optimize tokens with a planning tool that I built that allows easy prompt iteration/refinement and a visual view of the multi-agent launch plan with skills assignment per agent
> > > 
> > > > **buff\_samurai** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0fejv/) · 2 points
> > > > 
> > > > … and you can define agent’s model too, no need to refactor with Opus high.

> **UberBlueBear** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0ks7g/) · 7 points
> 
> Going through the [prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) and implementing some of the best practices significantly reduced my issues with context window usage.
> 
> Also, as others have said, work in small chunks…clearing the context window each time.

> **Mundane\_Reach9725** · [2026-03-25](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/ocgvz92/) · 2 points
> 
> The 200K limit is workable once you stop treating context as your primary memory and start treating files as memory instead. Use a [`CLAUDE.md`](http://claude.md/) for session hygiene, and write a session-handoff doc whenever you finish a logical unit. Break your work into smaller chunks—implement the auth middleware, then start a completely fresh conversation for the auth routes. The model just forgets things further back in the window, so structured external memory scales way better than raw context length.

> **ifthenthendont** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0fwiy/) · 3 points
> 
> Gsd
> 
> > **balancedgif** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1ghr3/) · 1 point
> > 
> > gsd is a token eating monster
> > 
> > > **UnifiedFlow** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1nswn/) · 1 point
> > > 
> > > I disagree. Its only a token eating monster if you insist on using it with max research/validation/phase settings. It has about 20 different knobs to control token usage.

> **Maleficent-Pair-808** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0nic7/) · 1 point
> 
> I tell it to spin up subagents for everything, and that it only act as a manager. Also I inform it to write to memory regularly and where possible clear its own context (it can’t seem to do that though)
> 
> > **PenfieldLabs** · [2026-03-16](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oaok3w8/) · 1 point
> > 
> > The 'write to memory regularly' instinct is right but the problem is where does it write to? If it's CLAUDE.md you're back to a flat file that gets bigger and noisier. If it's separate files you end up with a folder of disconnected notes. The missing piece is a memory layer that understands relationships: a knowledge graph.

> **Failcoach** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0yfrb/) · 1 point
> 
> With a little time and reflection I developed rough understanding how big my PRDs can be to finish at around 150k tokens.

> **FineInstruction1397** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa18acb/) · 1 point
> 
> disable auto-compact and use "/clear"  
> best context management

> **GPThought** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1aypj/) · 1 point
> 
> i keep a CONTEXT.md file at root with architecture notes. when context fills up claude reads that instead of me reexplaining the whole setup. still hits limits but helps a lot
> 
> > **PenfieldLabs** · [2026-03-16](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oaojx38/) · 1 point
> > 
> > CONTEXT.md works but it's a flat file, no structure, no relationships between concepts, no way to query by time. What we've been exploring is knowledge graph approaches; typed connections between memories with temporal filtering. So instead of 'here's everything about my project' it's 'what decisions did I make about auth last week' and you get just that, with the reasoning chain attached. The file-based approach breaks down once your project has more than a dozen interconnected decisions.
> > 
> > > **GPThought** · [2026-03-16](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oaq4s90/) · 1 point
> > > 
> > > knowledge graphs are the right direction but the tooling isnt there yet. tried a few and spent more time debugging the graph than using it. for now im just dumping structured markdown with good search. when you need to query by time you can parse the headers
> > > 
> > > > **PenfieldLabs** · [2026-03-16](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oasftp2/) · 1 point
> > > > 
> > > > That's exactly the problem we've been trying to solve. If the setup is tedious, or the system is unreliable, nobody will use it. Our approach: no code to download, no configs to debug. Connector install on platforms that support it, MCP remote or API for everything else. Most people are up and running in under 5 minutes (if you already have an account 1-2 minutes). The graph builds as you use it, you don't have to think about it.

> **DabaDay** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1d8ji/) · 1 point
> 
> Ralph loop fixes this

> **\_Bo\_Knows** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1eaqk/) · 1 point
> 
> Best I’ve found is chunk up your work into manageable context and use subagents/Context Fork isolation. I suggest turning all of that into a set of skills that make up your workflow. Here is mine as an example. [https://github.com/boshu2/agentops](https://github.com/boshu2/agentops)

> **yopetey** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1mzfi/) · 1 point
> 
> this [link](https://hannahstulberg.substack.com/p/claude-code-for-everything-finally?r=7m6lj&triedRedirect=true&utm_medium=ios) helped me specifically in this [article](https://hannahstulberg.substack.com/p/claude-code-for-everything-why-ai) they talk about Manual compaction (Run `/compact` with the instructions Claude helped you draft.) This is just a quick TLDR the article goes into more detail

> **koneu** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1ojyz/) · 1 point
> 
> I have Claude document stuff. I let it write various files that turn out to be concise and helpful. So I always have it document before a commit and before I manually clean up. 

> **Chris266** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1rxg3/) · 1 point
> 
> I created a skill called context handoff that runs when I reach 75% of my context. It creates a handoff doc about things we've been working on in our session common pitfalls and knowledge gained. What's coming up, etc... then I start a new session and tell it to read the handoff doc, rinse repeat. I find it works better than compaction so far.
> 
> > **sandman\_br** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa4l7vq/) · 1 point
> > 
> > How is this different from compact the context?
> > 
> > > **Chris266** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa66gz4/) · 1 point
> > > 
> > > Well im not entirely sure how technically different it is but it seems faster to me and I get a record right in my project of the handoff and the date and time. I can check it out and remove or add anything I want before I get the new session to load it.

> **titomb345** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1vtpq/) · 1 point
> 
> check out RTK

> **Aminuteortwotiltwo** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1z9q2/) · 1 point
> 
> Cmon buddy you can do some of the thinking. Hopefully we haven’t already given up on that!
> 
> What are the ways you have to prepare a new instance?
> 
> You have your prompt, and literally as detailed of other markdown files as you want and they can be referenced at any time.
> 
> Can you create a skill that utilizes your multiple opportunities for reference and direction in order to allow a new instance the very best material for the very best outcomes?
> 
> Have you tried asking Claude for suggestions?
> 
> > **Aminuteortwotiltwo** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa1zwy9/) · 1 point
> > 
> > Oh and compact sucks. It compacts the conversation, not the relevant operations. Redesign it and use it the second you see context hit 50% to update a permanent reference doc. Hint: use md files as your truth, not the material within the chat window. I never use compact, in fact, compact usually leads me to trouble shooting 95% of the time.

> **l0ng\_time\_lurker** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa22pwh/) · 1 point
> 
> In CLaude for Excel I work extra to batch questions and replies, sometimes to "1"

> **emandzee** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa2b2gc/) · 1 point
> 
> Markdown files in the project knowledge bank, a markdown file request requesting ZERO LOSS OF CONTEXT every now and then (I’ve been doing it intuitively when I feel I’ve been chatting without it compacting for a while). It’s been working for me

> **lmp515k** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa2g94v/) · 1 point
> 
> I write my tasks into ADO and the read from there when in start working. I keep ado up to date as I go along using the ado mcp. So I think I am effectively using ado for my context.

> **Hanna\_Bjorn** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa2rhyk/) · 1 point
> 
> Imagine telling someone *"Man, 200k context just isn't enough, a I'm gonna go for the model with 1M"* like two years ago lol

> **IulianHI** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa2xwpk/) · 1 point
> 
> Solid question. I've found the CLAUDE.md approach works best - I keep architecture docs, constraints, and current sprint goals in there. Claude reads it automatically each session so the core context survives compaction. Also started using subagents for research-heavy tasks; they do the token-intensive work and report back summaries, which keeps my main context clean. The key is treating files as your long-term memory, not the chat window.

> **PlantainAmbitious3** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa3cka2/) · 1 point
> 
> tbh the compaction drift is one of the most frustrating parts. ive been writing pretty detailed CLAUDE.md files for each project and it helps a lot because after compact it can at least reload the key rules. still not perfect though, sometimes it just forgets entire design decisions from earlier in the conversation. breaking work into smaller focused sessions has been the biggest improvement for me so far.

> **mark\_tycana** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa43y7h/) · 1 point
> 
> I have had good experience using tools like GSD.

> **ruso-0** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa4drwu/) · 1 point
> 
> This is painfully accurate. The compaction problem is real — I've tracked it across dozens of sessions. After compaction, Claude loses the architectural constraints you set early in the conversation and starts making decisions that contradict your original plan.
> 
> What I've found helps: keep a [CLAUDE.md](http://claude.md/) file in your project root with the critical constraints (schemas, naming conventions, architectural rules). Claude Code reads it at session start, and even after compaction the file is still on disk so you can tell Claude to re-read it. It's not perfect but it recovers maybe 70% of what compaction destroys.
> 
> The deeper issue is that Claude burns through context way too fast by reading entire files when it only needs one function. A 2000-line file eats ~5000 tokens in one read. If you could compress those reads to just signatures + key lines, you'd push the compaction wall back significantly.
> 
> The 1M context on Codex sounds amazing on paper but I'd be curious how it handles quality at that scale — more context doesn't always mean better reasoning. Have you noticed any degradation in code quality with very long sessions on Codex vs shorter Claude sessions?

> **sandman\_br** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa4kuli/) · 1 point
> 
> Ralph loop

> **Deep\_Ad1959** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa56dep/) · 1 point
> 
> biggest thing that helped me was breaking work into smaller conversations instead of trying to keep one massive session alive. start a new chat for each feature or task, keep a CLAUDE.md file at the root with all the important project context so claude picks it up fresh each time. also being selective about what tools you connect helps, every MCP tool response eats context too. i trim my tool configs to only whats needed for the current task

> **Hopeful\_Ad6629** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa5jhb6/) · 1 point
> 
> Honestly, what I do is I have 2 windows open, one is Claude desktop, and one is Claude code terminal.
> 
> The Claude desktop and I plan stuff out and I have it write an MD file for stuff, then I save the md file to the project directory and have Claude code read it, it’ll ask me a few questions that either I answer or copy it over to the Claude desktop for confirmation and back. Then Claude code goes on to build it. I rarely hit the compact window this way.
> 
> Or Claude code will go into planning mode, create the plan then allows me to clear most of the context window when I accept the plan and it goes to execute.
> 
> But to parrot others, having an MD file really does help, and also having an mcp with an extended memory helps too.

> **Outrageous\_Style\_300** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa6brh4/) · 1 point
> 
> And here I am, having to use Claude vis Github CoPilot license at work - stuck at 120k 😑

> **pkg95** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa6gerc/) · 1 point
> 
> I have worked with 2 plugins: claaud-mem and claude-context
> 
> Recently, using the later one, and finding it bete in some cases over simple claude-mem.
> 
> Saved me appox 65-70% in real work cases (over benchmarks which are not as useful and claim 98%).

> **egorfdrv** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa7pd4a/) · 1 point
> 
> Use claude-context-optimizer plugin [https://github.com/egorfedorov/claude-context-optimizer](https://github.com/egorfedorov/claude-context-optimizer)

> **mrtrly** · [2026-03-15](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oai5eu0/) · 1 point
> 
> three things that actually moved the needle for me on context management:
> 
> 1. CLAUDE.md for session hygiene, not just project context. I have explicit rules in mine: write a session-handoff.md whenever I say /done. next session starts by reading that file. no context rebuilt from scratch.
> 2. compact before Claude does it for you. when responses start feeling sloppier, I just say 'summarize what we've built so far and reset from that.' 30 seconds, saves you from 50 degraded messages.
> 3. split your context files. architecture notes, API docs, task lists — all separate. load only what's relevant to the current session. stuffing everything into one CLAUDE.md is burning context budget before you write a single line of code.
> 
> 200K is real but most sessions don't need it if you're disciplined about scope. the real issue is treating Claude Code like a persistent colleague when it's actually a stateless session you need to brief every time.

> **Mundane\_Reach9725** · [2026-03-20](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/objdef3/) · 1 point
> 
> The 200K (or even 1M) window is a trap if you treat it like primary memory. You have to shift your thinking to a file-based memory system.
> 
> Keep a [`CLAUDE.md`](http://claude.md/) and a [`PLAN.md`](http://plan.md/) in your root directory. Force the model to document its architecture and current state into those files constantly. When the context buffer inevitably gets compacted or you need to wipe it clean to regain reasoning sharpness, the model just re-reads the markdown files to instantly orient itself. Context should be for immediate execution, files should be for state.

> **nicoloboschi** · [2026-03-25](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/occbxtv/) · 1 point
> 
> The context window problem is pervasive. You might want to explore Hindsight, a fully open-source memory system for AI agents. It helps extend context beyond the limitations of models like Claude. [https://github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

> **Ill-Pilot-6049** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa09o2o/) · 1 point
> 
> tell claude to deploy subagents. Each subagent has 200k context. They will report the information up the chain.

> **Staggo47** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0sra2/) · 1 point
> 
> [This](https://youtu.be/mZzhfPle9QU?si=oFlR_XHAo53fvaqw) video explores an interesting way to think about "context engineering"

> **ThesisWarrior** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0e6kb/) · 0 points
> 
> Tasks Summary and current task summary md files.
> 
> Implement one feature succesfully. Request claude to Update summary and currect task md. Save project or repo at this stage. Clear conversation. New conversation. Reference those context files to build you new feature set. This in tandem with a tight claude.md file saved me tokens BIGTIME and improved my success hit rate by at least 50% no joke.
> 
> If you do from the very start of your project especially youll be very pleased with results. Why? Because its the accumulation of concise info in your context files over the timeline of the project that tightens the guardrails more and more the further you progress.
> 
> Here is a longer list from a previous post I made re developing an audio plugin
> 
> \- always implement major features in planning mode
> 
> \- use other ai i.e. chatgpt to formulate specific concise prompts to feed Claude. the more accurate the higher your first time hit rate success. Fewer words superior context.
> 
> \- create and ask Claude to update context files i.e. current\_task.md and session\_summary.md in Sonnet or Haiku mode after every feature implementation and SAVE those specific files with your git or backups.
> 
> \- Use /CLEAR after EVERY succesful implementation or part suxcesfull implementation. you can now reference those context files in new conversation context as a summary placeholder. saved me a heap of tokens. insisting on continuing long comversations until I had a resoltuon was KILLING my token use in Opus.
> 
> \- ask Claude to clean up dead or stale code after every implementation regardless if there were hiccups or not as often it'll still find stuff to clean-up
> 
> \- describe bugs first and give it option to look at DEBUG logs ONLY if required else it'll often trawl debug files burning tokens when it had the solution all along
> 
> \- ask it tk validate results by reading SPECIFIC debug files or diag logs when you want to be sure a fix worked as expected and to expose any unintended silent code changes that break other parts of your system (happens every now and then)
> 
> \- often end requests with 'dont change anything. demo understanding and advise. Do NOT break ANY existing logic or functions'
> 
> \- install MCP libraries - they turbocharge your KB, solutions adhere to industry standards and ensures it sticks to specific coding protocols related to the product you are developing. Claude will look here first before going down git rabbitholes
> 
> \- maintain a spreadsheet with your ai prompt, ai response, screenshot,summary, solution, 'explain in simple terms' and files modified. may seem like overkill but I find excellent for tracking and understanding your project over long time frame. the time invested here was well worth it for me.Break each module of your product into seperate worksheet tabs for easy breakdown/ seperation of your application components. you can then track all new issues or feature implementation in one master document
> 
> \- build your code outside of Claude (saves tokens) and only use it to build if you have build Warnings you want to remediate
> 
> > **Londonluton** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa112xq/) · 1 point
> > 
> > > - Use /CLEAR after EVERY succesful implementation or part suxcesfull implementation. you can now reference those context files in new conversation context as a summary placeholder. saved me a heap of tokens. insisting on continuing long comversations until I had a resoltuon was KILLING my token use in Opus
> > 
> > Don't use clear, start a new instance and save the outputted "Claude --resume XYZ" it gives you into the session summary file so you have a way to keep track of the original conversation too
> > 
> > > **ThesisWarrior** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa5rcu5/) · 1 point
> > > 
> > > My understanding is that resume uses more tokens. And that clear and concise context files are often more efficient. Notice i mentioned 'successful' or 'partly successful' implementation. Happy to be corrected though. Session summary is appropriate in some intances but I find that it includes a lot of stuff that you may literally not want to be parsed in a new conversation since not all of it was useful or lead to successful outcome. Horse for courses i guess ;)
> > > 
> > > > **Londonluton** · [2026-03-13](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa5smxz/) · 1 point
> > > > 
> > > > I don't mean to USE the resume, I mean if you make new chats, the old one doesn't get overwritten when you clear it. The "claude resume" command being saved into your session summaries means you can always just find that exact convo again if ever you need to revisit it

> **YoghiThorn** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0ar2n/) · 0 points
> 
> I break down the work into manageable chunks, and in my [CLAUDE.md](http://claude.md/), standards and documentation archive I have the overarching design documents, worklog, canonical data schema and a few other things. The md file tells it to look that stuff up when in doubt, and then ask. Works really. well.
> 
> It helps claude ingest the valuable context without trying to make it live through many /compacts. I've got a repo with what that looks like (with my business stuff stubbed out) if anyone wants to see what the pattern is like.

> **Schtick\_** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0ok8p/) · 0 points
> 
> Research Plan Build repeat.

> **DramaLlamaDad** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0s5kv/) · 0 points
> 
> The more context grows, the worse it performs in every single model. Models with 1 mln context might have a purpose for something but you will always get better results coding if you keep context low. Also, super important to understand the U shaped nature of context awareness, it understands the early stuff and the recent stuff really well but loses track of all that stuff in the middle. This means you really need to understand what is going on in your context at the start.
> 
> Use zero MCP's unless they are really needed and prefer skills. Make sure you're getting your money's worth out of your skills and agents and remove those that aren't earning their keep. Make sure your [claude.md](http://claude.md/) is super focused AND don't keep it in a human-friendly format; instead, tell it to strip out all the human niceties and focus it on just the facts. I keep an "ai-format.md" file around which tells it all the stuff to strip out and to keep the human version in claude\_human.md. I edit the claude\_human.md, then tell it to convert that to claude.md in ai format.
> 
> Next, plan your tasks in bite-sized chunks. If any task is so large that it would require compaction, you have already failed. Use a research phase as a session before big task planning sessions. Have it build a research document on API's, code base, file locations, important code sections, etc, and then do the planning in a new session that you start by having it read the research so it doesn't waste all its context doing research in the planning.
> 
> Remember that CC sessions are designed for an average session but you need to be aware of the actual task and pick the right strategy depending on the task. If you're adding a small bit of functionality onto something or fixing a simple bug, the normal CC planning works fine. If you're doing a bigger feature, you need to consider other strategies, like having it build out a local, phased plan file that is broken up into bite sized phases that include the phase plan, tests for completion, updating documentation, and then pushing it to revision control when done before starting the next session. This will keep you both working in bite-sized chunks and also allow you to complete large projects a piece at a time.
> 
> Opus/GPT Codex are both getting better at this stuff but they still ship with just a general purpose planning system. It is up to you to figure out when you need to do more.

> **crimsonroninx** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0sa3x/) · 0 points
> 
> How the hell are you using so much context? Break your work down into smaller chunks. And always start fresh context beyond 100-120k.
> 
> The only time I've had context issues is when I tried to work on a project that had been ai slop coded and there were 50x 2k LOC files. Thats so inefficient for both humans and LLMs.
> 
> Make sure your files are small. Coding principles are still important eg. SOLID, DRY etc.

> **Keep-Darwin-Going** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0uv4y/) · 0 points
> 
> If you need 1 million context you probably doing it wrong, any work too big to fit can be splitted up using plan and sub agent. I have almost never have to deal with this problem beside sometime Claude decide it is a good ideal to read the whole image into context or something along that line.

> **MolassesLate4676** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0x04a/) · 0 points
> 
> Have people just started using LLM’s?

> · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0723t/) · 0 points
> 
> \[removed\]
> 
> > **ClaudeAI-ModTeam** · [2026-03-12](https://reddit.com/r/ClaudeAI/comments/1rrkv0h/how_are_you_guys_managing_context_in_claude_code/oa0nehi/) · 0 points
> > 
> > We do not allow low content, low relevance advertising here.