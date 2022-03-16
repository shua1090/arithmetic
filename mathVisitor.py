import antlr_generated.mathlangVisitor
from antlr_generated.mathlangParser import mathlangParser

class mathVisitor(antlr_generated.mathlangVisitor.mathlangVisitor):
    def visitStart(self, ctx: mathlangParser.StartContext):
        return super().visitStart(ctx)

    def visitNumber(self, ctx: mathlangParser.NumberContext):
        return int(ctx.NUMBER().getText())

    def visitParentheses(self, ctx: mathlangParser.ParenthesesContext):
        return self.visit(ctx.inner)

    def visitUnary_Neg(self, ctx: mathlangParser.Unary_NegContext):
        return - self.visit(ctx.inner)

    def visitPower(self, ctx: mathlangParser.PowerContext):
        return self.visit(ctx.left) ** self.visit(ctx.right)

    def visitMultiplicationOrDivision(self, ctx: mathlangParser.MultiplicationOrDivisionContext):
        if ctx.op.text == "*":
            return self.visit(ctx.left) * self.visit(ctx.right)
        else:
            return self.visit(ctx.left) // self.visit(ctx.right)

    def visitAdditionOrSubtraction(self, ctx: mathlangParser.AdditionOrSubtractionContext):
        if ctx.op.text == "+":
            return self.visit(ctx.left) + self.visit(ctx.right)
        else:
            return self.visit(ctx.left) - self.visit(ctx.right)