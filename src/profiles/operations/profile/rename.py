from config import settings
from config.paths import Paths

from src.helpers.json import JsonFile
from src.helpers.fs import rename_dir


def rename_profile(
    old_profile_name: str,
    new_profile_name: str
):
    JsonFile.patch(
        path=Paths.profile_file(old_profile_name),
        updates={
            'name': new_profile_name
        },
        schema=settings.JSON.profile_schema
    )
    
    rename_dir(
        src=Paths.PROFILES / old_profile_name,
        new_name=new_profile_name
    )
