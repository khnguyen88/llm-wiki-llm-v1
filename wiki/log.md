# Wiki Log

A chronological record of operations on the external knowledge base.

## [2026-04-22] System initialized
- Created directory structure: wiki/, wiki/concepts/, wiki/entities/, wiki/summaries/, wiki/qanda/
- Initialized wiki/index.md and wiki/log.md
- External knowledge base ready for first source ingestion

## [2026-04-22] schema created
- Created schema/WIKI_AGENTS.md - LLM as wiki maintainer
- Created schema/WIKI_SCHEMA.md - file formats and conventions
- Created schema/WIKI_WORKFLOWS.md - Ingest, Query, Lint workflows

## [2026-04-22] ingest | Karpathy LLM Wiki Gist
- Source: raw/articles/karpathy-github-llm-wiki.md
- Created summary: summaries/llm-wiki-pattern.md
- Created concepts: concepts/llm_wiki.md, concepts/index_guided_retrieval.md, concepts/compound_knowledge.md, concepts/memex.md
- Created entity: entities/andrej_karpathy.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-22] ingest | Karpathy Tweet on LLM Knowledge Bases
- Source: raw/articles/karpathy-tweet-llm-wiki.md
- Created summary: summaries/karpathy-tweet-llm-wiki.md
- Updated concepts: llm_wiki (added source), index_guided_retrieval (added source), compound_knowledge (added source)
- Updated entity: andrej_karpathy (added source)
- Updated sources-manifest.md

## [2026-04-22] ingest | Farzapedia Commentary
- Source: raw/articles/farzapedia.md
- Created summary: summaries/farzapedia-commentary.md
- Created concepts: concepts/file_over_app.md, concepts/byoai.md
- Updated sources-manifest.md, synthesis.md

## [2026-04-22] ingest | Claude Code Router
- Source: raw/repos/claude-code-router/ (README.md, docs/, examples/)
- Created summary: summaries/claude-code-router.md
- Created concepts: concepts/model_routing.md, concepts/request_transformers.md, concepts/claude_code.md
- Created entity: entities/claude_code_router.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-22] ingest | Headless Claude Code PowerShell Script
- Source: raw/document/working_ps_script_to_run_headless_claude_code.txt
- Created summary: summaries/headless-claude-code-ps.md
- Created concept: concepts/headless_llm_execution.md
- Updated index.md, sources-manifest.md, cross-references on claude-code-router and model_routing

---

*Append new entries at the bottom*