from dataclasses import dataclass
from typing import List, Optional, Any


@dataclass(frozen=True)
class CallbackNode:
    name: str
    args: List[Any]


@dataclass(frozen=True)
class RuleNode:
    condition: CallbackNode
    actions: List[CallbackNode]
    goto: Optional[str]
    interval: Optional[float]


@dataclass
class StepNode:
    name: Optional[str]
    actions: List[CallbackNode]
    label: Optional[str]
    delay: Optional[float]
    timeout: Optional[float]
    goto: Optional[str]
    rules: List[RuleNode]
    repeat: Optional[int]


@dataclass
class PipelineNode:
    steps: List[StepNode]
