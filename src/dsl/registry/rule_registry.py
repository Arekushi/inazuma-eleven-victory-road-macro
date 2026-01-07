from typing import Tuple
from src.enums.language import Language
from src.dsl.specs import CallableSpec, ArgumentSpec
from src.macro.rules import (
    has_no_spirit_left,
    passives_are_valid,
    is_image_on_screen
)


RULE_REGISTRY: dict[str, CallableSpec] = {
    'has_no_spirit_left': CallableSpec(
        name='has_no_spirit_left',
        factory=lambda: lambda ctx: has_no_spirit_left(ctx),
    ),
    'is_image_on_screen': CallableSpec(
        name='is_image_on_screen',
        factory=lambda image_name, region=None, confidence=0.9, grayscale=True, language=None:
            lambda ctx: is_image_on_screen(
                image_name=image_name,
                language=language or ctx.get('profile').language,
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
    'passives_are_valid': CallableSpec(
        name='passives_are_valid',
        factory=lambda: lambda ctx: passives_are_valid(ctx),
    ),
}
