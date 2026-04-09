from .base import PipelineLogHandler
from src.pipeline.enums import PipelineEventType
from config import settings


class StepTimeoutLogHandler(PipelineLogHandler):
    event_type = PipelineEventType.STEP_TIMEOUT

    def handle(self, logger, event):
        logger.warning(
            settings.CLI.PIPELINE.timeout,
            extra={
                'step_name': event.snapshot.current_step,
                'loop_count': event.snapshot.loop_count + 1,
                'max_loops': event.snapshot.max_loops or '∞',
            }
        )
