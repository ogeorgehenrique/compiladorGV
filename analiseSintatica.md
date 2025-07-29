# Etapa 3: Analisador Sintático

O arquivo parser.py implementa a segunda fase da compilação, chamada análise sintática, responsável por verificar se a sequência de tokens extraída pelo analisador léxico segue as regras gramaticais da linguagem. Essa etapa é essencial para garantir que o código está estruturado corretamente antes de passar para o analisador semantico.

# Objetivo da Análise Sintática

Verificar se os tokens formam estruturas válidas segundo a gramática da linguagem. Isso inclui:
- Declarações de variáveis corretas (int x;)
- Estruturas de controle bem formadas (se, enquanto, para)
- Retornos válidos dentro de funções
- Verificação de blocos e uso correto de {}, (), ;

# Componentes envolvidos na análise sintática

| Arquivo/Classe              | Função                                                                 |
|----------------------------|------------------------------------------------------------------------|
| `CompiladorGV.g4`          | Define as regras gramaticais (sintaxe) da linguagem.                   |
| `CompiladorGVParser.py`    | Gerado automaticamente pelo ANTLR a partir da gramática `.g4`.        |
| `parser.py`                | Script principal que executa a análise sintática.                      |
| `CommonTokenStream` (ANTLR4) | Encapsula os tokens a serem analisados pelo parser.                 |
| `MyParserErrorListener.py` | Define um ouvinte personalizado para lidar com erros sintáticos.       |
| `ParseTreeGenerator.py`    | Visita a árvore sintática e gera a saída gráfica (AST) em formato DOT. |

# Como Funciona?


## 1. Leitura do código-fonte

O parser.py recebe o caminho de um arquivo de código-fonte como argumento, assim como o scanner.py. Ele transforma esse arquivo em um input_stream.
```
input_stream = FileStream(argv[1], encoding="utf-8")
```

## 2. Geração de tokens com o Lexer

O código é lido e passado para o CompiladorGVLexer, gerando os tokens léxicos.
```
lexer = CompiladorGVLexer(input_stream)
tokens = CommonTokenStream(lexer)
```

## 3. Análise Sintática com o Parser

Os tokens são analisados pelo CompiladorGVParser, que aplica as regras da gramática e constrói a árvore sintática (Parse Tree).
```
parser = CompiladorGVParser(tokens)
tree = parser.inicio()  # início é a regra inicial da gramática
```

## 4. Captura e personalização de erros sintáticos

Antes de iniciar a análise, o listener padrão do ANTLR é removido, e o MyParserErrorListener é adicionado para capturar erros de forma personalizada.

```
parser.removeErrorListeners()
parser.addErrorListener(MyParserErrorListener())
```
Esse ouvinte exibe erros como: 

```
ERRO SINTÁTICO [Linha 3, Coluna 5]: Esperado ';' após 'retorna'
```

## 5. Geração da Árvore Sintática (AST)

Após a análise, a árvore sintática é percorrida por um visitante personalizado (ParseTreeGenerator) e convertida para o formato .dot, utilizado por ferramentas gráficas como o Graphviz.

```
visitor = ParseTreeGenerator()
visitor.visit(tree)

with open("saida_ast.dot", "w") as f:
    f.write("digraph AST {\n")
    f.write("\n".join(visitor.output))
    f.write("\n}")
```

## 6. Integração com o Gerador TAC

Se o argumento --gerar-tac for passado via terminal, o parser.py também chama a classe TACGenerator, responsável por transformar a árvore sintática em código intermediário (Three Address Code).

```
if "--gerar-tac" in argv:
    tacgen = TACGenerator()
    tacgen.visit(tree)
    tacgen.salvar_em_arquivo("saida.tac")
```
# Importância dessa etapa

A análise sintática garante que o código-fonte obedece à estrutura definida pela linguagem. Erros como:
- falta de ponto e vírgula
- blocos mal fechados
- expressões incorretas
- retorno fora da função

são detectados aqui. Sem passar nessa etapa, o código não pode avançar para a geração de código intermediário ou execução.

# Entendendo o Código

Nessa parte vamos detalhar as classes criadas manualmente que compõem a etapa de análise sintática do compilador:

# Parser.py

Script principal da análise sintática. Suas funções:
	1.	Lê o código-fonte.
	2.	Gera tokens (com o lexer).
	3.	Verifica a estrutura sintática com o parser.
	4.	Chama o gerador de AST (árvore sintática).
	5.	Gera a TAC, se necessário.

