# Bias and Limitations

This notebook focuses on a point that is easy to miss when a model appears fluent: strong outputs do not imply neutral, fair, or reliable behavior.

## What This Notebook Is Really About

The real subject here is not just model performance. It is the gap between impressive language behavior and trustworthy behavior.

Pretrained models absorb patterns from large datasets, and those datasets contain social bias, stereotypes, and uneven representation. The model therefore learns more than syntax and semantics. It also learns undesirable patterns from its training data.

## Core Ideas

### Pretrained models inherit bias from data

A model trained on biased text distributions will reproduce biased associations unless that problem is addressed explicitly.

### Good predictions can still be harmful

A response may look coherent and still reinforce stereotypes or exclude certain groups. Fluency is not the same as safety.

### Benchmark success does not equal real-world reliability

A model can score well on standard tasks and still behave poorly in open-ended or socially sensitive settings.

### Evaluation must include judgment, not just metrics

Some failures are not visible in accuracy scores. They appear when we inspect examples closely and ask what assumptions the model is making.

## What I Learned

- Models reflect their data more than they reflect any abstract idea of truth or fairness.
- Bias is not a side issue added after modeling. It is part of understanding how these systems behave.
- Responsible use requires critical evaluation of outputs, not passive trust in them.
- Model limitations are often easiest to see in edge cases, ambiguous prompts, and socially loaded examples.

## Why This Matters

This notebook is a reminder that using Transformer models well means more than getting them to run.

It also means asking what kinds of patterns they reproduce, where they fail, and what risks they introduce when their outputs are treated as neutral or authoritative.
