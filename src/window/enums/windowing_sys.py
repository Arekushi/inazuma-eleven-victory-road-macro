from enum import Enum


class WindowingSys(Enum):
    X11 = 'x11'
    WAYLAND = 'wayland'
    XWAYLAND = 'xwayland'
    DESKTOP_WINDOW_MANAGER = 'desktop-window-manager'
