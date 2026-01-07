from src.dsl.token import TokenType, TokenStream
from src.dsl.parser.sub import ArgumentParser
from src.dsl.parser import CallbackNode


class CallbackParser:
    def __init__(self, stream: TokenStream):
        self.stream = stream
        self.arg_parser = ArgumentParser(stream)

    def parse(self):
        name = self.stream.expect(TokenType.IDENT).value
        args = []

        while self.arg_parser.is_argument_start():
            args.append(self.arg_parser.parse())

        return CallbackNode(name, args)
