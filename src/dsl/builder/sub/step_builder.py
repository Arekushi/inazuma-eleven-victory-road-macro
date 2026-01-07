from src.dsl.builder.sub import RuleBuilder, ActionBuilder
from src.dsl.parser import StepNode
from src.pipeline.core import Step
from src.dsl.registry import RULE_REGISTRY, ACTION_REGISTRY


class StepBuilder:
    def __init__(self):
        self.action_builder = ActionBuilder(ACTION_REGISTRY)
        self.rule_builder = RuleBuilder(RULE_REGISTRY, self.action_builder)

    def build(self, node: StepNode) -> Step:
        actions = [
            self.action_builder.build(action)
            for action in node.actions
        ]

        rules = [
            self.rule_builder.build(rule)
            for rule in node.rules
        ]

        return Step(
            name=node.name,
            label=node.label,
            actions=actions,
            rules=rules,
            delay_after=node.delay or 0.0,
            timeout=node.timeout or 30.0,
            repeat=node.repeat or 1,
            goto=node.goto,
        )
