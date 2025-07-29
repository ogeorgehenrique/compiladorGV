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

# Importância dessa etapa

A análise sintática garante que o código-fonte obedece à estrutura definida pela linguagem. Erros como:
- falta de ponto e vírgula
- blocos mal fechados
- expressões incorretas
- retorno fora da função

são detectados aqui. Sem passar nessa etapa, o código não pode avançar para a geração de código intermediário ou execução.

## Entendendo o Código

Nessa parte vamos detalhar as classes criadas manualmente que compõem a etapa de análise sintática do compilador:

# Parser.py

O parser.py é o coração da etapa de análise sintática do seu compilador. Ele conecta:
1. Leitura do código-fonte
2. Análise léxica e sintática
3. Tratamento de erros
4. Visualização da árvore sintática

```
from antlr4 import *                                        
from CompiladorGVLexer import CompiladorGVLexer             
from CompiladorGVParser import CompiladorGVParser           
from MyParserErrorListener import MyParserErrorListener     
from ParseTreeGenerator import ParseTreeGenerator           
import sys

def main(argv):
    if len(argv) < 2:
        print("Uso: python parser.py <arquivo_fonte>")
        return

    input_stream = FileStream(argv[1], encoding='utf-8')    
    lexer = CompiladorGVLexer(input_stream)                 
    tokens = CommonTokenStream(lexer)                       
    parser = CompiladorGVParser(tokens)                     


    parser.removeErrorListeners()
    parser.addErrorListener(MyParserErrorListener())

    try:
        tree = parser.inicio()  
        visitor = ParseTreeGenerator()
        visitor.visit(tree)

        
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

- Remove as mensagem de erro padrão geradas pelo ANTLR

```
parser.removeErrorListeners()
parser.addErrorListener(MyParserErrorListener())
```
Remove os ouvintes de erro padrão do ANTLR e adiciona o ouvinte personalizado MyParserErrorListener, que exibe mensagens de erro sintático mais compreensíveis e detalhadas.

- Inicio visita aos ramos da arvoré AST

Cria uma instância do visitante que vai percorrer a árvore sintática (Parse Tree) para gerar uma representação visual dela (AST).
```
visitor = ParseTreeGenerator()
visitor.visit(tree)
```

- Criação do arquivo visual da árvore AST

Cria um arquivo saida_ast.dot, no formato reconhecido pelo Graphviz, para visualizar a árvore sintática abstrata (AST). O conteúdo é montado a partir da lista visitor.output.
```
with open("saida_ast.dot", "w") as f:
	f.write("digraph AST {\n")
	f.write("\n".join(visitor.output))
	f.write("\n}")
```
- Mensagem de confirmações

Se tudo correr bem, exibe mensagens positivas confirmando que a análise sintática foi concluída e a AST foi salva com sucesso.

```
print("Programa analisado com sucesso! ✅")
print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
```

- Ponto de parada, caso haja alguma exceção

Se qualquer exceção for levantada durante a análise sintática, essa parte captura e imprime o erro com formatação em vermelho, e encerra o programa com erro (exit code 1).

```
except Exception as e:
	print(f"\033[91mErro durante a análise: {e}\033[0m")
	sys.exit(1)
```

- Chamada do main

Ponto de entrada do script. Executa a função main() passando os argumentos recebidos da linha de comando (nome do arquivo-fonte)
```
if __name__ == '__main__':
    main(sys.argv)
```

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

## Código com explicações linha a linha


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


# ParseTreeGenerator

Responsável por gerar a representação gráfica da Árvore de Derivação (Parse Tree) do seu código-fonte com base na gramática definida. Esse script é extremamente útil para visualizar como o código está sendo interpretado pelo parser do compilador e pode te ajudar muito na depuração e entendimento de estruturas complexas.

O que essa classe faz, em resumo?
- Percorre toda a árvore sintática construída pelo ANTLR.
- Para cada regra ou token visitado, gera um nó com nome legível.
- Adiciona ligações entre os nós, formando um grafo em formato DOT.
- Permite a visualização gráfica da estrutura do código, o que é crucial para debug, ensino e entendimento da linguagem.

```
from antlr4 import *

