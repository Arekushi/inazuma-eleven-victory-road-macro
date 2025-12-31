from typing import Protocol, Optional
from src.pipeline.classes import PipelineContext


class ContextCallable(Protocol):
    def __call__(self, ctx: PipelineContext) -> None: ...
