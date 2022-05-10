grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// Program Structure
program: bclass+ EOF;
bclass: CLASS ID COLON ID class_body | CLASS ID class_body;

// Class Body
class_body: LP class_stmt+ RP | LP RP;
class_stmt: constructor | destructor | funcdecl | valdecl SEMI | vardecl SEMI;

// Id and $Id in Variable/Const Decl
id_vas: (ID | DOLLARID) id_va (expr);
id_va: COMMA (ID | DOLLARID) id_va (expr) COMMA | COLON dttyp ASSOP;

// Attribute declaration
valdecl: VAL idlist COLON dttyp | VAL id_vas;
vardecl: VAR idlist COLON dttyp | VAR id_vas;

// Statement in Class Body
funcdecl: (ID | DOLLARID) LB paramlist RB blockstmt | (ID | DOLLARID) LB RB blockstmt;
constructor: CONSTRUCTOR LB paramlist RB blockstmt | CONSTRUCTOR LB RB blockstmt;
destructor: DESTRUCTOR LB RB blockstmt;

// List of ultility
param: bidlist COLON dttyp;
paramlist: param SEMI paramlist | param;
bidlist: ID COMMA bidlist | ID;
idlist: (ID | DOLLARID) COMMA idlist | (ID | DOLLARID);
valuelist: expr COMMA valuelist | expr;

// Blockstmt = Method body
blockstmt: (LP stmtlist RP) | (LP RP);
stmtlist: stmt stmtlist | stmt;
stmt: semi_stmt | blockstmt | foreachstmt | ifstmt;
semi_stmt: (bvaldecl | bvardecl | varass | funccall | rcb) SEMI ;

// Statement in Block Statement
// Id in Variable/Const Decl
block_id_vas: ID block_id_va expr;
block_id_va: COMMA ID block_id_va expr COMMA | COLON dttyp ASSOP;

// Variable/Const Decl
bvaldecl: VAL bidlist COLON dttyp | VAL block_id_vas;
bvardecl: VAR bidlist COLON dttyp | VAR block_id_vas;

// LHS
lhs: term8 DOT ID | ID DCOLON DOLLARID | LB lhs RB | ID;
index_lhs: lhs index_operators | LB index_lhs RB index_operators;

// Variable assignment
varass: lhs ASSOP expr | index_lhs ASSOP expr;

// Function call
func: ID LB valuelist RB | ID LB RB;
dollarfunc: DOLLARID LB valuelist RB | DOLLARID LB RB;
funccall: expr DOT func | ID DCOLON dollarfunc;

// Foreach statement
foreachstmt: FOREACH LB ID IN expr DDOT expr RB blockstmt
            | FOREACH LB ID IN expr DDOT expr BY expr RB blockstmt;

// If Elseif Else statement
ifstmt: ifpart elseif_part | ifpart;
ifpart: IF LB expr RB blockstmt;
elseif_part: ELSEIF LB expr RB blockstmt elseif_part | ELSEIF LB expr RB blockstmt | ELSE blockstmt;

// Other Statement: Return + Continue + Break
rcb: RETURN expr | RETURN | BREAK | CONTINUE;

// Data type in D96
datatype: INT | FLOAT | BOOLEAN | STRING;
dttype: (ARRAY LC dttype COMMA INTLIT RC) | datatype;
dttyp: dttype | ID;

// Expression
expr: term1 STR term1 | term1;
term1: term2 RELOP term2 | term2 ;
term2: term2 OROP term3  | term2 ANDOP term3 | term3 ;
term3: term3 ADDOP term4 | term3 MINOP term4 | term4;
term4: term4 MULOP term5 | term4 DIVOP term5 | term4 REMOP term5 | term5;
term5: NOTOP term5 | term6;
term6: MINOP term6 | term7;
term7: term8 index_operators | term8;
index_operators: LC expr RC | LC expr RC index_operators;
term8: term8 DOT (ID | func) | term9 ;
term9: ID DCOLON (DOLLARID | dollarfunc) | term10;
term10: (NEW ID LB valuelist? RB) | ID | (LB expr RB) | literal | SELF;

// Standalone Expr
literal: TRUE | FALSE | INTLIT | ZERO | FLOATLIT | STRINGLIT | NULL | arrayCell;
arrayCell: (ARRAY LB valuelist RB ) | (ARRAY LB RB);

// LEXICAL
// INT
fragment DC: 	[1-9] ([0-9] | '_' [0-9])*;
INTLIT: (BIN | OCT | DEC | HEX){
            trim_result = self.text
            self.text = trim_result.replace('_', '')
        };
BIN: 	'0'[bB] '1' ([0-1] | '_' [0-1]+)*;
OCT: 	'0'[1-7]([0-7] | '_' [0-7]+)* ;
DEC: 	DC;
HEX: 	'0' [xX] [1-9A-F] ([0-9A-F] | '_' [0-9A-F]+)*;
ZERO:   '0' | '0'[bB]'0' | '0'[xX]'0' | '00';

// FLOAT
FLOATLIT: ((DC | '0') '.' ([0-9])*
		| (DC | '0') '.' ([0-9])* [eE] [+-]? [0-9]+
		| (DC | '0') [eE] [+-]? [0-9]+ 
        | '.' ([0-9])* [eE] [+-]? [0-9]+) {
            trim_result = self.text
            self.text = trim_result.replace('_', '')
        };

// STRING
fragment QQ: '\'''"';
fragment LEGAL_CHAR: ~[\b\r\n\t\f\\'"] | LEGAL_ESC;
fragment S: '\'' ~'"';
fragment LEGAL_ESC: S | '\\' [brntf'\\];
fragment ILLEGAL_ESC: '\\' ~[brntf'\\];
STRINGLIT: '"' (LEGAL_CHAR | QQ)* '"' {self.text = self.text[1:-1]};
UNCLOSE_STRING: ('"' (LEGAL_CHAR | QQ)*) {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' (LEGAL_CHAR | QQ)* ILLEGAL_ESC  {
    raise IllegalEscape(self.text[1:])
};



// Comment
BCOMMENT: '##' .*? '##' -> skip;

// OPERATOR
STR: '==.' | '+.';
RELOP: '==' | '!=' | '>=' | '<=' | '>' | '<';
NOTOP: '!';
ANDOP: '&&';
OROP:  '||';
ASSOP: '=';
ADDOP: '+';
MINOP: '-';
MULOP: '*';
DIVOP: '/';
REMOP: '%';

// Variable Keyword
ARRAY: 'Array';
INT: 'Int';
FLOAT: 'Float';
TRUE: 'True';
FALSE: 'False';
BOOLEAN: 'Boolean';
STRING: 'String';
NULL: 'Null';

// Keyword
CLASS: 'Class';
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
RETURN: 'Return';
SELF: 'Self';
NEW: 'New';
IN: 'In';
BY: 'By';

// Special Operator
DCOLON: '::';
COLON: ':';
COMMA: ',';
SEMI: ';';
DDOT: '..';
DOT: '.';

// Bracket
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LC: '[';
RC: ']';

// Identifier (SI)
DOLLARID: '$' ([a-z] | [A-Z] | '_' | [0-9])+; 
ID: ([a-z] | [A-Z] | '_')([a-z] | [A-Z] | '_' | [0-9])*;
WS: [ \b\f\t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment NONCOMMENT: '#'~[#];
ERROR_CHAR: . {raise ErrorToken(self.text)};
