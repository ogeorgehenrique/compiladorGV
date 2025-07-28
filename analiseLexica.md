# Etapa 2: Analisador Léxico

O arquivo scanner.py implementa a primeira fase da compilação, chamada análise léxica, responsável por quebrar o código-fonte em unidades léxicas (tokens). Esta etapa é crucial para preparar o código para a análise sintática.


# Objetivo da Análise Léxica

Transformar o código-fonte bruto (texto) em uma sequência de tokens, que são unidades significativas da linguagem, como:
- Identificadores (x, main, contador)
- Palavras-chave (int, retorna, se)
- Operadores (+, =, ==)
- Símbolos (;, {, })
- Literais ("texto", 42, 3.14)

## Componentes envolvidos na análise léxica

| Arquivo/Classe               | Função                                                                 |
|-----------------------------|------------------------------------------------------------------------|
| `CompiladorGVLexer.g4`      | Arquivo de gramática léxica usado pelo ANTLR para gerar o `CompiladorGVLexer`. |
| `CompiladorGVLexer.py`      | Gerado automaticamente pelo ANTLR a partir da gramática `.g4`.        |
| `scanner.py`                | Script principal que executa a análise léxica.                         |
| `CommonTokenStream` (ANTLR4)| Estrutura de dados que armazena os tokens extraídos.                  |
| `MyLexerErrorListener.py` | Define um ouvinte personalizado para lidar com erros léxicos de forma amigável. |

# Como Funciona?

## 1. Leitura do arquivo-fonte

O scanner.py recebe o caminho de um arquivo de código-fonte como argumento, e o lê usando o FileStream, transformando-o em um stream de caracteres UTF-8.

```
input_stream = FileStream(argv[1], encoding='utf-8')
```

## 2. Tokenização via Lexer (CompiladorGVLexer)

Esse texto é passado para o CompiladorGVLexer, classe gerada automaticamente pelo ANTLR a partir da gramática .g4. Ela aplica as regras léxicas e identifica os tokens válidos.

```
lexer = CompiladorGVLexer(input_stream)
```

## 3. Coleta dos tokens via CommonTokenStream

O resultado é encapsulado em um CommonTokenStream, que é uma lista ordenada de tokens que pode ser passada para o parser posteriormente.

```
tokens = CommonTokenStream(lexer)
```

## 4. Impressão formatada dos tokens

O scanner.py pode iterar sobre os tokens e imprimi-los no terminal com informações úteis:

```
<Tipo, 'Lexema', Linha, Coluna>
```
exemplo:
```
<ID, 'contador', Linha 1, Coluna 4>
<ATRIBUICAO, '=', Linha 1, Coluna 13>
<INTEIRO, '10', Linha 1, Coluna 15>
```

## 5. Tratamento de erros léxicos

