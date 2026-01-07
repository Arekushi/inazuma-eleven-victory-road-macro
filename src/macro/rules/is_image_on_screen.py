import pyautogui
from pathlib import Path
from typing import Optional, Tuple
from config.paths import Paths
from src.enums import Language, FileExt


Region = Tuple[int, int, int, int]


def is_image_on_screen(
    image_name: str,
    language = Language.PT_BR,
    confidence=0.9,
    region: Optional[Region] = None,
    grayscale: bool = True
) -> bool:
    image_path = str((Paths.match_assets(language) / f'{image_name}.{FileExt.PNG}').resolve())
    
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
