# Generated from mathlang.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mathlangParser import mathlangParser
else:
    from mathlangParser import mathlangParser

# This class defines a complete listener for a parse tree produced by mathlangParser.
class mathlangListener(ParseTreeListener):

    # Enter a parse tree produced by mathlangParser#start.
    def enterStart(self, ctx:mathlangParser.StartContext):
        pass

    # Exit a parse tree produced by mathlangParser#start.
    def exitStart(self, ctx:mathlangParser.StartContext):
        pass


    # Enter a parse tree produced by mathlangParser#Number.
    def enterNumber(self, ctx:mathlangParser.NumberContext):
        pass

    # Exit a parse tree produced by mathlangParser#Number.
    def exitNumber(self, ctx:mathlangParser.NumberContext):
        pass


    # Enter a parse tree produced by mathlangParser#Unary_Neg.
    def enterUnary_Neg(self, ctx:mathlangParser.Unary_NegContext):
        pass

    # Exit a parse tree produced by mathlangParser#Unary_Neg.
    def exitUnary_Neg(self, ctx:mathlangParser.Unary_NegContext):
        pass


    # Enter a parse tree produced by mathlangParser#AdditionOrSubtraction.
    def enterAdditionOrSubtraction(self, ctx:mathlangParser.AdditionOrSubtractionContext):
        pass

    # Exit a parse tree produced by mathlangParser#AdditionOrSubtraction.
    def exitAdditionOrSubtraction(self, ctx:mathlangParser.AdditionOrSubtractionContext):
        pass


    # Enter a parse tree produced by mathlangParser#MultiplicationOrDivision.
    def enterMultiplicationOrDivision(self, ctx:mathlangParser.MultiplicationOrDivisionContext):
        pass

    # Exit a parse tree produced by mathlangParser#MultiplicationOrDivision.
    def exitMultiplicationOrDivision(self, ctx:mathlangParser.MultiplicationOrDivisionContext):
        pass


    # Enter a parse tree produced by mathlangParser#Parentheses.
    def enterParentheses(self, ctx:mathlangParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by mathlangParser#Parentheses.
    def exitParentheses(self, ctx:mathlangParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by mathlangParser#Power.
    def enterPower(self, ctx:mathlangParser.PowerContext):
        pass

    # Exit a parse tree produced by mathlangParser#Power.
    def exitPower(self, ctx:mathlangParser.PowerContext):
        pass



del mathlangParser