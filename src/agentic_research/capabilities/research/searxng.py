from typing import Any

import httpx

from .search import SearchProvider, SearchResult



class SearXNGProvider(SearchProvider):
    def __init__(
        self,
        base_url: str = "http://localhost:8080",
        timeout: float = 15.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def search(
        self,
        query: str,
        engines: list[str] | None = None,
    ) -> list[SearchResult]:
        params = {
            "q": query,
            "format": "json",
        }

        if engines:
            params["engines"] = ",".join(engines)

        response = httpx.get(
            f"{self.base_url}/search",
            params=params,
            timeout=self.timeout,
        )

        response.raise_for_status()

        data: dict[str, Any] = response.json()

        return [
            SearchResult(
                title=result.get("title", ""),
                url=result.get("url", ""),
                snippet=result.get("content", ""),
                engine=result.get("engine", ""),
                metadata=result,
            )
            for result in data.get("results", [])
            if result.get("url")
        ]