from config import settings
from config.paths import Paths

from src.helpers.json import JsonFile
from src.helpers.str.normalize_str import to_kebab_case
from src.profiles.classes import ProfileDict
from src.profiles.helpers import get_username
from src.helpers.fs.copying import copy_dir


def create_profile(profile: ProfileDict):
    if not profile.get('name'):
        profile.update({
            'name': to_kebab_case(get_username())
        })
    
    shared_profile_path = Paths.PROFILES / 'shared'
    new_profile_path = Paths.PROFILES / profile.get('name')
    
    copy_dir(
        src=shared_profile_path,
        dst=new_profile_path
    )
    
    JsonFile.write(
        path=Paths.profile_file(profile.get('name')),
        data=profile,
        schema=settings.JSON.profile_schema
    )
