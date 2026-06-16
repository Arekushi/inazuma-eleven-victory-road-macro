from dataclasses import dataclass
from src.vision.enums import HorizontalAnchor


@dataclass
class Region:
    x: int
    y: int
    width: int
    height: int
    horizontal_anchor: HorizontalAnchor = HorizontalAnchor.LEFT
    
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.width
        yield self.height
