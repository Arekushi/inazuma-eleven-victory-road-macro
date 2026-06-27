import time

from src.application import SystemOSDetector
from src.application.enums import SystemOS, GameAction
from src.input.enums import InputType, GamepadKey, InputMode
from src.input.mappings import GAMEPAD_ACTION_MAP
from src.input.providers import BaseInputProvider, InputProviderFactory
from src.input.exceptions import InputTypeUnavailableError


@InputProviderFactory.register(SystemOS.WINDOWS, InputMode.GAMEPAD)
class WindowsVGamepadProvider(BaseInputProvider):
    def __init__(self):
        if SystemOSDetector.detect() != SystemOS.WINDOWS:
            raise RuntimeError()
        
        try:
            import vgamepad as vg
            from src.input.mappings.gamepads.vgamepad_map import VGAMEPAD_KEY_MAP
            
            self.gamepad = vg.VX360Gamepad()
            self.VGAMEPAD_KEY_MAP = VGAMEPAD_KEY_MAP
        except Exception:
            raise InputTypeUnavailableError()
        
        self.action_map = GAMEPAD_ACTION_MAP

    def press(self, action: GameAction):
        binding = self._resolve_gameaction(action)
        key = GamepadKey(binding.key)
        gamepad_input = self.VGAMEPAD_KEY_MAP[key]

        if binding.type == InputType.GAMEPAD_BUTTON:
            self.gamepad.press_button(gamepad_input.button)
            self.gamepad.update()
            
            time.sleep(0.1)
            
            self.gamepad.release_button(gamepad_input.button)
            self.gamepad.update()

        elif binding.type == InputType.GAMEPAD_TRIGGER:
            gamepad_input.trigger(self.gamepad, gamepad_input.intensity)
            self.gamepad.update()
            
            time.sleep(0.1)
            
            gamepad_input.trigger(self.gamepad, 0)
            self.gamepad.update()

    def hold(self, action: GameAction, duration: float):
        binding = self._resolve_gameaction(action)
        key = GamepadKey(binding.key)
        gamepad_input = self.VGAMEPAD_KEY_MAP[key]
        
        if binding.type == InputType.GAMEPAD_BUTTON:
            self.gamepad.press_button(gamepad_input.button)
            self.gamepad.update()
            
            time.sleep(duration)
            
            self.gamepad.release_button(gamepad_input.button)
            self.gamepad.update()

        elif binding.type == InputType.GAMEPAD_TRIGGER:
            gamepad_input.trigger(self.gamepad, gamepad_input.intensity)
            self.gamepad.update()
            
            time.sleep(duration)
            
            gamepad_input.trigger(self.gamepad, 0)
            self.gamepad.update()
