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

O TAC (Código de Três Endereços) é um tipo de linguagem intermediária usada durante a compilação. Ele fica entre o código-fonte escrito pelo programador (como C ou Python) e o código de máquina final (executado pelo processador).

Cada linha (ou instrução) em TAC é bem simples: ela faz apenas uma operação por vez (como uma soma, comparação ou atribuição) e usa, no máximo, três valores:
- Dois valores de entrada (ex: a e b)
- Um local onde o resultado será guardado (ex: _t1)

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
Veja como ele quebra a expressão complexa em operações simples, que usam **três “endereços” por vez:**
- Dois operandos de entrada (como b e c)
- Um operando de saída (como _t1)

O TAC serve como uma forma intermediária e simplificada de representar o que o programa faz, dividindo tudo em pequenas operações que usam no máximo três partes: dois dados de entrada e um local para guardar o resultado.

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

O método `visitInicio()` é como apertar o botão “executar”: ele ativa toda a visitação que transforma a estrutura da AST em um conjunto de instruções TAC. Seu papel é fundamental, mesmo parecendo simples — ele garante que nada no programa ficará sem ser traduzido.

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

- Linhas 4, 5 e 6: 
```
if expressao_ctx:
	valor = self.visit(expressao_ctx)
	self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
```

1. valor = self.visit(expressao_ctx)

Processa a expressão recursivamente gerando TAC para calcular a expressão `(ex: 2 + 3 → _t0)` e retorna o resultado `(ex: _t0)`.

2. self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))

Cria uma instrução de atribuição no estilo: `x = _t0`
Aqui, `TAC_Operand("var", nome)` representa o destino da atribuição (x), e valor é o resultado da expressão.

- return None

O método não precisa retornar nada; sua única função é gerar código.

```
CODIGO FONTE:
int f;
int a = 2+2;
int b = 2;

TAC GERADO:
_t0 = 2 + 2
a = _t0
b = 2

```


O visitComando_declaracao() é essencial para capturar corretamente a criação de variáveis e suas inicializações no programa. Ele mostra como a semântica de uma linguagem de alto nível é traduzida para TAC, de forma estruturada, clara e modular.

---
**8. visitComando_atribuicao(self, ctx):**

Esse método é chamado quando o analisador encontra uma atribuição no código-fonte, como: `x = 5 + 3;` e seu papel é traduzir essa atribuição para uma ou mais instruções TAC, gerando os temporários intermediários e atribuindo corretamente o resultado.
```
 def visitComando_atribuicao(self, ctx):
        nome = ctx.atribuicao().ID().getText()
        valor = self.visit(ctx.atribuicao().expressao())
        self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
        return None
```
Esse método corresponde à regra de declaração da sua gramática ANTLR:
```
comando_atribuicao
    : atribuicao FINAL
    ;

atribuicao
    : ID RECEBE expressao
    ;	
```
- nome = ctx.atribuicao().ID().getText()

Acessa o identificador da variável do lado esquerdo da atribuição. `ctx.atribuicao()` acessa a sub-regra atribuicao dentro da classe `CompiladorGVParser(Parser):`, já o `.ID().getText()` retorna o nome da variável como string — por exemplo: "x".

- valor = self.visit(ctx.atribuicao().expressao())

Visita recursivamente a expressão do lado direito da atribuição:
```
x = 5 + 3;  →  expressao = 5 + 3
```
Isso pode gerar uma ou mais instruções TAC como: `_t0 = 5 + 3`, o valor retornado (_t0, 5, etc.) será usado como fonte da atribuição.

- self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))

Gera a instrução de atribuição no formato TAC: `x = _t0`

- return None

O método não retorna nada; sua função é exclusivamente gerar as instruções TAC e armazená-las na lista self.instrucoes.

Exemplo de funcionamento:
```
Código-fonte: total = a + b * 2;

TAC gerado:
_t0 = b * 2
_t1 = a + _t0
total = _t1
```
As duas primeiras instruções são geradas pelo `visitExpressao()`; a terceira é gerada aqui, em `visitComando_atribuicao()`.

- Comparação com visitComando_declaracao()

