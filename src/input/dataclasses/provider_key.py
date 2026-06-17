from dataclasses import dataclass

from src.application.enums import SystemOS
from src.input.enums import InputMode


@dataclass(frozen=True)
class ProviderKey:
    os: SystemOS
    mode: InputMode
