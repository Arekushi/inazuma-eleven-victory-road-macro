from src.passives.enums import PassiveQualityCriteria
from src.passives.classes import PassiveValues
from src.passives.ocr import normalize_passive_text, resolve_value_placeholder


def is_expected_passive_text(
    ocr_text: str,
    passive_text: str,
    passive_values: PassiveValues,
    passive_quality: PassiveQualityCriteria
) -> bool:
    if not ocr_text:
        return False

    ocr_norm = normalize_passive_text(ocr_text)
    passive_text_norm = normalize_passive_text(passive_text)

    expected_texts: set[str] = set()

    if passive_quality in (PassiveQualityCriteria.HIGH, PassiveQualityCriteria.ANY):
        expected_texts.add(
            resolve_value_placeholder(passive_text_norm, passive_values.high)
        )

    if passive_quality == PassiveQualityCriteria.ANY:
        expected_texts.add(
            resolve_value_placeholder(passive_text_norm, passive_values.low)
        )

    return ocr_norm in expected_texts
