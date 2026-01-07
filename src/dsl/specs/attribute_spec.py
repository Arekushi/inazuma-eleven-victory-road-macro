from dataclasses import dataclass


@dataclass(frozen=True)
class AttributeSpec:
    name: str
