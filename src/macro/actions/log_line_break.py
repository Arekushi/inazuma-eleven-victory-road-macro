from src.pipeline.classes import PipelineContext


def log_line_break(pipeline_ctx: PipelineContext):
    pipeline_ctx.logger.info('', extra={'_blank_line': True})
