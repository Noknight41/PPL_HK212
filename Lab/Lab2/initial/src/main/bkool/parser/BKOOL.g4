grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls EOF;
decls: decl decls | decl;
decl: vardecl | funcdecl;
DATATYPE: 'int' | 'float';

idlist: ID COMMA idlist | ID;
vardecl: DATATYPE idlist SEMI;

instance: ID | expr;
instlist: instance COMMA instlist | instance;

varass: ID ASS instance SEMI;
funccall: ID LB instlist RB SEMI;
returnal: 'return' instance SEMI;

paramlist: param SEMI paramlist | param;
param: DATATYPE idlist;
funcdecl: DATATYPE ID LB paramlist? RB LP body RP;

COMMA: ',';
SEMI: ';';
ASS: '=';
LB: '(';
RB: ')';
LP: '{';
RP: '}';

body: stmt body | stmt;
stmt: vardecl | varass | funccall | returnal;
expr: 'expr';
ID: [a-zA-Z]+;
WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};


