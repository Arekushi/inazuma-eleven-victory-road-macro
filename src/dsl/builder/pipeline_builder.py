from logging import Logger
from typing import Optional
from src.pipeline.core import Pipeline

from src.dsl.builder.sub import RuleBuilder, StepBuilder, ActionBuilder
from src.dsl.parser import PipelineNode


class PipelineBuilder:
    def __init__(self, pipeline_node: PipelineNode):
        self.step_builder = StepBuilder()
        self.pipeline_node = pipeline_node
        self._logger = None
        self._max_loops = None
        self._context_data = None

    def with_logger(self, logger: Logger):
        self._logger = logger
        return self

    def with_max_loops(self, max_loops: int):
        self._max_loops = max_loops
        return self

    def with_context(self, context: dict):
        self._context_data = context
        return self

    def build(self):
        steps = [
            self.step_builder.build(step_node)
            for step_node in self.pipeline_node.steps
        ]
        
        return Pipeline(
            steps,
            logger=self._logger,
            max_loops=self._max_loops,
            context_data=self._context_data
        )
