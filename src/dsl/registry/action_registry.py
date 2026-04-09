from src.dsl.specs import CallableSpec, ArgumentSpec
from src.application.enums import GameAction

from src.macro.actions import (
    focus_window,
    hold,
    press,
    log_line_break,
    send_notification,
    stop_pipeline,
)


ACTION_REGISTRY: dict[str, CallableSpec] = {
    'focus': CallableSpec(
        name='focus',
        factory=lambda title: lambda ctx: focus_window(title),
        arguments=[
            ArgumentSpec(
                name='title',
                type=str
            )
        ]
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
    'notify': CallableSpec(
        name='notify',
        factory=lambda title, msg: lambda ctx: send_notification(title, msg),
        arguments=[
            ArgumentSpec(
                name='title',
                type=str
            ),
            ArgumentSpec(
                name='msg',
                type=str
            ),
        ]
    ),
    'stop': CallableSpec(
        name='stop',
        factory=lambda: lambda ctx: stop_pipeline(),
    ),
    'log_line_break': CallableSpec(
        name='log_line_break',
        factory=lambda: lambda ctx: log_line_break(ctx)
    ),
}
