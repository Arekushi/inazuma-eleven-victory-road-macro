from pathlib import Path
from typing import Dict, Any, List

from config.paths import Paths
from src.helpers.fs.listing import list_files
from src.helpers.json import JsonFile
from src.enums import IEGame

from src.profiles.classes.passive_criteria import (
    DesiredPassive,
    DesiredSpirit,
    PassiveCriteria
)
from src.profiles.enums import PassiveQualityCriteria

from src.passives.enums import (
    SpiritRarity,
    SpiritType,
)


def _parse_desired_passive(data: dict) -> DesiredPassive:
    return DesiredPassive(
        id=int(data['id']),
        quality=PassiveQualityCriteria(data['quality'])
    )


def _parse_slots(data: dict) -> Dict[int, list[DesiredPassive]]:
    slots: Dict[int, list[DesiredPassive]] = {}

    for slot_str, passives in data.items():
        slot = int(slot_str)
        slots[slot] = [_parse_desired_passive(p) for p in passives]

    return slots


def _parse_desired_spirit(data: dict) -> DesiredSpirit:
    return DesiredSpirit(
        name=data.get('name'),
        quantity=int(data['quantity']),
        type=SpiritType(data['type']),
        rarity=SpiritRarity(data['rarity']),
        game=IEGame(data['game']),
        down=int(data['down']),
        right=int(data['right']),
    )


def _parse_passive_criteria(name: str, data: Dict[str, Any]) -> PassiveCriteria:
    return PassiveCriteria(
        name=name,
        spirit=_parse_desired_spirit(data['spirit']),
        slots=_parse_slots(data['slots'])
    )


def load_passive_criteria_from_path(file_path: str | Path) -> PassiveCriteria:
    file_path = Path(file_path)
    data = JsonFile.read(file_path)
    
    return _parse_passive_criteria(file_path.stem, data)


def load_passive_criterias_from_profile(profile_name: str) -> List[PassiveCriteria]:
    passive_criteria_files = list_files(Paths.all_passive_criteria(profile_name))
    
    return [
        load_passive_criteria_from_path(file)
        for file in passive_criteria_files
    ]
