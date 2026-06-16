import questionary

from enum import Enum
from typing import TypeVar


E = TypeVar("E", bound=Enum)


def prompt_enum(
    enum_cls: type[E],
    message: str
) -> E:
    result = questionary.select(
        message,
        choices=[
            questionary.Choice(
                title=item.name,
                value=item,
            )
            for item in enum_cls.__members__.values()
        ],
    ).ask()

    if result is None:
        raise KeyboardInterrupt('Operação cancelada')

    return result
