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

Este é o construtor da classe TACGenerator. Em Python, o método **__init __** é automaticamente chamado quando uma nova instância da classe é criada. Ele serve para inicializar os atributos da instância. 
```
  def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0
        self.instrucoes = []
```
-   self.temp_counter = 0

Cria e inicializa o contador de temporários com zero, para que durante a geração de código intermediário (TAC), quando temos expressões como: `a = b + c * d`é necessário usar de variáveis temporárias para armazenar os valores intermediários, como:
```
_t0 = c * d
_t1 = b + _t0
a = _t1
```
Cada vez que geramos um novo temporário `(_t0, _t1, _t2…)`, incrementamos esse contador para garantir nomes únicos.

- self.label_counter = 0

Inicializa o contador de rótulos (labels) com zero. Os rótulos são usados para controle de fluxo: saltos, loops, condicionais.
```
if cond goto L0
goto L1
L0:
   ...
L1:
```
O label_counter garante que cada `L0, L1, L2`, etc., seja único para evitar colisões.

- self.instrucoes = [ ]

Cria uma lista vazia que armazenará todas as instruções TAC geradas durante a visita à árvore de sintaxe. Ele aramzena Instâncias de TAC_Instruction, como:
```
TAC_Instruction('+', dest=_t1, arg1='a', arg2='b')
TAC_Instruction('label', dest='L0')
TAC_Instruction('goto', dest='L1')
```
**Ao final, essa lista pode ser impressa ou salva em arquivo .tac com todas as instruções intermediárias do programa analisado.**

----
**2. def novo_temp(self):**

Este método é responsável por gerar uma nova variável temporária toda vez que uma expressão intermediária precisa ser avaliada. Esse método é essencial para gerar variáveis intermediárias únicas, permitindo a decomposição de expressões complexas em passos simples, legíveis e compatíveis com linguagens de máquina ou Assembly. Ele encapsula uma abstração poderosa da lógica de armazenamento temporário que um compilador precisa para gerar código intermediário correto.
```
def novo_temp(self):
        nome = f"_t{self.temp_counter}"
        self.temp_counter += 1
        return TAC_Operand("temp", nome)
```
- nome = f"_t{self.temp_counter}"

Cria uma string com nome exclusivo para a variável temporária, usando o contador `self.temp_counter`. Se `self.temp_counter == 0`, o nome gerado será "`_t0`". Esse método é necessaário durante a tradução de expressões compostas, como: `a = b + c * d;` onde você precisa armazenar os resultados intermediários:
```
_t0 = c * d
_t1 = b + _t0
a = _t1
```
Essas variáveis _t0, _t1 são criadas automaticamente, e cada chamada a novo_temp() cuida disso.
- self.temp_counter += 1

Incrementa o contador para garantir que a próxima variável gerada tenha um nome único.
Exemplo de sequência:
- Primeira chamada: retorna _t0
- Segunda chamada: retorna _t1
- Terceira chamada: _t2 ...
Essa lógica evita colisão de nomes e mantém a estrutura do código intermediário clara e organizada.

- return TAC_Operand("temp", nome)

Retorna um objeto da classe TAC_Operand com:
- tipo="temp" → indicando que é uma variável temporária
- valor="_tX" → o nome gerado
 Isso padroniza o uso de operandos dentro da geração TAC. Esse TAC_Operand será usado, por exemplo, como dest ou arg1/arg2 em instruções TAC_Instruction.
 ```
Exemplo de retorno:
TAC_Operand("temp", "_t3")
```

---
**3. def nova_label(self):**

O método nova_label() é responsável por gerar rótulos (labels) únicos que são usados no código intermediário TAC para controlar o fluxo de execução, como em estruturas de decisão (se, senao) e repetição (enquanto, para).
Esses rótulos funcionam como marcadores de posição no código, representando pontos de salto (jump) para goto, if, if_false, etc.
```
def nova_label(self):
        nome = f"L{self.label_counter}"
        self.label_counter += 1
        return TAC_Operand("label", nome)
```
- nome = f"L{self.label_counter}"

