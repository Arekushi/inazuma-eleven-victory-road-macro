from typing import Dict
from src.dsl.specs import AttributeSpec


RULE_ATTRIBUTE_REGISTRY: Dict[str, AttributeSpec] = {
    'goto': AttributeSpec(
        name='goto'
    )
}
