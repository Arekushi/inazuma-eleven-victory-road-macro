class StepNavigator:
    def __init__(self):
        self.goto: str | None = None
        self._decided = False

    def go_to(self, label: str):
        self.goto = label
        self._decided = True

    def next(self):
        self.goto = None
        self._decided = True

    def has_target(self) -> bool:
        return self._decided
