from src.application.enums import SystemOS
from src.window.dataclasses import BackendKey
from src.window.enums import WindowingSys
from src.window.interfaces import BaseWindowBackend


class WindowBackendRegistry:
    _registry: dict[BackendKey, type[BaseWindowBackend]] = {}
    _instances: dict[BackendKey, BaseWindowBackend] = {}

    @classmethod
    def register(cls, os: SystemOS, windowing_sys: WindowingSys):
        def wrapper(backend_cls):
            cls._registry[BackendKey(os, windowing_sys)] = backend_cls
            return backend_cls
        return wrapper

    @classmethod
    def get(
        cls,
        os: SystemOS,
        windowing_sys: WindowingSys
    ) -> BaseWindowBackend:
        key = BackendKey(os, windowing_sys)

        if key not in cls._instances:
            backend_cls = cls._registry.get(key)

            if backend_cls is None:
                raise ValueError(
                    f'No backend for {os} + {windowing_sys}'
                )

            cls._instances[key] = backend_cls()

        return cls._instances[key]
