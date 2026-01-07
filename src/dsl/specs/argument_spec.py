from typing import Any, Callable, Type
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentSpec:
    name: str
    type: Type | tuple[Type, ...]
    optional: bool = False
    validator: Callable[[Any], bool] | None = None
