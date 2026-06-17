import pywinctl as pwc

from src.window.dataclasses import WindowRect


class WindowsOSWindowFinder:
    
    @classmethod
    def get_by_title(cls, title: str):
        title = title.lower()

        for window in pwc.getAllWindows():
            if window.title.casefold().find(title.casefold()) != -1:
                return window

        raise Exception('Window not found')
    
    @classmethod
    def get_window_rect(cls, title: str) -> WindowRect:
        window = cls.get_by_title(title)
        
        return WindowRect(
            left=window.left,
            top=window.top,
            width=window.width,
            height=window.height,
            right=window.right,
            bottom=window.bottom,
        )
