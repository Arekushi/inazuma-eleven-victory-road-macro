import mss
import pywinctl as pwc
from pywinctl import Window

from typing import Optional, Tuple
from src.window.dataclasses import WindowContext, WindowRect


class WindowContextResolver:
    _monitors = None

    @classmethod
    def resolve(cls, title: str) -> Optional[WindowContext]:
        window = cls.get_window_by_title(title)

        if window is None:
            return None

        rect = cls._get_window_rect(window)
        monitor_index = cls._find_monitor_index_by_window(rect)

        return WindowContext(rect, monitor_index)

    @staticmethod
    def get_window_by_title(title: str) -> Optional[Window]:
        title = title.lower()

        for window in pwc.getAllWindows():
            try:
                if window.title.casefold().find(title.casefold()) != -1:
                    return window
            except Exception:
                pass

        return None

    @classmethod
    def _get_monitors(cls):
        if cls._monitors is None:
            with mss.mss() as sct:
                cls._monitors = sct.monitors[1:]

        return cls._monitors

    @staticmethod
    def _get_window_rect(window) -> WindowRect:
        return WindowRect(
            left=window.left,
            top=window.top,
            width=window.width,
            height=window.height,
            right=window.right,
            bottom=window.bottom,
        )

    @staticmethod
    def _get_window_center(rect: WindowRect) -> Tuple[int, int]:
        return (
            rect.left + rect.width // 2,
            rect.top + rect.height // 2,
        )

    @classmethod
    def _find_monitor_index_by_window(cls, rect: WindowRect) -> int:
        cx, cy = cls._get_window_center(rect)

        for index, monitor in enumerate(cls._get_monitors()):
            if (
                monitor['left'] <= cx < monitor['left'] + monitor['width']
                and monitor['top'] <= cy < monitor['top'] + monitor['height']
            ):
                return index

        return 0
