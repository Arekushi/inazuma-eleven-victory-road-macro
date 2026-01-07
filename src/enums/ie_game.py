from src.helpers.json import JsonSerializableEnum


class IEGame(JsonSerializableEnum):
    IE1 = ('IE1', 1)
    IE2 = ('IE2', 2)
    IE3 = ('IE3', 3)
    GO = ('GO', 4)
    GO2 = ('GO2', 5)
    GO_GALAXY = ('GO_GALAXY', 6)
    ARES = ('ARES', 7)
    ORION = ('ORION', 8)
    VICTORY_ROAD = ('VICTORY_ROAD', 9)

    def __init__(self, code: str, order: int):
        self.code = code
        self.order = order

    @property
    def json(self):
        return self.code

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            for member in cls:
                if member.code == value:
                    return member
        return None
