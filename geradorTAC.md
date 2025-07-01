# Geração de Código Intermediário TAC
Etapa 3 – Geração de Código Intermediário (TAC)
- Criar uma classe TACGenerator que visita a AST (sua árvore sintática abstrata).
- Utilizar padrão visitor (como você já fez com ParseTreeGenerator).
- Implementar a geração de instruções de três endereços.
- Criar representações para:
- Operandos (TAC_Operand) → variáveis, temporários _t0, _t1, etc.
- Instruções (TAC_Instruction) → ex: ADD _t0, a, b
- Adicionar suporte a expressões, atribuições, condições, laços e funções.
- Adicionar suporte a etiquetas (labels): L0:, L1:, etc.
- Habilitar geração com flag --gerar-tac.
- Salvar tudo em um arquivo exemplo.tac.

## O que é TAC? Conceito e Objetivo

Definição

TAC (Three Address Code) é uma forma de representação intermediária entre o código fonte e o código de máquina. Cada instrução do TAC realiza no máximo uma operação e trabalha, geralmente, com três operandos: dois de entrada e um de saída.

Por que usar TAC?
- Independência da máquina: Não é ligado à arquitetura física do processador.
- Facilidade de otimização: É muito mais simples aplicar otimizações nesta forma intermediária.
- Base para geração de código final: Pode ser traduzido para LLVM IR, Assembly, bytecode, etc.

Exemplo simples:

Código em C:
```
int x = (a + b) * (c - d);
```
Em Tac:
```
_t1 = a + b
_t2 = c - d
x = _t1 * _t2
```
## Anatomia de uma Instrução TAC

Cada instrução no TAC segue a estrutura:
```
resultado = operando1 operador operando2
```
ou seja:
```
dest = arg1 op arg2
```
Tipos de instruções comuns:

| Tipo               | Exemplo TAC        | Significado                                 |
|--------------------|--------------------|---------------------------------------------|
| Atribuição simples | `x = a`            | Atribui valor de `a` a `x`                  |
| Aritmética         | `_t1 = a + b`      | Soma `a` e `b` e guarda em `_t1`           |
| Comparação         | `_t2 = a < b`      | Resultado é `1` (true) ou `0` (false)       |
| Condicional        | `if _t2 goto L0`   | Vai para `L0` se `_t2` for verdadeiro       |
| Incondicional      | `goto L1`          | Vai para `L1` diretamente                   |
| Chamada de função  | `param x / t0 = call f` | Empilha argumentos e chama função     |
| Retorno            | `return x`         | Retorna valor `x`                           |


## 1. TAC_Operand.py
A classe **TAC_Operand** representa um operando individual dentro de uma instrução de código intermediário (TAC). Ela abstrai “quem” ou “o que” está participando de uma operação, atribuição, condição ou chamada.

Pense nela como o “peão” que pode ser uma variável, constante, temporário ou até mesmo um rótulo (label) de controle de fluxo.
```
class TAC_Operand:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # 'var', 'temp', 'const', 'label'
        self.valor = valor

    def __str__(self):
        return str(self.valor)
```
**Detalhamento dos Componentes**

**1. self.tipo**

Este atributo indica o tipo de operando, ou seja, o que ele representa na TAC. Os valores possíveis são:
| Tipo    | Significado                                | Exemplo        |
|---------|--------------------------------------------|----------------|
| `var`   | Variável definida pelo usuário             | `x`, `total`   |
| `temp`  | Variável temporária (gerada internamente)  | `_t0`, `_t1`   |
| `const` | Constante literal (número ou string)       | `5`, `"oi"`    |
| `label` | Rótulo usado para saltos condicionais/incondicionais | `L0`, `L1` |

**2. self.valor**

Esse atributo guarda o valor literal ou identificador usado na instrução TAC.

Exemplos:
- Se tipo = 'var', então valor = 'x'
- Se tipo = 'temp', então valor = '_t0'
- Se tipo = 'const', então valor = '5'

**3. Metódo __str __**

A função __str __ define como esse objeto será impresso como string quando usado em print() ou dentro de outras instruções.
```
def __str__(self):
    return str(self.valor)
```
Essa função faz com que, ao imprimir um TAC_Operand, o que apareça seja apenas o valor (e não o tipo).

**Exemplos de uso:**


