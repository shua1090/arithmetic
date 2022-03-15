# Generated from luxlang.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .luxlangParser import luxlangParser
else:
    from luxlangParser import luxlangParser

# This class defines a complete listener for a parse tree produced by luxlangParser.
class luxlangListener(ParseTreeListener):

    # Enter a parse tree produced by luxlangParser#start.
    def enterStart(self, ctx:luxlangParser.StartContext):
        pass

    # Exit a parse tree produced by luxlangParser#start.
    def exitStart(self, ctx:luxlangParser.StartContext):
        pass


    # Enter a parse tree produced by luxlangParser#Number.
    def enterNumber(self, ctx:luxlangParser.NumberContext):
        pass

    # Exit a parse tree produced by luxlangParser#Number.
    def exitNumber(self, ctx:luxlangParser.NumberContext):
        pass


    # Enter a parse tree produced by luxlangParser#AdditionOrSubtraction.
    def enterAdditionOrSubtraction(self, ctx:luxlangParser.AdditionOrSubtractionContext):
        pass

    # Exit a parse tree produced by luxlangParser#AdditionOrSubtraction.
    def exitAdditionOrSubtraction(self, ctx:luxlangParser.AdditionOrSubtractionContext):
        pass


    # Enter a parse tree produced by luxlangParser#MultiplicationOrDivision.
    def enterMultiplicationOrDivision(self, ctx:luxlangParser.MultiplicationOrDivisionContext):
        pass

    # Exit a parse tree produced by luxlangParser#MultiplicationOrDivision.
    def exitMultiplicationOrDivision(self, ctx:luxlangParser.MultiplicationOrDivisionContext):
        pass


    # Enter a parse tree produced by luxlangParser#Parentheses.
    def enterParentheses(self, ctx:luxlangParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by luxlangParser#Parentheses.
    def exitParentheses(self, ctx:luxlangParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by luxlangParser#Power.
    def enterPower(self, ctx:luxlangParser.PowerContext):
        pass

    # Exit a parse tree produced by luxlangParser#Power.
    def exitPower(self, ctx:luxlangParser.PowerContext):
        pass



del luxlangParser