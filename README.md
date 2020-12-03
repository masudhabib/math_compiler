# math_compiler in Python

- Toy compiler performs basic mathematical calculations like addition, subtraction, multiplication and division.
- The code uses RPLY python package to implement lexer and Parser using LexerGenerator and ParserGenerator modules.
- Parsing also follows precedence rule defined by BODMAS and does not have any limitations on number of operands and digits in the operands.
EBNF is used to define the grammar.

- The code is divided in 3 modules. Each module contains Parser, Lexer and AST tree builder.

## Compiling from source code

### Pre-requisites for build.run
- Any OS with Python 2 interpreter
- Python IDE (Pycharm)

### Executing the program

- Run the program by executing ```Main.py``` file in Pycharm
- Provide the input in following format:
Input follows the grammer "PRINT LEFT_PAREN expression RIGHT_PAREN EOL" and format should be followed.
 * ```print(45+22-9);```
 * ```print(45+22-9);```
 * ```print(4*2-1);```
 * ```print(2*8/4);```
 * ```print(6/3*2+12);```
