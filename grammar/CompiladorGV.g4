
grammar primeiroCodigo;


//TOKENS
ESCREVER: 'escrever';
LER: 'ler';
SE: 'se';
SENAO: 'senao';
PARA: 'para';
ENQUANTO: 'enquanto';
//TIPO_INT: 'inteiro';



ABRE_PAR: '(';
FECHA_PAR: ')';
ABRE_CHAVE: '{';
FECHA_CHAVE: '}';
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
MENOR_IGUAL_Q: '>=';
MAIOR_IGUAL_Q: '<=';
AND: '&&';
OR: '||';
NOT: '!';


STRING: '"' (~["\r\n])* '"';
INTEIRO: [0-9]+;
FLOAT: [0-9]+ '.'[0-9]* EXPONENT? 
| '.' [0-9]+ EXPONENT? 
| [0-9]+ EXPONENT?
;

fragment
EXPONENT: [e|E] [+|-]? [0-9]+;

//NUMBER: INTEIRO | FLOAT;


ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\n\r\f]+ -> skip;

inicio 
    :comandos+
    ;
    
comandos
    : comando_ler
    | comando_escrever
    | comando_se
    | comando_para
    | comando_enquanto
    //| comando_senao
    ;
    
comando_ler:
    LER ABRE_PAR ID FECHA_PAR FINAL;
    
comando_escrever:
    ESCREVER ABRE_PAR (STRING | expressao) FECHA_PAR FINAL;
    
comando_se:
    SE ABRE_PAR condicao FECHA_PAR ABRE_CHAVE comandos+ FECHA_CHAVE (SENAO ABRE_CHAVE comandos+ FECHA_CHAVE)?;

//comando_senao:
  //  SENAO ABRE_CHAVE comandos+ FECHA_CHAVE;
    
//eu que montei essa logica, mas o chat disse q tem como simplificar, ai usei a de cima    
//    SE ABRE_PAR condicao FECHA_PAR ABRE_CHAVE comandos+ FECHA_CHAVE 
//    | SE ABRE_PAR condicao FECHA_PAR operador_logico SE ABRE_PAR condicao FECHA_PAR ABRE_CHAVE comandos+ FECHA_CHAVE
//    ;
 
comando_para:
    PARA ABRE_PAR atribuicao FINAL condicao FINAL incremento FECHA_PAR
    ABRE_CHAVE comandos+ FECHA_CHAVE;
    
    //PARA ABRE_PAR (expressao operador expressao)
    //FINAL (expressao operador expressao)
    //FINAL (ID INCREMENTO | DECREMENTO)
    //FECHA_PAR ABRE_CHAVE comandos+ FECHA_CHAVE
    //;
    
comando_enquanto:
    ENQUANTO ABRE_PAR condicao FECHA_PAR
    bloco
    ;

//Auxiliar da funcao for    
atribuicao:
    ID RECEBE expressao;

//Auxiliar da funcao for
incremento:
    ID INCREMENTO
    | ID DECREMENTO
    | atribuicao
    ;

 bloco:
    ABRE_PAR comando+ FECHA_PAR FINAL;
 
//Auxliar para as funcoes SE/SENAO/PARA    
condicao
    : expressao operador expressao
    | condicao AND condicao
    | condicao OR condicao
    | ABRE_PAR condicao FECHA_PAR
    ;
    
    
 //OPERADORES  
operador
    : IGUAL_EXATO
    | DIFERENTE
    | MAIOR_Q
    | MENOR_Q
    | MENOR_IGUAL_Q
    | MAIOR_IGUAL_Q
    | RECEBE
    ;

//OPERADOR LOGICO
operador_logico
    : AND
    | OR
    | NOT    
    ;

//Expressoes com precedencia
expressao:
    expressao op=(MULT| DIV) expressao
    | expressao op=(PLUS|MINUS) expressao
    | ABRE_PAR expressao FECHA_PAR
    | INTEIRO | FLOAT
    | ID
    ;




    

//expr: term ((PLUS|MINUS) term)*;
//term: factor((MULT|DIV) factor)*;
//factor: NUMBER;
