from rply import LexerGenerator

class Lex():
    def __init__(self):
        self.lex = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lex.add('PRINT', r'print')
        # Parenthesis
        self.lex.add('LEFT_PAREN', r'\(')
        self.lex.add('RIGHT_PAREN', r'\)')
        # End of line
        self.lex.add('EOL', r'\;')
        # Mathematical Operators
        self.lex.add('SUM', r'\+')
        self.lex.add('SUB', r'\-')
        self.lex.add('MUL', r'\*')
        self.lex.add('DIV', r'\/')
        # Number
        self.lex.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lex.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lex.build()