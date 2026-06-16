from dataclasses import dataclass
from typing import Any


@dataclass
class WindowRect:
    left: float | int | Any
    top: float | int | Any
    width: float | int | Any
    height: float | int | Any
    right: float | int | Any
    bottom: float | int | Any
