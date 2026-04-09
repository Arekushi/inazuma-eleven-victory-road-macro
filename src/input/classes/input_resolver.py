from src.application.enums import GameAction
from src.input.classes import InputBinding


class InputResolver:

    def __init__(self, action_map):
        self.action_map = action_map

    def resolve(self, action: GameAction) -> InputBinding:
        return self.action_map[action]

