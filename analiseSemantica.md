# Etapa 4: Análise Semântica

A etapa de análise semântica é a terceira fase lógica do processo de compilação (após a análise léxica e sintática). Ela é responsável por verificar o significado do código, assegurando que as instruções seguem as regras de coerência da linguagem, mesmo que estejam sintaticamente corretas.

Enquanto o parser **(CompiladorGVParser + MyParserErrorListener)** e o ParseTreeGenerator cuidam da estrutura gramatical e erros como execução da regra inicio(), a análise semântica atua sobre a lógica e o significado do código.

# Objetivo da Análise Semântica

Enquanto a análise sintática verifica como o código está escrito, a análise semântica verifica o que o código está querendo fazer e se isso faz sentido. Alguns exemplos de erros semânticos que essa etapa detecta:
- Uso de variáveis não declaradas
- Declaração duplicada de variáveis ou funções
- Tipos incompatíveis em expressões (ex: int + string)
- Retorno incorreto em funções
- Uso de funções com parâmetros incorretos
- Escopos mal definidos (como usar variáveis fora de seu contexto)

# Componentes envolvidos na análise semântica

| Arquivo/Classe         | Função                                                                 |
|------------------------|------------------------------------------------------------------------|
| `main.py`              | Dispara a análise semântica após a análise sintática.                  |
| `ASTBuilderVisitor.py` | Constrói a Árvore Sintática Abstrata (AST) com base na árvore de derivação. |
| `SemanticAnalyzer.py`  | Percorre a AST realizando todas as validações semânticas.              |
| `SymbolTable.py`       | Classe auxiliar para controle de escopos e símbolos.                   |

# Como Funciona?

A análise semântica acontece depois que o código-fonte já passou pela análise léxica e sintática.

## 1. Construção da AST

O ASTBuilderVisitor é um visitante que transforma a árvore de derivação (Parse Tree) produzida pelo ANTLR em uma Árvore Sintática Abstrata (AST) simplificada, que representa apenas as estruturas relevantes do programa.

```
visitor = ASTBuilderVisitor()
ast = visitor.visit(tree)
```
Essa AST contém apenas as informações essenciais (sem símbolos auxiliares ou tokens sintáticos), o que facilita muito a análise semântica.


## 2. Execução da Análise Semântica

O SemanticAnalyzer percorre a AST e verifica, por exemplo:

- Se todas as variáveis foram declaradas antes de serem usadas
- Se os tipos são compatíveis em atribuições e expressões
- Se funções são declaradas corretamente e chamadas com os parâmetros certos
- Se comandos como retorna estão dentro de funções
- Se existe tentativa de divisão por zero
- Se variáveis estão sendo usadas de maneira coerente com seu tipo
- Se há redeclarações inválidas de símbolos
- Se o retorno da função está adequado ao tipo declarado

```
analisador = SemanticAnalyzer()
analisador.visit(ast)
```
Quando um erro é detectado, ele é armazenado em uma lista de erros e exibido com mensagens claras, como:

```
ERRO SEMÂNTICO [Linha 5]: Variável 'contador' usada antes de ser declarada.
```

# Importância dessa etapa

A análise semântica garante que o código não apenas parece correto, mas que faz sentido dentro da lógica da linguagem. Sem essa etapa, seria possível compilar programas que resultariam em comportamentos errados, ambiguidades ou falhas em tempo de execução.

Essa etapa é também onde o compilador começa a “entender” o que o código realmente significa, e não apenas como ele está escrito.


# Entendendo a estrutura do código

Nesta etapa, os principais arquivos envolvidos são:

# ASTBuilderVisitor.py

Este script é responsável por:
- Traduzir a árvore sintática bruta em uma AST compacta.
- Criar nós específicos (como Função, Variável, Atribuição, Expressão).
- Eliminar tokens e estruturas intermediárias desnecessárias para a análise.

