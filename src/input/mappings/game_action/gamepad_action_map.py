from src.input.enums import InputType, GamepadKey
from src.input.classes import InputBinding
from src.application.enums import GameAction


GAMEPAD_ACTION_MAP: dict[GameAction, InputBinding] = {
    GameAction.CONFIRM: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.A),
    GameAction.CONFIRM_TEAM: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.START),
    GameAction.LIST_TEAMS: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.Y),
    GameAction.KICK_OFF: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.A),
    GameAction.COMMANDER_MODE: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.DPAD_DOWN),
    GameAction.C_CAMERA: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.RB),
    GameAction.SKIP: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.Y),
    GameAction.UP: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.DPAD_UP),
    GameAction.DOWN: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.DPAD_DOWN),
    GameAction.LEFT: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.DPAD_LEFT),
    GameAction.RIGHT: InputBinding(InputType.GAMEPAD_BUTTON, GamepadKey.DPAD_RIGHT),
}
