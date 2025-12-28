import time
import pygetwindow as gw

def focus_window(title_contains, wait_after=0.3):
    """
    Dá foco em uma janela cujo título contenha `title_contains`.

    Retorna:
        True  -> janela já estava em foco ou foco aplicado com sucesso
        False -> janela não encontrada
    """

    windows = gw.getWindowsWithTitle(title_contains)

    if not windows:
        return False

    window = windows[0]

    active = gw.getActiveWindow()
    if active and active._hWnd == window._hWnd:
        return True

    if window.isMinimized:
        window.restore()
        time.sleep(0.1)

    window.activate()
    time.sleep(wait_after)

    return True
