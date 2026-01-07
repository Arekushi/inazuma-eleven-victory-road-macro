from typing import Dict
from src.dsl.specs import AttributeSpec


STEP_ATTRIBUTE_REGISTRY: Dict[str, AttributeSpec] = {
    'delay': AttributeSpec(
        name='delay'
    ),
    'timeout': AttributeSpec(
        name='timeout'
    ),
    'repeat': AttributeSpec(
        name='repeat'
    ),
    'goto': AttributeSpec(
        name='goto'
    ),
    'name': AttributeSpec(
        name='name'
    ),
    'label': AttributeSpec(
        name='label'
    ),
}
