import time
import pydirectinput

from src.input.enums.input_type import InputType
from src.input.classes import InputBinding
from src.input.abc import PressCapability


class DesktopController(PressCapability):
    def press(self, binding: InputBinding):
        if binding.type == InputType.KEYBOARD:
            pydirectinput.press([binding.key.value])
        elif binding.type == InputType.MOUSE:
            pydirectinput.click(button=binding.key.value)

    def hold(self, binding: InputBinding, duration_seconds: float):
        if binding.type == InputType.KEYBOARD:
            try:
                pydirectinput.keyDown(binding.key.value)
                time.sleep(duration_seconds)
            finally:
                pydirectinput.keyUp(binding.key.value)
