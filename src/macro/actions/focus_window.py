from src.window import WindowController


def focus_window(title_contains: str, wait_after=0.3) -> bool:
    try:
        WindowController.focus_window(title_contains, wait_after)
        return True
    except Exception:
        return False
