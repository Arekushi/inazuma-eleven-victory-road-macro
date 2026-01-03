from logging import Logger
from typing import Optional

from src.logging import LoggerFactory


class PipelineContext:
    def __init__(
        self,
        initial_data: Optional[dict] = None,
        logger: Optional[Logger] = None
    ):
        self._data = initial_data.copy() if initial_data else {}
        self._logger = logger or LoggerFactory.get_logger(__name__)

    @property
    def logger(self) -> Logger:
        return self._logger

    def get(self, key: str, default=None):
        return self._data.get(key, default)

    def set(self, key: str, value):
        self._data[key] = value

    def has(self, key: str) -> bool:
        return key in self._data

    def update(self, data: dict):
        self._data.update(data)
    
    def pop(self, key: str, default=None):
        if self.has(key):
            return self._data.pop(key)
        
        return default

    def all(self) -> dict:
        return self._data.copy()
