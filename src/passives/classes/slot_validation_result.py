from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class SlotValidationResult:
    slot: int
    valid: bool
    ocr_text: str
    desired_text: str
