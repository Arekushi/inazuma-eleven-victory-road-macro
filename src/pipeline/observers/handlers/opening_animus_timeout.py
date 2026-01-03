from typing import Dict
from config import settings

from .base import PipelineLogHandler
from src.passives.classes import SlotValidationResult
from src.pipeline.enums import PipelineEventType
from src.passives.ocr import normalize_passive_text


class OpeningAnimusTimeoutLogHandler(PipelineLogHandler):
    event_type = PipelineEventType.STEP_TIMEOUT

    def handle(self, logger, event):
        slot_validation_result: Dict[int, SlotValidationResult] = \
            event.snapshot.context.pop('slot_validation_result')
        
        if slot_validation_result:
            for result in slot_validation_result.values():        
                logger.info(
                    settings.CLI.OPENING_ANIMUS.passives,
                    extra={
                        'loop_count': event.snapshot.loop_count + 1,
                        'max_loops': event.snapshot.max_loops or '∞',
                        'slot_number': result.slot,
                        'passive_ocr_text': normalize_passive_text(result.ocr_text)
                    }
                )
