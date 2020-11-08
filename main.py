from lex import Lex
from parser import Parser
import re

input = input("Enter the equation to calculate:")
# left = input.split('(')[0] + '('
# right = ')' + input.split(')')[1]
# numbers = re.findall('\d+', input.split('(')[1].split(')')[0])
# operator = re.findall('[\+\-\*\/]', input.split('(')[1].split(')')[0])
# expression = ''
#
# for i in range(len(numbers),1,-1):
#     expression += (numbers[i-1]+operator[i-2])
# expression = expression + numbers[0]
# input = left + expression + right

lexer = Lex().get_lexer()
tokens = lexer.lex(input)

# for token in tokens:
#     print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
