# LLM Knowledge Base

**Your AI conversations compile themselves into a searchable knowledge base. External sources compile into a wiki.**

This project implements **two parallel systems** based on Karpathy's LLM Knowledge Base pattern:

1. **External Knowledge Base (wiki/)**: Web articles, papers, repos, and datasets compiled by the LLM into a structured wiki
2. **Internal Knowledge Base (knowledge/)**: Your Claude Code conversations compiled into a searchable knowledge base

Both use the same core insight: instead of RAG (rediscovering knowledge on every query), the LLM **incrementally builds and maintains a persistent wiki** that compacts knowledge over time.

---

## Quick Start

Tell your AI coding agent:

> "Read AGENTS.md and schema/WIKI_AGENTS.md. Set up the external knowledge base from sources in raw/. Large files will be segmented into processed/ first. Process the karpathy-llm-wiki.md source first."

The agent will:

1. Read the schema files to understand the wiki structure
2. Process sources from `raw/` into the `wiki/` folder
3. Update `wiki/index.md` and `wiki/log.md`
4. Create entity, concept, and summary pages

---

## How It Works

### External Knowledge Base (Karpathy's Pattern)

```
Raw sources (articles, papers, repos) -> [large files] -> processed/ (segmented markdown)
                                         -> [small files]  -> wiki/
    -> index.md, entities/, concepts/, summaries/, qanda/
        -> Query against index (no RAG needed)
```

