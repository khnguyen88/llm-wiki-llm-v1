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

## [2026-04-22] ingest | Claude Memory Compiler
- Source: raw/repos/claude-memory-compiler/ (README.md, AGENTS.md, scripts/flush.py, pyproject.toml)
- Created summary: summaries/claude-memory-compiler.md
- Created concept: concepts/memory_flush.md
- Created entity: entities/coleam00.md
- Updated index.md, sources-manifest.md, cross-references on llm_wiki, compound_knowledge, andrej_karpathy

## [2026-04-23] ingest | How to Navigate LLM Model Names
- Source: raw/articles/How to navigate LLM model names.md
- Created summary: summaries/how-to-navigate-llm-model-names.md
- Created concepts: concepts/llm_naming_conventions.md, concepts/model_quantization.md, concepts/parameter_counts.md, concepts/training_variants.md, concepts/model_distillation.md, concepts/mixture_of_experts.md
- Created entity: entities/trevor_royer.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-23] ingest | LLM Model Names Decoded
- Source: raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
- Created summary: summaries/llm-model-names-decoded.md
- Updated concepts: llm_naming_conventions, model_quantization, parameter_counts, training_variants, model_distillation, mixture_of_experts
- Created entities: entities/dylan_boudro.md, entities/bartowski.md, entities/unsloth.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-23] ingest | LLM Model Naming Conventions
- Source: raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
- Created summary: summaries/llm-model-naming-conventions.md
- Updated concepts: llm_naming_conventions, model_quantization, parameter_counts, training_variants
- Created entity: entities/abstract_algorithms.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-23] ingest | LLM Naming Explained
- Source: raw/articles/LLM Naming Explained (What do the options mean_).md
- Created summary: summaries/llm-naming-explained.md
- Updated concepts: llm_naming_conventions, model_quantization, parameter_counts
- Created entity: entities/martin_kollie.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-23] ingest | Naming Conventions of LLM Models
- Source: raw/articles/Naming Conventions of LLM Models.md
- Created summary: summaries/naming-conventions-of-llm-models.md
- Updated concepts: llm_naming_conventions, parameter_counts, training_variants
- Created entity: entities/sudarshan.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-23] ingest | Understanding Naming Conventions Of LLM Files
- Source: raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
- Created summary: summaries/understanding-naming-conventions-of-llm-files.md
- Updated concepts: llm_naming_conventions, model_quantization, parameter_counts, model_formats, training_variants
- Created entity: entities/templespark.md
- Updated index.md, sources-manifest.md, synthesis.md

## [2026-04-23] query | Qwen3.6-35b-a3b naming explained
- Question: explain how to interpret qwen3.6-35b-a3b — what does that mean?
- Read: concepts/llm_naming_conventions, concepts/parameter_counts, concepts/mixture_of_experts, concepts/model_quantization, concepts/training_variants, summaries/llm-model-names-decoded
- Created: qanda/qwen3-6-35b-a3b-naming.md
- Updated: wiki/index.md, wiki/log.md

---

*Append new entries at the bottom*