Esse visitante é mais semântico do que sintático: ele constrói a intenção do programa.

A classe ASTBuilderVisitor estende o CompiladorGVVisitor gerado automaticamente pelo ANTLR e tem como objetivo percorrer a árvore sintática gerada a partir do código-fonte, interpretando cada construção da linguagem (declarações, comandos, expressões, etc.) e gerando uma estrutura em forma de dicionário (JSON-like) que representa de forma limpa e sem ruído a lógica e estrutura do programa.

Além disso, ele já faz uma construção inicial da Tabela de Símbolos, que é essencial para o analisador semântico posterior. A tabela de símbolos é usada para armazenar:
- Declarações de variáveis
- Escopos (funções, blocos)
- Tipos de dados
- Parâmetros de funções
- Retornos esperados

## Código ASTBuilderVisitor.py

```
from src.grammar.CompiladorGVVisitor import CompiladorGVVisitor
from src.grammar.CompiladorGVParser import CompiladorGVParser

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # pilha de escopos

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()

    def define(self, name, info):
        self.scopes[-1][name] = info

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

class ASTBuilderVisitor(CompiladorGVVisitor):
    def __init__(self):
        super().__init__()
        self.symbol_table = SymbolTable()

    def visitInicio(self, ctx: CompiladorGVParser.InicioContext):
        return {
            "type": "Program",
            "body": [self.visit(c) for c in ctx.comandos()]
        }

    def visitComandos(self, ctx: CompiladorGVParser.ComandosContext):
        if ctx.comando_declaracao_funcao():
            return self.visit(ctx.comando_declaracao_funcao())
        elif ctx.comando_chamada_funcao():
            return self.visit(ctx.comando_chamada_funcao())
        elif ctx.comando_retorno():
            return self.visit(ctx.comando_retorno())
        elif ctx.comando_ler():
            return self.visit(ctx.comando_ler())
        elif ctx.comando_escrever():
            return self.visit(ctx.comando_escrever())
        elif ctx.comando_se():
            return self.visit(ctx.comando_se())
        elif ctx.comando_para():
            return self.visit(ctx.comando_para())
        elif ctx.comando_enquanto():
            return self.visit(ctx.comando_enquanto())
        elif ctx.comando_atribuicao():
            return self.visit(ctx.comando_atribuicao())
        elif ctx.comando_declaracao():
            return self.visit(ctx.comando_declaracao())
        else:
            return None

    def visitComando_declaracao_funcao(self, ctx):
        tipo = ctx.getChild(0).getText()
        nome = ctx.ID().getText()
        parametros = []
        if ctx.parametros():
            parametros = [self.visit(p) for p in ctx.parametros().parametro()]
        corpo = self.visit(ctx.bloco_funcao())
        
        node = {
            "type": "FunctionDeclaration",
            "returnType": tipo,
            "name": nome,
            "params": parametros,
            "body": corpo
        }
        # Definir função na tabela de símbolos
        self.visitFunctionDeclaration(node)
        return node

    def visitParametro(self, ctx):
        return {
            "type": "Parameter",
            "paramType": ctx.getChild(0).getText(),
            "name": ctx.ID().getText()
        }

    def visitComando_declaracao_funcao(self, ctx):
        tipo = ctx.getChild(0).getText()
        nome = ctx.ID().getText()
        parametros = []
        if ctx.parametros():
            parametros = [self.visit(p) for p in ctx.parametros().parametro()]
        corpo = self.visit(ctx.bloco_funcao())
        return {
            "type": "FunctionDeclaration",
            "returnType": tipo,
            "name": nome,
            "params": parametros,
            "body": corpo
        }


    def visitComando_retorno(self, ctx):
        return {
            "type": "Return",
            "value": self.visit(ctx.expressao())
        }

    def visitComando_ler(self, ctx):
        return {
            "type": "Read",
            "identifier": ctx.ID().getText()
        }

    def visitComando_escrever(self, ctx):
        if ctx.STRING():
            return {
                "type": "Write",
                "value": ctx.STRING().getText()
            }
        return {
            "type": "Write",
            "value": self.visit(ctx.expressao())
        }

    def visitComando_se(self, ctx):
        return {
            "type": "IfStatement",
            "condition": self.visit(ctx.condicao()),
            "then": self.visit(ctx.bloco(0)),
            "else": self.visit(ctx.bloco(1)) if ctx.SENAO() else None
        }

    def visitComando_para(self, ctx):
        return {
            "type": "ForStatement",
            "init": self.visit(ctx.atribuicao()),
            "condition": self.visit(ctx.condicao()),
            "increment": self.visit(ctx.incremento()),
            "body": self.visit(ctx.bloco())
        }

    def visitComando_enquanto(self, ctx):
        return {
            "type": "WhileStatement",
            "condition": self.visit(ctx.condicao()),
            "body": self.visit(ctx.bloco())
        }

    def visitComando_atribuicao(self, ctx):
        return self.visit(ctx.atribuicao())

    def visitAtribuicao(self, ctx):
        return {
            "type": "Assignment",
            "target": ctx.ID().getText(),
            "value": self.visit(ctx.expressao())
        }

    def visitComando_declaracao(self, ctx):
        tipo = ctx.getChild(0).getText()
        nome = ctx.ID().getText()
        valor = self.visit(ctx.expressao()) if ctx.expressao() else None
        
        # Define variável no escopo atual
        self.symbol_table.define(nome, {
            "type": "variable",
            "varType": tipo,
            "value": valor
        })
        
        return {
            "type": "VariableDeclaration",
            "varType": tipo,
            "name": nome,
            "value": valor
        }

    def visitIncremento(self, ctx):
        if ctx.INCREMENTO():
            return {"type": "Increment", "target": ctx.ID().getText()}
        elif ctx.DECREMENTO():
            return {"type": "Decrement", "target": ctx.ID().getText()}
        else:
            return self.visit(ctx.atribuicao())

    def visitCondicao(self, ctx):
        if ctx.operador():  # caso: expressao operador expressao
            return {
                "type": "condicao_binaria",
                "left": self.visit(ctx.expressao(0)),
                "op": ctx.operador().getText(),
                "right": self.visit(ctx.expressao(1))
            }
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            # caso: (condicao)
            return self.visit(ctx.condicao(0))
        elif ctx.AND():
            # caso: condicao AND condicao
            return {
                "type": "condicao_logica",
                "op": "&&",
                "left": self.visit(ctx.condicao(0)),
                "right": self.visit(ctx.condicao(1))
            }
        elif ctx.OR():
            # caso: condicao OR condicao
            return {
                "type": "condicao_logica",
                "op": "||",
                "left": self.visit(ctx.condicao(0)),
                "right": self.visit(ctx.condicao(1))
            }
        else:
            raise Exception("Condicao não reconhecida")

    def visitExpressao(self, ctx):
        if hasattr(ctx, "op") and ctx.op:
            return {
                "type": "BinaryExpression",
                "operator": ctx.op.text,
                "left": self.visit(ctx.expressao(0)),
                "right": self.visit(ctx.expressao(1))
            }
        elif ctx.ID() and ctx.ABRE_PAR():
            nome = ctx.ID().getText()
            args = []
            # if ctx.lista_argumentos():
            if hasattr(ctx, "lista_argumentos") and ctx.lista_argumentos():
                args = [self.visit(e) for e in ctx.lista_argumentos().expressao()]
            return {
                "type": "FunctionCall",
                "name": nome,
                "arguments": args
            }
        elif ctx.ABRE_PAR():
            return self.visit(ctx.expressao(0))
        elif ctx.INTEIRO():
            return {"type": "IntLiteral", "value": int(ctx.INTEIRO().getText())}
        elif ctx.FLOAT():
            return {"type": "FloatLiteral", "value": float(ctx.FLOAT().getText())}
        elif ctx.STRING():
            return {"type": "StringLiteral", "value": ctx.STRING().getText()}
        elif ctx.ID():
            return {"type": "Identifier", "name": ctx.ID().getText()}

    def visitBloco(self, ctx):
        return {
            "type": "Block",
            "statements": [self.visit(c) for c in ctx.comandos()]
        }

    def visitBloco_funcao(self, ctx):
        statements = [self.visit(c) for c in ctx.comandos()]
        retorno = self.visit(ctx.comando_retorno())
        statements.append(retorno)
        return {
            "type": "Block",
            "statements": statements
        }
    
    def visitFunctionDeclaration(self, node):
        func_name = node["name"]
        return_type = node["returnType"]
        params = node["params"]

        # Define função no escopo global (nível 0)
        self.symbol_table.define(func_name, {
            "type": "function",
            "returnType": return_type,
            "params": params
        })

        # Cria escopo para corpo da função
        self.symbol_table.push_scope()

        # Define parâmetros no escopo da função
        for param in params:
            self.symbol_table.define(param["name"], {"type": param["paramType"]})

        # Visita corpo para capturar definições internas
        self.visit(node["body"])

        # Sai do escopo da função
        self.symbol_table.pop_scope()
```

