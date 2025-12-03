from langsmith.client import Client
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

client = Client()

llm = ChatOllama(model="llama3.1:latest", temperature=0)

prompt = client.pull_prompt("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()