from src.window.dataclasses import WindowRect
from src.window.interfaces import BaseWindowBackend
from src.window.backends.windows import (
    WindowsOSWindowFinder,
    WindowsOSWindowFocuser
)
from src.window.enums import WindowingSys
from src.application.enums import SystemOS
from src.window.backends import WindowBackendRegistry


@WindowBackendRegistry.register(SystemOS.WINDOWS, WindowingSys.DESKTOP_WINDOW_MANAGER)
class WindowsOSBackend(BaseWindowBackend):    
    def find_window(self, title: str):
        return WindowsOSWindowFinder.get_by_title(title)

    def focus(self, title: str, wait_after: float = 0.3) -> bool:
        return WindowsOSWindowFocuser.focus(title, wait_after)

    def get_window_rect(self, title: str) -> WindowRect:
        return WindowsOSWindowFinder.get_window_rect(title)
