from enum import Enum


class MouseButton(Enum):
    LEFT = 'LEFT'
    MIDDLE = 'MIDDLE'
    RIGHT = 'RIGHT'
    PRIMARY = 'PRIMARY'
    SECONDARY = 'SECONDARY'
    
    def __str__(self) -> str:
        return self.value
