from agentic_research.models.base import ModelProvider


class Agent:
    def __init__(
        self,
        provider: ModelProvider,
        system_prompt: str = "You are a helpful AI assistant.",
    ) -> None:
        self.provider = provider
        self.system_prompt = system_prompt

        self.messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

    def run(self, user_input: str) -> str:
        self.messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = self.provider.generate(self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        return response