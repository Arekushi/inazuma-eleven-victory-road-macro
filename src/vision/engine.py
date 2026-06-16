from typing import Optional

from src.vision import (
    capture_screenshot,
    load_template,
    scale_template,
    match,
    RegionResolver
)
from src.vision.dataclasses import Region
from src.window.dataclasses import WindowContext


def exists(
    image_name: str,
    region: Optional[Region],
    window_ctx: WindowContext,
    confidence: float = 0.9
) -> bool:
    region_resolver = RegionResolver(window_ctx)
    template = load_template(image_name)
    template = scale_template(template)
    
    region = region_resolver.resolve(region)
    screenshot = capture_screenshot(region)
    
    return match(screenshot, template, confidence).exists
