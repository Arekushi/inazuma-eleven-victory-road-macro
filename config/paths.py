from pathlib import Path

from src.enums import Language, FileExt


class Paths:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    ASSETS = PROJECT_ROOT / 'assets'
    MACROS = PROJECT_ROOT / 'macros'
    TEMP = PROJECT_ROOT / 'temp'

    @staticmethod
    def assets_lang(lang: Language) -> Path:
        return Paths.ASSETS / lang.value

    @staticmethod
    def match_assets(lang: Language) -> Path:
        return Paths.assets_lang(lang) / 'match'
    
    @staticmethod
    def macro(
        sub_folder: str,
        file_name: str
    ) -> Path:
        return Paths.MACROS / sub_folder / f'{file_name}.{FileExt.VML}'
