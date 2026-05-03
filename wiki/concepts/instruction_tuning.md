---
title: "Instruction Tuning"
summary: "Fine-tuning method that trains LLMs on instruction-response pairs, producing models that reliably follow user prompts"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/How to navigate LLM model names.md
tags:
  - llm
  - training
  - fine-tuning
  - alignment
created: "2026-05-01T12:00:00Z"
updated: "2026-05-02T12:00:00Z"
confidence: 0.9
provenance: merged
---

# Instruction Tuning

Instruction tuning (suffix: `-instruct`, `-IT`, or `-it`) is a fine-tuning method that trains LLMs on instruction-response pairs via supervised fine-tuning (SFT). It produces models that reliably follow user prompts: "Summarize this," "Write a function that..." -- the standard variant for most use cases. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Training Variant Hierarchy

| Variant | Description | When to Use |
|---|---|---|
| Base | Pretrained on text corpora via next-token prediction; completes text patterns but does not follow instructions reliably | Fine-tuning your own model, research, text completion |
| Instruct / IT | Fine-tuned on instruction-response pairs (SFT); follows user prompts reliably | Coding, Q&A, summarization, analysis -- virtually everything |
| Chat | Further optimized for multi-turn conversations with RLHF or DPO; better at maintaining context | Chatbot applications, interactive assistants |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Additional Training Suffixes

| Suffix | Meaning |
|---|---|
| `-DPO` | Trained with Direct Preference Optimization (alignment technique) |
| `-RLHF` | Trained with Reinforcement Learning from Human Feedback |
| `-reasoning` / `-thinking` | Optimized for chain-of-thought reasoning |
| `-vision` / `-VL` | Supports image input (vision-language) |
| `-coder` | Fine-tuned specifically for code generation |
| `-abliterated` | Safety refusal behavior surgically removed post-training |
| `-uncensored` | Trained on unfiltered data to remove guardrails |
| `-LoRA` | Fine-tuned with Low-Rank Adaptation (adapter weights only) |

^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Naming Guidance

For general use, always pick the instruct/IT variant. Base models are for researchers and fine-tuners. "Instruct" has largely replaced "chat" as the standard naming for conversational models in modern conventions. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md] ^[raw/articles/How to navigate LLM model names.md]

Alignment tags in model names serve as the strongest first filter for model selection -- deploying a base model in a user-facing assistant role is one of the most common and costly selection mistakes. However, Instruct quality varies across vendors -- always benchmark on your task set before deployment. ^[raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md]

## Related

- [[concepts/distillation]]
- [[concepts/model_naming]]
- [[concepts/quantization]]
- [[entities/hugging_face]]
