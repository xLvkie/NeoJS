grammar NeoJS;

// ==========================================
// 1. REGLAS SINTÁCTICAS (PARSER)
// ==========================================

program : declaration* EOF ;

declaration
    : itemDecl
    | weaponDecl
    | recipeDecl
    | mobDecl
    | modifyDecl
    ;

itemDecl   : TK_ITEM ID LBRACE attrList RBRACE ;
weaponDecl : TK_WEAPON ID LBRACE attrList RBRACE ;
recipeDecl : TK_RECIPE ID LBRACE attrList RBRACE ;
mobDecl    : TK_MOB ID LBRACE attrList RBRACE ;
modifyDecl : TK_MODIFY (TK_ITEM | TK_MOB) ID LBRACE attrList RBRACE ;

attrList   : (attr SEMI)+ ;
attr       : ID COLON value ;

value
    : NUMBER
    | STRING
    | PERCENTAGE
    | TRUE
    | FALSE
    | ID
    ;

// ==========================================
// 2. REGLAS LÉXICAS (LEXER)
// ==========================================

TK_ITEM   : 'item' ;
TK_WEAPON : 'weapon' ;
TK_RECIPE : 'recipe' ;
TK_MOB    : 'mob' ;
TK_MODIFY : 'modify' ;
TRUE      : 'true' ;
FALSE     : 'false' ;

LBRACE : '{' ;
RBRACE : '}' ;
SEMI   : ';' ;
COLON  : ':' ;

PERCENTAGE : [0-9]+ ('.' [0-9]+)? '%' ;
NUMBER     : '-'? [0-9]+ ('.' [0-9]+)? ;
STRING     : '"' ~["\r\n]* '"' ;
ID         : [a-zA-Z_] [a-zA-Z_0-9]* (':' [a-zA-Z_] [a-zA-Z_0-9]*)* ;

COMMENT : '//' ~[\r\n]* -> skip ;
WS      : [ \t\r\n]+ -> skip ;