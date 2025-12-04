Here's the polished markdown:

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

**Features**
------------

* **Retrieve**: Retrieve relevant documents from a vector store.
* **Grade Documents**: Grade the relevance of the retrieved documents using a language model.
* **Generate**: Generate an answer based on the graded documents and question.
* **Web Search**: If the generated answer is not grounded in facts, perform a web search to gather additional information.
* **Hallucination Grader**: Detect and prevent hallucinations by evaluating the relevance of generated answers. This feature uses a combination of natural language processing (NLP) techniques and machine learning algorithms to identify potential hallucinations.
	+ Implementation details:
		- Utilizes a pre-trained language model for document grading
		- Employs a threshold-based approach to detect hallucinations
* **Recent Updates**:
	+ Improved language model-based grading for more accurate document relevance evaluation
	+ Enhanced web search integration for gathering additional information

**Components**
--------------

* `graph/chain/retrieval_grader.py`: A language model-based grader for evaluating the relevance of retrieved documents.
* `app` function in `graph/graph.py`: This will start the graph-based workflow and generate an answer to the user's question.

**Tech Stack**
-------------

* **Programming Language**: Python 3.9
* **Vector Store**: Faiss (Facebook AI Similarity Search)
* **Web Search**: Google Custom Search API
* **Natural Language Processing Library**: NLTK
* **Machine Learning Framework**: TensorFlow

**Usage**
-----

To run the workflow, follow these steps:

1. Install the required libraries by running `pip install -r requirements.txt`.
2. Set up a vector store using Faiss and populate it with relevant documents.
3. Configure the web search API credentials in the `graph/graph.py` file.
4. Execute the `app` function in `graph/graph.py` to start the graph-based workflow.

**Requirements**
--------------

* **Python**: 3.9
* **Ollama library**
* **Faiss (Facebook AI Similarity Search)**
* **Google Custom Search API**
* **NLTK**
* **TensorFlow**

**Contributing**
--------------

We welcome contributions! Please submit a pull request with your changes.

**License**
---------

This project is licensed under the MIT License.