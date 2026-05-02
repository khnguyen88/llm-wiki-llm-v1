---
title: "How to Navigate LLM Model Names"
summary: "Red Hat guide breaking down LLM model name components: branded names, versioning, parameter size, model purposes (base, instruct, vision, code, embedding, guard, reasoning), quantization, distillation, and mixture of experts"
type: summary
sources:
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - naming-conventions
  - model-selection
  - red-hat
created: "2026-05-02T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
---

# How to Navigate LLM Model Names

## Summary

This Red Hat article demystifies LLM model naming by breaking it into six components: branded names, version numbers, parameter size, model purpose, quantization, and architecture type. It provides concrete vRAM examples and explains how each naming element maps to practical deployment decisions. ^[raw/articles/How to navigate LLM model names.md]

## Branded Names

Model families carry branded names that identify architectural lineage and vendor — e.g., IBM's Granite (evoking reliability), Meta's Llama (derived from **L** arge **La** nguage **M** odel **M** eta **A** I). Some names are marketing-driven; others encode technical acronyms. ^[raw/articles/How to navigate LLM model names.md]

## Versioning

Models use simplified semantic versioning (major.minor, typically omitting patch). Major version changes indicate architectural or training-data shifts that may break compatibility with serving tools like vLLM. Minor versions correspond to incremental improvements or data refreshes. ^[raw/articles/How to navigate LLM model names.md]

## Model Size

Parameter count (e.g., 8B, 278M) directly determines storage size and vRAM requirements. Concrete examples: granite-3.2-8b-instruct fits on a single A10 GPU (24 GB vRAM) with limited context; Llama-3.1-405b-instruct requires 900+ GB vRAM across sixteen H100s. ^[raw/articles/How to navigate LLM model names.md]

## Model Purposes

LLMs are designed for different tasks, and the purpose is often encoded in the model name:

| Purpose | Name Signal | Description |
|---------|-----------|-------------|
| Base | `base` | Generic pretrained starting point for fine-tuning; rarely used directly |
| Instruct | `instruct` | Fine-tuned to follow instructions; the default for conversational use. Older models may use "chat" instead |
| Vision | `vision` | Multi-modal: accepts text + images, outputs text. "vision-instruct" variants combine both |
| Code | `code` | Optimized for coding tasks; largely superseded by general instruct models that include code capability |
| Embedding | `embedding` | Converts text to numerical vectors for storage and retrieval in vector databases; often paired with RAG |
| Guard | `guard`, `guardian` | Identifies unsafe content; used as input/output filters in chat workflows |
| Reasoning | `reasoning` | Uses chain-of-thought processing internally before responding (e.g., DeepSeek R1) |

^[raw/articles/How to navigate LLM model names.md]

## Quantization

Quantization converts weights from high-precision (32-bit or 16-bit float) to lower-precision types (8-bit float or integer), dramatically reducing model size and vRAM at a potential cost to accuracy. Example: Llama 405B drops from 900+ GB at fp16 to ~450 GB at fp8. Neural Magic uses notation like "w4a16" (4-bit weights, 16-bit activations). ^[raw/articles/How to navigate LLM model names.md]

## Distillation

Distillation creates smaller "student" models from larger "teacher" models, reducing training time while preserving accuracy. Model names indicate the teacher — e.g., deepseek-r1-distill-llama-70b was distilled using Llama 70B as the teacher. DeepSeek popularized this technique. ^[raw/articles/How to navigate LLM model names.md]

## Mixture of Experts

MoE models activate only a fraction of parameters per token via a routing layer, achieving large-model knowledge at small-model compute cost. Two naming conventions exist:

| Model | Notation | Meaning |
|-------|----------|---------|
| Mixtral-8x7B-v0.1 | `NxP` | 8 experts, 7B active params per token; total 46B (not 56B due to shared params) |
| Llama-4-Scout-17B-16E | `PxN` | 16 experts, 17B active params; total 109B (not 272B due to shared params) |

^[raw/articles/How to navigate LLM model names.md]

## Key Quotes

> "One of the first challenges of working with large language models (LLMs) is understanding their names." ^[raw/articles/How to navigate LLM model names.md:12]

> "Instruct models are one of the most common model types you will encounter, and if you are looking for a conversational model this is most likely what you want." ^[raw/articles/How to navigate LLM model names.md:53-54]

> "Unlike traditional LLMs that simply attempt to predict the next word in the sequence, reasoning models try to work through a chain-of-thought processing, internally asking and refining questions before delivering a final response." ^[raw/articles/How to navigate LLM model names.md:78]

> "Quantization is the process of converting a model weights from high precision data types such as 32-bit or 16-bit floating point numbers to lower precision types such as 8-bit floating point or integer values." ^[raw/articles/How to navigate LLM model names.md:84-85]

## Related

- [[concepts/model_naming]]
- [[concepts/quantization]]
- [[concepts/distillation]]
- [[concepts/mixture_of_experts]]
- [[concepts/instruction_tuning]]
- [[concepts/vision_models]]
- [[concepts/guard_models]]
- [[concepts/embedding_models]]