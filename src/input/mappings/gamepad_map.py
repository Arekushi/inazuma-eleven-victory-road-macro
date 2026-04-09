import vgamepad as vg

from src.input.classes.gamepad_input import GamepadInput
from src.input.enums.gamepad_key import GamepadKey


GAMEPAD_KEY_MAP: dict[GamepadKey, GamepadInput] = {
    GamepadKey.A: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A),
    GamepadKey.B: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B),
    GamepadKey.X: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X),
    GamepadKey.Y: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y),
    GamepadKey.START: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START),
    GamepadKey.BACK: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK),
    GamepadKey.RB: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER),
    GamepadKey.LB: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER),
    GamepadKey.DPAD_UP: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP),
    GamepadKey.DPAD_DOWN: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN),
    GamepadKey.DPAD_LEFT: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT),
    GamepadKey.DPAD_RIGHT: GamepadInput(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT),
    GamepadKey.RT: GamepadInput(trigger=lambda gp, v: gp.right_trigger(value=v)),
    GamepadKey.LT: GamepadInput(trigger=lambda gp, v: gp.left_trigger(value=v)),
}
