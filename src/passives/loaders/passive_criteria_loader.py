import json
from pathlib import Path
from typing import Dict, Any

from src.enums import Language
from src.passives.enums import PlayerRarity, PlayerType, PassiveQualityCriteria
from src.passives.classes import DesiredPassive, PassiveCriteria


def _parse_passive_criteria(data: Dict[str, Any]) -> PassiveCriteria:
    slots: Dict[int, list[DesiredPassive]] = {}
    slots_data = data.get('slots', {})
    
    language = Language(data.get('language', None))
    player_type = PlayerType(data.get('player-type', None))
    player_rarity = PlayerRarity(data.get('player-rarity', None))

    for slot_str, passives in slots_data.items():
        slot = int(slot_str)

        slots[slot] = [
            DesiredPassive(
                id=int(passive['id']),
                quality=PassiveQualityCriteria(passive['quality'])
            )
            for passive in passives
        ]

    return PassiveCriteria(
        language=language,
        player_type=player_type,
        player_rarity=player_rarity,
        slots=slots
    )


def load_passive_criteria_from_path(path: str | Path) -> PassiveCriteria:
    path = Path(path)

    with path.open(encoding='utf-8') as file:
        data = json.load(file)

    return _parse_passive_criteria(data)
