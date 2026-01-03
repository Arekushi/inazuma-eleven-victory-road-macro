from src.pipeline.classes import PipelineContext
from src.passives.services import validate_passive_criteria
from src.passives.classes import Passive, PassiveCriteria


def passives_are_valid(pipeline_ctx: PipelineContext) -> bool:
    if pipeline_ctx is None:
        return False
    
    passives: Passive = pipeline_ctx.get('passives')
    criteria: PassiveCriteria = pipeline_ctx.get('criteria')
    
    if passives and criteria:
        result = validate_passive_criteria(
            passives=passives,
            criteria=criteria
        )
        
        pipeline_ctx.set('slot_validation_result', result)
        
        return all(result[key].valid for key in result)

    return False
