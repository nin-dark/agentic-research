from collections.abc import Callable



Tool = Callable[..., object]



class CapabilityRegistry:
    def __init__(self) -> None:
        self._tools: list[Callable] = []

    def register(self, tool: Callable) -> None:
        self._tools.append(tool)

    def register_many(self, tools: list[Tool]) -> None:
        self._tools.extend(tools)

    def get_tools(self) -> list[Tool]:
        return list(self._tools)