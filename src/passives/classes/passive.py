from dataclasses import dataclass
from typing import Dict

from src.passives.enums import SpiritType, SpiritRarity
from src.passives.classes import PassiveValues


@dataclass(frozen=True)
class Passive:
    id: int
    archetype: str | None
    text: str
    values: Dict[SpiritType, Dict[SpiritRarity, PassiveValues]]
