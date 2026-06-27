try:
    from evdev import ecodes as e
except ImportError:
    e = None

from src.input.dataclasses import GamepadInput
from src.input.enums import GamepadKey



if e is not None:
    EVDEV_KEY_MAP: dict[GamepadKey, GamepadInput] = {
        GamepadKey.A: GamepadInput(button=e.BTN_SOUTH),
        GamepadKey.B: GamepadInput(button=e.BTN_EAST),
        GamepadKey.X: GamepadInput(button=e.BTN_NORTH),
        GamepadKey.Y: GamepadInput(button=e.BTN_WEST),
        GamepadKey.START: GamepadInput(button=e.BTN_START),
        GamepadKey.BACK: GamepadInput(button=e.BTN_SELECT),
        GamepadKey.RB: GamepadInput(button=e.BTN_TR),
        GamepadKey.LB: GamepadInput(button=e.BTN_TL),
        GamepadKey.DPAD_UP: GamepadInput(button=e.BTN_DPAD_UP),
        GamepadKey.DPAD_DOWN: GamepadInput(button=e.BTN_DPAD_DOWN),
        GamepadKey.DPAD_LEFT: GamepadInput(button=e.BTN_DPAD_LEFT),
        GamepadKey.DPAD_RIGHT: GamepadInput(button=e.BTN_DPAD_RIGHT,),
        GamepadKey.RT: GamepadInput(trigger=lambda ui, value: ui.write(e.EV_ABS, e.ABS_RZ, value)),
        GamepadKey.LT: GamepadInput(trigger=lambda ui, value: ui.write(e.EV_ABS, e.ABS_Z, value)),
    }
else:
    EVDEV_KEY_MAP = {}
