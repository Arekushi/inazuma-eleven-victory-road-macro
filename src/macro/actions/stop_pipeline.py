from src.pipeline.exceptions import StopPipeline


def stop_pipeline():
    raise StopPipeline()
