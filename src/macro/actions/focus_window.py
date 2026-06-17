from src.window import WindowController


def focus_window(title_contains: str, wait_after=0.3) -> bool:
    return WindowController.focus_window(title_contains, wait_after)
