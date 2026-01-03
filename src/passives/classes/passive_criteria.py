from dataclasses import dataclass
from typing import Dict, List, Optional

from src.enums import Language
from src.passives.enums import PlayerType, PlayerRarity, PassiveQualityCriteria


@dataclass(frozen=True)
class DesiredPassive:
    id: str
    quality: PassiveQualityCriteria


@dataclass(frozen=True)
class PassiveCriteria:
    language: Language
    quantity: int
    player_type: PlayerType
    player_rarity: PlayerRarity
    slots: Dict[int, List[DesiredPassive]]
    name: Optional[str] = None
