from src.input.classes import InputResolver
from src.input.controllers import GamepadController, DesktopController
from src.input.mappings.game_action import GAMEPAD_ACTION_MAP, DESKTOP_ACTION_MAP
from src.input.classes import InputBundle
from src.input.enums import InputMode


INPUT_PROVIDERS = {
    InputMode.GAMEPAD: lambda: InputBundle(
        controller=GamepadController(),
        resolver=InputResolver(GAMEPAD_ACTION_MAP),
    ),
    InputMode.DESKTOP: lambda: InputBundle(
        controller=DesktopController(),
        resolver=InputResolver(DESKTOP_ACTION_MAP),
    ),
}
