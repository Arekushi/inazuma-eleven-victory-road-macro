import pyautogui
from pathlib import Path
from typing import Optional, Tuple


Region = Tuple[int, int, int, int]


def is_image_on_screen(
    image_path,
    confidence=0.9,
    region: Optional[Region] = None,
    grayscale: bool = True
) -> bool:    
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
