from typing import Any
from dataclasses import dataclass
from src.dsl.token import TokenType


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: Any
    line: int
    column: int
