from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from src.input.enums import InputMode
from src.enums import Language


@dataclass
class MatchConfig:
    macro_path: Path
    input_mode: InputMode
    language: Language
    enable_log: bool = False
    max_loops: Optional[int] = None
