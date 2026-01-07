from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Macro:
    name: str
    path: Path