| Aspecto                | Declaração (`int x = ...`)          | Atribuição (`x = ...`)              |
|------------------------|-------------------------------------|-------------------------------------|
| Nome do método         | `visitComando_declaracao()`         | `visitComando_atribuicao()`         |
| Cria variável?         | Sim (implícito)                     | Não — apenas usa uma já existente   |
| Gera instrução `x = ...`? | Sim (caso com valor inicial)     | Sim                                 |
| Pode não gerar TAC?    | Sim (se for só `int x;`)            | Não — sempre gera `x = ...`         |

---
**9.  def visitExpressao(self, ctx):**
Cria um novo rótulo para controle de fluxo:
```
```
# tem um erro
**10.  def visitCondicao(self, ctx):**

O visitCondicao() serve para avaliar expressões condicionais que retornam verdadeiro ou falso, gerar os temporários e instruções TAC correspondentes e preparar essas expressões para uso em estruturas de controle, como se, enquanto, para, etc. Esse método é chamado sempre que uma condição lógica ou relacional aparece no código, como: `a > b
(a + b > c) && (d != e)`
```
def visitCondicao(self, ctx):
        filhos = ctx.getChildCount()
        texto = ctx.getText()
        print(f"\033[91m[DEBUG] CONDICAO: {texto} ({filhos} filhos)\033[0m")

        if filhos == 3:
            esq = ctx.getChild(0)
            op = ctx.getChild(1).getText()
            dir = ctx.getChild(2)

            # Recursivamente visita condicoes
            if hasattr(esq, 'condicao') or isinstance(esq, type(ctx)):
                arg1 = self.visit(esq)
            else:
                arg1 = self.visit(esq)

            if hasattr(dir, 'condicao') or isinstance(dir, type(ctx)):
                arg2 = self.visit(dir)
            else:
                arg2 = self.visit(dir)

            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
            print(f"\033[92m[DEBUG] CONDICAO BINARIA: {arg1} {op} {arg2} → {temp}\033[0m")
            return temp

        elif filhos == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        else:
            print("\033[91m[ERRO] Condição inválida ou não suportada ainda\033[0m")
            return None
```
Esse método corresponde à regra de declaração da sua gramática ANTLR:
```
condicao
    : expressao operador expressao
    | condicao AND condicao
    | condicao OR condicao
    | ABRE_PAR condicao FECHA_PAR
    ;
```
- Cabeçalho (primeiras 3 linhas)
```
filhos = ctx.getChildCount()
texto = ctx.getText()
print(f"\033[91m[DEBUG] CONDICAO: {texto} ({filhos} filhos)\033[0m")
```
essa etapa extrai os filhos: número de elementos na árvore sintática, o texto: representação textual da condição e exibe no terminal o que está sendo processado, útil para depuração.
-  Caso 1: Condição binária simples (ex: a < b)
```
if filhos == 3:
    esq = ctx.getChild(0)
    op = ctx.getChild(1).getText()
    dir = ctx.getChild(2)
```
Identifica o padrão: algo operador algo `a < b`
- Visita recursiva dos operandos (ainda dentro do caso 1)
```
if hasattr(esq, 'condicao') or isinstance(esq, type(ctx)):
    arg1 = self.visit(esq)
else:
    arg1 = self.visit(esq)

if hasattr(dir, 'condicao') or isinstance(dir, type(ctx)):
    arg2 = self.visit(dir)
else:
    arg2 = self.visit(dir)
```
A lógica acima garante que tanto os operandos simples quanto os compostos (aninhados) sejam processados corretamente.
-  Geração da instrução TAC
```
temp = self.novo_temp()
self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
print(f"\033[92m[DEBUG] CONDICAO BINARIA: {arg1} {op} {arg2} → {temp}\033[0m")
return temp
```
Gera uma instrução TAC correspondente: `_t0 = a < b` ou `_t1 = _t0 && _t2`
Retorna o temporário resultante para ser usado em instruções if, if_false, etc.

- Caso 2: Condição entre parênteses
Realiza a visita ao conteúdo entre os parênteses, ignorando ( e ).
```
elif filhos == 3 and ctx.getChild(0).getText() == '(':
    return self.visit(ctx.getChild(1))
```
---

