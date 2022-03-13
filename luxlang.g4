grammar luxlang;
program : statement+;
statement : let | show ;
let : 'let' VAR '=' INT ;
show : 'show' (INT | VAR) ;

VAR : [a-z]+ ;
INT : [0-9]+ ;
WS : [ \n\t\r]+ -> skip;