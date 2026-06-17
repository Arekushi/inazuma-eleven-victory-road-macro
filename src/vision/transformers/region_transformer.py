from config import settings
from src.vision.screen import get_ui_scale, get_screen_size
from src.vision.dataclasses import Region
from src.vision.enums import HorizontalAnchor
from src.window.dataclasses import WindowRect


class RegionTransformer:

    @classmethod
    def transform(
        cls,
        region: Region,
        window_rect: WindowRect,
    ) -> Region:

        region = cls.scale(region)
        region = cls.to_global(region, window_rect)
        region = cls.resolve_anchor(region, window_rect.width)

        return region

    @classmethod
    def scale(cls, region: Region, safe=True) -> Region:
        scale = get_ui_scale()

        x, y, width, height = region

        result = Region(
            round(x * scale),
            round(y * scale),
            round(width * scale),
            round(height * scale),
            region.horizontal_anchor
        )

        if safe:
            return cls.safe_region(result)

        return result

    @classmethod
    def safe_region(cls, region: Region) -> Region:
        x, y, width, height = region
        screen_width, screen_height = get_screen_size()

        x = max(0, x)
        y = max(0, y)

        right = min(screen_width, x + width)
        bottom = min(screen_height, y + height)

        return Region(
            x,
            y,
            max(0, right - x),
            max(0, bottom - y),
            region.horizontal_anchor
        )

    @classmethod
    def to_global(
        cls,
        region: Region,
        window_rect: WindowRect,
    ) -> Region:
        x, y, width, height = region

        return Region(
            window_rect.left + x,
            window_rect.top + y,
            width,
            height,
            region.horizontal_anchor
        )

    @classmethod
    def resolve_anchor(
        cls,
        region: Region,
        screen_width: int
    ) -> Region:
        scale = get_ui_scale()
        x, y, width, height = region

        if region.horizontal_anchor == HorizontalAnchor.RIGHT:
            scaled_base_width = int(settings.APP.base_width) * scale
            right_margin = scaled_base_width - x
            x = round(screen_width - right_margin)

        elif region.horizontal_anchor == HorizontalAnchor.CENTER:
            scaled_base_width = int(settings.APP.base_width) * scale
            offset = (screen_width - scaled_base_width) / 2
            x = round(x + offset)

        return Region(
            x,
            y,
            width,
            height,
            region.horizontal_anchor
        )
