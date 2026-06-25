import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")


if not groq_key:
    raise ValueError("Enter your Groq API key in .env file")
llm = ChatOpenAI(
api_key=groq_key,
base_url="https://api.groq.com/openai/v1",
model="openai/gpt-oss-20b",
temperature=0.0
)
