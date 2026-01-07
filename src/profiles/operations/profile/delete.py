from config.paths import Paths
from src.helpers.fs.deleting import delete_dir


def delete_profile(profile_name: str):
    delete_dir(
        path=Paths.PROFILES / profile_name,
        must_exist=False
    )
