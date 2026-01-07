from pathlib import Path

from src.helpers.fs.exceptions import (
    DirectoryNotFoundException,
    NotADirectory,
    DirectoryRenameException,
    DirectoryAlreadyExists,
    FileOperationException
)


def rename_dir(
    src: str | Path,
    new_name: str,
    *,
    overwrite: bool = False
) -> Path:
    src = Path(src).expanduser().resolve()

    if not src.exists():
        raise DirectoryNotFoundException(f'Diretório não encontrado: {src}')

    if not src.is_dir():
        raise NotADirectory(f'Não é um diretório: {src}')

    if '/' in new_name or '\\' in new_name:
        raise ValueError('new_name deve ser apenas o nome do diretório')

    dst = src.with_name(new_name)

    if dst.exists():
        if not overwrite:
            raise DirectoryAlreadyExists(f'Diretório já existe: {dst}')
        if not dst.is_dir():
            raise DirectoryRenameException(
                f'O destino existe e não é um diretório: {dst}'
            )

    src.rename(dst)
    return dst


def rename_file(
    path: str | Path,
    new_name: str,
    *,
    overwrite: bool = False
) -> Path:
    path = Path(path).expanduser().resolve()

    if not path.exists():
        raise FileOperationException(f'Arquivo não encontrado: {path}')

    if not path.is_file():
        raise FileOperationException(f'Não é um arquivo: {path}')

    new_path = path.with_name(new_name)

    if new_path.exists() and not overwrite:
        raise FileOperationException(f'Arquivo já existe: {new_path}')

    return path.rename(new_path)
