import platform
import shutil

from pydantic_ai import RunContext



def get_system_info(ctx: RunContext) -> str:
    system = platform.system()
    release = platform.release()
    machine = platform.machine()
    python_version = platform.python_version()

    total, used, free = shutil.disk_usage("/")

    return (
        f"OS: {system}\n"
        f"Kernel: {release}\n"
        f"Architecture: {machine}\n"
        f"Python: {python_version}\n"
        f"Root filesystem: "
        f"{used // (1024**3)} GiB used / "
        f"{total // (1024**3)} GiB total"
    )