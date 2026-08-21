from setuptools import setup

setup(
    name='seallexer',
    version='0.1',
    py_modules=['seal_lexer'],
    entry_points='''
    [pygments.lexers]
    seal = seal_lexer:SealLexer
    ''',
)
