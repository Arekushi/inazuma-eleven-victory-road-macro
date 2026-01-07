from src.dsl.parser import CallbackNode
from src.dsl.builder.sub import CallableBuilder


class ActionBuilder:
    def __init__(self, action_registry):
        self.callable_builder = CallableBuilder(action_registry)

    def build(self, node: CallbackNode):
        return self.callable_builder.build(node)
