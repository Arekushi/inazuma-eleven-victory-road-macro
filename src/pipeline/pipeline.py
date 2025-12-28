import time
import random

from typing import List
from config import settings
from rich.console import Console
from src.pipeline.flow_context import FlowContext
from src.pipeline.step import Step


console = Console()


class Pipeline:
    def __init__(self, steps: List[Step], max_loops: int | None = None):
        self.steps = steps
        self.max_loops = max_loops
        self.current = 0
        self.loop_count = 0
        self._label_map = self._build_label_map()

    def run(self):
        while True:
            has_more_steps = self._tick()

            if not has_more_steps:
                self.loop_count += 1

                if self.max_loops is not None and self.loop_count >= self.max_loops:
                    break

                self.reset()

    def reset(self):
        self.current = 0
        for step in self.steps:
            step.reset()

    def _tick(self) -> bool:
        if self.current >= len(self.steps):
            return False

        step = self.steps[self.current]
        self._enter_step(step)

        if self._has_timed_out(step):
            self._handle_timeout(step)
            return True

        ctx = FlowContext()
        self._execute_step(step, ctx)

        if ctx.has_target():
            target = self._resolve_label(ctx.goto)
            self._transition(step, target)
        else:
            time.sleep(0.05)

        return True
    
    def _execute_step(self, step: Step, ctx: FlowContext):
        for rule in step.rules:
            if rule.evaluate(ctx):
                return

        step.execute_actions()
        
        if step.rules:
            return

        if step.goto is not None:
            ctx.go_to(step.goto)
        else:
            ctx.next()

    def _determine_next_step(self, goto: str | None):
        if goto is None:
            return self.current + 1

        return self._resolve_label(goto)

    def _transition(self, step: Step, target_index: int):
        self._delay(
            step.delay_after,
            step.delay_jitter
        )

        step.reset()
        self.current = target_index

    def _has_timed_out(self, step: Step):
        return time.time() - step._start_time > step.timeout

    def _handle_timeout(self, step: Step):
        console.print(
            settings.CLI.PIPELINE.timeout
                .replace('<step_name>', step.name)
                .replace('<loop_count>', f'{self.loop_count}')
                .replace('<loop_length>', f'{self.max_loops}' if self.max_loops is not None else '∞')
        )

        if step.goto:
            self.current = self._resolve_label(step.goto)
        else:
            self.current += 1

        step.reset()

    def _enter_step(self, step: Step):
        if step._start_time is None:
            step._start_time = time.time()
            console.print(
                settings.CLI.PIPELINE.enter_step
                    .replace('<step_name>', step.name)
                    .replace('<loop_count>', f'{self.loop_count}')
                    .replace('<loop_length>', f'{self.max_loops}' if self.max_loops is not None else '∞')
            )

    def _build_label_map(self):
        label_map = {}

        for index, step in enumerate(self.steps):
            if step.label:
                if step.label in label_map:
                    raise ValueError(f"Label duplicado: {step.label}")
                label_map[step.label] = index

            label_map[str(index)] = index

        return label_map

    def _resolve_label(self, label: str | None):
        if not label:
            return self.current + 1

        if label not in self._label_map:
            raise ValueError(f"Label não encontrado: {label}")

        return self._label_map[label]

    def _delay(self, base: float, jitter: float):
        base = max(base, 0.0)
        extra = random.uniform(0, jitter) if jitter > 0 else 0.0
        time.sleep(base + extra)
