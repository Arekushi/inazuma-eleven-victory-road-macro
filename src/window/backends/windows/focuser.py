import time


class WindowsOSWindowFocuser:
    
    @staticmethod
    def focus(title: str, wait_after: float = 0.3) -> bool:
        import pygetwindow as gw
        import win32gui
        import win32api
        import win32con

        def clear_input_state():
            for key in range(256):
                win32api.GetAsyncKeyState(key)

        def release_mouse():
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

        windows = gw.getWindowsWithTitle(title)

        if not windows:
            return False

        hwnd = windows[0]._hWnd

        if win32gui.GetForegroundWindow() == hwnd:
            return True

        release_mouse()
        clear_input_state()

        time.sleep(0.05)

        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
        win32gui.SetForegroundWindow(hwnd)
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)

        time.sleep(wait_after)
        return True
