import sys
import time

from src.application.enums import SystemOS, GameAction
from src.input.providers import BaseInputProvider, InputProviderFactory

from src.input.enums import InputType, GamepadKey, InputMode
from src.input.mappings import GAMEPAD_ACTION_MAP


@InputProviderFactory.register(SystemOS.LINUX, InputMode.GAMEPAD)
class LinuxEvdevProvider(BaseInputProvider):
    def __init__(self):
        self.action_map = GAMEPAD_ACTION_MAP
        
        if sys.platform != 'linux':
            raise RuntimeError()

        from src.input.mappings import EVDEV_KEY_MAP
        from evdev import UInput, ecodes as e
        
        self.e = e
        self.EVDEV_KEY_MAP = EVDEV_KEY_MAP
        
        capabilities = {
            e.EV_KEY: [
                e.BTN_SOUTH, e.BTN_EAST, e.BTN_NORTH, e.BTN_WEST,
                e.BTN_START, e.BTN_SELECT,
                e.BTN_TL, e.BTN_TR,
                e.BTN_DPAD_UP, e.BTN_DPAD_DOWN,
                e.BTN_DPAD_LEFT, e.BTN_DPAD_RIGHT,
            ],
            e.EV_ABS: [
                (e.ABS_Z, (0, 255, 0, 0)),
                (e.ABS_RZ, (0, 255, 0, 0)),
            ]
        }

        self.ui = UInput(capabilities, name='Custom Gamepad')

    def press(self, action: GameAction):
        binding = self._resolve_gameaction(action)
        key = GamepadKey(binding.key)
        gamepad_input = self.EVDEV_KEY_MAP[key]

        if binding.type == InputType.GAMEPAD_BUTTON:
            self.ui.write(self.e.EV_KEY, gamepad_input.button, 1)
            self.ui.syn()

            time.sleep(0.1)

            self.ui.write(self.e.EV_KEY, gamepad_input.button, 0)
            self.ui.syn()

        elif binding.type == InputType.GAMEPAD_TRIGGER:
            gamepad_input.trigger(self.ui, gamepad_input.intensity)
            self.ui.syn()

            time.sleep(0.1)

            gamepad_input.trigger(self.ui, 0)
            self.ui.syn()

    def hold(self, action: GameAction, duration_seconds: float):
        binding = self._resolve_gameaction(action)
        key = GamepadKey(binding.key)
        gamepad_input = self.EVDEV_KEY_MAP[key]

        if binding.type == InputType.GAMEPAD_BUTTON:
            self.ui.write(self.e.EV_KEY, gamepad_input.button, 1)
            self.ui.syn()

            time.sleep(duration_seconds)

            self.ui.write(self.e.EV_KEY, gamepad_input.button, 0)
            self.ui.syn()

        elif binding.type == InputType.GAMEPAD_TRIGGER:
            gamepad_input.trigger(self.ui, gamepad_input.intensity)
            self.ui.syn()

            time.sleep(duration_seconds)

            gamepad_input.trigger(self.ui, 0)
            self.ui.syn()
