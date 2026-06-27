from src.input.providers import BaseInputProvider
from src.application.enums import GameAction


class InputController():
    def __init__(self, provider: BaseInputProvider):
        self.provider = provider
    
    def press(self, action: GameAction):
        self.provider.press(action)

    def hold(self, action: GameAction, duration_seconds: float):
        self.provider.hold(action, duration_seconds)
