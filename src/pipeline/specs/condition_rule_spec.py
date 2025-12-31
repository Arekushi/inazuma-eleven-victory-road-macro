from typing import Callable, TypedDict
from typing_extensions import NotRequired


class ConditionRuleSpec(TypedDict):
    when: Callable[[], bool]

    actions: NotRequired[list[Callable]]

    goto: NotRequired[str]
    interval: NotRequired[float]
