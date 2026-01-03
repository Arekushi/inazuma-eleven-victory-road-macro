from typing import Dict

from src.passives.matchers import is_expected_passive_text
from src.passives.classes import Passive, PassiveCriteria, SlotValidationResult
from src.passives.ocr import read_text_from_passive_slot


def validate_passive_criteria(
    passives: Dict[str, Passive],
    criteria: PassiveCriteria
) -> Dict[int, SlotValidationResult]:

    result: Dict[int, SlotValidationResult] = {}

    for slot, desired_passives in criteria.slots.items():
        ocr_text = read_text_from_passive_slot(slot)
        desired_text = None
        slot_valid = False

        for desired in desired_passives:
            passive = passives[desired.id]

            if is_expected_passive_text(
                ocr_text=ocr_text,
                passive_text=passive.text,
                passive_values=passive.values[criteria.player_type][criteria.player_rarity],
                passive_quality=desired.quality
            ):
                slot_valid = True
                desired_text = passive.text
                break

        result[slot] = SlotValidationResult(
            slot=slot,
            valid=slot_valid,
            ocr_text=ocr_text,
            desired_text=desired_text
        )

    return result
