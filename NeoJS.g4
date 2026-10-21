grammar NeoJS;

// ==========================================
// 1. REGLAS SINTÁCTICAS (PARSER)
// ==========================================

program : declaration* EOF ;

declaration
    : itemDecl
    | bossDecl
    | lootDecl
    | modifyDecl
    ;

// Bloques principales de creación
itemDecl   : TK_ITEM ID LBRACE attrList RBRACE ;

bossDecl   : TK_BOSS ID LBRACE attrList RBRACE
           | TK_PHASE ID LBRACE attrList RBRACE ;

lootDecl   : TK_LOOT ID LBRACE dropList RBRACE ;

// Bloque de modificación existente
modifyDecl : TK_MODIFY TK_ITEM ID LBRACE attrList RBRACE ;

// Reglas para tablas de botín (Loot)
dropList   : dropDecl+ ;
dropDecl   : TK_DROP ID LBRACE attrList RBRACE ;

// Lista de atributos (Punto y coma obligatorio al final de cada atributo)
attrList   : (attr SEMI)+ ;

attr       : ID COLON value
           | TK_CONDITION COLON condition ;

value
    : NUMBER
    | STRING
    | PERCENTAGE
    | TIME_LITERAL
    | TRUE
    | FALSE
    | ID
    ;

condition  : ID OP_REL value ;

// ==========================================
// 2. REGLAS LÉXICAS (LEXER)
// ==========================================

// PALABRAS CLAVE (Prioridad alta antes que ID)
TK_ITEM      : 'item' ;
TK_BOSS      : 'boss' ;
TK_PHASE     : 'phase' ;
TK_LOOT      : 'loot' ;
TK_DROP      : 'drop' ;
TK_MODIFY    : 'modify' ;
TK_CONDITION : 'condition' ;
TRUE         : 'true' ;
FALSE        : 'false' ;

// OPERADORES Y DELIMITADORES
OP_REL : '==' | '!=' | '<=' | '>=' | '<' | '>' ;
LBRACE : '{' ;
RBRACE : '}' ;
SEMI   : ';' ;
COLON  : ':' ;

// LITERALES E IDENTIFICADORES
TIME_LITERAL : [0-9]+ ':' [0-9]+ ;
PERCENTAGE   : [0-9]+ ('.' [0-9]+)? '%' ;
NUMBER       : [0-9]+ ('.' [0-9]+)? ;
STRING       : '"' ~["\r\n]* '"' ;
ID           : [a-zA-Z_] [a-zA-Z_0-9]* (':' [a-zA-Z_] [a-zA-Z_0-9]*)* ;

// IGNORADOS
WS : [ \t\r\n]+ -> skip ;