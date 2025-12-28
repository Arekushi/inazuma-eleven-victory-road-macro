from typing import Callable, Iterable, TypedDict
from typing_extensions import NotRequired
from src.pipeline.condition_rule import ConditionRule


class StepSpec(TypedDict):
    name: str
    label: NotRequired[str]

    actions: NotRequired[Iterable[Callable]]
    rules: NotRequired[list[ConditionRule]]

    goto: NotRequired[str]

    delay_after: NotRequired[float]
    delay_jitter: NotRequired[float]

    timeout: NotRequired[float]
    on_timeout: NotRequired[str | int]
