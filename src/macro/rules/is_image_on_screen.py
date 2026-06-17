from pathlib import Path

from config import settings
from typing import Optional
from config.paths import Paths
from src.application.enums import FileExt

from src.vision import exists
from src.vision.dataclasses import Region
from src.window.backends import WindowBackendResolver


def is_image_on_screen(
    image_name: str,
    region: Optional[Region],
    confidence=0.9
) -> bool:
    image_path = Path(Paths.ASSETS / f'{image_name}.{FileExt.PNG}').resolve()
    window_rect = WindowBackendResolver.resolve().get_window_rect(settings.APP.window_name)
    
    try:
        result = exists(
            image_name=image_path,
            region=region,
            window_rect=window_rect,
            confidence=confidence,
        )
        
        return result
    except Exception as e:
        print(e)
        return False
