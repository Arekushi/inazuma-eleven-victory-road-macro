class PipelineContext:
    def __init__(self, initial_data: dict | None = None):
        self._data = initial_data.copy() if initial_data else {}

    def get(self, key: str, default=None):
        return self._data.get(key, default)

    def set(self, key: str, value):
        self._data[key] = value

    def has(self, key: str) -> bool:
        return key in self._data

    def update(self, data: dict):
        self._data.update(data)

    def all(self) -> dict:
        return self._data.copy()