Imagine uma instrução TAC assim:
```
_t0 = a + b
```
Ela será representada como:
```
TAC_Instruction('+', dest=_t0, arg1=a, arg2=b)
```
Onde:
```
arg1 = TAC_Operand('var', 'a')
arg2 = TAC_Operand('var', 'b')
dest = TAC_Operand('temp', '_t0')
```
- Em Atrubuições:
```
x = 5
```
```
TAC_Instruction('=', TAC_Operand('var', 'x'), TAC_Operand('const', 5))
```
- Em expressões Aritméticas:
```
_t0 = x + y
```
```
TAC_Instruction('+', TAC_Operand('temp', '_t0'), TAC_Operand('var', 'x'), TAC_Operand('var', 'y'))
```
- Em controle de Fluxo:
```
if _t1 goto L1
```
```
TAC_Instruction('if_goto', dest=TAC_Operand('label', 'L1'), arg1=TAC_Operand('temp', '_t1'))
```

## 2. TAC_Instruction.py
A classe **TAC_Instruction** representa uma única instrução de código intermediário no formato TAC (Three Address Code).
Ela é a unidade básica que modela operações como:
- Atribuições
- Expressões aritméticas
- Comparações
- Saltos condicionais/incondicionais
- Chamadas de função
- Retornos

É como uma “linha” em uma linguagem de montagem intermediária!
Ela segue o formato Three Address Code (TAC):
```
x = y op z
```
- x → resultado (destino)
- y, z → operandos (variáveis, temporários, constantes)
- op → operador (aritmético, relacional, lógico, controle)

A TAC_Instruction modela o que acontece na TAC, com até três endereços `(dest, arg1, arg2)`
```
class TAC_Instruction:
    def __init__(self, op, dest=None, arg1=None, arg2=None):
        self.op = op            # operador (ex: '+', '-', '=', 'if_goto')
        self.dest = dest        # destino (pode ser um temp, var ou label)
        self.arg1 = arg1        # primeiro argumento
        self.arg2 = arg2        # segundo argumento (pode ser None)
    
    def __str__(self):
        if self.op == "label":
            return f"{self.dest}:"
        elif self.op == "goto":
            return f"goto {self.dest}"
        elif self.op == "if_goto":
            return f"if {self.arg1} goto {self.dest}"
        elif self.op == "return":
            return f"return {self.arg1}" if self.arg1 else "return"
        elif self.op == "call":
            # Caso com retorno: _t0 = call func
            if self.dest:
                return f"{self.dest} = call {self.arg1}"
            # Caso sem retorno: call func
            else:
                return f"call {self.arg1}"
        elif self.op == "param":
            return f"param {self.arg1}"
        elif self.op == "=":
            return f"{self.dest} = {self.arg1}"
        elif self.arg1 and self.arg2:
            return f"{self.dest} = {self.arg1} {self.op} {self.arg2}"
        elif self.arg1 and self.dest:
            return f"{self.dest} = {self.op} {self.arg1}"
        elif self.dest and not self.arg1 and not self.arg2:
            return f"{self.op} {self.dest}"
        elif self.op == "if_false":
            return f"ifFalse {self.arg1} goto {self.dest}"
        else:
            return f"{self.op}"
```
**Detalhamento dos Componentes**
- op: objeto que representa a operação (+, call, goto)
- dest: onde o resultado será armazenado (ou o destino de um salto)
- arg1 e arg2: operandos usados na operação

| Atributo | Descrição                                                                 |
|----------|---------------------------------------------------------------------------|
| `op`     | Operação ou instrução: `'='`, `'+'`, `'goto'`, `'return'`, etc            |
| `dest`   | O local onde o resultado será armazenado (ex: uma variável, temporário ou rótulo) |
| `arg1`   | Primeiro operando (ex: variável, temporário ou constante)                 |
| `arg2`   | Segundo operando (opcional)                                               |

**Dicionário**

