from lex import Lex
from parser import Parser

# take input mathematical equation from command line
input = input("Enter the equation to calculate:")

# passing the input expression to Lexer to convert into tokens
lexer = Lex().get_lexer()
tokens = lexer.lex(input)

# Calling parser module to parse the expression and perform calculations
parseGen = Parser()
parseGen.parse()
parser = parseGen.get_parser()
parser.parse(tokens).eval()
