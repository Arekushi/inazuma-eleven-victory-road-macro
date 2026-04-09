from typing import Tuple
from src.enums.language import Language
from src.dsl.specs import CallableSpec, ArgumentSpec

from src.macro.rules import (
    is_image_on_screen,
    is_black_screen
)


RULE_REGISTRY: dict[str, CallableSpec] = {
    'is_image_on_screen': CallableSpec(
        name='is_image_on_screen',
        factory=lambda image_name, region=None, confidence=0.9, grayscale=True, language=None:
            lambda ctx: is_image_on_screen(
                image_name=image_name,
                language=language or ctx.get('language'),
                region=region,
                confidence=confidence,
                grayscale=grayscale
            ),
        arguments=[
            ArgumentSpec(
                name='image_name',
                type=str
            ),
            ArgumentSpec(
                name='region',
                type=Tuple[int, int, int, int],
                optional=True
            ),
            ArgumentSpec(
                name='confidence',
                type=float,
                optional=True
            ),
            ArgumentSpec(
                name='grayscale',
                type=bool,
                optional=True
            ),
            ArgumentSpec(
                name='language',
                type=Language,
                optional=True
            ),
        ]
    ),
    'is_black_screen': CallableSpec(
        name='is_black_screen',
        factory=lambda: is_black_screen
    )
}
