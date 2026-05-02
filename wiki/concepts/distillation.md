---
title: "Distillation"
summary: "Training technique where a smaller student model learns to replicate a larger teacher model's outputs, transferring capability at smaller scale"
type: concept
sources:
  - raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md
tags:
  - llm
  - training
  - distillation
  - efficiency
created: "2026-05-01T12:00:00Z"
updated: "2026-05-01T12:00:00Z"
confidence: 0.9
provenance: extracted
---

# Distillation

Distillation is a training technique where a smaller "student" model is trained to replicate a larger "teacher" model's outputs. When you see "-Distill" in a model name, it means the model learned its skills from a bigger model, not just from raw data. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Key Points

- The student model learns from the teacher's outputs rather than only from original training data, transferring capabilities at smaller scale ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- DeepSeek-R1-Distill-Qwen-32B: a Qwen 2.5 32B model fine-tuned on 800,000 chain-of-thought reasoning samples from DeepSeek-R1 (671B); outperforms OpenAI o1-mini on multiple benchmarks despite being ~20x smaller ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- The 2026 trend: DeepSeek-R1 proved you can get 80%+ of frontier reasoning in a 7-32B model through distillation; everyone is distilling now ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]
- Model names with "-distilled" or "-Distill" suffix indicate distilled models (e.g., DeepSeek-R1-Distill-Qwen-32B) ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Details

Distillation is part of the broader 2026 "distillation economy" trend. DeepSeek-R1 demonstrated that frontier reasoning capabilities can be compressed into models 20x smaller, and this approach has been widely adopted. The result is a new class of small, capable models that punch far above their parameter count. ^[raw/articles/LLM Model Names Decoded_ A Developer's Guide to Parameters, Quantization & Formats.md]

## Related

- [[concepts/instruction_tuning]]
- [[entities/deepseek]]
- [[entities/qwen]]