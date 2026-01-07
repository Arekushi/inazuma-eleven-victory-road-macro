import csv
from pathlib import Path
from typing import Dict
from config.paths import Paths

from src.enums import Language
from src.passives.enums import PassiveType, SpiritType, SpiritRarity
from src.passives.classes import PassiveValues, Passive


def parse_passive_row(
    row: Dict[str, str],
    spirit_type: SpiritType
) -> Passive:
    passive_id = int(row['id'])
    archetype = row.get('archetype') or None
    text = row['text']

    values_by_rarity: Dict[SpiritRarity, PassiveValues] = {}

    for spirit_rarity in SpiritRarity:
        low = float(row[f'{spirit_rarity.value}_low'])
        high = float(row[f'{spirit_rarity.value}_high'])

        values_by_rarity[spirit_rarity] = PassiveValues(
            low=low,
            high=high
        )

    return Passive(
        id=passive_id,
        archetype=archetype,
        text=text,
        values={spirit_type: values_by_rarity},
    )


def load_passives_from_path(
    path: Path,
    spirit_type: SpiritType
) -> Dict[int, Passive]:
    passives: Dict[int, Passive] = {}

    with path.open(encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            passive = parse_passive_row(
                row=row,
                spirit_type=spirit_type
            )
            passives[passive.id] = passive

    return passives


def load_passives_by_type(
    spirit_type: SpiritType,
    language: Language,
    type: PassiveType
) -> Dict[int, Passive]:
    passive_path = Paths.passive_data_by_type(language, spirit_type, type)
    
    return load_passives_from_path(
        path=passive_path,
        spirit_type=spirit_type
    )


def load_passives(
    spirit_type: SpiritType,
    language: Language,
) -> Dict[int, Passive]:
    all_passives: Dict[int, Passive] = {}

    for passive_type in PassiveType:
        all_passives.update(
            load_passives_by_type(
                spirit_type=spirit_type,
                language=language,
                type=passive_type
            )
        )

    return all_passives
