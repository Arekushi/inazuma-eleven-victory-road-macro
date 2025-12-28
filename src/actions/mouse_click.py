import pyautogui

def mouse_click(x=None, y=None, button="left"):
    """
    Clique do mouse.
    - Se x e y forem None, clica na posição atual.
    - button: left | right | middle
    """
    if x is not None and y is not None:
        pyautogui.click(x=x, y=y, button=button)
    else:
        pyautogui.click(button=button)