- **raw/**: Source documents (read-only for LLM)
- **processed/**: Segmented markdown from large raw files (PDFs, long reports) broken into LLM-sized parts
- **wiki/**: LLM-generated markdown (index, entities, concepts, summaries, qanda, synthesis)
- **schema/WIKI_AGENTS.md**: Defines LLM as wiki maintainer

### Internal Knowledge Base (claude-memory-compiler)

```
Conversations -> Hooks -> daily/ -> compile.py -> knowledge/
    -> SessionStart injects index -> cycle repeats
```

- **daily/**: Conversation logs (read-only for LLM)
- **knowledge/**: Compiled knowledge (index, concepts, connections, qa)
- **AGENTS.md**: Defines LLM as compiler

---

## Project Structure

```
llm-wiki-llm-v1/
├── raw/                          # External sources (articles, papers, repos, datasets)
│   ├── articles/
│   ├── papers/
│   ├── repos/
│   ├── datasets/
│   ├── assets/                   # Images and attachments
│   ├── document/                 # Document sources (papers, PDFs, datasets)
│   ├── web/                      # Web sources (articles, repos, tweets)
│   ├── forum-thread/             # Forum discussions
│   └── transcripts/              # Conversation transcripts
├── processed/                    # Segmented markdown from large raw files
│   ├── articles/
│   ├── papers/
│   ├── repos/
│   ├── datasets/
│   ├── assets/
│   ├── document/                 # Segmented document sources
│   ├── web/                      # Segmented web sources
│   ├── forum-thread/             # Segmented forum discussions
│   └── transcripts/              # Segmented conversation transcripts
├── wiki/                         # External knowledge base (LLM-owned)
│   ├── index.md                  #   Master catalog
│   ├── sources-manifest.md       #   Source tracking (raw/processed → wiki status)
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
├── .claude/                      # Claude Code configuration
│   ├── settings.json
│   └── agents/                   # Project-specific agents
│       ├── wiki-maintainer.md
│       ├── document-processor.md
│       ├── knowledge-compiler.md
│       ├── wiki-linter.md
│       ├── wiki-query.md
│       └── sync-check.md
└── README.md                     # This file
```

---

## Key Commands

### External Knowledge Base

```bash
# Process a source from raw/ (large files are segmented into processed/ first)
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

## Obsidian Integration

Both knowledge bases work natively in Obsidian:

- **Graph View**: Visualize connections
- **Dataview**: Query frontmatter for dynamic tables
- **Marp**: Generate slide decks
- **Backlinks**: Automatically maintained via `[[wikilinks]]`

---

## Files You Should Read

| File                         | Purpose                                                 |
| ---------------------------- | ------------------------------------------------------- |
| **AGENTS.md**                | Internal KB schema — how the LLM compiles conversations |
| **schema/WIKI_AGENTS.md**    | External KB schema — how the LLM maintains the wiki     |
| **schema/WIKI_SCHEMA.md**    | File formats and conventions for the external wiki      |
| **schema/WIKI_WORKFLOWS.md** | Ingest, Query, and Lint workflows                       |
| **.claude/agents/**          | Project-specific Claude Code agents                     |
| **CLAUDE.md**                | Project instructions for Claude Code sessions           |

---

## Architecture Comparison

| Aspect      | External KB                               | Internal KB                  |
| ----------- | ----------------------------------------- | ---------------------------- |
| Raw data    | Articles, papers, repos                   | Claude Code conversations    |
| Staging     | `processed/` (segmented from large files) | N/A                          |
| Compiled to | `wiki/`                                   | `knowledge/`                 |
| Schema      | `schema/WIKI_*.md`                        | `AGENTS.md`                  |
| Trigger     | Manual "Process this source"              | Automatic hooks (SessionEnd) |
| Main use    | Research, learning                        | Coding patterns, decisions   |

---

## The Core Idea

**Most people use RAG**: Upload files, LLM retrieves chunks at query time, generates answer. The LLM rediscoveres knowledge from scratch on every question.

**Your approach**: The LLM incrementally builds a persistent wiki. When you add a new source, the LLM reads it, extracts key information, and integrates it into the existing wiki. The knowledge is compiled once and kept current.

**The key difference**: The wiki is a **persistent, compounding artifact**. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

## How to get started

### Github Repo

#### Why

- We want to create a remote repository of our wiki LLM vault in the event that we lose it.

#### Steps

- Create a new Github repo
    - Include a **README.md** and **.gitignore**

- Clone github repo to locally (create local git repository)

- Open project folder in VS Code

### Karpathy LLM Wiki / Vault Template

-

#### Why

- This is the basis of our Karpathy LLM Project Folder. This folder contains markdown files that an LLM harness can use to build up the project infrastructure

- We use a template to ensure that it is consistent throughout the project

### Karpathy Base

- In the project folder create a directory called "init_source"

- Download these files into the directory:
    - [Karpathy's Wiki LLM markdown](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
    - [Karpathy's Original Tweet on Wiki LLM](https://x.com/i/flow/login?redirect_after_login=%2Fkarpathy%2Fthread%2F20398056595256445950)
    -

- Youtube video - https://www.youtube.com/watch?v=7huCP6RkcY4

### Karpathy Extension (Cole Medin Extension)

#### Why

- Expands Karpathy's Wiki LLM to extrapolate, log, and summarize daily work activites

#### Steps

- Download files from [Cole Medin's Karpathy LLM Repo](https://github.com/coleam00/claude-memory-compiler)

* Tell your AI coding agent / harness:

    > "Clone https://github.com/coleam00/claude-memory-compiler into this project. Set up the Claude Code hooks so my conversations automatically get captured into daily logs, compiled into a knowledge base, and injected back into future sessions. Read the AGENTS.md for the full technical reference on how everything works."

- Youtube video - https://www.youtube.com/watch?v=7huCP6RkcY4

### Obsidian

#### Why

- Graphically maps all of your source together and provide infrastructure to read documents

#### Steps

- Download and install the latest Obisdian program onto your computer
    - https://obsidian.md/

- Go to Obisidian Manager

- Open the project folder as vault

    > "Open folder as vault"

- This will create an .obsidian folder that will track all of your documents

### Tools to Install

#### Crawl4AI

---

#### Steps (Easy Docker Version)

- **Preferred method**
- This docker instance can be spun and used across multiple project

- Download and install Install docker desktop for Windows
    - [Download Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)

#### Steps (Local Project)

```powershell
# Force install into the active venv's Python directly
python -m pip install "crawl4ai[all]"

# Then run setup
python -m pip install playwright
python -m playwright install chromium
```
