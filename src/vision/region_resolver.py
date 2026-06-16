from src.vision import (
    scale_region,
    to_global_region,
    resolve_anchored_region
)
from src.vision.dataclasses import Region
from src.window.dataclasses import WindowContext


class RegionResolver:
    def __init__(self, window_ctx: WindowContext):
        self.window_ctx = window_ctx

    def resolve(self, region) -> Region:
        region = scale_region(region)
        region = to_global_region(self.window_ctx.rect, region)
        region = resolve_anchored_region(region, self.window_ctx.rect.width)
        return region
