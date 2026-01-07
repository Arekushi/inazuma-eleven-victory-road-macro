import time
import ctypes
import pygetwindow as gw
import win32gui
import win32process
import win32api

user32 = ctypes.windll.user32

def focus_window(title_contains: str, wait_after=0.3) -> bool:
    windows = gw.getWindowsWithTitle(title_contains)
    if not windows:
        return False

    window = windows[0]
    hwnd = window._hWnd

    fg_hwnd = win32gui.GetForegroundWindow()

    fg_thread, _ = win32process.GetWindowThreadProcessId(fg_hwnd)
    target_thread, _ = win32process.GetWindowThreadProcessId(hwnd)
    current_thread = win32api.GetCurrentThreadId()

    user32.AttachThreadInput(fg_thread, current_thread, True)
    user32.AttachThreadInput(target_thread, current_thread, True)

    if win32gui.IsIconic(hwnd):
        win32gui.ShowWindow(hwnd, 9)

    win32gui.SetForegroundWindow(hwnd)
    win32gui.BringWindowToTop(hwnd)
    win32gui.SetActiveWindow(hwnd)

    user32.AttachThreadInput(fg_thread, current_thread, False)
    user32.AttachThreadInput(target_thread, current_thread, False)

    time.sleep(wait_after)
    return True
