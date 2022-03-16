from antlr4 import *
from mathVisitor import mathVisitor
from antlr_generated.mathlangLexer import mathlangLexer
from antlr_generated.mathlangParser import mathlangParser
def main():
    input_stream = StdinStream()
    lexer = mathlangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mathlangParser(stream)
    tree = parser.start()
    vis = mathVisitor()
    output = vis.visit(tree)
    print("Result:" , output)

if __name__ == "__main__":
    main()