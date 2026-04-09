from enum import Enum


class GamepadKey(str, Enum):
    A = 'A'
    B = 'B'
    X = 'X'
    Y = 'Y'
    START = 'START'
    BACK = 'BACK'
    RB = 'RB'
    LB = 'LB'
    DPAD_UP = 'DPAD_UP'
    DPAD_DOWN = 'DPAD_DOWN'
    DPAD_LEFT = 'DPAD_LEFT'
    DPAD_RIGHT = 'DPAD_RIGHT'
    RT = 'RT'
    LT = 'LT'

    def __str__(self) -> str:
        return self.value