**11. def visitComando_se(self, ctx):**

Esse método é responsável por avaliar a condição do comando `se`, gerar labels para os ramos do `then`, `else` e para o fim do bloco condicional, produzir as instruções de desvio condicional e incondicional no TAC, Visitar e traduzir os blocos `then` e `else`, se existirem, e marcar o ponto de continuação da execução após o `se`.
```
def visitComando_se(self, ctx):
        print("\033[96m[DEBUG] INICIANDO 'se'\033[0m")
        cond_resultado = self.visit(ctx.condicao())  # _t0

        label_then = self.nova_label()
        label_else = self.nova_label()
        label_end = self.nova_label()

        print(f"\033[96m[DEBUG] Labels: THEN={label_then}, ELSE={label_else}, END={label_end}\033[0m")

        self.add_instrucao(TAC_Instruction("if_goto", dest=label_then, arg1=cond_resultado))
        self.add_instrucao(TAC_Instruction("goto", dest=label_else))

        self.add_instrucao(TAC_Instruction("label", dest=label_then))
        print("\033[96m[DEBUG] Visitando bloco THEN\033[0m")
        for comando in ctx.bloco(0).comandos():
            self.visit(comando)
        self.add_instrucao(TAC_Instruction("goto", dest=label_end))

        self.add_instrucao(TAC_Instruction("label", dest=label_else))
        if ctx.SENAO():
            print("\033[96m[DEBUG] Visitando bloco ELSE\033[0m")
            for comando in ctx.bloco(1).comandos():
                self.visit(comando)

        self.add_instrucao(TAC_Instruction("label", dest=label_end))
        print("\033[96m[DEBUG] Finalizando 'se'\033[0m")
```
- print("\033[96m[DEBUG] INICIANDO 'se'\033[0m")

Imprime uma mensagem de depuração informando que o bloco se começou a ser processado. Útil para rastrear a geração do código.

- cond_resultado = self.visit(ctx.condicao())  # _t0

O método visit(ctx.condicao()) gera TAC para a condição lógica e retorna um operand temporário, como _t0, que conterá 1 (true) ou 0 (false).
Exemplo: `se (a > b)` pode gerar o TAC `_t0 = a > b`

-  Linhas 4–6: Geração de labels:
```
label_then = self.nova_label()
label_else = self.nova_label()
label_end = self.nova_label()
```
Esses labels representam:

| Label        | Significado                      |
|--------------|----------------------------------|
| `label_then` | Início do bloco `then`           |
| `label_else` | Início do bloco `else` (opcional)|
| `label_end`  | Continuação após o `se`          |

Eles são criados usando self.nova_label(), que gera L0, L1, etc.

- print(f"\033[96m[DEBUG] Labels: THEN={label_then}, ELSE={label_else}, END={label_end}\033[0m")

Debug do que foi feito, essa linha apenas exibe os labels gerados para facilitar o rastreamento.

- Linhas 9–10: Desvio condicional e incondicional
```
self.add_instrucao(TAC_Instruction("if_goto", dest=label_then, arg1=cond_resultado))
self.add_instrucao(TAC_Instruction("goto", dest=label_else))
```
Se a condição for verdadeira (if_goto), vá para o bloco then. Caso contrário, vá diretamente para else: `if _t0 goto L0`
`goto L1`

- Linhas 12–14: Marca e executa o bloco THEN
```
self.add_instrucao(TAC_Instruction("label", dest=label_then))
print("\033[96m[DEBUG] Visitando bloco THEN\033[0m")
for comando in ctx.bloco(0).comandos():
    self.visit(comando)
```
label_then é colocado no TAC.
Cada comando do bloco then é visitado e traduzido.

- self.add_instrucao(TAC_Instruction("goto", dest=label_end))
Evita que o código do else seja executado caso o then já tenha sido.

