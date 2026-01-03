import pyautogui
from src.enums import Key


def key_press(key: Key):
    """
    Pressiona e solta uma tecla.
    Ex: 'a', 'enter', 'esc', 'f1'
    """
    pyautogui.press([key])
