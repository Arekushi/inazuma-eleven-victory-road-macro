import time
import pydirectinput

from src.enums import Key


def key_hold(key: Key, seconds: float):    
    try:
        pydirectinput.keyDown(key)
        time.sleep(seconds)
    finally:
        pydirectinput.keyUp(key)
