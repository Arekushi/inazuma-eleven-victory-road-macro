from typing import Any
from dataclasses import dataclass
from src.input.classes import InputResolver


@dataclass
class InputBundle:
    controller: Any
    resolver: InputResolver
