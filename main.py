import sys
from antlr4 import *
from luxListener import luxListener
from antlr_generated.luxlangLexer import luxlangLexer
from antlr_generated.luxlangParser import luxlangParser
def main(argv):
    input_stream = StdinStream()
    lexer = luxlangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = luxlangParser(stream)
    parser.addParseListener(luxListener())
    tree = parser.program()

if __name__ == '__main__':
    main(sys.argv)