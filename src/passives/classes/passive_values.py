from dataclasses import dataclass


@dataclass(frozen=True)
class PassiveValues:
    low: float
    high: float
