from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider


provider = OllamaProvider(
    base_url="http://localhost:11434/v1",
)

model = OpenAIChatModel(
    "qwen3:8b",
    provider=provider,
)

agent = Agent(
    model,
    instructions="You are a helpful AI assistant.",
)


if __name__ == "__main__":
    result = agent.run_sync(
        "Explain what an agentic AI system is in one sentence."
    )

    print(result.output)