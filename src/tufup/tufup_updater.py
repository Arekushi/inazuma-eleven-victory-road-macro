from pathlib import Path
from string import Template
from tufup.client import Client
from rich.console import Console

from config import settings, Paths
from src.tufup import GithubRepository
from src.tufup.dataclasses import UpdateInfo
from src.helpers.fs import create_dir


console = Console()


class TufupUpdater:
    def __init__(
        self,
        install_dir = '.'
    ):
        self.app_name = settings.GITHUB.repo
        self.current_version = settings.GITHUB.app_version
        self.install_dir = Path(install_dir)
        self.metadata_dir = Paths.METADATA

        self.repository = GithubRepository(
            owner=settings.GITHUB.owner,
            repo=settings.GITHUB.repo,
        )

        self._client = None

    @property
    def client(self) -> Client:
        if self._client is None:
            release = self.repository.get_latest_release()

            self._client = Client(
                app_name=self.app_name,
                app_install_dir=self.install_dir,
                target_dir=Paths.TEMP,
                current_version=self.current_version,
                metadata_dir=self.metadata_dir,
                metadata_base_url=release.metadata_base_url,
                target_base_url=release.target_base_url,
            )

        return self._client

    def check_update(self) -> UpdateInfo | None:
        update = self.client.check_for_updates()

        if update is None:
            return None

        return UpdateInfo(
            version=update.version,
        )

    def update(self):
        update_info = self.check_update()
        
        if update_info:
            console.print(
                Template(settings.CLI.TUFUP.has_update)
                    .safe_substitute({'version': update_info.version})
            )
            console.print(settings.CLI.TUFUP.please_confirm)
            create_dir(Paths.TEMP)
            self.client.download_and_apply_update()
            return True

        return False
