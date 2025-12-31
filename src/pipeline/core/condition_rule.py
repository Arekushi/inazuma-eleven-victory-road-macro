import time
from typing import Callable, Iterable, Optional

from src.pipeline.helpers import with_context
from src.pipeline.classes import PipelineContext, StepNavigator


class ConditionRule:
    def __init__(
        self,
        when: Callable[[Optional[PipelineContext]], None],
        *,
        actions: Optional[Iterable[Callable[[Optional[PipelineContext]], None]]] = None,
        goto: str | None = None,
        interval: float | None = None
    ):
        self.when = when
        self.actions = actions or []
        self.goto = goto
        self.interval = interval

        self._last_check = 0.0
    
    def execute_actions(self, pipeline_ctx: PipelineContext):
        for action in self.actions:
            action_with_ctx = with_context(action)
            action_with_ctx(pipeline_ctx)

    def can_evaluate(self):
        if self.interval is None:
            return True

        now = time.time()
        if now - self._last_check >= self.interval:
            self._last_check = now
            return True

        return False

    def evaluate(
        self,
        pipeline_ctx: PipelineContext,
        step_nav: StepNavigator
    ) -> bool:
        if not self.can_evaluate():
            return False

        when_with_ctx = with_context(self.when)
        if not when_with_ctx(pipeline_ctx):
            return False
        
        self.execute_actions(pipeline_ctx)
        step_nav.go_to(self.goto)

        return True

    @classmethod
    def from_spec(cls, spec):
        return cls(
            when=spec['when'],
            actions=spec.get('actions', []),
            goto=spec.get('goto'),
            interval=spec.get('interval'),
        )
