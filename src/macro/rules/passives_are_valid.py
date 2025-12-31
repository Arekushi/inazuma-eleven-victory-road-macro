from typing import List

from src.passives.services.passive_criteria_validator import validate_passive_criteria
from src.passives.classes.passive import Passive
from src.passives.classes.passive_criteria import PassiveCriteria


def passives_are_valid(
    criteria: PassiveCriteria,
    passives: List[Passive]
) -> bool:    
    result = validate_passive_criteria(
        passives=passives,
        criteria=criteria
    )
    
    return all(result.values())
