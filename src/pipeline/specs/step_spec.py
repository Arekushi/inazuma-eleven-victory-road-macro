from typing import Iterable, TypedDict
from typing_extensions import NotRequired

from src.pipeline.helpers import ContextCallable
from src.pipeline.core import ConditionRule


class StepSpec(TypedDict):
    name: str
    label: NotRequired[str]

    actions: NotRequired[Iterable[ContextCallable]]
    rules: NotRequired[list[ConditionRule]]

    goto: NotRequired[str]

    delay_after: NotRequired[float]
    delay_jitter: NotRequired[float]

    timeout: NotRequired[float]
    on_timeout: NotRequired[str | int]
    repeat: NotRequired[int]
