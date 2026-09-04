from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider

from agentic_research.capabilities.registry import CapabilityRegistry
from agentic_research.capabilities.linux import get_tools as get_linux_tools

provider = OllamaProvider(
    base_url="http://localhost:11434/v1",
)

model = OpenAIChatModel(
    "qwen3:8b",
    provider=provider,
)

registry = CapabilityRegistry()

registry.register_many(get_linux_tools())

agent = Agent(
    model,
    instructions="You are a helpful AI assistant.",
    tools=registry.get_tools(),
)

if __name__ == "__main__":
    result = agent.run_sync(
        "What operating system, kernel and architecture am I running?"
            "Use the system information tool."
    )

    print(result.output)