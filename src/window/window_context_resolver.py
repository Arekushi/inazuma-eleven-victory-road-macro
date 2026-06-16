import mss
import pygetwindow as gw
from pygetwindow import Win32Window
from typing import Optional, Tuple, List

from src.window.dataclasses import WindowContext, WindowRect


class WindowContextResolver:
    _monitors = None

    @classmethod
    def resolve(cls, title: str) -> Optional[WindowContext]:
        window = cls._get_window_by_title(title)

        if not window:
            return None

        rect = cls._get_window_rect(window)
        index = cls._find_monitor_index_for_window(rect)

        return WindowContext(rect, index)

    @classmethod
    def _get_monitors(cls):
        if cls._monitors is None:
            with mss.mss() as sct:
                cls._monitors = sct.monitors[1:]

        return cls._monitors

    @classmethod
    def _get_window_by_title(cls, title: str) -> Optional[Win32Window]:
        windows: List[Win32Window] = gw.getAllWindows()

        title = title.lower()

        for w in windows:
            if w.title and title in w.title.lower():
                return w

        return None

    @classmethod
    def _get_window_rect(cls, window: Win32Window) -> WindowRect:
        return WindowRect(
            left=window.left,
            top=window.top,
            width=window.width,
            height=window.height,
            right=window.left + window.width,
            bottom=window.top + window.height
        )

    @classmethod
    def _get_window_center(cls, rect: WindowRect) -> Tuple[int, int]:
        return (
            rect.left + rect.width // 2,
            rect.top + rect.height // 2,
        )

    @classmethod
    def _find_monitor_index_for_window(cls, rect: WindowRect) -> int:
        cx, cy = cls._get_window_center(rect)
        monitors = cls._get_monitors()

        for index, monitor in enumerate(monitors):
            if (
                monitor['left'] <= cx < monitor['left'] + monitor['width']
                and monitor['top'] <= cy < monitor['top'] + monitor['height']
            ):
                return index

        return 0
