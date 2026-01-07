from typing import List

from src.dsl.token import TokenStream, TokenType, Token
from src.dsl.parser import PipelineNode
from src.dsl.parser.sub import StepParser


class Parser:
    def __init__(self, tokens: List[Token]):
        self.stream = TokenStream(tokens)
        self.step_parser = StepParser(self.stream)
    
    def parse(self):
        steps = []

        while not self.stream.at_end():
            if self.stream.match(TokenType.NEWLINE):
                continue

            if self._is_step_start():
                steps.append(self.step_parser.parse())
                continue

            self.stream.error('Esperado nome de step')

        return PipelineNode(steps)

    def _is_step_start(self):
        return (
            self.stream.current().type is TokenType.STRING
            and self.stream.peek().type is TokenType.COLON
        )
