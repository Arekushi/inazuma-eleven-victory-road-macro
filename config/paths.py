from pathlib import Path

from src.passives.enums import SpiritType, PassiveType
from src.enums import Language, FileExt


class Paths:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    ASSETS = PROJECT_ROOT / 'assets'
    DATA = PROJECT_ROOT / 'data'
    PROFILES = PROJECT_ROOT / 'profiles'
    TEMP = PROJECT_ROOT / 'temp'

    @staticmethod
    def assets_lang(lang: Language) -> Path:
        return Paths.ASSETS / lang.value

    @staticmethod
    def match_assets(lang: Language) -> Path:
        return Paths.assets_lang(lang) / 'match'

    @staticmethod
    def data_lang(lang: Language) -> Path:
        return Paths.DATA / lang.value
    
    @staticmethod
    def passive_data_by_type(
        language: Language,
        spirit_type: SpiritType,
        type: PassiveType
    ) -> Path:
        return Paths.data_lang(language) / 'passives' / spirit_type.value / f'{type.value}.{FileExt.CSV.value}'
    
    @staticmethod
    def passive_criteria(
        profile_name: str,
        passive_criteria_name: str
    ) -> Path:
        return Paths.PROFILES / profile_name / 'passive-criteria' / f'{passive_criteria_name}.{FileExt.JSON.value}'
    
    @staticmethod
    def all_passive_criteria(
        profile_name: str
    ) -> Path:
        return Paths.PROFILES / profile_name / 'passive-criteria'
    
    @staticmethod
    def macro(
        profile_name: str,
        file_name: str
    ) -> Path:
        return Paths.PROFILES / profile_name / 'macros' / f'{file_name}.{FileExt.VML.value}'
    
    @staticmethod
    def macros(
        profile_name: str
    ) -> Path:
        return Paths.PROFILES / profile_name / 'macros'
    
    @staticmethod
    def profile_file(profile_name: str) -> Path:
        return Paths.PROFILES / profile_name / f'profile.{FileExt.JSON.value}'
