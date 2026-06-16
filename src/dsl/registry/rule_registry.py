from src.dsl.specs import CallableSpec, ArgumentSpec

from src.vision.dataclasses import Region
from src.vision.enums import HorizontalAnchor
from src.macro.rules import (
    is_image_on_screen
)


RULE_REGISTRY: dict[str, CallableSpec] = {
    'is_image_on_screen': CallableSpec(
        name='is_image_on_screen',
        factory=lambda image_name, region=None, horizontal_anchor=HorizontalAnchor.LEFT, confidence=0.9:
            lambda ctx: is_image_on_screen(
                image_name=image_name,
                region=Region(*region, horizontal_anchor),
                confidence=confidence
            ),
        arguments=[
            ArgumentSpec(
                name='image_name',
                type=str
            ),
            ArgumentSpec(
                name='region',
                type=tuple,
                optional=True
            ),
            ArgumentSpec(
                name='horizontal_anchor',
                type=HorizontalAnchor,
                optional=True
            ),
            ArgumentSpec(
                name='confidence',
                type=float,
                optional=True
            )
        ]
    )
}
