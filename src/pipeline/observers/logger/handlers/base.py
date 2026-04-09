from logging import Logger
from abc import ABC, abstractmethod

from src.pipeline.classes import PipelineEvent
from src.pipeline.enums import PipelineEventType


class PipelineLogHandler(ABC):
    event_type: PipelineEventType

    @abstractmethod
    def handle(
        self,
        logger: Logger,
        event: PipelineEvent
    ) -> None:
        pass