Cria um nome exclusivo para um rótulo, concatenando a letra “L” com o valor atual do contador de rótulos `self.label_counter`, Se `label_counter == 0 → nome = "L0"`, se `label_counter == 1 → nome = "L1"` e assim por diante.
Esses nomes serão usados como destinos de saltos no TAC, como em:
```
ifFalse _t0 goto L1
goto L2
L1:
```
- self.label_counter += 1

Incrementa o contador de rótulos para garantir que o próximo rótulo gerado tenha um nome diferente, evitando assim, que dois goto apontem para o mesmo label por engano, o que poderia quebrar a lógica de controle de fluxo.

- return TAC_Operand("label", nome)

Retorna um objeto do tipo TAC_Operand, com:
- tipo = "label" → identifica que é um rótulo (e não uma variável, constante, etc.)
- valor = "L0", "L1", ... → o nome gerado
```
TAC_Instruction("label", dest=label)
TAC_Instruction("goto", dest=label)
TAC_Instruction("if_false", dest=label, arg1=condicao)
```
---
**4. def add_instrucao(self, instrucao):**

O método add_instrucao() é responsável por registrar uma instrução TAC (Three Address Code) na lista principal que está sendo construída durante a geração de código intermediário.
Em outras palavras, toda vez que uma nova instrução TAC é criada (por exemplo, uma operação aritmética, uma atribuição, um salto), ela é adicionada ao final da lista `self.instrucoes` usando este método,ou seja, é uma lista de objetos da classe TAC_Instruction que representa o corpo do código intermediário gerado. Cada item dessa lista será convertido em uma linha do arquivo .tac final.

O método add_instrucao() é o coração do gerador TAC. Ele funciona como uma “impressora” de instruções internas, acumulando tudo que deve ser transformado no código intermediário final. Sua simplicidade esconde sua importância: sem ele, nada seria registrado!
```
    def add_instrucao(self, instrucao):
        self.instrucoes.append(instrucao)
```
- self.instrucoes.append(instrucao)
Adiciona uma nova instrução TAC à lista principal de instruções, seu tipo de argumento esperado é o `TAC_Instruction`, ou seja, o método espera receber um objeto construído assim:
```
temp = self.novo_temp()  # cria _t0
self.add_instrucao(TAC_Instruction("+", temp, "5", "3"))
self.add_instrucao(TAC_Instruction("=", "a", temp))
```
A lista self.instrucoes conterá:
```
[
  TAC_Instruction("+", _t0, 5, 3),
  TAC_Instruction("=", a, _t0)
]
```
Este método é chamado indiretamente por praticamente todos os visit... da classe TACGenerator:
| Método Visitante            | Exemplo de instrução adicionada via `add_instrucao()` |
|-----------------------------|--------------------------------------------------------|
| `visitExpressao()`          | `_t1 = a + b`                                          |
| `visitComando_atribuicao()` | `x = _t1`                                              |
| `visitComando_para()`       | `goto L0`                                              |
| `visitComando_retorno()`    | `return x`                                             |
| `visitComando_ler()`        | `x = call leia()`                                      |

---

**5. def salvar_em_arquivo(self, nome_arquivo):**

O método salvar_em_arquivo() tem como função persistir no disco todo o código intermediário TAC gerado, escrevendo cada instrução da lista self.instrucoes em um arquivo de texto .tac. Esse método transforma a representação interna (em objetos TAC_Instruction) em um formato textual legível, que representa o programa intermediário pronto para ser lido, interpretado ou transformado para etapas posteriores, como geração de código final (assembly, bytecode, etc.).

Ao final da visita à árvore de sintaxe, todos os métodos visit...() terão adicionado suas instruções na lista self.instrucoes. É nessa hora que você chama salvar_em_arquivo() para transformar isso em um arquivo .tac.

O método salvar_em_arquivo() é o último passo da geração de código intermediário — ele pega o resultado de toda a análise sintática, semântica e da geração de TAC, e o transforma em um arquivo físico.

Sem ele, o que foi feito existiria apenas na memória — seria invisível para o mundo exterior.
```
def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "w") as f:
            for instr in self.instrucoes:
                f.write(str(instr) + "\n")
```
---
**6. def visitInicio(self, ctx):**

