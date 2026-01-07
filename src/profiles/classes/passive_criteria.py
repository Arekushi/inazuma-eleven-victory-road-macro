from dataclasses import dataclass
from typing import Dict, List, Optional, TypedDict

from src.profiles.enums import PassiveQualityCriteria
from src.enums import IEGame
from src.passives.enums import SpiritType, SpiritRarity


@dataclass(frozen=True)
class DesiredPassive:
    id: int
    quality: PassiveQualityCriteria


@dataclass(frozen=True)
class DesiredSpirit:
    quantity: int
    type: SpiritType
    rarity: SpiritRarity
    game: IEGame
    down: int
    right: int
    name: Optional[str] = None


@dataclass(frozen=True)
class PassiveCriteria:
    name: str
    spirit: DesiredSpirit
    slots: Dict[int, List[DesiredPassive]]


class DesiredPassiveDict(TypedDict):
    id: int
    quality: PassiveQualityCriteria


class DesiredSpiritDict(TypedDict):
    quantity: int
    type: SpiritType
    rarity: SpiritRarity
    game: IEGame
    down: int
    right: int
    name: Optional[str] = None


class PassiveCriteriaDict(TypedDict):
    name: str
    spirit: DesiredSpiritDict
    slots: Dict[int, List[DesiredPassiveDict]]
