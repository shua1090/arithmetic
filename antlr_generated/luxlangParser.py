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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\34\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2")
        buf.write("\16\2\r\3\3\3\3\5\3\22\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\2\2\6\2\4\6\b\2\3\3\2\6\7\2\31\2\13\3\2\2\2\4")
        buf.write("\21\3\2\2\2\6\23\3\2\2\2\b\30\3\2\2\2\n\f\5\4\3\2\13\n")
        buf.write("\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3")
        buf.write("\2\2\2\17\22\5\6\4\2\20\22\5\b\5\2\21\17\3\2\2\2\21\20")
        buf.write("\3\2\2\2\22\5\3\2\2\2\23\24\7\3\2\2\24\25\7\6\2\2\25\26")
        buf.write("\7\4\2\2\26\27\7\7\2\2\27\7\3\2\2\2\30\31\7\5\2\2\31\32")
        buf.write("\t\2\2\2\32\t\3\2\2\2\4\r\21")
        return buf.getvalue()


class luxlangParser ( Parser ):

    grammarFileName = "luxlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "'show'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "INT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_let = 2
    RULE_show = 3

    ruleNames =  [ "program", "statement", "let", "show" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VAR=4
    INT=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(luxlangParser.StatementContext)
            else:
                return self.getTypedRuleContext(luxlangParser.StatementContext,i)


        def getRuleIndex(self):
            return luxlangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = luxlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==luxlangParser.T__0 or _la==luxlangParser.T__2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def let(self):
            return self.getTypedRuleContext(luxlangParser.LetContext,0)


        def show(self):
            return self.getTypedRuleContext(luxlangParser.ShowContext,0)


        def getRuleIndex(self):
            return luxlangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = luxlangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [luxlangParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.let()
                pass
            elif token in [luxlangParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.show()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(luxlangParser.VAR, 0)

        def INT(self):
            return self.getToken(luxlangParser.INT, 0)

        def getRuleIndex(self):
            return luxlangParser.RULE_let

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)




    def let(self):

        localctx = luxlangParser.LetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_let)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(luxlangParser.T__0)
            self.state = 18
            self.match(luxlangParser.VAR)
            self.state = 19
            self.match(luxlangParser.T__1)
            self.state = 20
            self.match(luxlangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(luxlangParser.INT, 0)

        def VAR(self):
            return self.getToken(luxlangParser.VAR, 0)

        def getRuleIndex(self):
            return luxlangParser.RULE_show

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow" ):
                listener.enterShow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow" ):
                listener.exitShow(self)




    def show(self):

        localctx = luxlangParser.ShowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_show)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(luxlangParser.T__2)
            self.state = 23
            _la = self._input.LA(1)
            if not(_la==luxlangParser.VAR or _la==luxlangParser.INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





