from config import settings
from src.dsl.specs import CallableSpec, ArgumentSpec
from src.application.enums import GameAction

from src.macro.actions import (
    focus_window,
    hold,
    press,
    stop_pipeline
)


ACTION_REGISTRY: dict[str, CallableSpec] = {
    'focus_window': CallableSpec(
        name='focus',
        factory=lambda: lambda ctx: focus_window(settings.APP.window_name),
    ),
    'press': CallableSpec(
        name='press',
        factory=lambda action: lambda ctx: press(ctx, action),
        arguments=[
            ArgumentSpec(
                name='action',
                type=GameAction
            )
        ]
    ),
    'hold': CallableSpec(
        name='hold',
        factory=lambda action, seconds: lambda ctx: hold(ctx, action, seconds),
        arguments=[
            ArgumentSpec(
                name='action',
                type=GameAction
            ),
            ArgumentSpec(
                name='seconds',
                type=float
            )
        ]
    ),
    'stop': CallableSpec(
        name='stop',
        factory=lambda: lambda ctx: stop_pipeline(),
    ),
}
