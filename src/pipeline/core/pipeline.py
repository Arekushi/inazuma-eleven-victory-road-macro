from logging import Logger
import time
import random

from typing import Dict, List, Optional
from config import settings
from rich.console import Console

from src.pipeline.enums import PipelineEventType
from src.pipeline.exceptions import StopPipeline
from src.pipeline.classes import PipelineContext, StepNavigator, \
    PipelineObserver, PipelineEvent, PipelineSnapshot
from src.pipeline.core import Step


console = Console()


class Pipeline:
    def __init__(
        self,
        steps: List[Step],
        logger: Logger,
        max_loops: Optional[int] = None,
        context_data: Optional[dict] = None,
    ):
        self.steps = steps
        self.max_loops = max_loops
        self.current = 0
        self.loop_count = 0
        self.context = PipelineContext(
            initial_data=context_data,
            logger=logger
        )

        self._logger = logger
        self._observers: list[PipelineObserver] = []
        self._label_map = self._build_label_map()

    def run(self):
        self._emit(PipelineEventType.PIPELINE_START)

        try:
            while True:
                has_more_steps = self._tick()

                if not has_more_steps:
                    self.loop_count += 1

                    if self.max_loops is not None and self.loop_count >= self.max_loops:
                        break

                    self.reset()
        except StopPipeline:
            pass
        finally:
            self._emit(PipelineEventType.PIPELINE_END)

    def reset(self):
        self.current = 0
        for step in self.steps:
            step.reset()
        
        self._emit(PipelineEventType.PIPELINE_RESET)

    def add_observer(self, observer: PipelineObserver):
        self._observers.append(observer)

    def _tick(self) -> bool:
        if self.current >= len(self.steps):
            return False

        step = self.steps[self.current]
        self._enter_step(step)

        if self._has_timed_out(step):
            self._handle_timeout(step)
            return True

        step_nav = StepNavigator()
        self._execute_step(step, step_nav)

        if step_nav.has_target():
            target = self._get_index_label(step_nav.goto)
            self._transition(step, target)
        else:
            time.sleep(0.05)

        return True

    def _execute_step(self, step: Step, step_nav: StepNavigator):
        for rule in step.rules:
            if rule.evaluate(self.context, step_nav):
                return

        step.execute_actions(self.context)
        step.increment_repeat()

        if step._current_repeat < step.repeat:
            self._delay(step.delay_after, step.delay_jitter)
            return

        if step.rules:
            return

        if step.goto is not None:
            step_nav.go_to(step.goto)
        else:
            step_nav.next()

    def _transition(self, step: Step, target_index: int):
        target_step = self.steps[target_index] if 0 <= target_index < len(self.steps) else self.steps[0]
        self._emit(PipelineEventType.STEP_TRANSITION, target_step.name)

        self._delay(
            step.delay_after,
            step.delay_jitter
        )

        step.reset()
        self.current = target_index

    def _has_timed_out(self, step: Step):
        return time.time() - step._start_time > step.timeout

    def _handle_timeout(self, step: Step):
        self._emit(PipelineEventType.STEP_TIMEOUT)

        if step.goto:
            self.current = self._get_index_label(step.goto)
        else:
            self.current += 1

        step.reset()

    def _enter_step(self, step: Step):
        if step._start_time is None:
            step._start_time = time.time()
            self._emit(PipelineEventType.STEP_ENTER)

    def _build_label_map(self) -> Dict[str, int]:
        label_map = {}

        for index, step in enumerate(self.steps):
            if step.label:
                if step.label in label_map:
                    raise ValueError(f'Label duplicado: {step.label}')
                label_map[step.label] = index

            label_map[str(index)] = index

        return label_map

    def _get_index_label(self, label: str | None) -> int:
        if not label:
            return self.current + 1

        if label not in self._label_map:
            raise ValueError(f'Label não encontrado: {label}')

        return self._label_map[label]

    def _delay(self, base: float, jitter: float):
        base = max(base, 0.0)
        extra = random.uniform(0, jitter) if jitter > 0 else 0.0
        time.sleep(base + extra)

    def _emit(
        self,
        type: PipelineEventType,
        transition_to: Optional[str] = None
    ):
        event = PipelineEvent(
            type=type,
            snapshot=self._snapshot(),
            transition_to=transition_to
        )
        
        for observer in self._observers:
            observer.notify(event)
    
    def _snapshot(self) -> PipelineSnapshot:
        step_name = None

        if 0 <= self.current < len(self.steps):
            step_name = self.steps[self.current].name

        
        return PipelineSnapshot(
            current_step=step_name,
            loop_count=self.loop_count,
            max_loops=self.max_loops,
            context=self.context
        )
