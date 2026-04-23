---
title: "How to Navigate LLM Model Names"
type: summary
date: 2026-04-23
sources:
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - naming-conventions
  - quantization
  - model-types
---

# How to Navigate LLM Model Names

**Author:** [[entities/trevor_royer|Trevor Royer]]  
**Source:** [Red Hat Developers](https://developers.redhat.com/articles/2025/04/03/how-navigate-llm-model-names)  
**Published:** 2025-04-03

## Summary

A practical guide to decoding LLM model names by breaking down branded names, version numbers, parameter counts, model purposes, quantization codes, distillation labels, and Mixture of Experts (MoE) notation.

## Key Components of Model Names

- **Branded names**: Identify the model family and creator (e.g., IBM Granite, Meta Llama). Llama stands for **L**arge **La**nguage **M**odel **M**eta **A**I.
- **Versions**: Simplified semantic versioning (major.minor). Major versions indicate architecture or training changes; minor versions indicate incremental improvements.
- **Model size**: Parameter counts in billions (B) or millions (M). Directly impacts file size and VRAM requirements. For example, granite-3.2-8b-instruct fits on a 24 GB A10 GPU, while llama-3.1-405b-instruct requires 900+ GB VRAM.
- **Model purposes**: Common suffixes include `base` (pretrained foundation), `instruct` (follows prompts), `chat` (multi-turn conversation, falling out of favor), `vision` (multimodal), `code` (coding optimized), `embedding` (vector generation), `guard` (safety filtering), and `reasoning` (chain-of-thought).

## Quantization

Quantization converts weights from high-precision formats (FP32, FP16) to lower precision (FP8, INT8, INT4), dramatically reducing model size at a potential accuracy cost. Common labels include `fp8`, `int8`, and codes like `w4a16` (4-bit weights, 16-bit activations).

## Distillation

A technique where a smaller "student" model is trained from a larger "teacher" model. Example: `deepseek-r1-distill-llama-70b` indicates the model was distilled using Llama 70B as the teacher.

## Mixture of Experts (MoE)

Only a fraction of parameters are active per token. Two common naming conventions:
- `Mixtral-8x7B`: 8 experts, 7B active parameters per token, 46B total parameters.
- `Llama-4-Scout-17B-16E`: 16 experts, 17B active parameters, 109B total parameters (shared parameters reduce the total from 16*17=272).

## Key Claims

- Understanding naming conventions helps select the right model for specific use cases and hardware constraints.
- New naming conventions will continue to emerge as the field evolves.

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/model_quantization]]
- [[concepts/parameter_counts]]
- [[concepts/training_variants]]
- [[concepts/model_distillation]]
- [[concepts/mixture_of_experts]]
