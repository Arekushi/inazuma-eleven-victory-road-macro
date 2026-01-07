import shutil
from pathlib import Path

from src.helpers.fs.exceptions import (
    DirectoryNotFoundException,
    NotADirectory,
    FileOperationException
)


def delete_dir(path: str | Path, *, must_exist: bool = True):
    path = Path(path).expanduser().resolve()

    if not path.exists():
        if must_exist:
            raise DirectoryNotFoundException(f'Diretório não encontrado: {path}')
        return

    if not path.is_dir():
        raise NotADirectory(f'Não é um diretório: {path}')

    shutil.rmtree(path)


def delete_file(path: str | Path) -> None:
    path = Path(path).expanduser().resolve()

    if not path.exists():
        raise FileOperationException(f'Arquivo não encontrado: {path}')

    if not path.is_file():
        raise FileOperationException(f'Não é um arquivo: {path}')

    path.unlink()
