**Project Title & Description**
==============================

Advanced RAG (Reinforced Agent Generator) is an open-source project that leverages large language models to generate answers to user questions. It uses a combination of web search and vector-based retrieval to gather relevant documents, which are then used to ground the generated answer in facts.

**Key Features**
-----------------

*   **Web Search Integration**: The system can route user queries to web search when necessary.
*   **Vector-Based Retrieval**: Advanced RAG utilizes a vector store to retrieve relevant documents related to agents, prompt engineering, and adversarial attacks. This retrieval process works by converting user queries into vectors that are then matched against the stored vectors in the vector store, allowing for efficient and accurate document retrieval.
*   **LLM Generation with LLaMA and Ollama**: The system uses large language models (LLMs) to generate answers based on the retrieved documents. Both LLaMA and Ollama are utilized for generation tasks, enabling the system to leverage the strengths of each model.
*   **Hallucination Grading with LLMs**: A grading mechanism is implemented to assess whether the generated answer is grounded in facts or contains hallucinations. This mechanism utilizes large language models (LLMs) to evaluate the generated answer and provide a score indicating its accuracy.
*   **State Graph Workflow**: Advanced RAG employs a state graph workflow that includes nodes for retrieval, document grading, generation, and web search. This modular architecture facilitates efficient processing of user queries and ensures that relevant information is retrieved and utilized for generation.

**Hallucination Grading with LLMs**
--------------------------------

The system's hallucination grading mechanism utilizes large language models (LLMs) to assess the generated answer. This approach enables accurate identification of factual inaccuracies and hallucinations.

**State Graph Workflow**
------------------------

Advanced RAG employs a state graph workflow that includes nodes for retrieval, document grading, generation, and web search. This modular architecture facilitates efficient processing of user queries and ensures that relevant information is retrieved and utilized for generation.

The state graph workflow is implemented in the `graph/graph.py` file, which defines a `GraphState` class representing the state of the graph. The `graph/consts.py` file defines constants for different states in the graph.

**Tech Stack**
---------------

*   **Python 3.x**: The primary programming language used for development.
*   **LangChain**: An open-source library for building conversational AI applications.
*   **LLMs (Large Language Models)**: Utilized for generation and grading tasks, including LLaMA and Ollama.

**Getting Started**
-------------------

To run the Advanced RAG system, follow these steps:

1.  Clone the repository using `git clone`.
2.  Install required dependencies by running `pip install -r requirements.txt`.
3.  Set up environment variables for web search and vector store access.
4.  Run the system using `python main.py`.

**Testing**
------------

The project includes unit tests to ensure the correctness of individual components. To run the tests, execute `python -m unittest discover` in the root directory.

**Contributing**
----------------

We welcome contributions from the community! If you'd like to contribute to Advanced RAG, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement changes and write unit tests as necessary.
4.  Submit a pull request with a clear description of your changes.

**Vector-Based Retrieval Implementation**
----------------------------------------

The vector-based retrieval process is implemented in the `graph/chain/retrieval_grader.py` file, which defines a grader that uses an LLM to assess the relevance of retrieved documents.

**LLM Generation with LLaMA and Ollama**
-----------------------------------------

The system uses large language models (LLMs) to generate answers based on the retrieved documents. Both LLaMA and Ollama are utilized for generation tasks, enabling the system to leverage the strengths of each model. The implementation details can be found in the `graph/chain/generation.py` file.

**Hallucination Grading with LLMs**
--------------------------------

The hallucination grading mechanism is implemented using large language models (LLMs) to evaluate the generated answer and provide a score indicating its accuracy. The implementation details can be found in the `graph/chain/hallucination_grader.py` file.

**License**
----------

Advanced RAG is released under the MIT License. See `LICENSE.txt` for details.

Note: This README file provides an overview of the project's features, tech stack, and setup instructions. For more detailed information on individual components or implementation specifics, please refer to the corresponding documentation within the codebase.