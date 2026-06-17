import time

from src.application import SystemOSDetector
from src.application.enums import SystemOS, GameAction
from src.input.enums import InputType, InputMode
from src.input.providers import BaseInputProvider, InputProviderFactory
from src.input.mappings import DESKTOP_ACTION_MAP


@InputProviderFactory.register(SystemOS.WINDOWS, InputMode.DESKTOP)
class WindowsDesktopProvider(BaseInputProvider):
    
    def __init__(self):
        if SystemOSDetector.detect() != SystemOS.WINDOWS:
            raise RuntimeError()
        
        import pydirectinput as pdi
        
        self.pdi = pdi
        self.action_map = DESKTOP_ACTION_MAP
    
    def press(self, action: GameAction):
        binding = self._resolve_gameaction(action)
        
        if binding.type == InputType.KEYBOARD:
            self.pdi.press([binding.key.value])
        elif binding.type == InputType.MOUSE:
            self.pdi.click(button=binding.key.value)

    def hold(self, action: GameAction, duration_seconds: float):
        binding = self._resolve_gameaction(action)
        
        if binding.type == InputType.KEYBOARD:
            try:
                self.pdi.keyDown(binding.key.value)
                time.sleep(duration_seconds)
            finally:
                self.pdi.keyUp(binding.key.value)
