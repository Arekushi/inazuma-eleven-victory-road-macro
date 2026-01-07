from enum import Enum


class JsonSerializableEnum(Enum):
    @property
    def json(self):
        return self.value[0]
