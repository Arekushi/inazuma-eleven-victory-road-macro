from typing import Any
from src.dsl.token import TokenStream, TokenType


class ArgumentParser:
    def __init__(self, stream: TokenStream):
        self.stream = stream

    def parse(self) -> Any:
        tok = self.stream.current()

        if tok.type is TokenType.STRING:
            self.stream.advance()
            return tok.value

        if tok.type is TokenType.NUMBER:
            return self._parse_number_or_duration()

        if tok.type is TokenType.BOOLEAN:
            self.stream.advance()
            return tok.value

        if tok.type is TokenType.LPAREN:
            return self._parse_tuple()

        if tok.type is TokenType.IDENT:
            self.stream.advance()
            return tok.value

        self.stream.error('Argumento inválido')
    
    def is_argument_start(self) -> bool:
        return self.stream.current().type in {
            TokenType.STRING,
            TokenType.NUMBER,
            TokenType.BOOLEAN,
            TokenType.IDENT,
            TokenType.LPAREN,
        }
    
    def _parse_number_or_duration(self):
        number = self.stream.expect(TokenType.NUMBER).value

        if self._is_duration_unit():
            self.stream.advance()
            return float(number)

        return number

    def _parse_tuple(self):
        values = []
        self.stream.expect(TokenType.LPAREN)

        while True:
            values.append(self.parse())

            if self.stream.match(TokenType.COMMA):
                continue
            break

        self.stream.expect(TokenType.RPAREN)
        return tuple(values)

    def _is_duration_unit(self) -> bool:
        return (
            self.stream.current().type is TokenType.IDENT
            and self.stream.current().value == 's'
        )
