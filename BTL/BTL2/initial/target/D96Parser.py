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
        buf.write("\u024a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3|\n\3\3\4\3\4\3\4\3\4\5\4\u0082")
        buf.write("\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u008c\n\5\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0092\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u0099")
        buf.write("\n\7\3\7\3\7\5\7\u009d\n\7\3\b\3\b\3\b\5\b\u00a2\n\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u00b5\n\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00be\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00c7\n\f\3\r\3\r\3\r\5\r\u00cc\n\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00e0\n\20\3\21\3\21\5\21\u00e4\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00ef\n\23\3\24\3\24\3\24\3\24\5\24\u00f5\n\24\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u00fb\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u0105\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u010c\n\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0114\n\30\3\31\3\31\3\31\3\31\5\31\u011a\n\31\3\32\3")
        buf.write("\32\3\32\3\32\5\32\u0120\n\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u0129\n\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u013b\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u0144\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u014d\n\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u0157\n \3 \3 ")
        buf.write("\3 \7 \u015c\n \f \16 \u015f\13 \3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u016d\n\"\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\5#\u0177\n#\3$\3$\3$\5$\u017c\n$\3$\3$\3%\3")
        buf.write("%\3%\5%\u0183\n%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u0191\n&\3\'\3\'\5\'\u0195\n\'\3(\3(\3)\3)\3*\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\5*\u01a4\n*\3*\3*\3*\3+\3+\3+\3+\5")
        buf.write("+\u01ad\n+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\5-\u01c4\n-\3.\3.\3.\3.\3.\5.\u01cb")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u01d2\n/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\7\60\u01dd\n\60\f\60\16\60\u01e0")
        buf.write("\13\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u01eb\n\61\f\61\16\61\u01ee\13\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u01fc")
        buf.write("\n\62\f\62\16\62\u01ff\13\62\3\63\3\63\3\63\5\63\u0204")
        buf.write("\n\63\3\64\3\64\3\64\5\64\u0209\n\64\3\65\3\65\3\65\3")
        buf.write("\65\5\65\u020f\n\65\3\66\3\66\3\66\3\66\5\66\u0215\n\66")
        buf.write("\3\66\5\66\u0218\n\66\3\66\3\66\3\66\3\66\5\66\u021e\n")
        buf.write("\66\7\66\u0220\n\66\f\66\16\66\u0223\13\66\3\67\3\67\3")
        buf.write("\67\3\67\5\67\u0229\n\67\3\67\5\67\u022c\n\67\38\38\3")
        buf.write("8\38\58\u0232\n8\38\38\38\38\38\38\38\58\u023b\n8\39\3")
        buf.write("9\39\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0248\n:\3:\2\7>^`bj;")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\4\3\2=>\4\2\27")
        buf.write("\27\31\33\2\u025d\2t\3\2\2\2\4{\3\2\2\2\6}\3\2\2\2\b\u008b")
        buf.write("\3\2\2\2\n\u0091\3\2\2\2\f\u009c\3\2\2\2\16\u009e\3\2")
        buf.write("\2\2\20\u00a6\3\2\2\2\22\u00b4\3\2\2\2\24\u00bd\3\2\2")
        buf.write("\2\26\u00c6\3\2\2\2\30\u00c8\3\2\2\2\32\u00d0\3\2\2\2")
        buf.write("\34\u00d5\3\2\2\2\36\u00df\3\2\2\2 \u00e3\3\2\2\2\"\u00e5")
        buf.write("\3\2\2\2$\u00ee\3\2\2\2&\u00f4\3\2\2\2(\u00fa\3\2\2\2")
        buf.write("*\u0104\3\2\2\2,\u010b\3\2\2\2.\u0113\3\2\2\2\60\u0119")
        buf.write("\3\2\2\2\62\u011f\3\2\2\2\64\u0128\3\2\2\2\66\u012c\3")
        buf.write("\2\2\28\u013a\3\2\2\2:\u0143\3\2\2\2<\u014c\3\2\2\2>\u0156")
        buf.write("\3\2\2\2@\u0160\3\2\2\2B\u016c\3\2\2\2D\u0176\3\2\2\2")
        buf.write("F\u0178\3\2\2\2H\u017f\3\2\2\2J\u0190\3\2\2\2L\u0192\3")
        buf.write("\2\2\2N\u0196\3\2\2\2P\u0198\3\2\2\2R\u019a\3\2\2\2T\u01ac")
        buf.write("\3\2\2\2V\u01ae\3\2\2\2X\u01c3\3\2\2\2Z\u01ca\3\2\2\2")
        buf.write("\\\u01d1\3\2\2\2^\u01d3\3\2\2\2`\u01e1\3\2\2\2b\u01ef")
        buf.write("\3\2\2\2d\u0203\3\2\2\2f\u0208\3\2\2\2h\u020e\3\2\2\2")
        buf.write("j\u0217\3\2\2\2l\u022b\3\2\2\2n\u023a\3\2\2\2p\u023c\3")
        buf.write("\2\2\2r\u0247\3\2\2\2tu\5\4\3\2uv\7\2\2\3v\3\3\2\2\2w")
        buf.write("x\5\6\4\2xy\5\4\3\2y|\3\2\2\2z|\5\6\4\2{w\3\2\2\2{z\3")
        buf.write("\2\2\2|\5\3\2\2\2}~\7\36\2\2~\u0081\7>\2\2\177\u0080\7")
        buf.write("8\2\2\u0080\u0082\7>\2\2\u0081\177\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\5\b\5\2\u0084")
        buf.write("\7\3\2\2\2\u0085\u0086\7\63\2\2\u0086\u0087\5\n\6\2\u0087")
        buf.write("\u0088\7\64\2\2\u0088\u008c\3\2\2\2\u0089\u008a\7\63\2")
        buf.write("\2\u008a\u008c\7\64\2\2\u008b\u0085\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008c\t\3\2\2\2\u008d\u008e\5\f\7\2\u008e\u008f")
        buf.write("\5\n\6\2\u008f\u0092\3\2\2\2\u0090\u0092\5\f\7\2\u0091")
        buf.write("\u008d\3\2\2\2\u0091\u0090\3\2\2\2\u0092\13\3\2\2\2\u0093")
        buf.write("\u009d\5\30\r\2\u0094\u009d\5\32\16\2\u0095\u009d\5\16")
        buf.write("\b\2\u0096\u0099\5\24\13\2\u0097\u0099\5\26\f\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\7:\2\2\u009b\u009d\3\2\2\2\u009c\u0093\3")
        buf.write("\2\2\2\u009c\u0094\3\2\2\2\u009c\u0095\3\2\2\2\u009c\u0098")
        buf.write("\3\2\2\2\u009d\r\3\2\2\2\u009e\u009f\t\2\2\2\u009f\u00a1")
        buf.write("\7\61\2\2\u00a0\u00a2\5$\23\2\u00a1\u00a0\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\7\62\2")
        buf.write("\2\u00a4\u00a5\5.\30\2\u00a5\17\3\2\2\2\u00a6\u00a7\t")
        buf.write("\2\2\2\u00a7\u00a8\5\22\n\2\u00a8\u00a9\5Z.\2\u00a9\21")
        buf.write("\3\2\2\2\u00aa\u00ab\79\2\2\u00ab\u00ac\t\2\2\2\u00ac")
        buf.write("\u00ad\5\22\n\2\u00ad\u00ae\5Z.\2\u00ae\u00af\79\2\2\u00af")
        buf.write("\u00b5\3\2\2\2\u00b0\u00b1\78\2\2\u00b1\u00b2\5 \21\2")
        buf.write("\u00b2\u00b3\7\60\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00aa")
        buf.write("\3\2\2\2\u00b4\u00b0\3\2\2\2\u00b5\23\3\2\2\2\u00b6\u00b7")
        buf.write("\7\37\2\2\u00b7\u00b8\5(\25\2\u00b8\u00b9\78\2\2\u00b9")
        buf.write("\u00ba\5 \21\2\u00ba\u00be\3\2\2\2\u00bb\u00bc\7\37\2")
        buf.write("\2\u00bc\u00be\5\20\t\2\u00bd\u00b6\3\2\2\2\u00bd\u00bb")
        buf.write("\3\2\2\2\u00be\25\3\2\2\2\u00bf\u00c0\7 \2\2\u00c0\u00c1")
        buf.write("\5(\25\2\u00c1\u00c2\78\2\2\u00c2\u00c3\5 \21\2\u00c3")
        buf.write("\u00c7\3\2\2\2\u00c4\u00c5\7 \2\2\u00c5\u00c7\5\20\t\2")
        buf.write("\u00c6\u00bf\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\27\3\2")
        buf.write("\2\2\u00c8\u00c9\7!\2\2\u00c9\u00cb\7\61\2\2\u00ca\u00cc")
        buf.write("\5$\23\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00ce\7\62\2\2\u00ce\u00cf\5.\30")
        buf.write("\2\u00cf\31\3\2\2\2\u00d0\u00d1\7\"\2\2\u00d1\u00d2\7")
        buf.write("\61\2\2\u00d2\u00d3\7\62\2\2\u00d3\u00d4\5.\30\2\u00d4")
        buf.write("\33\3\2\2\2\u00d5\u00d6\t\3\2\2\u00d6\35\3\2\2\2\u00d7")
        buf.write("\u00d8\7\26\2\2\u00d8\u00d9\7\65\2\2\u00d9\u00da\5\36")
        buf.write("\20\2\u00da\u00db\79\2\2\u00db\u00dc\7\3\2\2\u00dc\u00dd")
        buf.write("\7\66\2\2\u00dd\u00e0\3\2\2\2\u00de\u00e0\5\34\17\2\u00df")
        buf.write("\u00d7\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\37\3\2\2\2\u00e1")
        buf.write("\u00e4\5\36\20\2\u00e2\u00e4\7>\2\2\u00e3\u00e1\3\2\2")
        buf.write("\2\u00e3\u00e2\3\2\2\2\u00e4!\3\2\2\2\u00e5\u00e6\5&\24")
        buf.write("\2\u00e6\u00e7\78\2\2\u00e7\u00e8\5 \21\2\u00e8#\3\2\2")
        buf.write("\2\u00e9\u00ea\5\"\22\2\u00ea\u00eb\7:\2\2\u00eb\u00ec")
        buf.write("\5$\23\2\u00ec\u00ef\3\2\2\2\u00ed\u00ef\5\"\22\2\u00ee")
        buf.write("\u00e9\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef%\3\2\2\2\u00f0")
        buf.write("\u00f1\7>\2\2\u00f1\u00f2\79\2\2\u00f2\u00f5\5&\24\2\u00f3")
        buf.write("\u00f5\7>\2\2\u00f4\u00f0\3\2\2\2\u00f4\u00f3\3\2\2\2")
        buf.write("\u00f5\'\3\2\2\2\u00f6\u00f7\t\2\2\2\u00f7\u00f8\79\2")
        buf.write("\2\u00f8\u00fb\5(\25\2\u00f9\u00fb\t\2\2\2\u00fa\u00f6")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb)\3\2\2\2\u00fc\u0105")
        buf.write("\7\24\2\2\u00fd\u0105\7\25\2\2\u00fe\u0105\7\t\2\2\u00ff")
        buf.write("\u0105\7\3\2\2\u0100\u0105\7\13\2\2\u0101\u0105\7\b\2")
        buf.write("\2\u0102\u0105\7\35\2\2\u0103\u0105\5r:\2\u0104\u00fc")
        buf.write("\3\2\2\2\u0104\u00fd\3\2\2\2\u0104\u00fe\3\2\2\2\u0104")
        buf.write("\u00ff\3\2\2\2\u0104\u0100\3\2\2\2\u0104\u0101\3\2\2\2")
        buf.write("\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105+\3\2\2")
        buf.write("\2\u0106\u0107\5Z.\2\u0107\u0108\79\2\2\u0108\u0109\5")
        buf.write(",\27\2\u0109\u010c\3\2\2\2\u010a\u010c\5Z.\2\u010b\u0106")
        buf.write("\3\2\2\2\u010b\u010a\3\2\2\2\u010c-\3\2\2\2\u010d\u010e")
        buf.write("\7\63\2\2\u010e\u010f\5\60\31\2\u010f\u0110\7\64\2\2\u0110")
        buf.write("\u0114\3\2\2\2\u0111\u0112\7\63\2\2\u0112\u0114\7\64\2")
        buf.write("\2\u0113\u010d\3\2\2\2\u0113\u0111\3\2\2\2\u0114/\3\2")
        buf.write("\2\2\u0115\u0116\5\62\32\2\u0116\u0117\5\60\31\2\u0117")
        buf.write("\u011a\3\2\2\2\u0118\u011a\5\62\32\2\u0119\u0115\3\2\2")
        buf.write("\2\u0119\u0118\3\2\2\2\u011a\61\3\2\2\2\u011b\u0120\5")
        buf.write("\64\33\2\u011c\u0120\5R*\2\u011d\u0120\5T+\2\u011e\u0120")
        buf.write("\5.\30\2\u011f\u011b\3\2\2\2\u011f\u011c\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120\63\3\2\2\2\u0121")
        buf.write("\u0129\5:\36\2\u0122\u0129\5<\37\2\u0123\u0129\5D#\2\u0124")
        buf.write("\u0129\5L\'\2\u0125\u0129\5J&\2\u0126\u0129\5P)\2\u0127")
        buf.write("\u0129\5N(\2\u0128\u0121\3\2\2\2\u0128\u0122\3\2\2\2\u0128")
        buf.write("\u0123\3\2\2\2\u0128\u0124\3\2\2\2\u0128\u0125\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0127\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u012b\7:\2\2\u012b\65\3\2\2\2\u012c\u012d")
        buf.write("\7>\2\2\u012d\u012e\58\35\2\u012e\u012f\5Z.\2\u012f\67")
        buf.write("\3\2\2\2\u0130\u0131\79\2\2\u0131\u0132\7>\2\2\u0132\u0133")
        buf.write("\58\35\2\u0133\u0134\5Z.\2\u0134\u0135\79\2\2\u0135\u013b")
        buf.write("\3\2\2\2\u0136\u0137\78\2\2\u0137\u0138\5 \21\2\u0138")
        buf.write("\u0139\7\60\2\2\u0139\u013b\3\2\2\2\u013a\u0130\3\2\2")
        buf.write("\2\u013a\u0136\3\2\2\2\u013b9\3\2\2\2\u013c\u013d\7\37")
        buf.write("\2\2\u013d\u013e\5&\24\2\u013e\u013f\78\2\2\u013f\u0140")
        buf.write("\5 \21\2\u0140\u0144\3\2\2\2\u0141\u0142\7\37\2\2\u0142")
        buf.write("\u0144\5\66\34\2\u0143\u013c\3\2\2\2\u0143\u0141\3\2\2")
        buf.write("\2\u0144;\3\2\2\2\u0145\u0146\7 \2\2\u0146\u0147\5&\24")
        buf.write("\2\u0147\u0148\78\2\2\u0148\u0149\5 \21\2\u0149\u014d")
        buf.write("\3\2\2\2\u014a\u014b\7 \2\2\u014b\u014d\5\66\34\2\u014c")
        buf.write("\u0145\3\2\2\2\u014c\u014a\3\2\2\2\u014d=\3\2\2\2\u014e")
        buf.write("\u014f\b \1\2\u014f\u0150\7>\2\2\u0150\u0151\7\67\2\2")
        buf.write("\u0151\u0157\7=\2\2\u0152\u0153\5p9\2\u0153\u0154\7>\2")
        buf.write("\2\u0154\u0157\3\2\2\2\u0155\u0157\7>\2\2\u0156\u014e")
        buf.write("\3\2\2\2\u0156\u0152\3\2\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u015d\3\2\2\2\u0158\u0159\f\6\2\2\u0159\u015a\7<\2\2")
        buf.write("\u015a\u015c\7>\2\2\u015b\u0158\3\2\2\2\u015c\u015f\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e?")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\5> \2\u0161\u0162")
        buf.write("\5B\"\2\u0162A\3\2\2\2\u0163\u0164\7\65\2\2\u0164\u0165")
        buf.write("\5Z.\2\u0165\u0166\7\66\2\2\u0166\u016d\3\2\2\2\u0167")
        buf.write("\u0168\7\65\2\2\u0168\u0169\5Z.\2\u0169\u016a\7\66\2\2")
        buf.write("\u016a\u016b\5B\"\2\u016b\u016d\3\2\2\2\u016c\u0163\3")
        buf.write("\2\2\2\u016c\u0167\3\2\2\2\u016dC\3\2\2\2\u016e\u016f")
        buf.write("\5> \2\u016f\u0170\7\60\2\2\u0170\u0171\5Z.\2\u0171\u0177")
        buf.write("\3\2\2\2\u0172\u0173\5@!\2\u0173\u0174\7\60\2\2\u0174")
        buf.write("\u0175\5Z.\2\u0175\u0177\3\2\2\2\u0176\u016e\3\2\2\2\u0176")
        buf.write("\u0172\3\2\2\2\u0177E\3\2\2\2\u0178\u0179\7>\2\2\u0179")
        buf.write("\u017b\7\61\2\2\u017a\u017c\5,\27\2\u017b\u017a\3\2\2")
        buf.write("\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e")
        buf.write("\7\62\2\2\u017eG\3\2\2\2\u017f\u0180\7=\2\2\u0180\u0182")
        buf.write("\7\61\2\2\u0181\u0183\5,\27\2\u0182\u0181\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\7\62\2")
        buf.write("\2\u0185I\3\2\2\2\u0186\u0187\5Z.\2\u0187\u0188\7<\2\2")
        buf.write("\u0188\u0189\5F$\2\u0189\u0191\3\2\2\2\u018a\u018b\7>")
        buf.write("\2\2\u018b\u018c\7\67\2\2\u018c\u0191\5H%\2\u018d\u018e")
        buf.write("\5p9\2\u018e\u018f\5F$\2\u018f\u0191\3\2\2\2\u0190\u0186")
        buf.write("\3\2\2\2\u0190\u018a\3\2\2\2\u0190\u018d\3\2\2\2\u0191")
        buf.write("K\3\2\2\2\u0192\u0194\7\34\2\2\u0193\u0195\5Z.\2\u0194")
        buf.write("\u0193\3\2\2\2\u0194\u0195\3\2\2\2\u0195M\3\2\2\2\u0196")
        buf.write("\u0197\7\17\2\2\u0197O\3\2\2\2\u0198\u0199\7\16\2\2\u0199")
        buf.write("Q\3\2\2\2\u019a\u019b\7\23\2\2\u019b\u019c\7\61\2\2\u019c")
        buf.write("\u019d\7>\2\2\u019d\u019e\7\30\2\2\u019e\u019f\5Z.\2\u019f")
        buf.write("\u01a0\7;\2\2\u01a0\u01a3\5Z.\2\u01a1\u01a2\7$\2\2\u01a2")
        buf.write("\u01a4\5Z.\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a6\7\62\2\2\u01a6\u01a7\5.\30")
        buf.write("\2\u01a7S\3\2\2\2\u01a8\u01a9\5V,\2\u01a9\u01aa\5X-\2")
        buf.write("\u01aa\u01ad\3\2\2\2\u01ab\u01ad\5V,\2\u01ac\u01a8\3\2")
        buf.write("\2\2\u01ac\u01ab\3\2\2\2\u01adU\3\2\2\2\u01ae\u01af\7")
        buf.write("\20\2\2\u01af\u01b0\7\61\2\2\u01b0\u01b1\5Z.\2\u01b1\u01b2")
        buf.write("\7\62\2\2\u01b2\u01b3\5.\30\2\u01b3W\3\2\2\2\u01b4\u01b5")
        buf.write("\7\21\2\2\u01b5\u01b6\7\61\2\2\u01b6\u01b7\5Z.\2\u01b7")
        buf.write("\u01b8\7\62\2\2\u01b8\u01b9\5.\30\2\u01b9\u01ba\5X-\2")
        buf.write("\u01ba\u01c4\3\2\2\2\u01bb\u01bc\7\21\2\2\u01bc\u01bd")
        buf.write("\7\61\2\2\u01bd\u01be\5Z.\2\u01be\u01bf\7\62\2\2\u01bf")
        buf.write("\u01c0\5.\30\2\u01c0\u01c4\3\2\2\2\u01c1\u01c2\7\22\2")
        buf.write("\2\u01c2\u01c4\5.\30\2\u01c3\u01b4\3\2\2\2\u01c3\u01bb")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4Y\3\2\2\2\u01c5\u01c6")
        buf.write("\5\\/\2\u01c6\u01c7\7&\2\2\u01c7\u01c8\5\\/\2\u01c8\u01cb")
        buf.write("\3\2\2\2\u01c9\u01cb\5\\/\2\u01ca\u01c5\3\2\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb[\3\2\2\2\u01cc\u01cd\5^\60\2\u01cd")
        buf.write("\u01ce\7\'\2\2\u01ce\u01cf\5^\60\2\u01cf\u01d2\3\2\2\2")
        buf.write("\u01d0\u01d2\5^\60\2\u01d1\u01cc\3\2\2\2\u01d1\u01d0\3")
        buf.write("\2\2\2\u01d2]\3\2\2\2\u01d3\u01d4\b\60\1\2\u01d4\u01d5")
        buf.write("\5`\61\2\u01d5\u01de\3\2\2\2\u01d6\u01d7\f\5\2\2\u01d7")
        buf.write("\u01d8\7*\2\2\u01d8\u01dd\5`\61\2\u01d9\u01da\f\4\2\2")
        buf.write("\u01da\u01db\7)\2\2\u01db\u01dd\5`\61\2\u01dc\u01d6\3")
        buf.write("\2\2\2\u01dc\u01d9\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df_\3\2\2\2\u01e0\u01de")
        buf.write("\3\2\2\2\u01e1\u01e2\b\61\1\2\u01e2\u01e3\5b\62\2\u01e3")
        buf.write("\u01ec\3\2\2\2\u01e4\u01e5\f\5\2\2\u01e5\u01e6\7+\2\2")
        buf.write("\u01e6\u01eb\5b\62\2\u01e7\u01e8\f\4\2\2\u01e8\u01e9\7")
        buf.write(",\2\2\u01e9\u01eb\5b\62\2\u01ea\u01e4\3\2\2\2\u01ea\u01e7")
        buf.write("\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01eda\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef")
        buf.write("\u01f0\b\62\1\2\u01f0\u01f1\5d\63\2\u01f1\u01fd\3\2\2")
        buf.write("\2\u01f2\u01f3\f\6\2\2\u01f3\u01f4\7-\2\2\u01f4\u01fc")
        buf.write("\5d\63\2\u01f5\u01f6\f\5\2\2\u01f6\u01f7\7.\2\2\u01f7")
        buf.write("\u01fc\5d\63\2\u01f8\u01f9\f\4\2\2\u01f9\u01fa\7/\2\2")
        buf.write("\u01fa\u01fc\5d\63\2\u01fb\u01f2\3\2\2\2\u01fb\u01f5\3")
        buf.write("\2\2\2\u01fb\u01f8\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fec\3\2\2\2\u01ff\u01fd")
        buf.write("\3\2\2\2\u0200\u0201\7(\2\2\u0201\u0204\5d\63\2\u0202")
        buf.write("\u0204\5f\64\2\u0203\u0200\3\2\2\2\u0203\u0202\3\2\2\2")
        buf.write("\u0204e\3\2\2\2\u0205\u0206\7,\2\2\u0206\u0209\5f\64\2")
        buf.write("\u0207\u0209\5h\65\2\u0208\u0205\3\2\2\2\u0208\u0207\3")
        buf.write("\2\2\2\u0209g\3\2\2\2\u020a\u020b\5j\66\2\u020b\u020c")
        buf.write("\5B\"\2\u020c\u020f\3\2\2\2\u020d\u020f\5j\66\2\u020e")
        buf.write("\u020a\3\2\2\2\u020e\u020d\3\2\2\2\u020fi\3\2\2\2\u0210")
        buf.write("\u0211\b\66\1\2\u0211\u0214\5p9\2\u0212\u0215\7>\2\2\u0213")
        buf.write("\u0215\5F$\2\u0214\u0212\3\2\2\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("\u0218\3\2\2\2\u0216\u0218\5l\67\2\u0217\u0210\3\2\2\2")
        buf.write("\u0217\u0216\3\2\2\2\u0218\u0221\3\2\2\2\u0219\u021a\f")
        buf.write("\5\2\2\u021a\u021d\7<\2\2\u021b\u021e\7>\2\2\u021c\u021e")
        buf.write("\5F$\2\u021d\u021b\3\2\2\2\u021d\u021c\3\2\2\2\u021e\u0220")
        buf.write("\3\2\2\2\u021f\u0219\3\2\2\2\u0220\u0223\3\2\2\2\u0221")
        buf.write("\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222k\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0224\u0225\7>\2\2\u0225\u0228\7\67\2\2")
        buf.write("\u0226\u0229\7=\2\2\u0227\u0229\5H%\2\u0228\u0226\3\2")
        buf.write("\2\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u022c")
        buf.write("\5n8\2\u022b\u0224\3\2\2\2\u022b\u022a\3\2\2\2\u022cm")
        buf.write("\3\2\2\2\u022d\u022e\7#\2\2\u022e\u022f\7>\2\2\u022f\u0231")
        buf.write("\7\61\2\2\u0230\u0232\5,\27\2\u0231\u0230\3\2\2\2\u0231")
        buf.write("\u0232\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u023b\7\62\2")
        buf.write("\2\u0234\u023b\7>\2\2\u0235\u0236\7\61\2\2\u0236\u0237")
        buf.write("\5Z.\2\u0237\u0238\7\62\2\2\u0238\u023b\3\2\2\2\u0239")
        buf.write("\u023b\5*\26\2\u023a\u022d\3\2\2\2\u023a\u0234\3\2\2\2")
        buf.write("\u023a\u0235\3\2\2\2\u023a\u0239\3\2\2\2\u023bo\3\2\2")
        buf.write("\2\u023c\u023d\7%\2\2\u023d\u023e\7<\2\2\u023eq\3\2\2")
        buf.write("\2\u023f\u0240\7\26\2\2\u0240\u0241\7\61\2\2\u0241\u0242")
        buf.write("\5,\27\2\u0242\u0243\7\62\2\2\u0243\u0248\3\2\2\2\u0244")
        buf.write("\u0245\7\26\2\2\u0245\u0246\7\61\2\2\u0246\u0248\7\62")
        buf.write("\2\2\u0247\u023f\3\2\2\2\u0247\u0244\3\2\2\2\u0248s\3")
        buf.write("\2\2\2:{\u0081\u008b\u0091\u0098\u009c\u00a1\u00b4\u00bd")
        buf.write("\u00c6\u00cb\u00df\u00e3\u00ee\u00f4\u00fa\u0104\u010b")
        buf.write("\u0113\u0119\u011f\u0128\u013a\u0143\u014c\u0156\u015d")
        buf.write("\u016c\u0176\u017b\u0182\u0190\u0194\u01a3\u01ac\u01c3")
        buf.write("\u01ca\u01d1\u01dc\u01de\u01ea\u01ec\u01fb\u01fd\u0203")
        buf.write("\u0208\u020e\u0214\u0217\u021d\u0221\u0228\u022b\u0231")
        buf.write("\u023a\u0247")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
                     "'Foreach'", "'True'", "'False'", "'Array'", "'Int'", 
                     "'In'", "'Float'", "'Boolean'", "'String'", "'Return'", 
                     "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "'Self'", "<INVALID>", 
                     "<INVALID>", "'!'", "'&&'", "'||'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'::'", "':'", "','", "';'", "'..'", "'.'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "BIN", "OCT", "DEC", "HEX", 
                      "ZERO", "FLOATLIT", "BCOMMENT", "STRINGLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "INT", 
                      "IN", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                      "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "STR", "RELOP", "NOTOP", "ANDOP", 
                      "OROP", "ADDOP", "MINOP", "MULOP", "DIVOP", "REMOP", 
                      "ASSOP", "LB", "RB", "LP", "RP", "LC", "RC", "DCOLON", 
                      "COLON", "COMMA", "SEMI", "DDOT", "DOT", "DOLLARID", 
                      "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_bclasses = 1
    RULE_bclass = 2
    RULE_class_body = 3
    RULE_class_stmt_list = 4
    RULE_class_stmt = 5
    RULE_funcdecl = 6
    RULE_id_vas = 7
    RULE_id_va = 8
    RULE_valdecl = 9
    RULE_vardecl = 10
    RULE_constructor = 11
    RULE_destructor = 12
    RULE_datatype = 13
    RULE_dttype = 14
    RULE_dttyp = 15
    RULE_param = 16
    RULE_paramlist = 17
    RULE_bidlist = 18
    RULE_idlist = 19
    RULE_lit = 20
    RULE_valuelist = 21
    RULE_blockstmt = 22
    RULE_stmtlist = 23
    RULE_stmt = 24
    RULE_semi_stmt = 25
    RULE_bid_vas = 26
    RULE_bid_va = 27
    RULE_bvaldecl = 28
    RULE_bvardecl = 29
    RULE_scalar = 30
    RULE_index_scalar = 31
    RULE_index_operators = 32
    RULE_varass = 33
    RULE_func = 34
    RULE_dollarfunc = 35
    RULE_funccall = 36
    RULE_returnal = 37
    RULE_cont = 38
    RULE_brk = 39
    RULE_forstmt = 40
    RULE_ifstmt = 41
    RULE_ifpart = 42
    RULE_elseif_part = 43
    RULE_expr = 44
    RULE_term1 = 45
    RULE_term2 = 46
    RULE_term3 = 47
    RULE_term4 = 48
    RULE_term5 = 49
    RULE_term6 = 50
    RULE_term7 = 51
    RULE_term8 = 52
    RULE_term9 = 53
    RULE_term10 = 54
    RULE_sd = 55
    RULE_array = 56

    ruleNames =  [ "program", "bclasses", "bclass", "class_body", "class_stmt_list", 
                   "class_stmt", "funcdecl", "id_vas", "id_va", "valdecl", 
                   "vardecl", "constructor", "destructor", "datatype", "dttype", 
                   "dttyp", "param", "paramlist", "bidlist", "idlist", "lit", 
                   "valuelist", "blockstmt", "stmtlist", "stmt", "semi_stmt", 
                   "bid_vas", "bid_va", "bvaldecl", "bvardecl", "scalar", 
                   "index_scalar", "index_operators", "varass", "func", 
                   "dollarfunc", "funccall", "returnal", "cont", "brk", 
                   "forstmt", "ifstmt", "ifpart", "elseif_part", "expr", 
                   "term1", "term2", "term3", "term4", "term5", "term6", 
                   "term7", "term8", "term9", "term10", "sd", "array" ]

    EOF = Token.EOF
    INTLIT=1
    BIN=2
    OCT=3
    DEC=4
    HEX=5
    ZERO=6
    FLOATLIT=7
    BCOMMENT=8
    STRINGLIT=9
    UNCLOSE_STRING=10
    ILLEGAL_ESCAPE=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSEIF=15
    ELSE=16
    FOREACH=17
    TRUE=18
    FALSE=19
    ARRAY=20
    INT=21
    IN=22
    FLOAT=23
    BOOLEAN=24
    STRING=25
    RETURN=26
    NULL=27
    CLASS=28
    VAL=29
    VAR=30
    CONSTRUCTOR=31
    DESTRUCTOR=32
    NEW=33
    BY=34
    SELF=35
    STR=36
    RELOP=37
    NOTOP=38
    ANDOP=39
    OROP=40
    ADDOP=41
    MINOP=42
    MULOP=43
    DIVOP=44
    REMOP=45
    ASSOP=46
    LB=47
    RB=48
    LP=49
    RP=50
    LC=51
    RC=52
    DCOLON=53
    COLON=54
    COMMA=55
    SEMI=56
    DDOT=57
    DOT=58
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

        def bclasses(self):
            return self.getTypedRuleContext(D96Parser.BclassesContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.bclasses()
            self.state = 115
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BclassesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bclass(self):
            return self.getTypedRuleContext(D96Parser.BclassContext,0)


        def bclasses(self):
            return self.getTypedRuleContext(D96Parser.BclassesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_bclasses

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBclasses" ):
                return visitor.visitBclasses(self)
            else:
                return visitor.visitChildren(self)




    def bclasses(self):

        localctx = D96Parser.BclassesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bclasses)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.bclass()
                self.state = 118
                self.bclasses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.bclass()
                pass


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

        def class_body(self):
            return self.getTypedRuleContext(D96Parser.Class_bodyContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_bclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBclass" ):
                return visitor.visitBclass(self)
            else:
                return visitor.visitChildren(self)




    def bclass(self):

        localctx = D96Parser.BclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bclass)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(D96Parser.CLASS)
            self.state = 124
            self.match(D96Parser.ID)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 125
                self.match(D96Parser.COLON)
                self.state = 126
                self.match(D96Parser.ID)


            self.state = 129
            self.class_body()
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

        def class_stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Class_stmt_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = D96Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_body)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(D96Parser.LP)
                self.state = 132
                self.class_stmt_list()
                self.state = 133
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(D96Parser.LP)
                self.state = 136
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_stmt(self):
            return self.getTypedRuleContext(D96Parser.Class_stmtContext,0)


        def class_stmt_list(self):
            return self.getTypedRuleContext(D96Parser.Class_stmt_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_stmt_list" ):
                return visitor.visitClass_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def class_stmt_list(self):

        localctx = D96Parser.Class_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_class_stmt_list)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.class_stmt()
                self.state = 140
                self.class_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.class_stmt()
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


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def valdecl(self):
            return self.getTypedRuleContext(D96Parser.ValdeclContext,0)


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
        self.enterRule(localctx, 10, self.RULE_class_stmt)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.destructor()
                pass
            elif token in [D96Parser.DOLLARID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.funcdecl()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL]:
                    self.state = 148
                    self.valdecl()
                    pass
                elif token in [D96Parser.VAR]:
                    self.state = 149
                    self.vardecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 152
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


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLARID(self):
            return self.getToken(D96Parser.DOLLARID, 0)

        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = D96Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 157
            self.match(D96Parser.LB)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 158
                self.paramlist()


            self.state = 161
            self.match(D96Parser.RB)
            self.state = 162
            self.blockstmt()
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
        self.enterRule(localctx, 14, self.RULE_id_vas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 165
            self.id_va()

            self.state = 166
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
        self.enterRule(localctx, 16, self.RULE_id_va)
        self._la = 0 # Token type
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(D96Parser.COMMA)
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 170
                self.id_va()

                self.state = 171
                self.expr()
                self.state = 172
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(D96Parser.COLON)
                self.state = 175
                self.dttyp()
                self.state = 176
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
        self.enterRule(localctx, 18, self.RULE_valdecl)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(D96Parser.VAL)
                self.state = 181
                self.idlist()
                self.state = 182
                self.match(D96Parser.COLON)
                self.state = 183
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(D96Parser.VAL)
                self.state = 186
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
        self.enterRule(localctx, 20, self.RULE_vardecl)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(D96Parser.VAR)
                self.state = 190
                self.idlist()
                self.state = 191
                self.match(D96Parser.COLON)
                self.state = 192
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(D96Parser.VAR)
                self.state = 195
                self.id_vas()
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(D96Parser.ParamlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 199
            self.match(D96Parser.LB)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 200
                self.paramlist()


            self.state = 203
            self.match(D96Parser.RB)
            self.state = 204
            self.blockstmt()
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
        self.enterRule(localctx, 24, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(D96Parser.DESTRUCTOR)
            self.state = 207
            self.match(D96Parser.LB)
            self.state = 208
            self.match(D96Parser.RB)
            self.state = 209
            self.blockstmt()
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
        self.enterRule(localctx, 26, self.RULE_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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
        self.enterRule(localctx, 28, self.RULE_dttype)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(D96Parser.ARRAY)
                self.state = 214
                self.match(D96Parser.LC)
                self.state = 215
                self.dttype()
                self.state = 216
                self.match(D96Parser.COMMA)
                self.state = 217
                self.match(D96Parser.INTLIT)
                self.state = 218
                self.match(D96Parser.RC)
                pass
            elif token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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
        self.enterRule(localctx, 30, self.RULE_dttyp)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY, D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.dttype()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
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
        self.enterRule(localctx, 32, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.bidlist()
            self.state = 228
            self.match(D96Parser.COLON)
            self.state = 229
            self.dttyp()
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
        self.enterRule(localctx, 34, self.RULE_paramlist)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.param()
                self.state = 232
                self.match(D96Parser.SEMI)
                self.state = 233
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.param()
                pass


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
        self.enterRule(localctx, 36, self.RULE_bidlist)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(D96Parser.ID)
                self.state = 239
                self.match(D96Parser.COMMA)
                self.state = 240
                self.bidlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
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
        self.enterRule(localctx, 38, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOLLARID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self.match(D96Parser.COMMA)
                self.state = 246
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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


    class LitContext(ParserRuleContext):
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

        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = D96Parser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lit)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(D96Parser.TRUE)
                pass
            elif token in [D96Parser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(D96Parser.FALSE)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ZERO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.match(D96Parser.ZERO)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 8)
                self.state = 257
                self.array()
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
        self.enterRule(localctx, 42, self.RULE_valuelist)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.expr()
                self.state = 261
                self.match(D96Parser.COMMA)
                self.state = 262
                self.valuelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
        self.enterRule(localctx, 44, self.RULE_blockstmt)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(D96Parser.LP)
                self.state = 268
                self.stmtlist()
                self.state = 269
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(D96Parser.LP)
                self.state = 272
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
        self.enterRule(localctx, 46, self.RULE_stmtlist)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.stmt()
                self.state = 276
                self.stmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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


        def forstmt(self):
            return self.getTypedRuleContext(D96Parser.ForstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(D96Parser.IfstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(D96Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.NOTOP, D96Parser.MINOP, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.semi_stmt()
                pass
            elif token in [D96Parser.FOREACH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.forstmt()
                pass
            elif token in [D96Parser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.ifstmt()
                pass
            elif token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.blockstmt()
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


        def returnal(self):
            return self.getTypedRuleContext(D96Parser.ReturnalContext,0)


        def funccall(self):
            return self.getTypedRuleContext(D96Parser.FunccallContext,0)


        def brk(self):
            return self.getTypedRuleContext(D96Parser.BrkContext,0)


        def cont(self):
            return self.getTypedRuleContext(D96Parser.ContContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_semi_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemi_stmt" ):
                return visitor.visitSemi_stmt(self)
            else:
                return visitor.visitChildren(self)




    def semi_stmt(self):

        localctx = D96Parser.Semi_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_semi_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 287
                self.bvaldecl()
                pass

            elif la_ == 2:
                self.state = 288
                self.bvardecl()
                pass

            elif la_ == 3:
                self.state = 289
                self.varass()
                pass

            elif la_ == 4:
                self.state = 290
                self.returnal()
                pass

            elif la_ == 5:
                self.state = 291
                self.funccall()
                pass

            elif la_ == 6:
                self.state = 292
                self.brk()
                pass

            elif la_ == 7:
                self.state = 293
                self.cont()
                pass


            self.state = 296
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
        self.enterRule(localctx, 52, self.RULE_bid_vas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(D96Parser.ID)
            self.state = 299
            self.bid_va()
            self.state = 300
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
        self.enterRule(localctx, 54, self.RULE_bid_va)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(D96Parser.COMMA)
                self.state = 303
                self.match(D96Parser.ID)
                self.state = 304
                self.bid_va()
                self.state = 305
                self.expr()
                self.state = 306
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(D96Parser.COLON)
                self.state = 309
                self.dttyp()
                self.state = 310
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
        self.enterRule(localctx, 56, self.RULE_bvaldecl)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(D96Parser.VAL)
                self.state = 315
                self.bidlist()
                self.state = 316
                self.match(D96Parser.COLON)
                self.state = 317
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(D96Parser.VAL)
                self.state = 320
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
        self.enterRule(localctx, 58, self.RULE_bvardecl)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(D96Parser.VAR)
                self.state = 324
                self.bidlist()
                self.state = 325
                self.match(D96Parser.COLON)
                self.state = 326
                self.dttyp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.match(D96Parser.VAR)
                self.state = 329
                self.bid_vas()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):
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

        def sd(self):
            return self.getTypedRuleContext(D96Parser.SdContext,0)


        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)



    def scalar(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ScalarContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_scalar, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 333
                self.match(D96Parser.ID)
                self.state = 334
                self.match(D96Parser.DCOLON)
                self.state = 335
                self.match(D96Parser.DOLLARID)
                pass

            elif la_ == 2:
                self.state = 336
                self.sd()
                self.state = 337
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 339
                self.match(D96Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ScalarContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_scalar)
                    self.state = 342
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 343
                    self.match(D96Parser.DOT)
                    self.state = 344
                    self.match(D96Parser.ID) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_scalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_scalar" ):
                return visitor.visitIndex_scalar(self)
            else:
                return visitor.visitChildren(self)




    def index_scalar(self):

        localctx = D96Parser.Index_scalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_index_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.scalar(0)
            self.state = 351
            self.index_operators()
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
        self.enterRule(localctx, 64, self.RULE_index_operators)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(D96Parser.LC)
                self.state = 354
                self.expr()
                self.state = 355
                self.match(D96Parser.RC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(D96Parser.LC)
                self.state = 358
                self.expr()
                self.state = 359
                self.match(D96Parser.RC)
                self.state = 360
                self.index_operators()
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

        def scalar(self):
            return self.getTypedRuleContext(D96Parser.ScalarContext,0)


        def ASSOP(self):
            return self.getToken(D96Parser.ASSOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def index_scalar(self):
            return self.getTypedRuleContext(D96Parser.Index_scalarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarass" ):
                return visitor.visitVarass(self)
            else:
                return visitor.visitChildren(self)




    def varass(self):

        localctx = D96Parser.VarassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_varass)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.scalar(0)
                self.state = 365
                self.match(D96Parser.ASSOP)
                self.state = 366
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.index_scalar()
                self.state = 369
                self.match(D96Parser.ASSOP)
                self.state = 370
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def valuelist(self):
            return self.getTypedRuleContext(D96Parser.ValuelistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = D96Parser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(D96Parser.ID)
            self.state = 375
            self.match(D96Parser.LB)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.NOTOP) | (1 << D96Parser.MINOP) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 376
                self.valuelist()


            self.state = 379
            self.match(D96Parser.RB)
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def valuelist(self):
            return self.getTypedRuleContext(D96Parser.ValuelistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_dollarfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDollarfunc" ):
                return visitor.visitDollarfunc(self)
            else:
                return visitor.visitChildren(self)




    def dollarfunc(self):

        localctx = D96Parser.DollarfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_dollarfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(D96Parser.DOLLARID)
            self.state = 382
            self.match(D96Parser.LB)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.NOTOP) | (1 << D96Parser.MINOP) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 383
                self.valuelist()


            self.state = 386
            self.match(D96Parser.RB)
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


        def sd(self):
            return self.getTypedRuleContext(D96Parser.SdContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = D96Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_funccall)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.expr()
                self.state = 389
                self.match(D96Parser.DOT)
                self.state = 390
                self.func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.match(D96Parser.ID)
                self.state = 393
                self.match(D96Parser.DCOLON)
                self.state = 394
                self.dollarfunc()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.sd()
                self.state = 396
                self.func()
                pass


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

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_returnal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnal" ):
                return visitor.visitReturnal(self)
            else:
                return visitor.visitChildren(self)




    def returnal(self):

        localctx = D96Parser.ReturnalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_returnal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(D96Parser.RETURN)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.NOTOP) | (1 << D96Parser.MINOP) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 401
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_cont

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont" ):
                return visitor.visitCont(self)
            else:
                return visitor.visitChildren(self)




    def cont(self):

        localctx = D96Parser.ContContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_cont)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(D96Parser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BrkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_brk

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrk" ):
                return visitor.visitBrk(self)
            else:
                return visitor.visitChildren(self)




    def brk(self):

        localctx = D96Parser.BrkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_brk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(D96Parser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
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
            return D96Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = D96Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(D96Parser.FOREACH)
            self.state = 409
            self.match(D96Parser.LB)
            self.state = 410
            self.match(D96Parser.ID)
            self.state = 411
            self.match(D96Parser.IN)
            self.state = 412
            self.expr()
            self.state = 413
            self.match(D96Parser.DDOT)
            self.state = 414
            self.expr()
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 415
                self.match(D96Parser.BY)
                self.state = 416
                self.expr()


            self.state = 419
            self.match(D96Parser.RB)
            self.state = 420
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
        self.enterRule(localctx, 82, self.RULE_ifstmt)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.ifpart()
                self.state = 423
                self.elseif_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
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
        self.enterRule(localctx, 84, self.RULE_ifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.IF)
            self.state = 429
            self.match(D96Parser.LB)
            self.state = 430
            self.expr()
            self.state = 431
            self.match(D96Parser.RB)
            self.state = 432
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
        self.enterRule(localctx, 86, self.RULE_elseif_part)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(D96Parser.ELSEIF)
                self.state = 435
                self.match(D96Parser.LB)
                self.state = 436
                self.expr()
                self.state = 437
                self.match(D96Parser.RB)
                self.state = 438
                self.blockstmt()
                self.state = 439
                self.elseif_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(D96Parser.ELSEIF)
                self.state = 442
                self.match(D96Parser.LB)
                self.state = 443
                self.expr()
                self.state = 444
                self.match(D96Parser.RB)
                self.state = 445
                self.blockstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 447
                self.match(D96Parser.ELSE)
                self.state = 448
                self.blockstmt()
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
        self.enterRule(localctx, 88, self.RULE_expr)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.term1()
                self.state = 452
                self.match(D96Parser.STR)
                self.state = 453
                self.term1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
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
        self.enterRule(localctx, 90, self.RULE_term1)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.term2(0)
                self.state = 459
                self.match(D96Parser.RELOP)
                self.state = 460
                self.term2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_term2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 476
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 474
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Term2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                        self.state = 468
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 469
                        self.match(D96Parser.OROP)
                        self.state = 470
                        self.term3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Term2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                        self.state = 471
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 472
                        self.match(D96Parser.ANDOP)
                        self.state = 473
                        self.term3(0)
                        pass

             
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_term3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.term4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 488
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Term3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                        self.state = 482
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 483
                        self.match(D96Parser.ADDOP)
                        self.state = 484
                        self.term4(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Term3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                        self.state = 485
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 486
                        self.match(D96Parser.MINOP)
                        self.state = 487
                        self.term4(0)
                        pass

             
                self.state = 492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_term4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.term5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 505
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Term4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                        self.state = 496
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 497
                        self.match(D96Parser.MULOP)
                        self.state = 498
                        self.term5()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Term4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                        self.state = 499
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 500
                        self.match(D96Parser.DIVOP)
                        self.state = 501
                        self.term5()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Term4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                        self.state = 502
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 503
                        self.match(D96Parser.REMOP)
                        self.state = 504
                        self.term5()
                        pass

             
                self.state = 509
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 98, self.RULE_term5)
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.match(D96Parser.NOTOP)
                self.state = 511
                self.term5()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.MINOP, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
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
        self.enterRule(localctx, 100, self.RULE_term6)
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.match(D96Parser.MINOP)
                self.state = 516
                self.term6()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
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
        self.enterRule(localctx, 102, self.RULE_term7)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.term8(0)
                self.state = 521
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.term8(0)
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

        def sd(self):
            return self.getTypedRuleContext(D96Parser.SdContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(D96Parser.FuncContext,0)


        def term9(self):
            return self.getTypedRuleContext(D96Parser.Term9Context,0)


        def term8(self):
            return self.getTypedRuleContext(D96Parser.Term8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_term8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SELF]:
                self.state = 527
                self.sd()
                self.state = 530
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 528
                    self.match(D96Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 529
                    self.func()
                    pass


                pass
            elif token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.LB, D96Parser.ID]:
                self.state = 532
                self.term9()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 543
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Term8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term8)
                    self.state = 535
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 536
                    self.match(D96Parser.DOT)
                    self.state = 539
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 537
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 538
                        self.func()
                        pass

             
                self.state = 545
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 106, self.RULE_term9)
        try:
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.match(D96Parser.ID)
                self.state = 547
                self.match(D96Parser.DCOLON)
                self.state = 550
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                if la_ == 1:
                    self.state = 548
                    self.match(D96Parser.DOLLARID)
                    pass

                elif la_ == 2:
                    self.state = 549
                    self.dollarfunc()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
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


        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_term10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm10" ):
                return visitor.visitTerm10(self)
            else:
                return visitor.visitChildren(self)




    def term10(self):

        localctx = D96Parser.Term10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_term10)
        self._la = 0 # Token type
        try:
            self.state = 568
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.match(D96Parser.NEW)
                self.state = 556
                self.match(D96Parser.ID)
                self.state = 557
                self.match(D96Parser.LB)
                self.state = 559
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.NOTOP) | (1 << D96Parser.MINOP) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                    self.state = 558
                    self.valuelist()


                self.state = 561
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 563
                self.match(D96Parser.LB)
                self.state = 564
                self.expr()
                self.state = 565
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INTLIT, D96Parser.ZERO, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 567
                self.lit()
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


    class SdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_sd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSd" ):
                return visitor.visitSd(self)
            else:
                return visitor.visitChildren(self)




    def sd(self):

        localctx = D96Parser.SdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_sd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(D96Parser.SELF)
            self.state = 571
            self.match(D96Parser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
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
            return D96Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_array)
        try:
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 573
                self.match(D96Parser.ARRAY)
                self.state = 574
                self.match(D96Parser.LB)
                self.state = 575
                self.valuelist()
                self.state = 576
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
                self.match(D96Parser.ARRAY)
                self.state = 579
                self.match(D96Parser.LB)
                self.state = 580
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
        self._predicates[30] = self.scalar_sempred
        self._predicates[46] = self.term2_sempred
        self._predicates[47] = self.term3_sempred
        self._predicates[48] = self.term4_sempred
        self._predicates[52] = self.term8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def scalar_sempred(self, localctx:ScalarContext, predIndex:int):
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
                return self.precpred(self._ctx, 3)
         




