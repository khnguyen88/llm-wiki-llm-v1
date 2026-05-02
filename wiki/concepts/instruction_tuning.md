---
title: "Instruction Tuning"
summary: "Fine-tuning method that trains LLMs on instruction-response pairs, producing models that reliably follow user prompts"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
tags:
  - llm
  - training
  - fine-tuning
  - alignment
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Instruction Tuning

Instruction tuning (suffix: `-instruct`, `-IT`, or `-it`) is a fine-tuning method that trains LLMs on instruction-response pairs via supervised fine-tuning. It produces models that reliably follow user prompts: "Summarize this," "Write a function that..." — the standard variant for most use cases. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Points

- Three main training variants: Base (pretrained, text completion only), Instruct/IT (fine-tuned on instruction-response pairs, follows prompts reliably), Chat (further optimized for multi-turn conversation via RLHF or DPO) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- For general use, always pick the instruct/IT variant; base models are for researchers and fine-tuners ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Additional training suffixes indicate specialized fine-tuning: DPO (alignment via Direct Preference Optimization), RLHF (Reinforcement Learning from Human Feedback), reasoning/thinking (chain-of-thought optimization), vision/VL (image input support), coder (code generation) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- LoRA (Low-Rank Adaptation) enables efficient fine-tuning by training only adapter weights; QLoRA applies LoRA on top of a 4-bit quantized base model ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Alignment tags in model names (Instruct, Chat, base) serve as the strongest first filter for model selection; deploying a base model in a user-facing assistant role is one of the most common and costly mistakes ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]
- Instruct quality varies across vendors — the label alone does not guarantee consistent instruction-following behavior; benchmark on your task set before deployment ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

## Details

The training variant hierarchy is: base (pretrained, raw text completion) → instruct (follows prompts reliably) → chat (optimized for multi-turn dialogue). Each layer builds on the previous one. Base models are for researchers who want to fine-tune their own model or study raw text completion. Instruct models are the default for virtually all practical use cases. Chat models add conversational context awareness. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

Other derivative suffixes found in community fine-tunes: `-abliterated` (safety refusal behavior surgically removed post-training), `-uncensored` (trained on unfiltered data to remove guardrails), `-reasoning` (optimized for chain-of-thought reasoning). ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/distillation]]
- [[concepts/quantization]]
- [[concepts/model_naming]]
- [[entities/hugging_face]]