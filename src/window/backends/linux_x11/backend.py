from src.window.dataclasses import WindowRect
from src.window.interfaces import BaseWindowBackend
from src.window.backends.linux_x11 import (
    LinuxX11WindowFinder,
    LinuxX11WindowFocuser
)
from src.window.enums import WindowingSys
from src.application.enums import SystemOS
from src.window.backends import WindowBackendRegistry


@WindowBackendRegistry.register(SystemOS.LINUX, WindowingSys.X11)
class LinuxX11Backend(BaseWindowBackend):    
    def find_window(self, title: str):
        return LinuxX11WindowFinder.get_by_title(title)

    def focus(self, title: str, wait_after: float = 0.3) -> bool:
        return LinuxX11WindowFocuser.focus(title, wait_after)

    def get_window_rect(self, title: str) -> WindowRect:
        return LinuxX11WindowFinder.get_window_rect(title)
