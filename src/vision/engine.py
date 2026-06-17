from typing import Optional

from src.vision import (
    capture_screenshot,
    load_template,
    scale_template,
    match,
    RegionTransformer
)
from src.vision.dataclasses import Region
from src.window.dataclasses import WindowRect


def exists(
    image_name: str,
    region: Optional[Region],
    window_rect: WindowRect,
    confidence: float = 0.9
) -> bool:
    template = load_template(image_name)
    template = scale_template(template)
    
    transformed_region = RegionTransformer.transform(region, window_rect)
    screenshot = capture_screenshot(transformed_region)
    
    return match(screenshot, template, confidence).exists
