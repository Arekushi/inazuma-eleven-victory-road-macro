from collections import defaultdict
from typing import Dict, List
from logging import Logger

from src.pipeline.classes import PipelineObserver
from src.pipeline.enums import PipelineEventType
from .handlers.base import PipelineLogHandler


class PipelineLogger(PipelineObserver):

    def __init__(
        self,
        logger: Logger,
        handlers: list[PipelineLogHandler]
    ):
        self._logger = logger
        self._handlers: Dict[
            PipelineEventType,
            List[PipelineLogHandler]
        ] = defaultdict(list)

        for handler in handlers:
            self._handlers[handler.event_type].append(handler)

    def notify(self, event):
        for handler in self._handlers.get(event.type, []):
            handler.handle(self._logger, event)