## Principais funções do ASTBuilderVisitor

| Função                                                   | Descrição                                                                                       |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `visitInicio`                                            | Ponto de entrada do programa, retorna um nó `Program` com a lista de comandos.                 |
| `visitComandos`                                          | Despacha o tipo de comando (declaração, escrita, leitura, atribuição etc).                     |
| `visitComando_declaracao_funcao`                         | Constrói um nó de declaração de função e registra a função na tabela de símbolos.              |
| `visitComando_declaracao`                                | Constrói um nó de declaração de variável e registra na tabela de símbolos.                     |
| `visitComando_retorno`, `visitComando_ler`, `visitComando_escrever` | Criam nós semânticos correspondentes (`Return`, `Read`, `Write`).                              |
| `visitExpressao`                                         | Analisa expressões aritméticas, literais, chamadas de função e variáveis.                      |
| `visitCondicao`                                          | Tratar operadores relacionais e lógicos.                                                       |
| `visitFunctionDeclaration`                               | Lida com escopos e parâmetros das funções.                                                     |
| `SymbolTable`                                            | Gerencia os escopos da linguagem e resolve símbolos (variáveis, funções).                      |

## Importância no Compilador

Este script é o elo entre o parser e o analisador semântico:
- Ele transforma estruturas detalhadas (Parse Tree) em estruturas compactas e semânticas (AST).
- Já detecta e organiza escopos, algo vital para verificar contextos no código.
- Constrói uma estrutura de dados hierárquica, onde cada parte do programa está representada em formato JSON-like.

