from typing import Any, Type, TypeVar


T = TypeVar('T')


def require(obj: Any, capability: Type[T]) -> T:
    if not isinstance(obj, capability):
        raise RuntimeError(
            f"{obj} não implementa {capability.__name__}"
        )

    return obj
