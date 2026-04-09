from src.input.enums import InputType, KeyboardKey, MouseButton
from src.input.classes import InputBinding
from src.application.enums import GameAction


DESKTOP_ACTION_MAP: dict[GameAction, InputBinding] = {
    GameAction.CONFIRM: InputBinding(InputType.KEYBOARD, KeyboardKey.ENTER),
    GameAction.CONFIRM_TEAM: InputBinding(InputType.KEYBOARD, KeyboardKey.ALT),
    GameAction.LIST_TEAMS: InputBinding(InputType.KEYBOARD, KeyboardKey.V),
    GameAction.KICK_OFF: InputBinding(InputType.MOUSE, MouseButton.LEFT),
    GameAction.COMMANDER_MODE: InputBinding(InputType.KEYBOARD, KeyboardKey.U),
    GameAction.C_CAMERA: InputBinding(InputType.KEYBOARD, KeyboardKey.C),
    GameAction.SKIP: InputBinding(InputType.KEYBOARD, KeyboardKey.V),
    GameAction.UP: InputBinding(InputType.KEYBOARD, KeyboardKey.UP),
    GameAction.DOWN: InputBinding(InputType.KEYBOARD, KeyboardKey.DOWN),
    GameAction.LEFT: InputBinding(InputType.KEYBOARD, KeyboardKey.LEFT),
    GameAction.RIGHT: InputBinding(InputType.KEYBOARD, KeyboardKey.RIGHT),
}
