from pathlib import Path

from src.dsl.builder import PipelineBuilder
from src.dsl.lexer import Lexer
from src.dsl.parser import Parser


class PipelineCompiler:
    @staticmethod
    def compile_file(path: Path, encoding='utf-8'):
        text = path.read_text(encoding=encoding)
        return PipelineCompiler.compile_text(text)
    
    @staticmethod
    def compile_text(text: str):
        lexer = Lexer(text)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        ast = parser.parse()

        builder = PipelineBuilder(ast)
        return builder.build()
