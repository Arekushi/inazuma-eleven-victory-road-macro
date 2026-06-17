import platform
from src.application.enums import SystemOS


class SystemInfo:
    @staticmethod
    def get_os() -> SystemOS:
        system = platform.system()

        if system == 'Windows':
            return SystemOS.WINDOWS

        if system == 'Linux':
            return SystemOS.LINUX

        raise RuntimeError(
            f'Unsupported operating system: {system}'
        )
