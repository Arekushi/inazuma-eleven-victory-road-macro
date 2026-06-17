from src.window.backends import WindowBackendResolver


def focus_window(title_contains: str, wait_after=0.3) -> bool:
    return WindowBackendResolver.resolve().focus(title_contains, wait_after)