O método visitInicio inicia a visita na raiz da árvore sintática abstrata (AST) gerada pelo ANTLR a partir do código-fonte analisado. Ele serve como ponto de partida para percorrer e traduzir cada comando do programa para instruções TAC.
```
 def visitInicio(self, ctx):
        self.visitChildren(ctx)
        return None
```
Esse método corresponde à regra inicio da sua gramática ANTLR:
```
inicio
    : comandos+
    ;
```
Ou seja, o nó inicio contém uma lista de comandos que compõem o programa-fonte. Logo, `visitInicio()` deve chamar os visitadores apropriados para todos esses comandos — e isso é feito via `self.visitChildren(ctx)`.
- self.visitChildren(ctx)
Chama automaticamente o método `visitXXX()` correspondente para cada filho de ctx. Como ctx é um InicioContext, seus filhos são ComandosContext (cada comando no programa).
Exemplo:
```
int main() {
    int x = 10;
    escreva(x);
    retorna x;
}
```
Fluxo executado por `visitInicio()`:
1.	visitInicio() → encontra três comandos:
- declaração de variável int x = 10
- comando escreva(x)
- comando retorna x
2.	Ele chama:
- visitComando_declaracao(...)
- visitComando_escrever(...)
- visitComando_retorno(...)
É uma chamada recursiva em profundidade que processa o programa de cima para baixo.

O método `v`sitInicio()` é como apertar o botão “executar”: ele ativa toda a visitação que transforma a estrutura da AST em um conjunto de instruções TAC. Seu papel é fundamental, mesmo parecendo simples — ele garante que nada no programa ficará sem ser traduzido.

---
**7. def visitComando_declaracao(self, ctx):**

Esse método é responsável por processar uma declaração de variável na linguagem de alto nível e gerar o código intermediário (TAC) correspondente.
```
def visitComando_declaracao(self, ctx):
        nome = ctx.ID().getText()
        expressao_ctx = ctx.expressao()
        
        if expressao_ctx:
            valor = self.visit(expressao_ctx)
            self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
        
        return None
```
Esse método corresponde à regra de declaração da sua gramática ANTLR:
```
comando_declaracao
    : TIPO_INT ID (RECEBE expressao)? FINAL
    | TIPO_STRING ID (RECEBE expressao)? FINAL
```
Ou seja, a linguagem permite:
1. Declarações sem valor inicial: int x;
2. Declarações com inicialização: int x = 10;

- nome = ctx.ID().getText()

É responsável por extrair o nome da variável declarada (x, total, numero, etc.).
`ctx.ID()` acessa o token do identificador e `.getText()` retorna o texto bruto — ex: "total".

- expressao_ctx = ctx.expressao()

Verifica se há uma expressão presente após o sinal =.
Se for `int x = 2 + 3;` então `ctx.expressao()` é a subárvore da expressão 2 + 3.

- ```if expressao_ctx:
    valor = self.visit(expressao_ctx)
    self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
  ```

  	1.	self.visit(expressao_ctx):
  Processa a expressão recursivamente gerando TAC para calcular a expressão `(ex: 2 + 3 → _t0)` e retorna o resultado `(ex: _t0)`.
	3.	TAC_Instruction("=", ...):
	•	Cria uma instrução de atribuição no estilo: `x = _t0`
Aqui, `TAC_Operand("var", nome)` representa o destino da atribuição (x), e valor é o resultado da expressão.

- return None

O método não precisa retornar nada; sua única função é gerar código.

**3. def nova_label(self):**
Cria um novo rótulo para controle de fluxo:
```
```
**3. def nova_label(self):**
Cria um novo rótulo para controle de fluxo:
```
```
**3. def nova_label(self):**
Cria um novo rótulo para controle de fluxo:
```
```
**3. def nova_label(self):**
Cria um novo rótulo para controle de fluxo:
```
```
**3. def nova_label(self):**
Cria um novo rótulo para controle de fluxo:
```
```
**3. def nova_label(self):**
Cria um novo rótulo para controle de fluxo:
```
```








