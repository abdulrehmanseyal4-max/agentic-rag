Here is the polished Markdown version of the README file:

**Agentic RAG**
================

A graph-based workflow for generating answers to user questions using a combination of vectorstore and web search.

**Overview**
------------

This project implements a graph-based workflow for generating answers to user questions. The workflow consists of several nodes, each representing a different step in the process:

1. **Retrieve**: Retrieve relevant documents from a vector store.
2. **Grade Documents**: Grade the relevance of the retrieved documents using a language model.
3. **Generate**: Generate an answer based on the graded documents and question.
4. **Web Search**: If the generated answer is not grounded in facts, perform a web search to gather additional information.

**Components**
--------------

* `graph/chain/retrieval_grader.py`: A language model-based grader for evaluating the relevance of retrieved documents.
*

**Usage**
-----

To run the workflow, simply execute the `app` function in `graph/graph.py`. This will start the graph-based workflow and generate an answer to the user's question.

**Requirements**
--------------

* Ollama library

**Contributing**
--------------

Contributions are welcome! Please submit a pull request with your changes.

**License**
---------

This project is licensed under the MIT License.
