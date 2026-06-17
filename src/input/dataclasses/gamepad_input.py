from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class GamepadInput:
    button: Optional[int] = None
    trigger: Optional[callable] = None
    intensity: int = 255
