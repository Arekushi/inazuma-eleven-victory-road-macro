from enum import Enum


class InputType(str, Enum):
    KEYBOARD = 'keyboard'
    MOUSE = 'mouse'
    GAMEPAD_BUTTON = 'gamepad_button'
    GAMEPAD_TRIGGER = 'gamepad_trigger'
