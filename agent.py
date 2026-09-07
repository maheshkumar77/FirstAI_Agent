from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools import calculator, study_planner, save_note


model = ChatOllama(
    model="qwen3:1.7b",
    temperature=0
)


agent = create_agent(
    model=model,
    tools=[calculator, study_planner, save_note]
)