## Exemplo da saída gerada (AST simplificada)

Um código como:
```
int main() {
   int x = 10;
   escreve(x);
   retorna x;
}
```
Gera uma estrutura AST como:
```
{
  "type": "Program",
  "body": [
    {
      "type": "FunctionDeclaration",
      "returnType": "int",
      "name": "main",
      "params": [],
      "body": {
        "type": "Block",
        "statements": [
          {
            "type": "VariableDeclaration",
            "varType": "int",
            "name": "x",
            "value": { "type": "IntLiteral", "value": 10 }
          },
          {
            "type": "Write",
            "value": { "type": "Identifier", "name": "x" }
          },
          {
            "type": "Return",
            "value": { "type": "Identifier", "name": "x" }
          }
        ]
      }
    }
  ]
}
```
Essa estrutura é fácil de navegar, analítica e pronta para ser verificada semanticamente.


# SemanticAnalyzer.py

O arquivo SemanticAnalyzer.py é responsável por realizar a Análise Semântica do programa.
Essa etapa acontece após a criação da AST (Árvore Sintática Abstrata) e tem como objetivo verificar se o código faz sentido logicamente, mesmo que esteja sintaticamente correto.

## Em resumo, o SemanticAnalyzer.py:
- Percorre a AST construída pelo ASTBuilderVisitor
- Verifica declarações de variáveis e funções
- Garante que os tipos estejam corretos em expressões, atribuições e retornos
- Confirma o uso de escopos e regras da linguagem
- Armazena os identificadores válidos em uma Tabela de Símbolos
- Gera mensagens de erro semânticas claras e detalhadas

