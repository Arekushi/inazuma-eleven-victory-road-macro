from enum import Enum
from dataclasses import is_dataclass, asdict
from pathlib import Path
from typing import Any


class JsonNormalizer:
    @staticmethod
    def normalize(value: Any) -> Any:
        if isinstance(value, Enum):
            return getattr(value, 'json', value.value)

        if is_dataclass(value):
            return JsonNormalizer.normalize(asdict(value))

        if isinstance(value, Path):
            return str(value)

        if isinstance(value, dict):
            return {
                k: JsonNormalizer.normalize(v)
                for k, v in value.items()
            }

        if isinstance(value, (list, tuple, set)):
            return [
                JsonNormalizer.normalize(v)
                for v in value
            ]

        return value
