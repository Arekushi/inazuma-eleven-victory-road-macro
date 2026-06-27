from src.input.exceptions import InputTypeUnavailableError
from src.input.providers import BaseInputProvider
from src.application.enums import GameAction


class InputController():
    def __init__(self, provider: BaseInputProvider):
        self.provider = provider
    
    def press(self, action: GameAction):
        try:
            self.provider.press(action)
        except KeyError:
            raise InputTypeUnavailableError()

    def hold(self, action: GameAction, duration_seconds: float):
        try:
            self.provider.hold(action, duration_seconds)
        except KeyError:
            raise InputTypeUnavailableError()
