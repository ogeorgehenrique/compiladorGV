#Etapa 2: Analisador Léxico

O arquivo scanner.py implementa a primeira fase da compilação, chamada análise léxica, responsável por quebrar o código-fonte em unidades léxicas (tokens). Esta etapa é crucial para preparar o código para a análise sintática.

⸻

# Objetivo da análise léxica

Transformar o código-fonte bruto (texto) em uma sequência de tokens, que são unidades significativas da linguagem, como:
- Identificadores (x, main, contador)
- Palavras-chave (int, retorna, se)
- Operadores (+, =, ==)
	•	símbolos (;, {, })
	•	literais ("texto", 42, 3.14)

Componentes envolvidos na análise léxica

| Arquivo/Classe               | Função                                                                 |
|-----------------------------|------------------------------------------------------------------------|
| `CompiladorGVLexer.g4`      | Arquivo de gramática léxica usado pelo ANTLR para gerar o `CompiladorGVLexer`. |
| `CompiladorGVLexer.py`      | Gerado automaticamente pelo ANTLR a partir da gramática `.g4`.        |
| `scanner.py`                | Script principal que executa a análise léxica.                         |
| `CommonTokenStream` (ANTLR4)| Estrutura de dados que armazena os tokens extraídos.                  |
| `MyLexerErrorListener.py` (opcional) | (Se usado) Define um ouvinte personalizado para lidar com erros léxicos de forma amigável. |

Funcionamento detalhado

1. 📥 Leitura do arquivo-fonte

O scanner.py recebe o caminho de um arquivo de código-fonte como argumento, e o lê usando o FileStream, transformando-o em um stream de caracteres UTF-8.

```
input_stream = FileStream(argv[1], encoding='utf-8')
```

2. 🧾 Tokenização via Lexer (CompiladorGVLexer)

Esse texto é passado para o CompiladorGVLexer, classe gerada automaticamente pelo ANTLR a partir da gramática .g4. Ela aplica as regras léxicas e identifica os tokens válidos.

```
lexer = CompiladorGVLexer(input_stream)
```

3. 🧹 Coleta dos tokens via CommonTokenStream

O resultado é encapsulado em um CommonTokenStream, que é uma lista ordenada de tokens que pode ser passada para o parser posteriormente.

```
tokens = CommonTokenStream(lexer)
```

4. 📤 Impressão formatada dos tokens

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

5. 🚨 Tratamento de erros léxicos (se implementado)

Se o código conter símbolos inválidos (ex: @, #, &), o lexer pode disparar um erro. Caso você implemente um MyLexerErrorListener, ele pode interceptar esses erros e mostrar mensagens personalizadas, como:

```
ERRO LÉXICO [Linha 1, Coluna 5]: Símbolo '@' não reconhecido pela linguagem.
```

# Importância dessa etapa

A análise léxica é a base de todo o processo de compilação. Ela garante que os símbolos do código estão corretos, respeitam a sintaxe da linguagem e são compreensíveis para as etapas seguintes (sintática, semântica, etc). Um erro aqui impede qualquer análise posterior.