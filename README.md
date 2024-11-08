# Generative AI Search Evaluations

This repository contains the tools and results for evaluating AI generated summaries.

## Set-Up

To use this repository, first you will need to set up a virtual environment.

In the root of the repository run:

```bash
python -m venv venv
```

On Windows run:

```bash
myenv\Scripts\activate
```

On mac/OS/Linux run:

```bash
source myenv/bin/activate
```

Within your virtual environment run:

```bash
pip install -r "requirements.txt"
```

## Examples

This repository contains example notebooks in the `example_notebooks` folder. These examples implement LLM-as-a-Judge and demonstrate the theory behind LLM-as-a-Judge.

## Augmentation

The `augmentation` folder allows you to apply basic augmentations to prompts such as typos, misspellings and poor punctuation.

This let's you test the quality of summaries using poor quality prompts.

#### Contributors
- Will Poulett