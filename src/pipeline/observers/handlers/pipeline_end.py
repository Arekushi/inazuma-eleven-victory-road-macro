from .base import PipelineLogHandler
from src.pipeline.enums import PipelineEventType


class PipelineEndLogHandler(PipelineLogHandler):
    event_type = PipelineEventType.PIPELINE_END

    def handle(self, logger, event):
        logger.info('Pipeline finished')
