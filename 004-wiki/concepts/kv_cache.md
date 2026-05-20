---
title: "KV Cache"
summary: A stack of saved key and value vectors from prior tokens kept in GPU memory during transformer inference, eliminating redundant recomputation and reducing generation cost by roughly 1000x compared to naive attention
type: concept
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - kv-cache
  - inference
  - transformers
  - gpu-memory
  - memoization
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
confidence: 0.95
provenance: merged
---

# KV Cache

A stack of saved key and value vectors from prior tokens kept in GPU memory during transformer inference. After each token is generated, its K and V vectors are appended to the cache. For the next token, only the new pair is computed; attention runs against the full cached stack. The KV cache is the single most important optimization for transformer inference, reducing per-token cost by roughly 1,000x compared to naive recomputation.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Origins

The KV cache applies the principle of [[004-wiki/concepts/memoization|memoization]] -- coined by [[004-wiki/entities/donald_michie|Donald Michie]] in 1968 -- to the attention mechanism. The core idea: if the same input produces the same output through the same matrices, save the result rather than recompute it. Michie proposed that functions should have both a "rule part" (computational procedure) and a "rote part" (lookup table), with the machine deciding which to use. The KV cache is the rote part for attention.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Why Cache K and V (Not Embeddings)?

Embeddings are cheap to compute -- they are simple lookups from a stored table. The expensive operation is the matrix multiplication that transforms each embedding into a key vector and a value vector: roughly 16 million multiplications per token per matrix, across 40 layers, yielding ~2 billion operations per token just for setup. Caching the intermediate result (K and V) rather than the input (embedding) is what eliminates the redundant work.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Memory Cost

For a typical 70-billion-parameter model, each token consumes about 0.5 MB of KV cache. At 100,000 tokens, that is 50 GB of cache per user. Each concurrent user has their own independent cache. This makes [[004-wiki/concepts/memory_wall|GPU memory bandwidth]] the binding constraint on inference cost, not compute.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Optimization Techniques

Several techniques reduce KV cache memory pressure:

| Technique | Approach | KV Cache Reduction |
|-----------|----------|-------------------|
| [[004-wiki/concepts/grouped_query_attention|GQA]] | Shares K/V heads across groups of query heads | 8x for Llama 3 70B |
| [[004-wiki/concepts/multi_query_attention|MQA]] | Single K/V head shared across all query heads | 64x for same model |
| [[004-wiki/concepts/paged_attention|PagedAttention]] | OS-style virtual memory paging for KV cache blocks | Near-zero fragmentation |
| Quantization | Store K/V in INT8 or FP8 instead of FP16 | 2x reduction |
| Sliding window | Cache only recent tokens | Bounded memory |

### Grouped Query Attention (GQA)

Introduced by Ainslie et al. (2023), GQA interpolates between Multi-Head Attention (MHA) and Multi-Query Attention (MQA) by sharing K/V heads across groups of query heads. Standard MHA gives each query head its own K/V pair; MQA collapses all K/V heads to one; GQA uses G groups (1 < G < H). GQA-8 achieves quality close to MHA with speed close to MQA. Llama 3 70B uses GQA with 64 query heads and 8 KV heads, reducing its KV cache from 20 GB to 2.5 GB at 8K context (FP16). Existing MHA checkpoints can be converted to GQA by mean-pooling K/V heads within groups, requiring only ~5% of original pre-training compute for fine-tuning.

### Multi-Query Attention (MQA)

Introduced by Shazeer (2019), MQA uses a single K/V head shared across all query heads. This maximizes inference speed but can degrade quality and training stability, especially in larger models. It is used in PaLM 540B and Falcon 40B.

### PagedAttention

Developed for vLLM (Kwon et al., SOSP 2023), PagedAttention applies OS-style virtual memory paging to KV cache management. Instead of allocating contiguous memory for each request's KV cache (which causes 13-57% internal fragmentation and 8-38% external fragmentation), it divides the cache into fixed-size blocks that can be placed non-contiguously in physical memory, using block tables for indirection. This achieves near-zero fragmentation (96.3% useful KV storage vs 20-38% in prior systems) and enables copy-on-write sharing across parallel samples and shared prefixes. The approach achieves 2-4x higher throughput than contiguous allocation despite ~20-26% higher per-kernel attention latency, because far more requests can be batched simultaneously.

## Prompt Caching

[[004-wiki/concepts/prompt_caching|Prompt caching]] extends the KV cache across API calls. Anthropic introduced this in 2024: if a subsequent request shares the same prefix as a recent one, the provider keeps the cached KV state in GPU memory and runs attention against it without recomputing. The first call pays to build the cache; subsequent calls rent it at 90% lower cost. This requires placing stable content (system prompts, tools, documents) before dynamic content (user questions), because any change in the prefix invalidates all cache entries from that point onward.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Open Questions

- What is the optimal number of GQA groups for models below 7B parameters?
- How will MLA (Multi-Head Latent Attention from DeepSeek-V2) compare to GQA at scale?

## Related

- [[004-wiki/concepts/attention_mechanism]]
- [[004-wiki/concepts/memory_wall]]
- [[004-wiki/concepts/memoization]]
- [[004-wiki/concepts/prompt_caching]]
- [[004-wiki/concepts/token_embedding]]
- [[004-wiki/entities/donald_michie]]
- [[004-wiki/summaries/adam-rosler-kv-cache-2026-05-12]]