try:
    from .game_action.gamepad_action_map import GAMEPAD_ACTION_MAP
    from .gamepads.vgamepad_map import VGAMEPAD_KEY_MAP
except Exception:
    pass

try:
    from .game_action.desktop_action_map import DESKTOP_ACTION_MAP
    from .gamepads.evdev_map import EVDEV_KEY_MAP
except Exception:
    pass
