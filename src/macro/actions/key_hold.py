import time
import pyautogui

from src.enums import Key


def key_hold(key: Key, seconds: float):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
