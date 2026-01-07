from src.dsl.token import TokenType, TokenStream
from src.dsl.parser.sub import ActionParser, AttributeParser, RuleParser
from src.dsl.parser import StepNode
from src.dsl.registry import STEP_ATTRIBUTE_REGISTRY


class StepParser:
    def __init__(self, stream: TokenStream):
        self.stream = stream
        self.action_parser = ActionParser(stream)
        self.rule_parser = RuleParser(stream)
        self.attr_parser = AttributeParser(stream)

    def parse(self):
        step_name = self.stream.expect(TokenType.STRING).value
        
        self.stream.expect(TokenType.COLON)
        self.stream.expect(TokenType.NEWLINE)
        self.stream.expect(TokenType.INDENT)
        
        actions = []
        rules = []
        attrs = {}

        while not self.stream.match(TokenType.DEDENT):
            if self.stream.match(TokenType.NEWLINE):
                continue

            if self._is_attribute_start():
                name, value = self.attr_parser.parse()

                spec = STEP_ATTRIBUTE_REGISTRY.get(name)
                if not spec:
                    self.stream.error(f'Atributo inválido em step: @{name}')

                attrs[name] = value
                continue
            
            if self._is_action_start():
                actions.append(self.action_parser.parse())
                continue
            
            if self._is_rule_start():
                rules.append(self.rule_parser.parse())
                continue
            
            self.stream.error('Item inválido dentro do Step')

        return StepNode(
            name=step_name,
            actions=actions,
            rules=rules,
            label=attrs.get('label'),
            delay=attrs.get('delay'),
            goto=attrs.get('goto'),
            repeat=attrs.get('repeat'),
            timeout=attrs.get('timeout')
        )

    def _is_action_start(self) -> bool:
        return self.stream.match_ident('do')

    def _is_rule_start(self) -> bool:
        return self.stream.match_ident('when')

    def _is_attribute_start(self) -> bool:
        return self.stream.current().type is TokenType.AT