- Linhas 17–21: Verifica se há bloco ELSE
```
self.add_instrucao(TAC_Instruction("label", dest=label_else))
if ctx.SENAO():
    print("\033[96m[DEBUG] Visitando bloco ELSE\033[0m")
    for comando in ctx.bloco(1).comandos():
        self.visit(comando)
```
Marca o label do else.
1. 	Se SENAO estiver presente no código-fonte, o bloco else é traduzido normalmente.
2. 	Se não houver senao, apenas o label é gerado como destino do salto anterior.

- self.add_instrucao(TAC_Instruction("label", dest=label_end))

Marca o fim da estrutura se, indicando onde a execução deve continuar, sendo fundamental para aninhamento de condicionais.

- print("\033[96m[DEBUG] Finalizando 'se'\033[0m")
Mensagem de Degub que indica o fim do código.
```
COGIGO FONTE
int a = 3;
int b = 5;
se (a < b) {
  escreva("menor");
} senao {
  escreva("maior ou igual");
}

TAC GERADO
_t0 = a < b
if _t0 goto L0
goto L1
L0:
print "menor"
goto L2
L1:
print "maior ou igual"
L2:
```
---
**12. def visitComando_enquanto(self, ctx):**

Este método é responsável por cuidar da tradução da estrutura de repetição enquanto (equivalente ao while do C) para código intermediário TAC. Esse metodo Gera o fluxo de controle para laços enquanto, traduz a condição do laço em TAC, cria labels para marcar o início e o fim do loop e garante que o corpo do loop seja reavaliado enquanto a condição for verdadeira.
```
def visitComando_enquanto(self, ctx):
        print("\033[95m[DEBUG] INICIANDO 'enquanto'\033[0m")

        label_inicio = self.nova_label()
        label_fim = self.nova_label()

        print(f"\033[95m[DEBUG] Labels: INICIO={label_inicio}, FIM={label_fim}\033[0m")

        self.add_instrucao(TAC_Instruction("label", dest=label_inicio))

        cond_resultado = self.visit(ctx.condicao())
        print(f"\033[95m[DEBUG] CONDICAO: {cond_resultado}\033[0m")

        # Correção: if_false condicao goto FIM
        self.add_instrucao(TAC_Instruction("if_false", dest=label_fim, arg1=cond_resultado))

        print("\033[95m[DEBUG] Visitando bloco do 'enquanto'\033[0m")
        for comando in ctx.bloco().comandos():
            self.visit(comando)

        self.add_instrucao(TAC_Instruction("goto", dest=label_inicio))
        self.add_instrucao(TAC_Instruction("label", dest=label_fim))
        print("\033[95m[DEBUG] Finalizando 'enquanto'\033[0m")
```

- print("\033[95m[DEBUG] INICIANDO 'enquanto'\033[0m")

Mensagem de depuração para identificar o início da tradução do laço enquanto.

- Linhas 2 e 3: Geração dos labels de controle
```
label_inicio = self.nova_label()
label_fim = self.nova_label()
```
Dois labels são gerados: `label_inicio` que marca o ponto de reavaliação da condição e `label_fim` que marca o fim do laço. Esses labels são essenciais para manter o controle do fluxo durante a execução do loop.

- print(f"\033[95m[DEBUG] Labels: INICIO={label_inicio}, FIM={label_fim}\033[0m")

Mostra os nomes gerados dos labels para fins de depuração.

- self.add_instrucao(TAC_Instruction("label", dest=label_inicio))
Esse label será o ponto de retorno após cada iteração do laço.

- Linha 10 e 11: Geração da condição
```
cond_resultado = self.visit(ctx.condicao())
print(f"\033[95m[DEBUG] CONDICAO: {cond_resultado}\033[0m")
```
`self.visit(ctx.condicao())` avalia a condição do laço e gera o TAC correspondente. O resultado é um temporário (ex: _t0) com valor 1 (true) ou 0 (false).

- self.add_instrucao(TAC_Instruction("if_false", dest=label_fim, arg1=cond_resultado))
Aqui está o coração da lógica:
1. Se a condição for falsa, salta para label_fim, encerrando o laço.
2. Caso contrário, continua para o corpo do loop. O TAC gerado: `ifFalse _t0 goto L1`

