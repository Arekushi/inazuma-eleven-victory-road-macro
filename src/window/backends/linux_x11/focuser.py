import time
import subprocess

from src.window.backends.linux_x11 import LinuxX11WindowFinder


class LinuxX11WindowFocuser:

    @staticmethod
    def focus_window(title: str, wait_after: float = 0.3) -> bool:
        window = LinuxX11WindowFinder.get_by_title(title)

        if window is None:
            return False

        if window.isMinimized:
            window.restore()

        try:
            window.activate()
        except Exception:
            subprocess.run(['wmctrl', '-a', title])
        
        time.sleep(wait_after)
        return True
