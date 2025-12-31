import csv
from pathlib import Path
from typing import Dict
from config.paths import Paths

from src.enums import Language
from src.passives.enums import PassiveType, PlayerType, PlayerRarity
from src.passives.classes import PassiveValues, Passive


def parse_passive_row(
    row: Dict[str, str],
    player_type: PlayerType
) -> Passive:
    passive_id = int(row['id'])
    archetype = row.get('archetype') or None
    text = row['text']

    values_by_rarity: Dict[PlayerRarity, PassiveValues] = {}

    for player_rarity in PlayerRarity:
        low = float(row[f'{player_rarity.value}_low'])
        high = float(row[f'{player_rarity.value}_high'])

        values_by_rarity[player_rarity] = PassiveValues(
            low=low,
            high=high
        )

    return Passive(
        id=passive_id,
        archetype=archetype,
        text=text,
        values={player_type: values_by_rarity},
    )


def load_passives_from_path(
    path: Path,
    player_type: PlayerType
) -> Dict[str, Passive]:
    passives: Dict[str, Passive] = {}

    with path.open(encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            passive = parse_passive_row(
                row=row,
                player_type=player_type
            )
            passives[passive.id] = passive

    return passives


def load_passives_by_type(
    player_type: PlayerType,
    language: Language,
    type: PassiveType
) -> Dict[str, Passive]:
    path = Paths.passives(language, player_type) / f'{type.value}.csv'
    return load_passives_from_path(
        path=path,
        player_type=player_type
    )


def load_passives(
    player_type: PlayerType,
    language: Language,
) -> Dict[str, Passive]:
    all_passives: Dict[str, Passive] = {}

    for passive_type in PassiveType:
        all_passives.update(
            load_passives_by_type(
                player_type=player_type,
                language=language,
                type=passive_type
            )
        )

    return all_passives
