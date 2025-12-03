from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

load_dotenv()

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = []
for url in urls:
    docs.extend(WebBaseLoader(url).load())

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)

splitted_docs = text_splitter.split_documents(docs)

# vectorstore = Chroma.from_documents(
#     documents=splitted_docs,
#     collection_name="rag-chroma",
#     embedding=OllamaEmbeddings(model="mxbai-embed-large:latest"),
#     persist_directory="./.chroma",
# )

retriever = Chroma(
    collection_name="rag-chroma",
    embedding_function=OllamaEmbeddings(model="mxbai-embed-large:latest"),
    persist_directory="./.chroma",
).as_retriever()