# Construção da Gramática CompiladorGV.g4
A gramática é um dos componentes centrais de um compilador. Ela define formalmente quais construções sintáticas são válidas na linguagem, ou seja, o que o programa pode ou não conter em termos de comandos, expressões, funções, etc.
No caso da linguagem GV (George e Vinicius Language), utilizamos o ANTLR4 para construir essa gramática, composta por duas seções principais: **Definição dos Tokens (Análise Léxica) e Regras Sintáticas (Análise de Estrutura)**

## Por que a gramática é necessária?

A gramática:
- Define as regras de sintaxe da linguagem.
- Permite ao ANTLR gerar automaticamente um parser e um lexer.
- Facilita a validação e compreensão estrutural do código-fonte.
- Constrói a árvore sintática (Parse Tree), usada por outras fases do compilador.

## Estrutura da gramática

A gramática CompiladorGV está dividida em duas partes:

| Parte              | O que define                                                   | Exemplo                        |
|--------------------|----------------------------------------------------------------|--------------------------------|
| Tokens (Lexemas)   | As palavras-chave e símbolos da linguagem                      | `int`, `if`, `+`, `;`          |
| Regras Sintáticas  | A estrutura do código, ou seja, como os tokens se combinam     | `if (condição) { comandos }`   |

# Gramática Completa

```
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


 expressao
    : expressao op=(MULT | DIV) expressao
    | expressao op=(PLUS | MINUS) expressao
 // | ID ABRE_PAR lista_argumentos? FECHA_PAR    // CHAMADA DE FUNÇÃO!!!
    | ID ABRE_PAR expressao (VIRGULA expressao)* FECHA_PAR   // chamada de função (ajustada)
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


//funcao que retorna o erro LEXICO
ERRO: . { raise Exception(f"\033[91mERRO LÉXICO [Linha {self.line}, Coluna {self.column + 1}]: Símbolo '{self.text}' inválido.\033[0m") };
```


## 1. Definição dos Tokens (Análise Léxica)

- Define palavras-chave reservadas da linguagem.
```
LEIA: 'leia';
ESCREVA: 'escreva';
SE: 'se';
SENAO: 'senao';
PARA: 'para';
ENQUANTO: 'enquanto';
RETORNA: 'retorna';
...
```

- Define os tipos de dados disponíveis na linguagem.
```
TIPO_INT: 'int';
TIPO_STRING: 'string';
...
```

- Define operadores aritméticos.
```
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
```

- Define operadores relacionais e lógicos.

```
IGUAL_EXATO: '==';
DIFERENTE: '!=';
...
AND: '&&';
OR: '||';
NOT: '!';
```

- Define valores literais, como strings, inteiros e floats.

```
STRING: '"' (~["\r\n])* '"';
INTEIRO: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]* EXPONENT?;
```

- Define identificadores (nomes de variáveis, funções) e ignora espaços em branco.

```
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
```

## 2. Regras Sintáticas (Análise de Estrutura)

As regras sintáticas são compostas por comandos e expressões que formam programas válidos. Algumas delas:

- Regra principal:

Ela define que todo programa deve ter ao menos um comando.
```
inicio: comandos+;
```

- Comandos válidos:

```
comandos:
    | comando_declaracao_funcao
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
```

Exemplos de regras sintáticas importantes

| Regra                      | O que permite fazer                                     |
|---------------------------|----------------------------------------------------------|
| `comando_se`              | Criar estruturas condicionais com `se` e `senao`         |
| `comando_para`            | Criar laços de repetição `para (...) { ... }`            |
| `comando_declaracao_funcao` | Declarar funções                                       |
| `expressao`               | Usar operadores e valores                                |

## Exemplo de regra para condição:
```
condicao:
      expressao operador expressao
    | condicao AND condicao
    | condicao OR condicao
    | ABRE_PAR condicao FECHA_PAR
    ;
```
Essa regra permite condições como:
```
(a < b && b > c) || (x == y)
```

## Tratamento de Erros Léxicos

No final da gramática, há uma regra especial:
```
ERRO: . { raise Exception(f"\033[91mERRO LÉXICO [Linha {self.line}, Coluna {self.column + 1}]: Símbolo '{self.text}' inválido.\033[0m") };
```
Ela captura qualquer símbolo inválido e lança uma exceção, exibindo o erro com linha e coluna, como:
```
ERRO LÉXICO [Linha 1, Coluna 5]: Símbolo '#' inválido.
```







