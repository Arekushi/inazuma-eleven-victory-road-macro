from config import settings
from src.window.backends import WindowBackendResolver


def get_screen_size():
    rect = WindowBackendResolver.resolve().get_window_rect(settings.APP.window_name)
    return rect.width, rect.height


def get_ui_scale():
    _, screen_height = get_screen_size()
    return screen_height / int(settings.APP.base_height)
