# DeepEval

[DeepEval](https://docs.confident-ai.com/docs/getting-started) is an open-source evaluation framework for LLMs.

It aims to be easy to implement and contains over 14 LLM evaluation metrics.

It's github is [here](https://github.com/confident-ai/deepeval).

You can use any LLM to run evaluations.

## Metrics

### [G-Eval](https://docs.confident-ai.com/docs/metrics-llm-evals)

G-Eval is a framework that uses LLMs with chain-of-thoughts (CoT) to evaluate LLM outputs based on **any** custom criteria. It is the most versatile metric offered by DeepEval.

As demonstrated in this [paper](https://arxiv.org/abs/2303.16634), it is capable of evaluating almost any use case with human-like accuracy.

As any custom criteria can be evaluated with G-Eval, it may be very useful for this project.

**Should we use this metric?** Yes - this is very versatile, with a methodology backed by a scientific paper. It allows you to pass an input (Our question to the summariser), the actual output, the expected output and the context.

### [Summarisation](https://docs.confident-ai.com/docs/metrics-summarization)

The summarization metric uses LLMs to determine whether your LLM (application) is generating factually correct summaries while including the necessary details from the original text. #Add more explainer

The score is calculated by taking the lowest value of either the alignment or coverage score. Alignment measures whether the returned summary has any hallucinations or contradicting text, whilst the coverage score measures if all the necessary information from the original text is included.

The coverage calculated by generating `n` questions from the reference text, then for each question, generating a 'yes', 'no' or 'I don't know' answer based on the summary. For alignment, `n` questions are again generated but this time from the summary, and answers are generated based on the original text. An article explaining the method can be found [here](https://www.confident-ai.com/blog/a-step-by-step-guide-to-evaluating-an-llm-text-summarization-task#calculating-alignment-score).

Given up to 10 documents can be used per summary, we may need high `n` values to accurately measure the coverage. We might also always expect coverage to be lower than the alignment score as information will be missed more often than hallucinations occur. For this reason, we may want to split alignment and coverage scores.

**Should use use this metric?** Maybe, this is a good general summary metric. However, given the number of documents which feed into the summary we may wish to split teh alignment and coverage score up, possibly using G-Eval.

### [Faithfulness](https://docs.confident-ai.com/docs/metrics-faithfulness)

This method assesses if the actual output of your LLM factually aligns with the contents of your retrieved context.

This is useful as we do not have a 'ground truth' summary for evaluation, but we do have the retrieved documents.

**Should use use this metric?** Yes - although we could implement this ourselves using G-Eval.

### [Answer Relevancy](https://docs.confident-ai.com/docs/metrics-faithfulness)

This measures how relevant the actual_output of your LLM is compared to the provided input.

It may be useful to us as we can ask questions with the search feature, and want a relevant response.

**Should use use this metric?** Yes - although we could implement this ourselves using G-Eval.

### [Contextual Relevancy](https://docs.confident-ai.com/docs/metrics-contextual-relevancy)

This evaluates the overall relevance of the information presented in your retrieval context for a given input. It considers the total number of relevant statements compared to the total number of statements.

**Should use use this metric?** Yes, this is an easy to understand measurement of relevance.

### [Contextual Precision](https://docs.confident-ai.com/docs/metrics-contextual-precision)

The contextual precision metric measures your RAG pipeline's retriever by evaluating whether nodes in your retrieval context that are relevant to the given input are ranked higher than irrelevant ones.

This is similar to precision at K, but this measurement takes into consideration the order of returned results.

**Should use use this metric?** Maybe, precision at K is simpler to understand, but LLMs are better at giving attention to information given earlier in the prompt.

### [Contextual Recall](https://docs.confident-ai.com/docs/metrics-contextual-recall)

This measures the quality of your summary by evaluating the extent of which the retrieved context aligns with the expected output.

**Should use use this metric?** Yes. Although whilst this is a useful metric to include, we're limited by having no expected output in this project.

### [RAGAS](https://docs.confident-ai.com/docs/metrics-ragas)

RAGAS averages across four distinct metrics: Relevancy, Faithfulness, Precision and Recall. However, it needs an expected output.

**Should use use this metric?** NYes. Although whilst this is a useful metric to include, we're limited by having no expected output in this project.

### [Hallucination](https://docs.confident-ai.com/docs/metrics-hallucination)

This evaluates if your LLM generates factually correct information by comparing the actual output to the provided context.

It considers the number of contradicted statements compared to the total number of statements.

**Should use use this metric?** Yes.

### [Toxicity](https://docs.confident-ai.com/docs/metrics-toxicity)

This evaluates toxicness in LLM outputs, given the input and output. DeepEval give their definition of toxicity [here](https://docs.confident-ai.com/docs/metrics-toxicity).

**Should use use this metric?** Yes, although if the supplier is using content filters this may be expensive and not necessary.

### [Bias](https://docs.confident-ai.com/docs/metrics-bias)

This considers if your LLM output contains gender, racial, or political bias.

**Should use use this metric?** Yes, although if the supplier is using content filters this may be expensive and not necessary.

### [Custom Metrics](https://docs.confident-ai.com/docs/metrics-custom)

It is very easy to build custom metrics using DeepEval. They have good documentation on doing so [here](https://docs.confident-ai.com/docs/metrics-custom).

**Should use use this metric?** No, whilst this is useful, G-Eval offers the same versatility and is better aligned to humans.

## [Test Cases](https://docs.confident-ai.com/docs/evaluation-test-cases)

A test case allows you to use evaluation metrics you have defined to unit test LLM applications.

You can integrate evaluations with Pytest.