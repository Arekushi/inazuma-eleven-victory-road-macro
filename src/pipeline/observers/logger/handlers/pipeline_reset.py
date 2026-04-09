from .base import PipelineLogHandler
from src.pipeline.enums import PipelineEventType


class PipelineResetLogHandler(PipelineLogHandler):
    event_type = PipelineEventType.PIPELINE_RESET

    def handle(self, logger, event):
        logger.info('', extra={'_blank_line': True})
