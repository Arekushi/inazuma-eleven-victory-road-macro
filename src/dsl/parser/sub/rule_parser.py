from src.dsl.token import TokenType, TokenStream
from src.dsl.parser.sub import ActionParser, ArgumentParser, AttributeParser, CallbackParser
from src.dsl.parser import RuleNode
from src.dsl.registry import RULE_ATTRIBUTE_REGISTRY


class RuleParser:
    def __init__(self, stream: TokenStream):
        self.stream = stream
        self.action_parser = ActionParser(stream)
        self.arg_parser = ArgumentParser(stream)
        self.attr_parser = AttributeParser(stream)
        self.callback_parser = CallbackParser(stream)

    def parse(self):
        actions = []
        interval = None
        attrs = {}
        
        self.stream.expect(TokenType.LBRACKET)
        condition = self.callback_parser.parse()
        self.stream.expect(TokenType.RBRACKET)
        
        if self.stream.is_ident('every'):
            self.stream.advance()
            interval = self.arg_parser.parse()
        
        self.stream.expect(TokenType.COLON)
        self.stream.expect(TokenType.NEWLINE)
        self.stream.expect(TokenType.INDENT)
        
        while not self.stream.match(TokenType.DEDENT):
            if self._is_action_start():
                actions.append(self.action_parser.parse())
                continue
            elif self._is_attribute_start():
                name, value = self.attr_parser.parse()
                spec = RULE_ATTRIBUTE_REGISTRY.get(name)
                
                if not spec:
                    self.stream.error(f'Atributo inválido em rule: @{name}')

                attrs[name] = value
                continue
            elif self.stream.match(TokenType.NEWLINE):
                continue
            
            self.stream.error('Comando inválido dentro de rule')
        
        return RuleNode(
            condition=condition,
            actions=actions,
            interval=interval,
            goto=attrs.get('goto'),
        )

    def _is_action_start(self) -> bool:
        return self.stream.match_ident('do')
    
    def _is_attribute_start(self) -> bool:
        return self.stream.current().type is TokenType.AT
