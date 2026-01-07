import shutil
from pathlib import Path


def copy_dir(src: str | Path, dst: str | Path, overwrite: bool = False):
    src = Path(src)
    dst = Path(dst)

    if dst.exists():
        if overwrite:
            shutil.rmtree(dst)
        else:
            raise FileExistsError(f'Diretório já existe: {dst}')

    shutil.copytree(src, dst)
