from config import settings, Paths
from src.profiles.classes import ProfileDict
from src.helpers.json import JsonFile


def patch_profile(
    profile_name: str,
    profile_patch: ProfileDict
):
    JsonFile.patch(
        path=Paths.profile_file(profile_name),
        updates=profile_patch,
        schema=settings.JSON.profile_schema
    )
