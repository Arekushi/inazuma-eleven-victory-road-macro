from dataclasses import dataclass
from typing import Union

from src.input.enums import (
    InputType,
    KeyboardKey,
    GamepadKey,
    MouseButton
)


InputKey = Union[KeyboardKey, GamepadKey, MouseButton]


@dataclass
class InputBinding:
    type: InputType
    key: InputKey
