import requests

from src.tufup.dataclasses import ReleaseInfo


class GithubRepository:
    def __init__(
        self,
        owner: str,
        repo: str,
        timeout: float = 10.0,
    ):
        self.owner = owner
        self.repo = repo
        self.timeout = timeout
        self._release_info = None

    @property
    def api_url(self) -> str:
        return (
            f'https://api.github.com/repos/'
            f'{self.owner}/{self.repo}/releases/latest'
        )

    @property
    def metadata_url(self):
        return self.get_latest_release().metadata_base_url

    @property
    def target_url(self):
        return self.get_latest_release().target_base_url

    @property
    def latest_version(self):
        return self.get_latest_release().version

    def get_latest_release(self):
        if self._release_info is None:
            self._release_info = self._fetch_release()

        return self._release_info

    def _fetch_release(self) -> ReleaseInfo:
        response = requests.get(
            self.api_url,
            timeout=self.timeout,
        )
        response.raise_for_status()

        release = response.json()

        tag = release['tag_name']
        version = tag.removeprefix('v')

        base_url = (
            f'https://github.com/'
            f'{self.owner}/'
            f'{self.repo}/'
            f'releases/download/'
            f'{tag}'
        )

        return ReleaseInfo(
            version=version,
            tag=tag,
            metadata_base_url=base_url,
            target_base_url=base_url,
        )
