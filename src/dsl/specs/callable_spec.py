from dataclasses import dataclass, field
from typing import Callable, List, Optional
from src.dsl.specs import ArgumentSpec


@dataclass(frozen=True)
class CallableSpec:
    name: str
    factory: Callable[..., Callable]
    arguments: Optional[List[ArgumentSpec]] = field(default_factory=list)
