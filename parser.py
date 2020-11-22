
from rply import ParserGenerator
from ast import *

class Parser():
    # Provide list of tokens acceptable for the parser.
    # Also define precedence of operators and evaluate expression from left to right.
    def __init__(self):
        self.parseGen = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'LEFT_PAREN', 'RIGHT_PAREN',
             'EOL', 'SUM', 'SUB', 'MUL', 'DIV'],
            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV'])
            ]
        )

    def parse(self):
        # Defining the input expression grammar using decorator method production
        @self.parseGen.production('INPUT : PRINT LEFT_PAREN expression RIGHT_PAREN EOL')
        def program(exp):
            return Print(exp[2])

        @self.parseGen.production('expression : expression SUM expression')
        @self.parseGen.production('expression : expression SUB expression')
        @self.parseGen.production('expression : expression MUL expression')
        @self.parseGen.production('expression : expression DIV expression')
        def expression(exp):
            left = exp[0]
            right = exp[2]
            operator = exp[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)


        @self.parseGen.production('expression : NUMBER')
        def number(exp):
            return Number(exp[0].value)

        @self.parseGen.error
        def error_handle(token):
            raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())



    def get_parser(self):
        return self.parseGen.build()
