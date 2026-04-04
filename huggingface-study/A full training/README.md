# Hugging Face Transformers Notes: Full Training with BERT on MRPC

This folder documents a hands-on study of fine-tuning `bert-base-uncased` on the GLUE MRPC task with the Hugging Face ecosystem.

The goal is not just to run the notebook, but to understand what the training loop is doing and why each step matters.

## Task

- Dataset: GLUE MRPC
- Problem type: sentence-pair classification
- Objective: predict whether two sentences are paraphrases

## Core Idea

At a high level, training is a repeated correction process:

```text
prediction -> error measurement -> gradient computation -> parameter update
```

Everything in the notebook supports that loop.

## Training Pipeline

1. Load the MRPC dataset.
2. Tokenize sentence pairs with the BERT tokenizer.
3. Remove unused columns and rename `label` to `labels`.
4. Build dataloaders with dynamic padding.
5. Load `AutoModelForSequenceClassification`.
6. Run training with `loss.backward()`, optimizer updates, and a learning-rate scheduler.
7. Evaluate with accuracy and F1.

## What Matters Conceptually

### 1. Tokenization is not just preprocessing

For a sentence-pair task, both sentences must be encoded together so the model can learn their relationship, not just their individual meanings.

### 2. `logits` are raw scores, not probabilities

The model produces logits first. The predicted class comes from comparing those scores, typically with `argmax`.

### 3. `backward()` and `step()` do different jobs

- `loss.backward()` computes how the parameters should change.
- `optimizer.step()` applies those changes.

One is analysis, the other is execution.

### 4. The optimizer is not enough on its own

The scheduler matters because fine-tuning is sensitive to learning-rate behavior. A linear decay schedule helps stabilize later training steps.

### 5. Training and evaluation have different rules

During training, the model updates weights and tracks gradients.
During evaluation, gradients should be disabled and weights must stay fixed.

## Common Failure Points

- Forgetting to rename `label` to `labels`
- Moving the model to GPU but leaving batches on CPU
- Forgetting `optimizer.zero_grad()`
- Running evaluation without `torch.no_grad()`
- Misreading logits as probabilities

## Libraries Used

- `transformers`
- `datasets`
- `torch`
- `evaluate`
- `accelerate`

## Why This Notebook Is Useful

This notebook is a good bridge between high-level Trainer-based workflows and lower-level PyTorch training loops.

It makes the mechanics of fine-tuning visible:

- how batches are formed,
- how the loss is produced,
- how gradients flow,
- and how model parameters actually change over time.

## Next Steps

- Run inference on custom sentence pairs
- Compare manual training with the `Trainer` API
- Try another task such as NER or question answering
- Experiment with batch size, learning rate, and number of epochs
