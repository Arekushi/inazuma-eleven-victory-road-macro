import logging
from rich.console import Console
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class LoggerConfig:
    log_filename: str
    name: str = __name__
    level: int = logging.INFO
    log_to_console: bool = True
    log_to_file: bool = True
    rich_console: Console | None = None
