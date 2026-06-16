import cv2
from src.vision.dataclasses import MatchResult


def match(
    screenshot,
    template,
    confidence: float = 0.9
) -> MatchResult:
    if screenshot.shape[-1] == 4:
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    if template.shape[-1] == 4:
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)

    screen_g = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    template_g = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(
        screen_g,
        template_g,
        cv2.TM_CCOEFF_NORMED
    )

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    return MatchResult(
        max_val >= confidence,
        max_loc,
        max_val
    )
