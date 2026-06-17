import os

from src.window.enums import WindowingSys


class WindowingSystemDetector:

    @staticmethod
    def detect() -> WindowingSys | None:
        if os.name == 'nt':
            return WindowingSys.DESKTOP_WINDOW_MANAGER

        session_type = os.environ.get('XDG_SESSION_TYPE')

        if session_type == 'wayland':
            if os.environ.get('DISPLAY'):
                return WindowingSys.XWAYLAND

            return WindowingSys.WAYLAND

        if session_type == 'x11':
            return WindowingSys.X11

        return None
