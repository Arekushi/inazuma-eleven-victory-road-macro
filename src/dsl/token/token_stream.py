from typing import List

from src.dsl.token import Token, TokenType


class TokenStream:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def peek(self, offset=1):
        return self.tokens[self.pos + offset]

    def advance(self):
        self.pos += 1

    def match(self, *types: TokenType):
        if self.current().type in types:
            tok = self.current()
            self.pos += 1
            return tok
        return None

    def expect(self, type_: TokenType):
        tok = self.match(type_)
        if not tok:
            self.error(f'Esperado {type_.name}')
        return tok

    def at_end(self):
        return self.current().type == TokenType.EOF

    def error(self, msg):
        tok = self.current()
        raise SyntaxError(f'[Linha {tok.line}] {msg}')
    
    def is_ident(self, value: str | None = None) -> bool:
        if self.current().type is not TokenType.IDENT:
            return False
        return value is None or self.current().value == value

    def match_ident(self, value: str) -> bool:
        if self.is_ident(value):
            self.advance()
            return True
        return False
