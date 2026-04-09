import pyautogui


def is_black_screen():
    pixel = pyautogui.pixel(100, 100)
    return pixel == (0, 0, 0)
