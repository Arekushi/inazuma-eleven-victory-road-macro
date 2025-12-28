import time
from typing import Callable
from src.pipeline.flow_context import FlowContext
from src.pipeline.spec.condition_rule_spec import ConditionRuleSpec


class ConditionRule:
    def __init__(
        self,
        when: callable,
        *,
        actions: list[Callable],
        goto: str | None = None,
        interval: float | None = None
    ):
        self.when = when
        self.actions = actions or []
        self.goto = goto
        self.interval = interval

        self._last_check = 0.0
    
    def execute_actions(self):
        for action in self.actions:
            action()

    def can_evaluate(self):
        if self.interval is None:
            return True

        now = time.time()
        if now - self._last_check >= self.interval:
            self._last_check = now
            return True

        return False

    def evaluate(self, ctx: FlowContext) -> bool:
        if not self.can_evaluate():
            return False

        if not self.when():
            return False
        
        self.execute_actions()
        ctx.go_to(self.goto)

        return True

    @classmethod
    def from_spec(cls, spec: ConditionRuleSpec):
        return cls(
            when=spec['when'],
            actions=spec.get('actions', []),
            goto=spec.get('goto'),
            interval=spec.get('interval'),
        )
