from enum import Enum, auto


class PipelineEventType(Enum):
    PIPELINE_START = auto()
    PIPELINE_END = auto()
    PIPELINE_RESET = auto()
    STEP_ENTER = auto()
    STEP_TRANSITION = auto()
    STEP_TIMEOUT = auto()
