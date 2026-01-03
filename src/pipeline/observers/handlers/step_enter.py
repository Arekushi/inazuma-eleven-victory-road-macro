from .base import PipelineLogHandler
from src.pipeline.enums import PipelineEventType
from config import settings


class StepEnterLogHandler(PipelineLogHandler):
    event_type = PipelineEventType.STEP_ENTER

    def handle(self, logger, event):
        logger.info(
            settings.CLI.PIPELINE.enter_step,
            extra={
                'step_name': event.snapshot.current_step,
                'loop_count': event.snapshot.loop_count + 1,
                'max_loops': event.snapshot.max_loops or '∞',
            }
        )
