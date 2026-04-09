from abc import ABC, abstractmethod
from src.input.classes import InputBinding


class PressCapability(ABC):

    @abstractmethod
    def press(self, binding: InputBinding):
        pass

    @abstractmethod
    def hold(self, binding: InputBinding, duration_seconds: float):
        pass
