# Geração de Código Intermediário TAC

## O que é TAC? Conceito e Objetivo

Definição

TAC (Three Address Code) é uma forma de representação intermediária entre o código fonte e o código de máquina. Cada instrução do TAC realiza no máximo uma operação e trabalha, geralmente, com três operandos: dois de entrada e um de saída.

Por que usar TAC?
- Independência da máquina: Não é ligado à arquitetura física do processador.
- Facilidade de otimização: É muito mais simples aplicar otimizações nesta forma intermediária.
- Base para geração de código final: Pode ser traduzido para Assembly, bytecode, etc.

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

1. self.tipo

Este atributo indica o tipo de operando, ou seja, o que ele representa na TAC. Os valores possíveis são:
| Tipo    | Significado                                | Exemplo        |
|---------|--------------------------------------------|----------------|
| `var`   | Variável definida pelo usuário             | `x`, `total`   |
| `temp`  | Variável temporária (gerada internamente)  | `_t0`, `_t1`   |
| `const` | Constante literal (número ou string)       | `5`, `"oi"`    |
| `label` | Rótulo usado para saltos condicionais/incondicionais | `L0`, `L1` |

2. self.valor

Esse atributo guarda o valor literal ou identificador usado na instrução TAC.

Exemplos:
- Se tipo = 'var', então valor = 'x'
- Se tipo = 'temp', então valor = '_t0'
- Se tipo = 'const', então valor = '5'

3. __str __
A função __str __ define como esse objeto será impresso como string quando usado em print() ou dentro de outras instruções.
```
def __str__(self):
    return str(self.valor)
```
Essa função faz com que, ao imprimir um TAC_Operand, o que apareça seja apenas o valor (e não o tipo).

Como funciona:
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












Essa classe representa qualquer operando de uma instrução TAC:
- var: nome de variável (ex: x)
- temp: temporário gerado automaticamente (_t0, _t1, …)
- const: constantes literais (5, "texto")
- label: etiquetas de desvio (L0, L1, …)

 2. TAC_Instruction.py
O que faz:

Modela uma única instrução do TAC, como:
	•	t1 = a + b
	•	x = t1
	•	goto L0
	•	if t2 goto L1
	•	L0:

É flexível para lidar com operações aritméticas, condicionais, saltos e atribuições.

3. TACGenerator.py
    