## Exemplo de Erros Semânticos Detectados

- Variável usada antes de ser declarada
- Atribuição de um string para uma variável int
- Função chamada com número incorreto de argumentos
- Função sem return do tipo correto
- Repetição de nomes em parâmetros ou variáveis

# Código

```
from symbol_table import SymbolTable

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        
        self.errors = []
        self.current_function_return_type = None

    def error(self, message, node=None):
        if node and "line" in node and "column" in node:
            message = f"[Linha {node['line']}, Coluna {node['column']}] {message}"
        self.errors.append(message)

    def visit(self, node):
        if not node:
            return None
        method_name = f"visit_{node['type']}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        print(f"[Aviso] Visitador genérico para tipo desconhecido: {node}")

    def visit_Program(self, node):
        for stmt in node["body"]:
            self.visit(stmt)

    def visit_FunctionDeclaration(self, node):
        if self.symbol_table.lookup(node["name"]):
            self.error(f"Função '{node['name']}' já declarada.", node)
        else:
            self.symbol_table.define(node["name"], {
                "type": "function",
                "returnType": node["returnType"],
                "params": node["params"]
            })

        self.symbol_table.push_scope()
        for param in node["params"]:
            if self.symbol_table.lookup(param["name"]):
                self.error(f"Parâmetro '{param['name']}' já declarado na função '{node['name']}'.", param)
            self.symbol_table.define(param["name"], {"type": param["paramType"]})

        self.current_function_return_type = node["returnType"]
        self.visit(node["body"])
        self.symbol_table.pop_scope()

    def visit_Block(self, node):
        self.symbol_table.push_scope()
        for stmt in node["statements"]:
            self.visit(stmt)
        self.symbol_table.pop_scope()

    def visit_VariableDeclaration(self, node):
        if self.symbol_table.lookup(node["name"]):
            self.error(f"Variável '{node['name']}' já declarada.", node)
        else:
            self.symbol_table.define(node["name"], {
                "type": "variable",
                "varType": node["varType"]
            })
        if node["value"]:
            value_type = self.visit(node["value"])
            if value_type and value_type != node["varType"]:
                self.error(f"Tipo incompatível em atribuição à variável '{node['name']}': esperado {node['varType']}, encontrado {value_type}", node)

    def visit_Assignment(self, node):
        var_info = self.symbol_table.lookup(node["target"])
        if not var_info:
            self.error(f"Variável '{node['target']}' não declarada.", node)
        else:
            if var_info["type"] != "variable":
                self.error(f"'{node['target']}' não é uma variável.", node)
            value_type = self.visit(node["value"])
            if value_type and value_type != var_info["varType"]:
                self.error(f"Tipo incompatível em atribuição a '{node['target']}': esperado {var_info['varType']}, encontrado {value_type}", node)

    def visit_Return(self, node):
        value_type = self.visit(node["value"])
        if value_type is None:
            self.error(f"Tipo de retorno inválido: expressão não reconhecida.", node)
        elif self.current_function_return_type != value_type:
            self.error(f"Tipo de retorno incompatível: esperado {self.current_function_return_type}, encontrado {value_type}", node)

    def visit_IfStatement(self, node):
        self.visit(node["condition"])
        self.visit(node["then"])
        if node["else"]:
            self.visit(node["else"])

    def visit_ForStatement(self, node):
        self.symbol_table.push_scope()
        self.visit(node["init"])
        self.visit(node["condition"])
        self.visit(node["increment"])
        self.visit(node["body"])
        self.symbol_table.pop_scope()

    def visit_WhileStatement(self, node):
        self.visit(node["condition"])
        self.visit(node["body"])

    def visit_Read(self, node):
        var_info = self.symbol_table.lookup(node["identifier"])
        if not var_info:
            self.error(f"Variável '{node['identifier']}' não declarada para leitura.", node)

    def visit_Write(self, node):
        if isinstance(node["value"], dict):
            self.visit(node["value"])

    def visit_Increment(self, node):
        var_info = self.symbol_table.lookup(node["target"])
        if not var_info:
            self.error(f"Variável '{node['target']}' não declarada para incremento.", node)

    def visit_Decrement(self, node):
        var_info = self.symbol_table.lookup(node["target"])
        if not var_info:
            self.error(f"Variável '{node['target']}' não declarada para decremento.", node)

    def visit_condicao_binaria(self, node):
        self.visit(node["left"])
        self.visit(node["right"])

    def visit_condicao_logica(self, node):
        self.visit(node["left"])
        self.visit(node["right"])

    def visit_BinaryExpression(self, node):
        left_type = self.visit(node["left"])
        right_type = self.visit(node["right"])

        # Verifica divisão por zero
        if node.get("operator") == "/":
            if node["right"]["type"] in ("IntLiteral", "FloatLiteral") and node["right"]["value"] == 0:
                self.error("Divisão por zero detectada.", node["right"])

        if left_type != right_type:
            self.error(f"Expressão binária com tipos incompatíveis: {left_type} e {right_type}", node)
            return None

        return left_type

    def visit_FunctionCall(self, node):
        func_info = self.symbol_table.lookup(node["name"])
        if not func_info:
            self.error(f"Função '{node['name']}' não declarada.", node)
        else:
            if func_info["type"] != "function":
                self.error(f"'{node['name']}' não é uma função.", node)
            else:
                expected = len(func_info["params"])
                given = len(node["arguments"])
                if expected != given:
                    self.error(f"Função '{node['name']}' chamada com {given} argumentos, mas espera {expected}.", node)
        for arg in node["arguments"]:
            self.visit(arg)

    def visit_Identifier(self, node):
        var_info = self.symbol_table.lookup(node["name"])
        if not var_info:
            self.error(f"Identificador '{node['name']}' não declarado.", node)
            return None
        return var_info.get("varType") or var_info.get("type")

    def visit_IntLiteral(self, node):
        return "int"

    def visit_FloatLiteral(self, node):
        return "float"

    def visit_StringLiteral(self, node):
        return "string"

    def visit_Parameter(self, node):
        pass

    def analyze(self, ast):
        self.visit(ast)
```

