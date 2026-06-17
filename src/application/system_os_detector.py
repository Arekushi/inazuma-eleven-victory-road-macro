import platform

from src.application.enums import SystemOS


class SystemOSDetector:

    @staticmethod
    def detect() -> SystemOS:
        system = platform.system()

        if system == 'Windows':
            return SystemOS.WINDOWS

        if system == 'Linux':
            return SystemOS.LINUX

        raise ValueError(f'Unsupported OS: {system}')
