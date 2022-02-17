# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\7\2")
        buf.write("\34\n\2\f\2\16\2\37\13\2\3\3\3\3\3\3\3\3\6\3%\n\3\r\3")
        buf.write("\16\3&\7\3)\n\3\f\3\16\3,\13\3\3\3\5\3/\n\3\3\4\3\4\7")
        buf.write("\4\63\n\4\f\4\16\4\66\13\4\3\4\3\4\5\4:\n\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\b\6\bE\n\b\r\b\16\bF\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\2\2\r\3\2\5\2\7\3\t")
        buf.write("\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13\3\2\6\3\2\63;\3")
        buf.write("\2\62;\4\2\62;aa\5\2\13\f\17\17\"\"\2W\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2")
        buf.write("\2\2\5.\3\2\2\2\79\3\2\2\2\t;\3\2\2\2\13=\3\2\2\2\r?\3")
        buf.write("\2\2\2\17D\3\2\2\2\21J\3\2\2\2\23L\3\2\2\2\25N\3\2\2\2")
        buf.write("\27P\3\2\2\2\31\35\t\2\2\2\32\34\t\3\2\2\33\32\3\2\2\2")
        buf.write("\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\4\3\2\2")
        buf.write("\2\37\35\3\2\2\2 *\t\2\2\2!)\t\3\2\2\"$\7a\2\2#%\t\3\2")
        buf.write("\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2\2")
        buf.write("(!\3\2\2\2(\"\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+/")
        buf.write("\3\2\2\2,*\3\2\2\2-/\7\62\2\2. \3\2\2\2.-\3\2\2\2/\6\3")
        buf.write("\2\2\2\60\64\t\2\2\2\61\63\t\4\2\2\62\61\3\2\2\2\63\66")
        buf.write("\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66")
        buf.write("\64\3\2\2\2\67:\b\4\2\28:\7\62\2\29\60\3\2\2\298\3\2\2")
        buf.write("\2:\b\3\2\2\2;<\7=\2\2<\n\3\2\2\2=>\7<\2\2>\f\3\2\2\2")
        buf.write("?@\7X\2\2@A\7c\2\2AB\7t\2\2B\16\3\2\2\2CE\t\5\2\2DC\3")
        buf.write("\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GH\3\2\2\2HI\b\b\3")
        buf.write("\2I\20\3\2\2\2JK\13\2\2\2K\22\3\2\2\2LM\13\2\2\2M\24\3")
        buf.write("\2\2\2NO\13\2\2\2O\26\3\2\2\2PQ\13\2\2\2Q\30\3\2\2\2\f")
        buf.write("\2\35&(*.\62\649F\4\3\4\2\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID5 = 1
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
            "ID5", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DF1", "DF2", "ID5", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.ID5_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ID5_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    trim_result = self.text
                    self.text = trim_result.replace('_', '')
                
     


