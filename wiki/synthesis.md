---
title: Synthesis
type: synthesis
date: 2026-04-23
sources:
  - raw/articles/karpathy-github-llm-wiki.md
  - raw/articles/karpathy-tweet-llm-wiki.md
  - raw/articles/farzapedia.md
  - raw/repos/claude-code-router/
  - raw/document/working_ps_script_to_run_headless_claude_code.txt
  - raw/repos/claude-memory-compiler/
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/LLM Naming Explained (What do the options mean_).md
  - raw/articles/Naming Conventions of LLM Models.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
---

# Synthesis

## Key Themes

- **Persistent, compounding knowledge**: The LLM Wiki pattern replaces RAG's rediscovery-per-query with a wiki that grows richer with every source and question. Cross-references, contradictions, and synthesis accumulate permanently.
- **File over app, BYOAI**: Knowledge lives in universal formats (markdown, images) under your control, not locked in an AI provider. Any LLM can plug in. This is both a practical and philosophical stance.
- **LLM as maintainer, human as curator**: The tedious bookkeeping (cross-references, consistency, summaries) is the LLM's job. The human directs sources, asks questions, and judges what matters.
- **Index-guided retrieval at scale**: At ~100 sources, a structured index.md outperforms vector similarity. At ~2,000+ articles, add hybrid RAG as a pre-filter.
- **Model routing as enabler**: Tools like [[claude-code-router]] make the BYOAI principle concrete — any LLM can plug in because a proxy handles format translation and routing. This is the infrastructure layer that makes "file over app, BYOAI" viable in practice.

## Key Findings

- A single source touches 10-15 wiki pages — entities, concepts, summaries, cross-references
- Karpathy's own research wiki reached ~100 articles / ~400K words and works well without RAG
- The approach traces back to Vannevar Bush's Memex (1945): personal, curated knowledge with associative trails
- Answers can be filed back into the wiki, creating a compounding loop where exploration enriches the KB
- The three operations (ingest, query, lint) form a complete cycle for building and maintaining knowledge
- Claude Code Router demonstrates the BYOAI pattern in practice: a proxy that unifies multiple LLM providers behind one interface, with scenario-based routing, format transformers, and per-project config. This is the tooling layer that makes "use any LLM" actually work.
- Headless execution bridges LLM tools into automation workflows — the PowerShell script shows a complete pattern: check router status, conditionally start it, run a task with `--dangerously-skip-permissions`, and clean up. This is how [[model_routing]] moves from interactive use to CI/CD and batch processing.
- [[claude-memory-compiler]] is the reference implementation of this entire architecture — it operationalizes the LLM Wiki pattern with hooks for automatic capture, a flush-compile-query-lint pipeline, and the same index-guided retrieval. This project's scripts and hooks are adapted from its originals.
- **LLM naming conventions encode deployment-critical metadata:** A model name is structured metadata, not an arbitrary label. The pattern `[Org/]Family-Version-Size[-Active]-Training[-Format][-Quantization]` communicates parameter count, alignment stage, quantization method, and hardware requirements at a glance.
- **Quantization is the dominant deployment decision:** Q4_K_M is the mainstream default (~92% quality, ~75% size reduction). GPU-native formats (AWQ, GPTQ, EXL2) outperform GGUF on NVIDIA but lack CPU fallback. The rule of thumb: prefer a larger model at lower quantization over a smaller model at higher quantization.
- **MoE is everywhere in 2026:** Mixture of Experts has become the default architecture for frontier open-weight models. The naming convention encodes total vs active parameters (e.g., 35B-A3B), which determines RAM vs compute costs. Knowledge capacity scales with total parameters; inference speed scales with active parameters.
- **Paid vs open-source naming reflects different design goals:** Paid models (GPT-4o, Gemini 1.5 Pro) are product artifacts with branding tiers. Open-source models are engineering artifacts with explicit technical metadata. Understanding this difference prevents costly deployment mistakes like selecting a base model for a chatbot use case.
- **The distillation economy is reshaping local inference:** DeepSeek-R1 proved that 80%+ of frontier reasoning can be captured in 7-32B distilled models. Community quantizers (bartowski, unsloth) and fine-tuning labs (Nous Research, Eric Hartford) have become critical infrastructure nodes in the open-weight ecosystem.

## Open Questions

- At what scale does index-guided retrieval break down? Karpathy suggests ~2,000 articles
- How well does finetuning on a wiki work as an alternative to context-window retrieval?
- What product could make this workflow accessible beyond the "agent-proficient" user?
- How do multi-user wikis work? Can team wikis be maintained by LLMs with human review?
- At what parameter scale does quantization quality degradation become unacceptable for production use cases?
- Will MoE architectures eventually dominate dense models entirely, or will both coexist?

## How This File Works

This file represents the "thesis" of your knowledge base. The LLM maintains it by:
1. Reading new source summaries
2. Identifying how they connect to existing knowledge
3. Updating themes and findings
4. Noting any contradictions or gaps

You rarely need to edit this directly - let the LLM maintain it as you add sources.

---

*Last updated: 2026-04-23*