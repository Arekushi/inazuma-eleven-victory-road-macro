from .base import PipelineLogHandler
from src.pipeline.enums import PipelineEventType


class PipelineStartLogHandler(PipelineLogHandler):
    event_type = PipelineEventType.PIPELINE_START

    def handle(self, logger, event):
        logger.info('Pipeline started')
