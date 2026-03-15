import os

from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv


load_dotenv()

llm = LLM(
    model="openai/gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    #base_url="https://api.openai.com/v1"  You only use base_url when connecting to non-OpenAI endpoints -- Local LLM (Ollama) - http://localhost:11434, OpenRouter - https://openrouter.ai/api/v1,  Azure OpenAI - Azure endpoint URL , Azure endpoint URL - https://api.together.xyz/v1
    temperature=0.7, 
    max_tokens=1000,
    timeout=120
)

thinker = Agent(
    role="Critical Thinker",
    goal="Analyse the text and identify if any conflicting information within",
    llm=llm,
    backstory=(
        "You are a who understands details very well and expert negotiator. \
        You can identify conflicting statements information in given text."
    ),

)


