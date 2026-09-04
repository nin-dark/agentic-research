from abc import ABC, abstractmethod
from typing import Any

class ModelProvider(ABC):
	@abstractmethod
	def generate(
		self,
		messages: list[dict[str, str]],
		**kwargs: Any,
	) -> str:
		raise NotImplementedError