Se o código conter símbolos inválidos (ex: @, #, &), o lexer pode disparar um erro. Caso você implemente um MyLexerErrorListener, ele pode interceptar esses erros e mostrar mensagens personalizadas, como:

```
ERRO LÉXICO [Linha 1, Coluna 5]: Símbolo '@' não reconhecido pela linguagem.
```

# Importância dessa etapa

A análise léxica é a base de todo o processo de compilação. Ela garante que os símbolos do código estão corretos, respeitam a sintaxe da linguagem e são compreensíveis para as etapas seguintes (sintática, semântica, etc). Um erro aqui impede qualquer análise posterior.

# Entendendo o Código
Nessa parte vamos detrinchar todas as classes que foram implementadas por mim e realizam a analise Lexica do meu compilador:

# Scanner.py

O scanner.py representa a etapa de análise léxica, onde:
1. o código é lido.
2. analisado caracter por caracter.
3. dividido em tokens,
4. e esses tokens são mostrados para o usuário com precisão.

É a base de todo compilador, pois garante que a entrada é composta por símbolos válidos.

O objetivo desse script é realizar a análise léxica de um código fonte da sua linguagem, utilizando o ANTLR4, ou seja, ele converte o código fonte em tokens com base na gramática léxica definida com ANTLR4.

```
from antlr4 import *                            
from CompiladorGVLexer import CompiladorGVLexer 
import sys

def main(argv):
    if len(argv) < 2:
        print("Uso: python scanner.py <caminho_do_arquivo>")
        return
    
    input_file = argv[1] 
    input_stream = FileStream(input_file, encoding="utf-8")  
    lexer = CompiladorGVLexer(input_stream)                  
    token = lexer.nextToken()                                
  
    print("-" * 33)                                           
    print(f"{'Tipo||':<5} {'Lexema||':<5} {'Linha||':<5} {'Coluna||'}")
    print("-" * 33)

    try:
        while token.type != Token.EOF:
            tipo_token = lexer.symbolicNames[token.type]
            lexema = token.text
            linha = token.line
            coluna = token.column + 1

            print(f"<{tipo_token}, '{lexema}', {linha}, {coluna}>")

            token = lexer.nextToken()
    except Exception as e:
        print(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)
```
## Código com explicações linha a linha

- `from antlr4 import *`

Responsavel pela importação Geral da ANTLR4, carregando todas as funcionalidades da biblioteca ANTLR4 (como FileStream, Token, etc), usadas para leitura do arquivo e geração dos tokens.

- `from CompiladorGVLexer import CompiladorGVLexer`

Importa a classe CompiladorGVLexer, que foi automaticamente criada com base no seu arquivo CompiladorGV.g4. Essa classe sabe como identificar palavras-chave, identificadores, operadores, números, etc., de acordo com a gramática definida.

- `import sys`

Permite acessar os argumentos da linha de comando (argv) e encerrar o programa (sys.exit) em caso de erro.

- `def main(argv):`

Função principal do programa, que executa toda a análise léxica. Recebe os argumentos da linha de comando como entrada (o nome do arquivo, por exemplo).

- `if len(argv) < 2:`

Verifica se o usuário passou o nome do arquivo a ser analisado. Se não passou, imprime uma mensagem de uso e encerra a função sem erro.
  
- `input_file = argv[1]`

Captura o caminho do arquivo passado pelo usuário via terminal.

- `input_stream = FileStream(input_file, encoding="utf-8")`

Lê o arquivo como uma sequência de caracteres (stream). O FileStream converte o arquivo para um formato que o ANTLR consegue analisar. O encoding="utf-8" garante suporte a acentuação e símbolos especiais da língua portuguesa.

- `lexer = CompiladorGVLexer(input_stream)`

Instancia o analisador léxico (lexer), que processa o input_stream e gera tokens com base nas regras definidas no .g4.

- `token = lexer.nextToken()`

Lê o primeiro token do fluxo. A análise léxica no ANTLR é feita token por token, como uma leitura sequencial.

- Impressão do cabeçalho da tabela de tokens
```
    print("-" * 33)
    print(f"{'Tipo||':<5} {'Lexema||':<5} {'Linha||':<5} {'Coluna||'}")
    print("-" * 33)
```
Exibe um cabeçalho no terminal, simulando uma tabela onde cada linha será um token encontrado no código.
1. Tipo: nome simbólico do token (INT, ID, SE, ATRIB, etc.)
2. Lexema: o texto lido do código-fonte (main, x, =, 42)
3. Linha/Coluna: onde ele aparece no código original

- Loop principal: leitura dos tokens
```
    try:
        while token.type != Token.EOF:
```
Enquanto não for o fim do arquivo, continua lendo tokens. O tipo EOF (End Of File) indica que todos os caracteres foram processados.

- `tipo_token = lexer.symbolicNames[token.type]`

Cada token tem um tipo numérico, mas o ANTLR associa esse tipo a um nome simbólico definido na gramática (Nome simbólico do token), como INT, ID, SOMA, SE.

- `lexema = token.text`

É o trecho do código-fonte que corresponde ao token (Texto real do token (lexema)).
Exemplo: se o token for do tipo ID, o lexema pode ser "contador".

- Localização do token no código-fonte:
```
linha = token.line
coluna = token.column + 1
```
1. linha: linha em que o token aparece.
2. coluna: a coluna onde o lexema começa (ajustada com +1 para exibição humana, já que começa em 0).

- `print(f"<{tipo_token}, '{lexema}', {linha}, {coluna}>")`

Imprime o token formatado, seguindo o padrão: `<TIPO, 'lexema', linha, coluna>`

Exemplo:
```
<ID, 'main', 1, 5>
<INT, '10', 2, 9>
```

- `token = lexer.nextToken()`

Avança para o próximo token, repetindo o processo até atingir EOF.

- Tratamento de erros

```
    except Exception as e:
        print(str(e))
        sys.exit(1)
```
Caso ocorra alguma exceção inesperada, ela é exibida no terminal, e o programa encerra com status de erro.

- Execução do script como principal
```
if __name__ == '__main__':
    main(sys.argv)
```
Bloco padrão de execução em Python, Chama a função main passando os argumentos da linha de comando apenas quando o arquivo for executado diretamente (não importado como módulo).

**Resumo Visual do Fluxo**

`arquivo.c ➜ FileStream ➜ CompiladorGVLexer ➜ Tokens ➜ Impressão no terminal`

# MyLexerErrorListener

A classe MyLexerErrorListener personaliza o tratamento de erros léxicos na etapa de análise léxica do compilador. Seu principal papel é substituir a mensagem padrão do ANTLR por uma saída mais clara, objetiva e compreensível para o programador. Seu principal objetivo é interceptar erros de símbolos inválidos ou malformados durante a tokenização do código-fonte e exibir mensagens de erro bem localizadas e explicativas.

```
from antlr4.error.ErrorListener import ErrorListener

class MyLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        erro = msg.split(":")[-1].strip()
        print(f"ERRO LÉXICO [Linha {line}, Coluna {column + 1}]: Símbolo '{erro}' inválido.")
        print("-" * 60)
```

## Código com explicações linha a linha

- `from antlr4.error.ErrorListener import ErrorListener`

Importa a classe base ErrorListener do ANTLR, necessária para criar um ouvidor personalizado de erros.

- `class MyLexerErrorListener(ErrorListener):`

Cria uma subclasse chamada MyLexerErrorListener que herda os comportamentos da classe ErrorListener, permitindo sobrescrever o método syntaxError responsável pelos erros léxicos.

- `def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):`

Este método é automaticamente chamado pelo ANTLR sempre que ocorre um erro léxico.
1. recognizer: o analisador léxico (Lexer)
2. offendingSymbol: símbolo onde o erro foi detectado
3. line e column: localização do erro no código
4. msg: mensagem padrão de erro gerada pelo ANTLR
5. e: exceção (RecognitionException) associada ao erro (pode ser None)


- `erro = msg.split(":")[-1].strip()`

Extrai apenas o símbolo inválido da mensagem completa do ANTLR. Isso torna o aviso mais limpo e direto, ignorando o restante do texto técnico.

-`print(f"ERRO LÉXICO [Linha {line}, Coluna {column + 1}]: Símbolo '{erro}' inválido.")` 
Exibe a mensagem personalizada no formato:
```
ERRO LÉXICO [Linha X, Coluna Y]: Símbolo '#' inválido.
```
Isso ajuda o programador a identificar com precisão o erro.

- `print("-" * 60)`
Adiciona uma linha de separação para destacar visualmente o erro no terminal.

## Exemplo de Erro Detectado por MyLexerErrorListener
```
Código de entrada:
int a = @;

Saída esperada no terminal:
ERRO LÉXICO [Linha 1, Coluna 9]: Símbolo '@' inválido.
------------------------------------------------------------
```

A classe MyLexerErrorListener é fundamental para a usabilidade do compilador, pois:
1. Melhora a compreensão de erros durante a análise léxica.
2. Substitui mensagens técnicas e genéricas por algo claro e direto.
3. Facilita a localização e correção rápida dos erros de digitação ou símbolos não permitidos na linguagem.


# MyParserErrorListener

A classe MyParserErrorListener estende o comportamento padrão do ANTLR para exibir mensagens de erro sintático personalizadas, facilitando a identificação e correção de problemas no código fonte.

Interceptar e exibir erros de análise sintática com mensagens claras e contextualizadas, destacando o símbolo incorreto e a expectativa do compilador.

```
from antlr4.error.ErrorListener import ErrorListener
import sys

class MyParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        RED = "\033[91m"
        RESET = "\033[0m"
        simbolo = offendingSymbol.text if offendingSymbol else "símbolo desconhecido"

        if simbolo == "<EOF>":
            simbolo = "fim do arquivo"

        # Tratamento de mensagens específicas com base no conteúdo da mensagem do ANTLR
        if msg.startswith("missing"):
            esperado = msg.split(" ")[1].strip("'")
            if esperado == "';'":
                print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado ';' após '{simbolo}'{RESET}")
            else:
                print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado {esperado} após '{simbolo}'{RESET}")

        elif "no viable alternative" in msg:
            print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Comando incompleto ou mal formado antes de '{simbolo}'{RESET}")

        else:
            print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")

        sys.exit(1)
```

- `from antlr4.error.ErrorListener import ErrorListener`

Importa a classe base ErrorListener, que permite sobrescrever os métodos de tratamento de erro do ANTLR.

- `import sys`

Permite encerrar o programa com sys.exit(1) ao detectar um erro.

- `class MyParserErrorListener(ErrorListener):`

Cria uma subclasse de ErrorListener chamada MyParserErrorListener, usada para interceptar erros sintáticos.

- `def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):`

Este método é chamado automaticamente pelo ANTLR quando ocorre um erro de sintaxe.
1. recognizer: o analisador sintático (parser)
2. offendingSymbol: símbolo onde o erro ocorreu
3. line e column: localização do erro no código-fonte
4. msg: mensagem padrão gerada pelo ANTLR
5. e: exceção lançada (pode ser None)

- Códigos ANSI para colorir a mensagem de erro no terminal
```
RED = "\033[91m"
RESET = "\033[0m"
```
Define cores para exibir erros em vermelho no terminal, tornando a leitura mais visível.

- `simbolo = offendingSymbol.text if offendingSymbol else "símbolo desconhecido"`

Tenta capturar o texto do símbolo ofensivo; caso não exista, usa uma mensagem padrão.

- Exibe uma mensagem quando chega ao fim o arquivo 
```
if simbolo == "<EOF>":
    simbolo = "fim do arquivo"
```
Melhora a clareza da mensagem ao interpretar EOF como “fim do arquivo”.

## Tratamento de mensagens específicas

- Verifica se o erro é de “símbolo ausente”

Detecta mensagens de símbolo ausente (missing ';' at 'x') e extrai o token esperado.
```
if msg.startswith("missing"):
    esperado = msg.split(" ")[1].strip("'")
```

- Mensagem personalizada e clara quando um ponto e vírgula é esquecido
```
if esperado == "';'":
    print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado ';' após '{simbolo}'{RESET}")
```

- Mensagem para outros símbolos ausentes, como `)`, `}` ou `,`
```
else:
    print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado {esperado} após '{simbolo}'{RESET}")
```

- Mensagens genéricas quando o parser não encontra nenhuma regra válida para seguir — normalmente por estruturas incompletas.

```
elif "no viable alternative" in msg:
    print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Comando incompleto ou mal formado antes de '{simbolo}'{RESET}")
```

- Fallback: exibe a mensagem original do ANTLR com uma formatação amigável.

```
else:
    print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")
```
 ## Exemplos de erros comuns:

1. Esquecendo ponto e vírgula:
```
int a = 1
retorna 0;
```
Saída: `ERRO SINTÁTICO [Linha 2, Coluna 5]: Esperado ';' após 'a'`

2. Estrutura incompleta:
```
se (x == 1) 
retorna 0;
```
Saída: `ERRO SINTÁTICO [Linha 2, Coluna 1]: Comando incompleto ou mal formado antes de 'retorna'`










