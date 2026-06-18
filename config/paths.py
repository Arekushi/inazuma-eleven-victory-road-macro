from pathlib import Path

from src.application.enums import FileExt


class Paths:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    ASSETS = PROJECT_ROOT / 'assets'
    MACROS = PROJECT_ROOT / 'macros'
    TEMP = PROJECT_ROOT / 'temp'
    REPO = PROJECT_ROOT / 'repo'
    METADATA = REPO / 'metadata'
    
    @staticmethod
    def macro_file(
        file_name: str
    ) -> Path:
        return Paths.MACROS / f'{file_name}.{FileExt.VML}'