class ParseTreeGenerator:
    def __init__(self):
        self.node_counter = 0
        self.output = []


    def new_node(self, label):
        node_name = f"n{self.node_counter}"
        # Corrige problema de aspas internas no label
        label = label.replace('"', r'\"')
        self.output.append(f'{node_name} [label="{label}"];')
        self.node_counter += 1
        return node_name


    def add_edge(self, parent, child):
        self.output.append(f"{parent} -> {child};")

    def visit(self, ctx):
        if ctx is None:
            return self.new_node("null")

        if isinstance(ctx, TerminalNode):
            # Para tokens terminais (ex: palavras-chave, símbolos)
            return self.new_node(f"'{ctx.getText()}'")

        # Para regras da gramática
        rule_name = type(ctx).__name__.replace("Context", "")
        node = self.new_node(rule_name)

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            child_node = self.visit(child)
            self.add_edge(node, child_node)

        return node
```

## Código com explicações linha a linha

- `from antlr4 import *`

Importa os recursos da biblioteca ANTLR4, incluindo:

1. ParserRuleContext (classe base de todos os nós da árvore)
2. TerminalNode (representa um token terminal como int, ;, +, etc.)


- `class ParseTreeGenerator:`

Define a classe ParseTreeGenerator, que será usada para visitar a árvore sintática e gerar sua representação em formato de grafo (.dot), usada para desenhar a árvore de derivação com ferramentas como o Graphviz.

- Método construtor da classe

```
def __init__(self):
	self.node_counter = 0
	self.output = []
```
1. self.node_counter: contador numérico para dar nomes únicos aos nós da árvore (n0, n1, n2, ...).
2. self.output: lista de strings que armazenará linhas do grafo em formato DOT, como:

```
n0 [label="Expressao"];
n0 -> n1;
```

- Método auxiliar que cria um novo nó da árvore

```
def new_node(self, label):
        node_name = f"n{self.node_counter}"
        # Corrige problema de aspas internas no label
        label = label.replace('"', r'\"')
        self.output.append(f'{node_name} [label="{label}"];')
        self.node_counter += 1
        return node_name
```
1. label: nome do nó (como Expressao, ID, +, etc).
2. node_name: nome interno do nó no grafo, como n3.
3. Corrige possíveis aspas internas no rótulo para evitar erros no DOT.
4. Armazena a linha correspondente no output e retorna o nome do nó criado.
Exemplo de saída: `n4 [label="Expressao"];`

- Método auxiliar para adicionar uma aresta (ligação) entre dois nós da árvore no grafo. Recebe os nomes dos nós parent e child.

```
    def add_edge(self, parent, child):
        self.output.append(f"{parent} -> {child};")
```
Exemplo de saída: `n1 -> n2;`


- `def visit(self, ctx):`
Método principal que percorre recursivamente a árvore sintática gerada pelo parser.

O argumento ctx (context): representa um nó da árvore (pode ser terminal ou não-terminal).

- Tratamento de especial caso haja um nó nulo

Caso o contexto seja nulo (nó inexistente), cria um nó especial com o rótulo "null", apenas para manter a estrutura da árvore intacta.

```
if ctx is None:
	return self.new_node("null")
```

- Criação de nó "terminal"

Se o nó for um terminal da linguagem (ex: `"+"`, `"int"`, `"main"`, etc), cria um nó com o texto do token e encerra a recursão nesse ramo.

```
if isinstance(ctx, TerminalNode):
	return self.new_node(f"'{ctx.getText()}'")
```

- Criação de nó interno

Se for um nó interno da árvore (ou seja, uma regra da gramática como Expressao, Comando, Bloco, etc), extrai o nome da regra removendo "Context" e cria o nó com esse rótulo.

```
rule_name = type(ctx).__name__.replace("Context", "")
node = self.new_node(rule_name)
```

- Percorre todos os filhos do nó atual, chamando visit() recursivamente para cada um:

```
for i in range(ctx.getChildCount()):
	child = ctx.getChild(i)
	child_node = self.visit(child)
	self.add_edge(node, child_node)
```
1.	Visita o filho.
2.	Cria o nó correspondente.
3.	Adiciona uma aresta entre o nó atual e seu filho.

- `return node`

Retorna o nome do nó atual, permitindo que a recursão monte a árvore completa corretamente.

**Exemplo de saída .dot gerada por essa classe:**
```
digraph AST {
n0 [label="Inicio"];
n1 [label="'int'"];
n2 [label="'main'"];
n3 [label="'('"];
n4 [label="parametros"];
...
n0 -> n1;
n0 -> n2;
...
}
```

