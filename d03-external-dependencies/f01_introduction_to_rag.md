# Introduction to RAG
_______________________________________________________________________________

## What is RAG? 

RAG stands for `Retrieval-Augmented Generation`

RAG is a design pattern for building 
AI (Artificial Intelligence) applications.

RAG is a technique that allows LLMs (Large Language Models) to incorporate
new information from external data sources.

This improves the accuracy of responses that an AI application 
can return to the user, 
because application now has access to domain-specific knowledge 
about a topic.

It also reduces `hallucinations`.

A `hallucination` is when the AI model confidently gives
and incorrect answer because it lacks the data required 
to answer that question.

In simple terms, RAG is used to overcome the limitations of an LLM.
_______________________________________________________________________________

## What tools are used to build RAG?

- If you are using `Python`, you would use the `LangChain` framework
- If you are using `Rust`, you would use the `Rig` framework
_______________________________________________________________________________

## What are the steps of a RAG workflow?

1. Intergrate data into the AI system

2. The user asks a question to the AI application via a prompt.

A prompt is the text input from the user that contains intructions for a task
that they want the AI application to perform, as well any required context 
that the AI application can use to give a custom response, 
rather than a generic one.

3. Then the AI application retrieves the most relevant documents.

4. The documents are inserted into the prompt as additional context.

5. Then the language model can generate an answer.
_______________________________________________________________________________



_______________________________________________________________________________
