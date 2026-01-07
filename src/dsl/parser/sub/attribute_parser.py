from src.dsl.token import TokenType, TokenStream
from src.dsl.parser.sub import ArgumentParser


class AttributeParser:
    def __init__(self, stream: TokenStream):
        self.stream = stream
        self.arg_parser = ArgumentParser(stream)

    def parse(self):
        self.stream.expect(TokenType.AT)
        name = self.stream.expect(TokenType.IDENT).value
        value = self.arg_parser.parse()
        return name, value
