import time
import pyautogui
from src.enums.key import Key


def key_hold(key: Key, seconds: float):
    """
    Segura uma tecla por X segundos e solta.
    """
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
