# Behind the Pipeline (PyTorch)

This notebook breaks a Hugging Face `pipeline` into its underlying parts and shows what actually happens between raw text input and final model output.

## What This Notebook Is Really About

The main point is that a pipeline is not magic. It is a convenient wrapper around a sequence of concrete steps:

```text
text -> tokenization -> tensors -> model forward pass -> logits -> post-processing
```

Once that flow is clear, the higher-level API becomes much easier to reason about.

## Core Ideas

### A pipeline is an interface, not a different model

The same pretrained checkpoint can be used through a high-level `pipeline` or through explicit tokenizer and model calls. The difference is convenience, not capability.

### Tokenizers define how text enters the model

Raw strings cannot go directly into a Transformer. They must first be converted into token IDs, attention masks, and other structured inputs.

### Models operate on tensors, not words

The forward pass is numerical. By the time the model sees the input, language has already been transformed into vectors and tensor shapes.

### Logits are intermediate signals

The model does not directly output labels like "positive" or "negative." It produces logits, and those logits are interpreted afterward.

## What I Learned

- A `pipeline` is useful because it hides repetitive setup, not because it changes the underlying computation.
- Tokenization is the true entry point into Transformer inference.
- Inspecting tensors and logits makes model behavior much less mysterious.
- High-level abstractions are easier to trust once the lower-level path is visible.

## Why This Matters

This notebook is a bridge between "I can run a model" and "I understand how the model is being run."

That shift matters because debugging, customization, and fine-tuning all require understanding what sits behind the pipeline abstraction.
