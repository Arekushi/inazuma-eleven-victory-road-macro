from dataclasses import dataclass


@dataclass
class ReleaseInfo:
    version: str
    tag: str
    metadata_base_url: str
    target_base_url: str
