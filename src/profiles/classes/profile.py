from dataclasses import dataclass
from typing import Dict, Optional, TypedDict

from src.profiles.classes import Macro
from src.enums import Language


@dataclass(frozen=True)
class Profile:
    name: str
    language: Language
    macros: Optional[Dict[str, Macro]] = None


class ProfileDict(TypedDict, total=False):
    name: str
    language: Language
