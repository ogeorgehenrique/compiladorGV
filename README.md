# 🚀 CompiladorGV

Projeto acadêmico desenvolvido para a disciplina de **Compiladores (2025/1)**.

Este repositório contém o desenvolvimento de um **compilador** para uma linguagem de programação **inspirada em C e PASCAL**, com sintaxe simplificada e palavras-chave em português.

---

## 📚 Descrição do Projeto

O **CompiladorGV** realiza as etapas de análise léxica e sintática utilizando **ANTLR4** e gera a árvore sintática (AST) dos programas escritos na linguagem.

A linguagem implementada é capaz de manipular:

- Tipos primitivos (`int`, `string`)
- Entrada e saída de dados (`leia()`, `escreva()`)
- Controle de fluxo (`se`, `senao`, `para`, `enquanto`)
- Declaração e chamada de funções (`int soma(int a, int b) { retorna a+b; }`)
- Expressões aritméticas e lógicas
- Retorno de valores com `retorna`
- Geração de ASTs para visualização (Graphviz)

---

## 🛠 Funcionalidades Implementadas

- 📖 **Declaração de Variáveis:**  
  `int x = 10;`, `string nome = "GeorgeLindao";`
  
- 🔢 **Expressões Aritméticas e Lógicas:**  
  `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`

- 🧠 **Controle de Fluxo:**  
  `se (...) {}`, `senao {}`, `para (...) {}`, `enquanto (...) {}`

- 📥 **Entrada e Saída:**  
  `leia(x);`, `escreva("Texto");`, `escreva(x + 1);`

- 🧩 **Declaração e Chamada de Funções:**  
  `int soma(int a, int b) { retorna a+b; }`  
  `soma(2, 3);`

- 🔁 **Retorno de Funções:**  
  `retorna resultado;`

- 🌳 **Geração de Árvore Sintática (AST)**

---

## 📦 Estrutura do Projeto
```bash
CompiladorGV/
├── README.md
├── grammar/
│   └── CompiladorGV.g4             # Gramática ANTLR
├── src/
│   ├── scanner.py                  # Analisador Léxico
│   ├── parser.py                   # Analisador Sintático
│   └── ast_generator.py (opcional) # AST Generator
├── exemplos/
│   ├── triangulo_pascal.txt        # Exemplo de programa
│   ├── classificacao_triangulo.txt # Exemplo de programa
├── docs/
│   ├── ASTs/
│   └── Relatorio_Compilador.pdf
├── .gitignore
└── LICENSE (opcional)
```
---


## 🚀 Como Executar

### 1. Instalar dependências

- [Python 3.x](https://www.python.org/) (ou Java)
- [ANTLR 4](https://www.antlr.org/)
- [Graphviz](https://graphviz.gitlab.io/)

### 2. Gerar os arquivos do ANTLR

```bash
# Exemplo em Python
antlr4 -Dlanguage=Python3 -o src/ grammar/CompiladorGV.g4

📋 Programas de Teste
	•	Triângulo de Pascal:
Imprime as linhas do triângulo de Pascal até n linhas.
	•	Classificação de Triângulos:
Lê três lados e classifica como equilátero, isósceles ou escaleno.

⸻

📄 Licença

Projeto acadêmico de uso livre para fins educacionais.

⸻

✍️ Autor

