---
title: "KV Cache: The Invisible Trick Behind Every LLM"
summary: Adam Rosler's video explaining how KV cache works as the key inference optimization in transformers, covering tokens, embeddings, dot products, attention mechanics, memoization history, GPU memory constraints, and prompt caching
type: summary
sources:
  - raw/transcripts/adam-rosler-2026-05-12.md
tags:
  - kv-cache
  - attention
  - inference
  - memoization
  - memory-wall
  - prompt-caching
  - transformers
  - gpu-memory
created: "2026-05-12T12:00:00Z"
updated: "2026-05-12T12:00:00Z"
---

# KV Cache: The Invisible Trick Behind Every LLM

## Summary

Adam Rosler explains why the second call to the same LLM prompt costs 20 times less than the first, tracing the answer from the fundamentals of attention mechanics through to the concept of the KV cache and the memory wall that governs modern AI economics. The video connects Donald Michie's 1968 concept of memoization to the practice of caching key and value vectors in GPU memory, and shows how Anthropic's prompt caching makes this reuse explicit across API calls.^[raw/transcripts/adam-rosler-2026-05-12.md]

## From Sequential to Parallel (and Back Again)

Before transformers, language models processed sentences one word at a time, making training slow. The 2017 "Attention Is All You Need" paper enabled every word to attend to every other word in parallel, dramatically accelerating training. But inference -- generating responses -- remains sequential: each new token depends on all prior tokens. Transformers lose their training-time parallelism at inference time.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Tokens, Embeddings, and Dot Products

Three foundational concepts underlie the KV cache:

| Concept | Description |
|---------|-------------|
| **Token** | A chunk of text (sometimes a whole word, sometimes a fragment); the model slices prompts into tokens before any processing |
| **Embedding** | A vector of ~4,000 numbers per token, drawn from a learned lookup table stored in the model file |
| **Dot product** | A single number measuring alignment between two vectors; related concepts yield positive values, orthogonal concepts yield zero, opposite concepts yield negatives |

During pre-training, the model nudges embeddings so related concepts point in similar directions (e.g., "cat" and "kitten" align, while "cat" and "yacht" do not). This means semantic relatedness reduces to a single arithmetic operation.^[raw/transcripts/adam-rosler-2026-05-12.md]

## The Attention Mechanism: Keys, Values, and Queries

For each token, the model computes two new vectors from its embedding:

| Vector | Role | How computed |
|--------|------|-------------|
| **Key (K)** | What the token advertises if another token looks at it | Embedding multiplied by a learned key matrix |
| **Value (V)** | What the token actually contributes if selected | Embedding multiplied by a learned value matrix |
| **Query (Q)** | What the current token is searching for | Embedding multiplied by a learned query matrix |

Splitting each token's role into "advertising" (key) and "contributing" (value) lets the model learn different patterns of advertisement and contribution. To predict the next token, the query dots against every prior key to produce attention scores, which weight the corresponding values.^[raw/transcripts/adam-rosler-2026-05-12.md]

## The Computational Cost Problem

Multiplying a 4,000-dimensional embedding by a 4,000x4,000 matrix is 16 million multiplications per token. Across 40 stacked layers, each computing its own attention, that is roughly 600 million multiplications per token for keys alone, and the same for values -- about 2 billion math operations per token just for setup. The naive transformer recomputes K and V for the entire prefix on every generation step. By 1,000 tokens deep, the model has recomputed the same key for the word "the" roughly 1,000 times.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Memoization and the KV Cache

Computer scientists recognized this waste pattern in 1968. Donald Michie coined "memoization" (from "memorandum" -- "to be remembered") in his paper "Memo Functions and Machine Learning," proposing that functions should cache their results rather than recompute them. Applied to attention, this yields the KV cache: a stack of saved keys and values from prior tokens kept in GPU memory. After each token, its K and V are appended. For the next token, only the new pair is computed; attention runs against the full cached stack. Caching K and V (not the raw embedding) is critical because the expensive operation is the matrix multiplication that transforms embeddings into K and V. Without this optimization, generation would cost roughly 1,000 times more compute.^[raw/transcripts/adam-rosler-2026-05-12.md]

## The Memory Wall

The KV cache lives in GPU memory, and every generated token adds another entry. For a typical 70-billion-parameter model, each token consumes about half a megabyte of cache. Generating 100,000 tokens means carrying 50 GB of cache, and each concurrent user has their own. In 1995, William Wulf and Sally McKee identified the "memory wall": compute performance doubles regularly, but memory bandwidth does not. This gap means inference providers are selling GPU memory bandwidth, not compute.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Prompt Caching and Prefix Ordering

Anthropic introduced prompt caching in 2024, making the KV cache reusable across API calls. Sending the same prefix as a recent request lets the provider keep the cached KV state in GPU memory and run attention against it without recomputing. The first call pays to build the cache; subsequent calls rent it. This is why prompt ordering matters: stable content (system prompt, tools, retrieved documents) should go at the bottom, and the user's question at the end. Any change in the prefix invalidates every cache entry from that point onward. Tail-loading the dynamic content preserves the cache for free.^[raw/transcripts/adam-rosler-2026-05-12.md]

## Key Quotes

> "Same prompt, same model. The first call costs a dollar, the second cost 5 cents, 20 times cheaper."^[raw/transcripts/adam-rosler-2026-05-12.md:1]

> "Inference, which is what happens when the model is generating responses for you, is still sequential. Each new word depends on the words before it."^[raw/transcripts/adam-rosler-2026-05-12.md:1]

> "Computer scientists noticed this kind of waste back in 1968. Donald Michie called it memorization. Save the answer. Do not compute it twice."^[raw/transcripts/adam-rosler-2026-05-12.md:3]

> "Your inference provider is not selling you compute. They are selling you GPU memory bandwidth."^[raw/transcripts/adam-rosler-2026-05-12.md:4]

> "Long context is not slow because the model thinks harder. It is slow because the cache is bigger."^[raw/transcripts/adam-rosler-2026-05-12.md:5]

> "Reason order matters. Put stable stuff at the bottom. Put the user's actual question at the end."^[raw/transcripts/adam-rosler-2026-05-12.md:5]

## Related

- [[004-wiki/concepts/kv_cache]]
- [[004-wiki/concepts/attention_mechanism]]
- [[004-wiki/concepts/prompt_caching]]
- [[004-wiki/concepts/memory_wall]]
- [[004-wiki/concepts/token_embedding]]
- [[004-wiki/entities/adam_rosler]]
- [[004-wiki/entities/donald_michie]]