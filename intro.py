import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent = create_agent(
    model="gpt-5",
    tools=[],
    system_prompt="You are a helpful assistant.",
)

print(agent)