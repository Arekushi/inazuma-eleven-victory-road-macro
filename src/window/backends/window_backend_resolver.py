from src.application import SystemOSDetector, WindowingSystemDetector
from src.window.backends import WindowBackendRegistry
from src.window.interfaces import BaseWindowBackend


class WindowBackendResolver:

    @staticmethod
    def resolve() -> BaseWindowBackend:
        os = SystemOSDetector.detect()
        windowing_sys = WindowingSystemDetector.detect()

        return WindowBackendRegistry.get(os, windowing_sys)
