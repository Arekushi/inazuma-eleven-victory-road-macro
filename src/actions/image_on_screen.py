from pathlib import Path
import pyautogui
from typing import Optional, Tuple


Region = Tuple[int, int, int, int]


def image_on_screen(
    image_path,
    confidence=0.9,
    region: Optional[Region] = None,
    grayscale: bool = True
):
    """
    Verifica se uma imagem está presente na tela.
    Retorna True ou False.
    """
    
    if isinstance(image_path, Path):
        image_path = str(image_path.resolve())
    
    try:
        return pyautogui.locateOnScreen(
            image_path,
            confidence=confidence,
            region=region,
            grayscale=grayscale
        ) is not None
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        print(e)
        return False
