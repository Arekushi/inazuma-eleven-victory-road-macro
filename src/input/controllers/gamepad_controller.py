import time
import vgamepad as vg

from src.input.enums import InputType, GamepadKey
from src.input.classes import InputBinding
from src.input.abc import PressCapability
from src.input.mappings import GAMEPAD_KEY_MAP


class GamepadController(PressCapability):
    def __init__(self):
        self.gamepad = vg.VX360Gamepad()

    def press(self, binding: InputBinding):
        key = GamepadKey(binding.key)
        input_data = GAMEPAD_KEY_MAP[key]

        if binding.type == InputType.GAMEPAD_BUTTON:
            self.gamepad.press_button(input_data.button)
            self.gamepad.update()
            time.sleep(0.1)
            self.gamepad.release_button(input_data.button)
            self.gamepad.update()

        elif binding.type == InputType.GAMEPAD_TRIGGER:
            input_data.trigger(self.gamepad, input_data.intensity)
            self.gamepad.update()
            time.sleep(0.1)
            input_data.trigger(self.gamepad, 0)
            self.gamepad.update()

    def hold(self, binding: InputBinding, duration: float):
        key = GamepadKey(binding.key)
        input_data = GAMEPAD_KEY_MAP[key]
        
        if binding.type == InputType.GAMEPAD_BUTTON:
            self.gamepad.press_button(input_data.button)
            self.gamepad.update()
            time.sleep(duration)
            self.gamepad.release_button(input_data.button)
            self.gamepad.update()

        elif binding.type == InputType.GAMEPAD_TRIGGER:
            input_data.trigger(self.gamepad, input_data.intensity)
            self.gamepad.update()
            time.sleep(duration)
            input_data.trigger(self.gamepad, 0)
            self.gamepad.update()
