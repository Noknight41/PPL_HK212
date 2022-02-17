# Generated from d:\My_Stuff\PPL\Lab\Lab2\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\62\n\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6")
        buf.write("\fC\n\f\r\f\16\fD\3\r\3\r\3\r\3\r\3\16\3\16\3\16\2\2\17")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\3\2\4\4\2C\\c|\5\2\13\f\17\17\"\"\2N\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35")
        buf.write("\3\2\2\2\5$\3\2\2\2\7\61\3\2\2\2\t\63\3\2\2\2\13\65\3")
        buf.write("\2\2\2\r\67\3\2\2\2\179\3\2\2\2\21;\3\2\2\2\23=\3\2\2")
        buf.write("\2\25?\3\2\2\2\27B\3\2\2\2\31F\3\2\2\2\33J\3\2\2\2\35")
        buf.write("\36\7t\2\2\36\37\7g\2\2\37 \7v\2\2 !\7w\2\2!\"\7t\2\2")
        buf.write("\"#\7p\2\2#\4\3\2\2\2$%\7g\2\2%&\7z\2\2&\'\7r\2\2\'(\7")
        buf.write("t\2\2(\6\3\2\2\2)*\7k\2\2*+\7p\2\2+\62\7v\2\2,-\7h\2\2")
        buf.write("-.\7n\2\2./\7q\2\2/\60\7c\2\2\60\62\7v\2\2\61)\3\2\2\2")
        buf.write("\61,\3\2\2\2\62\b\3\2\2\2\63\64\7.\2\2\64\n\3\2\2\2\65")
        buf.write("\66\7=\2\2\66\f\3\2\2\2\678\7?\2\28\16\3\2\2\29:\7*\2")
        buf.write("\2:\20\3\2\2\2;<\7+\2\2<\22\3\2\2\2=>\7}\2\2>\24\3\2\2")
        buf.write("\2?@\7\177\2\2@\26\3\2\2\2AC\t\2\2\2BA\3\2\2\2CD\3\2\2")
        buf.write("\2DB\3\2\2\2DE\3\2\2\2E\30\3\2\2\2FG\t\3\2\2GH\3\2\2\2")
        buf.write("HI\b\r\2\2I\32\3\2\2\2JK\13\2\2\2KL\b\16\3\2L\34\3\2\2")
        buf.write("\2\5\2\61D\4\b\2\2\3\16\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    DATATYPE = 3
    COMMA = 4
    SEMI = 5
    ASS = 6
    LB = 7
    RB = 8
    LP = 9
    RP = 10
    ID = 11
    WS = 12
    ERROR_CHAR = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'expr'", "','", "';'", "'='", "'('", "')'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "DATATYPE", "COMMA", "SEMI", "ASS", "LB", "RB", "LP", "RP", 
            "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "DATATYPE", "COMMA", "SEMI", "ASS", "LB", 
                  "RB", "LP", "RP", "ID", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


