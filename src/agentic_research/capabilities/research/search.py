from abc import ABC, abstractmethod

from pydantic import BaseModel, Field



class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str = ""
    engine: str = ""
    metadata: dict[str, object] = Field(default_factory=dict)


class SearchProvider(ABC):
    @abstractmethod
    def search(self, query: str) -> list[SearchResult]:
        raise NotImplementedError