import pydirectinput

from src.enums import Key


def key_press(key: Key):
    pydirectinput.press([key])
