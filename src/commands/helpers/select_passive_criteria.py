import questionary
from typing import List


def select_passive_criteria(passive_criterias: List[str]) -> str:
    if not passive_criterias:
        raise RuntimeError('Nenhuma Passive-Criteria encontrada')

    return questionary.select(
        'Escolha uma passive-criteria:',
        choices=passive_criterias
    ).ask()
