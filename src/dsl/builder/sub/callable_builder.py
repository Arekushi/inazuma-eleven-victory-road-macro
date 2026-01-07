from typing import Any
from src.dsl.typing import ArgumentConverter
from src.dsl.parser import CallbackNode
from src.dsl.specs import CallableSpec, ArgumentSpec


class CallableBuilder:
    def __init__(self, registry: dict[str, CallableSpec]):
        self.registry = registry
        self.converter = ArgumentConverter()
    
    def build(self, node: CallbackNode):
        spec = self._get_spec(node)
        bound_args = self.bind_args(node, spec)
        converted_args = self.convert_args(bound_args, spec)
        self.validate_args(converted_args, spec)

        return spec.factory(**converted_args)
    
    def _get_spec(self, node: CallbackNode) -> CallableSpec:        
        try:
            return self.registry[node.name]
        except KeyError:
            raise Exception(f"Ação desconhecida '{node.name}'")
    
    def bind_args(
        self,
        node: CallbackNode,
        spec: CallableSpec
    ) -> dict[str, Any]:

        args = node.args
        specs = spec.arguments

        min_args = len([a for a in specs if not a.optional])
        max_args = len(specs)

        if not (min_args <= len(args) <= max_args):
            raise ValueError(
                f'{spec.name}: esperado entre {min_args} e {max_args} argumentos, '
                f'recebido {len(args)}'
            )

        bound = {}

        for i, arg_spec in enumerate(specs):
            if i >= len(args):
                if arg_spec.optional:
                    break
                raise ValueError(
                    f'{spec.name}: argumento obrigatório ausente: {arg_spec.name}'
                )

            bound[arg_spec.name] = args[i]

        return bound
    
    def validate_args(
        self,
        args: dict[str, Any],
        spec: CallableSpec
    ):
        for arg_spec in spec.arguments:
            if arg_spec.name not in args:
                continue

            value = args[arg_spec.name]

            self._validate_type(
                spec.name,
                arg_spec,
                value
            )

            self._validate_custom(
                value,
                arg_spec
            )

    def convert_args(self, args: dict, spec):
        return {
            arg_spec.name: self.converter.convert(
                args[arg_spec.name],
                arg_spec.type,
                arg_spec.name
            )
            for arg_spec in spec.arguments
            if arg_spec.name in args
        }

    def _validate_type(
        self,
        callable_name: str,
        spec: ArgumentSpec,
        value: Any
    ):
        expected = spec.type

        if expected is Any:
            return value
        
        if getattr(expected, '__origin__', None) is tuple:
            return self._validate_tuple(callable_name, spec, value)

        if not isinstance(value, expected):
            raise TypeError(
                f'{callable_name}: argumento "{spec.name}" '
                f'esperado {expected}, recebido {type(value)}'
            )

        return value
    
    def _validate_tuple(
        self,
        callable_name: str,
        spec: ArgumentSpec,
        value: Any
    ):
        if not isinstance(value, tuple):
            raise TypeError(
                f'{callable_name}: argumento "{spec.name}" '
                f'esperado tuple, recebido {type(value)}'
            )

        expected_types = spec.type.__args__

        if len(value) != len(expected_types):
            raise ValueError(
                f'{callable_name}: argumento "{spec.name}" '
                f'esperado tuple de tamanho {len(expected_types)}'
            )

        for i, (v, t) in enumerate(zip(value, expected_types)):
            if not isinstance(v, t):
                raise TypeError(
                    f'{callable_name}: argumento "{spec.name}"[{i}] '
                    f'esperado {t}, recebido {type(v)}'
                )

        return value

    def _validate_custom(self, value, spec: ArgumentSpec):
        if spec.validator and not spec.validator(value):
            raise Exception(
                f"Valor inválido para argumento '{spec.name}': {value}"
            )
