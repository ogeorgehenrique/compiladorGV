grammar CompiladorGV;

// ---------------- TOKENS ----------------
LEIA: 'leia';
ESCREVA: 'escreva';
SE: 'se';
SENAO: 'senao';
PARA: 'para';
ENQUANTO: 'enquanto';
RETORNA: 'retorna';

TIPO_INT: 'int';
TIPO_STRING: 'string';

ABRE_PAR: '(';
FECHA_PAR: ')';
ABRE_CHAVE: '{';
FECHA_CHAVE: '}';
VIRGULA: ',';
FINAL: ';';
RECEBE: '=';
INCREMENTO: '++';
DECREMENTO: '--';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

IGUAL_EXATO: '==';
DIFERENTE: '!=';
MAIOR_Q: '>';
MENOR_Q: '<';
MENOR_IGUAL_Q: '<=';
MAIOR_IGUAL_Q: '>=';

AND: '&&';
OR: '||';
NOT: '!';

STRING: '"' (~["\r\n])* '"';
INTEIRO: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]* EXPONENT?
     | '.' [0-9]+ EXPONENT?
     | [0-9]+ EXPONENT?;

fragment EXPONENT: [eE] [+\-]? [0-9]+;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;

// ---------------- REGRAS ----------------

inicio
    : comandos+
    ;

comandos
    : comando_declaracao_funcao
    | comando_chamada_funcao
    | comando_retorno
    | comando_ler
    | comando_escrever
    | comando_se
    | comando_para
    | comando_enquanto
    | comando_atribuicao
    | comando_declaracao
    ;

comando_declaracao_funcao
    : (TIPO_INT | TIPO_STRING) ID ABRE_PAR parametros? FECHA_PAR bloco_funcao
    ;

comando_chamada_funcao
    : ID ABRE_PAR argumentos? FECHA_PAR FINAL
    ;

parametros
    : parametro (VIRGULA parametro)*
    ;

parametro
    : (TIPO_INT | TIPO_STRING) ID
    ;

argumentos
    : expressao (VIRGULA expressao)*
    ;

comando_retorno
    : RETORNA expressao FINAL
    ;

comando_ler
    : LEIA ABRE_PAR ID FECHA_PAR FINAL
    ;

comando_escrever
    : ESCREVA ABRE_PAR (STRING | expressao) FECHA_PAR FINAL
    ;

comando_se
    : SE ABRE_PAR condicao FECHA_PAR bloco (SENAO bloco)?
    ;

comando_para
    : PARA ABRE_PAR atribuicao FINAL condicao FINAL incremento FECHA_PAR bloco
    ;

comando_enquanto
    : ENQUANTO ABRE_PAR condicao FECHA_PAR bloco
    ;

comando_atribuicao
    : atribuicao FINAL
    ;

comando_declaracao
    : TIPO_INT ID (RECEBE expressao)? FINAL
    | TIPO_STRING ID (RECEBE expressao)? FINAL
    ;

atribuicao
    : ID RECEBE expressao
    ;

incremento
    : ID INCREMENTO
    | ID DECREMENTO
    | atribuicao
    ;

condicao
    : expressao operador expressao
    | condicao AND condicao
    | condicao OR condicao
    | ABRE_PAR condicao FECHA_PAR
    ;

operador
    : IGUAL_EXATO
    | DIFERENTE
    | MAIOR_Q
    | MENOR_Q
    | MAIOR_IGUAL_Q
    | MENOR_IGUAL_Q
    | RECEBE
    ;

lista_argumentos
    : expressao (',' expressao)*
    ;
    
// expressao
//     : expressao op=(MULT | DIV) expressao
//     | expressao op=(PLUS | MINUS) expressao
//     | ABRE_PAR expressao FECHA_PAR
//     | INTEIRO
//     | FLOAT
//     | STRING
//     | ID
//     ;
 expressao
    : expressao op=(MULT | DIV) expressao
    | expressao op=(PLUS | MINUS) expressao
    | ID ABRE_PAR lista_argumentos? FECHA_PAR    // CHAMADA DE FUNÇÃO!!!
    | ABRE_PAR expressao FECHA_PAR
    | INTEIRO
    | FLOAT
    | STRING
    | ID
    ;


bloco
    : ABRE_CHAVE comandos+ FECHA_CHAVE
    ;

bloco_funcao
    : ABRE_CHAVE comandos* comando_retorno FECHA_CHAVE
    ;


//ERRO: . { raise Exception("Símbolo inválido: " + getText()) };
//ERRO: . { raise RuntimeError("Símbolo inválido"); };
//ERRO: . { System.err.println("ERRO LÉXICO [Linha " + getLine() + ", Coluna " + getCharPositionInLine() + "]: Símbolo '" + getText() + "' inválido."); };
//ERRO: . { raise RuntimeError(f"ERRO LÉXICO [Linha {self._line}, Coluna {self._column}]: Símbolo '{self.text}' inválido") };
//ERRO: . { raise Exception("Símbolo inválido: " + getText()) };
//ERRO: . { print(f"ERRO LÉXICO [Linha {self.line}, Coluna {self.column+1}]: Símbolo '{self.text}' inválido."); };
//ERRO: . { print("\033[91mERRO LÉXICO [Linha " + str(self.line) + ", Coluna " + str(self.column + 1) + "]: Símbolo '" + self.text + "' inválido.\033[0m"); };
ERRO: . { raise Exception(f"\033[91mERRO LÉXICO [Linha {self.line}, Coluna {self.column + 1}]: Símbolo '{self.text}' inválido.\033[0m") };