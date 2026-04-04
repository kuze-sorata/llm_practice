# Tokenizers (PyTorch)

This notebook examines the step that makes Transformer models possible at all: turning text into discrete units the model can represent numerically.

## What This Notebook Is Really About

The main lesson is that tokenization is not a trivial preprocessing step. It is the interface between human language and model computation.

Without tokenization, there is no stable vocabulary, no input IDs, and no way for the model to process text as tensors.

## Core Ideas

### Tokenization is a representation decision

How text is split changes what the model can recognize efficiently. Word-level splitting is simple, but subword tokenization is what makes modern Transformer vocabularies practical.

### Vocabulary lookup is how text becomes numbers

Tokens must be mapped into IDs before they can be embedded and processed by the model.

### Special tokens carry structure

Tokens such as classification or separator markers are not ordinary words. They tell the model how to organize and interpret the input.

### Decoding is only a partial reversal

Going from IDs back to text is useful, but it also reveals that tokenization is not always a perfectly intuitive mirror of natural language.

## What I Learned

- Tokenizers do more than split strings. They define the model's input language.
- Subword tokenization is a practical compromise between vocabulary size and coverage.
- Special tokens are part of the model interface and should be treated as such.
- Understanding encoding and decoding makes debugging downstream model behavior much easier.

## Why This Matters

This notebook makes it clear that tokenization is foundational, not peripheral.

If I do not understand the tokenizer, I do not fully understand what the model is actually reading.
