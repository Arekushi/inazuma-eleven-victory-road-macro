from src.enums import Key, MouseButton
from src.dsl.specs import CallableSpec, ArgumentSpec

from src.macro.actions import (
    focus_window,
    key_hold,
    key_press,
    log_line_break,
    mouse_click,
    register_spirit_opened,
    send_notification,
    stop_pipeline,
    goto_spirit
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
        factory=lambda key: lambda ctx: key_press(key),
        arguments=[
            ArgumentSpec(
                name='key',
                type=Key
            )
        ]
    ),
    'hold': CallableSpec(
        name='hold',
        factory=lambda key, seconds: lambda ctx: key_hold(key, seconds),
        arguments=[
            ArgumentSpec(
                name='key',
                type=Key
            ),
            ArgumentSpec(
                name='seconds',
                type=float
            )
        ]
    ),
    'click': CallableSpec(
        name='click',
        factory=lambda x, y, button=MouseButton.LEFT: lambda ctx: mouse_click(x, y, button),
        arguments=[
            ArgumentSpec(
                name='x',
                type=int
            ),
            ArgumentSpec(
                name='y',
                type=int
            ),
            ArgumentSpec(
                name='button',
                type=MouseButton,
                optional=True
            ),
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
    'register_spirit_opened': CallableSpec(
        name='register_spirit_opened',
        factory=lambda: lambda ctx: register_spirit_opened(ctx),
    ),
    'log_line_break': CallableSpec(
        name='log_line_break',
        factory=lambda: lambda ctx: log_line_break(ctx)
    ),
    'goto_spirit': CallableSpec(
        name='goto_spirit',
        factory=lambda sleep = 0.5:
            lambda ctx: goto_spirit(ctx, sleep),
        arguments=[
            ArgumentSpec(
                name='sleep',
                type=float,
                optional=True
            ),
        ]
    )
}
