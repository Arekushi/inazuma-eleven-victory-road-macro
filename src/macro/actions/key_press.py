import pyautogui
from src.enums import Key


def key_press(key: Key):
    pyautogui.press([key])
