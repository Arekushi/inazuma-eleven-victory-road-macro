from typing import Optional
from dataclasses import dataclass

from src.pipeline.classes import PipelineSnapshot
from src.pipeline.enums import PipelineEventType


@dataclass
class PipelineEvent:
    type: PipelineEventType
    snapshot: PipelineSnapshot
    transition_to: Optional[str] = None
