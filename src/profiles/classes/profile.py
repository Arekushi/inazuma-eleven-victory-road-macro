from dataclasses import dataclass
from typing import Any, Dict, Optional, TypedDict

from src.profiles.classes import Macro, PassiveCriteria
from src.enums import Language


@dataclass(frozen=True)
class Profile:
    name: str
    language: Language
    macros: Optional[Dict[str, Macro]] = None
    passive_criterias: Optional[Dict[str, PassiveCriteria]] = None


class ProfileDict(TypedDict, total=False):
    name: str
    language: Language
