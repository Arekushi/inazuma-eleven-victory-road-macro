import pyautogui
from pywinauto.keyboard import send_keys
from src.enums import Key

def key_press(key: Key):
    """
    Pressiona e solta uma tecla.
    Ex: 'a', 'enter', 'esc', 'f1'
    """
    pyautogui.press([key])
