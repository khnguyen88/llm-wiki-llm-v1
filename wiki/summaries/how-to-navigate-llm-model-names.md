---
title: "How to Navigate LLM Model Names"
summary: "Red Hat developer article by Trevor Royer that demystifies LLM naming conventions including branded names, versions, model sizes, quantization, distillation, and Mixture of Experts"
type: summary
sources:
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - naming-conventions
  - red-hat
  - model-selection
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
---

# How to Navigate LLM Model Names

## Summary

This article by Trevor Royer (Red Hat Developer, April 2025) provides a practical guide to understanding LLM naming conventions. It breaks down the components commonly found in model names -- branded names, version numbers, model size indicators, purpose/alignment tags, quantization levels, distillation markers, and architectural hints like MoE. The article emphasizes that understanding these conventions helps users select the right model for their hardware and use case. ^[raw/articles/How to navigate LLM model names.md]

## Branded Names and Versions

Model families carry branded names that identify architectural lineage and vendor. Some are acronyms -- Llama stands for "Large Language Model Meta AI" -- while others are marketing-driven, like IBM's Granite evoking rock-solid reliability. ^[raw/articles/How to navigate LLM model names.md]

Version numbers follow simplified semantic versioning (major.minor, omitting patch). Major version changes indicate significant architectural or training-data shifts that may break compatibility with serving tools like vLLM. Minor versions correspond to incremental improvements or data refreshes. ^[raw/articles/How to navigate LLM model names.md]

## Model Size and Hardware Implications

Parameters (or weights) are numerical values learned during training. The parameter count directly impacts storage size and GPU vRAM requirements.

| Parameter Count | Example Model | Hardware Requirement |
|---|---|---|
| 8B | granite-3.2-8b-instruct | Fits on A10 GPU (24 GB vRAM) with limited context |
| 405B | llama-3.1-405b-instruct | 900+ GB vRAM, commonly run on 16x H100 (80 GB each) |

^[raw/articles/How to navigate LLM model names.md]

## Model Purpose Categories

| Purpose | Name Signal | Description |
|---|---|---|
| Base | `base` | Generic pretrained starting point for fine-tuning; rarely used directly |
| Instruct | `instruct` | Fine-tuned to follow instructions; default for conversational use. Older models may use "chat" |
| Vision | `vision` | Multi-modal: accepts text + images, outputs text. "vision-instruct" combines both capabilities |
| Code | `code` | Optimized for coding tasks; largely superseded by general instruct models |
| Embedding | `embedding` | Converts text to numerical vectors for vector databases and RAG |
| Guard | `guard`, `guardian` | Safety filtering for detecting unsafe content in chat workflows |
| Reasoning | `reasoning` | Chain-of-thought processing before responding, popularized by DeepSeek R1 |

^[raw/articles/How to navigate LLM model names.md]

## Quantization

Quantization converts model weights from high-precision types (32-bit or 16-bit float) to lower-precision types (8-bit or 4-bit), dramatically reducing model size at the cost of potential accuracy loss. Concrete example: Llama 405B drops from 900+ GB at fp16 to ~450 GB at fp8. Some models use Neural Magic's "w4a16" notation (4-bit weights, 16-bit activations). ^[raw/articles/How to navigate LLM model names.md]

## Distillation

Distillation creates smaller "student" models from larger "teacher" models, reducing training time while preserving accuracy. Model names indicate the teacher -- e.g., `deepseek-r1-distill-llama-70b` was distilled using Llama 70B as the teacher. DeepSeek popularized this technique. ^[raw/articles/How to navigate LLM model names.md]

## Mixture of Experts

MoE models activate only a fraction of parameters per token via a routing layer. Two naming conventions exist:

| Model | Notation | Meaning |
|---|---|---|
| Mixtral-8x7B-v0.1 | NxP | 8 experts, 7B active per token; 46B total (shared params) |
| Llama-4-Scout-17B-16E | PxE | 16 experts, 17B active per token; 109B total (shared params) |

^[raw/articles/How to navigate LLM model names.md]

## Key Quotes

> "One of the first challenges of working with large language models (LLMs) is understanding their names." ^[raw/articles/How to navigate LLM model names.md:12]

> "Instruct models are one of the most common model types you will encounter, and if you are looking for a conversational model this is most likely what you want." ^[raw/articles/How to navigate LLM model names.md:53-54]

> "Quantization is the process of converting a model weights from high precision data types such as 32-bit or 16-bit floating point numbers to lower precision types such as 8-bit floating point or integer values." ^[raw/articles/How to navigate LLM model names.md:84-85]
