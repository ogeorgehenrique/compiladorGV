# 🚀 CompiladorGV
**Projeto acadêmico da disciplina de Compiladores (2025/1).** Este repositório apresenta o desenvolvimento de um compilador educacional para uma linguagem de programação de sintaxe simplificada, inspirada nas linguagens C e Pascal, com palavras-chave em português.
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
│   ├── ParseTreeGenerator.py    # Gera .dot da AST completa
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
	•	Coloridas (vermelho)
	•	Com linha e coluna
	•	Com texto amigável
Exemplos:
```
ERRO LÉXICO [Linha 2, Coluna 14]: Símbolo '#' inválido.
ERRO SINTÁTICO [Linha 5, Coluna 12]: Esperado ';' após 'retorna'
```
---
# 📚 Exemplos implementados:
	•	programa_teste.txt: exemplo básico com escrita e retorno
	•	triangulo_pascal.txt: usando para, expressões e condições para imprimir o triângulo de Pascal
	•	classificacao_triangulo.txt: uso de se, senao se, expressões lógicas e chamadas de função
 ---
 # 🚀 Como executar
 ```
# Rodar scanner:
python3 src/grammar/scanner.py exemplos/arquivo.txt

# Rodar parser e gerar AST:
python3 src/grammar/parser.py exemplos/arquivo.txt

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
