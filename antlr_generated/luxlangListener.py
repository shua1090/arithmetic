# Generated from luxlang.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .luxlangParser import luxlangParser
else:
    from luxlangParser import luxlangParser

# This class defines a complete listener for a parse tree produced by luxlangParser.
class luxlangListener(ParseTreeListener):
    dictionary = {}

    # Enter a parse tree produced by luxlangParser#program.
    def enterProgram(self, ctx:luxlangParser.ProgramContext):
        print("Entering Program")
        pass

    # Exit a parse tree produced by luxlangParser#program.
    def exitProgram(self, ctx:luxlangParser.ProgramContext):
        print("Exiting Program")
        pass


    # Enter a parse tree produced by luxlangParser#statement.
    def enterStatement(self, ctx:luxlangParser.StatementContext):
        pass

    # Exit a parse tree produced by luxlangParser#statement.
    def exitStatement(self, ctx:luxlangParser.StatementContext):
        pass


    # Enter a parse tree produced by luxlangParser#let.
    def enterLet(self, ctx:luxlangParser.LetContext):
        pass

    # Exit a parse tree produced by luxlangParser#let.
    def exitLet(self, ctx:luxlangParser.LetContext):
        if ctx.VAR() != None:
            self.dictionary[ctx.VAR().getText()] = int(ctx.INT().getText())


    # Enter a parse tree produced by luxlangParser#show.
    def enterShow(self, ctx:luxlangParser.ShowContext):
        pass

    # Exit a parse tree produced by luxlangParser#show.
    def exitShow(self, ctx:luxlangParser.ShowContext):
        if ctx.INT() != None:
            print(ctx.INT().getText())
        elif ctx.VAR() != None:
            try:
                print(self.dictionary[ctx.VAR().getText()])
            except KeyError:
                print("VARIABLE", ctx.VAR(), "NOT FOUND")


del luxlangParser