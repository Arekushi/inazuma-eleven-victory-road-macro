from dataclasses import dataclass
from typing import Optional

from src.input.enums import InputMode


@dataclass
class MatchConfig:
    input_mode: InputMode
    max_loops: Optional[int] = None
    enable_log_file: bool = False
