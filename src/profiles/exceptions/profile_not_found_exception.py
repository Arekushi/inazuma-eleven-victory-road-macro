from pathlib import Path


class ProfileNotFoundException(FileNotFoundError):
    def __init__(self, name: str, base_path: Path):
        super().__init__(
            f"Profile '{name}' não encontrado em {base_path}"
        )
        self.name = name
        self.base_path = base_path
