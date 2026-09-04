from typing import Any

from .base import ModelProvider


class OllamaProvider(ModelProvider):
	def __init__(
		self,
		model: str,
		base_url: str = "http://localhost:11434",
	) -> None:
		self.model = model
		self.base_url = base_url.rstrip("/")

	def generate(
		self,
		messages: list[dict[str, str]],
		**kwargs: Any,
	) -> str:
		import json
		import urllib.request

		payload = {
			"model": self.model,
			"messages": messages,
			"stream": False,
			**kwargs,
		}

		request = urllib.request.Request(
			f"{self.base_url}/api/chat",
			data=json.dumps(payload).encode("utf-8"),
			headers={"Content-Type": "application/json"},
			method="POST",
		)

		with urllib.request.urlopen(request) as response:
			data = json.loads(response.read().decode("utf-8"))

		return data["message"]["content"]