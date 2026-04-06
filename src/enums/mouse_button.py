from enum import Enum


class MouseButton(Enum):
    LEFT = 'left'
    MIDDLE = 'middle'
    RIGHT = 'right'
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    
    def __str__(self) -> str:
        return self.value