## Como ele funciona internamente?

| Componente         | Função                                                                 |
|--------------------|------------------------------------------------------------------------|
| `self.symbol_table`| Gerencia escopos e símbolos (variáveis, funções, parâmetros etc.)      |
| `self.errors`      | Lista de mensagens de erro acumuladas                                  |
| `visit_*()`        | Métodos específicos para cada tipo de nó da AST                        |
| `analyze(ast)`     | Inicia a análise semântica percorrendo toda a AST                      |

## Principais métodos explicados

É aqui que o compilador decide o que pode ou não ser feito com base no significado do código.

Esse script contém a lógica principal da análise semântica. Algumas de suas responsabilidades:

| Método/Função            | O que faz                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------|
| `visit_Program`          | Inicia a análise, percorrendo todos os comandos do programa.                             |
| `visit_FunctionDeclaration` | Registra a função, analisa seus parâmetros e corpo, criando escopos.                   |
| `visit_Block`            | Cria novo escopo e analisa cada comando dentro do bloco.                                 |
| `visit_VariableDeclaration` | Verifica se a variável já foi declarada, define tipo e valor inicial.                 |
| `visit_Assignment`       | Garante que a variável foi declarada e que o tipo atribuído é compatível.                |
| `visit_IfStatement`      | Analisa a condição e os blocos então e senão, se existirem.                              |
| `visit_Return`           | Verifica se o tipo de retorno está compatível com o tipo da função atual.                |
| `visit_FunctionCall`     | Valida se a função existe, se está sendo chamada corretamente e com o número correto de argumentos. |
| `visit_BinaryExpression` | Verifica compatibilidade de tipos e detecta divisão por zero.                            |
| `visit_Identifier`       | Verifica se o identificador (variável) foi declarado previamente.                         |

