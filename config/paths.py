from pathlib import Path

from src.passives.enums.player_type import PlayerType
from src.enums import Language

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Paths:
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
    def passives(
        language: Language,
        player_type: PlayerType
    ) -> Path:
        return Paths.data_lang(language) / 'passives' / player_type.value
    
    @staticmethod
    def passive_criteria(
        user: str,
        file_name: str
    ) -> Path:
        return Paths.PROFILES / user / 'passive-criteria' / f'{file_name}.json'
