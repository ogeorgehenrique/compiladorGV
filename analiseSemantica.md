# Etapa 4: Análise Semântica

A etapa de análise semântica é a terceira fase lógica do processo de compilação (após a análise léxica e sintática). Ela é responsável por verificar o significado do código, assegurando que as instruções seguem as regras de coerência da linguagem, mesmo que estejam sintaticamente corretas.
A análise semântica ocorre após a análise sintática. Enquanto o parser **(CompiladorGVParser + MyParserErrorListener)** e o ParseTreeGenerator cuidam da estrutura gramatical e erros como execução da regra inicio(), a análise semântica atua sobre a estrutura lógica e de significado do código.

#Objetivo da Análise Semântica

Enquanto a análise sintática verifica a estrutura do código, a análise semântica verifica se o código faz sentido. Alguns exemplos de erros semânticos:
- Uso de variáveis não declaradas
- Declaração duplicada de variáveis
- Tipos incompatíveis em expressões (ex: int + string)
- Retorno incorreto em funções
- Uso de funções ou procedimentos com parâmetros inválidos

# Componentes envolvidos na análise semântica

| Arquivo/Classe           | Função                                                                 |
|--------------------------|------------------------------------------------------------------------|
| `compila.py`              | Dispara a análise semântica após a análise sintática.                  |
| `ASTBuilderVisitor.py`   | Constrói a Árvore Sintática Abstrata (AST) com base na árvore de derivação. |
| `SemanticAnalyzer.py`    | Percorre a AST realizando todas as validações semânticas.              |
| `CompiladorGV.g4`        | Define as regras sintáticas que geram os contextos para a AST.         |

# Como Funciona?

A análise semântica acontece depois que o código-fonte já passou pela análise léxica e sintática.

## 1. Construção da AST

O ASTBuilderVisitor é um visitante que transforma a árvore de derivação (Parse Tree) produzida pelo ANTLR em uma Árvore Sintática Abstrata (AST) simplificada, que representa apenas as estruturas relevantes do programa.
```
visitor = ASTBuilderVisitor()
ast = visitor.visit(tree)
```
Essa AST é usada porque contém apenas as informações essenciais (sem símbolos, parênteses, etc.), facilitando a análise semântica.


## 2. Execução da Análise Semântica

O SemanticAnalyzer percorre a AST e verifica, por exemplo:
- Se todas as variáveis foram declaradas antes de serem usadas
- Se os tipos de dados são coerentes nas atribuições
- Se funções têm retorno adequado
- Se escopos estão bem definidos
- Se comandos como retorna aparecem dentro de funções

```
analisador = SemanticAnalyzer()
analisador.visit(ast)
```
Caso ocorra algum erro, mensagens amigáveis são exibidas informando a linha, coluna e natureza do erro, como:
```
ERRO SEMÂNTICO [Linha 5]: Variável 'contador' usada antes de ser declarada.
```

# Importância dessa etapa

A análise semântica garante que o código não apenas parece correto, mas que faz sentido dentro da lógica da linguagem. Sem essa etapa, seria possível compilar programas que resultariam em comportamentos errados, ambiguidades ou falhas em tempo de execução.

Essa etapa é também onde o compilador começa a “entender” o que o código realmente significa, e não apenas como ele está escrito.


# Entendendo a estrutura do código

Nesta etapa, os principais arquivos envolvidos são:

## 1. ASTBuilderVisitor.py

Este script é responsável por:
- Traduzir a árvore sintática bruta em uma AST compacta.
- Criar nós específicos (como Função, Variável, Atribuição, Expressão).
- Eliminar tokens e estruturas intermediárias desnecessárias para a análise.

Esse visitante é mais semântico do que sintático: ele constrói a intenção do programa.


## 2. SemanticAnalyzer.py

Este é o cérebro da análise semântica:
- Percorre a AST node por node.
- Verifica regras de contexto (ex: escopo de variáveis).
- Monta uma tabela de símbolos.
- Dispara mensagens de erro quando alguma regra da linguagem é quebrada.

É aqui que o compilador decide o que pode ou não ser feito com base no significado do código.

**Exemplo de Fluxo Completo**
```
visitor = ASTBuilderVisitor()
ast = visitor.visit(tree)

analisador = SemanticAnalyzer()
analisador.visit(ast)
```
Se não houver erros, o programa prossegue para a geração de código intermediário (TAC). Caso contrário, a análise é interrompida e os erros são exibidos com clareza.





