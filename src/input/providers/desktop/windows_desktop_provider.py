import time
import pydirectinput

from src.application.enums import SystemOS, GameAction
from src.input.enums import InputType, InputMode
from src.input.providers import BaseInputProvider, InputProviderFactory
from src.input.mappings import DESKTOP_ACTION_MAP


@InputProviderFactory.register(SystemOS.WINDOWS, InputMode.DESKTOP)
class WindowsDesktopProvider(BaseInputProvider):
    
    def __init__(self):
        self.action_map = DESKTOP_ACTION_MAP
    
    def press(self, action: GameAction):
        binding = self._resolve_gameaction(action)
        
        if binding.type == InputType.KEYBOARD:
            pydirectinput.press([binding.key.value])
        elif binding.type == InputType.MOUSE:
            pydirectinput.click(button=binding.key.value)

    def hold(self, action: GameAction, duration_seconds: float):
        binding = self._resolve_gameaction(action)
        
        if binding.type == InputType.KEYBOARD:
            try:
                pydirectinput.keyDown(binding.key.value)
                time.sleep(duration_seconds)
            finally:
                pydirectinput.keyUp(binding.key.value)
