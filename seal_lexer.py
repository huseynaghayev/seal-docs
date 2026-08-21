# seal_lexer.py
from pygments.lexer import RegexLexer, words
from pygments.token import *

class SealLexer(RegexLexer):
    name = 'Seal'
    aliases = ['seal']
    filenames = ['*.seal']

    tokens = {
        'root': [
            (r'//.*$', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (words(('define', 'return', 'if', 'else', 'while',
                    'for', 'in', 'skip', 'stop', 'include',
                    'and', 'or', 'not', 'do', 'then'),
                   suffix=r'\b'), Keyword),
            (words(('null', 'true', 'false'), suffix=r'\b'), Keyword.Constant),
            (r'\$[a-zA-Z_][a-zA-Z0-9_]*', Name.Variable.Global),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
            (r'\d+\.\d*', Number.Float),
            (r'\d+', Number.Integer),
            (r'"[^"]*"', String.Double),
            (r"'[^']*'", String.Single),
            (r'->|\.\.\.?|[+\-*/%&|^~<>=!]=?|[(){}\[\].,?:]', Punctuation),
            (r'\s+', Text),
        ]
    }
