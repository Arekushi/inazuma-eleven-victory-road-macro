import logging
from logging.handlers import RotatingFileHandler
from typing import List

from rich.logging import RichHandler
from rich.console import Console
from config.paths import Paths
from src.logging import LoggerConfig
from src.logging.formatters import PipelineFileFormatter, PipelineConsoleFormatter
from src.logging.filters import TemplateFilter


class AppLogger:
    def __init__(self, config: LoggerConfig):
        self.config = config
        self.logger = logging.getLogger(config.name)
        self.logger.setLevel(config.level)
        self.logger.addFilter(TemplateFilter())

        if self.logger.handlers:
            return

        if config.log_to_file:
            self._add_file_handler(
                config.log_filename, filters=[]
            )

        if config.log_to_console:
            self._add_rich_console_handler(
                config.rich_console, filters=[]
            )

    def _add_file_handler(
        self,
        log_filename: str,
        filters: List[logging.Filter]
    ):
        log_path = Paths.TEMP / f'{log_filename}.log'
        log_path.parent.mkdir(parents=True, exist_ok=True)

        formatter = PipelineFileFormatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
        )

        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding='utf-8',
        )
        file_handler.setFormatter(formatter)

        for filter in filters:
            file_handler.addFilter(filter)

        self.logger.addHandler(file_handler)

    def _add_rich_console_handler(
        self,
        console: Console | None,
        filters: List[logging.Filter]
    ):
        rich_handler = RichHandler(
            console=console,
            show_time=True,
            markup=True,
            show_level=True,
            show_path=False,
            rich_tracebacks=True,
        )

        rich_handler.setFormatter(
            PipelineConsoleFormatter('%(message)s')
        )

        for filter in filters:
            rich_handler.addFilter(filter)

        self.logger.addHandler(rich_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger
