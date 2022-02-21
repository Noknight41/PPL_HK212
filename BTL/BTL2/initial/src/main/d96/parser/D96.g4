grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// Program General Structure
program: bclasses EOF;
bclasses: bclass bclasses | bclass;
bclass: (CLASS ID (COLON ID)?  class_body );

// Class Body
class_body: LP class_stmt_list RP | LP RP;
class_stmt_list: class_stmt class_stmt_list | class_stmt ;
class_stmt: constructor | destructor | funcdecl | ((valdecl | vardecl) SEMI);

// Statement in Class Body
funcdecl: (ID | DOLLARID) LB paramlist RB blockstmt | (ID | DOLLARID) LB RB blockstmt;

id_vas: (ID | DOLLARID) id_va (expr);
id_va: COMMA (ID | DOLLARID) id_va (expr) COMMA | COLON dttyp ASSOP;

valdecl: VAL idlist COLON dttyp | VAL id_vas;
vardecl: VAR idlist COLON dttyp | VAR id_vas;

constructor: CONSTRUCTOR LB paramlist RB blockstmt | CONSTRUCTOR LB RB blockstmt;
destructor: DESTRUCTOR LB RB blockstmt;

// Data type
datatype: INT | FLOAT | BOOLEAN | STRING;
dttype: (ARRAY LC dttype COMMA INTLIT RC) | datatype;
dttyp: dttype | ID;

param: bidlist COLON dttyp;
paramlist: param SEMI paramlist | param;

// List of ID
bidlist: ID COMMA bidlist | ID;
idlist: (ID | DOLLARID) COMMA idlist | (ID | DOLLARID);

lit: TRUE | FALSE | FLOATLIT | INTLIT | STRINGLIT | ZERO | NULL | array;
valuelist: expr COMMA valuelist | expr;

// Blockstmt = Method body
blockstmt: LP stmtlist RP | LP RP;
stmtlist: stmt stmtlist | stmt;
stmt: semi_stmt | forstmt | ifstmt | blockstmt;
semi_stmt: (bvaldecl | bvardecl | varass | returnal | funccall | brk | cont) SEMI ;

// Statement in Block Statement
// Attribute declaration
bid_vas: ID bid_va expr;
bid_va: COMMA ID bid_va expr COMMA | COLON dttyp ASSOP;
bvaldecl: VAL bidlist COLON dttyp | VAL bid_vas;
bvardecl: VAR bidlist COLON dttyp | VAR bid_vas;

// LHS + Variable assignment
scalar: scalar DOT ID | ID DCOLON DOLLARID | SELF DOT ID | ID;
index_scalar: scalar index_operators;
index_operators: LC expr RC | LC expr RC index_operators;
varass: scalar ASSOP expr | index_scalar ASSOP expr;

// Function call
func: ID LB valuelist? RB;
dollarfunc: DOLLARID LB valuelist? RB;
funccall: expr DOT func | ID DCOLON dollarfunc;

// Other Statement: Return + Continue + Break
returnal: RETURN expr?;
cont: CONTINUE;
brk: BREAK;

// Foreach statement
forstmt: FOREACH LB ID IN expr DDOT expr (BY expr)? RB blockstmt;

// If Elseif Else statement
ifstmt: ifpart elseif_part | ifpart;
ifpart: IF LB expr RB blockstmt;
elseif_part: ELSEIF LB expr RB blockstmt elseif_part | ELSEIF LB expr RB blockstmt | ELSE blockstmt;

// Expression Precedence and Associativity
expr: term1 STR term1 | term1;
term1: term2 RELOP term2 | term2 ;
term2: term2 OROP term3  | term2 ANDOP term3 | term3 ;
term3: term3 ADDOP term4 | term3 MINOP term4 | term4;
term4: term4 MULOP term5 | term4 DIVOP term5 | term4 REMOP term5 | term5;
term5: NOTOP term5 | term6;
term6: MINOP term6 | term7;
term7: term8 index_operators | term8;
term8: term8 DOT (ID | func) | term9 ;
term9: ID DCOLON (DOLLARID | dollarfunc) | term10;
term10: (NEW ID LB valuelist? RB) | ID | (LB expr RB) | lit | SELF;

// ARRAY
array: (ARRAY LB valuelist RB ) | (ARRAY LB RB);

//Literal
// INT
fragment DF2: 	[1-9] ([0-9] | '_' [0-9])*;
INTLIT: (BIN | OCT | DEC | HEX){
            trim_result = self.text
            self.text = trim_result.replace('_', '')
        };
BIN: 	'0'[bB] '1' ([0-1] | '_' [0-1]+)*;
OCT: 	'0'[1-7]([0-7] | '_' [0-7]+)* ;
DEC: 	DF2;
HEX: 	'0' [xX] [1-9A-F] ([0-9A-F] | '_' [0-9A-F]+)*;
ZERO:   '0' | '0'[bB]'0' | '0'[xX]'0' | '00';

// FLOAT
FLOATLIT: ((DF2 | '0') '.' ([0-9])*
		| (DF2 | '0') '.' ([0-9])* [eE] [+-]? [0-9]+
		| (DF2 | '0') [eE] [+-]? [0-9]+ 
        | '.' ([0-9])* [eE] [+-]? [0-9]+) {
            trim_result = self.text
            self.text = trim_result.replace('_', '')
        };

// BOOLEAN
BCOMMENT: '##' .*? '##' -> skip;

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



// Keyword
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
INT: 'Int';
IN: 'In';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
SELF: 'Self';

// STRING OPS
STR: '==.' | '+.';

// BOOLEAN OPS
RELOP: '==' | '!=' | '>=' | '<=' | '>' | '<';
NOTOP: '!';
ANDOP: '&&';
OROP:  '||';

// MATH OPS
ADDOP: '+';
MINOP: '-';
MULOP: '*';
DIVOP: '/';
REMOP: '%';
ASSOP: '=';

// Special Operator
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LC: '[';
RC: ']';
DCOLON: '::';
COLON: ':';
COMMA: ',';
SEMI: ';';
DDOT: '..';
DOT: '.';

// Identifier
DOLLARID: '$' ([a-z] | [A-Z] | '_' | [0-9])+; 
ID: ([a-z] | [A-Z] | '_')([a-z] | [A-Z] | '_' | [0-9])*;
WS: [ \b\f\t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment NONCOMMENT: '#'~[#];
ERROR_CHAR: . {raise ErrorToken(self.text)};
