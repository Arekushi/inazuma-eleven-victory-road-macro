from typing import Optional
from dataclasses import dataclass

from src.application.enums import SystemOS
from src.window.enums import WindowingSys


@dataclass(frozen=True)
class BackendKey:
    os: SystemOS
    windowing_sys: Optional[WindowingSys]
