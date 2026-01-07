from pathlib import Path
from typing import List

from config.paths import Paths

from src.helpers.json import JsonFile
from src.enums import Language
from src.profiles.loaders import load_passive_criterias_from_profile
from src.profiles.exceptions import ProfileNotFoundException
from src.profiles.classes import PassiveCriteria, Profile, Macro
from src.helpers.fs.listing import list_files, list_dir_names


def _load_macros(profile_name: str) -> dict[str, Macro]:
    macro_dir = Paths.macros(profile_name)

    return {
        file_path.stem: Macro(
            name=file_path.stem,
            path=file_path
        )
        for file_path in list_files(macro_dir)
    }


def _load_passive_criterias(profile_name: str) -> dict[str, PassiveCriteria]:
    criterias = load_passive_criterias_from_profile(profile_name)

    return {
        criteria.name: criteria
        for criteria in criterias
    }


def _parse_profile(
    data: dict,
    profile_name: str
) -> Profile:
    language = Language(data.get('language', Language.EN))
    macros = _load_macros(profile_name)
    passive_criterias = _load_passive_criterias(profile_name)
    
    return Profile(
        name=profile_name,
        language=language,
        macros=macros,
        passive_criterias=passive_criterias
    )


def load_profile_from_path(profile_path: str | Path) -> Profile:
    profile_name = profile_path.name
    profile_file = Paths.profile_file(profile_name)
    
    if not profile_file.exists():
        raise FileNotFoundError(
            f"Arquivo {profile_file.name} não encontrado em {profile_path}"
        )
        
    data = JsonFile.read(profile_file)
    return _parse_profile(data, profile_name)


def load_profile_by_name(name: str) -> Profile:
    profile_path = Paths.PROFILES / name

    if not profile_path.exists() or not profile_path.is_dir():
        raise ProfileNotFoundException(name, Paths.PROFILES)

    return load_profile_from_path(profile_path)


def load_all_profiles() -> List[Profile]:
    profile_names = list_dir_names(Paths.PROFILES)
    return [load_profile_by_name(name) for name in profile_names]
