class PassiveCriteriaNotFoundException(Exception):
    def __init__(self, criteria: str, profile: str):
        super().__init__(
            f"Passive criteria '{criteria}' não existe no profile '{profile}'"
        )
        self.criteria = criteria
        self.profile = profile
