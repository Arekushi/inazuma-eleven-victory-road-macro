from config import settings
from src.window import WindowContextResolver


def get_screen_size():
    ctx = WindowContextResolver.resolve(settings.APP.window_name)
    return ctx.rect.width, ctx.rect.height


def get_ui_scale():
    _, screen_height = get_screen_size()
    return screen_height / int(settings.APP.base_height)