- Linhas 16, 17 e 18: Tradução do corpo do laço
```
print("\033[95m[DEBUG] Visitando bloco do 'enquanto'\033[0m")
for comando in ctx.bloco().comandos():
    self.visit(comando)
```
Visita e traduz cada comando contido no corpo do enquanto e gera as instruções correspondentes ao que está dentro do laço.

- self.add_instrucao(TAC_Instruction("goto", dest=label_inicio))

Garante que, após executar o corpo, a condição será reavaliada. Esse é o comportamento esperado de um while: repetição com verificação antes.

- self.add_instrucao(TAC_Instruction("label", dest=label_fim))

Marca o ponto após o enquanto, ou seja, para onde o programa deve ir caso a condição não seja satisfeita.

- print("\033[95m[DEBUG] Finalizando 'enquanto'\033[0m")

Mensagem de depuração para identificar a finalização do laço enquanto.
Exemplo:
```
CODIGO FONTE
int i = 0;
enquanto(i < 5) {
    escreva(i);
    i = i + 1;
}

TAC GERADO
i = 0
L0:
_t0 = i < 5
ifFalse _t0 goto L1
print i
_t1 = i + 1
i = _t1
goto L0
L1:
```
---

**13.def visitComando_para(self, ctx):**

Esse método é responsável por traduzir o comando para (equivalente ao for em C) em código intermediário TAC.
```
def visitComando_para(self, ctx):
        self.visit(ctx.atribuicao())  # inicialização

        label_cond = self.nova_label()
        label_fim = self.nova_label()

        self.add_instrucao(TAC_Instruction("label", dest=label_cond))

        cond = self.visit(ctx.condicao())
        # Correção aqui
        self.add_instrucao(TAC_Instruction("if_false", dest=label_fim, arg1=cond))

        for comando in ctx.bloco().comandos():
            self.visit(comando)

        self.visit(ctx.incremento())
        self.add_instrucao(TAC_Instruction("goto", dest=label_cond))
        self.add_instrucao(TAC_Instruction("label", dest=label_fim))
```
O comando para em sua forma clássica:
```
para(inicialização; condição; incremento) {
    // corpo
}
```
é traduzido para o TAC usando:
1.	Inicialização → executada apenas uma vez;
2.	Condição → verificada antes de cada iteração;
3.	Incremento → executado ao fim de cada iteração;
4.	Bloco → corpo principal do loop.

- def visitComando_para(self, ctx):

Executa a inicialização (ex: i = 0). Isso acontece antes do loop começar.

- Linhas 3 e 4: Geração dos labels
```
label_cond = self.nova_label()
label_fim = self.nova_label()
```
A `label_cond` marca o ponto de verificação da condição e a `label_fim` marca o fim do laço.

- self.add_instrucao(TAC_Instruction("label", dest=label_cond))

O início da verificação de condição é marcado com label_cond.

- cond = self.visit(ctx.condicao())

Visita e avalia a condição do for, que deve resultar em um valor booleano (normalmente 1 ou 0), depois retorna um TAC_Operand contendo o temporário com o resultado que é atribuido a variável cond.

- self.add_instrucao(TAC_Instruction("if_false", dest=label_fim, arg1=cond))

Se a condição for falsa, salta para o final do laço (label_fim), do contrário, executa o corpo do laço.

- Linhas 12 e 13: Execução do corpo
```
for comando in ctx.bloco().comandos():
    self.visit(comando)
```
Visita e traduz cada comando do bloco do para. isso gera instruções TAC para o corpo do loop.

- self.visit(ctx.incremento())

Após o corpo, visita o incremento (ex: i = i + 1, i++, i--, etc). Executa esse trecho antes de voltar à verificação da condição.

- self.add_instrucao(TAC_Instruction("goto", dest=label_cond))

Faz o salto para reavaliar a condição, fechando o ciclo do loop.

- self.add_instrucao(TAC_Instruction("label", dest=label_fim))

Marca o local onde a execução continuará caso a condição seja falsa. Serve de ponto de escape do loop.
Exemplo:
```
CODIGO FONTE
para(i = 0; i < 3; i = i + 1) {
    escreva(i);
}

TAC GERADO
i = 0
L0:
_t0 = i < 3
ifFalse _t0 goto L1
print i
_t1 = i + 1
i = _t1
goto L0
L1:
```
Explicação do TAC gerado

