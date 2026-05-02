---
title: "LLM Wiki"
summary: "A personalization pattern where an LLM incrementally builds a persistent, compounding wiki of knowledge, putting the user in full control of their data"
type: concept
sources:
  - raw/articles/farzapedia.md
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
tags:
  - llm-wiki
  - personalization
  - knowledge-management
  - architecture
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T16:30:00Z"
confidence: 0.9
provenance: merged
---

# LLM Wiki

A pattern for AI personalization where the LLM incrementally builds and maintains a persistent wiki of structured knowledge, rather than relying on implicit learning. The wiki is explicit, inspectable, and controlled by the user. ^[raw/articles/farzapedia.md:4-6]

## Key Points

- The LLM Wiki pattern contrasts with the "status quo" approach where an AI "allegedly gets better the more you use it" through implicit learning ^[raw/articles/farzapedia.md:4]
- Memory artifacts are explicit and navigable — the user can see exactly what the AI does and does not know, and can inspect and manage the artifact even if the LLM does the direct text writing ^[raw/articles/farzapedia.md:6]
- Data remains under the user's control on their local computer, not locked inside an AI provider's system ^[raw/articles/farzapedia.md:7]
- The approach puts the user in full control: data is theirs, in universal formats, explicit and inspectable ^[raw/articles/farzapedia.md:11]
- Managing the wiki requires handling file directories, but agents make this simpler and can help significantly ^[raw/articles/farzapedia.md:13]
- Three architecture layers: raw sources (immutable, source of truth), the wiki (LLM-owned markdown), and the schema (configuration for LLM behavior) ^[raw/articles/karpathy-github-llm-wiki.md:29-35]
- Three core operations: ingest (integrate sources, touching 10-15 wiki pages), query (synthesize answers, file good answers back as new pages), lint (health-check for contradictions, orphans, gaps) ^[raw/articles/karpathy-github-llm-wiki.md:39-43]
- Navigation uses index.md (content catalog) and log.md (chronological record), avoiding embedding-based RAG at moderate scale (~100 sources) ^[raw/articles/karpathy-github-llm-wiki.md:47-51]
- The wiki works because LLMs eliminate the bookkeeping burden that causes humans to abandon knowledge bases ^[raw/articles/karpathy-github-llm-wiki.md:68-70]
- The idea is related to Vannevar Bush's Memex (1945) — the LLM solves the maintenance problem Bush could not ^[raw/articles/karpathy-github-llm-wiki.md:72]
- Applicable to diverse contexts: personal tracking, research, book reading, business/team wikis, competitive analysis, and more ^[raw/articles/karpathy-github-llm-wiki.md:19-25]
- The wiki is a git repository of markdown files, providing version history, branching, and collaboration for free ^[raw/articles/karpathy-github-llm-wiki.md:64]
- At ~100 articles and ~400K words, RAG is unnecessary — the LLM auto-maintains index files and brief summaries for navigation ^[raw/articles/karpathy-tweet-llm-wiki.md:13]
- Query outputs are filed back into the wiki, so explorations and queries always compound in the knowledge base ^[raw/articles/karpathy-tweet-llm-wiki.md:16]
- LLM health checks (linting) find inconsistencies, impute missing data, discover connections for new articles, and improve overall data integrity ^[raw/articles/karpathy-tweet-llm-wiki.md:19]
- Custom tools (e.g., a search engine) can be handed off to the LLM via CLI for larger queries ^[raw/articles/karpathy-tweet-llm-wiki.md:22]
- As the wiki grows, synthetic data generation and finetuning could embed knowledge in model weights rather than context windows ^[raw/articles/karpathy-tweet-llm-wiki.md:25]

## Details

The LLM Wiki pattern addresses personalization through four interconnected properties. **Explicit** means the knowledge artifact is viewable and manageable — not hidden in a black-box model. **Yours** means the data stays on the user's machine, extractable and portable. **File over app** means the data lives in universal formats like markdown and images, making it interoperable with any tool. **BYOAI** means any AI model can be plugged into the information, including finetuning an open source model on the wiki so it "knows" the user in its weights. ^[raw/articles/farzapedia.md:4-9]

Karpathy acknowledges this is not the simplest approach — it requires managing file directories — but argues that agents make it significantly easier. He further suggests that "agent proficiency" is a core skill of the 21st century, given that agents speak English and handle all the computer tasks. ^[raw/articles/farzapedia.md:13]

The architecture has three layers. **Raw sources** are the curated, immutable collection of source documents — the source of truth that the LLM reads but never modifies. **The wiki** is a directory of LLM-generated markdown files (summaries, entity pages, concept pages, comparisons, an overview, a synthesis) that the LLM owns entirely. **The schema** is a configuration document (e.g. CLAUDE.md) that tells the LLM how the wiki is structured and what workflows to follow, making the LLM a disciplined wiki maintainer rather than a generic chatbot. ^[raw/articles/karpathy-github-llm-wiki.md:29-35]

Karpathy's tweet describes a six-step practical workflow. **Data ingest**: source documents go into raw/, the LLM incrementally compiles a wiki with summaries, backlinks, and concept categorization. **IDE**: Obsidian serves as the viewing frontend; the LLM writes and maintains all wiki data. **Q&A**: at moderate scale (~100 articles, ~400K words), the LLM answers complex questions without RAG by relying on auto-maintained index files and summaries. **Output**: answers are rendered as markdown, slides, or images and filed back into the wiki so knowledge compounds. **Linting**: health checks find inconsistencies, impute missing data, and suggest new articles. **Extra tools**: custom CLIs (e.g., a search engine) are handed off to the LLM for larger queries. ^[raw/articles/karpathy-tweet-llm-wiki.md:7-22]

Use cases include personal tracking (goals, health, self-improvement), deep research (papers, articles, evolving thesis), book reading (character pages, themes, plot threads), business/team wikis (Slack threads, meeting transcripts, project documents), competitive analysis, due diligence, trip planning, course notes, and hobby deep-dives. The common thread is accumulating knowledge over time and wanting it organized rather than scattered. ^[raw/articles/karpathy-github-llm-wiki.md:19-25]

## Related

- [[concepts/file_over_app]]
- [[concepts/byoai]]
- [[concepts/rag]]
- [[concepts/memex]]
- [[entities/obsidian]]
- [[entities/qmd]]