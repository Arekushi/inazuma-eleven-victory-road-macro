import questionary
from typer import Typer

from config.paths import Paths
from src.helpers.fs.listing import list_files, list_dir_names


def prompt_macro_name(sub_folder: str = None) -> str:    
    if not sub_folder:
        sub_folder = questionary.select(
            'Escolha uma subpasta:',
            choices=list_dir_names(Paths.MACROS),
        ).ask()
    
    macros = [m.stem for m in list_files(Paths.MACROS / sub_folder)]
    macro_name = questionary.select(
        'Escolha um macro:',
        choices=macros,
    ).ask()
    
    if macro_name is None:
        raise Typer.Abort()
    
    return macro_name
