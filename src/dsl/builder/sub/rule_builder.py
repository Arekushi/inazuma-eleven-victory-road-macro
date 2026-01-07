from src.pipeline.core import ConditionRule
from src.dsl.builder.sub import CallableBuilder, ActionBuilder
from src.dsl.parser import RuleNode


class RuleBuilder:
    def __init__(
        self,
        rule_registry,
        action_builder: ActionBuilder
    ):
        self.callable_builder = CallableBuilder(rule_registry)
        self.action_builder = action_builder

    def build(self, node: RuleNode) -> ConditionRule:
        when_callable = self.callable_builder.build(node.condition)

        actions = [
            self.action_builder.build(action)
            for action in node.actions
        ]

        return ConditionRule(
            when=when_callable,
            actions=actions,
            goto=node.goto,
            interval=node.interval
        )
