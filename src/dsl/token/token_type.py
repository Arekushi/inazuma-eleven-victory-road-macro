from enum import Enum


class TokenType(Enum):
    STRING = 'STRING'
    NUMBER = 'NUMBER'
    IDENT = 'IDENT'
    BOOLEAN = 'BOOLEAN'
    LBRACKET = 'LBRACKET'
    RBRACKET = 'RBRACKET'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    COMMA = 'COMMA'
    COLON = 'COLON'
    PIPE = 'PIPE'
    AT = 'AT'
    NEWLINE = 'NEWLINE'
    INDENT = 'INDENT'
    DEDENT = 'DEDENT'
    EOF = 'EOF'
