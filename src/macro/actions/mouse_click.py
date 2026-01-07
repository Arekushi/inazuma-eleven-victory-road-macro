import pyautogui
from src.enums import MouseButton


def mouse_click(x=None, y=None, button = MouseButton.LEFT):
    if x is not None and y is not None:
        pyautogui.click(x=x, y=y, button=button.value)
    else:
        pyautogui.click(button=button)
