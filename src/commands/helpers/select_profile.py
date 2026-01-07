import questionary
from config.paths import Paths
from src.helpers.fs.listing import list_dir_names


def select_profile_name() -> str:
    profiles = list_dir_names(Paths.PROFILES)

    if not profiles:
        raise RuntimeError('Nenhum profile encontrado')

    return questionary.select(
        'Escolha um profile:',
        choices=profiles,
        default='shared'
    ).ask()
