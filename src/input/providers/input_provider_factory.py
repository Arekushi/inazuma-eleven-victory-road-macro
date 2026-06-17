from src.input.providers import BaseInputProvider
from src.application.enums import SystemOS
from src.input.enums import InputMode
from src.input.dataclasses import ProviderKey


class InputProviderFactory:
    _registry: dict[ProviderKey, type] = {}
    
    @classmethod
    def register(cls, os: SystemOS, mode: InputMode):
        def wrapper(provider_cls):
            cls._registry[ProviderKey(os, mode)] = provider_cls
            return provider_cls
        return wrapper
    
    @classmethod
    def create(cls, os: SystemOS, input_mode: InputMode) -> BaseInputProvider:
        key = ProviderKey(os, input_mode)
        provider_cls = cls._registry.get(key)

        if not provider_cls:
            raise ValueError(f'No provider for {os} + {input_mode}')

        return provider_cls()
