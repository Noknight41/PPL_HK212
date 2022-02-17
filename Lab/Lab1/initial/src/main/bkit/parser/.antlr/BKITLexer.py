# Generated from d:\My_Stuff\PPL\Lab\Lab1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\7\6\7/\n\7\r\7\16\7\60\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\2\2\f\3\2\5\3\7\4")
        buf.write("\t\5\13\6\r\7\17\b\21\t\23\n\25\13\3\2\4\3\2))\5\2\13")
        buf.write("\f\17\17\"\"\2=\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7%\3\2")
        buf.write("\2\2\t\'\3\2\2\2\13)\3\2\2\2\r.\3\2\2\2\17\64\3\2\2\2")
        buf.write("\21\66\3\2\2\2\238\3\2\2\2\25:\3\2\2\2\27\30\7)\2\2\30")
        buf.write("\4\3\2\2\2\31 \5\3\2\2\32\37\n\2\2\2\33\34\5\3\2\2\34")
        buf.write("\35\5\3\2\2\35\37\3\2\2\2\36\32\3\2\2\2\36\33\3\2\2\2")
        buf.write("\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\" \3\2\2")
        buf.write("\2#$\5\3\2\2$\6\3\2\2\2%&\7=\2\2&\b\3\2\2\2\'(\7<\2\2")
        buf.write("(\n\3\2\2\2)*\7X\2\2*+\7c\2\2+,\7t\2\2,\f\3\2\2\2-/\t")
        buf.write("\3\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2")
        buf.write("\61\62\3\2\2\2\62\63\b\7\2\2\63\16\3\2\2\2\64\65\13\2")
        buf.write("\2\2\65\20\3\2\2\2\66\67\13\2\2\2\67\22\3\2\2\289\13\2")
        buf.write("\2\29\24\3\2\2\2:;\13\2\2\2;\26\3\2\2\2\6\2\36 \60\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8
    UNTERMINATED_COMMENT = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "SINGQ", "STRING", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


