from enum import Enum


class FileExt(Enum):
    JSON = 'json'
    VML = 'vml'
    TOML = 'toml'
    CSV = 'csv'
    PNG = 'png'
    
    def __str__(self) -> str:
        return self.value
