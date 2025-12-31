import inspect

from typing import Callable, Optional
from src.pipeline.classes import PipelineContext


def with_context(func: Callable) -> Callable[[Optional[PipelineContext]], None]:
    sig = inspect.signature(func)
    
    if len(sig.parameters) == 0:
        return lambda ctx=None: func()
    else:
        return func
