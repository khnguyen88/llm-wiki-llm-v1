---
title: "Memory Wall"
summary: The growing gap between processor speed and memory access speed, coined by Wulf and McKee in 1995, predicting that memory bandwidth rather than compute would become the binding constraint on system performance
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - memory-wall
  - computer-architecture
  - gpu-memory
  - inference-cost
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Memory Wall

The growing gap between processor speed and memory access speed, where compute performance improves exponentially while memory bandwidth improves only incrementally. The term was coined by William A. Wulf and Sally A. McKee in their 1995 paper "Hitting the Memory Wall: Implications of the Obvious." In the context of LLM inference, the memory wall explains why GPU memory bandwidth -- not compute -- is the binding constraint on cost and throughput.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Origins

Wulf and McKee observed that processor performance was improving at 75-80% per year while DRAM speed improved at only ~7% per year. Using the average memory access time formula `t_avg = p x t_c + (1 - p) x t_m`, they showed that even with a perfect cache (only compulsory misses), the gap between cache and DRAM access times grows exponentially. Under conservative assumptions (1% compulsory miss rate, DRAM 4x slower than cache in 1994, 7%/year DRAM improvement, 80%/year processor improvement), average cycles per memory access would reach 1.52 by 2000, 8.25 by 2005, and 98.8 by 2010.

In their 2004 follow-up "Reflections on the Memory Wall," McKee noted that many applications do hit the memory wall: commercial transaction processing sees 65% node idle time, and scientific computing sees 95% node idle time. They concluded that all known mitigation techniques provide "one-time boosts" that delay but do not change the fundamentals.

## Implications for LLM Inference

For LLM serving, the memory wall means that [[004-wiki/concepts/kv_cache|KV cache]] size and GPU memory bandwidth dominate cost, not FLOPS. A 70B-parameter model at 100K context carries roughly 50 GB of KV cache per user. The inference provider is selling GPU memory bandwidth, not compute. This is why:

- Long context is expensive not because the model "thinks harder" but because the cache is bigger
- [[004-wiki/concepts/prompt_caching|prompt caching]] can reduce costs by 90% by avoiding redundant memory transfers
- Optimizations like [[004-wiki/concepts/grouped_query_attention|GQA]] and PagedAttention target memory, not compute

## Related

- [[004-wiki/concepts/kv_cache]]
- [[004-wiki/concepts/prompt_caching]]
- [[004-wiki/entities/wulf_and_mckee]]
- [[004-wiki/summaries/adam-rosler-kv-cache-2026-05-12]]