## Exemplo de fluxo da análise semântica:

```
visitor = ASTBuilderVisitor()
ast = visitor.visit(tree)

analisador = SemanticAnalyzer()
analisador.analyze(ast)

for erro in analisador.errors:
    print(erro)
```

Se houver erros, eles serão listados com informações como:

```
[Linha 12, Coluna 5] Variável 'total' usada antes de ser declarada.
[Linha 20, Coluna 10] Tipo incompatível em atribuição: esperado int, encontrado string
```

# SymbolTable.py

A SymbolTable (Tabela de Símbolos) é uma estrutura fundamental na análise semântica de um compilador.
Ela serve para armazenar e gerenciar informações sobre identificadores do programa, como variáveis, funções e parâmetros — incluindo seus nomes, tipos e escopos.

# O que essa implementação faz?

Essa versão da SymbolTable trabalha com escopos empilhados, permitindo que o compilador reconheça:
- Variáveis locais e globais
- Parâmetros de funções
- Ocultação de variáveis (shadowing)
- Fim de escopos (como fim de blocos {} ou funções)

# Código de SymbolTable.py
```
class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()

    def define(self, name, info):
        self.scopes[-1][name] = info

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

```

# Explicação dos métodos

| Método         | Função                                                                 |
|----------------|------------------------------------------------------------------------|
| `__init__()`   | Inicializa com uma pilha de escopos, começando pelo escopo global.     |
| `push_scope()` | Adiciona um novo escopo (ex: quando entra em uma função ou bloco).     |
| `pop_scope()`  | Remove o escopo atual (ex: ao sair de uma função/bloco).               |
| `define(name, info)` | Define (declara) um símbolo no escopo atual. Ex: `int x = 10;`   |
| `lookup(name)` | Busca um símbolo de forma hierárquica, do escopo mais interno para o mais externo. |

## Como funciona internamente

```
self.scopes = [{}]
```
1. self.scopes é uma lista de dicionários, onde cada dicionário representa um escopo.
2. O último item da lista representa o escopo atual.

Por exemplo:
```
[
  {"x": {"type": "int"}},             # escopo global
  {"x": {"type": "string"}}           # escopo atual (local)
]
```
Se x for procurado com lookup("x"), ele retorna a versão mais interna.

Exemplo prático

Suponha o código:
```
int x = 10;
void funcao() {
    int x = 20;
    escreve(x); // <- usa o x local
}
```
A SymbolTable vai funcionar assim:
	1.	No escopo global: define x = 10
	2.	Ao entrar em funcao(): push_scope() cria novo escopo
	3.	Define x = 20 localmente
	4.	lookup("x") encontra primeiro o x local
	5.	Ao sair da função: pop_scope() remove o escopo local

## Exemplo de uso típico

```
tabela = SymbolTable()
tabela.define("x", {"type": "int"})
print(tabela.lookup("x"))  # {'type': 'int'}

tabela.push_scope()
tabela.define("x", {"type": "string"})
print(tabela.lookup("x"))  # {'type': 'string'}

tabela.pop_scope()
print(tabela.lookup("x"))  # {'type': 'int'}
```



