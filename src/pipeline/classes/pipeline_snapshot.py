from dataclasses import dataclass
from typing import Optional

from src.pipeline.classes import PipelineContext


@dataclass(frozen=True)
class PipelineSnapshot:
    loop_count: int
    max_loops: int | None
    current_step: Optional[str]
    context: PipelineContext
