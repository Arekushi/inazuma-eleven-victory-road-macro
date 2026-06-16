from dataclasses import dataclass
from src.window.dataclasses import WindowRect


@dataclass
class WindowContext:
    rect: WindowRect
    monitor_index: int
