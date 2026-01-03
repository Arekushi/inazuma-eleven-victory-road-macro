from src.pipeline.classes import PipelineContext


def register_spirit_opened(pipeline_ctx: PipelineContext):
    if pipeline_ctx is None:
        return
    
    opened_count = pipeline_ctx.get('opened_spirits_count', 0)
    opened_count += 1
    pipeline_ctx.set('opened_spirits_count', opened_count)
    
    return opened_count
