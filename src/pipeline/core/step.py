from typing import Callable, Iterable, Optional

from src.pipeline.helpers import with_context
from src.pipeline.classes import PipelineContext
from src.pipeline.core import ConditionRule


class Step:
    def __init__(
        self,
        name,
        label: str | None = None,
        actions: Optional[Iterable[Callable[[Optional[PipelineContext]], None]]] = None,
        rules: list[ConditionRule] | None = None,
        goto: str | None = None,
        delay_after=0.0,
        delay_jitter: float = 0.0,
        timeout=30.0
    ):
        self.name = name 
        self.label = label
        
        self.rules = rules or []
        self.actions = actions or []
        
        self.goto = goto
        self.delay_after = delay_after
        self.delay_jitter = delay_jitter
        self.timeout = timeout

        self._start_time = None

    def execute_actions(self, pipeline_ctx: PipelineContext):
        for action in self.actions:
            action_with_ctx = with_context(action)
            action_with_ctx(pipeline_ctx)

    def reset(self):
        self._start_time = None
        
    @classmethod
    def from_spec(cls, spec):
        rules = [
            ConditionRule.from_spec(rule_spec)
            for rule_spec in spec.get('rules', [])
        ]
        
        return cls(
            name=spec['name'],
            label=spec.get('label'),
            actions=spec.get('actions'),
            rules=rules,
            goto=spec.get('goto'),
            delay_after=spec.get('delay_after', 0.0),
            delay_jitter=spec.get('delay_jitter', 0.0),
            timeout=spec.get('timeout', float('inf'))
        )
    
    @property
    def is_watcher(self):
        return bool(self.rules)
