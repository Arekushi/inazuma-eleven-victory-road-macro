from src.pipeline.classes import PipelineContext


def log_line_break(pipeline_ctx: PipelineContext):
    logger = pipeline_ctx.logger
    
    if logger:
        logger.info('', extra={'_blank_line': True})
