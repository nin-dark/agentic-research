from collections.abc import Callable

from .system import get_system_info



def get_tools() -> list[Callable]:
    return [
        get_system_info,
    ]