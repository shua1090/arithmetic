# Generated from mathlang.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mathlangParser import mathlangParser
else:
    from mathlangParser import mathlangParser

# This class defines a complete generic visitor for a parse tree produced by mathlangParser.

class mathlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mathlangParser#start.
    def visitStart(self, ctx:mathlangParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathlangParser#Number.
    def visitNumber(self, ctx:mathlangParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathlangParser#Unary_Neg.
    def visitUnary_Neg(self, ctx:mathlangParser.Unary_NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathlangParser#AdditionOrSubtraction.
    def visitAdditionOrSubtraction(self, ctx:mathlangParser.AdditionOrSubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathlangParser#MultiplicationOrDivision.
    def visitMultiplicationOrDivision(self, ctx:mathlangParser.MultiplicationOrDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathlangParser#Parentheses.
    def visitParentheses(self, ctx:mathlangParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathlangParser#Power.
    def visitPower(self, ctx:mathlangParser.PowerContext):
        return self.visitChildren(ctx)



del mathlangParser