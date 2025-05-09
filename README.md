# 🚀 CompiladorGV - Projeto acadêmico da disciplina de Compiladores (2025/1)
Este repositório apresenta o desenvolvimento de um compilador educacional para uma linguagem de programação de sintaxe simplificada, inspirada nas linguagens C e Pascal, com palavras-chave em português. 
O compilador foi implementado em Python utilizando a ferramenta ANTLR4, e é capaz de simular construções fundamentais de linguagens estruturadas, como declaração de variáveis, estruturas de controle, funções e análise léxica e sintática.

---
## ✨ Visão Geral
O **CompiladorGV** é um projeto acadêmico completo que implementa:

- Scanner (analisador léxico)
- Parser (analisador sintático)
- Geração de Árvore Sintática (AST)
- Suporte a estruturas de controle (`if`, `else`, `while`, `for`)
- Declaração e chamada de funções
- Tipos primitivos (`int`, `string`)
- Saída com mensagens de erro **coloridas e amigáveis**
---
## 🌐 Estrutura de Pastas
```bash
compiladorGV/
├── antlr-4.13.1-complete.jar     # Ferramenta ANTLR
├── grammar/                      # Gramática (.g4) e arquivos gerados
│   ├── CompiladorGV.g4           # Sua gramática principal
│   ├── scanner.py                # Scanner léxico
│   ├── parser.py                 # Parser sintático e gerador de AST
│   ├── MyLexerErrorListener.py
│   ├── MyParserErrorListener.py
│   ├── ParseTreeGenerator.py     # Gera .dot da AST completa
├── exemplos/                     # Testes de programas fonte
│   ├── programa_teste.txt
│   ├── triangulo_pascal.txt
│   └── classificacao_triangulo.txt
├── saida_ast.dot                 # Arquivo .dot gerado pelo parser
├── saida_ast.png                 # Imagem da AST (Graphviz)
├── README.md
```
---
## ⚙️ Recursos Suportados pela Gramática

### ✍️ Declarações
```
int x = 0;
string nome = "George";
```
### ⚖️ Expressões matemáticas e relacionais
```
y = x + 1;
x = a * (b + c);
se (x > 0 && y != 3) { ... }
```
### ⚡ Comandos de controle
```
se (condicao) { ... } senao { ... }
senao se (...) { ... }
para(i = 0; i < n; i = i + 1) { ... }
enquanto(x > 0) { ... }
```
### 🔎 Funções
```
int soma(int a, int b) {
    retorna a + b;
}

int main() {
    int total = soma(2, 3);
    retorna 0;
}
```
### 🔹 Escrita e leitura
```
escreva("Resultado:");
leia(x);
```
---
# 🎨 AST Visual

Após rodar o parser.py, você pode gerar a imagem da AST com:
```
dot -Tpng saida_ast.dot -o saida_ast.png
```
Exemplo de estrutura:
```
inicio
 └── funcao
     ├── tipo: int
     ├── nome: main
     └── bloco
         ├── escreva
         └── retorna
```
---
# 🔐 Mensagens de erro personalizadas

As mensagens de erro agora são:
- Coloridas (vermelho)
- Com linha e coluna
- Com texto amigável

Exemplos:
```
ERRO LÉXICO [Linha 2, Coluna 14]: Símbolo '#' inválido.
ERRO SINTÁTICO [Linha 5, Coluna 12]: Esperado ';' após 'retorna'
```
---
# 📚 Exemplos implementados:
	• teste.txt: exemplo básico com escrita e retorno
 	• programa_teste.txt: exemplo básico com atribuição e chamadas de funções
	• triangulo_pascal.txt: usando para, expressões e condições para imprimir o triângulo de Pascal
	• classificacao_triangulo.txt: uso de se, senao se, expressões lógicas e chamadas de função
 ---
 # 🔍 scanner.py — Analisador Léxico
O arquivo scanner.py é responsável pela análise léxica do código-fonte da linguagem. Ele utiliza o lexer gerado pelo ANTLR4 a partir da gramática definida (CompiladorGVLexer) para transformar o código em uma sequência de tokens, que são unidades mínimas da linguagem (como identificadores, palavras-chave, operadores, etc).
## 🔧 Funcionamento
1.	Leitura do arquivo: Recebe o caminho de um arquivo como argumento e o lê como uma stream de texto.
2.	Tokenização: O lexer processa o texto e identifica os tokens válidos, conforme a gramática da linguagem.
3.	Saída formatada: Exibe os tokens no terminal no formato <Tipo, 'Lexema', Linha, Coluna>, facilitando a análise visual do código.
4.	Tratamento de erros: Caso ocorra algum erro inesperado durante a análise, o programa imprime a mensagem de erro e encerra a execução.

Este script é uma etapa fundamental da cadeia de compilação, pois valida se os símbolos usados no código são reconhecidos pela linguagem antes de passar para a análise sintática.

---
# 📘 parser.py — Analisador Sintático
O arquivo parser.py é responsável pela análise sintática do código-fonte. Ele verifica se a sequência de tokens (gerada pelo scanner) está de acordo com as regras gramaticais definidas na linguagem, além de gerar uma árvore de derivação (AST) para representar a estrutura hierárquica do código.
## 🧠 Funcionamento
1.	Leitura do código: O arquivo-fonte é lido e convertido em tokens pelo CompiladorGVLexer.
2.	Parser e tratamento de erros:
3.	Um analisador sintático (CompiladorGVParser) processa os tokens.
4.	Listeners padrões de erro do ANTLR são removidos e substituídos por um listener customizado (MyParserErrorListener) que exibe mensagens de erro mais amigáveis.
5.	Geração da AST:
6.	A árvore sintática é visitada pelo ParseTreeGenerator, um visitante personalizado que percorre os nós da árvore.
7.	O resultado é salvo no arquivo saida_ast.dot, que pode ser visualizado como um grafo representando a estrutura do código.
8.	Mensagens finais:
9.	Se o código estiver sintaticamente correto, o script exibe mensagens de sucesso.
10.	Em caso de erro, uma mensagem vermelha é exibida e a execução é encerrada.

Este script garante que o programa esteja corretamente estruturado antes de seguir para etapas mais avançadas da compilação.

---
 # 🚀 Como executar
 ```
# Rodar scanner:
python3 src/grammar/scanner.py exemplos/arquivo.txt

# Rodar parser e gerar AST:
python3 src/grammar/parser.py exemplos/arquivo.txt

# Rodas o programa completo (parser e scanner)
python3 src/grammar/executar_compilador.py exemplos/teste.txt

# Gerar imagem da árvore:
dot -Tpng saida_ast.dot -o saida_ast.png
```
---
# 📊 Status do Projeto
	•	Scanner com erros coloridos
	•	Parser com mensagens sintáticas amigáveis
	•	AST textual e visual com Graphviz
	•	Suporte a funções, laços, condicionais e expressões
	•	Pronto para ser apresentado ou expandido com semântica/intermediário
