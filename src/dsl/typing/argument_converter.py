from enum import Enum
from typing import Any, Type, get_origin, get_args


class ArgumentConverter:
    def convert(self, value: Any, expected_type: Type, arg_name: str):
        if value is None:
            return None

        if self._is_enum(expected_type):
            return self._to_enum(value, expected_type, arg_name)

        if expected_type is bool:
            return self._to_bool(value, arg_name)

        if self._is_typed_tuple(expected_type):
            return self._to_tuple(value, expected_type, arg_name)

        if not isinstance(value, expected_type):
            raise TypeError(
                f'Argumento "{arg_name}" esperado {expected_type.__name__}, '
                f'recebido {type(value).__name__}'
            )

        return value
    
    def _is_enum(self, t: Type) -> bool:
        return isinstance(t, Type) and issubclass(t, Enum)

    def _is_typed_tuple(self, t: Type) -> bool:
        return get_origin(t) is tuple

    def _to_enum(self, value, enum_type, arg_name):
        if isinstance(value, enum_type):
            return value

        if isinstance(value, str):
            try:
                return enum_type[value]
            except KeyError:
                valid = ', '.join(e.name for e in enum_type)
                raise ValueError(
                    f'Valor inválido para {arg_name}: {value}. '
                    f'Esperado um de: {valid}'
                )

        raise TypeError(
            f'Argumento "{arg_name}" deve ser string ou {enum_type.__name__}'
        )

    def _to_bool(self, value, arg_name):
        if isinstance(value, bool):
            return value

        if isinstance(value, str):
            if value.lower() in ('true', 'yes', '1'):
                return True
            if value.lower() in ('false', 'no', '0'):
                return False

        raise ValueError(f'Argumento "{arg_name}" inválido para bool')

    def _to_tuple(self, value, tuple_type, arg_name):
        if not isinstance(value, tuple):
            raise TypeError(
                f'Argumento "{arg_name}" deve ser tuple'
            )

        expected_types = get_args(tuple_type)

        if len(value) != len(expected_types):
            raise ValueError(
                f'Argumento "{arg_name}" esperado tuple de tamanho {len(expected_types)}'
            )

        return tuple(
            self.convert(v, t, arg_name)
            for v, t in zip(value, expected_types)
        )
