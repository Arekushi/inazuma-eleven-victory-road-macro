from pathlib import Path
from typing import List
from src.enums import FileExt


def list_filenames_by_extension(path: Path, ext: FileExt) -> List[str]:
    return [p.stem for p in path.glob(f"*{ext.value}")]


def list_files(path: Path) -> List[Path]:
    return [p for p in path.iterdir() if p.is_file()]


def list_filenames(path: Path) -> List[str]:
    return [p.name for p in path.iterdir() if p.is_file()]


def list_filenames_stem(path: Path) -> List[str]:
    return [p.stem for p in path.iterdir() if p.is_file()]


def list_dir(path: Path) -> List[Path]:
    return [p for p in path.iterdir() if p.is_dir()]


def list_dir_names(path: Path) -> List[str]:
    return [p.name for p in path.iterdir() if p.is_dir()]
