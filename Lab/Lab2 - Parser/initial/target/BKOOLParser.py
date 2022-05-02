# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("w\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3*\n\3\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\5\5")
        buf.write("\64\n\5\3\6\3\6\3\6\3\6\3\7\3\7\5\7<\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\5\bC\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\fY\n")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16b\n\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17m\n\17\3\20\3")
        buf.write("\20\3\20\3\20\5\20s\n\20\3\21\3\21\3\21\2\2\22\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \2\2\2q\2\"\3\2\2\2\4")
        buf.write(")\3\2\2\2\6-\3\2\2\2\b\63\3\2\2\2\n\65\3\2\2\2\f;\3\2")
        buf.write("\2\2\16B\3\2\2\2\20D\3\2\2\2\22I\3\2\2\2\24O\3\2\2\2\26")
        buf.write("X\3\2\2\2\30Z\3\2\2\2\32]\3\2\2\2\34l\3\2\2\2\36r\3\2")
        buf.write("\2\2 t\3\2\2\2\"#\5\4\3\2#$\7\2\2\3$\3\3\2\2\2%&\5\6\4")
        buf.write("\2&\'\5\4\3\2\'*\3\2\2\2(*\5\6\4\2)%\3\2\2\2)(\3\2\2\2")
        buf.write("*\5\3\2\2\2+.\5\n\6\2,.\5\32\16\2-+\3\2\2\2-,\3\2\2\2")
        buf.write(".\7\3\2\2\2/\60\7\r\2\2\60\61\7\6\2\2\61\64\5\b\5\2\62")
        buf.write("\64\7\r\2\2\63/\3\2\2\2\63\62\3\2\2\2\64\t\3\2\2\2\65")
        buf.write("\66\7\5\2\2\66\67\5\b\5\2\678\7\7\2\28\13\3\2\2\29<\7")
        buf.write("\r\2\2:<\5 \21\2;9\3\2\2\2;:\3\2\2\2<\r\3\2\2\2=>\5\f")
        buf.write("\7\2>?\7\6\2\2?@\5\16\b\2@C\3\2\2\2AC\5\f\7\2B=\3\2\2")
        buf.write("\2BA\3\2\2\2C\17\3\2\2\2DE\7\r\2\2EF\7\b\2\2FG\5\f\7\2")
        buf.write("GH\7\7\2\2H\21\3\2\2\2IJ\7\r\2\2JK\7\t\2\2KL\5\16\b\2")
        buf.write("LM\7\n\2\2MN\7\7\2\2N\23\3\2\2\2OP\7\3\2\2PQ\5\f\7\2Q")
        buf.write("R\7\7\2\2R\25\3\2\2\2ST\5\30\r\2TU\7\7\2\2UV\5\26\f\2")
        buf.write("VY\3\2\2\2WY\5\30\r\2XS\3\2\2\2XW\3\2\2\2Y\27\3\2\2\2")
        buf.write("Z[\7\5\2\2[\\\5\b\5\2\\\31\3\2\2\2]^\7\5\2\2^_\7\r\2\2")
        buf.write("_a\7\t\2\2`b\5\26\f\2a`\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd")
        buf.write("\7\n\2\2de\7\13\2\2ef\5\34\17\2fg\7\f\2\2g\33\3\2\2\2")
        buf.write("hi\5\36\20\2ij\5\34\17\2jm\3\2\2\2km\5\36\20\2lh\3\2\2")
        buf.write("\2lk\3\2\2\2m\35\3\2\2\2ns\5\n\6\2os\5\20\t\2ps\5\22\n")
        buf.write("\2qs\5\24\13\2rn\3\2\2\2ro\3\2\2\2rp\3\2\2\2rq\3\2\2\2")
        buf.write("s\37\3\2\2\2tu\7\4\2\2u!\3\2\2\2\13)-\63;BXalr")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'expr'", "<INVALID>", "','", 
                     "';'", "'='", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DATATYPE", 
                      "COMMA", "SEMI", "ASS", "LB", "RB", "LP", "RP", "ID", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_idlist = 3
    RULE_vardecl = 4
    RULE_instance = 5
    RULE_instlist = 6
    RULE_varass = 7
    RULE_funccall = 8
    RULE_returnal = 9
    RULE_paramlist = 10
    RULE_param = 11
    RULE_funcdecl = 12
    RULE_body = 13
    RULE_stmt = 14
    RULE_expr = 15

    ruleNames =  [ "program", "decls", "decl", "idlist", "vardecl", "instance", 
                   "instlist", "varass", "funccall", "returnal", "paramlist", 
                   "param", "funcdecl", "body", "stmt", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DATATYPE=3
    COMMA=4
    SEMI=5
    ASS=6
    LB=7
    RB=8
    LP=9
    RP=10
    ID=11
    WS=12
    ERROR_CHAR=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.decls()
            self.state = 33
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.decl()
                self.state = 36
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idlist)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(BKOOLParser.ID)
                self.state = 46
                self.match(BKOOLParser.COMMA)
                self.state = 47
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATATYPE(self):
            return self.getToken(BKOOLParser.DATATYPE, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(BKOOLParser.DATATYPE)
            self.state = 52
            self.idlist()
            self.state = 53
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance" ):
                return visitor.visitInstance(self)
            else:
                return visitor.visitChildren(self)




    def instance(self):

        localctx = BKOOLParser.InstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instance)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.expr()
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


    class InstlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance(self):
            return self.getTypedRuleContext(BKOOLParser.InstanceContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def instlist(self):
            return self.getTypedRuleContext(BKOOLParser.InstlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstlist" ):
                return visitor.visitInstlist(self)
            else:
                return visitor.visitChildren(self)




    def instlist(self):

        localctx = BKOOLParser.InstlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instlist)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.instance()
                self.state = 60
                self.match(BKOOLParser.COMMA)
                self.state = 61
                self.instlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.instance()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASS(self):
            return self.getToken(BKOOLParser.ASS, 0)

        def instance(self):
            return self.getTypedRuleContext(BKOOLParser.InstanceContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_varass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarass" ):
                return visitor.visitVarass(self)
            else:
                return visitor.visitChildren(self)




    def varass(self):

        localctx = BKOOLParser.VarassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(BKOOLParser.ID)
            self.state = 67
            self.match(BKOOLParser.ASS)
            self.state = 68
            self.instance()
            self.state = 69
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def instlist(self):
            return self.getTypedRuleContext(BKOOLParser.InstlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = BKOOLParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(BKOOLParser.ID)
            self.state = 72
            self.match(BKOOLParser.LB)
            self.state = 73
            self.instlist()
            self.state = 74
            self.match(BKOOLParser.RB)
            self.state = 75
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance(self):
            return self.getTypedRuleContext(BKOOLParser.InstanceContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnal" ):
                return visitor.visitReturnal(self)
            else:
                return visitor.visitChildren(self)




    def returnal(self):

        localctx = BKOOLParser.ReturnalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(BKOOLParser.T__0)
            self.state = 78
            self.instance()
            self.state = 79
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramlist)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.param()
                self.state = 82
                self.match(BKOOLParser.SEMI)
                self.state = 83
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATATYPE(self):
            return self.getToken(BKOOLParser.DATATYPE, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(BKOOLParser.DATATYPE)
            self.state = 89
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATATYPE(self):
            return self.getToken(BKOOLParser.DATATYPE, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BKOOLParser.DATATYPE)
            self.state = 92
            self.match(BKOOLParser.ID)
            self.state = 93
            self.match(BKOOLParser.LB)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.DATATYPE:
                self.state = 94
                self.paramlist()


            self.state = 97
            self.match(BKOOLParser.RB)
            self.state = 98
            self.match(BKOOLParser.LP)
            self.state = 99
            self.body()
            self.state = 100
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_body)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.stmt()
                self.state = 103
                self.body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def varass(self):
            return self.getTypedRuleContext(BKOOLParser.VarassContext,0)


        def funccall(self):
            return self.getTypedRuleContext(BKOOLParser.FunccallContext,0)


        def returnal(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.varass()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.returnal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BKOOLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





