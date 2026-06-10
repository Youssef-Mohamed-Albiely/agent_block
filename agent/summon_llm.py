import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
api_key=os.environ.get("GROQ_API_KEY"),
base_url="https://api.groq.com/openai/v1",
model="openai/gpt-oss-20b",
temperature=0.0
)
