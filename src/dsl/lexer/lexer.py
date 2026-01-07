import re
import ast
from src.dsl.token import TokenType, Token


class Lexer:
    INDENT_WIDTH = 4

    TOKEN_REGEX = re.compile(
        r'''
            (?P<STRING>"([^"\\]|\\.)*")
        |   (?P<BOOLEAN>\btrue\b|\bfalse\b)
        |   (?P<NUMBER>\d+\.\d+|\d+)
        |   (?P<IDENT>[A-Za-z_][A-Za-z0-9_-]*)
        |   (?P<LBRACKET>\[)
        |   (?P<RBRACKET>\])
        |   (?P<LPAREN>\()
        |   (?P<RPAREN>\))
        |   (?P<COMMA>,)
        |   (?P<COLON>:)
        |   (?P<PIPE>\|)
        |   (?P<AT>@)
        ''',
        re.VERBOSE | re.IGNORECASE
    )

    def __init__(self, text: str):
        self.lines = text.splitlines()
        self.line_no = 0
        self.indents = [0]
        self.tokens: list[Token] = []
    
    def tokenize(self) -> list[Token]:
        for self.line_no, raw in enumerate(self.lines, start=1):
            if raw.strip() == '' or raw.lstrip().startswith('#'):
                continue

            self._handle_indent(raw)
            self._tokenize_line(raw.lstrip())

            self.tokens.append(Token(TokenType.NEWLINE, None, self.line_no, 0))

        self._finalize_indents()
        self.tokens.append(Token(TokenType.EOF, None, self.line_no + 1, 0))
        return self.tokens

    def _handle_indent(self, line: str):
        spaces = len(line) - len(line.lstrip(' '))

        if spaces % self.INDENT_WIDTH != 0:
            raise SyntaxError(
                f'Linha {self.line_no}: indentação inválida'
            )

        if spaces > self.indents[-1]:
            self.indents.append(spaces)
            self.tokens.append(Token(TokenType.INDENT, None, self.line_no, 0))
        else:
            while spaces < self.indents[-1]:
                self.indents.pop()
                self.tokens.append(Token(TokenType.DEDENT, None, self.line_no, 0))

    def _tokenize_line(self, line: str):
        pos = 0
        length = len(line)

        while pos < length:
            if line[pos].isspace():
                pos += 1
                continue

            match = self.TOKEN_REGEX.match(line, pos)
            if not match:
                raise SyntaxError(
                    f'Linha {self.line_no}: token inválido'
                )

            group_name = match.lastgroup
            kind = TokenType[group_name]
            value = match.group(group_name)

            if kind is TokenType.STRING:
                value = ast.literal_eval(value)
            elif kind is TokenType.NUMBER:
                value = float(value) if '.' in value else int(value)
            elif kind == TokenType.BOOLEAN:
                value = value.lower() == 'true'

            self.tokens.append(Token(kind, value, self.line_no, pos))
            pos = match.end()

    def _finalize_indents(self):
        while len(self.indents) > 1:
            self.indents.pop()
            self.tokens.append(Token(TokenType.DEDENT, None, self.line_no, 0))
