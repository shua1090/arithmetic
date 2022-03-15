# Generated from luxlang.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\37\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\17\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\32\n")
        buf.write("\3\f\3\16\3\35\13\3\3\3\2\3\4\4\2\4\2\4\3\2\6\7\3\2\b")
        buf.write("\t\2 \2\6\3\2\2\2\4\16\3\2\2\2\6\7\5\4\3\2\7\3\3\2\2\2")
        buf.write("\b\t\b\3\1\2\t\17\7\n\2\2\n\13\7\3\2\2\13\f\5\4\3\2\f")
        buf.write("\r\7\4\2\2\r\17\3\2\2\2\16\b\3\2\2\2\16\n\3\2\2\2\17\33")
        buf.write("\3\2\2\2\20\21\f\5\2\2\21\22\7\5\2\2\22\32\5\4\3\6\23")
        buf.write("\24\f\4\2\2\24\25\t\2\2\2\25\32\5\4\3\5\26\27\f\3\2\2")
        buf.write("\27\30\t\3\2\2\30\32\5\4\3\4\31\20\3\2\2\2\31\23\3\2\2")
        buf.write("\2\31\26\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2")
        buf.write("\2\2\34\5\3\2\2\2\35\33\3\2\2\2\5\16\31\33")
        return buf.getvalue()


class luxlangParser ( Parser ):

    grammarFileName = "luxlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'^'", "'*'", "'/'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "POW", "MUL", 
                      "DIV", "ADD", "SUB", "NUMBER", "WHITESPACE" ]

    RULE_start = 0
    RULE_expression = 1

    ruleNames =  [ "start", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    POW=3
    MUL=4
    DIV=5
    ADD=6
    SUB=7
    NUMBER=8
    WHITESPACE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(luxlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return luxlangParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = luxlangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return luxlangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a luxlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(luxlangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)


    class AdditionOrSubtractionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a luxlangParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.operator = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(luxlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(luxlangParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(luxlangParser.ADD, 0)
        def SUB(self):
            return self.getToken(luxlangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionOrSubtraction" ):
                listener.enterAdditionOrSubtraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionOrSubtraction" ):
                listener.exitAdditionOrSubtraction(self)


    class MultiplicationOrDivisionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a luxlangParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.operator = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(luxlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(luxlangParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(luxlangParser.MUL, 0)
        def DIV(self):
            return self.getToken(luxlangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationOrDivision" ):
                listener.enterMultiplicationOrDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationOrDivision" ):
                listener.exitMultiplicationOrDivision(self)


    class ParenthesesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a luxlangParser.ExpressionContext
            super().__init__(parser)
            self.inner = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(luxlangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)


    class PowerContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a luxlangParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.operator = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(luxlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(luxlangParser.ExpressionContext,i)

        def POW(self):
            return self.getToken(luxlangParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = luxlangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [luxlangParser.NUMBER]:
                localctx = luxlangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(luxlangParser.NUMBER)
                pass
            elif token in [luxlangParser.T__0]:
                localctx = luxlangParser.ParenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(luxlangParser.T__0)
                self.state = 9
                localctx.inner = self.expression(0)
                self.state = 10
                self.match(luxlangParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 23
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = luxlangParser.PowerContext(self, luxlangParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        localctx.operator = self.match(luxlangParser.POW)
                        self.state = 16
                        localctx.right = self.expression(4)
                        pass

                    elif la_ == 2:
                        localctx = luxlangParser.MultiplicationOrDivisionContext(self, luxlangParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 17
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 18
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==luxlangParser.MUL or _la==luxlangParser.DIV):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 19
                        localctx.right = self.expression(3)
                        pass

                    elif la_ == 3:
                        localctx = luxlangParser.AdditionOrSubtractionContext(self, luxlangParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 20
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 21
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==luxlangParser.ADD or _la==luxlangParser.SUB):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        localctx.right = self.expression(2)
                        pass

             
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