```
from antlr4 import *                                        #importa todos os utilitários da biblioteca ANTLR4
from CompiladorGVLexer import CompiladorGVLexer             #Importa a classe léxica gerada automaticamente pelo ANTLR a partir da gramática .g4. Essa classe é usada para converter o código-fonte em tokens.
from CompiladorGVParser import CompiladorGVParser           #importa a classe do parser gerado pelo ANTLR. Essa classe define as regras de análise sintática da linguagem.
from MyParserErrorListener import MyParserErrorListener     #importa uma classe personalizada que estende o comportamento padrão de tratamento de erros do ANTLR, permitindo exibir mensagens de erro sintático mais claras e customizadas.
from ParseTreeGenerator import ParseTreeGenerator           #Importa uma classe visitante personalizada usada para percorrer a árvore sintática gerada e montar sua representação visual (AST).
import sys

import TACGenerator


#Define a função principal que será executada com os argumentos da linha de comando.
def main(argv):
    if len(argv) < 2:
        print("Uso: python parser.py <arquivo_fonte>")
        return

    input_stream = FileStream(argv[1], encoding='utf-8')    #Lê o conteúdo do arquivo-fonte informado via terminal como um stream de texto.
    lexer = CompiladorGVLexer(input_stream)                 #Usa o lexer para gerar tokens a partir do conteúdo do arquivo.
    tokens = CommonTokenStream(lexer)                       #Esses tokens são agrupados em um CommonTokenStream, necessário para o parser funcionar corretamente.
    parser = CompiladorGVParser(tokens)                     #Cria uma instância do parser e alimenta com os tokens para iniciar a análise sintática.


    #Remove os tratadores de erro padrão do ANTLR e adiciona o personalizado 
    parser.removeErrorListeners()
    parser.addErrorListener(MyParserErrorListener())

    

    # Gerar TAC se ativado
    if "--gerar-tac" in argv:
        print("🚧 Etapa 4: Geração de Código Intermediário (TAC)")
        tacgen = TACGenerator()
        tacgen.visit(tree)
        tacgen.salvar_em_arquivo("saida.tac")
        print("✅ Código TAC gerado em 'saida.tac'")

    try:
        tree = parser.inicio()  #Tenta executar a análise sintática chamando a regra inicial da gramática (inicio). O retorno é a árvore sintática (parse tree).
        visitor = ParseTreeGenerator()
        visitor.visit(tree)

        #Cria um arquivo no formato DOT, que representa graficamente a árvore gerada (AST).
        with open("saida_ast.dot", "w") as f:
            f.write("digraph AST {\n")
            f.write("\n".join(visitor.output))
            f.write("\n}")
        print("Programa analisado com sucesso! ✅")
        print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
    except Exception as e:
        print(f"\033[91mErro durante a análise: {e}\033[0m")
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv) # type: ignore
```

## Código com explicações linha a linha

- `from antlr4 import *`

Isso inclui FileStream, CommonTokenStream, ParseTreeVisitor e outros recursos essenciais para o funcionamento do parser. É a base para integração com a infraestrutura gerada automaticamente pelo ANTLR.

- `from CompiladorGVLexer import CompiladorGVLexer`

Importa a classe do analisador léxico (lexer), que foi gerada automaticamente pelo ANTLR a partir da gramática .g4. Essa classe é usada para transformar o texto do código-fonte em tokens.

- from CompiladorGVParser import CompiladorGVParser`

Importa a classe do analisador sintático (parser) gerada automaticamente pelo ANTLR. Essa classe aplica as regras gramaticais da linguagem para construir a árvore sintática (Parse Tree) com base nos tokens.

- `from MyParserErrorListener import MyParserErrorListener`

Importa o ouvinte de erros personalizado, que trata erros sintáticos de forma amigável e mais explicativa do que o padrão do ANTLR. Ele substitui o listener padrão.

- `from ParseTreeGenerator import ParseTreeGenerator`

Importa uma classe visitante personalizada que percorre a árvore sintática para gerar sua representação em formato gráfico (AST), exportando para o formato DOT (Graphviz).

- `import sys`

Módulo da biblioteca padrão do Python utilizado para acessar argumentos da linha de comando (sys.argv) e encerrar a execução do script com sys.exit() em caso de erro.

- `import TACGenerator`

Importa o gerador de código intermediário (TAC - Three Address Code), que transforma a árvore sintática em uma forma intermediária de baixo nível, facilitando a tradução para código de máquina posteriormente.

- `def main(argv):`

Define a função principal que será executada quando o script for chamado via terminal. Ela recebe a lista de argumentos passados (argv).

-  `if len(argv) < 2:`

Verifica se o usuário passou corretamente o caminho do arquivo-fonte como argumento. Caso contrário, exibe a mensagem de uso e termina a execução.

- `input_stream = FileStream(argv[1], encoding='utf-8')`

Lê o arquivo-fonte informado e transforma seu conteúdo em uma stream de texto UTF-8 que será analisada pelo lexer.

- `lexer = CompiladorGVLexer(input_stream)`

Cria uma instância do lexer que recebe o input_stream e produz os tokens com base na gramática léxica definida.

- `tokens = CommonTokenStream(lexer)`

Armazena todos os tokens gerados em uma estrutura especial (CommonTokenStream) que será passada ao parser. Ele permite ao parser “navegar” entre os tokens conforme a gramática.

- `parser = CompiladorGVParser(tokens)`

Cria uma instância do parser com os tokens recebidos. Esse parser validará se a sequência de tokens segue a sintaxe da linguagem.

- ``


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











