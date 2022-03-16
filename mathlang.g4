grammar mathlang;

POW: '^';
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
NUMBER: [0-9]+;
WHITESPACE: [ \r\n\t]+ -> skip;

start : expression;
expression : NUMBER                                               # Number
   | '-' inner=expression                                      # Unary_Neg
   | '(' inner=expression ')'                             # Parentheses
   | left=expression op=POW right=expression        # Power
   | left=expression op=(MUL|DIV) right=expression  # MultiplicationOrDivision
   | left=expression op=(ADD|SUB) right=expression  # AdditionOrSubtraction
   ;