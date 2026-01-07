from config import settings
from config.paths import Paths

from src.enums.file_ext import FileExt
from src.helpers.json import JsonFile
from src.profiles.classes import PassiveCriteriaDict


def create_passive_criteria(
    profile_name: str,
    passive_criteria: PassiveCriteriaDict
):
    file_name = f"{passive_criteria.get('name')}.{FileExt.JSON.value}"
    file_path = Paths.all_passive_criteria(profile_name) / file_name
    
    JsonFile.write(
        path=file_path,
        data=passive_criteria,
        schema=settings.JSON.passive_criteria_schema
    )
