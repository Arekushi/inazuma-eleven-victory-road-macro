from abc import ABC, abstractmethod
from src.window.dataclasses import WindowRect


class BaseWindowBackend(ABC):

    @abstractmethod
    def find_window(self, title: str):
        pass

    @abstractmethod
    def focus(self, title: str, wait_after: float = 0.3) -> bool:
        pass

    @abstractmethod
    def get_window_rect(self, title: str) -> WindowRect:
        pass
