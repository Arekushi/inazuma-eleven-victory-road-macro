import time

from src.enums import Key
from src.profiles.classes import PassiveCriteria
from src.pipeline.classes import PipelineContext
from src.macro.actions import key_press


def goto_spirit(
    pipeline_ctx: PipelineContext,
    sleep = 0.5
):
    if not pipeline_ctx:
        return
    
    criteria: PassiveCriteria = pipeline_ctx.get('criteria')
    
    if not criteria:
        return
    
    for _ in range(criteria.spirit.game.order):
        key_press(Key.C)
        time.sleep(sleep)
    
    for _ in range(criteria.spirit.down):
        key_press(Key.DOWN)
        time.sleep(sleep)
    
    for _ in range(criteria.spirit.right):
        key_press(Key.RIGHT)
        time.sleep(sleep)
