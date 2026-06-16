from dataclasses import dataclass
from cv2.typing import Point


@dataclass
class MatchResult:
    exists: bool
    max_loc: Point
    max_val: float
