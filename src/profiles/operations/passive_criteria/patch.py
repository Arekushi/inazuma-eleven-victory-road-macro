from config import settings, Paths

from src.helpers.json import JsonFile
from src.profiles.classes import PassiveCriteriaDict


def patch_passive_criteria(
    profile_name: str,
    passive_criteria_name: str,
    passive_criteria_patch: PassiveCriteriaDict
):
    JsonFile.patch(
        path=Paths.passive_criteria(profile_name, passive_criteria_name),
        updates=passive_criteria_patch,
        schema=settings.JSON.passive_criteria_schema
    )
