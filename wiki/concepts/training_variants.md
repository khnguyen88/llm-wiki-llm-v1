---
title: "Training Variants"
type: concept
date: 2026-04-23
sources:
  - raw/articles/How to navigate LLM model names.md
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
  - raw/articles/LLM Model Naming Conventions_ How to Read Names and Why They Matter.md
  - raw/articles/Naming Conventions of LLM Models.md
  - raw/articles/Understanding Naming Conventions Of LLM Files_ A Comprehensive Guide.md
tags:
  - llm
  - fine-tuning
  - training
  - deployment
---

# Training Variants

After pretraining on massive text corpora, models are fine-tuned for specific behaviors. The training variant suffix in a model name tells you how the model was aligned and what tasks it is optimized for.

## Base (Pretrained)

- Trained via next-token prediction on massive text corpora.
- Completes text patterns but does not reliably follow instructions.
- **When to use:** Fine-tuning your own model, research, text completion.
- **Risk:** Deploying a base model in a user-facing assistant role is one of the most common and costly selection mistakes.

## Instruct / IT (Instruction Tuned)

- Fine-tuned on instruction-response pairs via supervised fine-tuning (SFT).
- Follows user prompts reliably: "Summarize this," "Write a function that..."
- The standard variant for most use cases.
- **When to use:** Coding, Q&A, summarization, analysis — virtually everything.
- **Note:** "Instruct" quality varies across vendors. Always benchmark on your task set.

## Chat

- Further optimized for multi-turn conversations with RLHF (Reinforcement Learning from Human Feedback) or DPO (Direct Preference Optimization).
- Better at maintaining context across a conversation.
- Some older models use "chat" where modern models use "instruct."
- **When to use:** Chatbot applications, interactive assistants.

## Other Training Suffixes

| Suffix | Meaning |
|--------|---------|
| `-DPO` | Direct Preference Optimization alignment |
| `-RLHF` | Reinforcement Learning from Human Feedback |
| `-reasoning` / `-thinking` | Chain-of-thought reasoning optimization |
| `-vision` / `-VL` | Supports image input (vision-language) |
| `-coder` | Fine-tuned for code generation |
| `-embedding` | Generates vector embeddings for RAG |
| `-guard` / `-guardian` | Safety/content filtering |
| `-medical` | Domain-specific fine-tuning for healthcare |

## Decision Flow

1. **Need raw inference or custom fine-tuning?** → Base model.
2. **Need general assistant behavior?** → Instruct/IT model.
3. **Need multi-turn conversation quality?** → Chat model.

For general use, always pick the instruct/IT variant. Base models are for researchers and fine-tuners.

## Related

- [[concepts/llm_naming_conventions]]
- [[concepts/model_distillation]]
- [[summaries/llm-model-names-decoded]]
- [[summaries/how-to-navigate-llm-model-names]]
- [[summaries/llm-model-naming-conventions]]
- [[summaries/naming-conventions-of-llm-models]]
