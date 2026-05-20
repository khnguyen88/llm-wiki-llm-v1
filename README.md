# LLM Knowledge Base

**Your AI conversations compile themselves into a searchable knowledge base. External sources compile into a wiki.**

This project implements **two parallel systems** based on Karpathy's LLM Knowledge Base pattern. Both use the same core insight: instead of RAG (rediscovering knowledge on every query), the LLM **incrementally builds and maintains a persistent wiki** that compacts knowledge over time.

---

## External Knowledge Base (`004-wiki/`)

Web articles, papers, repos, and datasets compiled by the LLM into a structured wiki. The LLM reads a structured `index.md` to find relevant articles — no vector search needed.

```
Raw sources (articles, papers, repos) -> [large files] -> 003-processed/ (segmented markdown)
                                         -> [small files]  -> 004-wiki/
AI-discovered sources (001b-ai-research/) -> [small files]  -> 004-wiki/
    -> index.md, entities/, concepts/, summaries/, qanda/
        -> Query against index (no RAG needed)
```

| Directory        | Purpose                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------- |
| **001a-raw/**         | Source documents (read-only for LLM)                                                     |
| **001b-ai-research/** | AI-discovered web sources (LLM-writes, immutable once saved)                             |
| **003-processed/**   | Segmented markdown from large raw files (PDFs, long reports) broken into LLM-sized parts |
| **004-wiki/**        | LLM-generated markdown (index, entities, concepts, summaries, qanda, synthesis)          |

## Internal Knowledge Base (`knowledge/`)

Your Claude Code conversations compiled into a searchable knowledge base. Hooks automatically capture sessions, compile them into knowledge articles, and inject context back into future sessions.

```
Conversations -> Hooks -> daily/ -> compile.py -> knowledge/
    -> SessionStart injects index -> cycle repeats
```

| Directory      | Purpose                                               |
| -------------- | ----------------------------------------------------- |
| **daily/**     | Conversation logs (read-only for LLM)                 |
| **knowledge/** | Compiled knowledge (index, concepts, connections, qa) |

---

## Quick Start

Tell your AI coding agent:

> "Read AGENTS.md and schema/WIKI_AGENTS.md. Set up the external knowledge base from sources in 001a-raw/ and 001b-ai-research/. Large files will be segmented into 003-processed/ first. Process the karpathy-llm-wiki.md source first."

The agent will:

1. Read the schema files to understand the wiki structure
2. Process sources from `001a-raw/` into the `004-wiki/` folder
3. Update `004-wiki/index.md` and `004-wiki/log.md`
4. Create entity, concept, and summary pages

---

## Project Structure

```
llm-wiki-llm-v1/
├── 001a-raw/                          # External sources (articles, papers, repos, datasets)
│   ├── articles/
│   ├── papers/
│   ├── repos/
│   ├── datasets/
│   ├── assets/                   # Images and attachments
│   ├── document/                 # Document sources (papers, PDFs, datasets)
│   ├── web/                      # Web sources (articles, repos, tweets)
│   ├── forum-thread/             # Forum discussions
│   └── transcripts/              # Conversation transcripts
├── 001b-ai-research/                  # AI-discovered web sources (immutable once saved)
│   ├── articles/
│   ├── papers/
│   ├── repos/
│   ├── datasets/
│   ├── assets/
│   ├── document/
│   ├── web/
│   ├── forum-thread/
│   └── transcripts/
├── 003-processed/                    # Segmented markdown from large raw files
│   ├── articles/
│   ├── papers/
│   ├── repos/
│   ├── datasets/
│   ├── assets/
│   ├── document/
│   ├── web/
│   ├── forum-thread/
│   └── transcripts/
├── 004-wiki/                         # External knowledge base (LLM-owned)
│   ├── index.md                  #   Master catalog
│   ├── sources-manifest.md       #   Source tracking (001a-raw/001b-ai-research/processed → wiki status)
│   ├── log.md                    #   Operation log
│   ├── synthesis.md              #   Overarching thesis
│   ├── concepts/                 #   Concept pages
│   ├── entities/                 #   Entity pages
│   ├── summaries/                #   Source summaries
│   └── qanda/                    #   Q&A articles
├── daily/                        # Internal conversation logs
├── knowledge/                    # Internal compiled knowledge
│   ├── index.md
│   ├── log.md
│   ├── concepts/
│   ├── connections/
│   └── qa/
├── schema/                       # Configuration
│   ├── WIKI_AGENTS.md            #   External KB schema
│   ├── WIKI_SCHEMA.md            #   External KB conventions
│   └── WIKI_WORKFLOWS.md         #   External KB workflows
├── AGENTS.md                     # Internal KB schema (coleam00/claude-memory-compiler)
├── scripts/                      # CLI tools
│   ├── compile.py                #   Compile daily logs -> knowledge
│   ├── query.py                  #   Ask the knowledge base
│   ├── lint.py                   #   Health checks
│   ├── flush.py                  #   Extract memories (background)
│   ├── config.py                 #   Path constants
│   └── utils.py                  #   Shared helpers
├── hooks/                        # Claude Code hooks
│   ├── session-start.py
│   ├── session-end.py
│   └── pre-compact.py
├── reports/                      # Lint reports
├── tools_scripts/                # Crawl scripts and utilities
│   ├── claude_en_urls.txt
│   ├── crawl_claude_docs.py
│   ├── crawl_openrouter_docs.py
│   ├── crawl4ai/
│   │   └── basic.py
│   └── rename_add_index.py
├── .claude/                      # Claude Code configuration
│   ├── settings.json
│   └── agents/                   # Project-specific agents
│       ├── wiki-maintainer.md
│       ├── document-processor.md
│       ├── knowledge-compiler.md
│       ├── wiki-linter.md
│       ├── wiki-query.md
│       ├── wiki-repair.md
│       ├── sync-check.md
│       ├── context-loader.md
│       ├── web-search.md
│       └── ai-research.md
└── README.md                     # This file
```

---

## Key Commands

### External Knowledge Base

```bash
# Process a source from 001a-raw/ (large files are segmented into 003-processed/ first)
# (Done by LLM when you say "Process this source")

# Query the wiki
uv run python scripts/query.py "What are the key concepts?"

# Lint the wiki for issues
uv run python scripts/lint.py
```

### Internal Knowledge Base

```bash
uv run python scripts/compile.py              # compile new daily logs
uv run python scripts/query.py "question"     # ask the knowledge base
uv run python scripts/query.py "question" --file-back # ask + save answer back
uv run python scripts/lint.py                 # run health checks
```

---

## Why No RAG?

Karpathy's insight: at personal scale (50-500 articles), the LLM reading a structured `index.md` outperforms vector similarity. The LLM understands what you're really asking; cosine similarity just finds similar words. RAG becomes necessary at ~2,000+ articles when the index exceeds the context window.

---

## The Core Idea

**Most people use RAG**: Upload files, LLM retrieves chunks at query time, generates answer. The LLM rediscovers knowledge from scratch on every question.

**Your approach**: The LLM incrementally builds a persistent wiki. When you add a new source, the LLM reads it, extracts key information, and integrates it into the existing wiki. The knowledge is compiled once and kept current.

**The key difference**: The wiki is a **persistent, compounding artifact**. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

---

## Architecture Comparison

| Aspect      | External KB                               | Internal KB                  |
| ----------- | ----------------------------------------- | ---------------------------- |
| Raw data    | Articles, papers, repos, 001b-ai-research/     | Claude Code conversations    |
| Staging     | `003-processed/` (segmented from large files) | N/A                          |
| Compiled to | `004-wiki/`                                   | `knowledge/`                 |
| Schema      | `schema/WIKI_*.md`                        | `AGENTS.md`                  |
| Trigger     | Manual "Process this source"              | Automatic hooks (SessionEnd) |
| Main use    | Research, learning                        | Coding patterns, decisions   |

---

## Sources & Integration

This project fuses four open-source projects, each contributing a distinct layer.

### Karpathy's LLM Wiki Pattern (Base)

- [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) / [Original tweet](https://x.com/karpathy/status/2039805659525644595)

**What it added:** The foundational insight and folder structure. No RAG — the LLM reads a structured index to find relevant articles. The `001a-raw/` → `004-wiki/` pipeline, wiki page types (entities, concepts, summaries, qanda), `index.md` as the retrieval hub, and `log.md` for audit trail all come from this pattern. The wiki-maintainer agent role and the principle that the LLM owns `004-wiki/` while humans own `001a-raw/` are also Karpathy's.

**Why we integrated it:** At personal scale (50-500 articles), index-guided retrieval outperforms vector similarity because the LLM understands what you're asking, not just what words look similar. This is the core thesis the entire project is built on.

### Cole Medin's claude-memory-compiler (Internal KB)

- [github.com/coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) / [YouTube walkthrough](https://www.youtube.com/watch?v=7huCP6RkcY4)

**What it added:** The `daily/` → `knowledge/` pipeline and all supporting infrastructure. This includes: Claude Code hooks (`session-start.py`, `session-end.py`, `pre-compact.py`) that automatically capture conversations; `flush.py` for background memory extraction; `compile.py` for compiling daily logs into knowledge articles; `query.py` and `lint.py` as CLI tools; `AGENTS.md` as the internal KB schema; the `knowledge-compiler` agent; and the concept that conversations are "source code" and `knowledge/` is the "executable."

**Why we integrated it:** Karpathy's pattern handles external sources only. Cole's system adds the missing half — automatically capturing and compiling your own AI conversations into a searchable internal KB, then injecting that context back into future sessions.

### Atomic Memory's llm-wiki-compiler (Schema & Quality)

- [github.com/atomicmemory/llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler)

**What it added:** Enhanced frontmatter with `summary`, `created`/`updated` timestamps, `confidence` (0-1), `provenance` (extracted|merged|inferred|ambiguous), `contradictedBy`, and `orphaned` fields. Claim-level citations (`^[001a-raw/articles/source.md]`, `^[001a-raw/articles/source.md:42-58]`). Expanded the linter from 8 to 12 checks (added: missing summary, duplicate concept, malformed citation, broken citation). The `wiki-linter`, `sync-check`, and `context-loader` agents. The `sources-manifest.md` tracking file and the `document-processor` agent for segmenting large files.

**Why we integrated it:** Karpathy's pattern has no quality gates. Atomic Memory adds provenance tracking (where a claim came from, how confident it is, whether it's been contradicted) and a linter that catches stale, orphaned, or contradictory content — essential when the wiki compounds over time.

### Josh Pocock's karpathy-obsidian-vault (Visualization)

- [github.com/joshpocock/karpathy-obsidian-vault](https://github.com/joshpocock/karpathy-obsidian-vault)

**What it added:** The `001b-ai-research/` directory — a separate namespace for AI-discovered web sources, distinct from user-curated `001a-raw/` files. This separation makes it clear what the human added vs. what the LLM found autonomously. Also added Obsidian-specific conventions — wikilink format `[[path/to/article]]`, Dataview frontmatter queries, Marp slide generation, graph view integration, and backlink navigation. The directory naming and frontmatter structure are designed to work natively inside Obsidian as a vault.

**Why we integrated it:** Distinguishing human-curated sources from AI-discovered ones prevents trust confusion — you always know which claims came from your own research vs. LLM web searches. Obsidian turns the compiled knowledge into something you can explore visually via graph view, backlinks, and Dataview.

---

## Obsidian Integration

Both knowledge bases work natively in Obsidian:

- **Graph View**: Visualize connections
- **Dataview**: Query frontmatter for dynamic tables
- **Marp**: Generate slide decks
- **Backlinks**: Automatically maintained via `[[wikilinks]]`

---

## Setup Guide

### GitHub Repository

**Why:** Create a remote repository to back up your wiki vault in case of data loss.

1. Create a new GitHub repo — include a **README.md** and **.gitignore**
2. Clone the GitHub repo locally
3. Open the project folder in VS Code

### Karpathy LLM Wiki / Vault Template

**Why:** This is the basis of the project folder. It contains markdown files that an LLM harness uses to build the project infrastructure. A template ensures consistency throughout the project.

1. In the project folder, create a directory called `init_source`
2. Download these files into the directory:
    - [Karpathy's Wiki LLM markdown](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
    - [Karpathy's Original Tweet on Wiki LLM](https://x.com/i/flow/login?redirect_after_login=%2Fkarpathy%2Fthread%2F20398056595256445950)

### Cole Medin Extension (claude-memory-compiler)

**Why:** Expands Karpathy's Wiki LLM to extrapolate, log, and summarize daily work activities. Includes tools and hooks for linting the wiki and maintaining link integrity.

1. Download files from [Cole Medin's Claude Memory Compiler Repo](https://github.com/coleam00/claude-memory-compiler)
2. Tell your AI coding agent:

    > "Clone https://github.com/coleam00/claude-memory-compiler into this project. Set up the Claude Code hooks so my conversations automatically get captured into daily logs, compiled into a knowledge base, and injected back into future sessions. Read the AGENTS.md for the full technical reference on how everything works."

3. YouTube walkthrough: <https://www.youtube.com/watch?v=7huCP6RkcY4>

### Atomic Memory Extension (llm-wiki-compiler)

**Why:** Enhances linting and review with structured page metadata (confidence, provenance, contradiction tracking), claim-level citations, and 4 additional lint checks. No CLI or MCP integration — pure schema and agent enhancements.

1. Download ideas from [Atomic Memory's LLM Wiki Compiler Repo](https://github.com/atomicmemory/llm-wiki-compiler)
2. Integrated features (no code installation required):

    > Enhanced frontmatter with `summary`, `created`/`updated` ISO 8601 timestamps, `confidence` (0-1), `provenance` (extracted\|merged\|inferred\|ambiguous), `contradictedBy` (page slugs), and `orphaned` (boolean). Added claim-level citations (`^[001a-raw/articles/source.md]`, `^[001a-raw/articles/source.md:42-58]`). Expanded linter from 8 to 12 checks.

### Josh Pocock Extension (karpathy-obsidian-vault)

**Why:** Provides the `001b-ai-research/` directory convention for separating human-curated sources from AI-discovered ones, and Obsidian vault integration for visual exploration.

1. Download files from [Josh Pocock's karpathy-obsidian-vault Repo](https://github.com/joshpocock/karpathy-obsidian-vault)

### Obsidian

**Why:** Graphically maps all sources together and provides infrastructure to read documents.

1. Download and install [Obsidian](https://obsidian.md/)
2. Open Obsidian and select **Open folder as vault**
3. Choose the project folder — Obsidian will create an `.obsidian` folder to track all documents

---

## Tools

### ccstatusline

Real-time session context window monitoring in the Claude Code status bar. Helps manage hallucination risk and output integrity by keeping context utilization visible.

Example output: `Model: glm-5.1:cloud | Ctx: 103.0k | Ctx Used: 52.0% | Cost: $55.31 | Session: 2hr 22m | ⎇ main | 𖠰 main`

**Setup:**

1. Add to your global Claude Code settings (`~/.claude/settings.json`):

```json
"statusLine": {
  "type": "command",
  "command": "npx -y ccstatusline@latest",
  "padding": 0
}
```

2. No separate install needed — `npx` downloads it on the fly each run.

3. Configure which widgets appear in the status line. Run the interactive widget editor:

```bash
npx -y ccstatusline@latest
# Then press 'a' to add widgets, 'd' to delete, 'Enter' to reorder
```

4. To match the example output above, add these widgets in order:

| Widget             | What it shows                             | Config key                             |
| ------------------ | ----------------------------------------- | -------------------------------------- |
| **Model**          | Current model name (e.g. `glm-5.1:cloud`) | `r` toggles raw value mode             |
| **Context Length** | Context window size (e.g. `103.0k`)       | Raw value mode for compact display     |
| **Context %**      | Context used percentage (e.g. `52.0%`)    | Press `u` to toggle used/remaining     |
| **Session Cost**   | Session cost in USD (e.g. `$55.31`)       | Requires CC 1.0.85+                    |
| **Session Clock**  | Elapsed session time (e.g. `2hr 22m`)     | Raw value mode for compact display     |
| **Git Branch**     | Current branch (e.g. `main`)              | Press `h` to hide when not in git repo |
| **Git Worktree**   | Active worktree name                      | Shows when in a worktree               |

5. Widget editor keybinds:

| Key     | Action                                            |
| ------- | ------------------------------------------------- |
| `a`     | Add widget                                        |
| `i`     | Insert widget before selected                     |
| `d`     | Delete selected widget                            |
| `Enter` | Enter/exit move mode (reorder)                    |
| `r`     | Toggle raw value mode (hides labels)              |
| `m`     | Cycle merge mode (off → merge → merge no padding) |

6. Settings are saved to `~/.config/ccstatusline/settings.json`. You can also edit this file directly or specify a custom path with `--config /path/to/settings.json`.

### Superpowers

Structured brainstorming, planning, and execution skills for Claude Code. Enforces discipline: brainstorm before building, write plans before coding, verify before claiming done. Skills include brainstorming, writing-plans, executing-plans, test-driven-development, systematic-debugging, verification-before-completion, and more.

**Setup:**

1. Enable in your global Claude Code settings (`~/.claude/settings.json`):

```json
"enabledPlugins": {
  "superpowers@claude-plugins-official": true
}
```

2. Skills are invoked automatically by Claude Code when relevant, or manually via `/brainstorming`, `/writing-plans`, `/executing-plans`, etc.

---

## Optional Tools

### Ollama

Run LLM models locally for background tasks, testing, or cost savings. Ollama serves local models through an OpenAI-compatible API that Claude Code Router can route to.

**Why:** Offload background tasks (linting, summarization, simple queries) to a local model instead of paying per-token for a cloud model. Also useful for air-gapped or offline work.

**Setup:**

1. Download and install [Ollama](https://ollama.com/)
2. Pull a model:

```bash
ollama pull qwen2.5-coder
```

3. Launch a model:

```bash
ollama run qwen2.5-coder
```

4. Ollama exposes an OpenAI-compatible endpoint at `http://localhost:11434/v1/chat/completions` — configure it as a provider in Claude Code Router (see below).

### Claude Code Router (ccr)

Route Claude Code requests to any model — local (Ollama), subscription (OpenRouter, Gemini, DeepSeek), or direct API (Anthropic). Run non-Claude models from within Claude Code with model-aware routing.

**Why:** Use cheaper models for background tasks, reasoning models for plan mode, long-context models for large files, and your primary model for everything else — all from a single `ccr code` command.

**Setup:**

1. Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code/quickstart) and [Claude Code Router](https://github.com/musistudio/claude-code-router):

```bash
npm install -g @anthropic-ai/claude-code
npm install -g @musistudio/claude-code-router
```

2. Create `~/.claude-code-router/config.json`. Example with local + cloud providers:

```json
{
	"Providers": [
		{
			"name": "ollama",
			"api_base_url": "http://localhost:11434/v1/chat/completions",
			"api_key": "ollama",
			"models": ["qwen2.5-coder:latest"]
		},
		{
			"name": "openrouter",
			"api_base_url": "https://openrouter.ai/api/v1/chat/completions",
			"api_key": "sk-or-xxx",
			"models": [
				"anthropic/claude-sonnet-4",
				"google/gemini-2.5-pro-preview"
			],
			"transformer": { "use": ["openrouter"] }
		},
		{
			"name": "deepseek",
			"api_base_url": "https://api.deepseek.com/chat/completions",
			"api_key": "sk-xxx",
			"models": ["deepseek-chat", "deepseek-reasoner"],
			"transformer": { "use": ["deepseek"] }
		}
	],
	"Router": {
		"default": "ollama,qwen2.5-coder:latest",
		"background": "ollama,qwen2.5-coder:latest",
		"think": "deepseek,deepseek-reasoner",
		"longContext": "openrouter,google/gemini-2.5-pro-preview",
		"longContextThreshold": 60000
	}
}
```

3. Start Claude Code through the router:

```bash
ccr code
```

4. Switch models on the fly inside Claude Code:

```
/model openrouter,anthropic/claude-sonnet-4
```

5. Manage providers and models interactively:

```bash
ccr model          # interactive model selector
ccr ui             # web-based config editor
ccr restart        # restart after config changes
```

6. Set environment variables so `claude` command also routes through ccr:

```bash
eval "$(ccr activate)"
```

For full documentation, see [github.com/musistudio/claude-code-router](https://github.com/musistudio/claude-code-router).

### OpenRouter

Unified API gateway to 200+ models from Anthropic, Google, Meta, Mistral, and more. Pay per token across all providers through a single API key.

**Why:** Access any model without managing separate API keys and billing for each provider. Works directly with Claude Code Router as a provider.

**Setup:**

1. Create an account at [openrouter.ai](https://openrouter.ai/)
2. Generate an API key from your [OpenRouter keys page](https://openrouter.ai/settings/keys)
3. Add as a provider in `~/.claude-code-router/config.json` (see Claude Code Router config above)
4. OpenRouter models support online search by appending `:online` to the model name:

```json
"models": ["anthropic/claude-sonnet-4:online"]
```

### Crawl4AI

Web crawling service for the LLM, exposed via MCP and a REST API. The preferred method is the Docker version, which can be shared across multiple projects.

**Setup (Docker):**

1. Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

2. Create a `.crawl4ai.env` file in your project root:

```env
# .crawl4ai.env
OPENAI_API_KEY=sk-or-your-openrouter-key
OPENAI_BASE_URL=https://openrouter.ai/api/v1

# Default model (use any OpenRouter model string)
LLM_PROVIDER=openai/gpt-4o
LLM_TEMPERATURE=0.7
```

> ⚠️ Never commit `.crawl4ai.env` to version control. Add it to `.gitignore`.

3. Run the container with the env file attached:

**macOS / Linux (bash):**

```bash
docker run -d \
  -p 11235:11235 \
  --name crawl4ai \
  --env-file .crawl4ai.env \
  --shm-size=1g \
  unclecode/crawl4ai:latest
```

**Windows (PowerShell):**

```powershell
docker run -d `
  -p 11235:11235 `
  --name crawl4ai `
  --env-file .crawl4ai.env `
  --shm-size=1g `
  unclecode/crawl4ai:latest
```

4. Connect Claude Code via MCP. Run this inside your project directory:

```bash
claude mcp add crawl4ai --url http://localhost:11235/mcp
```

Verify it's connected:

```bash
claude mcp list
```

You should see `crawl4ai` listed. Claude Code will now be able to call crawl4ai tools directly during conversations.

> ⚠️ Always start the Docker container before opening a Claude Code session. MCP connections are established at startup.

5. Use Crawl4AI via prompt

All of these trigger the `crawl` tool:

```
Crawl https://example.com
Scrape https://example.com
Fetch all content from https://example.com
Pull the page at https://example.com
```

All of these trigger a deep/recursive crawl:

```
Deep crawl https://docs.example.com
Crawl the entire site at https://docs.example.com
Index all pages under https://docs.example.com
Crawl https://docs.example.com up to 3 levels deep
```

**Stop & Start:**

```bash
docker stop crawl4ai       # Stop the container (keeps it, just pauses it)
docker start crawl4ai      # Start it again
docker restart crawl4ai    # Restart (stop + start in one command)
```

### Vane (Web Search API)

AI-synthesized web search engine (formerly Perplexica) that runs locally via Docker. Combines a SearxNG metasearch backend with an LLM chat model for reasoning and an embedding model for semantic retrieval — producing narrative responses with inline references instead of a raw list of URLs.

**Why:** Deeper synthesis than built-in WebSearch. In testing, Vane caught architectural details (Engram, mHC, OPD for DeepSeek V4) and correct pricing that built-in WebSearch missed entirely.

**Setup (Docker):**

1. Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

2. Run the Vane container (bundled with SearxNG):

**macOS / Linux (bash):**

```bash
docker run -d \
  -p 3000:3000 \
  -v vane-data:/home/vane/data \
  --name vane \
  itzcrazykns1337/vane:latest
```

**Windows (PowerShell):**

```powershell
docker run -d `
  -p 3000:3000 `
  -v vane-data:/home/vane/data `
  --name vane `
  itzcrazykns1337/vane:latest
```

3. Open `http://localhost:3000` in your browser and complete the setup wizard — configure your LLM providers (Ollama, OpenRouter, etc.) and search settings.

4. The project's Vane tools are pre-configured in `.claude/tools/` and `.claude/scripts/`:

| Tool                 | Definition                              | Script                                  |
| -------------------- | --------------------------------------- | --------------------------------------- |
| `vane_get_providers` | `.claude/tools/vane_get_providers.json` | `.claude/scripts/vane_get_providers.py` |
| `vane_web_search`    | `.claude/tools/vane_web_search.json`    | `.claude/scripts/vane_web_search.py`    |

5. Verify Vane is reachable:

```bash
uv run python .claude/scripts/vane_get_providers.py
```

> ⚠️ Always start the Docker container before opening a Claude Code session.

**Stop & Start:**

```bash
docker stop vane       # Stop the container
docker start vane      # Start it again
docker restart vane    # Restart (stop + start in one command)
```

**Usage:**

Two project agents use Vane — one ephemeral, one persistent:

| Agent           | Command                     | Behavior                                      | Output                      |
| --------------- | --------------------------- | --------------------------------------------- | --------------------------- |
| **web-search**  | "Search the web for X"      | Ephemeral — returns results, never saves      | stdout only (uses built-in) |
| **vane-search** | "Vane Search the web for X" | Ephemeral — returns results, never saves      | stdout only (uses vane)     |
| **ai-research** | "Research X and save it"    | Persistent — deep search + crawl4ai follow-up | saves to `001b-ai-research/web/` |

Both agents enforce the same citation convention: every factual claim must include an inline citation `[N]` referencing a numbered source, and all sources must be included verbatim (no filtering or truncation).

If Vane is unavailable, the web-search agent falls back to built-in WebSearch (with a notice that results may be shallower).

For full documentation, see [github.com/ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane).

---

### Document Processing Pipeline

Converts documents (PDF, DOCX, PPTX) to markdown via docling-serve, with OCR remediation powered by deepseek-ocr. Used by the `document-converter` → `ocr-remediator` → `markdown-chunker` pipeline. The pipeline produces segmented markdown in `003-processed/` for wiki ingestion.

**Why:** PDFs and binary documents can't be ingested directly into the wiki. This pipeline converts them to markdown, fixes OCR gaps in formulas/tables/diagrams, and segments large documents into LLM-sized chunks — all before wiki ingestion touches them.

**Setup:**

1. Prerequisites:
    - [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)
    - [Ollama](#ollama) (installed and running)
    - Python 3.11+ with `pipx` (for arrase/OCR CLI)

2. Create a `.docling.env` file in your project root:

```env
# Document Processing Pipeline — Required Environment Variables

# docling-serve Docker container URL
DOCLING_SERVE_URL=http://localhost:5001

# Ollama URL for arrase/deepseek-ocr
OLLAMA_URL=http://localhost:11434

# OpenRouter API key (for vision model OCR fallback)
# Get yours at: https://openrouter.ai/keys
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# ── Optional: Override thresholds ──────────────────────────────────────
# PDF_SPLIT_PAGE_SIZE=25
# DOCLING_CONFIDENCE_THRESHOLD=0.8
# ARRASE_CONFIDENCE_FLOOR=0.7
# LLM_OCR_CONFIDENCE_FLOOR=0.5
# CHUNK_MAX_WORDS=3000
# CHUNK_TARGET_WORDS=1500
# MAX_AUTO_ATTEMPTS=3
# WEBSEARCH_CONFIDENCE_FLOOR=0.6
```

> ⚠️ Never commit `.docling.env` to version control. It's already listed in `.gitignore`.

3. Pull and run the docling-serve Docker container:

**macOS / Linux (bash):**

```bash
docker run -d \
  -p 5001:5001 \
  --name docling-serve \
  quay.io/docling-project/docling-serve
```

**Windows (PowerShell):**

```powershell
docker run -d `
  -p 5001:5001 `
  --name docling-serve `
  quay.io/docling-project/docling-serve
```

> ⚠️ First run downloads ML models — the API won't respond until downloads complete (can take several minutes). Subsequent starts use cached models and initialize quickly.

4. Install the arrase/OCR CLI:

```bash
pipx install git+https://github.com/arrase/OCR.git
```

5. Pull the deepseek-ocr model in Ollama:

```bash
ollama pull deepseek-ocr:latest
```

**Verify:**

```bash
docker ps | grep docling-serve     # Container running on port 5001
ocr --version                       # arrase/OCR CLI installed
ollama list | grep deepseek-ocr     # deepseek-ocr model pulled
```

**Stop & Start:**

```bash
docker stop docling-serve       # Stop the container
docker start docling-serve      # Start it again
docker restart docling-serve    # Restart (stop + start in one command)
```

**Usage:**

Tell your AI coding agent:

```
Convert this document to markdown        → invokes document-converter agent
Fix OCR issues in 002-raw-preprocessed           → invokes ocr-remediator agent
Chunk this markdown into chapters        → invokes markdown-chunker agent
Process this PDF                         → invokes document-processor (full pipeline)
```

### Obsidian Clipper

Browser extension (Firefox) for extracting single-page articles or threads directly into your Obsidian vault.

**Why:** Quickly capture web content in one click without running a full crawl — ideal for one-off sources that don't warrant a Crawl4AI session.

**Setup:**

1. Install [Obsidian Clipper](https://obsidian.md/clipper) for Firefox
2. Point it to your vault folder
3. Click the Obsidian icon in your browser toolbar to clip any page as Markdown

---

## Files You Should Read

| File                         | Purpose                                                 |
| ---------------------------- | ------------------------------------------------------- |
| **AGENTS.md**                | Internal KB schema — how the LLM compiles conversations |
| **schema/WIKI_AGENTS.md**    | External KB schema — how the LLM maintains the wiki     |
| **schema/WIKI_SCHEMA.md**    | File formats and conventions for the external wiki      |
| **schema/WIKI_WORKFLOWS.md** | Ingest, Query, Lint, and Research workflows             |
| **.claude/agents/**          | Project-specific Claude Code agents                     |
| **CLAUDE.md**                | Project instructions for Claude Code sessions           |
