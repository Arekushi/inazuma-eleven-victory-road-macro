from src.dsl.parser.sub import CallbackParser
from src.dsl.token import TokenStream, TokenType


class ActionParser:
    def __init__(self, stream: TokenStream):
        self.stream = stream
        self.callback_parser = CallbackParser(stream)

    def parse(self):
        self.stream.expect(TokenType.LBRACKET)

        callback = self.callback_parser.parse()

        self.stream.expect(TokenType.RBRACKET)
        self.stream.expect(TokenType.NEWLINE)

        return callback
