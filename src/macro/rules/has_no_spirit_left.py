from src.profiles.classes import PassiveCriteria
from src.pipeline.classes import PipelineContext


def has_no_spirit_left(pipeline_ctx: PipelineContext) -> bool:
    if pipeline_ctx is None:
        return True
    
    criteria: PassiveCriteria = pipeline_ctx.get('criteria')
    
    if criteria is None:
        return True
    
    opened_spirits_count = pipeline_ctx.get('opened_spirits_count', 0)
    
    if opened_spirits_count >= criteria.spirit.quantity:
        pipeline_ctx.pop('opened_spirits_count')
        return True
    
    return False
