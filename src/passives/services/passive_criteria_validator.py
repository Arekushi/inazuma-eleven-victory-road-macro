from typing import Dict

from src.passives.matchers import is_expected_passive_text
from src.passives.classes import Passive, PassiveCriteria
from src.passives.ocr import read_text_from_passive_slot


def validate_passive_criteria(
    passives: Dict[str, Passive],
    criteria: PassiveCriteria
):
    result: Dict[int, bool] = {}
    
    for slot, desired_passives in criteria.slots.items():
        slot_valid = False
        ocr_text = read_text_from_passive_slot(slot)
        
        for desired in desired_passives:
            passive = passives[desired.id]
            passive_text = passive.text
            passive_values = passive.values[criteria.player_type][criteria.player_rarity]
            
            if is_expected_passive_text(
                ocr_text=ocr_text,
                passive_text=passive_text,
                passive_values=passive_values,
                passive_quality=desired.quality
            ):
                slot_valid = True
                break
                
        result[slot] = slot_valid
    
    return result
