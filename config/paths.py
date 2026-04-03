from pathlib import Path

from src.enums import Language, FileExt


class Paths:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    ASSETS = PROJECT_ROOT / 'assets'
    PROFILES = PROJECT_ROOT / 'profiles'
    TEMP = PROJECT_ROOT / 'temp'

    @staticmethod
    def assets_lang(lang: Language) -> Path:
        return Paths.ASSETS / lang.value

    @staticmethod
    def match_assets(lang: Language) -> Path:
        return Paths.assets_lang(lang) / 'match'
    
    @staticmethod
    def macro(
        profile_name: str,
        file_name: str
    ) -> Path:
        return Paths.PROFILES / profile_name / 'macros' / f'{file_name}.{FileExt.VML}'
    
    @staticmethod
    def macros(
        profile_name: str
    ) -> Path:
        return Paths.PROFILES / profile_name / 'macros'
    
    @staticmethod
    def profile_file(profile_name: str) -> Path:
        return Paths.PROFILES / profile_name / f'profile.{FileExt.JSON}'