Aqui está uma tabela completa com explicação semântica e exemplos de uso real para cada tipo de instrução TAC:
| Palavra-chave (`op`) | Significado                    | Descrição Técnica                                                             | Exemplo TAC            |
|----------------------|--------------------------------|-------------------------------------------------------------------------------|------------------------|
| `=`                  | Atribuição simples             | Copia valor de `arg1` para `dest`                                            | `x = y`                |
| `+`, `-`, `*`, `/`   | Operações aritméticas          | Executa operação entre `arg1` e `arg2` e armazena em `dest`                  | `_t0 = a + b`          |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | Operadores relacionais       | Compara `arg1` e `arg2`, resultado (`0` ou `1`) vai para `dest`             | `_t1 = x < y`          |
| `&&`, `\|\|`         | Operadores lógicos             | Aplica operação lógica entre `arg1` e `arg2`, resultado vai para `dest`     | `_t2 = a && b`         |
| `label`              | Rótulo (marcador de posição)   | Marca uma posição no código para saltos                                     | `L0:`                  |
| `goto`               | Salto incondicional            | Pula diretamente para um `label`                                             | `goto L1`              |
| `if_goto`            | Salto condicional (positivo)   | Se `arg1` for verdadeiro (≠ 0), salta para `dest`                            | `if _t3 goto L2`       |
| `ifFalse`            | Salto condicional (negativo)   | Se `arg1` for falso (== 0), salta para `dest`                                | `ifFalse _t4 goto L3`  |
| `param`              | Passagem de parâmetro          | Enfileira um argumento antes de chamar uma função                            | `param x`              |
| `call`               | Chamada de função              | Chama uma função; o resultado vai para `dest` (se houver)                    | `_t5 = call soma`      |
| `return`             | Retorno de função              | Encerra a função, possivelmente com valor de retorno                         | `return _t5`           |

**Metódo __str __**
Este método é o responsável por transformar a TAC_Instruction em uma linha textual que será escrita no arquivo .tac.
```
TAC_Instruction('+', dest="_t0", arg1="a", arg2="b")
→ str() → "_t0 = a + b"
```
Aqui está uma tabela completa com explicação semântica e exemplos de uso real para cada tipo de instrução TAC:
| Operação       | Formato Gerado                  | Exemplo              |
|----------------|----------------------------------|----------------------|
| `label`        | `dest:`                          | `L1:`                |
| `goto`         | `goto dest`                      | `goto L1`            |
| `if_goto`      | `if arg1 goto dest`              | `if _t0 goto L1`     |
| `ifFalse`      | `ifFalse arg1 goto dest`         | `ifFalse _t1 goto L2`|
| `return`       | `return arg1` (ou só `return`)   | `return _t2`         |
| `call`         | `dest = call func` ou `call func`| `_t1 = call soma`    |
| `param`        | `param arg1`                     | `param _t0`          |
| `=`            | `dest = arg1`                    | `x = 5`              |
| Binária        | `dest = arg1 op arg2`            | `_t0 = x + y`        |
| Unária/Invert  | `dest = op arg1`                 | `_t1 = - x`          |

**Exemplos de uso:**
- Atribuição Simples
```
x = 5
→ TAC_Instruction('=', dest=var_x, arg1=const_5)
→ Saída: x = 5
```
-  Operação Aritmética
```
→ TAC_Instruction('+', dest=_t0, arg1=a, arg2=b)
→ Saída: _t0 = a + b
```
-  Comparação
```
→ TAC_Instruction('<', dest=_t1, arg1=a, arg2=b)
→ Saída: _t1 = a < b
```
-  Salto Condicional
```
→ TAC_Instruction('if_goto', dest=L0, arg1=_t1)
→ Saída: if _t1 goto L0
```
- Salto com Negação (ifFalse)
```
→ TAC_Instruction('if_false', dest=L1, arg1=_t1)
→ Saída: ifFalse _t1 goto L1
```
- Função
```
param x
call soma
→ param x
→ call soma

_t0 = call soma
→ _t0 = call soma
```
**Relação com TAC_Operand**

Todos os arg1, arg2, e dest são geralmente instâncias de TAC_Operand, o que permite manter consistência de tipos e uso.
```
TAC_Instruction('+',
    dest=TAC_Operand('temp', '_t0'),
    arg1=TAC_Operand('var', 'x'),
    arg2=TAC_Operand('const', '1')
)
→ _t0 = x + 1
```
## 3. TACGenerator.py
É a peça central responsável por transformar sua AST (árvore sintática) em TAC (Three-Address Code), ou seja, o código intermediário do seu compilador. 
A TACGenerator é uma visita orientada à árvore gerada pelo parser, com o objetivo de produzir um conjunto de instruções intermediárias (TAC) que serão utilizadas para posterior geração de código de máquina ou código final (Assembly, LLVM IR, etc).

Ela herda de CompiladorGVVisitor, o que significa que ela implementa métodos visitX() que são chamados automaticamente ao percorrer a árvore gerada pela gramática ANTLR.

**1. def __init __(self):**
- self.instrucoes

Lista onde as instruções TAC geradas são armazenadas. Cada uma é uma instância de TAC_Instruction.

- self.temp_counter / self.label_counter

Contadores que garantem a criação de temporários e rótulos (labels) únicos: `_t0, _t1, _t2, ... L0, L1, L2, ...`
