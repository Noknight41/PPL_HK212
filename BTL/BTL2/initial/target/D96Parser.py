# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u023e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\6\2l\n\2\r\2\16\2m\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3z\n\3\3\4\3\4\6\4~\n\4\r\4\16")
        buf.write("\4\177\3\4\3\4\3\4\3\4\5\4\u0086\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u0091\n\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a1\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\5\b\u00aa\n\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u00b3\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u00bf\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00cb\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\5\r\u00d7\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\5\17\u00e1\n\17\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00e7\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00ee")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00f6\n\22\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00fc\n\23\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u0102\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u0109\n")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u011b\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\5\30\u0124\n\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u012d\n\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u0137\n\32\3\32\3\32")
        buf.write("\3\32\7\32\u013c\n\32\f\32\16\32\u013f\13\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u014c")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0156")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0160")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0169\n")
        buf.write("\37\3 \3 \3 \3 \3 \5 \u0170\n \3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\5!\u017b\n!\3!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0184\n")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\5$\u019b\n$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\5&\u01a7\n&\3\'\3\'\5\'\u01ab\n\'\3(\3(\3(\3(\3(\5(")
        buf.write("\u01b2\n(\3)\3)\3)\3)\3)\5)\u01b9\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\7*\u01c4\n*\f*\16*\u01c7\13*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\7+\u01d2\n+\f+\16+\u01d5\13+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\7,\u01e3\n,\f,\16,\u01e6\13")
        buf.write(",\3-\3-\3-\5-\u01eb\n-\3.\3.\3.\5.\u01f0\n.\3/\3/\3/\3")
        buf.write("/\5/\u01f6\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\5\60\u0201\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\5\61\u020a\n\61\7\61\u020c\n\61\f\61\16\61\u020f\13")
        buf.write("\61\3\62\3\62\3\62\3\62\5\62\u0215\n\62\3\62\5\62\u0218")
        buf.write("\n\62\3\63\3\63\3\63\3\63\5\63\u021e\n\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\5\63\u0228\n\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0232\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u023c\n\65\3\65")
        buf.write("\2\7\62RTV`\66\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh\2\4\3")
        buf.write("\2=>\4\2\26\27\32\33\2\u0254\2k\3\2\2\2\4y\3\2\2\2\6\u0085")
        buf.write("\3\2\2\2\b\u0090\3\2\2\2\n\u0092\3\2\2\2\f\u00a0\3\2\2")
        buf.write("\2\16\u00a9\3\2\2\2\20\u00b2\3\2\2\2\22\u00be\3\2\2\2")
        buf.write("\24\u00ca\3\2\2\2\26\u00cc\3\2\2\2\30\u00d6\3\2\2\2\32")
        buf.write("\u00d8\3\2\2\2\34\u00e0\3\2\2\2\36\u00e6\3\2\2\2 \u00ed")
        buf.write("\3\2\2\2\"\u00f5\3\2\2\2$\u00fb\3\2\2\2&\u0101\3\2\2\2")
        buf.write("(\u0108\3\2\2\2*\u010c\3\2\2\2,\u011a\3\2\2\2.\u0123\3")
        buf.write("\2\2\2\60\u012c\3\2\2\2\62\u0136\3\2\2\2\64\u0140\3\2")
        buf.write("\2\2\66\u014b\3\2\2\28\u0155\3\2\2\2:\u015f\3\2\2\2<\u0168")
        buf.write("\3\2\2\2>\u016f\3\2\2\2@\u0171\3\2\2\2B\u0183\3\2\2\2")
        buf.write("D\u0185\3\2\2\2F\u019a\3\2\2\2H\u019c\3\2\2\2J\u01a6\3")
        buf.write("\2\2\2L\u01aa\3\2\2\2N\u01b1\3\2\2\2P\u01b8\3\2\2\2R\u01ba")
        buf.write("\3\2\2\2T\u01c8\3\2\2\2V\u01d6\3\2\2\2X\u01ea\3\2\2\2")
        buf.write("Z\u01ef\3\2\2\2\\\u01f5\3\2\2\2^\u0200\3\2\2\2`\u0202")
        buf.write("\3\2\2\2b\u0217\3\2\2\2d\u0227\3\2\2\2f\u0231\3\2\2\2")
        buf.write("h\u023b\3\2\2\2jl\5\4\3\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2")
        buf.write("\2mn\3\2\2\2no\3\2\2\2op\7\2\2\3p\3\3\2\2\2qr\7\16\2\2")
        buf.write("rs\7>\2\2st\7\62\2\2tu\7>\2\2uz\5\6\4\2vw\7\16\2\2wx\7")
        buf.write(">\2\2xz\5\6\4\2yq\3\2\2\2yv\3\2\2\2z\5\3\2\2\2{}\79\2")
        buf.write("\2|~\5\b\5\2}|\3\2\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7:\2\2\u0082")
        buf.write("\u0086\3\2\2\2\u0083\u0084\79\2\2\u0084\u0086\7:\2\2\u0085")
        buf.write("{\3\2\2\2\u0085\u0083\3\2\2\2\u0086\7\3\2\2\2\u0087\u0091")
        buf.write("\5\24\13\2\u0088\u0091\5\26\f\2\u0089\u0091\5\22\n\2\u008a")
        buf.write("\u008b\5\16\b\2\u008b\u008c\7\64\2\2\u008c\u0091\3\2\2")
        buf.write("\2\u008d\u008e\5\20\t\2\u008e\u008f\7\64\2\2\u008f\u0091")
        buf.write("\3\2\2\2\u0090\u0087\3\2\2\2\u0090\u0088\3\2\2\2\u0090")
        buf.write("\u0089\3\2\2\2\u0090\u008a\3\2\2\2\u0090\u008d\3\2\2\2")
        buf.write("\u0091\t\3\2\2\2\u0092\u0093\t\2\2\2\u0093\u0094\5\f\7")
        buf.write("\2\u0094\u0095\5N(\2\u0095\13\3\2\2\2\u0096\u0097\7\63")
        buf.write("\2\2\u0097\u0098\t\2\2\2\u0098\u0099\5\f\7\2\u0099\u009a")
        buf.write("\5N(\2\u009a\u009b\7\63\2\2\u009b\u00a1\3\2\2\2\u009c")
        buf.write("\u009d\7\62\2\2\u009d\u009e\5L\'\2\u009e\u009f\7+\2\2")
        buf.write("\u009f\u00a1\3\2\2\2\u00a0\u0096\3\2\2\2\u00a0\u009c\3")
        buf.write("\2\2\2\u00a1\r\3\2\2\2\u00a2\u00a3\7\35\2\2\u00a3\u00a4")
        buf.write("\5\36\20\2\u00a4\u00a5\7\62\2\2\u00a5\u00a6\5L\'\2\u00a6")
        buf.write("\u00aa\3\2\2\2\u00a7\u00a8\7\35\2\2\u00a8\u00aa\5\n\6")
        buf.write("\2\u00a9\u00a2\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\17\3")
        buf.write("\2\2\2\u00ab\u00ac\7\36\2\2\u00ac\u00ad\5\36\20\2\u00ad")
        buf.write("\u00ae\7\62\2\2\u00ae\u00af\5L\'\2\u00af\u00b3\3\2\2\2")
        buf.write("\u00b0\u00b1\7\36\2\2\u00b1\u00b3\5\n\6\2\u00b2\u00ab")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\21\3\2\2\2\u00b4\u00b5")
        buf.write("\t\2\2\2\u00b5\u00b6\7\67\2\2\u00b6\u00b7\5\30\r\2\u00b7")
        buf.write("\u00b8\78\2\2\u00b8\u00b9\5\"\22\2\u00b9\u00bf\3\2\2\2")
        buf.write("\u00ba\u00bb\t\2\2\2\u00bb\u00bc\7\67\2\2\u00bc\u00bd")
        buf.write("\78\2\2\u00bd\u00bf\5\"\22\2\u00be\u00b4\3\2\2\2\u00be")
        buf.write("\u00ba\3\2\2\2\u00bf\23\3\2\2\2\u00c0\u00c1\7\37\2\2\u00c1")
        buf.write("\u00c2\7\67\2\2\u00c2\u00c3\5\30\r\2\u00c3\u00c4\78\2")
        buf.write("\2\u00c4\u00c5\5\"\22\2\u00c5\u00cb\3\2\2\2\u00c6\u00c7")
        buf.write("\7\37\2\2\u00c7\u00c8\7\67\2\2\u00c8\u00c9\78\2\2\u00c9")
        buf.write("\u00cb\5\"\22\2\u00ca\u00c0\3\2\2\2\u00ca\u00c6\3\2\2")
        buf.write("\2\u00cb\25\3\2\2\2\u00cc\u00cd\7 \2\2\u00cd\u00ce\7\67")
        buf.write("\2\2\u00ce\u00cf\78\2\2\u00cf\u00d0\5\"\22\2\u00d0\27")
        buf.write("\3\2\2\2\u00d1\u00d2\5\32\16\2\u00d2\u00d3\7\64\2\2\u00d3")
        buf.write("\u00d4\5\30\r\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5\32\16")
        buf.write("\2\u00d6\u00d1\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\31\3")
        buf.write("\2\2\2\u00d8\u00d9\5\34\17\2\u00d9\u00da\7\62\2\2\u00da")
        buf.write("\u00db\5L\'\2\u00db\33\3\2\2\2\u00dc\u00dd\7>\2\2\u00dd")
        buf.write("\u00de\7\63\2\2\u00de\u00e1\5\34\17\2\u00df\u00e1\7>\2")
        buf.write("\2\u00e0\u00dc\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\35\3")
        buf.write("\2\2\2\u00e2\u00e3\t\2\2\2\u00e3\u00e4\7\63\2\2\u00e4")
        buf.write("\u00e7\5\36\20\2\u00e5\u00e7\t\2\2\2\u00e6\u00e2\3\2\2")
        buf.write("\2\u00e6\u00e5\3\2\2\2\u00e7\37\3\2\2\2\u00e8\u00e9\5")
        buf.write("N(\2\u00e9\u00ea\7\63\2\2\u00ea\u00eb\5 \21\2\u00eb\u00ee")
        buf.write("\3\2\2\2\u00ec\u00ee\5N(\2\u00ed\u00e8\3\2\2\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee!\3\2\2\2\u00ef\u00f0\79\2\2\u00f0\u00f1")
        buf.write("\5$\23\2\u00f1\u00f2\7:\2\2\u00f2\u00f6\3\2\2\2\u00f3")
        buf.write("\u00f4\79\2\2\u00f4\u00f6\7:\2\2\u00f5\u00ef\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6#\3\2\2\2\u00f7\u00f8\5&\24\2\u00f8")
        buf.write("\u00f9\5$\23\2\u00f9\u00fc\3\2\2\2\u00fa\u00fc\5&\24\2")
        buf.write("\u00fb\u00f7\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc%\3\2\2")
        buf.write("\2\u00fd\u0102\5(\25\2\u00fe\u0102\5\"\22\2\u00ff\u0102")
        buf.write("\5@!\2\u0100\u0102\5B\"\2\u0101\u00fd\3\2\2\2\u0101\u00fe")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("\'\3\2\2\2\u0103\u0109\5.\30\2\u0104\u0109\5\60\31\2\u0105")
        buf.write("\u0109\5\66\34\2\u0106\u0109\5<\37\2\u0107\u0109\5> \2")
        buf.write("\u0108\u0103\3\2\2\2\u0108\u0104\3\2\2\2\u0108\u0105\3")
        buf.write("\2\2\2\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u010b\7\64\2\2\u010b)\3\2\2\2\u010c\u010d")
        buf.write("\7>\2\2\u010d\u010e\5,\27\2\u010e\u010f\5N(\2\u010f+\3")
        buf.write("\2\2\2\u0110\u0111\7\63\2\2\u0111\u0112\7>\2\2\u0112\u0113")
        buf.write("\5,\27\2\u0113\u0114\5N(\2\u0114\u0115\7\63\2\2\u0115")
        buf.write("\u011b\3\2\2\2\u0116\u0117\7\62\2\2\u0117\u0118\5L\'\2")
        buf.write("\u0118\u0119\7+\2\2\u0119\u011b\3\2\2\2\u011a\u0110\3")
        buf.write("\2\2\2\u011a\u0116\3\2\2\2\u011b-\3\2\2\2\u011c\u011d")
        buf.write("\7\35\2\2\u011d\u011e\5\34\17\2\u011e\u011f\7\62\2\2\u011f")
        buf.write("\u0120\5L\'\2\u0120\u0124\3\2\2\2\u0121\u0122\7\35\2\2")
        buf.write("\u0122\u0124\5*\26\2\u0123\u011c\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0124/\3\2\2\2\u0125\u0126\7\36\2\2\u0126\u0127")
        buf.write("\5\34\17\2\u0127\u0128\7\62\2\2\u0128\u0129\5L\'\2\u0129")
        buf.write("\u012d\3\2\2\2\u012a\u012b\7\36\2\2\u012b\u012d\5*\26")
        buf.write("\2\u012c\u0125\3\2\2\2\u012c\u012a\3\2\2\2\u012d\61\3")
        buf.write("\2\2\2\u012e\u012f\b\32\1\2\u012f\u0130\7%\2\2\u0130\u0131")
        buf.write("\7\66\2\2\u0131\u0137\7>\2\2\u0132\u0133\7>\2\2\u0133")
        buf.write("\u0134\7\61\2\2\u0134\u0137\7=\2\2\u0135\u0137\7>\2\2")
        buf.write("\u0136\u012e\3\2\2\2\u0136\u0132\3\2\2\2\u0136\u0135\3")
        buf.write("\2\2\2\u0137\u013d\3\2\2\2\u0138\u0139\f\6\2\2\u0139\u013a")
        buf.write("\7\66\2\2\u013a\u013c\7>\2\2\u013b\u0138\3\2\2\2\u013c")
        buf.write("\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2")
        buf.write("\u013e\63\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\5\62")
        buf.write("\32\2\u0141\u0142\5^\60\2\u0142\65\3\2\2\2\u0143\u0144")
        buf.write("\5\62\32\2\u0144\u0145\7+\2\2\u0145\u0146\5N(\2\u0146")
        buf.write("\u014c\3\2\2\2\u0147\u0148\5\64\33\2\u0148\u0149\7+\2")
        buf.write("\2\u0149\u014a\5N(\2\u014a\u014c\3\2\2\2\u014b\u0143\3")
        buf.write("\2\2\2\u014b\u0147\3\2\2\2\u014c\67\3\2\2\2\u014d\u014e")
        buf.write("\7>\2\2\u014e\u014f\7\67\2\2\u014f\u0150\5 \21\2\u0150")
        buf.write("\u0151\78\2\2\u0151\u0156\3\2\2\2\u0152\u0153\7>\2\2\u0153")
        buf.write("\u0154\7\67\2\2\u0154\u0156\78\2\2\u0155\u014d\3\2\2\2")
        buf.write("\u0155\u0152\3\2\2\2\u01569\3\2\2\2\u0157\u0158\7=\2\2")
        buf.write("\u0158\u0159\7\67\2\2\u0159\u015a\5 \21\2\u015a\u015b")
        buf.write("\78\2\2\u015b\u0160\3\2\2\2\u015c\u015d\7=\2\2\u015d\u015e")
        buf.write("\7\67\2\2\u015e\u0160\78\2\2\u015f\u0157\3\2\2\2\u015f")
        buf.write("\u015c\3\2\2\2\u0160;\3\2\2\2\u0161\u0162\5N(\2\u0162")
        buf.write("\u0163\7\66\2\2\u0163\u0164\58\35\2\u0164\u0169\3\2\2")
        buf.write("\2\u0165\u0166\7>\2\2\u0166\u0167\7\61\2\2\u0167\u0169")
        buf.write("\5:\36\2\u0168\u0161\3\2\2\2\u0168\u0165\3\2\2\2\u0169")
        buf.write("=\3\2\2\2\u016a\u016b\7!\2\2\u016b\u0170\5N(\2\u016c\u0170")
        buf.write("\7!\2\2\u016d\u0170\7\17\2\2\u016e\u0170\7\20\2\2\u016f")
        buf.write("\u016a\3\2\2\2\u016f\u016c\3\2\2\2\u016f\u016d\3\2\2\2")
        buf.write("\u016f\u016e\3\2\2\2\u0170?\3\2\2\2\u0171\u0172\7\24\2")
        buf.write("\2\u0172\u0173\7\67\2\2\u0173\u0174\7>\2\2\u0174\u0175")
        buf.write("\7#\2\2\u0175\u0176\5N(\2\u0176\u0177\7\65\2\2\u0177\u017a")
        buf.write("\5N(\2\u0178\u0179\7$\2\2\u0179\u017b\5N(\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017d\78\2\2\u017d\u017e\5\"\22\2\u017eA\3\2\2\2\u017f")
        buf.write("\u0180\5D#\2\u0180\u0181\5F$\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0184\5D#\2\u0183\u017f\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("C\3\2\2\2\u0185\u0186\7\21\2\2\u0186\u0187\7\67\2\2\u0187")
        buf.write("\u0188\5N(\2\u0188\u0189\78\2\2\u0189\u018a\5\"\22\2\u018a")
        buf.write("E\3\2\2\2\u018b\u018c\7\22\2\2\u018c\u018d\7\67\2\2\u018d")
        buf.write("\u018e\5N(\2\u018e\u018f\78\2\2\u018f\u0190\5\"\22\2\u0190")
        buf.write("\u0191\5F$\2\u0191\u019b\3\2\2\2\u0192\u0193\7\22\2\2")
        buf.write("\u0193\u0194\7\67\2\2\u0194\u0195\5N(\2\u0195\u0196\7")
        buf.write("8\2\2\u0196\u0197\5\"\22\2\u0197\u019b\3\2\2\2\u0198\u0199")
        buf.write("\7\23\2\2\u0199\u019b\5\"\22\2\u019a\u018b\3\2\2\2\u019a")
        buf.write("\u0192\3\2\2\2\u019a\u0198\3\2\2\2\u019bG\3\2\2\2\u019c")
        buf.write("\u019d\t\3\2\2\u019dI\3\2\2\2\u019e\u019f\7\25\2\2\u019f")
        buf.write("\u01a0\7;\2\2\u01a0\u01a1\5J&\2\u01a1\u01a2\7\63\2\2\u01a2")
        buf.write("\u01a3\7\3\2\2\u01a3\u01a4\7<\2\2\u01a4\u01a7\3\2\2\2")
        buf.write("\u01a5\u01a7\5H%\2\u01a6\u019e\3\2\2\2\u01a6\u01a5\3\2")
        buf.write("\2\2\u01a7K\3\2\2\2\u01a8\u01ab\5J&\2\u01a9\u01ab\7>\2")
        buf.write("\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abM\3\2")
        buf.write("\2\2\u01ac\u01ad\5P)\2\u01ad\u01ae\7&\2\2\u01ae\u01af")
        buf.write("\5P)\2\u01af\u01b2\3\2\2\2\u01b0\u01b2\5P)\2\u01b1\u01ac")
        buf.write("\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2O\3\2\2\2\u01b3\u01b4")
        buf.write("\5R*\2\u01b4\u01b5\7\'\2\2\u01b5\u01b6\5R*\2\u01b6\u01b9")
        buf.write("\3\2\2\2\u01b7\u01b9\5R*\2\u01b8\u01b3\3\2\2\2\u01b8\u01b7")
        buf.write("\3\2\2\2\u01b9Q\3\2\2\2\u01ba\u01bb\b*\1\2\u01bb\u01bc")
        buf.write("\5T+\2\u01bc\u01c5\3\2\2\2\u01bd\u01be\f\5\2\2\u01be\u01bf")
        buf.write("\7*\2\2\u01bf\u01c4\5T+\2\u01c0\u01c1\f\4\2\2\u01c1\u01c2")
        buf.write("\7)\2\2\u01c2\u01c4\5T+\2\u01c3\u01bd\3\2\2\2\u01c3\u01c0")
        buf.write("\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6S\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8")
        buf.write("\u01c9\b+\1\2\u01c9\u01ca\5V,\2\u01ca\u01d3\3\2\2\2\u01cb")
        buf.write("\u01cc\f\5\2\2\u01cc\u01cd\7,\2\2\u01cd\u01d2\5V,\2\u01ce")
        buf.write("\u01cf\f\4\2\2\u01cf\u01d0\7-\2\2\u01d0\u01d2\5V,\2\u01d1")
        buf.write("\u01cb\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d2\u01d5\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4U\3\2\2")
        buf.write("\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\b,\1\2\u01d7\u01d8")
        buf.write("\5X-\2\u01d8\u01e4\3\2\2\2\u01d9\u01da\f\6\2\2\u01da\u01db")
        buf.write("\7.\2\2\u01db\u01e3\5X-\2\u01dc\u01dd\f\5\2\2\u01dd\u01de")
        buf.write("\7/\2\2\u01de\u01e3\5X-\2\u01df\u01e0\f\4\2\2\u01e0\u01e1")
        buf.write("\7\60\2\2\u01e1\u01e3\5X-\2\u01e2\u01d9\3\2\2\2\u01e2")
        buf.write("\u01dc\3\2\2\2\u01e2\u01df\3\2\2\2\u01e3\u01e6\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5W\3\2\2")
        buf.write("\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7(\2\2\u01e8\u01eb")
        buf.write("\5X-\2\u01e9\u01eb\5Z.\2\u01ea\u01e7\3\2\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01ebY\3\2\2\2\u01ec\u01ed\7-\2\2\u01ed\u01f0")
        buf.write("\5Z.\2\u01ee\u01f0\5\\/\2\u01ef\u01ec\3\2\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0[\3\2\2\2\u01f1\u01f2\5`\61\2\u01f2\u01f3")
        buf.write("\5^\60\2\u01f3\u01f6\3\2\2\2\u01f4\u01f6\5`\61\2\u01f5")
        buf.write("\u01f1\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6]\3\2\2\2\u01f7")
        buf.write("\u01f8\7;\2\2\u01f8\u01f9\5N(\2\u01f9\u01fa\7<\2\2\u01fa")
        buf.write("\u0201\3\2\2\2\u01fb\u01fc\7;\2\2\u01fc\u01fd\5N(\2\u01fd")
        buf.write("\u01fe\7<\2\2\u01fe\u01ff\5^\60\2\u01ff\u0201\3\2\2\2")
        buf.write("\u0200\u01f7\3\2\2\2\u0200\u01fb\3\2\2\2\u0201_\3\2\2")
        buf.write("\2\u0202\u0203\b\61\1\2\u0203\u0204\5b\62\2\u0204\u020d")
        buf.write("\3\2\2\2\u0205\u0206\f\4\2\2\u0206\u0209\7\66\2\2\u0207")
        buf.write("\u020a\7>\2\2\u0208\u020a\58\35\2\u0209\u0207\3\2\2\2")
        buf.write("\u0209\u0208\3\2\2\2\u020a\u020c\3\2\2\2\u020b\u0205\3")
        buf.write("\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e")
        buf.write("\3\2\2\2\u020ea\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0211")
        buf.write("\7>\2\2\u0211\u0214\7\61\2\2\u0212\u0215\7=\2\2\u0213")
        buf.write("\u0215\5:\36\2\u0214\u0212\3\2\2\2\u0214\u0213\3\2\2\2")
        buf.write("\u0215\u0218\3\2\2\2\u0216\u0218\5d\63\2\u0217\u0210\3")
        buf.write("\2\2\2\u0217\u0216\3\2\2\2\u0218c\3\2\2\2\u0219\u021a")
        buf.write("\7\"\2\2\u021a\u021b\7>\2\2\u021b\u021d\7\67\2\2\u021c")
        buf.write("\u021e\5 \21\2\u021d\u021c\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u021f\3\2\2\2\u021f\u0228\78\2\2\u0220\u0228\7")
        buf.write(">\2\2\u0221\u0222\7\67\2\2\u0222\u0223\5N(\2\u0223\u0224")
        buf.write("\78\2\2\u0224\u0228\3\2\2\2\u0225\u0228\5f\64\2\u0226")
        buf.write("\u0228\7%\2\2\u0227\u0219\3\2\2\2\u0227\u0220\3\2\2\2")
        buf.write("\u0227\u0221\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0226\3")
        buf.write("\2\2\2\u0228e\3\2\2\2\u0229\u0232\7\30\2\2\u022a\u0232")
        buf.write("\7\31\2\2\u022b\u0232\7\t\2\2\u022c\u0232\7\3\2\2\u022d")
        buf.write("\u0232\7\n\2\2\u022e\u0232\7\b\2\2\u022f\u0232\7\34\2")
        buf.write("\2\u0230\u0232\5h\65\2\u0231\u0229\3\2\2\2\u0231\u022a")
        buf.write("\3\2\2\2\u0231\u022b\3\2\2\2\u0231\u022c\3\2\2\2\u0231")
        buf.write("\u022d\3\2\2\2\u0231\u022e\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0230\3\2\2\2\u0232g\3\2\2\2\u0233\u0234\7\25\2")
        buf.write("\2\u0234\u0235\7\67\2\2\u0235\u0236\5 \21\2\u0236\u0237")
        buf.write("\78\2\2\u0237\u023c\3\2\2\2\u0238\u0239\7\25\2\2\u0239")
        buf.write("\u023a\7\67\2\2\u023a\u023c\78\2\2\u023b\u0233\3\2\2\2")
        buf.write("\u023b\u0238\3\2\2\2\u023ci\3\2\2\2\67my\177\u0085\u0090")
        buf.write("\u00a0\u00a9\u00b2\u00be\u00ca\u00d6\u00e0\u00e6\u00ed")
        buf.write("\u00f5\u00fb\u0101\u0108\u011a\u0123\u012c\u0136\u013d")
        buf.write("\u014b\u0155\u015f\u0168\u016f\u017a\u0183\u019a\u01a6")
        buf.write("\u01aa\u01b1\u01b8\u01c3\u01c5\u01d1\u01d3\u01e2\u01e4")
        buf.write("\u01ea\u01ef\u01f5\u0200\u0209\u020d\u0214\u0217\u021d")
        buf.write("\u0227\u0231\u023b")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Class'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'Array'", "'Int'", "'Float'", 
                     "'True'", "'False'", "'Boolean'", "'String'", "'Null'", 
                     "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'Return'", "'New'", "'In'", "'By'", "'Self'", "<INVALID>", 
                     "<INVALID>", "'!'", "'&&'", "'||'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'::'", "':'", "','", "';'", "'..'", 
                     "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "BIN", "OCT", "DEC", "HEX", 
                      "ZERO", "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "BCOMMENT", "CLASS", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", "INT", 
                      "FLOAT", "TRUE", "FALSE", "BOOLEAN", "STRING", "NULL", 
                      "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "RETURN", 
                      "NEW", "IN", "BY", "SELF", "STR", "RELOP", "NOTOP", 
                      "ANDOP", "OROP", "ASSOP", "ADDOP", "MINOP", "MULOP", 
                      "DIVOP", "REMOP", "DCOLON", "COLON", "COMMA", "SEMI", 
                      "DDOT", "DOT", "LB", "RB", "LP", "RP", "LC", "RC", 
                      "DOLLARID", "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_bclass = 1
    RULE_class_body = 2
    RULE_class_stmt = 3
    RULE_id_vas = 4
    RULE_id_va = 5
    RULE_valdecl = 6
    RULE_vardecl = 7
    RULE_funcdecl = 8
    RULE_constructor = 9
    RULE_destructor = 10
    RULE_paramlist = 11
    RULE_param = 12
    RULE_bidlist = 13
    RULE_idlist = 14
    RULE_valuelist = 15
    RULE_blockstmt = 16
    RULE_stmtlist = 17
    RULE_stmt = 18
    RULE_semi_stmt = 19
    RULE_bid_vas = 20
    RULE_bid_va = 21
    RULE_bvaldecl = 22
    RULE_bvardecl = 23
    RULE_lhs = 24
    RULE_index_lhs = 25
    RULE_varass = 26
    RULE_func = 27
    RULE_dollarfunc = 28
    RULE_funccall = 29
    RULE_rcb = 30
    RULE_foreachstmt = 31
    RULE_ifstmt = 32
    RULE_ifpart = 33
    RULE_elseif_part = 34
    RULE_datatype = 35
    RULE_dttype = 36
    RULE_dttyp = 37
    RULE_expr = 38
    RULE_term1 = 39
    RULE_term2 = 40
    RULE_term3 = 41
    RULE_term4 = 42
    RULE_term5 = 43
    RULE_term6 = 44
    RULE_term7 = 45
    RULE_index_operators = 46
    RULE_term8 = 47
    RULE_term9 = 48
    RULE_term10 = 49
    RULE_literal = 50
    RULE_arrayCell = 51

    ruleNames =  [ "program", "bclass", "class_body", "class_stmt", "id_vas", 
                   "id_va", "valdecl", "vardecl", "funcdecl", "constructor", 
                   "destructor", "paramlist", "param", "bidlist", "idlist", 
                   "valuelist", "blockstmt", "stmtlist", "stmt", "semi_stmt", 
                   "bid_vas", "bid_va", "bvaldecl", "bvardecl", "lhs", "index_lhs", 
                   "varass", "func", "dollarfunc", "funccall", "rcb", "foreachstmt", 
                   "ifstmt", "ifpart", "elseif_part", "datatype", "dttype", 
                   "dttyp", "expr", "term1", "term2", "term3", "term4", 
                   "term5", "term6", "term7", "index_operators", "term8", 
                   "term9", "term10", "literal", "arrayCell" ]

    EOF = Token.EOF
    INTLIT=1
    BIN=2
    OCT=3
    DEC=4
    HEX=5
    ZERO=6
    FLOATLIT=7
    STRINGLIT=8
    UNCLOSE_STRING=9
    ILLEGAL_ESCAPE=10
    BCOMMENT=11
    CLASS=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSEIF=16
    ELSE=17
    FOREACH=18
    ARRAY=19
    INT=20
    FLOAT=21
    TRUE=22
    FALSE=23
    BOOLEAN=24
    STRING=25
    NULL=26
    VAL=27
    VAR=28
    CONSTRUCTOR=29
    DESTRUCTOR=30
    RETURN=31
    NEW=32
    IN=33
    BY=34
    SELF=35
    STR=36
    RELOP=37
    NOTOP=38
    ANDOP=39
    OROP=40
    ASSOP=41
    ADDOP=42
    MINOP=43
    MULOP=44
    DIVOP=45
    REMOP=46
    DCOLON=47
    COLON=48
    COMMA=49
    SEMI=50
    DDOT=51
    DOT=52
    LB=53
    RB=54
    LP=55
    RP=56
    LC=57
    RC=58
    DOLLARID=59
    ID=60
    WS=61
    ERROR_CHAR=62

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

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def bclass(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.BclassContext)
            else:
                return self.getTypedRuleContext(D96Parser.BclassContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.bclass()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 109
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBclass" ):
                return visitor.visitBclass(self)
            else:
                return visitor.visitChildren(self)




    def bclass(self):

        localctx = D96Parser.BclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bclass)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(D96Parser.CLASS)
                self.state = 112
                self.match(D96Parser.ID)
                self.state = 113
                self.match(D96Parser.COLON)
                self.state = 114
                self.match(D96Parser.ID)
                self.state = 115
                self.class_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(D96Parser.CLASS)
                self.state = 117
                self.match(D96Parser.ID)
                self.state = 118
                self.class_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def class_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_stmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(D96Parser.LP)
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 122
                    self.class_stmt()
                    self.state = 125 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.DOLLARID) | (1 << D96Parser.ID))) != 0)):
                        break

                self.state = 127
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(D96Parser.LP)
                self.state = 130
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(D96Parser.FuncdeclContext,0)


        def valdecl(self):
            return self.getTypedRuleContext(D96Parser.ValdeclContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def vardecl(self):
            return self.getTypedRuleContext(D96Parser.VardeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_stmt" ):
                return visitor.visitClass_stmt(self)
            else:
                return visitor.visitChildren(self)




    def class_stmt(self):

        localctx = D96Parser.Class_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_stmt)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.destructor()
                pass
            elif token in [D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.funcdecl()
                pass
            elif token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.valdecl()
                self.state = 137
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.vardecl()
                self.state = 140
                self.match(D96Parser.SEMI)
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


    class Id_vasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_va(self):
            return self.getTypedRuleContext(D96Parser.Id_vaContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_vas

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_vas" ):
                return visitor.visitId_vas(self)
            else:
                return visitor.visitChildren(self)




    def id_vas(self):

        localctx = D96Parser.Id_vasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_id_vas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            self.id_va()

            self.state = 146
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_vaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def id_va(self):
            return self.getTypedRuleContext(D96Parser.Id_vaContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def dttyp(self):
            return self.getTypedRuleContext(D96Parser.DttypContext,0)


        def ASSOP(self):
            return self.getToken(D96Parser.ASSOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_id_va

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_va" ):
                return visitor.visitId_va(self)
            else:
                return visitor.visitChildren(self)




    def id_va(self):

        localctx = D96Parser.Id_vaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_id_va)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(D96Parser.COMMA)
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.id_va()

                self.state = 151
                self.expr()
                self.state = 152
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(D96Parser.COLON)
                self.state = 155
                self.dttyp()
                self.state = 156
                self.match(D96Parser.ASSOP)
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


    class ValdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def dttyp(self):
            return self.getTypedRuleContext(D96Parser.DttypContext,0)


        def id_vas(self):
            return self.getTypedRuleContext(D96Parser.Id_vasContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_valdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValdecl" ):
                return visitor.visitValdecl(self)
            else:
                return visitor.visitChildren(self)




    def valdecl(self):

        localctx = D96Parser.ValdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_valdecl)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(D96Parser.VAL)
                self.state = 161
                self.idlist()
                self.state = 162
                self.match(D96Parser.COLON)
                self.state = 163
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(D96Parser.VAL)
                self.state = 166
                self.id_vas()
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

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def dttyp(self):
            return self.getTypedRuleContext(D96Parser.DttypContext,0)


        def id_vas(self):
            return self.getTypedRuleContext(D96Parser.Id_vasContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = D96Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vardecl)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(D96Parser.VAR)
                self.state = 170
                self.idlist()
                self.state = 171
                self.match(D96Parser.COLON)
                self.state = 172
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(D96Parser.VAR)
                self.state = 175
                self.id_vas()
                pass


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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = D96Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.match(D96Parser.LB)
                self.state = 180
                self.paramlist()
                self.state = 181
                self.match(D96Parser.RB)
                self.state = 182
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.match(D96Parser.LB)
                self.state = 186
                self.match(D96Parser.RB)
                self.state = 187
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constructor)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 191
                self.match(D96Parser.LB)
                self.state = 192
                self.paramlist()
                self.state = 193
                self.match(D96Parser.RB)
                self.state = 194
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 197
                self.match(D96Parser.LB)
                self.state = 198
                self.match(D96Parser.RB)
                self.state = 199
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(D96Parser.DESTRUCTOR)
            self.state = 203
            self.match(D96Parser.LB)
            self.state = 204
            self.match(D96Parser.RB)
            self.state = 205
            self.blockstmt()
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
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = D96Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramlist)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.param()
                self.state = 208
                self.match(D96Parser.SEMI)
                self.state = 209
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
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

        def bidlist(self):
            return self.getTypedRuleContext(D96Parser.BidlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def dttyp(self):
            return self.getTypedRuleContext(D96Parser.DttypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.bidlist()
            self.state = 215
            self.match(D96Parser.COLON)
            self.state = 216
            self.dttyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BidlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def bidlist(self):
            return self.getTypedRuleContext(D96Parser.BidlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bidlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBidlist" ):
                return visitor.visitBidlist(self)
            else:
                return visitor.visitChildren(self)




    def bidlist(self):

        localctx = D96Parser.BidlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_bidlist)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(D96Parser.ID)
                self.state = 219
                self.match(D96Parser.COMMA)
                self.state = 220
                self.bidlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(D96Parser.ID)
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

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 225
                self.match(D96Parser.COMMA)
                self.state = 226
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def valuelist(self):
            return self.getTypedRuleContext(D96Parser.ValuelistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_valuelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValuelist" ):
                return visitor.visitValuelist(self)
            else:
                return visitor.visitChildren(self)




    def valuelist(self):

        localctx = D96Parser.ValuelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_valuelist)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.expr()
                self.state = 231
                self.match(D96Parser.COMMA)
                self.state = 232
                self.valuelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(D96Parser.StmtlistContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = D96Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_blockstmt)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(D96Parser.LP)
                self.state = 238
                self.stmtlist()
                self.state = 239
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(D96Parser.LP)
                self.state = 242
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(D96Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = D96Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmtlist)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.stmt()
                self.state = 246
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
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

        def semi_stmt(self):
            return self.getTypedRuleContext(D96Parser.Semi_stmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def foreachstmt(self):
            return self.getTypedRuleContext(D96Parser.ForeachstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(D96Parser.IfstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.ARRAY, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.RETURN, D96Parser.NEW, D96Parser.SELF, D96Parser.NOTOP, D96Parser.MINOP, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.semi_stmt()
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.blockstmt()
                pass
            elif token in [D96Parser.FOREACH]:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.foreachstmt()
                pass
            elif token in [D96Parser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.ifstmt()
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


    class Semi_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def bvaldecl(self):
            return self.getTypedRuleContext(D96Parser.BvaldeclContext,0)


        def bvardecl(self):
            return self.getTypedRuleContext(D96Parser.BvardeclContext,0)


        def varass(self):
            return self.getTypedRuleContext(D96Parser.VarassContext,0)


        def funccall(self):
            return self.getTypedRuleContext(D96Parser.FunccallContext,0)


        def rcb(self):
            return self.getTypedRuleContext(D96Parser.RcbContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_semi_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemi_stmt" ):
                return visitor.visitSemi_stmt(self)
            else:
                return visitor.visitChildren(self)




    def semi_stmt(self):

        localctx = D96Parser.Semi_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_semi_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 257
                self.bvaldecl()
                pass

            elif la_ == 2:
                self.state = 258
                self.bvardecl()
                pass

            elif la_ == 3:
                self.state = 259
                self.varass()
                pass

            elif la_ == 4:
                self.state = 260
                self.funccall()
                pass

            elif la_ == 5:
                self.state = 261
                self.rcb()
                pass


            self.state = 264
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bid_vasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def bid_va(self):
            return self.getTypedRuleContext(D96Parser.Bid_vaContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bid_vas

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBid_vas" ):
                return visitor.visitBid_vas(self)
            else:
                return visitor.visitChildren(self)




    def bid_vas(self):

        localctx = D96Parser.Bid_vasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bid_vas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(D96Parser.ID)
            self.state = 267
            self.bid_va()
            self.state = 268
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bid_vaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def bid_va(self):
            return self.getTypedRuleContext(D96Parser.Bid_vaContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def dttyp(self):
            return self.getTypedRuleContext(D96Parser.DttypContext,0)


        def ASSOP(self):
            return self.getToken(D96Parser.ASSOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_bid_va

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBid_va" ):
                return visitor.visitBid_va(self)
            else:
                return visitor.visitChildren(self)




    def bid_va(self):

        localctx = D96Parser.Bid_vaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bid_va)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(D96Parser.COMMA)
                self.state = 271
                self.match(D96Parser.ID)
                self.state = 272
                self.bid_va()
                self.state = 273
                self.expr()
                self.state = 274
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(D96Parser.COLON)
                self.state = 277
                self.dttyp()
                self.state = 278
                self.match(D96Parser.ASSOP)
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


    class BvaldeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def bidlist(self):
            return self.getTypedRuleContext(D96Parser.BidlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def dttyp(self):
            return self.getTypedRuleContext(D96Parser.DttypContext,0)


        def bid_vas(self):
            return self.getTypedRuleContext(D96Parser.Bid_vasContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bvaldecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBvaldecl" ):
                return visitor.visitBvaldecl(self)
            else:
                return visitor.visitChildren(self)




    def bvaldecl(self):

        localctx = D96Parser.BvaldeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_bvaldecl)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(D96Parser.VAL)
                self.state = 283
                self.bidlist()
                self.state = 284
                self.match(D96Parser.COLON)
                self.state = 285
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(D96Parser.VAL)
                self.state = 288
                self.bid_vas()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def bidlist(self):
            return self.getTypedRuleContext(D96Parser.BidlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def dttyp(self):
            return self.getTypedRuleContext(D96Parser.DttypContext,0)


        def bid_vas(self):
            return self.getTypedRuleContext(D96Parser.Bid_vasContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bvardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBvardecl" ):
                return visitor.visitBvardecl(self)
            else:
                return visitor.visitChildren(self)




    def bvardecl(self):

        localctx = D96Parser.BvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_bvardecl)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(D96Parser.VAR)
                self.state = 292
                self.bidlist()
                self.state = 293
                self.match(D96Parser.COLON)
                self.state = 294
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(D96Parser.VAR)
                self.state = 297
                self.bid_vas()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DCOLON(self):
            return self.getToken(D96Parser.DCOLON, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 301
                self.match(D96Parser.SELF)
                self.state = 302
                self.match(D96Parser.DOT)
                self.state = 303
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.state = 304
                self.match(D96Parser.ID)
                self.state = 305
                self.match(D96Parser.DCOLON)
                self.state = 306
                self.match(D96Parser.DOLLARID)
                pass

            elif la_ == 3:
                self.state = 307
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.LhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                    self.state = 310
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 311
                    self.match(D96Parser.DOT)
                    self.state = 312
                    self.match(D96Parser.ID) 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_lhs" ):
                return visitor.visitIndex_lhs(self)
            else:
                return visitor.visitChildren(self)




    def index_lhs(self):

        localctx = D96Parser.Index_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_index_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.lhs(0)
            self.state = 319
            self.index_operators()
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

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSOP(self):
            return self.getToken(D96Parser.ASSOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def index_lhs(self):
            return self.getTypedRuleContext(D96Parser.Index_lhsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarass" ):
                return visitor.visitVarass(self)
            else:
                return visitor.visitChildren(self)




    def varass(self):

        localctx = D96Parser.VarassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_varass)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.lhs(0)
                self.state = 322
                self.match(D96Parser.ASSOP)
                self.state = 323
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.index_lhs()
                self.state = 326
                self.match(D96Parser.ASSOP)
                self.state = 327
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def valuelist(self):
            return self.getTypedRuleContext(D96Parser.ValuelistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = D96Parser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(D96Parser.ID)
                self.state = 332
                self.match(D96Parser.LB)
                self.state = 333
                self.valuelist()
                self.state = 334
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(D96Parser.ID)
                self.state = 337
                self.match(D96Parser.LB)
                self.state = 338
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DollarfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def valuelist(self):
            return self.getTypedRuleContext(D96Parser.ValuelistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_dollarfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDollarfunc" ):
                return visitor.visitDollarfunc(self)
            else:
                return visitor.visitChildren(self)




    def dollarfunc(self):

        localctx = D96Parser.DollarfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_dollarfunc)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(D96Parser.DOLLARID)
                self.state = 342
                self.match(D96Parser.LB)
                self.state = 343
                self.valuelist()
                self.state = 344
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(D96Parser.DOLLARID)
                self.state = 347
                self.match(D96Parser.LB)
                self.state = 348
                self.match(D96Parser.RB)
                pass


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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def func(self):
            return self.getTypedRuleContext(D96Parser.FuncContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DCOLON(self):
            return self.getToken(D96Parser.DCOLON, 0)

        def dollarfunc(self):
            return self.getTypedRuleContext(D96Parser.DollarfuncContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = D96Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funccall)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.expr()
                self.state = 352
                self.match(D96Parser.DOT)
                self.state = 353
                self.func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(D96Parser.ID)
                self.state = 356
                self.match(D96Parser.DCOLON)
                self.state = 357
                self.dollarfunc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RcbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_rcb

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRcb" ):
                return visitor.visitRcb(self)
            else:
                return visitor.visitChildren(self)




    def rcb(self):

        localctx = D96Parser.RcbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_rcb)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(D96Parser.RETURN)
                self.state = 361
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(D96Parser.RETURN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.match(D96Parser.BREAK)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
                self.match(D96Parser.CONTINUE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DDOT(self):
            return self.getToken(D96Parser.DDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreachstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeachstmt" ):
                return visitor.visitForeachstmt(self)
            else:
                return visitor.visitChildren(self)




    def foreachstmt(self):

        localctx = D96Parser.ForeachstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_foreachstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(D96Parser.FOREACH)
            self.state = 368
            self.match(D96Parser.LB)
            self.state = 369
            self.match(D96Parser.ID)
            self.state = 370
            self.match(D96Parser.IN)
            self.state = 371
            self.expr()
            self.state = 372
            self.match(D96Parser.DDOT)
            self.state = 373
            self.expr()
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 374
                self.match(D96Parser.BY)
                self.state = 375
                self.expr()


            self.state = 378
            self.match(D96Parser.RB)
            self.state = 379
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifpart(self):
            return self.getTypedRuleContext(D96Parser.IfpartContext,0)


        def elseif_part(self):
            return self.getTypedRuleContext(D96Parser.Elseif_partContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = D96Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifstmt)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.ifpart()
                self.state = 382
                self.elseif_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.ifpart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfpartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfpart" ):
                return visitor.visitIfpart(self)
            else:
                return visitor.visitChildren(self)




    def ifpart(self):

        localctx = D96Parser.IfpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.IF)
            self.state = 388
            self.match(D96Parser.LB)
            self.state = 389
            self.expr()
            self.state = 390
            self.match(D96Parser.RB)
            self.state = 391
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def elseif_part(self):
            return self.getTypedRuleContext(D96Parser.Elseif_partContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_elseif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_part" ):
                return visitor.visitElseif_part(self)
            else:
                return visitor.visitChildren(self)




    def elseif_part(self):

        localctx = D96Parser.Elseif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elseif_part)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(D96Parser.ELSEIF)
                self.state = 394
                self.match(D96Parser.LB)
                self.state = 395
                self.expr()
                self.state = 396
                self.match(D96Parser.RB)
                self.state = 397
                self.blockstmt()
                self.state = 398
                self.elseif_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(D96Parser.ELSEIF)
                self.state = 401
                self.match(D96Parser.LB)
                self.state = 402
                self.expr()
                self.state = 403
                self.match(D96Parser.RB)
                self.state = 404
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(D96Parser.ELSE)
                self.state = 407
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_datatype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatatype" ):
                return visitor.visitDatatype(self)
            else:
                return visitor.visitChildren(self)




    def datatype(self):

        localctx = D96Parser.DatatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
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


    class DttypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LC(self):
            return self.getToken(D96Parser.LC, 0)

        def dttype(self):
            return self.getTypedRuleContext(D96Parser.DttypeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RC(self):
            return self.getToken(D96Parser.RC, 0)

        def datatype(self):
            return self.getTypedRuleContext(D96Parser.DatatypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_dttype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDttype" ):
                return visitor.visitDttype(self)
            else:
                return visitor.visitChildren(self)




    def dttype(self):

        localctx = D96Parser.DttypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_dttype)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(D96Parser.ARRAY)
                self.state = 413
                self.match(D96Parser.LC)
                self.state = 414
                self.dttype()
                self.state = 415
                self.match(D96Parser.COMMA)
                self.state = 416
                self.match(D96Parser.INTLIT)
                self.state = 417
                self.match(D96Parser.RC)
                pass
            elif token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.datatype()
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


    class DttypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dttype(self):
            return self.getTypedRuleContext(D96Parser.DttypeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_dttyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDttyp" ):
                return visitor.visitDttyp(self)
            else:
                return visitor.visitChildren(self)




    def dttyp(self):

        localctx = D96Parser.DttypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_dttyp)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY, D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.dttype()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(D96Parser.ID)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Term1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Term1Context,i)


        def STR(self):
            return self.getToken(D96Parser.STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.term1()
                self.state = 427
                self.match(D96Parser.STR)
                self.state = 428
                self.term1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.term1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Term2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Term2Context,i)


        def RELOP(self):
            return self.getToken(D96Parser.RELOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_term1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm1" ):
                return visitor.visitTerm1(self)
            else:
                return visitor.visitChildren(self)




    def term1(self):

        localctx = D96Parser.Term1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_term1)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.term2(0)
                self.state = 434
                self.match(D96Parser.RELOP)
                self.state = 435
                self.term2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.term2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term3(self):
            return self.getTypedRuleContext(D96Parser.Term3Context,0)


        def term2(self):
            return self.getTypedRuleContext(D96Parser.Term2Context,0)


        def OROP(self):
            return self.getToken(D96Parser.OROP, 0)

        def ANDOP(self):
            return self.getToken(D96Parser.ANDOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_term2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm2" ):
                return visitor.visitTerm2(self)
            else:
                return visitor.visitChildren(self)



    def term2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Term2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_term2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 449
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Term2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                        self.state = 443
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 444
                        self.match(D96Parser.OROP)
                        self.state = 445
                        self.term3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Term2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                        self.state = 446
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 447
                        self.match(D96Parser.ANDOP)
                        self.state = 448
                        self.term3(0)
                        pass

             
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term4(self):
            return self.getTypedRuleContext(D96Parser.Term4Context,0)


        def term3(self):
            return self.getTypedRuleContext(D96Parser.Term3Context,0)


        def ADDOP(self):
            return self.getToken(D96Parser.ADDOP, 0)

        def MINOP(self):
            return self.getToken(D96Parser.MINOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_term3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm3" ):
                return visitor.visitTerm3(self)
            else:
                return visitor.visitChildren(self)



    def term3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Term3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_term3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.term4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 463
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Term3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                        self.state = 457
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 458
                        self.match(D96Parser.ADDOP)
                        self.state = 459
                        self.term4(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Term3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                        self.state = 460
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 461
                        self.match(D96Parser.MINOP)
                        self.state = 462
                        self.term4(0)
                        pass

             
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term5(self):
            return self.getTypedRuleContext(D96Parser.Term5Context,0)


        def term4(self):
            return self.getTypedRuleContext(D96Parser.Term4Context,0)


        def MULOP(self):
            return self.getToken(D96Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(D96Parser.DIVOP, 0)

        def REMOP(self):
            return self.getToken(D96Parser.REMOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_term4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm4" ):
                return visitor.visitTerm4(self)
            else:
                return visitor.visitChildren(self)



    def term4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Term4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_term4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.term5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 480
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Term4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                        self.state = 471
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 472
                        self.match(D96Parser.MULOP)
                        self.state = 473
                        self.term5()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Term4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                        self.state = 474
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 475
                        self.match(D96Parser.DIVOP)
                        self.state = 476
                        self.term5()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Term4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                        self.state = 477
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 478
                        self.match(D96Parser.REMOP)
                        self.state = 479
                        self.term5()
                        pass

             
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(D96Parser.NOTOP, 0)

        def term5(self):
            return self.getTypedRuleContext(D96Parser.Term5Context,0)


        def term6(self):
            return self.getTypedRuleContext(D96Parser.Term6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_term5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm5" ):
                return visitor.visitTerm5(self)
            else:
                return visitor.visitChildren(self)




    def term5(self):

        localctx = D96Parser.Term5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_term5)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(D96Parser.NOTOP)
                self.state = 486
                self.term5()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ARRAY, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINOP, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.term6()
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


    class Term6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINOP(self):
            return self.getToken(D96Parser.MINOP, 0)

        def term6(self):
            return self.getTypedRuleContext(D96Parser.Term6Context,0)


        def term7(self):
            return self.getTypedRuleContext(D96Parser.Term7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_term6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm6" ):
                return visitor.visitTerm6(self)
            else:
                return visitor.visitChildren(self)




    def term6(self):

        localctx = D96Parser.Term6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_term6)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.match(D96Parser.MINOP)
                self.state = 491
                self.term6()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ARRAY, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
                self.term7()
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


    class Term7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term8(self):
            return self.getTypedRuleContext(D96Parser.Term8Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_term7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm7" ):
                return visitor.visitTerm7(self)
            else:
                return visitor.visitChildren(self)




    def term7(self):

        localctx = D96Parser.Term7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_term7)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.term8(0)
                self.state = 496
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.term8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(D96Parser.LC, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RC(self):
            return self.getToken(D96Parser.RC, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_index_operators)
        try:
            self.state = 510
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(D96Parser.LC)
                self.state = 502
                self.expr()
                self.state = 503
                self.match(D96Parser.RC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.match(D96Parser.LC)
                self.state = 506
                self.expr()
                self.state = 507
                self.match(D96Parser.RC)
                self.state = 508
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term9(self):
            return self.getTypedRuleContext(D96Parser.Term9Context,0)


        def term8(self):
            return self.getTypedRuleContext(D96Parser.Term8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(D96Parser.FuncContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_term8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm8" ):
                return visitor.visitTerm8(self)
            else:
                return visitor.visitChildren(self)



    def term8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Term8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_term8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.term9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 523
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Term8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term8)
                    self.state = 515
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 516
                    self.match(D96Parser.DOT)
                    self.state = 519
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 517
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 518
                        self.func()
                        pass

             
                self.state = 525
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DCOLON(self):
            return self.getToken(D96Parser.DCOLON, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def dollarfunc(self):
            return self.getTypedRuleContext(D96Parser.DollarfuncContext,0)


        def term10(self):
            return self.getTypedRuleContext(D96Parser.Term10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_term9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm9" ):
                return visitor.visitTerm9(self)
            else:
                return visitor.visitChildren(self)




    def term9(self):

        localctx = D96Parser.Term9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_term9)
        try:
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(D96Parser.ID)
                self.state = 527
                self.match(D96Parser.DCOLON)
                self.state = 530
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 528
                    self.match(D96Parser.DOLLARID)
                    pass

                elif la_ == 2:
                    self.state = 529
                    self.dollarfunc()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.term10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def valuelist(self):
            return self.getTypedRuleContext(D96Parser.ValuelistContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_term10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm10" ):
                return visitor.visitTerm10(self)
            else:
                return visitor.visitChildren(self)




    def term10(self):

        localctx = D96Parser.Term10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_term10)
        self._la = 0 # Token type
        try:
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 535
                self.match(D96Parser.NEW)
                self.state = 536
                self.match(D96Parser.ID)
                self.state = 537
                self.match(D96Parser.LB)
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.NOTOP) | (1 << D96Parser.MINOP) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                    self.state = 538
                    self.valuelist()


                self.state = 541
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 543
                self.match(D96Parser.LB)
                self.state = 544
                self.expr()
                self.state = 545
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.ARRAY, D96Parser.TRUE, D96Parser.FALSE, D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 547
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 548
                self.match(D96Parser.SELF)
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def arrayCell(self):
            return self.getTypedRuleContext(D96Parser.ArrayCellContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literal)
        try:
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.match(D96Parser.TRUE)
                pass
            elif token in [D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.match(D96Parser.FALSE)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 553
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 554
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 555
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ZERO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 556
                self.match(D96Parser.ZERO)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 557
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 8)
                self.state = 558
                self.arrayCell()
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


    class ArrayCellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def valuelist(self):
            return self.getTypedRuleContext(D96Parser.ValuelistContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayCell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayCell" ):
                return visitor.visitArrayCell(self)
            else:
                return visitor.visitChildren(self)




    def arrayCell(self):

        localctx = D96Parser.ArrayCellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arrayCell)
        try:
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
                self.match(D96Parser.ARRAY)
                self.state = 562
                self.match(D96Parser.LB)
                self.state = 563
                self.valuelist()
                self.state = 564
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.match(D96Parser.ARRAY)
                self.state = 567
                self.match(D96Parser.LB)
                self.state = 568
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.lhs_sempred
        self._predicates[40] = self.term2_sempred
        self._predicates[41] = self.term3_sempred
        self._predicates[42] = self.term4_sempred
        self._predicates[47] = self.term8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

    def term2_sempred(self, localctx:Term2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term3_sempred(self, localctx:Term3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def term4_sempred(self, localctx:Term4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def term8_sempred(self, localctx:Term8Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




