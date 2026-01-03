from logging import Logger
from typing import Dict, Optional

from .logger_config import LoggerConfig
from .logger import AppLogger


class LoggerFactory:
    _loggers: Dict[str, Logger] = {}

    @classmethod
    def get_logger(
        cls,
        name: str = __name__,
        config: Optional[LoggerConfig] = None
    ) -> Logger:        
        if name not in cls._loggers:
            if config is None:
                config = LoggerConfig(
                    name=__name__,
                    log_filename=__name__
                )
            
            cls._loggers[name] = AppLogger(config).get_logger()

        return cls._loggers[name]
