from config.paths import Paths
from src.helpers.fs import delete_file


def delete_passive_criteria(
    profile_name: str,
    passive_criteria_name: str
):
    delete_file(Paths.passive_criteria(profile_name, passive_criteria_name))
