from lex import Lex

input = input("Enter the equation to calculate:")

lexer = Lex().get_lexer()
tokens = lexer.lex(input)

for token in tokens:
    print(token)