| Parte | TAC gerado                  | Finalidade                            |
|-------|-----------------------------|----------------------------------------|
| 1     | `i = 0`                     | Inicializa a variável de controle      |
| 2     | `L0:`                       | Label para início do loop              |
| 3     | `_t0 = i < 3`               | Avalia a condição                      |
| 4     | `ifFalse _t0 goto L1`       | Sai do loop se condição for falsa      |
| 5     | `print i`                   | Executa o corpo                        |
| 6     | `_t1 = i + 1; i = _t1`      | Executa o incremento                   |
| 7     | `goto L0`                   | Volta para a reavaliação               |
| 8     | `L1:`                       | Ponto após o fim do loop               |

---

**14.def visitComando_retorno(self, ctx):**

visitComando_retorno

Este método é responsável por traduzir o comando retorna da linguagem de alto nível para uma instrução TAC do tipo return. Essa instrução é crucial para indicar o fim da execução de uma função e (opcionalmente) o valor que deve ser devolvido.

```
def visitComando_retorno(self, ctx):
        print(f"\033[92m[DEBUG] ENTRANDO EM visitComando_retorno\033[0m")

        valor = self.visit(ctx.expressao()) if ctx.expressao() else None

        if valor:
            self.add_instrucao(TAC_Instruction("return", arg1=valor))
            print(f"\033[92m[DEBUG] RETORNO: return {valor}\033[0m")
        else:
            self.add_instrucao(TAC_Instruction("return"))
            print("\033[91m[ERRO SEMÂNTICO] Retorno sem valor detectado!\033[0m")
```

- def visitComando_retorno(self, ctx):

Define o visitante para a regra comando_retorno da sua gramática (que deve corresponder a algo como retorna expressao;).

- print(f"\033[92m[DEBUG] ENTRANDO EM visitComando_retorno\033[0m")

Um DEBUG é exibido no terminal para acompanhamento da execução.

- valor = self.visit(ctx.expressao()) if ctx.expressao() else None

1. Verifica se há uma expressão presente no retorna (ex: retorna 10;, retorna a + b;)
2. Se houver, chama self.visit(ctx.expressao()) para avaliar a expressão e gerar TAC para ela.
3. O resultado disso será uma instância de TAC_Operand representando o valor a ser retornado.
4. Se não houver expressão (ex: retorna;), o valor será None.

- Linha 5, 6 e 7: Geração da instrução TAC
```
if valor:
    self.add_instrucao(TAC_Instruction("return", arg1=valor))
    print(f"\033[92m[DEBUG] RETORNO: return {valor}\033[0m")
```
Se valor não for None, significa que temos um retorno com valor. O TAC gerado será algo como: `return _t0`, onde _t0 representa o resultado da expressão avaliada. por fim, a instrução é adicionada à lista com: `self.add_instrucao(...)`

- Linhas 8, 9 e 10: Retorno sem valor
```
else:
    self.add_instrucao(TAC_Instruction("return"))
    print("\033[91m[ERRO SEMÂNTICO] Retorno sem valor detectado!\033[0m")
```
Se não houver expressão (ctx.expressao() == None), adiciona a instrução TAC: `return`
Emite um alerta de erro semântico porque em linguagens fortemente tipadas, toda função com tipo de retorno definido deve retornar um valor.
```
EXEMPLO DE ERRO:
int soma(int a, int b) {
    retorna;
}
```
Isso pode causar problemas na etapa de geração de código final ou execução.
Exemplo de uso:
```
CODIGO FONTE:
int soma(int a, int b) {
    int r = a + b;
    retorna r;
}

TAC GERADO
_t0 = a + b
r = _t0
return r
```

- Papel da instrução return no TAC

A instrução return tem papel fundamental pois, indica o ponto de saída da função, permite retornar um valor para quem chamou a função (ex: soma(2,3)) e é uma das formas de controle de fluxo do TAC, como goto, if_goto, etc.







