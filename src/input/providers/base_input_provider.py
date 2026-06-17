from abc import ABC, abstractmethod

from src.input.dataclasses import InputBinding
from src.application.enums import GameAction


class BaseInputProvider(ABC):
    
    def __init__(self):
        self.action_map = None

    @abstractmethod
    def press(self, action: GameAction):
        pass

    @abstractmethod
    def hold(self, action: GameAction, duration_seconds: float):
        pass
    
    def _resolve_gameaction(self, action: GameAction) -> InputBinding:
        return self.action_map[action]
