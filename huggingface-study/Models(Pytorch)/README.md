# Models (PyTorch)

This notebook explores Transformer models more directly, outside the convenience of task-specific wrappers.

## What This Notebook Is Really About

The main lesson is that a model is not just a black box downloaded from the Hub. It has a structure, a configuration, parameters, and a defined input/output format.

That matters because using pretrained models well requires understanding the difference between architecture and learned weights.

## Core Ideas

### Configuration and parameters are different things

The config defines the model's structure and behavior. The parameters are the learned values that make the model useful.

### A pretrained model is reusable because it is standardized

The same architecture can be instantiated from config or loaded with pretrained weights from a checkpoint. This makes the ecosystem composable and consistent.

### Model outputs are structured objects

A forward pass does not just return a vague prediction. It returns tensors with shapes and meanings such as hidden states or logits.

### Saving and loading are part of the workflow

A model is something you inspect, reuse, serialize, and reload. Practical ML work depends on that portability.

## What I Learned

- Loading a checkpoint is only one part of using a model correctly; understanding its inputs and outputs matters just as much.
- Transformer models become less intimidating once I inspect their configuration and tensor shapes.
- Pretrained weights are what give the architecture practical knowledge, but the architecture still determines what kind of computation is possible.
- Working directly with the model object makes later fine-tuning workflows easier to understand.

## Why This Matters

This notebook helps shift the perspective from "calling a model" to "understanding what a model instance actually is."

That is a necessary step before debugging, modifying, or fine-tuning Transformer systems in a serious way.
