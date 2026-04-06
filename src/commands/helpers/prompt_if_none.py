from enum import Enum
from typing import Any

import typer


def prompt_if_none(resolver, *args, **kwargs) -> Any:
    def callback(
        ctx: typer.Context,
        param: typer.CallbackParam,
        value: Any
    ) -> Any:
        result = value if value is not None else resolver(*args, **kwargs)
        
        if isinstance(result, Enum):
            return result.value
        
        return result
    
    return callback
