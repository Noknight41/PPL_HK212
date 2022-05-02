# Generated from d:\My_Stuff\PPL\Lab\Lab1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5%\n\5\3\6\3\6\7\6")
        buf.write(")\n\6\f\6\16\6,\13\6\3\6\3\6\3\7\3\7\7\7\62\n\7\f\7\16")
        buf.write("\7\65\13\7\3\b\6\b8\n\b\r\b\16\b9\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\2\2\r\3\3\5\4\7\5\t\2\13\6\r\7")
        buf.write("\17\b\21\t\23\n\25\13\27\f\3\2\6\3\2))\3\2c|\4\2\62;c")
        buf.write("|\5\2\13\f\17\17\"\"\2G\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2")
        buf.write("\2\5\33\3\2\2\2\7\35\3\2\2\2\t$\3\2\2\2\13&\3\2\2\2\r")
        buf.write("/\3\2\2\2\17\67\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3")
        buf.write("\2\2\2\27C\3\2\2\2\31\32\7=\2\2\32\4\3\2\2\2\33\34\7<")
        buf.write("\2\2\34\6\3\2\2\2\35\36\7X\2\2\36\37\7c\2\2\37 \7t\2\2")
        buf.write(" \b\3\2\2\2!%\n\2\2\2\"#\7)\2\2#%\7)\2\2$!\3\2\2\2$\"")
        buf.write("\3\2\2\2%\n\3\2\2\2&*\7)\2\2\')\5\t\5\2(\'\3\2\2\2),\3")
        buf.write("\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2\2,*\3\2\2\2-.\7)\2")
        buf.write("\2.\f\3\2\2\2/\63\t\3\2\2\60\62\t\4\2\2\61\60\3\2\2\2")
        buf.write("\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\16\3\2\2")
        buf.write("\2\65\63\3\2\2\2\668\t\5\2\2\67\66\3\2\2\289\3\2\2\29")
        buf.write("\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\b\b\2\2<\20\3\2\2\2")
        buf.write("=>\13\2\2\2>\22\3\2\2\2?@\13\2\2\2@\24\3\2\2\2AB\13\2")
        buf.write("\2\2B\26\3\2\2\2CD\13\2\2\2D\30\3\2\2\2\b\2$*\61\639\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SEMI = 1
    COLON = 2
    VAR = 3
    STRING = 4
    ID = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9
    UNTERMINATED_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COLON", "VAR", "STRING", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "SEMI", "COLON", "VAR", "LEGALCHAR", "STRING", "ID", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


